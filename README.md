# MotionSensorBasedIntelegentCameraSystemWithOptimizedStorageAndRealTimeNotification
the system excels in efficient resource utilization, timely threat detection, and effective response. This project leverages Python as its primary programming language, harnessing the power of computer vision, image processing, and video processing skills to create a robust and versatile security solution.




#How it Work
How does proposed motion detection work?
A. The video enters a loop where it continuously reads frames from the video source.
B. For each frame, it performs the following steps: 
I. Converts the frame to grayscale and applies Gaussian blur for better motion detection 
results. 
II. Computes the absolute difference between the current and previous frames to detect 
motion. 
III. Thresholds the difference image to obtain binary motion regions. 
IV. Performs morphological operations (dilation) to fill in the gaps and improve the 
motion regions. 
V. Finds contours in the thresholded image to identify individual motion blobs.
VI. If a contour is large enough, it is considered as motion, and a bounding rectangle is 
drawn around it on the frame.
VII. The code tracks the number of consecutive frames with detected motion and starts or 
resumes recording if the threshold is reached. 
VIII. If motion is not detected, it pauses the recording.
IX. The frame is displayed with bounding rectangles (if applicable). 
X. If recording is in progress, the frame is written to the video file


#How does proposed compression technique work?
I. The Algorithm assumes that there is a folder named "recorded_video" containing the 
recorded video files. It also specifies the path for the compressed videos folder, which is 
"compressed_video". If the compressed videos folder doesn't exist, the code creates it.
II. The list of recorded video files in the recorded video folder is obtained.
III. The code loops through each recorded video file and performs the compression process.
IV. For each video file, the input file path and output file path are constructed.
V. The video clip is loaded using `VideoFileClip` from the moviepy library.
VI. The `resize` function is applied to the video clip to reduce its width while maintaining the 
aspect ratio. The width is set to 640 pixels, but you can adjust it to your desired value.
VII. The output file parameters are set, including the codec ("libx264") for video encoding 
VIII. The compressed video clip is saved as the output file using `write_videofile`.
IX. The video clips (original and compressed) are closed.
X. The compression progress is printed, showing the input file path and output file path for 
each compressed video.
XI. The original recorded video file is deleted using `os.remove`.
XII. Once all the video files have been processed, a message is printed to indicate the 
completion of the compression process.




#How does proposed Real-time notification technique work?
A real-time mail notification system for sending an email with an attached video file when 
motion is detected. 
I. The email configuration is set, including the sender's email address (`sender_email`), the 
receiver's email address (`receiver_email`), the subject of the email (`subject`), and the body of 
the email (`body`).
II. The code assumes there is a folder named "compressed_video" containing compressed 
video files. It selects the first video file in the folder (`selected_video_file`) and 
constructs the full path to the video file (`video_path`).
III. An `EmailMessage` object is created, and the sender, receiver, subject, and body are 
set.
IV. The selected video file is loaded using `VideoFileClip` 
V. The video is split into a 10-second clip 
VI. The split clip is saved as a temporary file named "temp.mp4".
VII. The temporary file is opened, and its contents are read. The split video is added as an 
attachment to the email message.
VIII. The temporary file is deleted.
IX. The video clips are closed.
X. An SMTP connection is established with the Gmail server (`smtp.gmail.com`).
XI. The connection is secured using `starttls`.
XII. The sender's email and password are provided for authentication using `login` method.
XIII. The email message is sent using `send_message` method.
XIV. A success message is printed if the email notification is sent successfully.
In summary, the technique we select a video file, splits it into a 10-second clip, attaches it to an 
email, and sends it to the specified receiver's email address. This system can be used to notify the 
receiver about detected motion and provide them with a video recording for further analysis or 
investigation.
