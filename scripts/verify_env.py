import torch
import sys

def main():
    """
    Main application entrypoint.

    Performs a "smoke test" to verify PyTorch and CUDA availability.
    """
    print("--- Kitting Station Smoke Test ---")

    try:
        print(f"Python Version: {sys.version.split()[0]}")
        print(f"PyTorch Version: {torch.__version__}")

        # The most critical test
        is_cuda = torch.cuda.is_available()
        print(f"CUDA Available: {is_cuda}")

        if not is_cuda:
            print("Error: CUDA is not available to PyTorch.")
            sys.exit(1)

        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print("-----------------------------------------")
        print("SUCCESS: Environment is verified.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()