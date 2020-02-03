from bricklane_platform.services.payment_processor import BankTranferProcessor, PaymentProcessor

class PaymentProcessorFactory(object):

    def __init__(self):
        self.processor_classes = {}
        self.register_processor('card', PaymentProcessor)
        self.register_processor('bank', BankTranferProcessor)

    def register_processor(self, source, processor_class):
        self.processor_classes[source] = processor_class
    
    def get_processor_class(self, source):  
        processor_class = self.processor_classes.get(source)

        if not processor_class:
            raise ValueError('{} processor not registered'.format(source))

        return processor_class