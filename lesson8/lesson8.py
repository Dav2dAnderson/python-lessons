# import string
# s = "Py#h$on"
# d = []
# for i in s:
#     if i in string.punctuation:
#         d.append(i)
# print(d)


"""
8-dars: Dict
"""

# user = dict(name="David", surname="Anderson", age=15)
# print(user["name"]) #user ning ismini olish(to'rtburchak qavsning ichiga kalit beriladi)
# user["age"] = 14 #userning yoshini o'zgartiradi yoki qo'shadi(agar bunday kalit yo'q bo'lsa)
# print(user)
# del user["surname"] #user ning surname ini o'chiradi


# men = {"name": "Davronbek",
#         "surname": "Nazarov",
#         "age": 15, 
#         "adress":"Uzbekistan, Fergana",
#         "email": "dav2danderson@gmail.com"}
# print(men)


fruits = {
    "banan":{"price":25000, "kg":23},
    "olma":{"price":15000, "kg":30},
    "mandarin":{"price":12000, "kg":25},
    "limon":{"price":30000, "kg":50},
    "kiwi":{"price":40000, "kg":32},
    "ananas":{"price":50000, "kg":8},
    "shaftoli":{"price":140000, "kg":12}
}

print("Assalomu Aleykum, do'konimizga hush kelibsiz!.")
income = {"overal_summa":0}


while True:

    user_choice = input("Meva nomini kiriting: ")
    
    if user_choice.lower() not in fruits:
        print("==============\n",user_choice, "Yo'q", "\n===============")

    else:
        print("==================\n",user_choice, "bor\n1kg-narxi:", fruits[user_choice]['price'],"\n===================")
        kg = input("Necha kg kerak:")
        if kg.isdigit():
            print("IsDigit ishladi")
            kg = int(kg)
            if kg <= fruits[user_choice]['kg']:
                print("Omborxonada bor")
                summa = kg * fruits[user_choice]['price']
                income["overal_summa"] += summa
                print(summa)
                fruits[user_choice]['kg']-=kg
            else:
                print(f"{user_choice} dan {kg} kilo qomagan.")
        if user_choice.lower() == "stop": 
            if income["overal_summa"] > 0:
                print('Sizdan', income["overal_summa"],"-sum")
            break

