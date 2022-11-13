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

