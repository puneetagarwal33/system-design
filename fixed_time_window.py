import time
class FixedTimeWindow:
    
    def __init__(self, capacity, window_size):
        self.capacity = capacity
        self.size = 0;
        self.window_size = window_size
        self.start_time = time.time()
    
    def reset(self):
        cur_time = time.time()
        diff_time = cur_time - self.start_time
        if diff_time >= self.window_size:
            self.size = 0;
            self.start_time = time.time()
    
    def allow(self):
       self.reset();
       if self.size < self.capacity:
            self.size += 1
            return True;
       return False;    

ftw = FixedTimeWindow(5, 1)
for i in range(10):
    response = ftw.allow();
    print(f"response recieved is {response}")
    if i == 5:
        time.sleep(1)
        
