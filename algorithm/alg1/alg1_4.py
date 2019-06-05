def vowel_count(s):
    vowel = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0} #모음이 담길 dic
    for i in s: # 문자열의 문자 반복문
        if i in vowel: # i가 vowel의 key라면
            vowel[i] += 1 # key에 해당되는 value 1추가
    for i, j in vowel.items(): # key와 value 쌍으로 출력
        print('vowel ' + i + ' : ' + str(j))

print('Enter one word : ')
s = input()
vowel_count(s)
