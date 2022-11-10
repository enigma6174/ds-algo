from main import HashMap

h = HashMap()

h.put(1, 1)
h.put(2, 2)
h.put("animal", "cat")
h.put("bird", "eagle")
h.put("number", 3.14)
h.put(6174, "kaprekar constant")
h.put(3.141, "pi")

print(h)

result = h.get("bird")
print(f"h.get(bird) -> {result}")

result = h.get("number")
print(f"h.get(number) -> {result}")

result = h.get(2)
print(f"h.get(2) -> {result}")

result = h.get("1")
print(f"h.get('1') -> {result}")

result = h.get("hello")
print(f"h.get(hello) -> {result}")

h.remove(2)
h.remove("number")

print(h)

print("\nUPDATING...\n")

h.put(1, "hello world")
h.put("1", 0.001)

print(h)

result = h.get(1)
print(f"h.get(1) -> {result}")

result = h.get("1")
print(f"h.get('1') -> {result}")
