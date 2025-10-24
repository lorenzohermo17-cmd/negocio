class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def add_stock(self,stock:int) -> str:
        if stock <= 0:
            return "No se puede agregar 0 o menos, que te pensas que sos"

        self.stock += stock

        return "Se cambio con exito el stock"

producto = Producto("Remera",40000,0)

producto.add_stock()