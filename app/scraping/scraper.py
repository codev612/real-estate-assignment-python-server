from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_driver():
    chrome_options = Options()
    chrome_options.binary_location = r"C:\chrome-win64\chrome.exe"
    # chrome_options.add_argument('--headless')  # Run browser in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print(driver)
    
    return driver

def scrape_listings():
    try:
        driver = get_driver()
        url = 'https://www.zillow.com/san-diego-ca/rentals/'
        driver.get(url)
        
        # Wait until the listings are loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "property-card-data"))
        )

        listings = []
        listings_elements = driver.find_elements(By.CLASS_NAME, "property-card-data")
        
        for item in listings_elements:
            try:
                price_element = item.find_element(By.CSS_SELECTOR, '[data-test="property-card-price"]')
                price = price_element.text.strip() if price_element else "N/A"
                
                link_element = item.find_element(By.CSS_SELECTOR, '[data-test="property-card-link"]')
                link = link_element.get_attribute('href') if link_element else "N/A"
                
                listings.append({'price': price, 'link': link})
            except Exception as e:
                print(f"Error extracting details for item: {e}")
                continue

        driver.quit()
        print(listings)
        return listings
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return []

# Call the function to test
scrape_listings()
