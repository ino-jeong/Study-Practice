'''
A[n] = flat end : 
|
|

B[n] = updide or downside end :
|            |
 |    or    |

C[n] = center end:
|
 |
|


A[n] = A[n-1] + A[n-2] + 2 * B[n] + C[n-1]
B[n] = A[n-1] + B[n-1]
C[n] = A[n-1] + C[n-2]

'''

def tiling(n, A, B, C):
    if n in A:
        return A[n]

    for i in range(3,n+1):
        if i in A:
            continue

        B[i] = A[i - 1] + B[i - 1]
        C[i] = A[i - 1] + C[i - 2]
        A[i] = A[i - 1] + A[i - 2] + 2 * B[i - 1] + C[i - 1]

    return A[n]

cases = int(input())
A = {}
A[1] = 1
A[2] = 5

B = {}
B[1] = 1
B[2] = 2

C = {}
C[1] = 1
C[2] = 1

for c in range(cases):
    n = int(input())
    print(tiling(n, A, B, C))

