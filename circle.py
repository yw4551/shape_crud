from shape import Shape


class Circle(Shape):
    def __init__(self, shape_id, radius):
        super().__init__(shape_id, shape_type="Circle")
        self.radius = radius

    def get_area(self):
        return self.radius**2 * 3.14

    def get_perimeter(self):
        return self.radius * 2 * 3.14

    def to_dict(self):
        final_dict = super().to_dict()
        final_dict["radius"] = self.radius
        return final_dict
