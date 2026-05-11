import ifcopenshell

filepath = r"C:\Users\РС\Desktop\Example_1.ifc"
model = ifcopenshell.open(filepath)

storeys = model.by_type("IfcBuildingStorey")
print("Схема IFC:", model.schema)
print("Количество этажей:", len(storeys))

print("\nСписок этажей:")
for storey in storeys:
    name = storey.Name if storey.Name else "Без имени"
    elevation = storey.Elevation if hasattr(storey, 'Elevation') and storey.Elevation is not None else "None"
    print(f"  Этаж: {name}, Elevation={elevation}")

print("\n" + "="*50)
print("Анализ этажности здания")
print("="*50)    