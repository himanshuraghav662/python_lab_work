class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

def pour_water(x, y, max_x, max_y):
    if x == 0:
        return 0, y
    elif y == max_y:
        return x, 0
    else:
        amount_to_pour = min(x, max_y - y)
        return x - amount_to_pour, y + amount_to_pour

def find_path(m, n, d):
    visited = set()
    queue = Queue()
    queue.enqueue((0, 0))

    while not queue.is_empty():
        x, y = queue.dequeue()

        if x == d or y == d:
            return f"Path found: ({x}, {y})"

        for operation in [(x, 0), (0, y), (m, y), (x, n), pour_water(x, y, m, n), pour_water(y, x, n, m)]:
            new_x, new_y = operation
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.enqueue((new_x, new_y))

    return "Path not found"

# Example usage:
m = 3  # Capacity of jug 1
n = 5  # Capacity of jug 2
d = 4  # Desired amount of water

result = find_path(m, n, d)
print(result)
