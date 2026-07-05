import random
class Celular:
    def __init__(self, fabricante, modelo, tela,  armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        porcentagem = random.randint(0, 100)
        carga = (porcentagem/100) * self.bateria

        print(f"O Celular está com {porcentagem}% de bateria e {int(carga)}mA de bateria restantes.")


celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False)

celular_android.verificar_carga_bateria()
        