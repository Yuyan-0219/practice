from selenium import webdriver

weB=webdriver.Chrome("chromedriver.exe")

urL="https://ecshweb.pchome.com.tw/search/v3.3/?q=%E6%B3%A1%E9%BA%B5"
weB.maximize_window()

weB.implicitly_wait(10)
weB.get(urL)


for mySoup in weB.find_elements_by_tag_name("dl"):
    try:
        print(mySoup.find_element_by_class_name("prod_name").text)
        print(mySoup.find_element_by_class_name("value").text)
        print(mySoup.find_element_by_tag_name("a").get_attribute("href"))
        print("----------------------------------------")
    except:
        continue

weB.close()
