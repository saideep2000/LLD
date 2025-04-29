from uuid import uuid
class Reservation():
    def __init__(self, expected_pick_up_date, expected_drop_off_date, car, customer):
        self.receipt_id = uuid.uuid4()
        self.expected_pick_up_date = expected_pick_up_date
        self.expected_drop_off_date = expected_drop_off_date
        self.pick_up_date = None
        self.drop_off_date = None
        self.car = car
        self.customer = customer