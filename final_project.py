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


import time
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from flask import Flask
from flask import Flask, render_template, request
import secret
import json
import requests as rq
app_final=Flask(__name__)
APIData=None
history_tree=[]


class TicketClass:
    def __init__(self,eventid,currency_list,min_list,max_list,count_list):
        self.eventid=eventid
        self.currency_list=currency_list
        self.min_list=min_list
        self.max_list=max_list
        self.count_list=count_list

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
    class_list=[]
    for i in APIData["_embedded"]["events"]:
        # print(i.keys())
        # print(i["_embedded"].keys())
        # print("name: ",i["name"])
        # print("city: ",i["_embedded"]["venues"][0]["city"]['name'])
        # print("eventdate: ",i["dates"]["start"]["localDate"])
        # print("salestart: ",i["sales"]["public"]["startDateTime"])
        # print("presaledate: ",i["sales"]["presales"][0]["startDateTime"])
        # print("id: ",i["id"])
        # print("url: ",i["url"])
        # print("img: ",i["images"][0]['url'])
        # print("pricemin: ",i["priceRanges"][0]["min"])
        # print("pricemin: ",i["priceRanges"][0]["currency"])
        # print("pricemax: ",i["priceRanges"][0]["max"])
        if "priceRanges" not in i.keys() and "presales" not in i["sales"].keys():
            tmp=EventClass(i["name"],i["_embedded"]["venues"][0]["city"]['name'],i["dates"]["start"]["localDate"],i["sales"]["public"]["startDateTime"],"N/A",i["id"],i["url"],i["images"][0]['url'],"N/A","N/A","N/A")

        elif "priceRanges" not in i.keys():
            tmp=EventClass(i["name"],i["_embedded"]["venues"][0]["city"]['name'],i["dates"]["start"]["localDate"],i["sales"]["public"]["startDateTime"],i["sales"]["presales"][0]["startDateTime"],i["id"],i["url"],i["images"][0]['url'],"N/A","N/A","N/A")
        elif "presales" not in i["sales"].keys():
            tmp=EventClass(i["name"],i["_embedded"]["venues"][0]["city"]['name'],i["dates"]["start"]["localDate"],i["sales"]["public"]["startDateTime"],"N/A",i["id"],i["url"],i["images"][0]['url'],i["priceRanges"][0]["min"],i["priceRanges"][0]["currency"],i["priceRanges"][0]["max"])
        else:
            tmp=EventClass(i["name"],i["_embedded"]["venues"][0]["city"]['name'],i["dates"]["start"]["localDate"],i["sales"]["public"]["startDateTime"],i["sales"]["presales"][0]["startDateTime"],i["id"],i["url"],i["images"][0]['url'],i["priceRanges"][0]["min"],i["priceRanges"][0]["currency"],i["priceRanges"][0]["max"])
        class_list.append(tmp)
    return class_list

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
    search_str=base_str+key_str+city_str+classN_str+end_str
    # search_str="https://app.ticketmaster.com/discovery/v2/events.json?keyword=lakers&city=new%20york&classN=sports&apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
    response=rq.get(search_str)
    APIData=json.loads(response.text)
    # print(APIData)
    class_list=data_process(APIData)
    # print(APIData)
    return class_list

def check_details(url_in):
    svc=  Service(GeckoDriverManager().install())
    options = {
        'disable_encoding': True  # Ask the server not to compress the response
    }
    profile = webdriver.FirefoxProfile()
    webdriver.Chrome
    driver = webdriver.Firefox(service=svc, seleniumwire_options=options, firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")
    driver.get(url_in)
    # driver.get("https://www.ticketmaster.com/pistons-vs-clippers-saddiq-bey-bobblehead-presented-by-bally-sports/event/08005D0BF0B74785?refArtist=K8vZ91718T7")
    button=WebDriverWait(driver,80).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[8]/div/div/div/div[3]/div/div/button")))
    button.click()
    for request in driver.requests:
        if request.response and "offeradapter" in request.url and "listpricerange" in request.url:
            print(request.url)
            # print(json.loads(request.response.body))
            ticket_dict=json.loads(request.response.body)
            
            print(ticket_dict["eventId"])
            eventid=ticket_dict["eventId"]
            currency_list=[]
            min_list=[]
            max_list=[]
            count_list=[]
            for i in ticket_dict["facets"]:
                currency_list.append(i["listPriceRange"][0]["currency"])
                min_list.append(i["listPriceRange"][0]["min"])
                max_list.append(i["listPriceRange"][0]["max"])
                count_list.append(i["count"])
            # print("currency: ",currency_list[0:10])
            # print("min_price: ",min_list[0:10])
            # print("min_price: ",max_list[0:10])
            # print("count: ",count_list[0:10])
            ticket_obj=TicketClass(eventid,currency_list,min_list,max_list,count_list)
            return ticket_obj
    return None

# [[artist,[venue,[classN,file_name]]],
#  [artist,[venue,[classN,file_name],
#                 [classN,file_name]]] ]

def save_results(APIData,artist,venue, classN):
    global history_tree
    file_name=artist+"_"+venue+"_"+classN+"_"+str(time.time())
    if len(history_tree)==0:
        history_tree.append([artist,[venue,[classN,file_name]]])
    else:
        found=False
        for i in history_tree:
            if i[0]==artist:
                for j in i[1:]:
                    if j[0]==venue:
                        for k in j[1:]:
                            if k[0]==classN:
                                k[1]=file_name#overwrite
                                found=True
                                break
                        if found==False:
                            j.append([classN,file_name])
                            found=True
                if found==False:
                    i.append([venue,[classN,file_name]])
                    found=True
        if found==False:
            i.append([artist,[venue,[classN,file_name]]])
            found=True
    print(history_tree)
    f=open("history_tree.json","w")
    f.write(str(history_tree))
    f.close()
    
                        
                            
                        

def load_history(keyword,city, classN):
    global history_tree
    pass

@app_final.route('/input')
def input():
    return render_template('input.html')  

@app_final.route('/table', methods=['POST','Get'])
def handle_the_form():
    global history_tree
    global APIData
    if request.method == 'GET':
        return f"The URL /table is accessed directly. Try going to '/input' to submit form"
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
            save_results(APIData,artist,venue, classN)
        elif op=="History":
            APIData=load_history(artist,venue, classN)
        else:
            return "Operation code ERROR!"
        return render_template('table.html', name=len(APIData), x=APIData) 

@app_final.route('/ticket', methods=['POST','Get'])
def ticket_handle():
    global APIData
    # print(APIData)
    if request.method == 'GET':
        return f"The URL /ticket is accessed directly. Try going to '/table' to submit form"
    if request.method == 'POST':
        spe_event=request.form["detail"]
        for i in APIData:
            if spe_event==i.name:
                ticket_obj=check_details(i.url)
                # currency_list,min_list,max_list,count_list):
                return render_template('ticket.html', name=len(ticket_obj.count_list), event=spe_event, count_list=ticket_obj.count_list,min_list=ticket_obj.min_list, max_list=ticket_obj.max_list, currency_list=ticket_obj.currency_list) 
        return f"The event name doesn't exist. Try going to '/table' to submit form"


if __name__ == '__main__':
    print("Starting Flask app")
    app_final.run(debug=True)

