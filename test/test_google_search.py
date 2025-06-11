import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

hub_url = os.getenv("SELENIUM_HUB", "http://selenium-hub:4444/wd/hub")

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Remote(command_executor=hub_url, options=options)

def run_test():
    driver = get_driver()
    driver.get("https://www.google.com")
    time.sleep(2)
    search = driver.find_element(By.NAME, "q")
    search.send_keys("devopsfarm")
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    links = driver.find_elements(By.XPATH, '//a')
    found = False
    with open("test/result.log", "w") as f:
        for link in links:
            url = link.get_attribute("href")
            if url:
                f.write(f"{url}\n")
                if "devopsfarm.in" in url:
                    found = True
        f.write("\n✅ devopsfarm.in Found!\n" if found else "\n❌ devopsfarm.in Not Found.\n")
    driver.quit()

if __name__ == "__main__":
    run_test()

