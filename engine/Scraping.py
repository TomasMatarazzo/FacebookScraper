
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import os
import time
import random
import pandas as pd
from engine.const import estados, estados_excel, categories
from engine.Extract import *
from pathlib import Path

#Remember in case there is no category
class Scraping:

    def __init__(self):
        self.url = ""


    def FindPage(self, arg1, arg2):

        try:
            #Starting de chrome driver

            marketplace = 'https://mobile.facebook.com/marketplace/'


            #Handling notifications

            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            chrome_options.add_experimental_option("prefs",prefs)

            #Specify the paht

            driver = webdriver.Chrome('C:/Users/tomas/Desktop/chromedriver.exe',chrome_options=chrome_options)

            #Later we will check with mobile-facebook

            driver.get('https://www.facebook.com')
            driver.maximize_window()
        except :
            print("Error1")


        try:
            #Login the user
            #Here we will need to create a random user

            username =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'email']")))
            password =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'pass']")))

            username.clear()
            username.send_keys('tomasm2008@hotmail.es')
            password.clear()
            password.send_keys('taekwondo2013')
            #Select on login button

            button =  WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type ='submit']")))
            button.click()

        except:
            print('Error2')


        try:
            # Going to the facebok marketplace
            #Here we select the location and filters
            time.sleep(10)
            driver.get(marketplace)
            time.sleep(10)
            i = arg1
            j = arg2
            state = estados[i]
            category = categories[j]

            url = marketplace + state + category

            a = datetime.datetime.now()
            url2 = str(a.strftime('%y-%m-%d-%H:%M:%S'))
            url_excel = estados_excel[1] + state + url2
            url_excel = url_excel.replace('/', '-')
            url_excel = url_excel.replace(':', '-')
            print(url_excel)

            driver.get(url)
        except:
            print("Error3")

        if 1:
            #Searching all the elements and saving it on a list
            time.sleep(random.randint(1,3))

            n_scrolls = 2

            print(marketplace + 'item/')
            for n in range(1,n_scrolls):
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)
                elements = driver.find_elements(By.CSS_SELECTOR, "a[class = '_9_7 _643_'] ")
                for element in elements:
                    src = [e.get_attribute('href') for e in elements]
                elements = [ e for e in src if str(e).startswith(marketplace + 'item/')]
                elements = list(set(elements))

        #Here is all the information

        info = []
        print(len(elements))
        i = 1
        for e in elements:
            i = i + 1
            if i < 5 :
                info.append(self.Extract(e,driver))
                print('-----\n')
            else:
                print('-listo')

        return info

    def Extract(self, url,driver):

            driver.get(url)
            information = {
                'link': url,
                'Title': '-',
                'Price': '-',
                'Profile': '-',
                'Description': '-',
                'Address': '-',
                'phone': '-',
                'email': '-'
            }
            # Searching the information for each item of the dic
            # Finding url
            information['link'] = url;
            time.sleep(2)

            # Finding the Title and price
            elements = driver.find_elements(By.CSS_SELECTOR,
                                            "div[class = '_59k _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt'] ")
            information['Title'] = elements[0].text
            information['Price'] = elements[1].text
            time.sleep(2)

            # Finding the name of the profile

            parent = driver.find_elements(By.CSS_SELECTOR, "div[class = '_9_7 _2rgt _1j-f _2rgt']")
            parent = [e.text for e in parent if e.text != '']
            if len(parent) >= 5:
                name = parent[5].split("\n")

            # In case it apppers a notification
            if name[0] == 'Seller Information':
                parent.pop(5)
            name = parent[5].split("\n")
            print(name)
            print('----')
            information['Profile'] = name[0]
            time.sleep(2)

            # Finding the description

            # This variable has all the information we will split to get better info
            data = parent[2]
            data = parent[2].split('\n')
            print(data)
            print('----')
            data = [data[i] for i in range(3, len(data))]
            time.sleep(2)

            # Description
            description = ' '.join(data)
            information['Description'] = description
            time.sleep(2)

            # Phone number
            for number in data:
                print(number)

            # Location
            time.sleep(2)
            location = driver.find_element(By.CSS_SELECTOR, "div[class = 'profileMapTile']")
            image = location.value_of_css_property('background-image')
            image = image[4:-1]
            print(information)
            return information

    def createExcel(self,info):

            #Create the folder where you will put the paths.
            df = pd.DataFrame(info)
            temp = str(Path(__file__).parent.absolute())
            df.to_excel(temp + '.xlsx')