import cv2
import sys

# Per our plan, the camera is device 0
# This corresponds to /dev/video0
CAMERA_INDEX = 0

def main():
    print("--- Camera Verification Test ---")
    try:
        print(f"CV2 Version: {cv2.__version__}")

        # Attempt to open the camera
        cap = cv2.VideoCapture(CAMERA_INDEX)

        if not cap.isOpened():
            print(f"Error: Cannot open camera at index {CAMERA_INDEX}.")
            print("Check 'docker-compose.yml' device mapping.")
            sys.exit(1)

        print("Successfully opened camera feed.")

        # Read one frame to confirm
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            sys.exit(1)

        print(f"SUCCESS: Captured 1 frame. Dimensions: {frame.shape}")

        # Clean up
        cap.release()
        print("----------------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()