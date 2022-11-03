from dao.productlinesDao import ProductsLines

class ProductLine:
    def __init__(self, productLine, textDescription):
        self.productLine = productLine
        self.textDescription = textDescription


class productLinesDto:

    @classmethod
    def getAllProductLines(cls):
        data = ProductsLines.findAllProductLines()
        newList = []
        for lista in data:
            newList.append(ProductLine(lista[0], lista[1]))
        return newList

    @classmethod
    def getDescription(cls, productCode):
        data = ProductsLines.findAllTextDescriptions(productCode)
        newList = []
        for lista in data: 
            newList.append(ProductLine(lista[0], lista[1]))
        return newList


