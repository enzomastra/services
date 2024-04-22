from flask import Flask
from flask_restful import Api
from .resources.home import Home
from .services.client_service import ClientService
from .services.order_service import OrderService
from .services.product_service import ProductService
from .services.product_brand_service import ProductBrandService

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    client_service = ClientService()
    order_service = OrderService()
    product_service = ProductService()
    product_brand_service = ProductBrandService()

    api.add_resource(Home, '/', resource_class_args=(client_service, order_service, product_service, product_brand_service))

    return app