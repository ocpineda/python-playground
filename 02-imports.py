import random
import sys


# use random import
for i in range(5):
    print(random.randint(1,10))

# use sys import
while True:
    print('type exit to exit')
    response = input()

    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')

