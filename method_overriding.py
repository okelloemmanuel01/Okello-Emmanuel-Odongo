
class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via Generic Payment")

class CreditCardPayment(Payment):
    def process_payment(self, amount):  # Method Overriding
        print(f"Processing payment of ${amount} via Credit Card")

class PayPalPayment(Payment):
    def process_payment(self, amount):  # Method Overriding
        print(f"Processing payment of ${amount} via PayPal")

# Usage
payment = Payment()
payment.process_payment(100)  # Output: "Processing payment of $100 via Generic Payment"

credit_pay = CreditCardPayment()
credit_pay.process_payment(150)  # Output: "Processing payment of $150 via Credit Card"

paypal_pay = PayPalPayment()
paypal_pay.process_payment(200)  # Output: "Processing payment of $200 via PayPal"