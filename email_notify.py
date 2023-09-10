import os
import smtplib
from email.message import EmailMessage
from moviepy.editor import VideoFileClip

# Email configuration
sender_email = 'techlab.leul@gmail.com'
receiver_email = 'janleul33@gmail.com'
subject = 'Captured Video'
body = 'Motion detected! It may be an intruder. Please check the attached video. for more video data cheack the store'

# Path to the compressed videos folder
compressed_videos_folder = "f:/compressed_videos"

# Select one compressed video file
selected_video_file = os.listdir(compressed_videos_folder)[0]

# Construct the path for the selected video file
video_path = os.path.join(compressed_videos_folder, selected_video_file)

# Create the email message
message = EmailMessage()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(body)

# Load the video clip
video_clip = VideoFileClip(video_path)

# Split the video into a 10-second clip
split_clip = video_clip.subclip(0, 10)

# Save the split clip as a temporary file
temp_file = "temp.mp4"
split_clip.write_videofile(temp_file, codec="libx264", audio_codec="aac")

# Add the split video as an attachment to the email
with open(temp_file, 'rb') as f:
    attachment_data = f.read()
    message.add_attachment(attachment_data, maintype='video', subtype='mp4', filename=selected_video_file)

# Delete the temporary file
os.remove(temp_file)

# Close the video clips
video_clip.close()
split_clip.close()

# Send the email notification
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, 'wajnmktcvnmvcpkc')  # password 
    smtp.send_message(message)

print("Email notification sent successfully!")
