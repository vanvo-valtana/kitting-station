# Start from our verified NVIDIA base image
FROM nvcr.io/nvidia/pytorch:25.06-py3-igpu

# Set the working directory (matches our compose file)
WORKDIR /app

# Install common OpenCV GUI dependencies for Ubuntu 24.04
# Replaces the obsolete 'libgl1-mesa-glx'
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglx-mesa0 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy our requirements file
COPY requirements.txt .

# Install our project's Python dependencies
RUN pip install -r requirements.txt