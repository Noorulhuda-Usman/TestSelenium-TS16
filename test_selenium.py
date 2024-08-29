from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Setup ChromeDriver using webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Open a website
    driver.get('https://www.example.com')
    
    # Print the title of the page
    print("Page title is:", driver.title)
    
    # Example: Wait for an element to be present
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    print("Element found:", element.text)
    
    # Wait for user input before closing the browser
    input("Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'driver' in locals():
        driver.quit()






