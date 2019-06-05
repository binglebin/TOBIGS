import numpy as np

class TwoLayerNet():
    """
    2 Layer Network를 만드려고 합니다.

    해당 네트워크는 다음과 같은 구조를 따릅니다.

    input - Linear - ReLU - Linear - Softmax

    Softmax 결과는 입력 N개의 데이터에 대해 각 클래스에 대한 확률입니다.
    """

    def __init__(self, input_size, hidden_size, output_size, std=1e-4):
        """
        네트워크에 필요한 가중치들을 initialization합니다.
        해당 가중치들은 self.params 라는 Dictionary에 담아둡니다.

        input_size: 데이터의 변수 개수 - D
        hidden_size: 히든 층의 H 개수 - H
        output_size: 클래스 개수 - C

        """
        # 여기에 가중치들을 init 하세요
        self.params = {}
        self.params["W1"] = std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size)
    def forward(self, X, y=None):
        """

        X: input 데이터 (N, D)
        y: 레이블 (N,)

        Linear - ReLU - Linear - Softmax - CrossEntropy Loss

        이 코드에서는,
        y가 주어지지 않으면 Softmax 결과 p와 Activation 결과 a를 return합니다.
        그 이유는 p와 a 모두 backward에서 미분할때 사용하기 때문입니다.
        y가 주어지면 CrossEntropy Error를 return합니다.

        """

        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        N, D = X.shape
        
        '''
        W1 : (D, H)
        b1 : (H)
        W2 : (H, C)
        b2 : (C)
        '''

        # 여기서 p를 구하는 작업을 수행하세요.

        h = np.dot(X, W1) + b1 
        a = np.maximum(0,h)
        scores = np.dot(a, W2) + b2
        p = np.exp(scores)/np.sum(np.exp(scores), axis = 1).reshape(-1,1)
        
        '''
        h : (N, H)
        a : (N, H)
        scores : (N, C)
        p = (N, C)
        '''
        
        
        if y is None:
            return p, a

        # 여기서 Loss를 구하는 작업을 수행하세요.
   
        Loss = -np.log(p[np.arange(N), y]).sum()
        Loss = Loss/N
        
        return Loss


    def backward(self, X, y, learning_rate=1e-5):
        """

        X: input 데이터 (N, D)
        y: 레이블 (N,)

        grads에는 Loss에 대한 W1, b1, W2, b2 미분 값이 기록됩니다.

        원래 backw 미분 결과를 return 하지만
        여기서는 Gradient Descent방식으로 가중치 갱신까지 합니다.

        """
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        
        '''
        W1 : (D, H)
        b1 : (H)
        W2 : (H, C)
        b2 : (C)
        '''
        
        N = X.shape[0] # 데이터 개수
        grads = {}

        #p, a는 forward 결과를 가져옵니다.
        p, a = self.forward(X)
        
        '''
        p = (N, C)
        a : (N, H)        
        '''
        
        # 여기에 각 파라미터에 대한 미분 값을 저장하세요.

        dp = p.copy() #list copy 미분값
        dp[np.arange(N), y] -= 1 # loss 함수를 ai로 미분하면 pi - yi
        da = np.dot(dp, W2.T)
        dh = da * (a > 0)
        
        '''
        dp = (N, C)
        da : (N, H)
        dh : (N, H)
        '''    
        
        grads["W2"] = (1/N) * np.dot(a.T, dp)
        grads["b2"] = (1/N) * np.sum(dp, axis = 0)
        grads["W1"] = (1/N) * np.dot(X.T, dh)
        grads["b1"] = (1/N) * np.sum(dh, axis = 0)
        

        self.params["W1"] -= learning_rate * grads["W1"]
        self.params["b1"] -= learning_rate * grads["b1"]
        self.params["W2"] -= learning_rate * grads["W2"]
        self.params["b2"] -= learning_rate * grads["b2"]

    def accuracy(self, X, y):
        N = X.shape[0]
        p, _ = self.forward(X)
        y_pred = np.argmax(p, axis = 1)

        return np.sum(y_pred==y)/N