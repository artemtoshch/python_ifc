import ifcopenshell
import ifcopenshell.util.element
filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall")
print("Количество стен в модели:", len(walls))

first_wall = walls[0]
print("\nИнформация о первой стене:")
print(f"GlobalId: {first_wall.GlobalId}")
print(f"Name: {first_wall.Name}")
print(f"ObjectType: {first_wall.ObjectType}")

psets = ifcopenshell.util.element.get_psets(first_wall)
print(psets)
for pset_name, props in psets.items():
    print("Pset:", pset_name)
    for prop_name, value in props.items():
        print("    ",prop_name, "=", value)