from shape import Shape
import math


class Hexagon(Shape):
    def __init__(self, shape_id, side):
        super().__init__(shape_id, shape_type="Hexagon")
        self.side = side

    def get_area(self):
        return round((3 * math.sqrt(3) * (self.side**2)) / 2, 2)

    def get_perimeter(self):
        return self.side * 6

    def to_dict(self):
        final_dict = super().to_dict()
        final_dict["side"] = self.side
        return final_dict
