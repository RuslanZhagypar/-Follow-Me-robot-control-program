
import csv  # a library to read csv files
from statistics import mean # a library to find the mean value
#from moviepy.editor import VideoFileClip
fields = [] # To store the headings of each column in a .csv file;
rows = []	# to store all the rows of a file
xarr = []	# to store x coordinate of each point
yarr = []	# to store y coordinate of each point
carr = []	# to store confidence index of each point

#clip = VideoFileClip("Gesture_Control.mp4")
length_of_video = 26 # the length of the video

filename = "Gesture_Control.csv"
with open(filename, 'r') as csvfile: 
	csvVar = csv.reader(csvfile)	# creating a csv reader object 
	fields = next(csvVar)
	for row in csvVar: 			# extracting each data row one by one 
		rows.append(row) 
  
    # get total number of rows 
	print("Total no. of rows: %d"%(csvVar.line_num)) 

sec_per_frame = length_of_video / (csvVar.line_num-1)# calculating sec/frame for determining the total time for each pose 

prev_state		=0 		# the value of 0 means no pose;

Left_Up_count	=0		# to count the occurence of HAPPY pose
Right_Up_count	=0		# to count the occurence of SURPRISE pose
Both_Up_count	=0		# to count the occurence of SAD pose


total_Left_Up	=0		# total number of frames will be recorder independently of previous state;
total_Right_Up	=0
total_Both_Up	=0

	
dur_Left_Up		=0		# durations for each emotion represent the number of successive frames/rows showing the same emotion;
dur_Right_Up	=0
dur_Both_Up		=0

Left_Up_Timing = []
Right_Up_Timing = []
Both_Up_Timing = []



DURATION=6			# the emotion will get recognized only if DURATION number of successive frames show the same emotion;
rowCount=0
for row in rows[:csvVar.line_num]: # A loop to iterate through all the rows/frames
	rowCount=rowCount+1
	col_count = 0		# simple int counter for column indexing					
	for col in row: 				# A loop to iterate through all columns in a row / frame;
		if 'x' in fields[col_count]:	# if the corresponding column number represents x coordinates, the value at this row and column will get parsed in "xarr" list ;
			xarr.append(col)  		
		if 'y' in fields[col_count]:	# if the corresponding column number represents y coordinates, the value at this row and column will get parsed in "yarr" list ;
			yarr.append(col)  
		if 'c' in fields[col_count]:	# if the corresponding column number represents index of confidence, the value at this row and column will get parsed in "carr" list ;
			carr.append(col)  	
		col_count = col_count+1

	carr_int = [float(i) for i in carr] # converting all string values in the carr list into float numbers
	th = mean(carr_int)					# for calculating the mean value of confidence;

	#Condition for Left_Up pose
	if ((yarr[4]>yarr[0] and yarr[7]<yarr[0]) and carr[4]>str(th) and carr[7]>str(th) and carr[0]>str(th)): # the conditions will be satisfied only if the confidences are higher than the mean
		if dur_Left_Up ==DURATION: #count until DURATION number of rows/frames show Left_Up pose															   					 				
			if prev_state==1:	 # checks if the previous state was Left_Up state (prev_state = 1)
				total_Left_Up=total_Left_Up+1	# if the previous state was Left_Up, there is no need to count it as new pose, just add to total happy time;
			else:							
				Left_Up_count= Left_Up_count+1	# if the previous state was NOT Left_Up, then increment the Left_Up counter
				total_Left_Up=total_Left_Up+6	# and add it to total Left_Up time;
				Left_Up_Timing.append(rowCount)	# at what frame Left_Up occured is written here
				prev_state=1				# now update the previous state to Left_Up;
		else:
			dur_Left_Up=dur_Left_Up+1			# Increment until the dur_Left_Up reaches the DURATION;

	else:									# If a row does not show Left_Up,
		dur_Left_Up=0							# then the duration counter of successive Left_Up frames is interupted; so, set it back to zero;
		#Condition for Right_Up pose
		if ((yarr[4]<yarr[0] and yarr[7]>yarr[0]) and carr[4]>str(th) and carr[7]>str(th) and carr[0]>str(th)): 
			if dur_Right_Up==DURATION:
				if prev_state==2:
					total_Right_Up=total_Right_Up+1
				else:
					Right_Up_count=Right_Up_count+1
					total_Right_Up=total_Right_Up+6
					Right_Up_Timing.append(rowCount)
					prev_state=2
			else:
				dur_Right_Up=dur_Right_Up+1
		else:
			dur_Right_Up=0
			#Condition for Both hand up
			if ((yarr[4]<yarr[0] and yarr[7]<yarr[0]) and carr[4]>str(th) and carr[7]>str(th) and carr[0]>str(th)): # the conditions will be satisfied only if the confidences are higher than the mean
				if dur_Both_Up==DURATION:
					if prev_state==3:
						total_Both_Up=total_Both_Up+1
					else:
						Both_Up_count=Both_Up_count+1
						total_Both_Up=total_Both_Up+1
						Both_Up_Timing.append(rowCount)
						prev_state=3
				else:
					dur_Both_Up=dur_Both_Up+1;
			else:
				dur_Both_Up=0
				prev_state=0	# if no condition was satisfied (i.e. no pose [was detected), then previous state remains as zero (no state)


	xarr.clear()	# the lists containing x, y and confidence values are cleared after each row/frame
	yarr.clear()
	carr.clear()

print("Total number of Left_Up moments: ",Left_Up_count,' \n')
print("Time the user was in the Left_Up state: ",round(total_Left_Up*sec_per_frame,2),'sec \n')
print("Total number of Right_Up moments: ",Right_Up_count,' \n')
print("Time the user was in the Right_Up state: ",round(total_Right_Up*sec_per_frame,2),'sec \n')
print("Total number of Both_Up moments: ",Both_Up_count,' \n')
print("Time the user was in the Both_Up state: ",round(total_Both_Up*sec_per_frame,2),'sec \n')

with open('GestureInfo.csv', mode='w') as GestureInfo:#writing into the 'GestureInfo.csv' file
    employee_writer = csv.writer(GestureInfo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(Left_Up_Timing)	#first row is for left hand
    employee_writer.writerow(Right_Up_Timing)	#second row is for right hand
    employee_writer.writerow(Both_Up_Timing)	#third row is for both hands