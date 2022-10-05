# Quiz 59

### Python Code

```.py
class Grid():
    def print():
        count = 1
        output = ''
        for n in range(5):  # 5 rows
            for i in range(5):  # 5 elements in each row
                output += str(count).center(5)  # center the grid
                count += 1
            print(output)  # print 1 row
            output = ''  # reset output to print next row

    def colored(r, g, b, text): # method to specify character colors using rgb notation
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    def print3d():
        count = 1
        output = ''
        for z in range(1,4):
            print(f'z{z}:')
            for n in range(5):  # 5 rows
                for i in range(5):  # 5 elements in each row
                    output += str(count).center(5)  # center the grid
                    count += 1
                colored_output = Grid.colored(255,0,0,output)
                print(colored_output)  # print 1 row
                output = ''  # reset output to print next row


test1 = Grid
test1.print()
test1.print3d()
```

### Test

