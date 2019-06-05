import numpy as np
import numpy.linalg as lin
from sklearn.preprocessing import StandardScaler


class mypca(object):
    '''
    k : component 수
    n : 원래 차원
    components : 고유벡터 저장소 shape (k,n)
    explain_values : 고유값 shape (k,)
    '''
    
    k = None
    components = None
    explain_values= None
    
    def __init__(self, k=None, X_train=None):
        '''
        k의 값이 initial에 없으면 None으로 유지
        '''
        if k is not None :
            self.k = k       
        if X_train is not None:
            self.fit(X_train)
            
    def fit(self,X_train=None):
        if X_train is None:
            print('Input is nothing!')
            return
        if self.k is None:
            self.k = min(X_train.shape[0],X_train.shape[1])
            
        #############################################
        # TO DO                                     #
        # 인풋 데이터의 공분산행렬을 이용해         #
        # components와 explain_values 완성          # 
        #############################################
        
        cov = np.cov(X_train.T) 
        explain_values_raw, components_raw = lin.eig(cov) 
        self.explain_values = explain_values_raw[:self.k] 
        self.components = components_raw.T[:self.k]
        
        '''
        cov = data의 공분산 행렬
        explain_values_raw = 공분산 행렬의 고유값 리스트
        components_raw = 공분산 행렬의 고유벡터 행렬
        explain_values = 줄이고 싶은 차원수 만큼 슬라이싱한 고유값 리스트
        components = 줄이고 싶은 차원수 만큼 슬라이싱한 고유벡터 행렬
        '''
        
        
        #############################################
        # END CODE                                  #
        #############################################
        
        return
    
    def transform(self,X=None):
        if X is None:
            print('Input is nothing!')
            return
        
        result = None
        '''
        N : X의 행 수
        result의 shape : (N, k)
        '''
        #############################################
        # TO DO                                     #
        # components를 이용해 변환결과인            #
        # result 계산                               #
        #############################################
        
        result = np.dot(X, self.components.T)
        
        '''
        result = N차원의 data에 k개의 고유벡터를 행렬곱하여 새로운 k차원의 데이터를 만듬
        '''
        
        #############################################
        # END CODE                                  #
        #############################################       
        return result
    
    def fit_transform(self,X=None):
        if X is None:
            print('Input is nothing!')
            return
        self.fit(X)
        return self.transform(X)