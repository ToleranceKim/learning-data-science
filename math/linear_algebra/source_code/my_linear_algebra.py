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

# vector_calculations

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

# matrix_calculations

def add(A, B):
    """
    행렬의 덧셈
    입력값 : 행렬의 덧셈을 수행할 행렬 A, B
    출력값 : 행렬 A와 행렬 B의 덧셈 결과인 행렬 C
    """
    
    n = len(A)
    p = len(A[0])
    
    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = A[i][j] + B[i][j]
            row.append(val)
        res.append(row)
    return res

def subtract(A, b):
    n = len(A)
    p = len(A[0])
    
    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = A[i][j] - B[i][j]
            row.append(val)
        res.append(row)
    return res

def scalar_mul(b, A):
    """
    행렬의 스칼라 곱
    입력값 : 스칼라 곱을 수행할 스칼라 b, 행렬 A
    출력값 : 스칼라 b와 행렬 A의 스칼라 곱 결과인 행렬 C
    """
    
    n = len(A)
    p = len(A[0])
    
    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = b * A[i][j]
            row.append(val)
        res.append(row)
    return res

def ele_product(A, B):
    """
    행렬의 원소 곱
    입력값 : 행렬의 원소 곱을 수행할 행렬 A, B
    출력값 : 행렬 A와 행렬 B의 원소 곱 결과인 행렬 C
    """
    
    n = len(A)
    p = len(A[0])
    
    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = A[i][j] * B[i][j]
            row.append(val)
        res.append(row)
    return res

def matmul(A, B):
    """
    행렬의 행렬 곱
    입력값 : 행렬 곱을 수행할 행렬 A, B
    출력값 : 행렬 A와 행렬 B의 행렬 곱 결과인 행렬 res
    """
    
    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    
    res = []
    for i in range (0, n):
        row = []
        for j in range(0, p2):
            val = 0
            for k in range(0, p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res

# matrix_properties

def transpose(A):
    """
    행렬의 전치 행렬
    입력값 : 전치 행렬을 구하고자 하는 행렬 A
    출력값 : 행렬 A의 전치 행렬 At
    """
    n = len(A)
    p = len(A[0])
    
    At = []
    for i in range(0, p):
        row = []
        for j in range(0, n):
            val = A[j][i]
            row.append(val)
        At.append(row)
    return At

def diag(A):
    """
    행렬의 대각 행렬
    입력값 : 대각 행렬을 구하고자 하는 행렬 A
    출력값 : 행렬 A의 대각 행렬 D
    """
    n = len(A)
    D = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(A[i][j])
            else:
                row.append(0)
        D.append(row)
    return D

def diag_ele(A):
    """
    대각 원소 구하기
    입력값 : 대각 원소를 구하고자 하는 행렬 A
    출력값 : 행렬 A의 대각 원소 리스트 d
    """
    n = len(A)
    d = []
    for i in range(0, n):
        d.append(A[i][i])
    return d

def ele2diag(a):
    """
    대각 원소 -> 대각 행렬 변환
    입력값 : 대각 원소 리스트 a
    출력값 : 대각 원소 a를 이용해 생성한 nxn 대각 행렬 D
    n : 대각 원소 리스트 a의 길이
    """
    n = len(a)
    D = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(a[i])
            else:
                row.append(0)
        D.append(row)
    return D

def identity(n):
    """
    단위 행렬 생성
    입력값 : 단위 행렬의 크기 n
    출력값 : nxn 단위 행렬 I
    """
    I = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    return I