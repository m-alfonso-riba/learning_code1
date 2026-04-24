import traceback

# Logger
from utils.Logger import Logger

num1 = 20
num2 = 0

def main():
    try:
        Logger.add_to_log("info", "Intentando calculo")
        result = num1 / num2
        Logger.add_to_log("info", "Calculo realizado")
        Logger.add_to_log("info", "El resultado es: {}".format(result))
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        Logger.add_to_log("error", "No se puede dividir entre 0...")

main()