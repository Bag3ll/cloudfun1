
Hw = "Hello world!"
print(Hw)

print(len(Hw))

print(Hw[0])

print(Hw[-1])

print(Hw[-2])

print(Hw[2:])   # print all string from 3rd char onward

print(Hw[-3:])  # print last 3 char of string

print(Hw[1:4])

spaces = "    spaces     "
print(len(spaces.strip()))

text = "here is some Text with Some words of text"
print(text.count("text"))
print(text.lower())
print(text.capitalize())
print(text.replace(" with", ","))

x = 2
y = 5.4
z = " there 25.4 unless we space"
print(str(x) + str(y) + z)
# make them all strings

intS = "6"
print(type(int(intS)))

name = "lass"
years = 7
height = 60.2
print(f'{name} is {years * 7} years old and {height} cm tall')

