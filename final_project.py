# #########################################
# ##### Name: Haolin Dong #####
# ##### Uniqname: haolind #####
# #########################################

# import json
# import requests as rq
# import time
# from selenium.webdriver.edge.options import Options
# # a="https://app.ticketmaster.com/discovery/v2/events.json?keyword=BlackPink&source=universe&countryCode=US&apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
# a="https://app.ticketmaster.com/discovery/v2/events/0A005D2C11E74A11.json?apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
# b="https://www.ticketmaster.com/blackpink-world-tour-born-pink-los-angeles-california-11-20-2022/event/0A005D2C11E74A11"
# s=rq.Session()
# time.sleep(2)
# response=s.get(a)
# time.sleep(2)
# cookies=dict(response.cookies)
# time.sleep(2)
# header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# response=s.get(b,cookies=cookies,headers=header)
# time.sleep(2)
# # RedliningData=json.loads(response.text)
# print(response.text)

# import time
# from selenium import webdriver
# # from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# driver = webdriver.Edge()
# driver.get("https://www.ticketmaster.com/blackpink-world-tour-born-pink-los-angeles-california-11-20-2022/event/0A005D2C11E74A11")
# time.sleep(5)
# networkScript = """
# var network = performance.getEntries() || {};
# return network;
# """
# networkRequests = driver.execute_script(networkScript)
# # URLs = [request['name'] for request in networkRequests if request['name'].split("/")[-1].startswith("ABC")]
# print(len(networkRequests))


# def control_flow():
#     keyword=input("Please enter keywords: ")
#     location=input("Please enter country name: ")
#     classification=input("Please enter classification name: ")
#     ifcompare=input("Please enter if you make comparison [y/n]: ")
#     url_head="https://app.ticketmaster.com/discovery/v2/events.json?"
#     url_tail="apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
#     if keyword!="":
#         url_head=url_head+"keyword="+keyword+"&"

import app
if __name__ == '__main__':
    print("Starting Flask app", app.name)
    app.run(debug=True)