a = 'spartacodingclub@gmail.com'

# 채워야하는 함수
def check_mail(s):
    if '@' in s:
        return True
    else:
        return False

# 결과값
print(check_mail(a))

# 채워야하는 함수
def get_mail(s):
    return s.split('@')[1].split('.')[0]
# 결과값
print(get_mail(a))

# 입력값
a = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']


# 채워야하는 함수
def count_list(a_list):
    result = {}
    for fruit in a_list:
        if fruit in result:
            result[fruit] += 1
        else:
            result[fruit] = 1
    return result
# 결과값
print(count_list(a))


import requests  # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print(rjson['RealtimeCityAir']['row'][0]['NO2'])

def get_mise(gu_name):
    for gu in rjson['RealtimeCityAir']['row']:
        if gu_name == gu['MSRSTE_NM']:
            return gu['IDEX_MVL']
    return "일치하는 구가 없습니다."


def get_under_100():
    for gu in rjson['RealtimeCityAir']['row']:
        if gu['IDEX_MVL'] < 100:
            print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

get_under_100()