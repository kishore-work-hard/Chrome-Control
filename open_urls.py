import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Read the Excel file into a DataFrame
excel_file = "ip.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet1")

# Extract the URLs from the 'IP' column
urls = df['IP'].tolist()

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Example username and password
username = "admin"
password = "Elvicto@123"

for url in urls:
    url_with_protocol = "http://" + url if not url.startswith(("http://", "https://")) else url
    print("Opening URL:", url_with_protocol)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url_with_protocol)

    # Example: Wait for the username input field and enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys(username)

    # Example: Wait for the password input field and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(password)

    # Example: Press Enter key to submit the form (after typing the password)
    password_input.send_keys(Keys.ENTER)



# Wait for user input before proceeding to the next iteration
input("Press Enter to continue...")
