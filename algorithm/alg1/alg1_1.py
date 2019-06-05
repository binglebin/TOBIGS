import re

s = input() #string 받기
low_s = s.lower() #소문자로 변환
trim_s = re.sub(r'[^\w\s]','',low_s) #정규식으로 구두점 없애기
list_s = trim_s.split() #공백 구분 list 만들기
set_s = set(list_s) #집합으로 중복 없애기
num_s=len(set_s) #집합 원소 개수
print(num_s) 