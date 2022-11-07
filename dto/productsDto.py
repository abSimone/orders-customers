from dao.productsDao import Product

class ProductObject:

    def __init__(self, CodProdotto, Nome, Linea, Scala, Produttore, Descrizione, QuantitaDisp, Prezzo, MSRP):
        self.CodProdotto = CodProdotto
        self.Nome = Nome
        self.Linea = Linea
        self.Scala = Scala
        self.Produttore = Produttore
        self.Descrizione = Descrizione
        self.QuantitaDisp = QuantitaDisp
        self.Prezzo = Prezzo
        self.MSRP = MSRP

class ProductNameObject:

    def __init__(self, CodProdotto, Nome):
        self.CodProdotto = CodProdotto
        self.Nome = Nome

class ProductQuantbject:

    def __init__(self, CodProdotto, QuantitaDisp):
        self.CodProdotto = CodProdotto
        self.QuantitaDisp = QuantitaDisp

class ProductPriceObject:

    def __init__(self, CodProdotto, Prezzo):
        self.CodProdotto = CodProdotto
        self.Prezzo = Prezzo

class ProductLineObject:

    def __init__(self, CodProdotto, ProdLine):
        self.CodProdotto = CodProdotto
        self.Prezzo = ProdLine

class ProductDto: 

    @classmethod
    def findAllProducts(cls):
        data = Product.getAllProducts()
        newList = []
        for lista in data:
            newList.append(ProductObject(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))
        return newList           

    @classmethod
    def findProductName(cls, productCode : str):
        data = Product.getProductName(productCode)
        newList = []
        for lista in data:
            newList.append(ProductNameObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findQuantityInStock(cls, productCode : str):
        data = Product.getQuantityInStock(productCode)
        newList = []
        for lista in data:
            newList.append(ProductQuantbject(lista[0], lista[1]))

        return newList

    @classmethod
    def findBuyPrice(cls, productCode : str):
        data = Product.getBuyPrice(productCode)
        newList = []
        for lista in data:
            newList.append(ProductPriceObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findProductLine(cls, productCode : str):
        data = Product.getProductLine(productCode)
        newList = []
        for lista in data:
            newList.append(ProductLineObject(lista[0], lista[1]))

        return newList