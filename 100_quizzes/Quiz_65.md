# Quiz 65

### Python Code

```.py
class Cascade():
    def __init__(self, number, water):
        self.number = number
        self.water = water
        self.spaces = ''

    def print(self):
        for i in range(self.number):
            print(self.spaces + self.water)
            self.spaces += " "
        return ''


test1 = Cascade(number=int(input()), water=input())
print(test1.print())
```

### Test

<img width="658" alt="Screen Shot 2022-10-24 at 9 51 23 AM" src="https://user-images.githubusercontent.com/89366878/197427534-fa7d2008-2984-484d-ac06-46df33c70a26.png">
