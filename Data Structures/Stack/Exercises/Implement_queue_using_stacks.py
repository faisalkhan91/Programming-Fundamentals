"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the
functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    - void push(int x) Pushes element x to the back of the queue.
    - int pop() Removes the element from the front of the queue and returns it.
    - int peek() Returns the element at the front of the queue.
    - boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

    -You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is
    empty operations are valid.
    -Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque
    (double-ended queue) as long as you use only a stack's standard operations.


Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Constraints:

    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words,
performing n operations will take overall O(n) time even if one of those operations may take longer.
"""



class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def __str__(self):
        return str.__dict__

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.input_stack:
            return None
        else:
            length = len(self.input_stack)
            for i in range(length):
                self.output_stack.append(self.input_stack.pop())
            popped = self.output_stack.pop()
            for i in range(length-1):
                self.input_stack.append(self.output_stack.pop())
            return popped

    def peek(self) -> int:
        if not self.input_stack:
            return None
        else:
            length = len(self.input_stack)
            for i in range(length):
                self.output_stack.append(self.input_stack.pop())
            popped = self.output_stack.pop()
            for i in range(length-1):
                self.input_stack.append(self.output_stack.pop())
            return popped

    def empty(self) -> bool:
        if self.input_stack == [] and self.output_stack == []:
            return True
        else:
            return False


# Declaration

myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
myQueue.push(3)
myQueue.peek()  # return 1
myQueue.peek()  # return 1
myQueue.pop()  # return 1, queue is [2]
myQueue.empty()  # return false
print(myQueue.input_stack)
print(myQueue.output_stack)


# This is the implementation with one stack but not used here as the problem requires us to use 2 stacks to implement a
# queue.
# class MyQueue:
#
#     def __init__(self):
#         self.data = []
#
#     def push(self, x: int) -> None:
#         self.data.append(x)
#
#     def pop(self) -> int:
#         to_return = self.data[0]
#         self.data.pop(0)
#         return to_return
#
#     def peek(self) -> int:
#         return self.data[0]
#
#     def empty(self) -> bool:
#         if self.data == 0:
#             return True
#         else:
#             return False
