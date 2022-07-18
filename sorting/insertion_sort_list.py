user_input_list=list(map(int,input("Enter the list seperated by spaceKO").split()))
for iterator in range(1,len(user_input_list)):
    key_poniter=user_input_list[iterator]
    j=iterator-1
    while j>=0 and key_poniter<user_input_list[j]:
        user_input_list[j+1]=user_input_list[j]
        j=j-1 
    user_input_list[j+1]=key_poniter
print(user_input_list)