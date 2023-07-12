from linked_list import LinkedList
from utils import print_list, insert, insert_at_index, search_multi, delete, delete_keys


buffer = [10, 20, 30, 40, 50]

lst = LinkedList()
ptr = lst.get_head()
print(ptr)

print_list(ptr)
insert(lst, buffer)

ptr = lst.get_head()
print_list(ptr)

insert(lst, [100, 1000, 10000], "tail")
insert(lst, [60, 70], "head")

ptr = lst.get_head()
print_list(ptr)

print(f"length: {lst.length}")

buffer = [
    [99, 4],
    [121, 7],
    [625, 5],
    [0.1, 0],
    [0.01, 0],
    [99, 12],
    [999, 20],
    [1331, 15]
]

insert_at_index(lst, buffer)

ptr = lst.get_head()
print_list(ptr)
print(f"length: {lst.length}")

buffer = [0.1, 200, 50, 625, 999, 10000, 121, 5, 534, 0.001, 0.01, 9]
search_multi(lst, buffer)

buffer = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print()

lst = LinkedList()

insert(lst, buffer, "tail")
ptr = lst.get_head()

print_list(ptr)
print(f"length: {lst.length}")

delete(lst, 5, "tail")

print_list(ptr)
print(f"length: {lst.length}")

delete(lst, 2)
ptr = lst.get_head()

print_list(ptr)
print(f"length: {lst.length}")

insert(lst, [20, 10])
ptr = lst.get_head()

print_list(ptr)
print(f"length: {lst.length}")

delete(lst, 3, "tail", algorithm=2)
ptr = lst.get_head()

print_list(ptr)
print(f"length: {lst.length}")

delete(lst, 2, "tail", algorithm=2)
ptr = lst.get_head()

print_list(ptr)
print(f"length: {lst.length}")

print()

insert(lst, buffer, "tail")
ptr = lst.get_head()

print_list(ptr)
print(f"length:{lst.length}")

print()

delete_buffer = [100, 50, 200, 34, 10, 30, 20, 12, 70, 80]
delete_keys(lst, delete_buffer)

print()

ptr = lst.get_head()
print_list(ptr)
print(f"length: {lst.length}")

print()

insert(lst, [11, 121, 1331])
insert(lst, [5, 25, 625], mode="tail")

ptr = lst.get_head()
print_list(ptr)
print(f"length: {lst.length}")

