import unittest
from decimal import Decimal

from bricklane_platform.services.share_engine import ShareEngine
from bricklane_platform.models.payment import Payment


def create_payment(customer_id, amount):
    payment = Payment()
    payment.customer_id = customer_id
    payment.amount = amount
    return payment


class TestShareEngine(unittest.TestCase):

    def setUp(self):
        self.share_engine = ShareEngine()
        self.share_price = Decimal("1.2")

    def test_generate_share_orders_different_customers(self):
        payments = [
            create_payment(456, Decimal("900")),
            create_payment(123, Decimal("4200")),
        ]

        result = self.share_engine.generate_share_orders(self.share_price, payments)

        self.assertEqual(
            result,
            [
                {"customer_id": 456, "shares": 750},
                {"customer_id": 123, "shares": 3500},
            ]
        )

    def test_generate_share_orders_same_customer(self):
        payments = [
            create_payment(456, Decimal("900")),
            create_payment(456, Decimal("4200")),
        ]

        result = self.share_engine.generate_share_orders(self.share_price, payments)

        self.assertEqual(
            result,
            [
                {"customer_id": 456, "shares": 4250},
            ]
        )
