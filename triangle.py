from shape import Shape


class Triangle(Shape):
    def __init__(self, shape_id, base, height, s1, s2, s3):
        super().__init__(shape_id, shape_type="Triangle")
        self.base = base
        self.height = height
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def get_area(self):
        return round(self.base * self.height / 2, 2)

    def get_perimeter(self):
        return self.s1 + self.s2 + self.s3

    def to_dict(self):
        final_dict = super().to_dict()
        final_dict["base"] = self.base
        final_dict["height"] = self.height
        final_dict["side1"] = self.s1
        final_dict["side2"] = self.s2
        final_dict["side3"] = self.s3
        return final_dict
