def countRepeat(f): 
    count = 0 #반복스펠링단어 개수를 담는 변수
    for line in f: #파일의 line for 문
        w = line.lower().strip() # 소문자변환 후 앞뒤 공백 제거
        change = 0 # 변경되는 횟수를 담는 변수
        check = 0 # 첫번째 letter 처리용 변수
        for i in w: #letter for문
            if check == 0: # 첫번째 letter 를 previous에 넣고 변경횟수 1추가
                previous = i
                check = 1
                change += 1
            else:
                if previous != i: # 만약 이전 letter와 현재 letter가 같다면 change 횟수 +1
                    change += 1 
                previous = i # 이전 letter 업데이트
        if len(set(w)) == change: # w의 unique letter 개수와 변경횟수가 같다면 반복스펠링단어
            count += 1 #반복스펠링단어 개수 +1
    print(count)

with open('a_dic.txt', 'r') as f:
    countRepeat(f)
