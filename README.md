# Kitting Station (Valtana Solutions)

This is the public-by-default portfolio project for Valtana Solutions LLC.

It is a containerized, GPU-accelerated computer vision system for validating manufacturing kits, built on a Jetson device.

# Automated Kitting Verification (AKV) System

[![CI - Lint, Test, and Build](https://github.com/vanvo-valtana/kitting-station/actions/workflows/ci.yml/badge.svg)](https://github.com/vanvo-valtana/kitting-station/actions/workflows/ci.yml)


## Core Architecture (SENSE-THINK-REPORT)

* **SENSE (The Light Box):** A custom "open-front" enclosure built from MDF and wooden dowels. It uses internal, diffuse A4 paper walls illuminated by 12V LEDs to create a shadowless, high-quality imaging environment.
* **THINK (The "Brain"):** A YOLOX model, running in a GPU-accelerated PyTorch container on the Jetson Orin, performs real-time part identification and counting.
* **REPORT (The "Result"):**
    * **Operator Feedback:** Simple, high-visibility 5V LEDs (Green for PASS, Red for FAIL) and a piezo buzzer (on FAIL) are driven directly by the Jetson's GPIO.
    * **Manager Feedback:** The main Python script logs all results (pass/fail, timestamp, missing parts) to a `pass_fail_log.csv` file for auditing.

## Technology Stack

* **Host:** NVIDIA Jetson Orin (JetPack 6.2)
* **Runtime:** Docker + Docker Compose
* **Base Image:** `nvcr.io/nvidia/pytorch:25.06-py3-igpu` (from `Dockerfile`)
* **AI Framework:** PyTorch
* **Vision:** OpenCV
* **Power:** A single 12V DC supply, stepped down to 5V via an LM2596 buck converter for the "REPORT" components.
* **CI/CD:** GitHub Actions (Flake8 Linting & Cross-Platform `arm64` Docker Build)

## Local Development (Makefile)

This project uses a `Makefile` to simplify all common Docker commands.

```bash
# Build the custom Docker image
make build

# Launch a bash shell in the container
make shell

# Run all verification tests (PyTorch & Camera)
make test

# Run the main application entrypoint
make run

# Run the data capture utility
make capture

