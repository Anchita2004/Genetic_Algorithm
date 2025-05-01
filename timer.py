from time import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time()
    yield
    end = time()
    print("Time taken: %.2fs" % (end - start))
