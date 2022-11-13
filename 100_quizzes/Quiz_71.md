# Quiz 71

### Python Code
```.py
class HextoAscii:
    def __init__(self, hexa:str):
        self.hexa = hexa

    def convert(self):
        hexbytes = []
        output = ''
        while self.hexa:  # break hexa string into bytes to convert
            hexbytes.append(self.hexa[:2])
            self.hexa = self.hexa[2:]

        counter = 1
        ascii = 0
        for byte in hexbytes:  # for each hexadecimal byte
            for digit in byte:  # for each digit in a byte, multiply by 16 to the increasing power
                if digit in 'qwertyuiopasdfghjklzxcvbnm':  # check if digit is a letter
                    digit = ord(digit) - 87  # if so convert to integer (a is 10, b is 11, etc)
                ascii += int(digit) * 16**counter
                counter -= 1
            output += chr(ascii)
            ascii = 0
            counter = 1
        return output


test1 = HextoAscii(hexa='48656c6c6f20576f726c64')
print(test1.convert())
```


### Test

