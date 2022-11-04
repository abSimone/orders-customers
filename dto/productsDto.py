from dao.productsDao import Product

class ProductDto: 

    @classmethod
    def findAllProducts(cls):
        data = Product.getAllProducts()
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0],
                            "Nome Prodotto" : lista[1],
                            "Linea" : lista[2],
                            "Scala" : lista[3],
                            "Produttore" : lista[4],
                            "Descrizione" : lista[5],
                            "Quantità Disponibile" : lista[6],
                            "Prezzo" : float(lista[7]),
                            "MSRP" : float(lista[8])})
        return newList           

    @classmethod
    def findProductName(cls, productCode : str):
        data = Product.getProductName(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0], "Nome Prodotto" : lista[1]})

        return newList

    @classmethod
    def findQuantityInStock(cls, productCode : str):
        data = Product.getQuantityInStock(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0], "Quantità Disponibile" : lista[1]})

        return newList

    @classmethod
    def findBuyPrice(cls, productCode : str):
        data = Product.getBuyPrice(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0], "Prezzo" : float(lista[1])})

        return newList

    @classmethod
    def findProductLine(cls, productCode : str):
        data = Product.getProductLine(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0], "Linea" : lista[1]})

        return newList