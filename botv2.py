from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # <-- ADD THIS IMPORT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# 1. Define the path to your downloaded WebDriver executable
# --- REPLACE THIS PATH with the actual location of the file you saved ---
CHROMEDRIVER_PATH = 'C:\\Drivers\\chromedriver.exe' # Example: 'C:\\Drivers\\chromedriver.exe' on Windows

# --- START OF NEW/MODIFIED CODE BLOCK ---

# 1.5. Configure Chrome Options to allow camera and microphone access
chrome_options = Options()
# Set the preference value to 1 (Allow) for media streams
prefs = {
    "profile.default_content_setting_values.media_stream_camera": 1,  # Allow camera
    "profile.default_content_setting_values.media_stream_mic": 1,    # Allow microphone (good practice)
}
chrome_options.add_experimental_option("prefs", prefs)

# 2. Use the Service object to specify the driver path
service = Service(executable_path=CHROMEDRIVER_PATH)

# 3. Initialize the browser, passing the configured options
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- END OF NEW/MODIFIED CODE BLOCK ---

# You can now use 'driver' to automate the website
driver.get("https://www.snapchat.com/web")
# ... rest of your code remains the same ...
print(f"Current page title: {driver.title}")

def sign_in(username, password):
    #user_field = driver.find_element(By.ID, 'ai_input')
    user_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'ai_input')))
    user_field.send_keys(username)
    #sleep(2)
    #user_field_submit = driver.find_element(By.CSS_SELECTOR, '.buttons_sdsButton__57EIz')
    user_field_submit = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.buttons_sdsButton__57EIz')))
    user_field_submit.click()
    #sleep(10)
    #pass_field = driver.find_element(By.ID, 'password')
    pass_field = WebDriverWait(driver, 20
                               ).until(EC.visibility_of_element_located((By.ID, 'password')))
    pass_field.send_keys(password)
    #sleep(1)
    #pass_field_submit = driver.find_element(By.CSS_SELECTOR, '.Login_next__2nEN0')
    pass_field_submit = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.Login_next__2nEN0')))
    pass_field_submit.click()
    #sleep(3)
    #no_notifs = driver.find_element(By.CSS_SELECTOR, '.cV8g1')
    no_notifs = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cV8g1')))
    no_notifs.click()
    #sleep(2)
    #open_cam = driver.find_element(By.CSS_SELECTOR, '.BN1L1')
    open_cam = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.BN1L1')))
    open_cam.click()

def send_pic(no_of_pics, account):
    x = 0
    sleep(3)
    while x < no_of_pics:
        #shutter = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/button[1]')
        #shutter = driver.find_element(By.XPATH, '//div[@aria-roledescription="draggable"]/ancestor::button[1]')
        shutter = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-roledescription="draggable"]/ancestor::button[1]')))
        sleep(0.3)
        #print(f"Element {shutter} is found.")
        #shutter = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Fpg8t > div.Vbjsg.WJjwl > div > div.ChLAv > div > div.L3KxA > div.IiObz.VvubJ > div > div > div > div > div > div.CYQZP > div > div.P9cx7 > div.VLm6Y')))
        #By.XPATH, '/html/body/main/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]'
        #driver.execute_script("arguments[0].click();", shutter)#By.CSS_SELECTOR, '#root > div.Fpg8t > div.Vbjsg.WJjwl > div > div.ChLAv > div > div.L3KxA > div.IiObz.VvubJ > div > div > div > div > div > div.CYQZP > div > div.P9cx7 > div.VLm6Y'
        shutter.click()
        #send = driver.find_element(By.XPATH, '//*[@id="snap-preview-container"]/div[2]/button[2]')
        #sleep(0.1)
        WebDriverWait(driver, 180).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'Ewflr')))
        send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snap-preview-container"]/div[2]/button[2]')))
        send.click()
        #name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="BN1L1"]/div/div/form/div/ul/ul/li[1]/div/div[1]/div[text()="Hugo W"]')))
        name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, f'//div[text()="{account}"]')))
        name.click()
        send_to = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Send"]')))
        send_to.click()
        x = x + 1
        print(x)

  
sign_in("username", "password")
send_pic(no. of times you want it to send(int), "snap username of person you want to send pictures to")
print("All pictures have been sent.\nClosing in 20 Seconds.")

sleep(20)

# Clean up
driver.quit()

