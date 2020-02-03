import unittest
from datetime import datetime

from bricklane_platform.models.payment import BankPayment, Payment
from bricklane_platform.models.card import Card


class TestPayment(unittest.TestCase):

    def setUp(self):
        self.data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "processed",
            "customer_id": "123",
            "date": "2019-02-01",
        }

    def test_init(self):
        with self.assertRaises(ValueError):
            payment = Payment()

    def test_init_with_data(self):

        payment = Payment(self.data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        card = payment.card

        self.assertIsInstance(card, Card)
        self.assertEqual(card.card_id, 45)
        self.assertEqual(card.status, "processed")

    def test_is_successful(self):
        self.data["card_status"] = "processed"
        payment = Payment(self.data)

        self.assertTrue(payment.is_successful())

    def test_is_successful_declined(self):
        self.data["card_status"] = "declined"
        payment = Payment(self.data)

        self.assertFalse(payment.is_successful())

    def test_is_successful_errored(self):
        self.data["card_status"] = "error"
        payment = Payment(self.data)

        self.assertFalse(payment.is_successful())


class TestBankPayment(unittest.TestCase):

    def setUp(self):
        self.data = {
            "amount": "2000",
            "bank_account_id": "45",
            "customer_id": "123",
            "date": "2019-02-01",
        }

    def test_init(self):
        with self.assertRaises(ValueError):
            payment = Payment()

    def test_init_with_data(self):
        payment = BankPayment(self.data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)
        self.assertEqual(payment.bank_account_id, 45)

    def test_is_successful_always_return_true(self):
        payment = BankPayment(self.data)

        self.assertTrue(payment.is_successful())