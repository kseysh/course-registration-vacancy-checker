import json

# 주어진 HTML 데이터

html_data = """
	<option value="1206574">법학과목 / 법학과목</option>
	<option value="0194002">기계공학과 / 기계공학</option>
	<option value="0198005">항공우주공학과 / 항공우주공학</option>
	<option value="1013446">조선해양공학과 / 조선해양공학</option>
	<option value="1014514">산업경영공학과 / 산업경영공학</option>
	<option value="1235021">화학공학과 / 화학공학</option>
	<option value="1235756">화학공학과 / 이차전지공학</option>
	<option value="0223022">고분자공학과 / 고분자공학</option>
	<option value="1016386">신소재공학과 / 신소재공학</option>
	<option value="1016757">신소재공학과 / 반도체공학</option>
	<option value="1017516">사회인프라공학과 / 사회인프라공학</option>
	<option value="0225028">환경공학과 / 환경공학</option>
	<option value="1104537">공간정보공학과 / 공간정보공학</option>
	<option value="0691156">건축학부 / 건축공학</option>
	<option value="0691305">건축학부 / 건축학</option>
	<option value="0930430">에너지자원공학과 / 에너지자원공학</option>
	<option value="1601284">전기전자공학부 / 전기전자공학</option>
	<option value="1601767">전기전자공학부 / 인공지능반도체공학</option>
	<option value="1602285">이차전지융합학과 / 이차전지융합학</option>
	<option value="1602756">이차전지융합학과 / 이차전지공학</option>
	<option value="1443732">공과대학(FVE) / 미래자동차공학</option>
	<option value="1565408">반도체시스템공학과 / 반도체</option>
	<option value="1565770">반도체시스템공학과 / 반도체시스템공학</option>
	<option value="1063157">수학과 / 수학</option>
	<option value="1064040">통계학과 / 통계학</option>
	<option value="1065039">물리학과 / 물리학</option>
	<option value="1066041">화학과 / 화학</option>
	<option value="1023307">해양과학과 / 해양과학</option>
	<option value="1186074">식품영양학과 / 식품영양학</option>
	<option value="1607045">경영학부 경영학과 / 경영학</option>
	<option value="1608093">경영학부 파이낸스경영학과 / 파이낸스경영학</option>
	<option value="0934339">아태물류학부 / 물류학</option>
	<option value="1187268">국제통상학과 / 국제통상학</option>
	<option value="0267059">국어교육과 / 국어교육</option>
	<option value="0268065">영어교육과 / 영어교육</option>
	<option value="0275054">사회교육과 / 사회교육</option>
	<option value="0273057">체육교육과 / 체육교육</option>
	<option value="0276055">교육학과 / 교육학</option>
	<option value="0749160">수학교육과 / 수학교육</option>
	<option value="0478051">행정학과 / 행정학</option>
	<option value="0477053">정치외교학과 / 정치외교학</option>
	<option value="0477774">정치외교학과 / 기후위기대응</option>
	<option value="1188047">경제학과 / 경제학</option>
	<option value="1189364">소비자학과 / 소비자학</option>
	<option value="1190557">아동심리학과 / 아동심리학</option>
	<option value="1191555">사회복지학과 / 사회복지학</option>
	<option value="1343693">미디어커뮤니케이션학과 / 미디어커뮤니케이션학</option>
	<option value="1026369">한국어문학과 / 한국어문학</option>
	<option value="0301071">사학과 / 사학</option>
	<option value="0302072">철학과 / 철학</option>
	<option value="1192556">중국학과 / 중국학</option>
	<option value="1028485">일본언어문화학과 / 일본언어문화</option>
	<option value="1604067">영미유럽인문융합학부 / 영어영문학</option>
	<option value="1604088">영미유럽인문융합학부 / 영미유럽인문융합학부</option>
	<option value="1604486">영미유럽인문융합학부 / 프랑스언어문화</option>
	<option value="1236588">문화콘텐츠문화경영학과 / 문화콘텐츠문화경영학</option>
	<option value="0317077">의예과 / 의예</option>
	<option value="0318078">의학과 / 의학</option>
	<option value="1600079">간호학과 / 간호학</option>
	<option value="1238590">소프트웨어융합공학과 / 소프트웨어융합공학</option>
	<option value="1239591">산업경영학과 / 산업경영학</option>
	<option value="1262600">메카트로닉스공학과 / 메카트로닉스공학</option>
	<option value="1263601">금융투자학과 / 금융투자학</option>
	<option value="1564769">반도체산업융합학과 / 반도체산업융합</option>
	<option value="1393686">IBT학과 / 국제경영학</option>
	<option value="1394687">ISE학과 / 융합시스템공학</option>
	<option value="1395695">KLC학과 / 국제한국언어문화학</option>
	<option value="1430217">컴퓨터공학과 / 컴퓨터공학</option>
	<option value="1389722">인공지능공학과 / 인공지능공학</option>
	<option value="1390723">데이터사이언스학과 / 데이터사이언스학</option>
	<option value="1391724">스마트모빌리티공학과 / 스마트모빌리티공학</option>
	<option value="1392725">디자인테크놀로지학과 / 디자인테크놀로지학</option>
	<option value="1223583">소프트웨어융합대학(SCSC) / 연계전공(SCSC)</option>
	<option value="1461344">예술체육대학 / 예술체육학부</option>
	<option value="1449558">조형예술학과 / 조형예술학</option>
	<option value="1450589">디자인융합학과 / 디자인융합학</option>
	<option value="1452519">스포츠과학과 / 스포츠과학</option>
	<option value="1453372">연극영화학과 / 연극영화학</option>
	<option value="1454288">의류디자인학과 / 의류디자인학</option>
	<option value="1581304">생명공학과 / 생명공학</option>
	<option value="1582306">생명과학과 / 생명과학</option>
	<option value="1583737">바이오제약공학과 / 바이오제약공학</option>
	<option value="1603353">첨단바이오의약학과 / 첨단바이오의약학</option>
	<option value="1613354">자유전공융합학부 / 자유전공융합학부</option>
	<option value="1614096">공학융합학부 / 공학융합학부</option>
	<option value="1615102">자연과학융합학부 / 자연과학융합학부</option>
	<option value="1616110">경영융합학부 / 경영융합학부</option>
	<option value="1617262">사회과학융합학부 / 사회과학융합학부</option>
	<option value="1618265">인문융합학부 / 인문융합학부</option>
	<option value="1631477">프런티어창의대학 / 프런티어창의대학</option>
"""

# 문자열 처리
lines = html_data.strip().split('\n')

result = []

# 각 <option> 요소를 순회하며 JSON 형식으로 변환
for idx, line in enumerate(lines):
    # line 예시: <option value="0194002">기계공학과 / 기계공학</option>
    value = line.split('"')[1]
    name = line.split('>')[1].split('<')[0]
    
    result.append({
        "value": value,
        "name": name
    })

# 결과를 JSON 형식으로 출력
majors_json = json.dumps(result, ensure_ascii=False, indent=4)

print(majors_json)

print("\n\n------------------\n\n")

majors_list = json.loads(majors_json)

for major in majors_list:
    print(f"'{major['value']}': '{major['name']}',")