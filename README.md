## Environment Setup:

 - FireFox 59.0
 - geckodriver
 - Python packages: selenium==3.14, seleniumwire, flask, pickle, requests


## Get Started:

1. intall all required python packages
2. intall FireFox browser, set `geckodriver.exe` into system `$PATH` 
3. set your api_key in secret.py


## Command to run:

```python final_project.py```

## File Organization:

 - templates/input.html: flask html for starter page
 - templates/table.html: flask html for event info
 - templates/ticket.html: flask html for ticket details
 - final_project.py: main script
 - history_tree.json: tree structure of search history
 - secret.py: file to save your API key
 - *.log: cached files of search results

 ## Demo Link:

    https://drive.google.com/file/d/1xhVn0F9qYupKNtRe32jpwc44U37yGYCX/view?usp=sharing

 ## Date Structure:

    True structure is used to save search history. It's a three-level tree, and the key of each level represents keyword, city, and classification separately. The value of the leaf is the cached file name. One example of the tree is shown below.

    ```
    [['lakers', ['', ['', 'lakers___1670479123.4224408.log']], 
                ['atlanta', ['', 'lakers_atlanta__1670479214.3113055.log'], 
                            ['sports', 'lakers_atlanta_sports_1670479224.87233.log']], 
    ['', ['orlando', ['', '_orlando__1670479238.7372603.log']]]]]
    ```


