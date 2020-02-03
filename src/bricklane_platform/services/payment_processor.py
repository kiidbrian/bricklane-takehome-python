import csv

from bricklane_platform.models.payment import BankPayment, Payment


class PaymentFactory(object):

    def __init__(self):
        self._payment_types = {}

    def register_payment(self, source, payment_type):
        self._payment_types[source] = payment_type

    def get_payment(self, source):
        payment = self._payment_types.get(source)

        if not payment:
            raise KeyError('{} is not registered'.format(source))

        return payment


class PaymentProcessor(object):

    def __init__(self):
        self.factory = PaymentFactory()
        self.factory.register_payment('card', Payment)
        self.factory.register_payment('bank', BankPayment)

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                payments.append(self.factory.get_payment(source)(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
