import time
class TokenBucket:
    
    def __init__(self, bucket_capacity, fill_rate_in_a_sec):
        self.bucket_capacity = bucket_capacity
        self.current_tokens = bucket_capacity
        self.fill_rate_in_a_sec = fill_rate_in_a_sec
        self.last_refill_time = time.time()
        
    
    def refill(self):
        cur_time = time.time()
        time_diff = cur_time - self.last_refill_time
        tokens_to_add = time_diff*self.fill_rate_in_a_sec;
        
        if time_diff >= 1:
            self.current_tokens = min(self.bucket_capacity, (self.current_tokens + tokens_to_add))
            self.last_refill_time = time.time()
    
    def allow(self):
        self.refill()
        if self.current_tokens > 0:
            self.current_tokens -= 1
            return True;
        return False;    
    
    
token_bucket = TokenBucket(10, 10)
for i in range(20):
    for j in range(20):
        response = token_bucket.allow()
        print(f"request is allow ? {response}")
    time.sleep(1)    
    
        

    
    
            
        
    
