import cv2
import os
import time
import sys

# --- Configuration ---
CAMERA_INDEX = 0
SAVE_PATH = "data/raw"
IMG_WIDTH = 640
IMG_HEIGHT = 480
# ---------------------

def main():
    """
    Terminal-based image capture script.
    
    Waits for the user to press 'Enter' to save a frame.
    Type 'q' and press 'Enter' to quit.
    """
    
    # Ensure the save directory exists
    try:
        os.makedirs(SAVE_PATH, exist_ok=True)
    except Exception as e:
        print(f"Error: Could not create directory {SAVE_PATH}. {e}")
        sys.exit(1)

    print(f"--- Data Capture Utility ---")
    print(f"Saving images to: {SAVE_PATH}")
    print(f"Press [Enter] to save an image.")
    print(f"Type 'q' + [Enter] to quit.")
    print("--------------------------------")
    
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"Error: Cannot open camera at index {CAMERA_INDEX}.")
        sys.exit(1)
        
    # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)
    
    print("Camera opened successfully. Ready for capture.")
    
    img_count = 0
    while True:
        try:
            # Get user input
            user_input = input(f"[{img_count} saved] > ")
            
            if user_input.strip().lower() == 'q':
                print("Quitting...")
                break
                
            # Grab a frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame from camera.")
                time.sleep(1) # Wait before retrying
                continue
                
            # Generate a unique filename
            filename = f"frame_{int(time.time() * 1000)}.jpg"
            filepath = os.path.join(SAVE_PATH, filename)
            
            # Save the image
            cv2.imwrite(filepath, frame)
            
            img_count += 1
            print(f"Saved: {filepath}")

        except KeyboardInterrupt:
            # Allow quitting with Ctrl+C
            print("\nQuitting (Ctrl+C)...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Clean up
    cap.release()
    print("--------------------------------")
    print(f"Capture session complete. Total images saved: {img_count}")

if __name__ == "__main__":
    main()