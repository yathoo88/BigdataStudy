from selenium import webdriver
url = "https://nid.naver.com/nidlogin.login"
data = {

}
# PhantomJS 드라이버 추출하기 --- (※1)
browser = webdriver.PhantomJS()
# 3초 대기하기 --- (※2)
browser.implicitly_wait(3)

# URL 읽어 들이기 --- (※3)
browser.get(url)

####네이버 메일 login
elemnet_id = browser.find_element_by_id("id") #id 입력 상자
elemnet_id.clear()
elemnet_id.send_keys("yathoo88")
elemnet_pw = browser.find_element_by_id("pw") #password 입력
elemnet_pw.clear()
elemnet_pw.send_keys("jenhs0186")
# 화면을 캡처해서 저장하기 --- (※4)
browser.save_screenshot("WebsiteLogin.png")
#login버튼 클릭
button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()




#### 메일 페이지 열기
browser.get("http://mail.naver.com")
browser.save_screenshot("naverMail.png")
titles = browser.find_elements_by_css_selector("strong.mail_title")
for title in titles :
    print("=====", title.text)




# 브라우저 종료하기 --- (※5)
browser.quit()