import unittest
from app import create_app
from app.services import ClientService, OrderService, ProductService, ProductBrandService
from app.services.atomic_process import AtomicProcess

class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = ClientService()
        self.order = OrderService()
        self.product = ProductService()
        self.product_brand = ProductBrandService()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_atomic_process(self):
        atomic_process = AtomicProcess()
        response = atomic_process.execute()
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()