# Queue Construction

### Python Code

```.py
'''Implementation'''
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return 'None'
        else:
            return self.queue.pop(0)

    def empty(self):
        if not self.queue:
            return 'False'
        else:
            return 'True'

    def __repr__(self):
        lines_length = 0
        list = ''
        for n in self.queue:
            if n == self.queue[-1]:
                list += str(n)
            else:
                list += str(n) + ' | '
            lines_length += len(str(n)) + 3
        lines = '-' * (lines_length+1)
        if not self.queue:
            return 'None'
        else:
            return f"{lines} \n| {list} |\n{lines}"


'''Interface'''
test1 = Queue()  # create queue
print(test1.dequeue())  # test dequeue without any values in the queue
print(test1.empty())  # check if queue has any values
test1.enqueue(13)  # append 13 to the end of the list
test1.enqueue(293)  # append 293 to the end of the list
print(test1)  # test repr to print all values in the queue
print(test1.empty())  # check if queue has any values
print(test1.dequeue())  # return and remove the first value in the queue
print(test1.dequeue())  # return and remove the first value in the queue
print(test1)  # test repr without any values in the queue
test1.enqueue('America')
test1.enqueue('Ryu')
print(test1)
```

### Test

<img width="872" alt="Screen Shot 2022-10-18 at 12 05 43 PM" src="https://user-images.githubusercontent.com/89366878/196333055-9a7bb0cc-8b68-428d-b073-ef50a4ec4bce.png">
