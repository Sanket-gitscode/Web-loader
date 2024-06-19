#simple web automation where it searches for multiple items on youtube.com

from selenium import webdriver
#importing selenium and webriver to work around webbrowser 

import time 
#importing time module to because if a website takes time to load we can delay the code to run

#webtape function 
def webtape():
    #Namel1 ie Name list 1 where you put the things you want to search or either fill in. 
    
    Namel1=["Orange","Cars","Science"]
    
    Searchingfor=""
    
    for everyelements in Namel1:
        #for iterating through every element in Namel[]
        Searchingfor=everyelements
    
        time.sleep(1)

        web=webdriver.Chrome()
        web.get('https://www.youtube.com/')

        Searchbar=Searchingfor
        fillin=web.find_element('xpath','/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
        fillin.send_keys(Searchbar)
        
        
        #Xpath of Submit button
        submitb=web.find_element('xpath','/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon/yt-icon-shape/icon-shape/div')
        submitb.click()
        
    while True:
        time.wait(100)   
       
       
        

webtape()
