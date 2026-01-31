import time
import threading
class TokenRateLimiter:
    def __init__(self, capacity, rate):
        self.max_capacty = capacity
        self.rate = rate
        self.current_capactity = capacity
        self.last_registerd_time = time.monotonic()

    def _refill_capactiy(self):
        current_time = time.monotonic()
        print(self.current_capactity)
        self.current_capactity = min(self.max_capacty,self.current_capactity+(current_time - self.last_registerd_time)*self.rate)


    def allowed(self, identity):
        with threading.Lock() as lock:
            print(f"Thread {identity } got lock")
            self._refill_capactiy()
            if self.current_capactity < 1:
                return False
            
            self.current_capactity = self.current_capactity - 1
            return True





trl = TokenRateLimiter(5,2)

def test_lock():
    def worker(identity):
        print(trl.allowed(identity))
    threads = [threading.Thread(target=worker,args=(i,)) for i in range(5)]
    for thread in threads:
        thread.start()
        thread.join()


test_lock()