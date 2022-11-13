# Quiz 69

### Python Code

```.py
def changeorder(words:str):
    words = words.split(' ')
    output = ''
    for word in words:
        output = word + " " + output
    return output


test1 = changeorder("Hello World!")
test2 = changeorder("Comp Sci!")
print(test1)
print(test2)
```

### Test

<img width="656" alt="Screen Shot 2022-11-14 at 12 12 40 AM" src="https://user-images.githubusercontent.com/89366878/201528987-1d01b5e5-3fd6-442b-8595-230e7ebe7f45.png">
