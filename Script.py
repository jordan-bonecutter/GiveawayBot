from selenium import webdriver

myName = "Jordan Bonecutter\t"
myEmail = "jordanbonecutter@gmail.com"

website = 'https://gleam.io/kymJb/technobuffalo-and-speck-cases-iphone-xs-giveaway?l=https%3A%2F%2Fwww.technobuffalo.com%2F2018%2F09%2F18%2Fspeck-iphone-xs-giveaway%2F' 
try:
    driver = webdriver.Safari()
except:
    print("Driver is busy, close and reopen the last used instance of Safari")
    quit()
driver.get(website)

#click the button
buttonPath = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[1]/div/ul/li[1]/a/i' 
button = driver.find_element_by_xpath(buttonPath)
button.click()

#login
textviewPath = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[2]/div/form/fieldset[2]/div[2]/div/div/div[1]/div' 
textview = driver.find_element_by_xpath(textviewPath)
textview.send_keys(myName)
textview.send_keys(myEmail)


#click the login button
buttonPath = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[2]/div/form/div/span[1]/button'
button = driver.find_element_by_xpath(buttonPath)
button.click()


#click the buttons!
timeButtons = ['//*[@id="em3626435"]/a/span[1]/span/span', '//*[@id="em3626437"]/a/span[1]/span/span', '//*[@id="em3626438"]/a/span[1]/span/span']
for timeButton in timeButtons:
    try:
        button = driver.find_element_by_id(timeButton)
        button.click()
    except:
        print('Invalid xpath!\n\n')

