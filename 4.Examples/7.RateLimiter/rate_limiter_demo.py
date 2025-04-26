from rate_limiter import RateLimiter
import time

class RateLimiterDemo():
    @staticmethod
    def run():
        rate_limiter = RateLimiter()

        # Set a limit of 5 requests per 10 seconds for user "user123"
        rate_limiter.set_user_limit("user123", 5, 10)
        
        # Test rate limiting
        for i in range(10):
            result = rate_limiter.allow_request("user123")
            print(f"Request {i+1}: {'Allowed' if result else 'Blocked'}")
            time.sleep(1)  # Wait 1 second between requests

        


if __name__ == "__main__":
    RateLimiterDemo.run()


# python3 4.Examples/7.RateLimiter/rate_limiter_demo.py