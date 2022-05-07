num_list = []
length_of_num_list = 9
for i in range(length_of_num_list):
    num_list.append(int(input()))
max_value = max(num_list)
position_of_value = num_list.index(max_value) + 1

# max_value = 0
# position_of_value = 0
# for index in range(length_of_num_list):
#     if max_value < num_list[index]:
#         max_value = num_list[index]
#         position_of_value = index + 1

print(max_value)
print(position_of_value)
