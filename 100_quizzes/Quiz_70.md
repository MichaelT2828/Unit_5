# Quiz 70

### Python Code
```.py
def truth_table():
    print("|A|B|C|AB+(not B)+(not BC)|")  # print the column headers
    for i in range(8):  # repeat for the 8 rows that represent the combinations of three variables
        binary = bin(i)[2:]  # take the row number in binary
        while len(binary) < 3:  # add appropriate "0"s to binary number to make sure each number is 3 digits
            binary = "0"+binary
        A, B, C = binary[0] == "1", binary[1] == "1", binary[2] == "1"  # convert integer to boolean
        result = int(not B or C)  # solve boolean equation and convert back to integer

        print(f"|{binary[0]}|{binary[1]}|{binary[2]}|", end="")
        print(f"{result}".center(19), end="")  # print centered result in column
        print("|")


truth_table()
```

### Test

<img width="656" alt="Screen Shot 2022-11-14 at 12 26 31 AM" src="https://user-images.githubusercontent.com/89366878/201529783-2f8a25df-caec-4e2a-a262-f2b3e27873bc.png">
