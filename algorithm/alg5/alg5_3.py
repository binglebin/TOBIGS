'''
3번. 최종파일을 만드는 데 필요한 비용의 최소값을 구하는 dp 알고리즘

첫번째 행렬 : input 리스트의 원소들을 대각 원소로 갖는 해당 원소의 비용의 최소값을 담는 행렬 
두번째 행렬 : 첫번째 행렬과 같은 모양의 해당 원소까지의 비용의 최소값을 담는 행렬
행렬의 대각선 기준 아래 원소는 사용하지 않는다.
진행방향은 행렬의 대각원소들부터 첫번째행의 마지막열까지 대각선으로 진행
첫번째 행의 마지막 열을 return
'''
def min_cost(num, file_cost):
    min_sum = [[0 for _ in range(num)] for _ in range(num)] # input 행렬과 같은 모양의 해당 원소의 비용의 최소값을 담는 이중 리스트 초기화
    cost_sum = [[0 for _ in range(num)] for _ in range(num)] # input 행렬과 같은 모양의 해당 원소까지의 비용의 최소값을 담는 이중 리스트 초기화
    for i in range(num): # min_sum 행렬의 대각원소에 input 리스트의 원소 할당
        min_sum[i][i] = file_cost[i]

    for l in range(1, num): #대각원소+1의 위치부터 첫번째 행의 마지막 열 까지의 반복
        for i in range(num - l): # l의 반복마다 처리하는 원소들이 대각방향이 되게 i 반복, j 할당
            j = i + l 
            cost_sum[i][j]= float('inf') #최소값을 구하는 행렬이기 때문에 원소 inf값으로 할당
            for k in range(i,j): 
                temp = min_sum[i][k] + min_sum[k+1][j] # 각각의 파일이 두번 처리 되지 않게 해당 원소의 비용을 구함
                temp2 = cost_sum[i][k] + cost_sum[k+1][j] + temp # 해당 원소 까지의 비용을 구함
                if cost_sum[i][j] > temp2: # 해당 원소까지의 비용이 최소값일때 해당 원소의 비용과 해당 원소까지의 비용을 각각 할당
                    min_sum[i][j] = temp
                    cost_sum[i][j] = temp2
    
    return cost_sum[0][num-1] #첫번째 행의 마지막 열을 return



num = int(input())
file_cost = [int(x) for x in input().split()]

print(min_cost(num, file_cost))