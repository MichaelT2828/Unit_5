# Stack Construction

### Python Code
```.py
from random import randint

class Stack():
    def __init__(self):
        self.stack = []

    def colored(self, r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    def pop(self): # take the last value out
        output = self.stack[-1]
        self.stack = self.stack[:-1]
        return output

    def push(self, value): # insert value at the end
        self.stack.append(value)
        return self.stack

    def empty(self): # check if list is empty
        return self.stack == []

    def __repr__(self):
        output = ''
        for a in self.stack:
            output += Stack.colored(self=self, r=randint(0,256), g=randint(0,256), b=randint(0,256), text=str(a))
        return output


test1 = Stack()
print(test1.push(345))
print(test1.push(24954))
print(test1.push("Hello World"))
print(test1.push("sfodsifjosodfmofijsmofijdm"))
print(test1)
print(test1.pop())
```

### Test

<img width="868" alt="Screen Shot 2022-10-18 at 12 34 17 PM" src="https://user-images.githubusercontent.com/89366878/196336275-5fed5e83-9d41-4cee-8f55-bb44222f8ab6.png">
