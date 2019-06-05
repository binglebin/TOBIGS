def uncompress(s):
    result = '' #반환될 값
    for i in s:
        if (i.isdigit()): #i가 digit이면 
            iter_num = int(i) #int로 바꿔 저장
        else:
            for j in range(iter_num): #앞의 iter_num만큼
                result += i #result에 i 추가
    return result

print(uncompress('2a5b1c'))
print(uncompress('3x5y2z'))