def initialize_adam(parameters) :
    """
    Initializes v and s as two python dictionaries with:
                - keys: "dW1", "db1", ..., "dWL", "dbL" 
                - values: numpy arrays of zeros of the same shape as the corresponding gradients/parameters.
    
    Arguments:
    parameters -- python dictionary containing your parameters.
                    parameters["W" + str(l)] = Wl
                    parameters["b" + str(l)] = bl
    
    Returns: 
    v -- python dictionary that will contain the exponentially weighted average of the gradient.
                    v["dW" + str(l)] = ...
                    v["db" + str(l)] = ...
    s -- python dictionary that will contain the exponentially weighted average of the squared gradient.
                    s["dW" + str(l)] = ...
                    s["db" + str(l)] = ...

    """
    
    L = len(parameters) // 2 # number of layers in the neural networks
    v = {}
    s = {}
    
    # Initialize v, s. Input: "parameters". Outputs: "v, s".
    for l in range(L):
    ### START CODE HERE ### (approx. 4 lines)
        v["dW" + str(l+1)] = np.zeros_like(parameters["W" + str(l+1)])
        v["db" + str(l+1)] = np.zeros_like(parameters["b" + str(l+1)])
        s["dW" + str(l+1)] = np.zeros_like(parameters["W" + str(l+1)])
        s["db" + str(l+1)] = np.zeros_like(parameters["b" + str(l+1)])
    ### END CODE HERE ###
    
    return v, s
'''
initialize_adam(parameters)
    - adam optimization 을 적용하기 위해 필요한 변수 initializing 함수
parameters
    - parameters : 각 Layer의 weight와 bias 이름을 key값으로 해당하는 값이 value에 저장되어있는 dictionary
return
    - v : momentum term
    - s : RMSProp term
        각 Layer의 weight와 bias의 gradient 이름을 key값으로
            각각의 크기에 맞는 영행렬로 초기화하여 value에 저장되어 있는 dictionary 
'''


def function1(parameters, grads, v, s, t, learning_rate = 0.01,
                                beta1 = 0.9, beta2 = 0.999,  epsilon = 1e-8):

    L = len(parameters) // 2                 
    v_corrected = {}                        
    s_corrected = {}                     
    
  
    for l in range(L):

       
        v["dW" + str(l+1)] = beta1 * v["dW" + str(l+1)] + (1-beta1) * grads["dW" + str(l+1)]
        v["db" + str(l+1)] = beta1 * v["db" + str(l+1)] + (1-beta1) * grads["db" + str(l+1)]
        '''
        momentum parameter를 이전 누적된 momentum term에 곱하고
        ( 1 - mumentum parameter )에 현재 gradient를 곱하여 더함
        '''
        v_corrected["dW" + str(l+1)] = v["dW" + str(l+1)]/(1-np.power(beta1,t))
        v_corrected["db" + str(l+1)] = v["db" + str(l+1)]/(1-np.power(beta1,t))
        
       '''
       가장 영향을 많이 주게 되는 초반 gradient 들의 영향을 줄이기 위해 
       (1- mometum parameter ^ t(횟수)승)을 나눠준다. 
       '''
        s["dW" + str(l+1)] = beta2 * s["dW" + str(l+1)] + (1-beta2) * np.square(grads["dW" + str(l+1)])
        s["db" + str(l+1)] = beta2 * s["db" + str(l+1)] + (1-beta2) * np.square(grads["db" + str(l+1)])
        '''
        RMSProp parameter를 이전 누적된 RMSProp term에 곱하고
        현재 gradient를 제곱하여 방향을 없애고 속도만 남겨 ( 1 - RMSProp parameter )에 곱하여 더함
        '''
        
        s_corrected["dW" + str(l+1)] = s["dW" + str(l+1)]/(1-np.power(beta2,t))
        s_corrected["db" + str(l+1)] = s["db" + str(l+1)]/(1-np.power(beta2,t))
        
        '''
       가장 영향을 많이 주게 되는 초반 gradient 들의 영향을 줄이기 위해 
       (1- RMSProp parameter ^ t(횟수)승)을 나눠준다. 
       '''

        parameters["W" + str(l+1)] = parameters["W" + str(l+1)] - learning_rate * v_corrected["dW" + str(l+1)]/(np.sqrt(s_corrected["dW" + str(l+1)]) + epsilon)
        parameters["b" + str(l+1)] = parameters["b" + str(l+1)] - learning_rate * v_corrected["db" + str(l+1)]/(np.sqrt(s_corrected["db" + str(l+1)]) + epsilon)
 
        '''
        learning rate에  momemtum term 을 곱하고 
        RMSProp term의 제곱근을 구하여 단위를 맞춰주고 나눠준 값을 parameter에 빼서 갱신
        '''

    return parameters, v, s

'''
function1
    - gradient를 adam optimization을 통해 weight와 bias를 학습시키는 함수
parameters
    - parameters : 각 Layer의 weight와 bias 이름을 key값으로 해당값이 저장되어있는 dictionary
    - grads : gradient 값이 저장되있는 dictionary
    - v : 이전 momentum term
    - s : 이전 RMSprop term
    - t : 학습 횟수
    - learning_rate = 0.01 : 학습률
    - beta1 = 0.9 : momentum parameter
    - beta2 = 0.999 : RMSprop parameter
    - epsilon = 1e-8 : 0 으로 나눠지지 않기 위해 넣는 작은 값
return
    - parameters : adam optimization 된 parameter
    - v = 현재 momentum
    - s = 현재 RMSProp
'''



def function2(X, parameters, keep_prob = 0.5):


    np.random.seed(1)

    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    W3 = parameters["W3"]
    b3 = parameters["b3"]

    # LINEAR -> RELU -> LINEAR -> RELU -> LINEAR -> SIGMOID
    Z1 = np.dot(W1, X) + b1
    A1 = relu(Z1)
    D1 = np.random.rand(A1.shape[0],A1.shape[1])
    D1 = D1 < keep_prob                                
    A1 = np.multiply(A1,D1)                             
    A1 = A1/keep_prob

    Z2 = np.dot(W2, A1) + b2
    A2 = relu(Z2)
    D2 = np.random.rand(A2.shape[0],A2.shape[1])                        
    D2 = D2 < keep_prob                               
    A2 = np.multiply(A2,D2)                           
    A2 = A2/keep_prob                                 
    
    Z3 = np.dot(W3, A2) + b3
    A3 = sigmoid(Z3)
    
    '''
    dropout
    relu 활성화 함수를 거친 데이터와 같은 크기의 0 ~ 1 사이의 난수 행렬을 만들어서
    dropout hyperparameter 이하의 원소를 True 나머지 원소를 False로 하는 boolean 행렬로 만듬
    이후 데이터와 원소기반 곱셈을 하여 특정 노드를 dropout
    나머지 데이터에 dropout으로 꺼질 확률의 기댓값인 dropout hyperparameter를 나눠준다.
    '''
    
    cache = (Z1, D1, A1, W1, b1, Z2, D2, A2, W2, b2, Z3, A3, W3, b3)

    return A3, cache

'''
function2
    - LINEAR -> RELU -> dropout -> LINEAR -> RELU -> dropout -> LINEAR -> SIGMOID 순전파 함수
parameter
    - X : train 데이터
    - parameters : weight와 bais
    - keep_prob = 0.5 : dropout 확률
return
    - A3 : 마지막 activation 함수를 통과한 값 (output layer)
    - cache  : (Z1, D1, A1, W1, b1, Z2, D2, A2, W2, b2, Z3, A3, W3, b3)
'''





def function3(X, Y, cache, keep_prob):

    
    m = X.shape[1]
    (Z1, D1, A1, W1, b1, Z2, D2, A2, W2, b2, Z3, A3, W3, b3) = cache
    
    dZ3 = A3 - Y
    dW3 = 1./m * np.dot(dZ3, A2.T)
    db3 = 1./m * np.sum(dZ3, axis=1, keepdims = True)
    dA2 = np.dot(W3.T, dZ3)
    
    dA2 = np.multiply(dA2,D2)             
    dA2 = dA2/keep_prob              

    dZ2 = np.multiply(dA2, np.int64(A2 > 0))
    dW2 = 1./m * np.dot(dZ2, A1.T)
    db2 = 1./m * np.sum(dZ2, axis=1, keepdims = True)
    
    dA1 = np.dot(W2.T, dZ2)

    dA1 = np.multiply(dA1,D1)             
    dA1 = dA1/keep_prob             

    dZ1 = np.multiply(dA1, np.int64(A1 > 0))
    dW1 = 1./m * np.dot(dZ1, X.T)
    db1 = 1./m * np.sum(dZ1, axis=1, keepdims = True)
    
    gradients = {"dZ3": dZ3, "dW3": dW3, "db3": db3,"dA2": dA2,
                 "dZ2": dZ2, "dW2": dW2, "db2": db2, "dA1": dA1, 
                 "dZ1": dZ1, "dW1": dW1, "db1": db1}
    
    return gradients

'''
function3
    - 역전파 함수
parameter
    - X : train 데이터
    - Y : test 데이터
    - cache : (Z1, D1, A1, W1, b1, Z2, D2, A2, W2, b2, Z3, A3, W3, b3)
    - keep_prob = 0.5 : dropout 확률
return
    - gradients : 역전파를 통해 나온 gradient 값들
'''
