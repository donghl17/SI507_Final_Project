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
from flask import Flask
from flask import Flask, render_template
import secret
app_final=Flask(__name__)

@app_final.route('/table/<nm>')
def table(nm):
    return render_template('table.html', name=nm)  


@app_final.route('/input/<nm>')
def input(nm):
    return render_template('input.html', name=nm)  

if __name__ == '__main__':
    print("Starting Flask app")
    app_final.run(debug=True)

# import time
# from selenium import webdriver

# profile = webdriver.FirefoxProfile()
# driver = webdriver.Firefox(firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")
# driver.get("https://www.ticketmaster.com/detroit-pistons-vs-memphis-grizzlies-detroit-michigan-12-04-2022/event/08005D0BFC4E4F80")
# time.sleep(5)
# networkScript = """
# var network = performance.getEntries() || {};
# return network;
# """
# networkRequests = driver.execute_script(networkScript)
# print(networkRequests)