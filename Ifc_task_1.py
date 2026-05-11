import ifcopenshell
filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall")
print("Число стен:", len(walls))