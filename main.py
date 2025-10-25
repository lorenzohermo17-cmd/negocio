class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price
    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")
        
        discount = (self.price * percentage) / 100
        self.price = self.price - discount
        return self.price
      
     def add_stock(self,stock:int) -> str:
        if stock <= 0:
            return "No se puede agregar 0 o menos, que te pensas que sos"

        self.stock += stock

        return "Se cambio con exito el stock"
    
product1 = Product("Laptop", 50, 1500)
print(f"El precio de {product1.name} originalmente era {product1.price} dolares y con el descuento aplicado queda en tan solo {product1.apply_discount (50)} dolares")

