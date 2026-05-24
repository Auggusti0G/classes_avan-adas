from typing import List

# ==========================================
# SUPERCLASSE (Classe 1)
# ==========================================
class Dispositivo:
    """Superclasse que define as propriedades básicas de qualquer eletrônico."""
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.ligado: bool = False

    def ligar(self) -> None:
        """Método 1: Altera o estado do dispositivo para ligado."""
        self.ligado = True
        print(f"[STATUS] O {self.modelo} está agora LIGADO.")

    def desligar(self) -> None:
        """Método 2: Altera o estado do dispositivo para desligado."""
        self.ligado = False
        print(f"[STATUS] O {self.modelo} está agora DESLIGADO.")


# ==========================================
# SUBCLASSES (Classes 2 e 3)
# ==========================================
class Smartphone(Dispositivo):
    """Subclasse que herda de Dispositivo e adiciona recursos de celular."""
    def __init__(self, marca: str, modelo: str, armazenamento: int) -> None:
        super().__init__(marca, modelo)
        self.armazenamento: int = armazenamento

    def instalar_app(self, nome_app: str) -> None:
        """Método 3: Simula a instalação de um aplicativo."""
        if self.ligado:
            print(f"[STORE] Aplicativo '{nome_app}' instalado com sucesso no {self.modelo}.")
        else:
            print(f"[ERRO] Ligue o {self.modelo} antes de instalar aplicativos.")

    def fazer_chamada(self, numero: str) -> None:
        """Método 4: Simula uma ligação telefônica."""
        if self.ligado:
            print(f"[TELEFONIA] Discando para {numero} através do {self.modelo}...")
        else:
            print(f"[ERRO] Impossível completar a ligação com o dispositivo desligado.")


class Notebook(Dispositivo):
    """Subclasse que herda de Dispositivo e adiciona recursos de computador."""
    def __init__(self, marca: str, modelo: str, ram: int) -> None:
        super().__init__(marca, modelo)
        self.ram: int = ram

    def abrir_programa(self, programa: str) -> None:
        """Método 5: Simula a abertura de um software."""
        if self.ligado:
            print(f"[SISTEMA O.P.] Executando '{programa}' utilizando {self.ram}GB de RAM.")
        else:
            print(f"[ERRO] Notebook precisa estar ligado para abrir programas.")

    def compilar_codigo(self) -> None:
        """Método 6: Simula o processamento de código de programação."""
        if self.ligado:
            print(f"[DEV] Compilando arquivos do projeto... Sucesso!")
        else:
            print(f"[ERRO] Ligue o computador para processar códigos.")


# ==========================================
# CLASSE GERENCIADORA INDEPENDENTE (Classe 4)
# ==========================================
class LaboratorioTI:
    """Classe responsável por gerenciar listas de dispositivos usando loops."""
    def __init__(self, nome_sala: str) -> None:
        self.nome_sala: str = nome_sala
        self.inventario: List[Dispositivo] = [] # Lista de objetos

    def adicionar_dispositivo(self, aparelho: Dispositivo) -> None:
        """Método 7: Adiciona um objeto de qualquer subclasse ao inventário."""
        self.inventario.append(aparelho)
        print(f"[INVENTÁRIO] {aparelho.modelo} adicionado ao {self.nome_sala}.")

    def listar_equipamentos(self) -> None:
        """Método 8: Varre a lista interna usando um loop 'for'."""
        print(f"\n--- EQUIPAMENTOS DO {self.nome_sala.upper()} ---")
        for dispositivo in self.inventario:
            estado = "Ligado" if dispositivo.ligado else "Desligado"
            print(f"• {dispositivo.marca} {dispositivo.modelo} | Status: {estado}")


# ==========================================
# EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == "__main__":
    # Inicializando a classe gerenciadora (Classe 4)
    meu_lab = LaboratorioTI("Laboratório de Redes")

    # Inicializando as subclasses (Classes 2 e 3) que herdam da Superclasse (Classe 1)
    celular = Smartphone(marca="Apple", modelo="iPhone 15", armazenamento=128)
    computador = Notebook(marca="Dell", modelo="Inspiron", ram=16)

    # Executando e testando os 8 métodos operacionais:
    
    # Métodos 1 e 2 (Herdados da Superclasse)
    computador.ligar()
    celular.ligar()
    
    # Métodos 3 e 4 (Exclusivos do Smartphone)
    celular.instalar_app("WhatsApp")
    celular.fazer_chamada("190")
    
    # Métodos 5 e 6 (Exclusivos do Notebook)
    computador.abrir_programa("VS Code")
    computador.compilar_codigo()
    
    # Métodos 7 e 8 (Exclusivos do Gerenciador de Listas)
    meu_lab.adicionar_dispositivo(celular)
    meu_lab.adicionar_dispositivo(computador)
    meu_lab.listar_equipamentos()