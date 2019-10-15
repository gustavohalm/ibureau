def rotate(arr, k):
    new_arr = []
    while k >=1:
        for i in range(0, len(arr)-1 ):
            element = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = element    
            #1 2 3 4 / 2 1 3 4 / 2 3 1 4 / 2 3 4 1  
        k -= 1 
    return arr

arr = list( map(int, input().split()) )
k = int(input())
print(rotate(arr, k))