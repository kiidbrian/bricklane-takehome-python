from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.config import PAYMENT_FEE_RATE

class BasePayment(object):
    
    customer_id = None
    date = None
    amount = None
    fee = None

    def __init__(self, data=None):
        
        if not data:
            return

    def is_successful(self):
        raise NotImplementedError('Implementation for success state NOT IMPLEMENTED')

class Payment(BasePayment):

    card_id = None

    def __init__(self, data=None):

        super(Payment, self).__init__(data)

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        card = Card()
        card.card_id = int(data["card_id"])
        card.status = data["card_status"]
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"


class BankPayment(BasePayment):

    bank_account_id = None

    def __init__(self, data=None):

        super(BankPayment, self).__init__(data)

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee
        
        self.bank_account_id = data["bank_account_id"]

    def is_successful(self):
        return True
