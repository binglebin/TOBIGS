def make_anagram(c_list, w, n): #c_list = 문자열의 문자가 담긴 list, w = anagram에 추가될 문자열, n = c_list의 문자열 index
    if len(w) == len(c_list): # recursive 함수 종료조건 = w의 길이가 c_list의 길이와 같아지면
        anagram.add(w) #  w를 anagram set에 add
    else:
        for i in range(len(w)+1): #w의 길이+1 반복
            new_w = w[:i] + c_list[n] + w[i:] # 기존 w를 i index를 기준으로 나눠서 사이에 c_list의 n번째 문자를 넣음
            make_anagram(c_list, new_w, n+1) #새로만들어진 new_w와 c_list의 다음 문자열을 가르킬 n+1을 넣어 함수 호출


s = input() # string 받기
c_list = list(s) # 문자열을 문제로 나눠서 list에 저장
w='' # anagram word가 들어갈 string 초기값 설정
anagram=set() # anagram word 가 들어갈 set 초기값 설정
make_anagram(c_list, w, 0) #함수 호출
print(anagram) #출력
