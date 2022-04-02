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


"""
This is the implementation of a queue using 2 stacks. Using 2 stacks is not uncommon in the industry as this can speed
up the performance in case of read and write, specially if one of the stack is in use.

In this solution the queue can be implemented using 2 stacks but either one of the operations i.e. enqueue or dequeue,
depending on how the solution is implemented will be O(n). In the solution below the dequeue (pop) is implemented as
O(n).
"""


# Implementation of myqueue class.
class MyQueue:
    def __init__(self):
        self.input_stack = []  # Initialization of the stack that will hold all the data.
        self.output_stack = []  # Initialization of the stack that will be used during dequeue operation.

    def __str__(self):
        return str.__dict__

    # Enqueue into the input stack.
    def push(self, x: int) -> None:
        self.input_stack.append(x)

    # Dequeue the stack by pushing all the popped elements from the input stack into the output stack and then popping
    # the last element of the output stack which is basically the first item in the queue and then pushing all the
    # elements back into the input stack.
    def pop(self) -> int:
        if not self.input_stack:  # If the input stack is empty.
            return None
        else:
            length = len(self.input_stack)
            # In this loop move all the elements from input stack to output stack, so that the first pushed item becomes
            # the top.
            for i in range(length):
                self.output_stack.append(self.input_stack.pop())
            popped = self.output_stack.pop()  # Pop the top element
            # Move all the elements back into the input stack in the original order minus the popped item.
            for i in range(length-1):
                self.input_stack.append(self.output_stack.pop())
            return popped

    # Method to peek into the queue, we are just using the array index to see the first item in the queue.
    def peek(self) -> int:
        if not self.input_stack:
            return None
        else:
            print("Peek:", self.input_stack[0])
            return self.input_stack[0]

    # Method to check if the queue is empty.
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
