def palindrome(B):
    if (2>B) | (B>10): #잘못된 input 예외처리
        print('invalid value (2 <= B <= 10)')
        return
    count = 0
    for i in range(1, 301):
        operand = i ** 2 # i 제곱을 피연산자에 저장
        B_num = '' # 진수변환된 숫자를 넣을 str
        check = 0
        while operand != 0 : # 피연산자가 0이되면 while문 종료
            quot = operand // B #몫
            remain = operand % B #나머지
            B_num = str(remain) + B_num #나머지을 이어붙여 진수변환
            operand = quot # 몫을 피연산자에 저장
        for j in range(len(B_num)//2): # 진수변환된 수의 길이의 절반만큼 for문
            if B_num[j] != B_num[-j-1]: #j번째 수와 대칭되는수를 비교하여 다르면 바깥 for문 continue
                check = 1 
                break
        if check == 1: 
            continue
        print (i, B_num) # 진수대칭변환 출력
        count += 1
    print(count, '개의 진수대칭변환이 있습니다')

palindrome(10)

palindrome(11)
