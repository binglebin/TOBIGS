def countDivisor(k, a, b):
    if (0>a) | (a>100000) | (0>b) | (b>100000): #잘못된 input 예외처리
        print('invalid value (0 <= a, b <= 100000)')
        return
    div_list = list()
    for i in range(a,b+1): 
        divisor =0 #약수 개수
        for j in range(1, i+1):
            if i % j == 0: # 나머지가 0이 되면 약수
                divisor += 1
        if k == divisor: # 목표 약수개수와 i의 약수개수가 같다면
            div_list.append(str(i)) #약수 list에 추가
    print(' '.join(div_list))
    print(len(div_list), '개 입니다.')


countDivisor(4,5,10)

countDivisor(4,-1,20)