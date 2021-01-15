from selenium.webdriver.common.keys import Keys
import time

def run_session(driver):
    driver.get("https://www.flipkart.com/") 
    time.sleep(3)

    #Close initial pop-up
    try:
        driver.find_element_by_css_selector('body > div._2Sn47c > div > div > button').click()
    except:
        print('Error! Pop-up Close Not Found!')
        driver.quit()
        return "Error"
    time.sleep(1)
    #Search product
    try:
        search_bar = driver.find_element_by_css_selector('#container > div > div._1kfTjk > div._1rH5Jn > div._2Xfa2_ > div._1cmsER > form > div > div > input')
        search_bar.send_keys("Samsung Galaxy S10")
    except:
        print('Error! Can not find searchbar')
        driver.quit()
        return "Error"
    time.sleep(1)
    #click on Category--> Mobile
    
    try:
        driver.find_element_by_css_selector('div._2Xfa2_ > div._1cmsER > form > ul > li:nth-child(1)').click()
    except:
        print('Error! Mobile Category Element Not Found')
        driver.quit()
        return "Error"
    time.sleep(3)
    #click on FlipKart Assured
    try:
        driver.find_element_by_css_selector('#container > div > div._3LxdjL._3NzWOH > div._3FqKqJ > div.E2-pcE._3zjXRo > div:nth-child(1) > div > div:nth-child(1) > div > section._2hbLCH._24gLJx > div._2iDkf8.shbqsL > label > div._3879cV').click()
        print('clicked on FKA')
    except:
        print('Error! Flipkart Assured Element Not Found')
        driver.quit()
        return "Error"
    time.sleep(3)
    #click on Samsung
    try:
        driver.find_element_by_css_selector('#container > div > div._3LxdjL._3NzWOH > div._3FqKqJ > div > div:nth-child(1) > div > div:nth-child(1) > div > section:nth-child(6) > div._3FPh42 > div > div > div > div > label > div._3879cV').click()
        print('Clicked on Samsung')
    except:
        print('Error! Samsung Checkbox Element Not Found')
        driver.quit()
        return "Error"
    time.sleep(3)
    #select price high to low
    try:
        driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[4]').click()
    except:
        print('Error! Element High to Low Not Found')
        driver.quit()
        return "Error"
    time.sleep(3)
    #get list
    try:
        product_price = driver.find_elements_by_css_selector('div._30jeq3._1_WHN1')
    except:
        print('Error! Unable to Fetch Prices')
        driver.quit()
        return "Error"
    try:
        product_url = driver.find_elements_by_class_name('_1fQZEK')
    except:
        print('Error! Unable to Fetch URLs')
        driver.quit()
        return "Error"
    try:
        product_name = driver.find_elements_by_class_name('_4rR01T')
    except:
        print('Error! Unable to Fetch Names')
        driver.quit()
        return "Error"
    print(len(product_url),len(product_price),len(product_name))


    for i in range(0,len(product_url)-1):
        print('----------------------------------------------------------')
        print('Name:'+str(product_name[i].text)+'\n'+'Price:'+ (product_price[i].text).encode("utf-8")+'\n'+'URL:'+str(product_url[i].get_attribute('href'))+'\n')
        

    driver.quit()
    return "Test Completed"
