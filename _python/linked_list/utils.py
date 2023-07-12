def print_list(ptr):
    if ptr is None:
        return

    while ptr.next is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print(ptr.data)


def insert(lst, buffer, mode="head"):
    if mode == "head":
        for item in buffer:
            lst.insert_at_head(item)
        return
    for item in buffer:
        lst.insert_at_tail(item)
    return


def insert_at_index(lst, buffer):
    for row in buffer:
        data, index = row[0], row[1]
        lst.insert_at_k(data, index)


def search_multi(lst, buffer):
    for i, item in enumerate(buffer):
        print(f"[{i+1}] {item}\tpresent in linked list?\t{lst.search(item)}")


def delete(lst, count, mode="head", algorithm=1):
    if mode == "tail" and algorithm == 1:
        for _ in range(count):
            lst.delete_at_tail(mode=1)
        return
    if mode == "tail" and algorithm == 2:
        for _ in range(count):
            lst.delete_at_tail(mode=2)
        return
    for _ in range(count):
        lst.delete_at_head()
    return


def delete_keys(lst, buffer):
    for item in buffer:
        print(f"DELETE_KEY {item}", end=" ")
        result = lst.delete_by_key(item)
        if result is None:
            print(f"[INFO] KEY_NOT_FOUND {item}")
        else:
            print(f"[INFO] SUCCESS")
