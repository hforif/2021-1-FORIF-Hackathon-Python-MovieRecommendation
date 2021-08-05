from selenium import webdriver
import time


url_login = 'https://nid.naver.com/nidlogin.login'
id = ''  # 네이버 아이디 입력
pw = ''  # 네이버 비번 입력

driver = webdriver.Chrome('/Users/seolyumin/chromedriver')  # 크롬드라이버 위치 입력
driver.get(url_login)
driver.implicitly_wait(2)

# execute_script 함수 사용하여 자바스크립트로 id,pw 넘겨주기
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

# 로그인 버튼 클릭하기
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)

# 브라우저 등록 / 등록 안 함
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/fieldset/span[2]/a').click()
time.sleep(1)

base_url = 'https://serieson.naver.com/movie/categoryList.nhn?categoryCode=100005&orderType=sale&sortingType=&mobileYn=&drmFreeYn=&freeYn=&discountYn=&tagCode=1&page={}'

comment_list = []
for page in range(1, 2):
    url = base_url.format(page)
    driver.get(url)
    time.sleep(3)
    for ul in range(1, 6):
        for li in range(1, 6):
            driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/div/ul[" + str(ul) + "]/li[" + str(li) + "]/a").click()
            title = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/h2").text
            rate = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/em").text
            plot = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[4]").text
            comment_list.append([title.replace("HD(1080) 19 ", "").replace("HD(1080) ", "").replace("19 ", ""), rate, plot])
            driver.back()
            time.sleep(1)

df = pd.DataFrame(comment_list, columns=['title', 'rate', 'plot'])
df.to_csv('navercommenttt.csv', encoding='utf-8', index=False)
file1 = pd.read_csv('navercommenttt.csv')
print(file1)