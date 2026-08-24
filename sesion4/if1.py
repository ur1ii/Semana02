import os
os.system("cls" if os.name == "nt" else "clear")

from colorama import Fore, Style

#Leer la nota de un estudiante
grade = int(input("Ingresa la nota: "))
if grade >= 70:
    print(Fore.GREEN + "Usted esta aprobado")
else:
    print(Fore.RED + "Su aprendizaje es inicial")
print(Style.RESET_ALL)


