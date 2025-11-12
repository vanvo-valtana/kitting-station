# Define all targets as .PHONY so 'make' doesn't
# get confused by a file named 'test' or 'build'
.PHONY: all test build shell capture test-env test-cam

# --- Development ---

# Build the custom docker image
build:
	docker compose build

# Launch a bash shell in the container
shell:
	docker compose run --rm app bash

# --- Verification ---

# Run the environment (PyTorch) test
test-env:
	docker compose run --rm app python3 /app/main.py

# Run the camera verification test
test-cam:
	docker compose run --rm app python3 /app/verify_cam.py

# Run ALL tests
test: test-env test-cam

# --- Application ---

# Run the data capture script
capture:
	docker compose run --rm app python3 /app/capture.py