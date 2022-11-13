# Quiz 70

### Python Code
```.py
def truth_table(equation):
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


truth_table("not B+C")
```

### Test

