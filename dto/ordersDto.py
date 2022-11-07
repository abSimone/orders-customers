from dao.ordersDao import Order

class OrderObject:

    def __init__(self, NumOrdine, DataOrdine, DataSpedizione, DataConsegna, Stato, Commenti, NumCliente):
        self.NumOrdine = NumOrdine
        self.DataOrdine = DataOrdine
        self.DataSpedizione = DataSpedizione
        self.DataConsegna = DataConsegna
        self.Stato = Stato
        self.Commenti = Commenti
        self.NumCliente = NumCliente

class OrderStatusObject:

    def __init__(self, NumOrdine, Status):
        self.NumOrdine = NumOrdine
        self.Status = Status

class ArticleStatusObject:

    def __init__(self, NumOrdine, Status, CodProd):
        self.NumOrdine = NumOrdine
        self.Status = Status
        self.CodProd = CodProd

class OrderDto:

    @classmethod
    def findAllOrders(cls):
        data = Order.getAllOrders()
        newList = []
        for lista in data:
            newList.append(OrderObject(lista[0], lista[1], lista[3], lista[2], lista[4], lista[5], lista[6]))

        return newList

    @classmethod
    def findOrderStatus(cls, orderNumber : int):
        data = Order.getOrderStatusByOrderNumber(orderNumber)
        for lista in data:
            return OrderStatusObject(lista[0], lista[1])

    @classmethod
    def findAllOrderStatus(cls):
        data = Order.getAllOrderStatus()
        newList = []
        for lista in data:
            newList.append(OrderStatusObject(lista[0], lista[1]))
        return newList


    @classmethod
    def findArticleStatus(cls, productCode : str):
        data = Order.getArticlesStatus(productCode)
        newList = []
        for lista in data:
            newList.append(ArticleStatusObject(lista[0], lista[1], lista[2]))    
            
        return newList
