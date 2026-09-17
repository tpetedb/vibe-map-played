import concurrent.futures
import time


def one_request(n):
    time.sleep(0.05)
    return n


start = time.perf_counter()
for n in range(20):
    one_request(n)
serial = time.perf_counter() - start
print(f"one at a time: {serial:.2f} s")

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    futures = [pool.submit(one_request, n) for n in range(20)]
    for future in concurrent.futures.as_completed(futures):
        future.result()
batched = time.perf_counter() - start
print(f"batched: {batched:.2f} s")
print(f"speedup: {serial / batched:.1f}x")
