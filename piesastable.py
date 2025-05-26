from tabulate import tabulate
tabla = [["Acero de Titanes", 12], ["Sombra Eterna", 20]]
print(tabulate(tabla, headers=["Material", "Cantidad"]))
# Precios unitarios
PRECIOS = {
    "acero_titanes": 2800 / 20,
    "saronita": 1800 / 20,
    "sombra": 450 / 20,
    "tierra": 280 / 20
}

# Recetas por pieza
RECETAS = {
    "pierna": {
        "acero_titanes": 12,
        "saronita": 8,
        "sombra": 20
    },
    "pies": {
        "acero_titanes": 8,
        "saronita": 5,
        "tierra": 12
    }
}

def calcular_materiales_y_costos(tipo, cantidad):
    materiales = RECETAS[tipo]
    total_materiales = {}
    total_costos_material = {}
    costo_unitario = 0
    tabla = []

    for mat, cant in materiales.items():
        total = cant * cantidad
        total_materiales[mat] = total
        total_costo = total * PRECIOS[mat]
        total_costos_material[mat] = total_costo
        costo_unitario += cant * PRECIOS[mat]
        tabla.append([mat.replace("_", " ").capitalize(), total, f"{total_costo:.2f} monedas"])

    costo_total = costo_unitario * cantidad
    return total_materiales, total_costos_material, costo_unitario, costo_total, tabla

def sumar_diccionarios(diccionarios):
    resumen = {}
    for dic in diccionarios:
        for k, v in dic.items():
            resumen[k] = resumen.get(k, 0) + v
    return resumen

def mostrar_tabla(tabla, titulo):
    print(f"\n=== {titulo} ===")
    print(tabulate(tabla, headers=["Material", "Cantidad", "Costo"], tablefmt="fancy_grid"))

def guardar_en_txt(resumen_tablas, costo_final):
    with open("resumen_materiales.txt", "w", encoding="utf-8") as file:
        for titulo, tabla in resumen_tablas:
            file.write(f"=== {titulo} ===\n")
            file.write(tabulate(tabla, headers=["Material", "Cantidad", "Costo"], tablefmt="grid"))
            file.write("\n\n")
        file.write(f"💵 Costo total general: {costo_final:.2f} monedas\n")


# Entradas del usuario
cant_piernas = int(input("Ingrese la cantidad de piezas de piernas: "))
mats_piernas, costos_piernas, costo_unit_pierna, total_piernas, tabla_piernas = calcular_materiales_y_costos("pierna", cant_piernas)

cant_pies = int(input("Ingrese la cantidad de piezas de pies: "))
mats_pies, costos_pies, costo_unit_pies, total_pies, tabla_pies = calcular_materiales_y_costos("pies", cant_pies)

# Totales generales
total_materiales = sumar_diccionarios([mats_piernas, mats_pies])
total_costos = sumar_diccionarios([costos_piernas, costos_pies])
costo_final = total_piernas + total_pies

# Crear tablas resumen
tabla_total = [[mat.replace("_", " ").capitalize(), total_materiales[mat], f"{total_costos[mat]:.2f} monedas"] for mat in total_materiales]

# Mostrar en consola
mostrar_tabla(tabla_piernas, f"Materiales para {cant_piernas} Pierna(s)")
mostrar_tabla(tabla_pies, f"Materiales para {cant_pies} Pie(s)")
mostrar_tabla(tabla_total, "Totales generales")
print(f"\n💵 Costo total general: {costo_final:.2f} monedas")

# Guardar en archivo
guardar_en_txt([
    (f"Materiales para {cant_piernas} Pierna(s)", tabla_piernas),
    (f"Materiales para {cant_pies} Pie(s)", tabla_pies),
    ("Totales generales", tabla_total)
], costo_final)

print("\n📄 Resumen guardado en 'resumen_materiales.txt'")
