from dao.productsDao import Product

class Product: 
    def __init__(self, product):
        self.product = product
        

    @classmethod
    def getAllProducts(cls):
        data = Product.getAllProducts()
        newList = []
        for lista in data:
            newList.append(Product(lista[0], lista[1]))
        return newList       

   

    @classmethod
    def getAllProductName(cls):
        data = Product.getAllProductName()
        newList = []
        for lista in data:
            newList.append(Product(lista[0], lista[1]))
        return newList       
    
    