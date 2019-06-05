def monotonic(raw_list): # 단조증가와 단조감소 비교함수
    inc = monotonic_increase(raw_list) #단조 증가일때 최소값
    raw_list.reverse() # list 뒤집기
    dec = monotonic_increase(raw_list) #단조 감소일때 최소값
    if inc <= dec: # 최소값 출력
        print(inc)
        return inc
    else:
        print(dec)
        return dec

def monotonic_increase(raw_list): #단조 증가일때 최소값 함수
    seq = [1]*len(raw_list) # idx가 최장증가수열의 마지막일때 길이를 담는 리스트
    tr = [-1]*len(raw_list) # idx가 최장증가수열에 포함되어 있을때 바로 앞 idx를 담는 리스트 (줄 세우기)
    n = len(raw_list)

    for i in range(n): #모든 idx
        for j in range(i): #i보다 작은 idx들
            if raw_list[i]>=raw_list[j]: #i번째 값이 j번째 값보다 크거나 같을때 
                if seq[i] < seq[j]+1: # i까지의 최장증가수열길이가 j까지의 최장증가수열길이+1보다 작다면
                    seq[i] = seq[j]+1 # i까지의 최장증가수열길이에 j까지의 최장증가수열길이에 1을 더한 값을 담고
                    tr[i] = j # i를 j뒤에 연결한다

    max_seq = max(seq) # idx가 최장 증가 수열의 마지막일때 가장 긴 값
    max_seq_idx = seq.index(max_seq) # max_seq의 idx
    temp = max_seq_idx 

    mono_list =[] #최장증가수열의 idx를 담을 list

    for i in range(max_seq): # 최장증가수열의 길이
        mono_list.append(temp) #최장증가수열의 마지막 원소를 list에 담고
        temp = tr[temp] #마지막 원소 바로 앞 원소를 담기위해 temp를 바로 앞 idx로 변경한다
    mono_list.sort()
    ch_list = list({x for x in range(n)} - set(mono_list)) #최장 증가 수열에 포함되지 않는 idx 리스트
    
    new_list = raw_list.copy() # 변경하기위한 새로운 list
    for i in ch_list: # 변경되야할 idx
        if i < mono_list[0]: #변경 되어야 할 idx가 최장증가수열의 첫번쨰 idx보다 작을떄 
            new_list[i] = new_list[0] # idx의 값을  최장증가수열의 첫번째 값으로 바꿔줌
        elif i > mono_list[len(mono_list)-1]: #변경 되어야 할 idx가 최장증가수열의 마지막 idx보다 클 때 
            new_list[i] = new_list[len(mono_list)-1] #idx의 값을 최장증가수열의 마지막 값으로 바꿔줌
        else:
            for j in range(len(mono_list)-1): # 최장증가수열 원소들 사이에 변경되야할 idx 위치를 찾기 위한 for 문 
                if (mono_list[j]<i)&(i<mono_list[j+1]): #변경되어야할 idx의 앞뒤로 가장 가까운 최장증가수열 idx를 찾기위한 if 문
                    if abs(new_list[mono_list[j]]-new_list[i])>abs(new_list[mono_list[j+1]]-new_list[i]): #변경되어야할 값의 앞의 값의 차와 뒤의값을 차를 비교하여 차가 적은 위치의 값으로 바꿈
                        new_list[i] = new_list[mono_list[j+1]]
                    else:
                        new_list[i] = new_list[mono_list[j]]

    result = 0 
    for i in range(n): 
        result += abs(new_list[i]-raw_list[i]) #원래의 list와 새로운 list의 편차를 더함

    return result



#user_input = [int(x) for x in input().split()] # space로 구분되어있는 input값을 int list로 변경

n = int(input())
user_input = list()
for i in range(n):
    user_input.append(int(input()))

monotonic(user_input)

4/9gAYIEDFdN-wzVCCAo8hYh8TUawwsANSqyCoZ00S5XyK5HKcRY7KeVE