# Use a minimal Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only the test script into the container
COPY test/test_google_search.py .
# (Optional) Copy test directory for writing result.log to correct location
RUN mkdir -p test

# Install required Python packages
RUN pip install --no-cache-dir selenium

# Environment variable for Selenium Hub URL
ENV SELENIUM_HUB=http://selenium-hub:4444/wd/hub

# Run the Python test
CMD ["python3", "test_google_search.py"]

