from user_bucket import UserBucket
from typing import Dict

class RateLimiter():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RateLimiter, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "initialised"):
            self.initialised = True

            # contructor part
            self.user_buckets : Dict[str, UserBucket] = {}

    def set_user_limit(self, user_id, max_limit, refill_rate):
        self.user_buckets[user_id] = UserBucket(max_limit, refill_rate)
    
    def allow_request(self, user_id):
        if user_id not in self.user_buckets:
            print(f"{user_id} you are not configured with us !!")
        if self.user_buckets[user_id].consume_token():
            return True
        print(f"sorry {user_id} you need to waiter longer !!")