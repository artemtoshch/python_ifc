import ifcopenshell

filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)

doors = model.by_type("IfcDoor")
min_width = 900
narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    
    print(f"Дверь:", name, "Ширина:", round(width), "Высота:", round(height) if height else None)
    
    if width is not None and width < min_width:
        narrow_doors.append((name, width, height))

print()
if narrow_doors:
    print(f"Количество узких дверей: {len(narrow_doors)}")
    for name, width, height in narrow_doors:
        print(f"{name}: ширина = {round(width)}, высота = {round(height) if height else None}")
else:
    print("Узких дверей не обнаружено.")