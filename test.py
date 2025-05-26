from tabulate import tabulate

tabla = [["Acero de Titanes", 12], ["Sombra Eterna", 20]]
print(tabulate(tabla, headers=["Material", "Cantidad"]))
