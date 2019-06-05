s, w = input().split(',') #string 받고 ,로 구분하기
s, w = s.strip(), w.strip() #각각 앞뒤 공백 없애기
num_w = s.count(w) #s안에 w가 몇번 들어가는지 count
print(num_w) 