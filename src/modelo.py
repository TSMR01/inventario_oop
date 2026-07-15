class Producto:
    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        producto_id: int | None = None
    ):
        self.id = producto_id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0")

        self._id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")

        self._nombre = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser numérico")

        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self._precio = float(valor)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if not isinstance(valor, int):
            raise TypeError("El stock debe ser un número entero")

        if valor < 0:
            raise ValueError("El stock no puede ser negativo")

        self._stock = valor

    def __str__(self):
        return (
            f"Producto(id={self.id}, nombre='{self.nombre}', "
            f"precio=${self.precio:.2f}, stock={self.stock})"
        )