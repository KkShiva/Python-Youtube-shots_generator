Setup

1. python -m venv myenv
2. myenv\Scripts\activate
3. pip install moviepy
4. install ImageMagick if not there
https://imagemagick.org/index.php

edit the path in thec code ShotsGenerator.py
```python
# Set the path to the ImageMagick binary
os.environ['IMAGEMAGICK_BINARY'] = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"
```
edit csv path
```python
csv_file_path = "C:/Users/shiva/PythonShot/quotes1_100.csv"
```

also edit input video and output path
```python
# Load your video
video = VideoFileClip("C:/Users/shiva/PythonShot/Ocean.mp4")
.......................................
....
...

    # Define the output file path
    output_file_path = f"C:/Users/shiva/PythonShot /out{idx + 1}.mp4"
```

if requid you can able to change font style to your costam font by changing 
```python
"C:/Users/shiva/PythonShot/Bison-Bold.ttf"
```

NOTE : Will genrate number of output based on the number of cells csv containg text.

example 

befor

![image](https://github.com/user-attachments/assets/df019bb2-7e8a-4d90-8e13-65020044922f)

after

![image](https://github.com/user-attachments/assets/350a102e-4fca-4ebb-91b1-064f55bbc50c)

https://github.com/user-attachments/assets/c4a93c86-46c0-4e66-959e-3417f8d4211c

