
import os
import time
from fractions import Fraction
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import ACTIVE, DISABLED
from picamera2 import Picamera2, Preview
from guizero import App, Text, TextBox, PushButton

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")

app = App(title="Plate Photo")
message = Text(app, text="Input File Name")
file_name = TextBox(app)
snap = PushButton(
    app,
    command=camera_config,
    text="Start"
)
app.display()
