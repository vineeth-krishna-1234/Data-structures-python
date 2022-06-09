def bubble_sort(input_list):
    n=len(input_list)
    for i in range(n):
        for j in range(n-i-1):
           if input_list[j]>input_list[j+1]:
               input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
    return(input_list)
input_list=list(map(int,input("Enter the list values seperated by space:").split()))
print(*bubble_sort(input_list))
