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
