import json
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon


class ShapeManager:
    shape_id = 1

    def __init__(self):
        self.file_path = "shapes.json"
        self.shapes = self.load_from_json()

    def create_shape(self, shape):
        max_id = max([s.id for s in self.shapes], default=0)
        shape.id = max_id + 1
        self.shapes.append(shape)
        self.save_to_json()

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape.id == shape_id:
                if shape.shape_type == "Square":
                    shape.side = new_data["side"]
                elif shape.shape_type == "Rectangle":
                    shape.width = new_data["width"]
                    shape.height = new_data["height"]
                elif shape.shape_type == "Circle":
                    shape.radius = new_data["radius"]
                elif shape.shape_type == "Triangle":
                    shape.base = new_data["base"]
                    shape.height = new_data["height"]
                    shape.s1 = new_data["side1"]
                    shape.s2 = new_data["side2"]
                    shape.s3 = new_data["side3"]
                elif shape.shape_type == "Hexagon":
                    shape.side = new_data["side"]

                self.save_to_json()
                return True
        return False

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return True
        return False

    def save_to_json(self):
        dicts = []
        for shape in self.shapes:
            dicts.append(shape.to_dict())

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(dicts, f)

    def load_from_json(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        loaded_shapes = []
        for shape in data:
            if shape["type"] == "Square":
                loaded_shapes.append(Square(shape["id"], shape["side"]))
            elif shape["type"] == "Rectangle":
                loaded_shapes.append(
                    Rectangle(shape["id"], shape["width"], shape["height"])
                )
            elif shape["type"] == "Circle":
                loaded_shapes.append(Circle(shape["id"], shape["radius"]))
            elif shape["type"] == "Triangle":
                loaded_shapes.append(
                    Triangle(
                        shape["id"],
                        shape["base"],
                        shape["height"],
                        shape["side1"],
                        shape["side2"],
                        shape["side3"],
                    )
                )
            elif shape["type"] == "Hexagon":
                loaded_shapes.append(Hexagon(shape["id"], shape["side"]))

        return loaded_shapes
