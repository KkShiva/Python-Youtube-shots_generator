import os
import csv

# Set the path to the ImageMagick binary
os.environ['IMAGEMAGICK_BINARY'] = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"


from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import textwrap

# Load your video
video = VideoFileClip("C:/Users/shiva/PythonShot/Ocean.mp4")

# Trim the video to the first 10 seconds
video_trimmed = video.subclip(0, 10)

# Get the width of the video
video_width = video_trimmed.w

# Read all text content from the CSV file into a list
csv_file_path = "C:/Users/shiva/PythonShot/quotes1_100.csv"
text_contents = []

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        text_contents.append(row[0])  # Read each row's first cell

# Define the font size
fontsize = 50

for idx, text_content in enumerate(text_contents):
    # Create a TextClip object with a large font size to calculate text width
    temp_text = TextClip(text_content, font="C:/Users/shiva/PythonShot/Bison-Bold.ttf", fontsize=fontsize, color="white")

    # Wrap the text if it exceeds the video width
    wrapped_text = textwrap.fill(text_content, width=int(video_width / (fontsize * 0.6)))  # 0.6 is an approximate ratio

    # Create a TextClip object with the wrapped text
    text_clip = TextClip(wrapped_text, font="C:/Users/shiva/PythonShot/Bison-Bold.ttf", fontsize=fontsize, color="white")

    # Define the top margin for the text
    top_margin = 700  # Adjust this value as needed

    # Set the position and duration of the text (text duration matches video duration)
    text_clip = text_clip.set_position(('center', top_margin)).set_duration(video_trimmed.duration)

    # Overlay the text on the trimmed video
    video_with_text = CompositeVideoClip([video_trimmed, text_clip])

    # Define the output file path
    output_file_path = f"C:/Users/shiva/PythonShot /out{idx + 1}.mp4"

    # Output the final video
    video_with_text.write_videofile(output_file_path, codec="libx264")

    print(f"Video with text '{text_content}' saved as {output_file_path}")