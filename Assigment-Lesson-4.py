from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = "C:\\Users\morant\Downloads\Selenium\chromedriver.exe"
firefox_path = "C:\\Users\morant\Downloads\Selenium\geckodriver.exe"

chrome_driver = webdriver.Chrome(executable_path=chrome_path)
firefox_driver = webdriver.Firefox(executable_path=firefox_path)

# 1.  Write a script which will open the following:
chrome_driver.get("https://www.walla.co.il")
firefox_driver.get("https://www.ynet.co.il")

# 2. In one of the browsers you open do the following:
#    a. Create a variable with the website’s title
walla_a = chrome_driver.title
print(f"{walla_a}")  # וואלה! NEWS - האתר המוביל בישראל - עדכונים מסביב לשעון
#    b. Refresh website
chrome_driver.refresh()
#    c. Get website name and compare it to the variable you created in clause 1.
walla_c = chrome_driver.title
print(f"{walla_c}")
print(walla_a == walla_c)  # True

chrome_driver.close()
firefox_driver.close()

# 3. Open a few browsers, locate any element, does the element has the same locators in the other browser?
# answer: yes
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
firefox_driver = webdriver.Firefox(executable_path=firefox_path)
chrome_driver.get("http://www.python.org")
firefox_driver.get("http://www.python.org")
chrome_driver.find_element_by_id("id-search-field")
firefox_driver.find_element_by_id("id-search-field")

chrome_driver.close()
firefox_driver.close()

# 4. Create a test with the following:
#       Open Google Translate web page
#       Write anything in Hebrew in the text area
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://translate.google.co.il/?")
element = chrome_driver.find_element_by_class_name("er8xn")
element.send_keys("שלום")
chrome_driver.close()

# 5. Open Youtube web page
#  - Type a name of a song
#  - Click on search.
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://www.youtube.com")
youtube = chrome_driver.find_element_by_id("search")
youtube.send_keys("led zeppelin stairway to heaven")
youtube.send_keys(Keys.ENTER)
chrome_driver.close()

# 6. Open Chrome browser on Google Translate website: https://translate.google.com/
#  - Find translation text field (the one you send keys to)
#     with 3 different locators and print the WebElement you created.
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://translate.google.com/#he/en")
element = chrome_driver.find_element_by_class_name("er8xn")
# element = chrome_driver.find_element_by_link_text("Source text")
element.send_keys("שלום")

# text_output = chrome_driver.find_element_by_id('c16')

output1 = chrome_driver.find_element_by_xpath("//*[@data-initial-value='*']")
print("Translated Paragraph:=> " + output1.text)

# 7. Open Chrome browser on Facebook website https://www.facebook.com/
#     Login into Facebook (No need to send me credentials).
# pass name login
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://www.facebook.com/")
chrome_driver.find_element_by_name("email").send_keys("username")
chrome_driver.find_element_by_name("pass").send_keys("password")
submit = chrome_driver.find_element_by_id("loginbutton")
submit.click()
chrome_driver.close()

# 8. Open Chrome browser on any webpage.
#     - Delete all cookies from browser.
#     - Make sure all cookies are deleted by printing all cookies stored in the browser.
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://www.facebook.com/")
all_cookies = chrome_driver.get_cookies()
print(f"cookies: {all_cookies}")
chrome_driver.delete_all_cookies()
all_cookies = chrome_driver.get_cookies()
print(f"cookies: {all_cookies}")
chrome_driver.close()

# 9. Open any browser on "Github" website https://github.com/
#    - Enter “Selenium” keyword in search textfield
#    - Press Enter to search (through code - of course).
chrome_driver = webdriver.Chrome(executable_path=chrome_path)
chrome_driver.get("https://github.com/")
github = chrome_driver.find_element_by_name("q")
github.send_keys("Selenium")
github.send_keys(Keys.ENTER)
continue_link = chrome_driver.find_elements_by_partial_link_text("SeleniumHQ")
chrome_driver.close()

# 10. Find a way to disable all extensions in
#      - Chrome
#      - Firefox
#      - Internet Explorer.
#      - Run browsers without extensions.


from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("start-maximized")
browser = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)
browser.get("https://github.com/")

from selenium.webdriver.firefox.options import Options

firefox_option = Options()
firefox_option.add_argument("--disable-extensions")
firefox_browser = webdriver.Firefox(options=firefox_option, executable_path=firefox_path)
firefox_browser.get("https://github.com/")

from selenium.webdriver.ie.options import Options

ie_driver = webdriver.Ie(executable_path="C:\\Users\morant\Downloads\Selenium\IEDriverServer.exe")
ie_option = Options()
ie_option.add_argument("--disable-extensions")
ie_driver.get_cookies("https://github.com/")
