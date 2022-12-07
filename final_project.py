# #########################################
# ##### Name: Haolin Dong #####
# ##### Uniqname: haolind #####
# #########################################

# def control_flow():
#     keyword=input("Please enter keywords: ")
#     location=input("Please enter country name: ")
#     classNification=input("Please enter classNification name: ")
#     ifcompare=input("Please enter if you make comparison [y/n]: ")
#     url_head="https://app.ticketmaster.com/discovery/v2/events.json?"
#     url_tail="apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
#     if keyword!="":
#         url_head=url_head+"keyword="+keyword+"&"


# import time
# from seleniumwire import webdriver
# from seleniumwire.utils import decode
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# import json

# svc=  Service(GeckoDriverManager().install())
# options = {
#     'disable_encoding': True  # Ask the server not to compress the response
# }
# profile = webdriver.FirefoxProfile()
# webdriver.Chrome
# driver = webdriver.Firefox(service=svc, seleniumwire_options=options, firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")
# driver.get("https://www.ticketmaster.com/pistons-vs-clippers-saddiq-bey-bobblehead-presented-by-bally-sports/event/08005D0BF0B74785?refArtist=K8vZ91718T7")
# button=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[8]/div/div/div/div[3]/div/div/button")))
# button.click()
# for request in driver.requests:
#     if request.response and "offeradapter" in request.url:
#         print(request.url)
#         print(request.response.body)
#         print("")



from flask import Flask
from flask import Flask, render_template, request
import secret
import json
import requests as rq
app_final=Flask(__name__)

# @app_final.route('/table/<nm>')
# def table(nm):
#     return render_template('table.html', name=nm)  

class EventClass:
    def __init__(self,name,city,eventdate,salestart,presaledate,id,url,img,pricemin,currency,pricemax):
        self.name=name
        self.city=city
        self.eventdate=eventdate
        self.salestart=salestart
        self.presaledate=presaledate
        self.id=id
        self.url=url
        self.img=img
        self.pricemin=pricemin
        self.currency=currency
        self.pricemax=pricemax


def data_process(APIData):
    for i in APIData["_embedded"]["events"]:
        # print(i.keys())
        # print(i["_embedded"].keys())
        print("name: ",i["name"])
        print("city: ",i["_embedded"]["venues"][0]["city"]['name'])
        print("eventdate: ",i["dates"]["start"]["localDate"])
        print("salestart: ",i["sales"]["public"]["startDateTime"])
        print("presaledate: ",i["sales"]["presales"][0]["startDateTime"])
        print("id: ",i["id"])
        print("url: ",i["url"])
        print("img: ",i["images"][0]['url'])
        print("pricemin: ",i["priceRanges"][0]["min"])
        print("pricemin: ",i["priceRanges"][0]["currency"])
        print("pricemax: ",i["priceRanges"][0]["max"])

def api_search(keyword,city, classN):
    base_str="https://app.ticketmaster.com/discovery/v2/events.json?"
    end_str="apikey="+secret.api_key
    if len(keyword)!=0:
        key_str="keyword="+keyword+"&"
    else:
        key_str=""
    if len(city)!=0:
        city_str="city="+city+"&"
    else:
        city_str=""
    if len(classN)!=0:
        classN_str="classN="+classN+"&"
    else:
        classN_str=""
    # search_str=base_str+key_str+city_str+classN_str+end_str
    search_str="https://app.ticketmaster.com/discovery/v2/events.json?keyword=lakers&city=new%20york&classN=sports&apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
    response=rq.get(search_str)
    APIData=json.loads(response.text)
    # print(search_str)
    data_process(APIData)
    # print(APIData)
    return str(len(APIData))

def load_history(keyword,city, classN):
    pass

@app_final.route('/input/<nm>')
def input(nm):
    return render_template('input.html', name=nm)  

@app_final.route('/table', methods=['POST','Get'])
def handle_the_form():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        artist=request.form["artist"]
        
        venue=request.form["venue"]
        classN=request.form["classN"]
        op=request.form["op"]
        # print(artist)
        # print(venue)
        # print(classN)
        # print(op)
        # print(len(artist)) # if len==0, then artist no input
        if op=="Search":
            APIData=api_search(artist,venue, classN)
        elif op=="History":
            APIData=load_history(artist,venue, classN)
        else:
            return "Operation code ERROR!"
        return render_template('table.html', name=APIData, venue=venue, classN=classN, op=op) 

if __name__ == '__main__':
    print("Starting Flask app")
    app_final.run(debug=True)

