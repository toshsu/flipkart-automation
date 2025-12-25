from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Flipkart
driver.get("https://www.flipkart.com/")
print("Flipkart opened!")

time.sleep(3)

# ---- Search Watch ----
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("watch")
search_box.submit()
print("Searched Watch")

time.sleep(4)

# ---- Open first product ----
first_product = driver.find_element(
    By.XPATH,
    "(//a[contains(@href,'/p/') and @rel='noopener noreferrer'])[1]"
)
first_product.click()
print("Opening product...")

# Switch to new tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(4)

# ---- Click Wishlist ❤️ ----
try:
    wishlist_btn = driver.find_element(
        By.XPATH,
        "//span[text()='Wishlist' or text()='WISHLIST']/ancestor::button"
    )
    wishlist_btn.click()
    print("Added to Wishlist Successfully ❤️")
except:
    print("Wishlist button not found (layout may be different).")

time.sleep(5)
driver.quit()