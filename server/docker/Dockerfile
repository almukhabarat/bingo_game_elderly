# Use a Debian base image
FROM debian:buster

# Install dependencies for running x86 binaries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libssl-dev \
    libffi-dev \
    wget \
    unzip \
    python \
    python-pip \
    python-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Download QEMU static binary for x86_64 emulation
RUN wget --no-check-certificate https://github.com/multiarch/qemu-user-static/releases/download/v5.2.0-2/qemu-x86_64-static -O /usr/bin/qemu-x86_64-static && \
    chmod +x /usr/bin/qemu-x86_64-static

# Copy the local NAOqi SDK files into the Docker image
COPY ./pynaoqi-python2.7-2.8.7.4-linux64 /opt/naoqi-sdk

# Set environment variables for NAOqi
ENV PYTHONPATH="/opt/naoqi-sdk/lib/python2.7/site-packages:$PYTHONPATH"
ENV PATH="/opt/naoqi-sdk/bin:$PATH"
ENV LD_LIBRARY_PATH="/opt/naoqi-sdk/lib:$LD_LIBRARY_PATH"

# Ensure the NAOqi SDK is in the Python path and library path
RUN echo 'export PYTHONPATH=/opt/naoqi-sdk/lib/python2.7/site-packages:$PYTHONPATH' >> /root/.bashrc && \
    echo 'export PATH=/opt/naoqi-sdk/bin:$PATH' >> /root/.bashrc && \
    echo 'export LD_LIBRARY_PATH=/opt/naoqi-sdk/lib:$LD_LIBRARY_PATH' >> /root/.bashrc

# Set the working directory
WORKDIR /opt/naoqi-sdk

# Run a Bash shell by default
CMD ["bash"]