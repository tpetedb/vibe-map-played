import time
from functools import lru_cache


@lru_cache
def water(kind):
    time.sleep(0.2)
    return f"a cup of {kind}"


for _ in range(2):
    start = time.perf_counter()
    water("cold")
    print(f"{(time.perf_counter() - start) * 1000:.0f} ms")
print(water.cache_info())
