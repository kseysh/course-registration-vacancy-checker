from django.http import HttpResponse
from sugang.models import *
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from .crawled_info.majors_list import majors

def crawl_course_info(request):
    service = Service("/Users/transfer_kk/Desktop/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    
    url = 'https://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx?callPage=Sugang_SaveAB'
    driver.get(url)
    
    for major in majors:
        select = Select(driver.find_element(By.NAME, 'ddlDept'))
        major_value = major["value"]
        major_name = major["name"]
        select.select_by_value(major_value)
        driver.find_element(By.CSS_SELECTOR, "#ibtnSearch1").click()
        driver.implicitly_wait(1)
        
        rows = driver.find_elements(By.CSS_SELECTOR, '#dgList > tbody > tr')

        for row in rows:
            code = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a > font").text.strip() # 학수번호
            name = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip() # 과목명
            grade = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text.strip() # 학년
            credit = row.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text.strip() # 학점
            subject = row.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text.strip() # 과목 구분
            time_and_classroom = row.find_element(By.CSS_SELECTOR, "td:nth-child(7)").text.strip() # 시간 및 강의실
            professor = row.find_element(By.CSS_SELECTOR, "td:nth-child(8)").text.strip() # 교수
            evaluation_method = row.find_element(By.CSS_SELECTOR, "td:nth-child(9)").text.strip() # 평가 방식
            remarks = row.find_element(By.CSS_SELECTOR, "td:nth-child(10)").text.strip() # 비고
            
            try:
                course, course_is_created = Course.objects.get_or_create(
                    major_name = major_name,
                    code = code,
                    name = name,
                    grade = grade,
                    credit = credit,
                    subject = subject,
                    time_and_classroom = time_and_classroom,
                    professor = professor,
                    evaluation_method = evaluation_method,
                    remarks = remarks,
                )
            except Exception as e:
                print("error: " + e , " major value: " + major_value)
            
            if course_is_created:
                print(course.name)
    driver.quit()
    return HttpResponse("success!")