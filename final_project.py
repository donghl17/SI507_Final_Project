# #########################################
# ##### Name: Haolin Dong #####
# ##### Uniqname: haolind #####
# #########################################

# # import json
# # import requests as rq
# # # a="https://app.ticketmaster.com/discovery/v2/events.json?keyword=BlackPink&source=universe&countryCode=US&apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
# # a="https://app.ticketmaster.com/discovery/v2/events/0A005D2C11E74A11.json?apikey=YAzeD7JmDWcJipX6Q3XEnAhJZMjxqBSA"
# # response=rq.get(a)
# # RedliningData=json.loads(response.text)
# # print(RedliningData)

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

