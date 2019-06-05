def climbingMonkeyProb(n):
    if 5>n: #잘못된 input 예외처리
        print('invalid value (5 <= n)')
        return
    print(climbingMonkey(n, 0, 0, 1)) #목표시간, 현재시간 0, 현재높이 0, 현재 확률 1

def climbingMonkey(n, k, len, prob): # 목표 시간과 현재 시간, 현재 높이, 현재 확률을 input으로 하는 재귀함수
    if (len >= 150): # 종료 조건 : 현재길이가 150을 넘거나 같을 때
        if (n == k): # 목표 시간과 현재 시간이 같다면 확률 반환
            return prob 
        else: # 다르다면 0 반환
            return 0
    else:
        prob = climbingMonkey(n, k+1, len+30, prob*0.5) + climbingMonkey(n, k+1, len+15, prob*0.5)  #시간 + 1, 현재길이 + 30/15, 확률 * 0.5을 input으로 재귀호출. 성공확률과 실패확률을 더해준다.
        return prob #확률 반환

climbingMonkeyProb(6)

climbingMonkeyProb(4)