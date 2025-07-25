# Use official Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set display port to avoid crash
ENV DISPLAY=:99

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose Streamlit port
EXPOSE 7860

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"] 