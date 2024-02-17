

# s = "          olma "
# print(s)
# print(s.strip())


# x = "page: salom"
# print(x.replace('page:', "*"))


# a = "page olmapage page"
# print(a.replace(" ","").isalpha())


# def date():
#     """Bugungi sanani aniqlab beruvchi funksiya"""
#     t = datetime.date.today()
#     print("=========\n", t, "\n==========")
#     return t
# result = date()
# print("9-qator", result)


# def toupper():
#     """To'liq ismimizni hamma harfini katta o'tkazib beruvchi funksiya"""
#     i = input("Enter Fullname: ")
#     print(i.upper())
# print(toupper.__doc__) #funksiyaning komentini chiqarib beradi
# toupper()

# surname = input("Your surname: ")
# print(surname.upper())


# def to_lower(value1, value2):
#     return value1.lower(), value2.lower()
    
# surname= input("Surname: ")
# firstname = input("Firstname:")
# a = to_lower(surname, firstname)
# print(a)



# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# def big_number(a,b):
#     if a > b:
#         print(a, "Katta")
#     else:
#         print(b, "katta")
# big_number(a, b)


# def katta_son(x,y):
#     if type(x) == int and type(y) == int:
#         return max(x,y)
#     else:
#         return False
# n = 15
# i = 18
# r = katta_son(n, i)
# print(r)

# def test(x, y, *args, **kwargs):
#     print(x,y, args, kwargs)
#     return False
# r = test(1,2, 3,4,5,6,78, ism="David")
# test()



# s = input("So'z kiriting: ")
# def satr(s):
#     if type(s) == str:
#         x = (s[::-1])
#         return x
#     else:
#         return False
# r = satr(s)
# print(r)



