# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY test/test_google_search.py .

RUN pip install selenium

ENV SELENIUM_HUB=http://selenium-hub:4444/wd/hub
CMD ["python3", "test_google_search.py"]

