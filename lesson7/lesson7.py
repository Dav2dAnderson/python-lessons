# List nima? List bu tartibli to'plam

# l = [15,88,90]
# l.insert(1, "ok")
# print(l)

# l = list(range(1,101)) # 1 dan 100 gachab bo'gan sonlarni list yaratib joylaydi
# l.reverse() # 1 dan 100 gacha bo'lgan sonlarni teskachi machasi chiqarib beradi
# print(l)

# l2 = [2,1,4,5,6,8,7,9,10]
# l2.sort() # List dagi sonlarni tartibli qilib beradi
# l2.sort(reverse=True) # Listdagi sonlarni tartibli qilib teskari machasi qilib beradi
# print(l2)


# l4 = [-1,8,4,7,67,-12]
# l5 = []
# for i in l4:
#     if i < 0:
#         l5.append(0)
#     else:
#         l5.append(i)
# print(l5)


l6 = ["a",1,2,3,"b","c",9,7,"d"]
l7 = []
for i in l6:
    if type(i) == str:
        l7.append(0)
    else:
        l7.append(i)
print(l7)


# def replace_str(el):
#     if type(el) == str:
#         return 0
#     return el
# l = ["a",1,2,3,"b","c",9,7,"d"]
# l2 = filter(replace_str, l)
# print(list(l2))



# l8 = [-1,8,43,75,-12]
# for obj_index, el in enumerate(l8):
#     if el <0:
#         l8[obj_index] = 0
# print(l8)


# t = ("python", "java")
# print(t.index('java'))
# t = tuple("Python")
# print(t)



# f = [2,4,5,6]
# def a(el):
#     return el ** 2
# f2 = map(a, f)
# print(list(f2))



# l = ["assalom", "olma", "nok", "kiwi", "agile"]

# def sort_a(obj_list: list) -> list:
#     l2 = []
#     for i in obj_list:
#         if type(i) == str and i[0].lower == "a":
#             l2.append(i)
#     return l2
# print(sort_a(l))

