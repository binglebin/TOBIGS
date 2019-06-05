def function1(x, gamma, beta, eps):

    N, D = x.shape


    mu = 1./N * np.sum(x, axis = 0)


    xmu = x - mu


    sq = xmu ** 2


    var = 1./N * np.sum(sq, axis = 0)


    sqrtvar = np.sqrt(var + eps)

    ivar = 1./sqrtvar


    xhat = xmu * ivar


    gammax = gamma * xhat


    out = gammax + beta

    cache = (xhat,gamma,xmu,ivar,sqrtvar,var,eps)

    return out, cache


'''
function1
    - batch nomalization  순전파 함수
parameters
    - x : train data의 batch
    - gamma : 정규화된것을 다시 한번 조정하는 scaling 파라미터
    - beta : 정규화된것을 다시 한번 조정하는 shift 파라미터
    - eps : 0 으로 나눠지지 않기 위해 넣는 작은 값
return
    - out : batch 데이터를 정규화시켜서 gamma와 beta로 재조정한 값
    - cache : (xhat,gamma,xmu,ivar,sqrtvar,var,eps)
'''




def function2(dout, cache):

  
    xhat,gamma,xmu,ivar,sqrtvar,var,eps = cache


    N,D = dout.shape


    dbeta = np.sum(dout, axis=0)
    dgammax = dout 


    dgamma = np.sum(dgammax*xhat, axis=0)
    dxhat = dgammax * gamma


    divar = np.sum(dxhat*xmu, axis=0)
    dxmu1 = dxhat * ivar


    dsqrtvar = -1. /(sqrtvar**2) * divar


    dvar = 0.5 * 1. /np.sqrt(var+eps) * dsqrtvar


    dsq = 1. /N * np.ones((N,D)) * dvar


    dxmu2 = 2 * xmu * dsq


    dx1 = (dxmu1 + dxmu2)
    dmu = -1 * np.sum(dxmu1+dxmu2, axis=0)


    dx2 = 1. /N * np.ones((N,D)) * dmu


    dx = dx1 + dx2

    return dx, dgamma, dbeta

'''
function1
    - batch nomalization  역전파 함수
parameters
    - dout : batch의 gradient
    - cache : (xhat,gamma,xmu,ivar,sqrtvar,var,eps)
return
    - dx : x의 gradient 값
    - dgamma : gamma의 gradient 값
    - dmu : mu의 gradient 값
'''