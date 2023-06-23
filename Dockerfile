RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install opencv-python-headless==4.5.3.56
