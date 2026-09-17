import queue
import threading

q = queue.Queue()
order = []


def worker():
    while True:
        letter, attempt = q.get()
        if letter == 3 and attempt == 1:
            order.append(f"retry {letter}")
            q.put((letter, 2))
        elif letter == 3:
            order.append(f"dead letter {letter}")
        else:
            order.append(f"delivered {letter}")
        q.task_done()


threading.Thread(target=worker, daemon=True).start()
for letter in (1, 2, 3):
    q.put((letter, 1))
q.join()
for line in order:
    print(line)
