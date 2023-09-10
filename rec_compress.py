import os
from moviepy.editor import VideoFileClip, vfx

# Path to the recorded videos folder
recorded_videos_folder = "f:/recorded_videos"

# Path to the compressed videos folder
compressed_videos_folder = "f:/compressed_videos"

# Create the compressed videos folder if it doesn't exist
if not os.path.exists(compressed_videos_folder):
    os.makedirs(compressed_videos_folder)

# Get the list of recorded video files in the folder
recorded_videos = os.listdir(recorded_videos_folder)

# Loop through each recorded video file
for video_file in recorded_videos:
    # Construct the paths for the input and output files
    input_file = os.path.join(recorded_videos_folder, video_file)
    output_file = os.path.join(compressed_videos_folder, os.path.splitext(video_file)[0] + "_compressed.mp4")
    
    # Load the video clip
    video_clip = VideoFileClip(input_file)
    
    # Compress the video clip
    compressed_clip = vfx.resize(video_clip, width=640)  # Adjust the width as desired
    
    # Set the output file parameters
    compressed_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    
    # Close the video clips
    video_clip.close()
    compressed_clip.close()
    
    # Print the compression progress
    print(f"Compressed: {input_file} -> {output_file}")

print("Compression complete!")
