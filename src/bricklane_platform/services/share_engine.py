from bricklane_platform.util import group_by


class ShareEngine(object):

    def generate_share_orders(self, share_price, payments):
        payments_by_customer = group_by(
            payments,
            lambda payment: payment.customer_id,
        )

        share_orders = []

        for customer_id in payments_by_customer:
            total_amount = sum(
                map(
                    lambda payment: payment.amount,
                    payments_by_customer[customer_id],
                )
            )

            share_orders.append(
                {
                    "customer_id": customer_id,
                    "shares": total_amount / share_price
                }
            )

        return share_orders
