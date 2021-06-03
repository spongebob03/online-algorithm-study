from math import gcd 

def solution(w,h):
    # 최대공약수 
    gcf = int(gcd(w,h))
    # 약분 
    abb_w = w//gcf
    abb_h = h//gcf 
    
    # 망가진 사각형 개수 
    messed_squares = (abb_w + abb_h - 1) * h // abb_h 
    
    return w * h - messed_squares
    