from main import LinkedList

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

list3.insert_after("data structures", "and")
list3.insert_after("hello", "my")

list3.print_list()

list3.delete("python")
list3.delete("my")

list3.print_list()

try:
    print("insert('not found', 'insert me!')")
    list3.insert_after("not found", "insert me!")
except Exception as e:
    print(e)

try:
    print("insert(None, 'again insert me!')")
    list3.insert_after(None, "again insert me!")
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