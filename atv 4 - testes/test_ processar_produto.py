
from itertools import product
from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.ProductRepository import ProductRepository
from Repositories.CustomerRepository import CustomerRepository


def test_processa_produto():
    # Arrange
    custumer1 = Customer(1, "Arthur")
    repositoryCustumer = CustomerRepository()
    repositoryCustumer.append_customer(custumer1)
    
    product1 = Product(3, "Rice", 20, 5)
    repositoryProduct = ProductRepository()
    repositoryProduct.append_product(product1)
    
    ordem = Order(1, custumer1)
    ordem_produto1 = OrderProduct()
    ordem_produto1.add_product(product1,10)
    ordem.add_order_product(ordem_produto1)
    
    #Act
    ordem.update_total_price()
    
    #Assert
    assert product1.get_stock() == 10
    
def test_integrado_baixar_estoque():
    #Arrange
    product = Product(3,"Rice",10,2)
   
    #Act
    product.down_stock(5)
    
    #Assert
    product.get_stock() == 15

def test_baixar_estoque():
    #Arrange
    produto = Product(1,"Salt",3.77,10)

    #ACT
    produto.down_stock(7)

    #Assert
    assert produto.stock == 3

    

