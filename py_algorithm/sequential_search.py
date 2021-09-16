def seq_search(A,key):
    for i in range(len(A)):
        if A[i] == key:
            return 1
        return -1
A_data = [32,14,5,17,23,9,11,4,26,29]
print("32찾기: ",seq_search(A_data, 32))
print("29찾기: ",seq_search(A_data, 29))