import time
from contextlib import contextmanager

@contextmanager
def timer(label="Operation"):
    start = time.time()
    yield
    end = time.time()
    print(f"{label} took {end - start:.3f}s")

with timer("Sleeping"):
    time.sleep(1.5)
