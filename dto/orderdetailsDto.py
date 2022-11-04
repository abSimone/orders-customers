from dao.orderdetailsDao import OrderDetails

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
                    elementObject["Articoli"].append({"Codice Prodotto" : lista[1], "Quantità ordinata" : lista[2], "Prezzo Unità" : lista[3]})

        return newList

    @classmethod
    def findAllOrdersArticlesNumber(cls):
        data = OrderDetails.getAllOrdersDetails()
        newList = []
        for lista in data:
            newList.append({"Numero Ordine" : lista[0],
                            "Numero Articoli" : lista[1]})
        
        return newList

    @classmethod
    def findArticlesNumberByOrderNumber(cls, orderNumber : int):
        data = OrderDetails.getNumberOfArticlesByOrderNumber(orderNumber)
        newList = []
        for lista in data:
            newList.append({"Numero Ordine" : lista[0],
                            "Numero Articoli" : lista[1]})

        return newList

    @classmethod
    def findAllArticlesQuantityOrdered(cls):
        data = OrderDetails.getAllArticlesQuantityOrdered()
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0],
                            "Quantità Venduta" : lista[1]})

        return newList

    @classmethod
    def findQuantityOrderedByArticle(cls, productCode : str):
        data = OrderDetails.getQuantityOrderedByArticle(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0],
                            "Quantità Venduta" : lista[1]})

        return newList
    
    @classmethod
    def findAllArticlesTotalEarnings(cls):
        data = OrderDetails.getAllArticlesTotalEarnings()
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0],
                            "Guadagni Totali" : lista[1]})

        return newList

    @classmethod
    def findTotalEarningsByArticle(cls, productCode : str):
        data = OrderDetails.getTotalEarningsByArticle(productCode)
        newList = []
        for lista in data:
            newList.append({"Codice Prodotto" : lista[0],
                            "Guadagni Totali" : lista[1]})

        return newList

    @classmethod
    def findAllOrdersTotalEarnings(cls):
        data = OrderDetails.getAllOrdersTotalEarnings()
        newList = []
        for lista in data:
            newList.append({"Numero Ordine" : lista[0],
                            "Guadagni Totali" : lista[1]})

        return newList

    @classmethod
    def findTotalEarningsByOrder(cls, orderNumber : int):
        data = OrderDetails.getTotalEarningsByOrder(orderNumber)
        newList = []
        for lista in data:
            newList.append({"Numero Ordine" : lista[0],
                            "Guadagni Totali" : lista[1]})

        return newList