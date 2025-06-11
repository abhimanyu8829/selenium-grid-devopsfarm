# Use a minimal Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the entire test directory
COPY test/ test/

# Install required Python packages
RUN pip install --no-cache-dir selenium

# Set environment variable for Selenium Hub
ENV SELENIUM_HUB=http://selenium-hub:4444/wd/hub

# Set the working directory to the test folder
WORKDIR /app/test

# Run the Python test
CMD ["python3", "test_google_search.py"]

