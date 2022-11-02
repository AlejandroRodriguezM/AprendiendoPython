# test1
def division(num1, num2):
    try:
        num3 = num1 / num2
        return num3
    except Exception:
        print("No se puede dividir entre 0")


if __name__ == '__main__':
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print(division(num1, num2))
