from django.http import HttpResponse

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .crawled_info.majors_list import majors
from .crawled_info.kita_majors_list import kitas
from sugang.models import *
import time


def crawl_course_info(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless') # Browser를 GUI없이 백그라운드에서 실행
    chrome_options.add_argument('--no-sandbox') # 보안 취약점에 노출될 가능성을 최소화하기 위해 사용되는 sandbox 보호 기능 해제
    service = Service("/Users/transfer_kk/Desktop/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get('https://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx?callPage=Sugang_SaveAB')
    start = time.time()
    is_crawl_majors = True
    lists = majors if is_crawl_majors else kitas
    
    try:
        for major in lists:
            select = Select(driver.find_element(By.NAME, 'ddlDept')) if is_crawl_majors else Select(driver.find_element(By.NAME, 'ddlKita'))
            major_value = major["value"]
            major_name = major["name"]
            select.select_by_value(major_value)
            if(is_crawl_majors) : driver.find_element(By.CSS_SELECTOR, "#ibtnSearch1").click()    
            else : driver.find_element(By.CSS_SELECTOR, "#ibtnSearch2").click()
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#dgList > tbody > tr')))
            rows = driver.find_elements(By.CSS_SELECTOR, '#dgList > tbody > tr')
            update_lists = [] 
            create_lists = []
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
                course = Course(
                    code = code, 
                    name = name,
                    grade = grade,
                    credit = credit,
                    subject = subject,
                    time_and_classroom = time_and_classroom,
                    professor = professor,
                    evaluation_method = evaluation_method,
                    remarks = remarks
                )   
                try:
                    if(Course.objects.exists(code = code)) : update_lists.append(course)
                    else : create_lists.append(course)
                except Exception as e:
                    print("\n---------------\nerror! " + " major value: " + major_name + "\n" +"course name: "+ name + "\n---------------\n")
            Course.objects.bulk_update(update_lists, ['major_name', 'name', 'grade', 'credit', 'subject', 'time_and_classroom', 'professor', 'evaluation_method', 'remarks'])
            Course.objects.bulk_create(create_lists)
            print("\n-----------\n" + major_name+" is OK" + "\n-----------\n")   
    except TypeError as e:
        print("Type error")
    except Exception as e:
        print("undefined error")
    finally:
        driver.quit()
    end = time.time()
    print("excute time : " + f"{end - start:.5f} sec")
    return HttpResponse(content="success!")
  
  
    
def crawl_course_vacancy(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless') # Browser를 GUI없이 백그라운드에서 실행
    chrome_options.add_argument('--no-sandbox') # 보안 취약점에 노출될 가능성을 최소화하기 위해 사용되는 sandbox 보호 기능 해제
    service = Service("/Users/transfer_kk/Desktop/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    start = time.time()
    try:
        driver.get('https://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx?callPage=Sugang_SaveAB')
        driver.add_cookie({"name":"ITISSugang", "value":"bigo=L+0gnQBAXrw=&grade=mXv8e05CoQE=&nowno=pcTw/Y5/29A=&change_Code=bGCcVaPhR+4=&ite_yn=qp7HMQ5dvNs=&pcode=G2D6xtRFEPg=&kicho=qp7HMQ5dvNs=&date14=LAPox8wwk7+53PT00PIU0A==&mincredit=bOFS5/mMm6U=&maxcredit=6gWfIS2AkdY=&pre_jaesu=vP8vv5LN+dI=&date_change=Z/RwgE+bG2Df3BjdH3eM3CwlA6y76crT&date_jaesu=CCQnQzTWZfM=&majors=2WdbESNCge0=&major_name=qp7HMQ5dvNs=&bokhag=qp7HMQ5dvNs=&dept_code=JltGKE1I2Aw=&major_code=2WdbESNCge0="})
        driver.add_cookie({"name":"ITISSugangHome", "value":"Grade=mXv8e05CoQE=&Term=9XCOn7R1QMI=&Kname=rdYyC0XmbRQaHBk04DY60A==&Dept_kname=drIw5mzH3OD3n1hdvkfNoeZYVjEPTSa5&Major_kname=drIw5mzH3ODvn8/JKmVK+g==&Manager=ccP/ybUZCSU=&Email=8DlY5mNAnBl8QkwNSuMr7/8U7pxOBfvH&Stno=6O/gxAPQyfIU9UuhsCZr9A==&Dept_code=JltGKE1I2Aw=&Major_code=2WdbESNCge0=&ClientAddress=ADz5uS4qFkikc8JqOUuFHA==&Ename=YNTNW7TuyEi8dJr/TwcPUw==&Dept_Ename=XC9PjrV2jtMcOfESGC/kZIp5AzpLxfvv&Major_ename=XC9PjrV2jtMcOfESGC/kZIp5AzpLxfvv&pwChgPop=ccP/ybUZCSU="})
        # IO bound
        code_prefixes = set()    
        is_crawl_majors = True
        lists = majors if is_crawl_majors else kitas
        for major in lists: 
            select = Select(driver.find_element(By.NAME, 'ddlDept')) if is_crawl_majors else Select(driver.find_element(By.NAME, 'ddlKita'))
            select.select_by_value(major["value"])            
            if is_crawl_majors : driver.find_element(By.CSS_SELECTOR, "#ibtnSearch1").click()
            else : driver.find_element(By.CSS_SELECTOR, "#ibtnSearch2").click()

            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#dgList > tbody > tr')))
            # IO bound
            rows = driver.find_elements(By.CSS_SELECTOR, "#dgList > tbody > tr")
            course_list = [] 
            new_courses = []
            for row in rows:
                code_prefix = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a > font").text.strip().split('-')[0] # 학수번호 앞 자리
                if(code_prefix in code_prefixes) : continue
                code_prefixes.add(code_prefix)
                row.find_element(By.CSS_SELECTOR, "td:nth-child(11) > input ").click()
                driver.switch_to.window(driver.window_handles[1])
                wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#dgList > tbody > tr')))
                # IO bound
                rows2 = driver.find_elements(By.CSS_SELECTOR, "#dgList > tbody > tr")
                for row2 in rows2:
                    code = row2.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()
                    course,course_is_created = Course.objects.get_or_create(code = code)
                    course.vacancy = row2.find_element(By.CSS_SELECTOR, "td:nth-child(8)").text.strip()
                    
                    if course_is_created:
                        name = row2.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text.strip()
                        professor = row2.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text.strip()
                        course.name = name
                        course.professor = professor
                        new_courses.append(course)
                        print("warn: (name: " + name + ", code: " + code + ", professor: " + professor)
                    else:
                        course_list.append(course)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            
            Course.objects.bulk_update(course_list, ['vacancy'])
            Course.objects.bulk_update(new_courses, ['name', 'professor', 'vacancy'])
            print("\n-----------\n" + major["name"]+" is OK" + "\n-----------\n")   
    except NoSuchElementException as e:
        print("error: " + e.msg)
    finally:
        driver.quit()
    
    end = time.time()
    print("excute time : " + f"{end - start:.5f} sec")
    return HttpResponse(content="success!")
    