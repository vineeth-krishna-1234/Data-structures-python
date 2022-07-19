from turtle import right


def Merge_sort(array):
    if len(array)>1:
        mid=len(array)//2
        left_subarray=array[:mid]
        right_subarray=array[mid:]
        Merge_sort(left_subarray)
        Merge_sort(right_subarray)
        left_array_iterator=right_array_iterator=argument_array_iterator=0
        while left_array_iterator<len(left_subarray) and right_array_iterator<len(right_subarray):
            if left_subarray[left_array_iterator]<right_subarray[right_array_iterator]:
                array[argument_array_iterator]=left_subarray[left_array_iterator]
                left_array_iterator+=1
            else:
                array[argument_array_iterator]=right_subarray[right_array_iterator]
                right_array_iterator+=1
            argument_array_iterator+=1
        
        while left_array_iterator<len(left_subarray):
            array[argument_array_iterator]=left_subarray[left_array_iterator]
            left_array_iterator+=1
            argument_array_iterator+=1

        while right_array_iterator<len(right_subarray):
            array[argument_array_iterator]=right_subarray[right_array_iterator]
            right_array_iterator+=1
            argument_array_iterator+=1



user_input_list=list(map(int,input("Enter the list seperated by space").split()))
Merge_sort(user_input_list)
print(user_input_list)
