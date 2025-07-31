# def Remove(duplicate):
#      final_list=[]
#      for num in duplicate:
#           if num not in final_list:
#                final_list.append(num)
#           return final_list
# duplicate= [2,4,16,52,5,2,20,4,50]
# print(Remove(duplicate)) 
 
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

duplicate = [2, 4, 16, 52, 5, 2, 20, 4, 50]
print(Remove(duplicate))