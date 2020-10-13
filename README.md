# -Follow-Me-robot-control-program
The given project aims to make a Nao robot to follow a human, who would lead the robot by raising its hand. The speed increases linearly as the hand rises, while turning action is also considered. Additionally, the robot recognizes visually gesture commands by reading the output of OpenPose software. The Naoqi module was used to work with a virtual robot in Choregraphe software. The code is written in Python language.

The instruction for using the RobotControl code:
1. Record a video with left-hand-up, right-hand-up, and/or both-hands-up
2. Name the video as "Gesture_Control.mp4"
3. Save the video in the folder "videos", which is located on the desktop
4. Run parse_video.py module
5. Run to_format.py module
6. Save the output .csv file in the desktop
7. Run the "PoseEstimation.py" module
8. See the "GestureInfo.csv" file in the desktop
9. Run the Choregraphe software
10. Run "RobotControl.py" module 
11. See that gesture commands in the video are executed
12. After, you can turn the robot by turning the 'LElbowYaw' angle
13. To move the robot, raise the robot hand by turning 'LShoulderPitch'


