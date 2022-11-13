# Quiz 68

### Python Code

```.py
def rocket(distance, time, velocity, fuel, fuel_consumption):
    output = "Welcome to Mars"
    A = distance > velocity * time
    B = distance > fuel * fuel_consumption
    if A and not B:
        output = "Failure, Not enough time"
    if B and not A:
        output = "Failure, Not enough fuel"
    if A and B:
        output = "Failure, Not enough time"
    return output


test1 = rocket(100, 100, 10, 100, 100)
test2 = rocket(50, 70, 100, 10, 2)
print(test1)
print(test2)
```

### Test

<img width="660" alt="Screen Shot 2022-11-14 at 12 05 07 AM" src="https://user-images.githubusercontent.com/89366878/201528640-c1b2360e-7305-4acf-9d46-19837d79cb6a.png">
