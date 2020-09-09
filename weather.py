from selenium import webdriver
driver = webdriver.Chrome()  #创建浏览器实例对象，打开浏览器
driver.maximize_window()  #把浏览器最大化
driver.get('http://www.weather.com.cn/html/province/xinjiang.shtml')

# ele=driver.find_element_by_id('forecastID')
# citys=ele.find_elements_by_tag_name('dl')
citys=driver.find_elements_by_css_selector('#forecastID dl')
l=[]
for i in citys:
    name=i.text.split('\n')[0]
    lweather=int(i.text.split('/')[-1].replace('℃',''))
    l.append((name,lweather))
print(l)
lowest=40
lwCity=[]
for j in l:
    if j[1]<lowest:
        lowest=j[1]
        lwCity=[j[0]]
    elif j[1]==lowest:
        lwCity.append(j[0])
print('最低温度为：%d℃，最低温度最低的城市有：%s'%(lowest,' '.join(lwCity)))
print('f最低温度为：{lowest}℃，最低温度最低的城市有：{" ".join(lwCity)}')
driver.quit()