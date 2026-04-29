import cv2
import mediapipe as mp
import numpy as np
from collections import deque

# 1. Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7
)

# Start Video Capture
cap = cv2.VideoCapture(0)

# 2. Setup Upgraded Variables
smooth_queue = deque(maxlen=5) # Stores last 5 points for butter-smooth averaging
prev_pt = None
current_hue = 0

# Grab the first frame to get the window size and create a permanent black canvas
success, frame = cap.read()
h, w, c = frame.shape
canvas = np.zeros((h, w, 3), dtype=np.uint8)

print("🎨 Draw your masterpiece! ")
print("👉 Move your index finger slowly to draw.")
print("👉 Press 'C' to clear the canvas.")
print("👉 Press 'ESC' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame for a natural mirror feel
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the exact tip of the index finger
            index_finger_tip = hand_landmarks.landmark[8]
            raw_x = int(index_finger_tip.x * w)
            raw_y = int(index_finger_tip.y * h)

            # --- UPGRADE 1: Motion Smoothing ---
            # Average the last 5 frames to completely remove hand/camera jitter
            smooth_queue.append((raw_x, raw_y))
            smooth_x = int(np.mean([pt[0] for pt in smooth_queue]))
            smooth_y = int(np.mean([pt[1] for pt in smooth_queue]))
            curr_pt = (smooth_x, smooth_y)

            # Cycle the colors slowly
            current_hue = (current_hue + 1) % 180
            
            # Convert HSV to BGR color
            color_hsv = np.uint8([[[current_hue, 255, 255]]])
            base_color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            base_color = (int(base_color[0]), int(base_color[1]), int(base_color[2]))

            if prev_pt is not None:
                # --- UPGRADE 2: Neon Tube Effect ---
                
                # Layer 1: The thick, colorful base glow
                cv2.line(canvas, prev_pt, curr_pt, base_color, thickness=18, lineType=cv2.LINE_AA)
                
                # Layer 2: The thin, bright inner core
                # We mix the base color with white (255) to make it pop
                core_color = (
                    min(255, base_color[0] + 120), 
                    min(255, base_color[1] + 120), 
                    min(255, base_color[2] + 120)
                )
                cv2.line(canvas, prev_pt, curr_pt, core_color, thickness=6, lineType=cv2.LINE_AA)

            prev_pt = curr_pt
    else:
        # If the camera loses your hand, break the line so it doesn't draw a random 
        # streak across the screen when your hand comes back.
        prev_pt = None
        smooth_queue.clear()

    # --- UPGRADE 3: Show the Permanent Canvas ---
    cv2.imshow('Satisfying Hand Patterns', canvas)

    # Keyboard Controls
    key = cv2.waitKey(1) & 0xFF
    if key == 27: # Press 'ESC' to exit
        break
    elif key == ord('c') or key == ord('C'): # Press 'C' to clear the screen
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

# Clean up
cap.release()
cv2.destroyAllWindows()