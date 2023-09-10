import cv2
import time
import os


# Define the video capture object
video = cv2.VideoCapture(0)

# Initialize motion status
motion_detected = False

# Define parameters for motion detection
motion_threshold = 110  # Adjust this value to set the motion sensitivity
min_motion_frames = 10   # Number of consecutive frames needed to trigger motion

# Initialize variables for motion detection
motion_frame_count = 0
last_frame = None

# Define the video codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = None
output_folder = "recorded_videos"  # Change this to the desired output folder path
recording = False

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while True:
    # Read the current frame from the video capture object
    ret, frame = video.read()
    
    # Convert the frame to grayscale for motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # If this is the first frame, save it for later comparison
    if last_frame is None:
        last_frame = gray
        continue
    
    # Compute the absolute difference between the current and previous frame
    frame_delta = cv2.absdiff(last_frame, gray)
    thresh = cv2.threshold(frame_delta, motion_threshold, 255, cv2.THRESH_BINARY)[1]
    
    # Apply a series of dilations to fill in the holes
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    # Find contours of the threshold image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Initialize motion detected flag for this iteration
    motion_detected_this_frame = False
    
    # Loop over the contours
    for contour in contours:
        # If the contour is too small, ignore it
        if cv2.contourArea(contour) < motion_threshold:
            continue
        
        # Motion detected
        motion_detected_this_frame = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Check if motion status has changed
    if motion_detected_this_frame:
        motion_frame_count += 1
        if motion_frame_count >= min_motion_frames:
            # Start or resume recording
            if not recording:
                current_time = time.strftime("%Y%m%d-%H%M%S")
                output_file = os.path.join(output_folder, f"recorded_video_{current_time}.avi")
                video_writer = cv2.VideoWriter(output_file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
                print("Recording started.")
                recording = True
    else:
        # Pause recording if motion is not detected
        if recording:
            video_writer.release()
            print("Recording paused.")
            recording = False
    
    # Display the frame
    cv2.imshow("Motion Detection", frame)
    
    # Save the frame to the recorded video file
    if recording:
        video_writer.write(frame)
    
    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# Release the video capture object and destroy the windows
video.release()
cv2.destroyAllWindows()

