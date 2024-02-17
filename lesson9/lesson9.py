
"""9-dars"""
"""dictionary methods"""

import string
import random

# thisdict = {
#     "name": "BMW",
#     "model": "M3",
#     "color": "Green"
# }

# x = thisdict.get("model")
# print("============\n",x,"\n==============")


# d = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(d.keys()) #kalitlarni qaytaradi
# print("=================================")
# print(d.values()) #qiymatlarni qaytaradi
# print("=================================")
# print(d.items()) #itemlarni qaytaradi ya'ni key&value qaytaradi


# d["color"] = "Black" #dict ga qo'shadi
# d2 = dict().fromkeys(["a","b","c"]) #kalit yaratadi va qiymatini None ga tengledi
# print(d2)
# print(d)

# print(d.get("brand")) #get() metodi dict dan kalit qiymatini olib beradi
# print(d.get("color")) # agar biz getga mavjud bo'lmagan kalit bersak None qaytaradi

# for key in d:
#     print(d[key])
# print("========================================")
# for i in d.items():
#     print(i)

# for key in d:
#     if type(d[key]) == int:
#         d[key] = 0
#     print(d[key])    

# for key, val in d.items():
#     print(f"kalit=> '{key}' qiymat => '{val}'")


# alpha = {}
# print(string.ascii_lowercase)

# c = 1
# for i in string.ascii_lowercase:
#     alpha[i] = c
#     c +=1
# print(alpha)



# result = dict()

# for i in words:
#     result[i] = words.count(i)
# print(result)

# words = "python c++ php java javascript".split()

# def big_word(words):
#     mlength = 0
#     word = ""
#     for i in words:
#         if len(i) > mlength:
#             mlength = len(i)
#             word = i
#     print(word)
# big_word(words)


# d = []

# def random_num(r):
#     for i in range(10):
#         r = random.randint(0, 100)
#         d.append(r)
#     print(d)
# random_num(d)


dict = {
    "users":[
        {"name":"Olim", "score":10},
        {"name":"David", "score":30},
        {"name":"Anvar", "score":20},
        {"name":"Zokir", "score":60},
        {"name":"Botir", "score":50},
        {"name":"Zayt", "score":80},
    ]
    }
success = []
fail = []


for i in dict["users"]:
    if i["score"] >= 50:
        success.append(i)
    else:
        fail.append(i)
print(success)
print(fail)