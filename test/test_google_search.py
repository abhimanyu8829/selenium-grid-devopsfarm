import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

# Get the Selenium Hub URL from environment variables, with a default value
hub_url = os.getenv("SELENIUM_HUB", "http://selenium-hub:4444/wd/hub")

def get_driver():
    """
    Creates and returns a remote WebDriver instance.
    Includes a retry mechanism to wait for the Selenium Hub to be ready.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Retry connecting to the Selenium Hub for up to 30 seconds
    for i in range(15):
        try:
            # Attempt to create a new remote session with the hub
            driver = webdriver.Remote(command_executor=hub_url, options=options)
            print("✅ Successfully connected to Selenium Hub.")
            return driver
        except WebDriverException as e:
            # If connection fails, wait and retry
            print(f"⏳ Connection attempt {i+1}/15 failed. Retrying in 2 seconds...")
            time.sleep(2)
    
    # If all retries fail, raise an exception
    raise Exception("❌ Could not connect to Selenium Hub after multiple retries.")

def run_test():
    """
    Runs the main test logic: searches Google and checks for a specific URL.
    """
    driver = get_driver()
    try:
        print("🚀 Starting the test: Navigating to Google.com")
        driver.get("https://www.google.com")
        time.sleep(2) # Wait for the page to load

        print("🔍 Finding the search box and entering 'devopsfarm'.")
        search = driver.find_element(By.NAME, "q")
        search.send_keys("devopsfarm")
        search.send_keys(Keys.RETURN)
        time.sleep(2) # Wait for search results to load

        print("📄 Processing search results...")
        links = driver.find_elements(By.XPATH, '//a')
        found = False
        
        # Ensure the 'test' directory exists before writing the file
        if not os.path.exists("test"):
            os.makedirs("test")
            
        with open("test/result.log", "w") as f:
            for link in links:
                url = link.get_attribute("href")
                if url:
                    f.write(f"{url}\n")
                    if "devopsfarm.in" in url:
                        print(f"🎉 Found matching URL: {url}")
                        found = True
            
            result_message = "✅ devopsfarm.in Found!" if found else "❌ devopsfarm.in Not Found."
            f.write(f"\n{result_message}\n")
            print(result_message)

    finally:
        # Always quit the driver to close the session and browser
        print("🛑 Test finished. Closing the driver.")
        driver.quit()

if __name__ == "__main__":
    run_test()
