from shape_manager import ShapeManager
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon

manager = ShapeManager()


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def open_menu():
    print("=== Menu ===")
    print("1. Add shape")
    print("2. Show all shapes")
    print("3. Update shape")
    print("4. Delete shape")
    print("5. Exit")


def handle_add_shape():
    shape_type = input("Enter the shape you would like to add: ").title()

    if shape_type == "Rectangle":
        width = get_float_input("Enter the width of the rectangle: ")
        height = get_float_input("Enter the height of the rectangle: ")
        manager.create_shape(Rectangle(manager.shape_id, width, height))
    elif shape_type == "Square":
        side = get_float_input("Enter the size of the side of the square: ")
        manager.create_shape(Square(manager.shape_id, side))
    elif shape_type == "Circle":
        radius = get_float_input("Enter the radius of the circle: ")
        manager.create_shape(Circle(manager.shape_id, radius))
    elif shape_type == "Triangle":
        base = get_float_input("Enter the base of the Triangle: ")
        height = get_float_input("Enter the height of the Triangle: ")
        side1 = get_float_input("Enter the size of the first side of the triangle: ")
        side2 = get_float_input("Enter the size of the second side of the triangle: ")
        side3 = get_float_input("Enter the size of the third side of the triangle: ")
        manager.create_shape(
            Triangle(manager.shape_id, base, height, side1, side2, side3)
        )
    elif shape_type == "Hexagon":
        side = get_float_input("Enter the size of the side of the hexagon: ")
        manager.create_shape(Hexagon(manager.shape_id, side))
    else:
        print(
            "The choice must be a shape in the list [Square, Rectangle, Circle, Triangle, Hexagon]"
        )


def handle_user_input():
    return get_int_input("Enter your choice? (1-5): ")


def handle_show_shapes():
    shapes = manager.get_all_shapes()
    if not shapes:
        print("There are no shapes to show")
        return

    for shape in shapes:
        print(f"--- Shape ID: {shape.id} ---")
        for key, value in shape.to_dict().items():
            print(f"{key.capitalize()}: {value}")
        print(f"Area: {shape.get_area()}")
        print(f"Perimeter: {shape.get_perimeter()}\n")


def handle_update_shape():
    shape_id = get_int_input("Enter the shape ID you want to update: ")

    shape_to_update = None
    for shape in manager.get_all_shapes():
        if shape.id == shape_id:
            shape_to_update = shape
            break

    if not shape_to_update:
        print("Shape ID not found.")
        return

    shape_type = shape_to_update.shape_type

    if shape_type == "Rectangle":
        width = get_float_input("Enter the new width of the rectangle: ")
        height = get_float_input("Enter the new height of the rectangle: ")
        manager.update_shape(
            shape_id, Rectangle(manager.shape_id, width, height).to_dict()
        )
    elif shape_type == "Square":
        side = get_float_input("Enter the new size of the side of the square: ")
        manager.update_shape(shape_id, Square(manager.shape_id, side).to_dict())
    elif shape_type == "Circle":
        radius = get_float_input("Enter the new radius of the circle: ")
        manager.update_shape(shape_id, Circle(manager.shape_id, radius).to_dict())
    elif shape_type == "Triangle":
        base = get_float_input("Enter the new base of the Triangle: ")
        height = get_float_input("Enter the new height of the Triangle: ")
        side1 = get_float_input(
            "Enter the new size of the first side of the triangle: "
        )
        side2 = get_float_input(
            "Enter the new size of the second side of the triangle: "
        )
        side3 = get_float_input(
            "Enter the new size of the third side of the triangle: "
        )
        manager.update_shape(
            shape_id,
            Triangle(manager.shape_id, base, height, side1, side2, side3).to_dict(),
        )
    elif shape_type == "Hexagon":
        side = get_float_input("Enter the new size of the side of the hexagon: ")
        manager.update_shape(shape_id, Hexagon(manager.shape_id, side).to_dict())


def handle_delete_shape():
    shape_id = get_int_input("Enter the shape ID you want to delete: ")
    manager.delete_shape(shape_id)


def main():
    print("=====================")
    print("=== Shape Manager ===")
    print("=====================\n")
    while True:
        open_menu()
        user_input = handle_user_input()

        if user_input == 1:
            handle_add_shape()
        elif user_input == 2:
            handle_show_shapes()
        elif user_input == 3:
            handle_update_shape()
        elif user_input == 4:
            handle_delete_shape()
        elif user_input == 5:
            break


if __name__ == "__main__":
    main()
