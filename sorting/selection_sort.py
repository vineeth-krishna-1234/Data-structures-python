def selection_sort(input_list):
    for i in range(len(input_list)):
        temp_var=input_list[i]
        temp_var_2=input_list.index(min(input_list[i:]))
        input_list[i]=input_list[temp_var_2]
        input_list[temp_var_2]=temp_var
    return("-".join(str(i) for i in input_list))
        
    
input_list =list(map(int,input("Enter the list values in a single line seperated by space:").split()))
print("The sorted array is: "+selection_sort(input_list))
