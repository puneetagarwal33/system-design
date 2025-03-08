import time
from collections import deque
class LeakyBucket:
    
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.cur_req = deque()
        self.leak_rate = leak_rate
        self.last_leak_time = time.time()
        
    def leak(self):
        cur_time = time.time()
        time_diff = cur_time - self.last_leak_time
        
        leak_req = int((time_diff)*self.leak_rate)
        
        if(time_diff > 1):
            req_needs_be_leaked = min(max(0, len(self.cur_req) - leak_req), self.capacity)
            for i in range(req_needs_be_leaked):
                self.cur_req.popleft()
            self.last_leak_time = time.time()    
    
    def allow(self, req_id) -> bool:
        self.leak();
        if len(self.cur_req) >= self.capacity:
            return False
        
        self.cur_req.append(req_id);    
        return True    
                
leaky_bucket = LeakyBucket(10, 5)
for i in range(20):
    response = leaky_bucket.allow(i)
    print(f"request returned with {response}")
    if i == 10:
        time.sleep(1)
        
        
        
        
