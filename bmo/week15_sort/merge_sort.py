def mergesort(n,S):
    h=n//2
    m=n-h
    if(n>1):
        U = S[:h]
        V = S[h :]
        print("split into two sets->",U,V)
        mergesort(h,U)
        mergesort(m,V)
        merge(h,m,U,V,S)

def merge(h,m,U,V,S): #U,V 배열 합쳐서 ->S
    #h,m은 배열 원소개수.
    i,j,k=0,0,0
    print("before merge",U,V)
    while(i<h and j<m):
        if(U[i]<V[j]):
            S[k]=U[i] #합치는 S[k]요소 더 작은 수로 대체
            i+=1
        else:
            S[k]=V[j]
            j+=1
        k+=1
    if(i>=h): #U리스트 다 돈면 남은 V의 요소 그대로 S에
        S[k:]=V[j:]
    else: #V리스트 다 돈거
        S[k:]=U[i:]
    print("mergesort->",S)


nlist=[15,20,35,7,19,78,45,36]#정렬되지 않은 배열
mergesort(len(nlist),nlist)