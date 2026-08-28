from colorama import Fore, Style
#Mostrar los números del 0 al 9
for number in range(10):
    if number % 2 == 0:
        print(Fore.GREEN + f"{number} es par."+ Style.RESET_ALL)
    else:
        print(Fore.RED + f"{number} es impar."+ Style.RESET_ALL)


