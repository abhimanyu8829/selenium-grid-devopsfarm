import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

hub_url = os.getenv("SELENIUM_HUB", "http://selenium-hub:4444/wd/hub")

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    for i in range(15):
        try:
            driver = webdriver.Remote(command_executor=hub_url, options=options)
            print("✅ Successfully connected to Selenium Hub.")
            return driver
        except WebDriverException as e:
            print(f"⏳ Connection attempt {i+1}/15 failed. Retrying in 2 seconds. Error: {e}")
            time.sleep(2)

    raise Exception("❌ Could not connect to Selenium Hub after multiple retries.")

def run_test():
    driver = None
    try:
        search_engine_url = "https://duckduckgo.com/"
        driver = get_driver()
        print(f"🚀 Starting the test: Navigating to {search_engine_url}")
        driver.get(search_engine_url)

        print("🌐 Current URL:", driver.current_url)
        print("📄 Page title:", driver.title)

        print("Waiting for DuckDuckGo homepage to load...")
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "search_form_input_homepage"))
            )
            print("✅ DuckDuckGo homepage loaded successfully using ID.")
        except TimeoutException:
            print("⚠️ ID-based search box not found. Trying by NAME='q'...")
            try:
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.NAME, "q"))
                )
                print("✅ DuckDuckGo homepage loaded successfully using NAME.")
            except TimeoutException:
                raise Exception("DuckDuckGo homepage did not load in time.")

        print("🔍 Finding the search box and entering 'amazon'.")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("amazon")
        search_box.send_keys(Keys.RETURN)

        print("Waiting for search results to load on DuckDuckGo...")
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.results--main"))
            )
            print("✅ DuckDuckGo search results loaded.")
        except TimeoutException:
            raise Exception("DuckDuckGo search results did not load in time.")

        print("📄 Processing search results...")
        links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
        found = False
        for link in links:
            href = link.get_attribute("href")
            if href:
                print("🔗", href)  # optional: remove this line if too verbose
                if "amazon.in" in href or "amazon.com" in href:
                    print("🎯 Found Amazon link:", href)
                    found = True
                    break

        result_message = (
            "✅ DuckDuckGo Search Test Passed: Found amazon.in or amazon.com!"
            if found else
            "❌ DuckDuckGo Search Test Failed: Could not find amazon.in or amazon.com."
        )
        print(result_message)

    except Exception as e:
        print(f"❌ An error occurred during the test: {e}")
    finally:
        print("🛑 Test finished. Closing the driver.")
        if driver:
            driver.quit()

if __name__ == "__main__":
    run_test()

