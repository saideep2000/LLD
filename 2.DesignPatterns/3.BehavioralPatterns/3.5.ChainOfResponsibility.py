
# Problem Statement :
# In many systems, requests need to be processed by a sequence of handlers where each 
# handler has the opportunity to deal with the request, but the sender doesn't need to
# know which handler will ultimately process it. Hard-wiring specific request-to-handler 
# mappings leads to rigid designs that are difficult to extend and maintain. The Chain of 
# Responsibility Design Pattern addresses this problem by decoupling the sender and 
# receiver. Instead of the sender invoking a method on a specific receiver, the request is 
# passed along a chain of potential handlers until one of them handles it. 
# This approach enables dynamic configuration of processing pipelines and flexible assignment of responsibilities.

# Example: Expense Approval Chain
# Consider an expense approval system where requests for expense reimbursements are 
# handled by different approvers based on the expense amount. For instance, a manager 
# might approve expenses up to $1,000, a director for amounts up to $5,000, and a 
# vice president for larger amounts. The chain of responsibility allows the expense 
# request to be passed along until the appropriate approver is found.

from abc import ABC, abstractmethod

# Base Handler: Defines the interface for handling requests and holds a reference to the next handler.
class Approver(ABC):
    def __init__(self, next_approver=None):
        self.next_approver = next_approver

    @abstractmethod
    def handle_request(self, amount: float):
        pass

# Concrete Handler: Manager can approve expenses up to $1,000.
class Manager(Approver):
    def handle_request(self, amount: float):
        if amount <= 1000:
            print(f"Manager approved the expense of ${amount:.2f}.")
        elif self.next_approver:
            print(f"Manager passes the request of ${amount:.2f} to the next approver.")
            self.next_approver.handle_request(amount)
        else:
            print("Expense request cannot be approved.")

# Concrete Handler: Director can approve expenses up to $5,000.
class Director(Approver):
    def handle_request(self, amount: float):
        if amount <= 5000:
            print(f"Director approved the expense of ${amount:.2f}.")
        elif self.next_approver:
            print(f"Director passes the request of ${amount:.2f} to the next approver.")
            self.next_approver.handle_request(amount)
        else:
            print("Expense request cannot be approved.")

# Concrete Handler: VicePresident handles larger expenses.
class VicePresident(Approver):
    def handle_request(self, amount: float):
        # No upper limit for this example.
        print(f"VicePresident approved the expense of ${amount:.2f}.")

# Client code to create and configure the chain of responsibility.
if __name__ == "__main__":
    # Build the chain: Manager -> Director -> VicePresident.
    vp = VicePresident()
    director = Director(next_approver=vp)
    manager = Manager(next_approver=director)

    # Example expense requests.
    expenses = [300, 1200, 4000, 8000]

    for expense in expenses:
        print(f"\nRequesting approval for expense of ${expense:.2f}:")
        manager.handle_request(expense)



# python3 2.DesignPatterns/3.BehavioralPatterns/3.5.ChainOfResponsibility.py