FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Pochi CLI
RUN curl -fsSL https://getpochi.com/install.sh | bash
ENV PATH="/root/.pochi/bin:$PATH"

# Create a non-root user
RUN useradd -m -s /bin/bash user

# Switch to the user
USER user
WORKDIR /home/user

# Add local bin to PATH
ENV PATH="/home/user/.local/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir e2b_code_interpreter pytest

# Set default command
CMD ["tail", "-f", "/dev/null"]
