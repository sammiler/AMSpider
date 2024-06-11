import time

# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup           # 网页解析


from selenium.webdriver import Keys, DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True


service = Service(executable_path='C:\\Users\\sammiler\\MyFile\\ChromeDriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.set_capability("desired:capabilities",desired_capabilities)
driver = webdriver.Chrome(service=service, options=options)

# 创建浏览器实例
driver.maximize_window()
# 打开网页

url = 'https://music.apple.com/us/artist/led-zeppelin/994656'

driver.get(url)

time.sleep(10)
albumset = set()
urlSet = set()
if url.find("full-albums") != -1:
    action = ActionChains(driver)

    divele = driver.find_element(By.XPATH,"//*[@id=\"scrollable-page\"]/main/div")

    # 600根据自己电脑调，目的是点击右边的空白
    action.move_to_element_with_offset(divele,600,0).click().perform()

    scrollLimit = 0
    reached_page_end = False
    singleRun = True
    last_height = driver.execute_script("return document.body.scrollHeight")
    while not reached_page_end:
        if scrollLimit > 0:
            scrollLimit = scrollLimit + 1
        if scrollLimit == 10:
            reached_page_end = True
        driver.find_element(By.XPATH,'//body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            if singleRun:
                scrollLimit = scrollLimit + 1
                singleRun = False
        else:
            last_height = new_height

    time.sleep(2)
    get_html = "Artist.html"
    # 打开文件，准备写入
    f = open(get_html, 'wb')
    # 写入文件
    f.write(driver.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
    print('写入成功')
    # 关闭文件
    f.close()
    htmlfile = open("Artist.html", 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    for item in soup.find_all('a',{'class':'product-lockup__link svelte-1b4jqbu'}):
      albumset.add(item['href'])
    print(len(albumset))
    outPutFile = "Artist.txt"
    outFile = open(outPutFile,"wb")
    outFile.truncate()
    outFile.seek(0)
    spaceStr = "\n"
    for item in albumset:
        print(item)
        outFile.write(str(item).encode('utf-8'))
        outFile.write(spaceStr.encode('utf-8'))
else:
    action = ActionChains(driver)
    scrollMap = driver.find_element(By.XPATH,"//*[@id=\"scrollable-page\"]/main/div/div[5]/div/div[2]/section/div[1]/ul")
    action.move_to_element(scrollMap).move_by_offset(600,0).click().perform()
    time.sleep(5)
    get_html = "Artist.html"
    # 打开文件，准备写入
    f = open(get_html, 'wb')
    # 写入文件
    f.write(driver.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
    print('写入成功')
    # 关闭文件
    f.close()
    htmlfile = open("Artist.html", 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    for item in soup.find_all('div',{'class':'section svelte-gla0uw','aria-label':'Albums'}):
        for albumItem in item.find_all('a',{'class':'product-lockup__link svelte-1b4jqbu'}):
            albumset.add(albumItem['href'])
    print(len(albumset))
    outPutFile = "Artist.txt"
    outFile = open(outPutFile,"wb")
    outFile.truncate()
    outFile.seek(0)
    spaceStr = "\n"
    for item in albumset:
        print(item)
        outFile.write(str(item).encode('utf-8'))
        outFile.write(spaceStr.encode('utf-8'))


