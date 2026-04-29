# Satisfying Neon Hand Drawing 🎨✨

An interactive, computer-vision-based drawing application that lets you create smooth, glowing neon patterns in the air using just your index finger! 

This project leverages **MediaPipe** for precise hand tracking and **OpenCV** to render a beautiful, color-shifting neon tube effect on a digital canvas.

## ✨ Features

* **Motion Smoothing:** Uses mathematical averaging to completely remove hand and camera jitter, resulting in butter-smooth, stable lines.
* **Neon Tube Effect:** Renders a layered drawing effect with a thick, colorful base glow and a bright, thin inner core to simulate realistic neon light.
* **Dynamic Color Cycling:** The drawing color automatically cycles through the color spectrum (HSV hue shift) as you move your finger.
* **Smart Line Breaking:** Automatically stops drawing if it loses track of your hand, preventing random streaks across your canvas when your hand reappears.

## 🛠️ Prerequisites

You will need Python 3.x installed. To install the required libraries, run the following command in your terminal or command prompt:

```bash
pip install opencv-python mediapipe numpy

How to Run and Play
Ensure your webcam is connected and accessible.

Run the Python script:

Bash
python neon_drawing.py
(Replace neon_drawing.py with the actual name of your Python file).

A window titled "Satisfying Hand Patterns" will open, showing a black canvas.

To Draw: Hold up your hand so the camera can see it. Move your index finger slowly to start drawing your neon masterpiece!

To Break the Line: Simply lower your hand or close your fist to hide your index finger from the camera.

⌨️ Controls
Move Index Finger: Draw on the canvas.

Press C: Clear the screen to start a new drawing.

Press ESC: Quit the application.
