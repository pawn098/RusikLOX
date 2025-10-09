from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get('https://demoqa.com/text-box')
driver.maximize_window()


box_full_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "userName")))
box_full_name.send_keys('Nikita')

box_email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "userEmail")))
box_email.send_keys('tr@gmail.com')

button_snbmit = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submit")))
button_snbmit.click()

box_output = WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "output")))
print(box_output.text)