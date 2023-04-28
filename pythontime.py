import time

def timed(f):
    t0 = time.time()
    fun()
    t1 = time.time()
    print(f"Elapsed time: {t1 - t0}")
    
def fun():
    for i in range(50_000_000):
        pass 

if __name__ == "__main__":
    timed(fun())
    