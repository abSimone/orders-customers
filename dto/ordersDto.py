from dao.ordersDao import Order

class OrderDto:

    @classmethod
    def findAllOrders(cls):
        data = Order.getAllOrders()
        newList = []
        for lista in data:
            newList.append({"Numero Ordine": lista[0],
                            "Data Ordine": lista[1],
                            "Data Spedizione": lista[3],
                            "Data Consegna": lista[2],
                            "Stato": lista[4],
                            "Commenti": lista[5],
                            "Numero Cliente": lista[6]})
        
        return newList
