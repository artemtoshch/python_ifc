import ifcopenshell
import ifcopenshell.api
import shutil

filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)

min_width = 900
doors = model.by_type("IfcDoor")
print("Двери в исходной модели:")
for door in doors:
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    print(f"  {door.Name}: ширина = {width}, высота = {height}")

output_file = r"C:\Users\РС\Desktop\copy_wide_doors.ifc"
shutil.copy2(filepath, output_file)

new_model = ifcopenshell.open(output_file)
for door in new_model.by_type("IfcDoor"):
    width = getattr(door, "OverallWidth", None)
    if width is not None and width < min_width:
        ifcopenshell.api.run("root.remove_product", new_model, product=door)

new_model.write(output_file)

check_model = ifcopenshell.open(output_file)
check_doors = check_model.by_type("IfcDoor")

ok = True
for door in check_doors:
    width = getattr(door, "OverallWidth", None)
    if width is not None and width < min_width:
        ok = False
        print(f"Ошибка: {door.Name} имеет ширину {width} < {min_width}")

if ok:
    print(f"Проверка пройдена. Все {len(check_doors)} двери имеют ширину >= {min_width}")
else:
    print("Проверка не пройдена")