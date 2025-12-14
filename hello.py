#day 1 (goal: bikin band name generator)
# input itu digunakan untuk mengambil input dari user
input("what is your name?")
print("hello " + input("what is your name?"))

# len itu digunakan untuk menghitung panjang dari sebuah string
print(len("hello"))

#variabel digunain untuk referein ke suatu nilai
name = input("what is your name?")
print("hello " + name)
#atau
name = input("what is your name?")
length = len(name)
print(length)

#project 1
print("welcome ke band name generator!")
city = input("what city did you grow up in?\n")
pet = input("what is your pet's name?\n")
print("your band name could be " + city + " " + pet)
