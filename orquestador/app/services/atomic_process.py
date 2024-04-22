from flask import jsonify
import requests

class AtomicProcess:

    def execute_client(self):
        result = requests.get('http://localhost:5001/api/v1')
        if result.status_code != 200:
            result = self.compensation_client()
        return result
    
    def compensation_client(self):
        result = requests.get('http://localhost:5001/api/v1/compensation')
        return result
    


    def execute_order(self):
        result = requests.get('http://localhost:5002/api/v1')
        if result.status_code != 200:
            result = self.compensation_order()
        return result
    
    def compensation_order(self):
        result = requests.get('http://localhost:5002/api/v1/compensation')
        return result
    


    def execute_product(self):
        result = requests.get('http://localhost:5003/api/v1')
        if result.status_code != 200:
            result = self.compensation_product()
        return result
    
    def compensation_product(self):
        result = requests.get('http://localhost:5003/api/v1/compensation')
        return result



    def execute_product_brand(self):
        result = requests.get('http://localhost:5004/api/v1')
        if result.status_code != 200:
            result = self.compensation_product_brand()
        return result
    
    def compensation_product_brand(self):
        result = requests.get('http://localhost:5004/api/v1/compensation')
        return result
    
    

    def execute(self):
        client = self.execute_client()
        order = self.execute_order ()
        product = self.execute_product()
        product_brand = self.execute_product_brand()
        if client.status_code == 200 and order.status_code == 200 and product.status_code == 200 and product_brand.status_code == 200:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "not working"})