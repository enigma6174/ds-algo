from python.data_structure.array import Array
from python.data_structure.stack import ArrayStack, LinkedStack


def test_linked_stack():
    stack = LinkedStack()
    
    print(stack.is_empty())
    
    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    
    print(stack.is_empty())
    
    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")
    
    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")
    
    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")
    
    print(f"pop(): {stack.pop()}")
    print(f"peek(): {stack.peek()}")
    print(f"size(): {stack.size()}")
    
    stack.push(99)
    stack.push(11)
    stack.push(121)
    stack.push(1331)
    stack.push(729)
    stack.push(625)
    
    print(f"peek(): {stack.peek()}")
    print(f"size(): {stack.size()}")


def test_array_stack():
    stack = ArrayStack()

    print(stack.is_empty())

    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    print(stack.is_empty())

    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")

    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")

    print(f"size(): {stack.size()}")
    print(f"peek(): {stack.peek()}")

    print(f"pop(): {stack.pop()}")
    print(f"peek(): {stack.peek()}")
    print(f"size(): {stack.size()}")

    stack.push(99)
    stack.push(11)
    stack.push(121)
    stack.push(1331)
    stack.push(729)
    stack.push(625)

    print(f"peek(): {stack.peek()}")
    print(f"size(): {stack.size()}")


test_linked_stack()
