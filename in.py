#day 2 (tip calculator)

#data types

#string
# print("hello"[0])
# print("hello"[4])
#disebut subscript yg kata ke- diatas

#integer
# operasi math
# print(123 + 345)
#cth:123_456_789.kita bisa tulis beri "_" biar mudah dibaca

#float (flooating number kek desimal)
# print(3.14159)
#boolean
# print(True)
# print(False)    

# name = input("what is your name")
# y = len(name)
# x = str(y)
# print("your name has " + x + " characters")

# a = float(123)
# print (type(a))

# print (str(70) + str(100.5))

angka_dua_digit = input("Masukkan angka dua digit: ")
if len(angka_dua_digit) == 2 and angka_dua_digit.isdigit():
    first_digit = angka_dua_digit[0]
    sec_digit = angka_dua_digit[1]
    print(int(first_digit) + int(sec_digit))
else:
    print("Input harus berupa dua digit angka.")