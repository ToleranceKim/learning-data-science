def zero_mat(n, p):
    """
    영 행렬 생성
    입력값 : 생성하고자 할 영 행렬의 크기 n행, p열
    출력값 : (n x p) 영 행렬 Z
    """
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z

def deepcopy(A):
    """
    깊은 복사(deepcopy) 구현
    입력값 : 깊은 복사를 하고자 하는 행렬 리스트 A
    출력값 : 깊은 복사된 결과 행렬 리스트 res
    """
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(0, n):
            for j in range(0, p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(0, n):
            res.append(A[i])
        return res


def v_add(u, v):
    """
    입력값 : 연산하고자하는 벡터 u, v
    출력값 : 벡터 u,v의 연산 결과
    """
    n = len(u)
    w = []
    
    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)
        
    return w

def v_subtract(u, v):
    n = len(u)
    w = []
    
    for i in range(0, n):
        val = u[i] - v[i]
        w.append(val)
    return w

def scalar_v_mul(a, u):
    """
    벡터의 스칼라 곱
    입력값 : 스칼라 a, 벡터 리스트 u
    출력값 : 스칼라 a와 벡터 리스트 u의 곱 결과 w
    """
    n = len(u)
    w = []
    
    for i in range(0, n):
        val = a * u[i]
        w.append(val)
    
    return w

def v_mul(u, v):
    """
    벡터의 원소 연산
    입력값 : 원소와 연산하고자 하는 벡터 리스트 u , v
    출력값 : 벡터 u, v의 원소 곲 결과 w
    """
    n = len(u)
    w = []
    
    for i in range(0, n):
        val = u[i] * v[i]
        w.append(val)
        
    return w

def v_div(u, v):
    n = len(u)
    w = []
    
    for i in range(0, n):
        val = u[i] / v[i]
        w.append(val)
        
    return w