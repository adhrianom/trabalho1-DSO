from view.SistemaView import SistemaView
from controller.SistemaController import SistemaController

def main():
    view = SistemaView()
    controller = SistemaController(view)
    view.configurarController(controller)
    view.mostrarMenuPrincipal()
    view.iniciar()

if __name__ == "__main__":
    main()