from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon

app = FastAPI()


manager = ShapeManager()


@app.get("/shapes", status_code=200)
def get_all_shapes():
    shapes = manager.get_all_shapes()
    return [shape.to_dict() for shape in shapes]


@app.get("/shapes/total-area", status_code=200)
def get_total_area():
    shapes = manager.get_all_shapes()
    total = sum(shape.get_area() for shape in shapes)
    return {"total_area": total}


@app.get("/shapes/{shape_id}", status_code=200)
def get_shape_by_id(shape_id: int):
    shapes = manager.get_all_shapes()
    for shape in shapes:
        if shape.id == shape_id:
            return shape.to_dict()
    raise HTTPException(404, f"Shape ID {shape_id} not found")


@app.post("/shapes", status_code=201)
def add_shape(shape: dict):
    try:
        shape_type = shape["type"]

        if shape_type.title() == "Square":
            new_shape = Square(0, shape["side"])
        elif shape_type.title() == "Rectangle":
            new_shape = Rectangle(0, shape["width"], shape["height"])
        elif shape_type.title() == "Circle":
            new_shape = Circle(0, shape["radius"])
        elif shape_type.title() == "Triangle":
            new_shape = Triangle(
                0,
                shape["base"],
                shape["height"],
                shape["side1"],
                shape["side2"],
                shape["side3"],
            )
        elif shape_type.title() == "Hexagon":
            new_shape = Hexagon(0, shape["side"])
        else:
            raise HTTPException(422, f"Invalid shape type '{shape['type']}'")

        manager.create_shape(new_shape)
        return {"message": "Shape created successfully."}
    except KeyError:
        raise HTTPException(422, "You are missing a key")


@app.put("/shapes/{shape_id}", status_code=200)
def update_shape(shape_id: int, shape: dict):
    try:
        updated = manager.update_shape(shape_id, shape)
        if not updated:
            raise HTTPException(404, f"Shape ID {shape_id} not found.")

        return {"message": f"Shape {shape_id} updated successfully."}
    except KeyError:
        raise HTTPException(422, "You are missing some items.")


@app.delete("/shapes/{shape_id}", status_code=200)
def delete_shape(shape_id: int):
    deleted = manager.delete_shape(shape_id)
    if not deleted:
        raise HTTPException(404, f"Shape ID {shape_id} not found.")

    return {"message": f"Shape {shape_id} deleted successfully."}
