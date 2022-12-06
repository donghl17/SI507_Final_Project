# #########################################
# ##### Name: Haolin Dong #####
# ##### Uniqname: haolind #####
# #########################################

# def control_flow():
#     keyword=input("Please enter keywords: ")
#     location=input("Please enter country name: ")
#     classification=input("Please enter classification name: ")
#     ifcompare=input("Please enter if you make comparison [y/n]: ")
#     url_head="https://app.ticketmaster.com/discovery/v2/events.json?"
#     url_tail="apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
#     if keyword!="":
#         url_head=url_head+"keyword="+keyword+"&"

import time
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import json

svc=  Service(GeckoDriverManager().install())
options = {
    'disable_encoding': True  # Ask the server not to compress the response
}
profile = webdriver.FirefoxProfile()
webdriver.Chrome
driver = webdriver.Firefox(service=svc, seleniumwire_options=options, firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")
driver.get("https://www.ticketmaster.com/pistons-vs-clippers-saddiq-bey-bobblehead-presented-by-bally-sports/event/08005D0BF0B74785?refArtist=K8vZ91718T7")
button=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[8]/div/div/div/div[3]/div/div/button")))
button.click()

for request in driver.requests:
    if request.response and "offeradapter" in request.url:
        print(request.url)
        print(request.response.body)
        print("")



# from flask import Flask
# from flask import Flask, render_template
# import secret
# app_final=Flask(__name__)

# @app_final.route('/table/<nm>')
# def table(nm):
#     return render_template('table.html', name=nm)  


# @app_final.route('/input/<nm>')
# def input(nm):
#     return render_template('input.html', name=nm)  

# if __name__ == '__main__':
#     print("Starting Flask app")
#     app_final.run(debug=True)

