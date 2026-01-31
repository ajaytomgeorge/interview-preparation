import time
import random
from threading import Lock, Thread
import asyncio
class TokenBucketLimiter():

    def __init__(self, capacity:float, rate:float,)-> None:
        self.capacity:float = capacity
        self.current_bucket:float = capacity
        self.rate:float = rate
        self.lock = Lock()
        self.last_time = time.monotonic()
        self.asyc_lock = asyncio.Lock()
    def _refill_tokens(self):
        self.current_bucket = min( self.capacity,self.current_bucket + ( time.monotonic() - self.last_time)* self.rate) 
        print("refilled", self.current_bucket)
        self.last_time = time.monotonic()

    async def async_consume_tokens(self, tokens:float):
        async with self.asyc_lock:
            print("acquired_lock")
            if  self.capacity != self.current_bucket:
                self._refill_tokens()
            if self.current_bucket< tokens:
                return False
            self.current_bucket-=tokens
            return True

async def main():
    bl = TokenBucketLimiter(5,5)
    async def worker(id):
        print("In workker", id)
        await asyncio.sleep(1)
        await bl.async_consume_tokens(5)
        print("Finished worker", id)

    await asyncio.gather(*[worker(id) for id in range(5)])

if __name__ == "__main__":
    asyncio.run(main())
        









# def test_rate_limit():
#     bl = TokenBucketLimiter(5,5)
#     for i in range(5):
#         time.sleep(1)
#         assert bl.cosume_tokens(5) == True


# def test_thread_lock():
#     bl = TokenBucketLimiter(500,5)
#     def worker(id):
#         print("my id", id)
#         out = bl.cosume_tokens(5)
#         print("my out", out)
#         if out:
#             print("consumed")
#         else:
#             print("didnt get thread")
    
#     threads = [Thread(target=worker, args=(id,)) for id in range(20)]

#     for t in threads:
#         t.start()
    
#     for t in threads:
#         t.join()


