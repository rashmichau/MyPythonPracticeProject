
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
'''from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by  import By

options=Options()
options.add_experimental_option("detach",True)
service=Service(EdgeChromiumDriverManager().install())

driver=webdriver.Edge(service=service,options=options)
driver.maximize_window()

driver.get("https://www.google.com")
#page_source=driver.page_source
#print(page_source)
print(driver.get_window_position(windowHandle="current"))
print(driver.get_window_rect())
print(driver.get_window_size())


#By XPATH
# input= driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
# input.send_keys("Facebook")
#by Class
# input=driver.find_element(By.CLASS_NAME,'gLFyf').send_keys("Amezon")

#By Id
# input=driver.find_element(By.ID,'APjFqb').send_keys("Facebook")

#By Name
#input=driver.find_element(By.NAME,'q').send_keys("Myntra")

#By Tag_name
# input=driver.find_element(By.TAG_NAME,'textarea').send_keys("Myntra")

# search=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
# search.click()'''

# WEB SCRAPING
#Fatching Details of single element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

'''options=Options()
options.add_experimental_option("detach",True)

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://www.flipkart.com/watches/pr?sid=r18")

watch_name=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]")
name=watch_name.text

watch_price=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/a[2]/div/div[1]')
price=watch_price.text

watch_mrp=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[2]')
MRP=watch_mrp.text

watch_disc=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div[1]/div[3]/span')
discount=watch_disc.text

watch_delivery=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div[2]/div/div')
delivery=watch_delivery.text
print('____________________________________________________________________')
print("watch_name :",name)
print('watch_price :', price)
print("MRP price :",MRP)
print("Total_Discount :",discount)
print("Delivery :",delivery)
print('--------------------------------------------------------------------')'''


options = Options()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.flipkart.com/watches/casio~brand/pr?sid=r18&sort=price_asc")

for j in range(2,12):
    for i in range(1,5):
        watch_name = driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/div[1]")
        name = watch_name.text

        watch_price = driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/a[2]/div[1]/div")
        price = watch_price.text

        watch_fullname = driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/a[1]")
        Full_name = watch_fullname.text

        delivery=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/a[2]/div[2]/div/div")
        Delivery_status=delivery.text
        print('____________________________________________________________________')
        print("watch_name :", name)
        print('watch_price :', price)
        print("Full_name :", Full_name)
        print("Delivery_status :",Delivery_status)




