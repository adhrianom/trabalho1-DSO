from view.SistemaView import SistemaView
from controller.SistemaController import SistemaController

def main():
    view = SistemaView()
    controller = SistemaController(view)
    controller.iniciarSistema()

if __name__ == "__main__":
    main()