import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyfiglet
from colorama import Fore, Style , init
import time
init(autoreset=True)
driver = webdriver.Chrome()
toolName = pyfiglet.figlet_format("InstaBruteForce")
print(Fore.GREEN + toolName)
print(Fore.RED + "=" * 40 + "\n")
print(Fore.YELLOW + "Welcome to InstaBruteForce 🤖\n")
print(Fore.WHITE + f"💻 Developed by:{Fore.GREEN} @ioxEyad \n")
print(Fore.WHITE + f"🐙 Github User:{Fore.GREEN} @ioxEyad \n")
print(Fore.WHITE + f"🤖 Telegram Account:{Fore.GREEN} @eyademadx \n")
print(Fore.RED + "=" * 40 + "\n")
print(Fore.RED + "=" * 40 + "\n")
if driver:
    print("Open Browser Successfully")
    driver.get("https://www.instagram.com/accounts/login/")


WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

# Close the driver after some time (optional)
# import time
time.sleep(5)
driver.quit()
