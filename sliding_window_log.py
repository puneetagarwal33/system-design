from collections import deque
import time
class SlidingWindowLog:
    def __init__(self, max_requests, window_size):
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = deque()
    
    def allow(self):
        cur_time = time.time()
        
        while self.requests and cur_time - self.requests[0] > self.window_size:
            self.requests.popleft()
        
        if len(self.requests) < self.max_requests:
            self.requests.append(cur_time)
            return True
        return False    
        
slidingwindowlog = SlidingWindowLog(5, 5)
for i in range(10):
    response = slidingwindowlog.allow();
    print(f"response recieved is {response}")
