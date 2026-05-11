import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.api

filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")
first_wall = walls[0]

print("Исходное имя:", first_wall.Name)
first_wall.Name = "MODIFIED_" + first_wall.Name

for relation in first_wall.IsDefinedBy:
    if relation.is_a("IfcRelDefinesByProperties") and relation.RelatingPropertyDefinition.Name == "Pset_WallCommon":
        pset = relation.RelatingPropertyDefinition
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"IsExternal": True})
        break

model.write("modified.ifc")

new_model = ifcopenshell.open("modified.ifc")
new_walls = new_model.by_type("IfcWall")
new_first_wall = new_walls[0]

print("Новое имя:", new_first_wall.Name)
psets = ifcopenshell.util.element.get_psets(new_first_wall)
print("IsExternal:", psets.get("Pset_WallCommon", {}).get("IsExternal"))