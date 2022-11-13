# Quiz 72

### Python Code
```.py
class XORbit:
    def __init__(self, a:hex, b:hex):
        self.a = a
        self.b = b

    def compute(self):
        xor = self.a ^ self.b  # bitwise xor operation between a and b
        return hex(xor)[2:]  # return result in hexadecimal without prefix 0x


test1 = XORbit(a=0x3b101c091d53320c000910, b=0x071d154502010a04000419)
print(test1.compute())
```

### Test

<img width="660" alt="Screen Shot 2022-11-14 at 1 04 19 AM" src="https://user-images.githubusercontent.com/89366878/201531564-7d7d9d9c-f227-4b9b-a7bf-1c382e703468.png">
