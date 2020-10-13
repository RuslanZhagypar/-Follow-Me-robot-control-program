import csv
from naoqi import ALProxy
import time

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.28])
keys.append([[-0.381946, [3, -0.106667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.28])
keys.append([[0.0184078, [3, -0.106667, 0], [3, 0, 0]]])

names.append("HipPitch")
times.append([0.28])
keys.append([[-0.11528, [3, -0.106667, 0], [3, 0, 0]]])

names.append("HipRoll")
times.append([0.28])
keys.append([[-0.0277314, [3, -0.106667, 0], [3, 0, 0]]])

names.append("KneePitch")
times.append([0.28])
keys.append([[0.000485729, [3, -0.106667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.28])
keys.append([[-0.120359, [3, -0.106667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.28, 2.28, 3.28, 4.24, 5.16])
keys.append([[-1.18469, [3, -0.106667, 0], [3, 0.666667, 0]], [-1.19555, [3, -0.666667, 0], [3, 0.333333, 0]], [-1.19555, [3, -0.333333, 0], [3, 0.32, 0]], [-1.19555, [3, -0.32, 0], [3, 0.306667, 0]], [-1.19555, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.28])
keys.append([[0.296193, [3, -0.106667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.28, 0.52, 1.08, 1.76, 2.28, 3.28, 4.24, 5.16, 5.36])
keys.append([[1.64436, [3, -0.106667, 0], [3, 0.08, 0]], [-1.46608, [3, -0.08, 0], [3, 0.186667, 0]], [-1.46608, [3, -0.186667, 0], [3, 0.226667, 0]], [-1.46608, [3, -0.226667, 0], [3, 0.173333, 0]], [-1.46608, [3, -0.173333, 0], [3, 0.333333, 0]], [-1.46608, [3, -0.333333, 0], [3, 0.32, 0]], [-1.46608, [3, -0.32, 0], [3, 0.306667, 0]], [-1.46608, [3, -0.306667, 0], [3, 0.0666667, 0]], [1.6633, [3, -0.0666667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.28, 2.28, 2.76, 3.28, 3.76, 4.24, 4.68, 5.16, 5.36])
keys.append([[0.0937356, [3, -0.106667, 0], [3, 0.666667, 0]], [0.555015, [3, -0.666667, 0], [3, 0.16, 0]], [0.0401426, [3, -0.16, 0], [3, 0.173333, 0]], [0.555015, [3, -0.173333, 0], [3, 0.16, 0]], [0.0401426, [3, -0.16, 0], [3, 0.16, 0]], [0.555015, [3, -0.16, 0], [3, 0.146667, 0]], [0.0401426, [3, -0.146667, 0], [3, 0.16, 0]], [0.555015, [3, -0.16, 0], [3, 0.0666667, 0]], [0.00872665, [3, -0.0666667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.28, 1.08])
keys.append([[-0.0320939, [3, -0.106667, 0], [3, 0.266667, 0]], [1.12748, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.28])
keys.append([[0.182689, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.28])
keys.append([[1.13437, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.28])
keys.append([[0.18253, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.28])
keys.append([[1.64293, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.28])
keys.append([[-0.138501, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.28])
keys.append([[0.199593, [3, -0.106667, 0], [3, 0, 0]]])



try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
   motion = ALProxy("ALMotion", "127.0.0.1", 9559)          #defining a motionProxy object
   textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)  #defining TTS object
   motion.angleInterpolationBezier(names, times, keys)        #Fetch the animation from joints 
   textSpeakProxy.say('Hi, human! I want to come with you')     
except BaseException, err:
  print err


handName = 'LElbowYaw'
useSen=0
print('INITIAL: ',motion.getAngles(handName, useSen))

y_past = 0.249              #initial value for 'LElbowYaw' when the arm is in down position in rad
motion.setBreathEnabled("Body",True)  #enable automatic motions of the robot 
time.sleep(2.0)
motion.setBreathEnabled("Body",False) #disable automatic motions of the robot, i.e. when no user command is sent to the robot, it does not move.
motion.setAngles(handName,0.249,0.5)  #set an initial position to the left hand 
time.sleep(3.0)
#------------------------------Code for working with PoseEstimation--------------------------------------
rows = [] # to store all the rows of a file
filename = "GestureInfo.csv"
with open(filename, 'r') as csvfile: 
  csvVar = csv.reader(csvfile)  # creating a csv reader object 
  for row in csvVar:      # extracting each data row one by one 
    rows.append(row) 

min_list =[]  #list to store three minimum values at a time
sequence = [] #list that stores the action sequences 
#print(rows)
j=0
p=0
SequenceLength = len(rows[0])+len(rows[1])+len(rows[2]) #the length of the sequence from the .csv file
rows[0] = [int(i) for i in rows[0]] 
rows[1] = [int(i) for i in rows[1]] 
rows[2] = [int(i) for i in rows[2]] 
while(j<SequenceLength):  #iterate thorugh all elements (actions) in the .csv file
  if(len(rows[0])!=0):  #check if the row is not empty
    min_list.append(min(rows[0]))  #find the minimum value in the row and store it to 'min_list'
  if(len(rows[1])!=0):
    min_list.append(min(rows[1]))
  if(len(rows[2])!=0):
    min_list.append(min(rows[2]))

  min_element = min(min_list) # find the least minimum value in 'min_list'
  while (True):
    try:
      rows[p].index(int(min_element))  #check if the minimum value is in one of the rows, if it is in one of them, take its index
      break                                 # index 0->left hand, 1-> right hand, 2-> both hands
    except:
      if (p==2):
        p=0
      else:
        p=p+1
      #print('Exception') 

  sequence.append(p)
  rows[p].remove(int(min_element))
  min_list[:] = []    #clear the list
  j=j+1     # move to find another element to the sequence
sequence.append(3)  # append value 3, which refers to NO action
print('sequence: ',sequence)
#----------------------------------------------------------------------------
i=0   # to iterate through elements in 'sequence'
while(1):
#----------------------Manual Turning---------------------------------------------------------------------
  y = motion.getAngles(handName, useSen)    #read the angle of the 'LElbowYaw'
  time.sleep(1.0)
  #print('y[0]',y[0])
  #print('y_past',y_past)
  if(y[0]-y_past > 0.18): #0.18rad=10deg angle resolution, i.e. robot turns CLOCKWISE only if the new angle is different from prev. for 10deg
    print('Turn Left manually')
    y_temp = motion.getAngles(handName, useSen) #Save the elbow's turned angle in 'y_temp' variable
    motion.moveTo(0,0,abs(y[0]))        #Turning the robot by the same angle the elbow is turned (y[0])
    time.sleep(2.0)
    motion.setAngles(handName,y_temp[0],0.5)  #Return the elbow once to the turned position to 'y_temp' 
    time.sleep(2.0)
    y = motion.getAngles(handName, useSen)    #get the elbow angle
    y_past = y[0]               #set the y_past to the recent elbow angle
  elif(y[0]-y_past < -0.18): #0.18rad=10deg angle resolution, i.e. robot turns COUNTER-CLOCKWISE only if the new angle is different from prev. for 10deg
    print('Turn Right manually')
    y_temp = motion.getAngles(handName, useSen)
    motion.moveTo(0,0,-abs(y[0]))
    time.sleep(2.0)
    motion.setAngles(handName,y_temp[0],0.5)
    time.sleep(2.0)
    y = motion.getAngles(handName, useSen)
    y_past = y[0]
  else:         # if there is no significant change in the elbow angle, then robot does not turn 
    y_past = y[0]   
 
#-------------------------Moving Forward Manually--------------------------------------------------------------------
  x = motion.getAngles("LShoulderPitch", 0) #Save the angle of 'LShoulderPitch' to variable x  
  if (x[0]>-1.392 and x[0]<0.435):          # if the saved angle is in between [-80deg ~ 25deg], then the robot moves
    Xvel_percentage = x[0]*(-0.8/1.827) + 0.39047 # a linear equation for calculating the velocity percentage from shoulder angle values
    motion.moveToward(Xvel_percentage, 0.0, 0.0)  #move forward with 'Xvel_percentage'
    time.sleep(1.0)
    print "Moving Speed X :",motion.getRobotVelocity()[0]," m/s"
  elif (x[0]<-1.392):                 # if the shoulder angle is higher than -80deg then the robot moves with max speed
    motion.moveToward(1.0, 0.0, 0.0)
    time.sleep(4.0)
    print "Moving Speed X :",motion.getRobotVelocity()[0]," m/s"
  else:
    motion.stopMove() 
#------------------------Reading the gesture commands--------------------------------------------------------------
  if(sequence[i]==0): # check if there is Left_up action
    print('Turn Left')
    y_temp = motion.getAngles(handName, useSen) #Save the elbow's turned angle in 'y_temp' variable
    motion.moveTo(0,0,abs(0.18))        #Turning Left  by 10deg
    time.sleep(2.0)
    motion.setAngles(handName,y_temp[0],0.5)  #Return the elbow once to the turned position to 'y_temp' 
    time.sleep(2.0)
    y = motion.getAngles(handName, useSen)    #get the elbow angle
    y_past = y[0]               #set the y_past to the recent elbow angle

  elif(sequence[i]==1): # check if there is Right_up action
    print('Turn Right')
    y_temp = motion.getAngles(handName, useSen)
    motion.moveTo(0,0,-abs(0.18))       #Turning Right  by 10deg
    time.sleep(2.0)
    motion.setAngles(handName,y_temp[0],0.5)
    time.sleep(2.0)
    y = motion.getAngles(handName, useSen)
    y_past = y[0]

  elif(sequence[i]==2):  # check if there is Both_up action 
    print('Move Forward')
    motion.moveToward(1.0, 0.0, 0.0) #move forward at full speed
    time.sleep(5.0)                  # for 5 seconds
    print "Moving Speed X :",motion.getRobotVelocity()[0]," m/s" 
    motion.moveToward(0.0, 0.0, 0.0) #stop moving
    y = motion.getAngles(handName, useSen)    #get the elbow angle
    y_past = y[0]               #set the y_past to the recent elbow angled
  if(i!=len(sequence)-1):
    i=i+1




