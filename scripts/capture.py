import cv2
import os
import time
import sys
import select

# --- Configuration ---
CAMERA_INDEX = 0
SAVE_PATH = "data/raw"
IMG_WIDTH = 640
IMG_HEIGHT = 480
# ---------------------

def is_enter_pressed():
    """Check for non-blocking [Enter] key press."""
    # select.select checks if sys.stdin (terminal input)
    # has data waiting to be read.
    # The '0' timeout makes it non-blocking.
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def main():
    """
    Headless, non-blocking image capture script.
    
    Fixes buffer lag by continuously reading frames.
    - Press [Enter] to save a frame.
    - Press [q] + [Enter] to quit.
    """
    
    try:
        os.makedirs(SAVE_PATH, exist_ok=True)
    except Exception as e:
        print(f"Error: Could not create directory {SAVE_PATH}. {e}")
        sys.exit(1)

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"Error: Cannot open camera at index {CAMERA_INDEX}.")
        sys.exit(1)
        
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
    
    print("--- Headless Data Capture Utility (v3) ---")
    print(f"Saving images to: {SAVE_PATH}")
    print("Press [Enter] to save an image.")
    print("Type 'q' + [Enter] to quit.")
    print("------------------------------------------")
    
    img_count = 0
    while True:
        # 1. Continuously read frames to clear the buffer
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            break
            
        # 2. Check for user input without blocking
        if is_enter_pressed():
            # Read the input
            line = sys.stdin.readline().strip()
            
            if line == 'q':
                print("Quitting...")
                break
                
            # If it was any other key (like Enter), save the frame
            filename = f"frame_{int(time.time() * 1000)}.jpg"
            filepath = os.path.join(SAVE_PATH, filename)
            
            # Save the *current* live frame
            cv2.imwrite(filepath, frame)
            
            img_count += 1
            print(f"[{img_count}] Saved: {filepath}")

    # Clean up
    cap.release()
    print("------------------------------------------")
    print(f"Capture session complete. Total images saved: {img_count}")

if __name__ == "__main__":
    main()