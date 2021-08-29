class Position:

    def __init__(self, x, y, gas):
        self.x = x
        self.y = y
        self.gas = gas
        # Datos para matriz
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None