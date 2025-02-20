from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (Make sure the path is correct for your ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open Aternos login page
driver.get('https://aternos.org/login')

# Wait for page to load
time.sleep(3)

# Log in (replace with your Aternos credentials)
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys('YOUR_USERNAME')
password.send_keys('YOUR_PASSWORD')

# Submit the login form
driver.find_element(By.ID, 'login').click()

# Wait for login to complete
time.sleep(5)

# Navigate to the server dashboard page
driver.get('https://aternos.org/server')

# Wait for the page to load
time.sleep(5)

# Check if the server is already running
server_status = driver.find_element(By.XPATH, '//*[contains(text(), "Server is running")]')

if not server_status:
    # Start the server (button or trigger may vary)
    start_button = driver.find_element(By.XPATH, '//*[contains(text(), "Start")]')
    start_button.click()

    # Wait for the server to start
    print("Starting server...")
    time.sleep(10)  # wait a bit for the server to start

# Repeat the check every 10 minutes
while True:
    time.sleep(600)  # Sleep for 10 minutes
    driver.refresh()
    
    # Re-check the server status
    if not driver.find_element(By.XPATH, '//*[contains(text(), "Server is running")]'):
        start_button = driver.find_element(By.XPATH, '//*[contains(text(), "Start")]')
        start_button.click()
        print("Server started again.")

# Close the browser after execution
driver.quit()
