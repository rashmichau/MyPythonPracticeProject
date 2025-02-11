
from selenium import webdriver
import time

# FOR CHROME
'''driver = webdriver.Chrome()

driver.get("https://www.google.com")


print(driver.title)
time.sleep(60)

driver.quit()'''

'''from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(90)
print(driver.title)

driver.quit()'''

#FOR EDGE
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

'''driver=webdriver.Edge()
driver.get("https://www.google.com")
time.sleep(30)'''


#FIREFOX
'''driver=webdriver.Firefox()
driver.get("https://www.google.com")
time.sleep(23)'''