#1st question
def count(str):
    vowels=0
    consonents=0
    vowel="aeiou"
    for i in str:
        if i in vowel:
            vowels+=1
    consonents=len(str)-vowels
    print(f'number of consonents in {str} = {consonents}')
    print(f'number of vowels in {str} = {vowels}')

#2nd question
def matmul(A,B):
     rows_A=len(A)
     cols_A=len(A[0])
     rows_B=len(B)
     cols_B=len(B[0])
     if cols_A == rows_B:
        C=[[0 for i in range(cols_B)] for j in range(rows_A)]
        for i in range(cols_A):
               for j in range(rows_B):
                    for k in range(cols_A):
                        C[i][j]+=A[i][j]*B[j][i]
        print(C)
     else:
          print("cannot multiply mattrices")

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

matmul(X,Y)

#3st question
def common(A,B):
    A=set(A)
    B=set(B)
    count=A & B
    print(len(count))

l1=[2,0,0,0]
l2=[2,3,1,0]
common(l1,l2)
common(l2,l1)

#4th question
def transpose(A):
    for i in range(len(A)):
        for j in range(len(A)):
                if(i>j):
                     temp=A[i][j]
                     A[i][j]=A[j][i]
                     A[j][i]=temp
                     
    print(A)

X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

Y = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

transpose(X)
