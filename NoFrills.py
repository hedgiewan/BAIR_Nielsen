
import os
import time
from picamera2 import Picamera2, Preview
from guizero import App, Text, TextBox, PushButton

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")

picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

def snap_plate():
    picam2.capture_file(file_name)

app = App(title="Plate Photo")
message = Text(app, text="Input File Name")
file_name = TextBox(app)

PushButton(
    app,
    command=snap_plate
    text="Start"
)

app.display()
