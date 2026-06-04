from shape import Shape


class Square(Shape):
    def __init__(self, shape_id, side):
        super().__init__(shape_id, shape_type="Square")
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return self.side * 4

    def to_dict(self):
        final_dict = super().to_dict()
        final_dict["side"] = self.side
        return final_dict
