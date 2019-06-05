'''
1번. 내려올 때 선택되어 왔던 모든 수의 합이 최대가 되는 경로의 합을 구하는 dp 알고리즘
이중 리스트로 input 삼각형과 같은 모양의 삼각형을 만들고 각 원소마다 해당 원소까지의 경로의 합이 가장 클 때의 합의 값을 저장한다.  
마지막 행의 원소들 중 가장 큰 값을 return
'''
def max_sum(num, triangle):
    max_sum = [[0 for _ in range(x+1)] for x in range(num)] # input 삼각형과 같은 모양의 합의 담는 이중 리스트 초기화

    max_sum[0][0] = triangle[0][0] #첫 값 복사
    for i in range(1,num): #윗 줄에서 첫값을 처리했으니 1부터 시작
        for j in range(i+1):
            if j==0: #원소가 삼각형의 왼쪽 끝변에 위치할 때 윗값을 더하여 할당
                max_sum[i][j] = triangle[i][j] + max_sum[i-1][j]
            elif j==i: #원소가 삼각형의 오른쪽 끝변에 위치할 때 윗값을 더하여 할당
                max_sum[i][j] = triangle[i][j] + max_sum[i-1][j-1]
                
            elif max_sum[i-1][j-1] > max_sum[i-1][j]: #합을 담는 리스트의 왼쪽 위값과 오른쪽 위값을 비교하여 더 큰 값을 더하여 할당
                max_sum[i][j] = triangle[i][j] + max_sum[i-1][j-1]
            else:
                max_sum[i][j] = triangle[i][j] + max_sum[i-1][j]

    return max(max_sum[num-1]) #마지막 행의 원소들 중 가장 큰 값을 return



num = int(input())

triangle = list()
for i in range(num):
    triangle.append([int(x) for x in input().split()])

print(max_sum(num, triangle))