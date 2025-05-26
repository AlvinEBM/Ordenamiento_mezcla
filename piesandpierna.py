

precioAcero=2800/20
precioSaroniraPrimordia=1800/20
precioTierraEterna=280/20
precioSombraEterna=450/20
precioFuegoEterno=750/20
precioAguaEterna=350/20

def pierna():
   return 12,8,20

acero_titanes_pierna,saronita_primordial_pierna,sombra_eterna=pierna()

#calculando el precio und de la piera 
precioUndPierna=(precioAcero*acero_titanes_pierna)+(precioSaroniraPrimordia*saronita_primordial_pierna)+(precioSombraEterna*sombra_eterna)
#print(f"\n Precio por und de pierna: {precioUndPierna}")


factor=int(input("ingrese la cantidad de piezas de piernas: "))
saronita_primordial_pierna*=factor
acero_titanes_pierna*=factor
sombra_eterna*=factor

#print("Materiales x" + str(factor) + ":", acero, saronita, sombra)
print(f"Materiales x {factor}")
print(f"Acero de titanes: {acero_titanes_pierna}")
print(f"Saronita primordial: {saronita_primordial_pierna}")
print(f"sombra eterna: {sombra_eterna}")#Acero de titanes: {acero_titanes},Saronita primordial: {saronita_primordial},sombra eterna: {sombra_eterna}")

costoPorPierna=(acero_titanes_pierna*precioAcero)+(saronita_primordial_pierna*precioSaroniraPrimordia)+(sombra_eterna*precioSombraEterna)
print(f"\n Precio por und de pierna: {precioUndPierna}")
print(f"Costo total por pierna: {costoPorPierna:2f} oros")


def pies():
   return 8,6,6,5

acero_titanes_pies,fuego_eterno,agua_eterna,saronita_primordial_pies=pies()

precioUndPIes=(precioAcero*acero_titanes_pies)+(precioFuegoEterno*fuego_eterno)+(precioSaroniraPrimordia*saronita_primordial_pies)+(agua_eterna*precioAguaEterna)
#print(f"\n Precio por und de pies: {precioUndPIes}")


factor=int(input("ingrese la cantidad de pieza de pies: "))
acero_titanes_pies*=factor
agua_eterna*=factor
fuego_eterno*=factor
saronita_primordial_pies*=factor

print(f"Materiales x {factor}")
print(f"Acero de titanes: {acero_titanes_pies}")
print(f"Saronita primordial: {saronita_primordial_pies}")
print(f"Agua eterna: {agua_eterna}")
print(f"Fuego eterno: {fuego_eterno}")

costoPorPies=(precioAcero*acero_titanes_pies)+(precioFuegoEterno*fuego_eterno)+(precioSaroniraPrimordia*saronita_primordial_pies)+(agua_eterna*precioAguaEterna)
print(f"\n Precio por und de pies: {precioUndPIes}")
print(f"Costo total por pie fabricado: {costoPorPies:2f}")
def total_materiales():
   
    total_acero_titanes=acero_titanes_pies+acero_titanes_pierna
    total_saronita_primordial=saronita_primordial_pierna+saronita_primordial_pies
    total_sombraEterna=sombra_eterna
    total_AguaEterna=agua_eterna
    total_FuegoEterno=fuego_eterno

    print("\n ---------TOTAL MATERIALES---------")
    print(f"Acero de titanes: {total_acero_titanes}")   
    print(f"Saronita Primordial: {total_saronita_primordial}")
    print(f"Sombra Eterna: {total_sombraEterna}")
    print(f"Agua Eterna: {total_AguaEterna}")
    print(f"Fuego Eterno: {total_FuegoEterno}")

    total_costo=costoPorPies+costoPorPierna
    print(f"costo total general: {total_costo}")
total_materiales()

costoPierna=3500
constoPies=2400
print(costoPierna*3)
print(constoPies*3)
subasta=costoPierna+constoPies
print(subasta*3)