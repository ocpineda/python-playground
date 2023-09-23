# hello world
print("hello");

# get area
width = 20
height = 10
area = width * height
print(area)

# if-else
x = 0
if x < 0:
    print('less than zero')
elif x > 0:
    print('greater than zero')
elif x == 0:
    print("equal to zero")
else:
    print('what the what??')

#for loop. i is cast to str because of concatenation
ceiling = 20
for i in range(5):
    print('I have this(' + str(i) + ')')

# print('Hi, what\'s you password?')
# password = input()
# print('your access is granted for pass' + str(password))

# answer should be 5050. For sum of 0 to 100. Notice range is 101. 
# range(start, stop, step)  stop position is not included so 101 instead of 100
total = 0
for num in range(101):
    total = total + num
print('Sum of all number from 1 - 100 with a for loop: ' + str(total))

# the same thing as above with a while loop
total = 0
counter = 0
while counter <= 100:
    total = total + counter
    counter = counter + 1
print('Sum of all number from 1 - 100 with a while loop: ' + str(total))