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
        lines = '-----'
        list = '|'
        for n in self.queue:
            if n == self.queue[-1]:
                list += str(n)
            else:
                list += str(n) + ' | '
            for i in range(len(str(n))):
                lines += '-'
        print(lines)
        list += '|'
        print(list)
        print(lines)


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

