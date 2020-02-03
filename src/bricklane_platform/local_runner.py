"""
BRICKLANE - INVESTMENT PLATFORM - LOCAL RUNNER

Do not edit this file
"""
import argparse
from decimal import Decimal

from bricklane_platform.services.share_engine import ShareEngine
from factory import PaymentProcessorFactory

from bricklane_platform.util import generate_csv

def main(csv_path, source, share_price):

    payment_processor = PaymentProcessorFactory().get_processor_class(source=source)()

    payments = payment_processor.get_payments(csv_path, source)
    eligible_payments = payment_processor.verify_payments(payments)

    share_engine = ShareEngine()
    share_orders = share_engine.generate_share_orders(share_price, eligible_payments)

    return generate_csv(["customer_id", "shares"], sorted(share_orders))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="Path to the payments CSV file")
    parser.add_argument("source", help="The source of the payment, currently only 'card' is supported")
    parser.add_argument("share_price", type=Decimal, help="Share price to generate share orders for e.g. '1.30'")
    args = parser.parse_args()

    print main(args.csv_path, args.source, args.share_price)
