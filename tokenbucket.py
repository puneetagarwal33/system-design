import time

class TokenBucket:
    
    def __init__(self, capacity, refill_rate_in_sec):
        self.capacity = capacity
        self.token = capacity
        self.refill_rate_in_sec = refill_rate_in_sec
        self.start_time = time.time()
    
    def refill(self):
        cur_time = time.time()
        if cur_time - self.start_time > self.refill_rate_in_sec:
            self.token = self.capacity
            self.start_time = cur_time
    
    def allow(self) -> bool:
        self.refill()
        cur_time = time.time()
        if self.token > 0:
            self.token -= 1
            return True
        return False;
    
    
tb = TokenBucket(10, 20)
for i in range(1,50):
        response = tb.allow();
        print(f"response recieved {response}")
        time.sleep(1)
        
            
