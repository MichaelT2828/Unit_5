# Quiz 66

### Python Code

```.py
class PlusSquare:
    def __init__(self, length):
        self.length = length

    def printSquare(self):
        print(self.length)
        for i in range(self.length):
            print(self.length*'+')


test1 = PlusSquare(length=5)
test2 = PlusSquare(length=25)
test3 = PlusSquare(length=12)
test4 = PlusSquare(length=9)
test1.printSquare()
test2.printSquare()
test3.printSquare()
test4.printSquare()
```

### Test

