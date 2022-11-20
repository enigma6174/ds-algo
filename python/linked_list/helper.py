from python.data_structure.linkedlist import LinkedList, DoublyLinkedList


# Helper function to test the singly linked list
def run_ll():
    print("LINKED_LIST_1\n")

    list1 = LinkedList()
    print(f"linked_list empty? {list1.is_empty()}")

    list1.insert_at_head(10)
    list1.insert_at_head(20)
    list1.insert_at_head(30)

    list1.print_list()

    list1.insert_at_tail(0)
    list1.insert_at_tail(-10)

    list1.print_list()

    print("\nLINKED_LIST_2\n")

    list2 = LinkedList()
    list2.insert_at_head(10)
    list2.insert_at_tail(20)
    list2.insert_at_tail(30)
    list2.insert_at_head(0)

    list2.print_list()
    print(f"linked_list empty? {list2.is_empty()}")

    print("\nLINKED_LIST_3\n")

    list3 = LinkedList()
    list3.insert_at_tail("hello")
    list3.insert_at_tail("world")
    list3.insert_at_tail("data structures")
    list3.insert_at_tail("algorithms")
    list3.insert_at_tail("python")
    list3.print_list()

    print(f"linked_list empty? {list3.is_empty()}")
    print("search_key: python ?", list3.search("python"))
    print("search_key: python ?", list3.search("hello"))
    print("search_key: python ?", list3.search("data structures"))
    print("search_key: javascript ?", list3.search("javascript"))

    list3.insert("data structures", "and")
    list3.insert("hello", "my")

    list3.print_list()

    list3.delete("python")
    list3.delete("my")

    list3.print_list()

    try:
        print("insert('not found', 'insert me!')")
        list3.insert("not found", "insert me!")
    except Exception as e:
        print(e)

    try:
        print("insert(None, 'again insert me!')")
        list3.insert(None, "again insert me!")
    except Exception as e:
        print(e)

    list3.print_list()

    try:
        print("delete('hello')")
        list3.delete("hello")
    except Exception as e:
        print(e)

    list3.print_list()

    try:
        print("delete_at_head() x3")
        list3.delete_at_head()
        list3.delete_at_head()
        list3.delete_at_head()
    except Exception as e:
        print(e)

    list3.print_list()

    try:
        print("delete('algorithms')")
        list3.delete("algorithms")
    except Exception as e:
        print(e)

    list3.print_list()

    try:
        print("delete_at_head()")
        list3.delete_at_head()
    except Exception as e:
        print(e)

    list3.print_list()


# Helper function to test the doubly linked list
def run_dll():
    t = DoublyLinkedList()

    t.insert_at_head(50)
    t.insert_at_head(40)
    t.insert_at_head(30)
    t.insert_at_head(20)
    t.insert_at_head(10)

    print("head -> tail:")
    t.print_list()

    print("\ntail -> head:")
    t.print_list(mode="tail")

    t.insert_at_tail(99)
    t.insert_at_tail(999)
    t.insert_at_tail(9999)

    print("\nhead -> tail")
    t.print_list()

    print("\ntail -> head")
    t.print_list(mode="tail")

    t.insert_at_head(111)
    t.insert_at_head(11111)

    print("\ncurrent list:")
    t.print_list()

    print("\ndelete at head x2")
    t.delete_at_head()
    t.delete_at_head()
    t.print_list()

    print("\ndelete at tail x3")
    t.delete_at_tail()
    t.delete_at_tail()
    t.delete_at_tail()
    t.print_list()

    print("insert(30, 99)")
    t.insert(30, 99)

    print("insert(99, 1000)")
    t.insert(99, 1000)

    print("insert(0, 100)")
    t.insert(0, 100)

    print("insert(10, -10)")
    t.insert(10, -10)

    print("insert(50, -50)")
    t.insert(50, -50)

    print("\ncurrent list")
    t.print_list()

    print("delete(-50)")
    t.delete(-50)

    print("delete(-10)")
    t.delete(-10)

    print("delete(0)")
    t.delete(0)

    print("delete(-99)")
    t.delete(-99)

    print("delete(10)")
    t.delete(10)

    print("\ncurrent list:")
    t.print_list()

    print()

    t.insert_at_head(44)
    t.insert_at_tail(55)
    t.print_list()


try:
    print("running doubly linked list")
    run_dll()
except Exception as e:
    print(e)

try:
    print("running singly linked list")
    run_ll()
except Exception as e:
    print(e)
