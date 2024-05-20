#nested loops
# nested loop in general concept having one loop inside of another loop!
#nested loop = the 'inner loop' will finish all it's iterations before finishing one iteration of the 'outer loop'

#let's create user prompt

rows = int(input("how many rows?:"))
columns = int(input("how many colmns?:"))
symbols = input("what is the symbol to use?:")

for i in range(rows):
   for j in range(columns):
        print(symbols,end="")
   print()

# loop control statements(break,continue,pass)

# loop control = to change a loops execution from it's normal seqence!

# break = terminates the loop entirely
# continue = skips to next iteration of the loop
# pass = does nothing, acts as a place holder!

while True:
    name = input("Enter your name:")
    if name !="":
        break


phone_number = "180-224-6786"
for i in phone_number:
    if i =="-":
        continue
    print(i,end="")

name = "xiang_tzu_xian_zhou"
for i in name:
    if i =="_":
        continue
    print(i,end="")

#pass statement!

for i in range(10,20):
    if i == 13:
        pass
    else:
         print(i)

name = "xian_tzu_xian_zhou"
for i in name:
    if i == "_":
        continue
    print(i,end="")

while True:
    name = input("enter your name:")
    if name!="":
        break

for i in range(10):
    if i == 4:
        pass
    else:
        print(i)
