from dao.orderdetailsDao import OrderDetails

class ArticleNumberObject:

    def __init__(self, NumOrdine, NumArticoli):
        self.NumOrdine = NumOrdine
        self.NumArticoli = NumArticoli

class ArticlesSoldObject:

    def __init__(self, CodProd, Quantita):
        self.CodProd = CodProd
        self.Quantita = Quantita

class ArticlesEarningsObject:

    def __init__(self, CodProd, Guadagni):
        self.CodProd = CodProd
        self.Guadagni = Guadagni

class OrdersEarningsObject:

    def __init__(self, NumOrdine, Guadagni):
        self.NumOrdine = NumOrdine
        self.Guadagni = Guadagni

class ArticlesDescriptionObject:

    def __init__(self, CodProd, Quantita, Prezzo):
        self.CodProd = CodProd
        self.Quantita = Quantita
        self.Prezzo = Prezzo

class OrderDetailsDto:

    @classmethod
    def findAllOrderDetails(cls):
        data = OrderDetails.getAllOrdersDetails()
        newList = []
        for lista in data:
            if {"Numero Ordine" : lista[0], "Articoli": []} not in newList:
                newList.append({"Numero Ordine" : lista[0],
                                "Articoli" : []})
        for elementObject in newList:
            for lista in data:
                if elementObject["Numero Ordine"] == lista[0]:
                    elementObject["Articoli"].append(ArticlesDescriptionObject(lista[1], lista[2], lista[3]))

        return newList

    @classmethod
    def findAllOrdersArticlesNumber(cls):
        data = OrderDetails.getAllOrdersDetails()
        newList = []
        for lista in data:
            newList.append(ArticleNumberObject(lista[0], lista[1]))
        
        return newList

    @classmethod
    def findArticlesNumberByOrderNumber(cls, orderNumber : int):
        data = OrderDetails.getNumberOfArticlesByOrderNumber(orderNumber)
        newList = []
        for lista in data:
            newList.append(ArticleNumberObject(lista[0], lista[1]))
        return newList

    @classmethod
    def findAllArticlesQuantityOrdered(cls):
        data = OrderDetails.getAllArticlesQuantityOrdered()
        newList = []
        for lista in data:
            newList.append(ArticlesSoldObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findQuantityOrderedByArticle(cls, productCode : str):
        data = OrderDetails.getQuantityOrderedByArticle(productCode)
        newList = []
        for lista in data:
            newList.append(ArticlesSoldObject(lista[0], lista[1]))

        return newList
    
    @classmethod
    def findAllArticlesTotalEarnings(cls):
        data = OrderDetails.getAllArticlesTotalEarnings()
        newList = []
        for lista in data:
            newList.append(ArticlesEarningsObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findTotalEarningsByArticle(cls, productCode : str):
        data = OrderDetails.getTotalEarningsByArticle(productCode)
        newList = []
        for lista in data:
            newList.append(ArticlesEarningsObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findAllOrdersTotalEarnings(cls):
        data = OrderDetails.getAllOrdersTotalEarnings()
        newList = []
        for lista in data:
            newList.append(OrdersEarningsObject(lista[0], lista[1]))

        return newList

    @classmethod
    def findTotalEarningsByOrder(cls, orderNumber : int):
        data = OrderDetails.getTotalEarningsByOrder(orderNumber)
        newList = []
        for lista in data:
            newList.append(OrdersEarningsObject(lista[0], lista[1]))

        return newList