from time import time
class UserBucket():
    def __init__(self, max_limit, refill_rate_token):
        self.max_limit = max_limit
        self.refill_rate_token = refill_rate_token
        self.current_token = max_limit
        self.last_time_visited = time()

    def consume_token(self) -> bool:
        self.refill_token()

        if self.current_token >= 1:
            self.current_token = self.current_token - 1
            return True
        return False
    


    def refill_token(self):
        elapsed_time = time() - self.last_time_visited
        cal_token_needed_to_be_added = elapsed_time * (self.max_limit/self.refill_rate_token)
        self.current_token = min(self.current_token, self.current_token + cal_token_needed_to_be_added)
        self.last_time_visited = time()
