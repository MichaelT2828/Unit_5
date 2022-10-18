# Array Construction

### Python Code
```.py
import random

'''Implementation'''
class Array():
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        # above notation is the same as:
        # self.data = []
        # for x in range(size):
        #   self.data.append(None)
        self.size = size

    def insert(self, index, value):
        if self.size < index or index < 0:
            print(f'\33[0;31m[Array] Index out of bounds\033[00m')
            return
        self.data[index] = value

    def indexing(self, index):
        if self.size < index or index < 0:
            print(f'\33[0;31m[Array] Index out of bounds\033[00m')
            return
        return self.data[index]

'''Random array of 10'''
test = Array(size=10)
grid = ''
for i in range(10):
    test.insert(index=i, value=random.randint(1,100))
    grid += str(test.indexing(i)).center(10)
print('Random array of 10 elements:')
print(grid)

'''5x5 Grid'''
test2 = Array(size=25)
for i in range(25):
    test2.insert(index=i, value=i+1)
grid2 = ''
count = 0
print("5x5 Array:")
for i in range(5):
    for n in range(5):
        grid2 += str(test2.indexing(n+count)).center(5)
    count += 5
    print(grid2)
    grid2 = ''
```

### Test

<img width="924" alt="Screen Shot 2022-10-18 at 12 38 24 PM" src="https://user-images.githubusercontent.com/89366878/196336758-c5f3f4c7-f950-46c6-8f7d-7058ca69b0c4.png">
