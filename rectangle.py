from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, width, height):
        super().__init__(shape_id, shape_type="Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def to_dict(self):
        final_dict = super().to_dict()
        final_dict["width"] = self.width
        final_dict["height"] = self.height
        return final_dict
