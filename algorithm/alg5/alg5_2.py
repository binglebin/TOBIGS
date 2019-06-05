'''
2번. 가져올 수 있는 금괴 개수의 최대값을 구하는 dp 알고리즘
이중 리스트로 input 행렬과 같은 모양의 행렬을 만들고 각 원소마다 해당 원소까지의 경로의 합이 가장 클 때의 합의 값을 저장한다.  
대각선으로 이동시 가져올 수 있는 금괴의 수가 줄어들기 때문에 고려하지 않는다.
마지막 행의 마지막 열을 return
'''
def max_gold(n, m, gold_room):
    max_sum = [[0 for _ in range(m)] for x in range(n)] # input 행렬과 같은 모양의 합의 담는 이중 리스트 초기화

    for i in range(n):
        for j in range(m):
            if i==0:
                if j==0: #첫 값 복사
                    max_sum[i][j] = gold_room[i][j]
                max_sum[i][j] = gold_room[i][j] + max_sum[i][j-1] # 첫번째 행의 경우 왼쪽 값을 더하여 할당
            elif j==0:
                max_sum[i][j] = gold_room[i][j] + max_sum[i-1][j] # 첫번째 열의 경우 윗 값을 더하여 할당
                
            elif max_sum[i][j-1] > max_sum[i-1][j]: #합을 담는 리스트의 왼쪽 값과 윗 값을 비교하여 더 큰 값을 더하여 할당
                max_sum[i][j] = gold_room[i][j] + max_sum[i][j-1]
            else:
                max_sum[i][j] = gold_room[i][j] + max_sum[i-1][j]

    return max_sum[n-1][m-1] #마지막 행의 마지막 열을 return


n, m= map(int, input().split())
gold_room=list()
for _ in range(n):
    gold_room.append([int(x) for x in input().split()])

print(max_gold(n, m, gold_room))