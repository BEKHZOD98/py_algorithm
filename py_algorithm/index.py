def sel_sort(A):  #선택 정력
    n=len(A)      #n: list의 A의 길이
    for i in range(n-1): #agar topsa qogani davom etadigan for loopi
        least = i
        for j in range(i+1,n): #eng kichkina index ni topadigan for loop
            if(A[j]<A[least]): #비교 연산
                least=j         #최소 항목 갱신 
        A[i], A[least] = A[least], A[i] #배열 항목 교환
        printStep(A, i + 1)     #중간 과정 출력용 문장 

def printStep(arr, val) :
    print(" Step %2d = " %val, end='')
    print(arr)
data = [5,9,656,4565,1,164,1]
print("Original :" , data)
sel_sort(data)
print("Selection: ", data)

