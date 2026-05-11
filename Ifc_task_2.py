#1
import ifcopenshell
filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall")
print("Количество стен в модели:", len(walls))

#2
first_wall = walls[0]
print("\nИнформация о первой стене:")
print(f"GlobalId: {first_wall.GlobalId}")
print(f"Name: {first_wall.Name}")
print(f"ObjectType: {first_wall.ObjectType}")