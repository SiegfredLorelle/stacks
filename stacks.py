import array as arr

class Stack:
    def __init__(self, *elements):
        self.stack = arr.array("l", elements)
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def display(self):
        [print(data) for data in arr.array("l", reversed(self.stack))]



class App:
    def __init__(self):
        ...

if __name__ == "__main__":
    stack1 = Stack(3,2,1,4)
    stack1.display()
    stack1.pop()
    print("THEN")
    stack1.push(3)
    stack1.display()

    print("THEN")
    stack1.push(5)
    stack1.push(-1)
    stack1.display()
    print("THEN")
    stack1.pop()
    stack1.display()

