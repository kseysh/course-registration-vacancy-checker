import time
from django.http import HttpResponse

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .crawled_info.majors_list import majors
from sugang.models import *

def crawl_course_info(request):
    service = Service("/Users/transfer_kk/Desktop/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    
    url = 'https://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx?callPage=Sugang_SaveAB'
    driver.get(url)
    
    try:
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
    except Exception as e:
        print("error: " + e)
    finally:
        driver.quit()
    return HttpResponse("success!")

def crawl_course_vacancy(request):
    service = Service("/Users/transfer_kk/Desktop/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    
    try:
        driver.get('https://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx?callPage=Sugang_SaveAB')
        driver.implicitly_wait(1)
        driver.add_cookie({"name":"ITISSugang", "value":"bigo=L+0gnQBAXrw=&grade=mXv8e05CoQE=&nowno=pcTw/Y5/29A=&change_Code=iWpeROjkMjo=&ite_yn=qp7HMQ5dvNs=&pcode=G2D6xtRFEPg=&kicho=qp7HMQ5dvNs=&date14=1mhtp5MGVj4ZyGL97/iKtw==&mincredit=bOFS5/mMm6U=&maxcredit=yeQGi3jUVk8=&pre_jaesu=vP8vv5LN+dI=&date_change=qvwd1Oz5ZGqaEUebf2E/LSfGAkGF2++d&date_jaesu=tYNaCmMN8Wo=&majors=2WdbESNCge0=&major_name=qp7HMQ5dvNs=&bokhag=qp7HMQ5dvNs=&dept_code=JltGKE1I2Aw=&major_code=2WdbESNCge0="})
        driver.implicitly_wait(1)
        driver.add_cookie({"name":"ITISSugangHome", "value":"Grade=mXv8e05CoQE=&Term=9XCOn7R1QMI=&Kname=rdYyC0XmbRQaHBk04DY60A==&Dept_kname=drIw5mzH3OD3n1hdvkfNoeZYVjEPTSa5&Major_kname=drIw5mzH3ODvn8/JKmVK+g==&Manager=ccP/ybUZCSU=&Email=8DlY5mNAnBl8QkwNSuMr7/8U7pxOBfvH&Stno=6O/gxAPQyfIU9UuhsCZr9A==&Dept_code=JltGKE1I2Aw=&Major_code=2WdbESNCge0=&ClientAddress=ADz5uS4qFkj6R9jwCqq5HA==&Ename=YNTNW7TuyEi8dJr/TwcPUw==&Dept_Ename=XC9PjrV2jtMcOfESGC/kZIp5AzpLxfvv&Major_ename=XC9PjrV2jtMcOfESGC/kZIp5AzpLxfvv&pwChgPop=ccP/ybUZCSU="})
        driver.implicitly_wait(1)
        
        for major in majors[65:]:
            select = Select(driver.find_element(By.NAME, 'ddlDept'))
            major_value = major["value"]
            select.select_by_value(major_value)
            driver.find_element(By.CSS_SELECTOR, "#ibtnSearch1").click()
            rows = driver.find_elements(By.CSS_SELECTOR, '#dgList > tbody > tr')
            course_list = []
            for row in rows:
                row.find_element(By.CSS_SELECTOR, "td:nth-child(11) > input ").click()
                driver.implicitly_wait(5)
                driver.switch_to.window(driver.window_handles[1])
                rows2 = driver.find_elements(By.CSS_SELECTOR, '#dgList > tbody > tr')
                for row2 in rows2:
                    code = row2.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()
                    vacancy = row2.find_element(By.CSS_SELECTOR, "td:nth-child(8)").text.strip()
                    course,course_is_created = Course.objects.get_or_create(code = code)
                    course.vacancy = vacancy
                    if course_is_created:
                        course.name = "미정"
                        course.save()
                    else:
                        course_list.append(course)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            if course_list:
                Course.objects.bulk_update(course_list, ['vacancy'])
            print("\n-----------\n" + major["name"]+" is OK" + "\n-----------\n")   
    except NoSuchElementException as e:
        print("error: " + e.msg)
    finally:
        driver.quit()
    return HttpResponse("success!")
    