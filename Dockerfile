# Use a minimal Python base image
FROM python:3.11-slim

# Set the working directory for copying source code
WORKDIR /app

# Copy the entire test directory from the host to /app/test inside the container
COPY test/ test/

# Install required Python packages
# --no-cache-dir reduces the image size by not storing build cache
RUN pip install --no-cache-dir selenium

# Set environment variable for Selenium Hub
# This can also be set in docker-compose.yml for more flexibility
ENV SELENIUM_HUB=http://selenium-hub:4444/wd/hub

# Set the working directory to where your test script resides
# This makes it easier to reference test files
WORKDIR /app/test

# Run the Python test
# Since WORKDIR is /app/test, the script name is just 'test_google_search.py'
# Note: If your current Python script is testing DuckDuckGo, consider renaming
# 'test_google_search.py' to something like 'test_duckduckgo_search.py' for clarity.
CMD ["python3", "test_google_search.py"]
