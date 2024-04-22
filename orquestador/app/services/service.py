from app.services import ClientService, OrderService ,ProductService, ProductBrandService 
from app.saga import SagaBuilder, SagaError

def funcionalidad(self) -> None:
    client = ClientService()
    order = OrderService()
    product = ProductService()
    product_brand = ProductBrandService()
    try:
        SagaBuilder.create() \
            .action(lambda:client.get_data(), lambda:client.get_compensation()) \
            .action(lambda:order.get_data(), lambda:order.get_compensation()) \
            .action(lambda:product.get_data(), lambda:product.get_compensation()) \
            .action(lambda:product_brand.get_data(), lambda:product_brand.get_compensation()) \
            .build().execute()
    except SagaError as e:
        print(e)