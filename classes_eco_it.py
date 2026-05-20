from datetime import datetime
from typing import List, Dict, Optional
import math

# ==========================================
# 11.1.3 PERFIL USUÁRIO
# ==========================================
class PerfilUsuario:
    """Extensão das informações do usuário, focada em localização e privacidade."""
    def __init__(self, id_perfil: int, endereco: str, cidade: str, uf: str, cep: str) -> None:
        self.idPerfil: int = id_perfil
        self.endereco: str = endereco
        self.cidade: str = cidade
        self.uf: str = uf
        self.cep: str = cep
        self.permitirLocalizacao: bool = False

    def atualizarEndereco(self, novo_endereco: str, nova_cidade: str, nova_uf: str, novo_cep: str) -> None:
        self.endereco = novo_endereco
        self.cidade = nova_cidade
        self.uf = nova_uf
        self.cep = novo_cep
        print(f"[Perfil] Endereço atualizado com sucesso para: {self.endereco}.")

    def ativarLocalizacao(self) -> None:
        self.permitirLocalizacao = True
        print("[Privacidade] Permissão de localização ATIVADA.")

    def desativarLocalizacao(self) -> None:
        self.permitirLocalizacao = False
        print("[Privacidade] Permissão de localização DESATIVADA.")


# ==========================================
# 11.1.2 USUÁRIO
# ==========================================
class Usuario:
    """Classe central que representa o ator principal do sistema."""
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, telefone: str) -> None:
        self.idUsuario: int = id_usuario
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.telefone: str = telefone
        self.dataCadastro: datetime = datetime.now()
        self.statusConta: str = "Inativo"
        self.perfil: Optional[PerfilUsuario] = None

    def cadastrar(self, perfil: PerfilUsuario) -> bool:
        self.perfil = perfil
        self.statusConta = "Ativo"
        print(f"[Conta] Usuário {self.nome} cadastrado e ativo com sucesso!")
        return True

    def login(self, email: str, senha: str) -> bool:
        if self.email == email and self.senha == senha:
            print(f"[Autenticação] Login bem-sucedido! Bem-vindo, {self.nome}.")
            return True
        print("[Autenticação] Falha no login: Email ou senha incorretos.")
        return False

    def logout(self) -> None:
        print(f"[Autenticação] Usuário {self.nome} efetuou logout do sistema.")

    def atualizarPerfil(self, novo_nome: str, novo_telefone: str) -> None:
        self.nome = novo_nome
        self.telefone = novo_telefone
        print("[Conta] Dados cadastrais básicos atualizados.")


# ==========================================
# 11.1.5 LOCALIZAÇÃO
# ==========================================
class Localizacao:
    """Gerencia as coordenadas geográficas e posicionamento regional."""
    def __init__(self, id_localizacao: int, latitude: float, longitude: float, cidade: str, regiao: str) -> None:
        self.idLocalizacao: int = id_localizacao
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.cidade: str = cidade
        self.regiao: str = regiao

    def capturarLocalizacao(self) -> tuple:
        return (self.latitude, self.longitude)

    def calcularDistancia(self, lat_destino: float, lon_destino: float) -> float:
        """Calcula a distância euclidiana simples entre dois pontos (aproximação)."""
        distancia = math.sqrt((self.latitude - lat_destino)**2 + (self.longitude - lon_destino)**2)
        return distancia * 111.0  # Conversão aproximada para Quilômetros

    def filtrarPorRegiao(self, lista_locais: List['Localizacao'], regiao_busca: str) -> List['Localizacao']:
        """MÉTODO CONCRETO COM LISTA E FOR: Filtra uma lista de localizações por região."""
        locais_filtrados: List[Localizacao] = []
        for local in lista_locais:
            if local.regiao.lower() == regiao_busca.lower():
                locais_filtrados.append(local)
        return locais_filtrados


# ==========================================
# 11.1.6 PONTO DE RECICLAGEM
# ==========================================
class PontoReciclagem:
    """Representa os locais físicos para descarte de resíduos."""
    def __init__(self, id_ponto: int, nome_ponto: str, endereco: str, cidade: str, regiao: str, 
                 latitude: float, longitude: float, horario: str, tipo_residuo: List[str]) -> None:
        self.idPonto: int = id_ponto
        self.nomePonto: str = nome_ponto
        self.endereco: str = endereco
        self.cidade: str = cidade
        self.regiao: str = regiao
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.horarioFuncionamento: str = horario
        self.tipoResiduoAceito: List[str] = tipo_residuo
        self.statusAtivo: bool = True

    @staticmethod
    def buscarPorRegiao(lista_pontos: List['PontoReciclagem'], regiao_alvo: str) -> List['PontoReciclagem']:
        """MÉTODO CONCRETO COM LISTA E FOR: Retorna os pontos ativos de uma região."""
        resultado: List[PontoReciclagem] = []
        for ponto in lista_pontos:
            if ponto.regiao.lower() == regiao_alvo.lower() and ponto.statusAtivo:
                resultado.append(ponto)
        return resultado

    @staticmethod
    def listarPontos(lista_pontos: List['PontoReciclagem']) -> None:
        """MÉTODO CONCRETO COM LISTA E FOR: Varre e imprime todos os pontos cadastrados."""
        print("\n--- LISTAGEM DE PONTOS DE RECICLAGEM ---")
        for ponto in lista_pontos:
            status = "Ativo" if ponto.statusAtivo else "Inativo"
            print(f"ID: {ponto.idPonto} | {ponto.nomePonto} | Resíduos: {', '.join(ponto.tipoResiduoAceito)} | [{status}]")

    def exibirDetalhes(self) -> str:
        return (f"Ponto: {self.nomePonto}\nEndereço: {self.endereco}, {self.cidade}\n"
                f"Funcionamento: {self.horarioFuncionamento}\nAceita: {', '.join(self.tipoResiduoAceito)}")


# ==========================================
# 11.1.7 SCORE
# ==========================================
class Score:
    """Sistema de gamificação para monitorar engajamento e contribuições."""
    def __init__(self, id_score: int) -> None:
        self.idScore: int = id_score
        self.pontosTotais: int = 0
        self.nivelUsuario: int = 1
        self.ultimaAtualizacao: datetime = datetime.now()
        self.quantidadeAcoes: int = 0

    def calcularPontos(self, peso_residuo_kg: float, multiplicador_tipo: int) -> int:
        pontos_ganhos = int(peso_residuo_kg * multiplicador_tipo)
        return pontos_ganhos

    def atualizarScore(self, novos_pontos: int) -> None:
        self.pontosTotais += novos_pontos
        self.quantidadeAcoes += 1
        self.ultimaAtualizacao = datetime.now()
        self.verificarNivel()
        print(f"[Score] +{novos_pontos} pontos adicionados! Total atual: {self.pontosTotais}.")

    def exibirPontuacao(self) -> None:
        print(f"--- SCORE CARD ---\nPontuação Total: {self.pontosTotais}\nNível: {self.nivelUsuario}\nAções Realizadas: {self.quantidadeAcoes}")

    def verificarNivel(self) -> None:
        # A cada 500 pontos o usuário sobe de nível
        novo_nivel = (self.pontosTotais // 500) + 1
        if novo_nivel > self.nivelUsuario:
            self.nivelUsuario = novo_nivel
            print(f"🎉 PARABÉNS! Você subiu para o Nível {self.nivelUsuario}!")


# ==========================================
# 11.1.8 FORMULÁRIO
# ==========================================
class Formulario:
    """Coleta dados comportamentais sobre as preferências de descarte."""
    def __init__(self, id_formulario: int) -> None:
        self.idFormulario: int = id_formulario
        self.dataPreenchimento: Optional[datetime] = None
        self.tipoResiduoPreferido: str = ""
        self.frequenciaUso: str = ""
        self.observacoes: str = ""

    def preencherFormulario(self, residuo: str, frequencia: str, obs: str) -> None:
        self.tipoResiduoPreferido = residuo
        self.frequenciaUso = frequencia
        self.observacoes = obs
        self.dataPreenchimento = datetime.now()

    def editarFormulario(self, residuo: str, frequencia: str, obs: str) -> None:
        self.preencherFormulario(residuo, frequencia, obs)
        print("[Formulário] Respostas atualizadas com sucesso.")

    def enviarFormulario(self) -> bool:
        if self.dataPreenchimento:
            print("[Formulário] Dados enviados com sucesso para a central de análise.")
            return True
        print("[Formulário] Erro: Preencha o formulário antes de enviar.")
        return False


# ==========================================
# 11.1.9 ATENDIMENTO IA
# ==========================================
class AtendimentoIA:
    """Interface de suporte automatizado para dúvidas de reciclagem."""
    def __init__(self, id_atendimento: int) -> None:
        self.idAtendimento: int = id_atendimento
        self.pergunta: str = ""
        self.resposta: str = ""
        self.dataHora: Optional[datetime] = None
        self.statusAtendimento: str = "Aberto"

    def enviarPergunta(self, pergunta_usuario: str) -> None:
        self.pergunta = pergunta_usuario
        self.dataHora = datetime.now()
        self.statusAtendimento = "Em Processamento"
        self.gerarResposta()

    def gerarResposta(self) -> None:
        # Simulação de resposta automatizada inteligente baseada em palavras-chave
        if "plástico" in self.pergunta.lower():
            self.resposta = "Plásticos PET devem ser lavados antes do descarte para evitar contaminação."
        elif "eletrônico" in self.pergunta.lower():
            self.resposta = "Resíduos eletrônicos possuem metais pesados e devem ir apenas para pontos especializados."
        else:
            self.resposta = "Obrigado por sua pergunta! Lembre-se de sempre separar o lixo úmido do lixo seco."
        
        self.statusAtendimento = "Concluído"

    def consultarHistorico(self) -> str:
        return f"[{self.dataHora}] P: {self.pergunta}\nR: {self.resposta} ({self.statusAtendimento})"


# ==========================================
# 11.1.10 HISTÓRICO CONSULTA
# ==========================================
class HistoricoConsulta:
    """Armazena o registro de consultas estruturadas realizadas no sistema."""
    def __init__(self, id_historico: int) -> None:
        self.idHistorico: int = id_historico
        self.dataHora: datetime = datetime.now()
        self.tipoConsulta: str = ""
        self.descricaoConsulta: str = ""
        self._registros: List[Dict[str, str]] = [] # Lista interna para simulação de banco de dados

    def registrarConsulta(self, tipo: str, descricao: str) -> None:
        registro = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "tipo": tipo,
            "descricao": descricao
        }
        self._registros.append(registro)

    def listarHistorico(self) -> List[Dict[str, str]]:
        """MÉTODO CONCRETO COM LISTA E FOR: Retorna e exibe todo o histórico."""
        print(f"\n--- LOGS DE CONSULTAS (ID HISTÓRICO: {self.idHistorico}) ---")
        for reg in self._registros:
            print(f"[{reg['data']}] Tipo: {reg['tipo']} | Ação: {reg['descricao']}")
        return self._registros

    def limparHistorico(self) -> None:
        self._registros.clear()
        print("[Histórico] Logs limpos com sucesso.")


# ==========================================
# 11.1.11 NOTIFICAÇÃO
# ==========================================
class Notificacao:
    """Gerencia as mensagens diretas e alertas enviados ao usuário."""
    def __init__(self, id_notificacao: int, titulo: str, mensagem: str) -> None:
        self.idNotificacao: int = id_notificacao
        self.titulo: str = titulo
        self.mensagem: str = mensagem
        self.dataEnvio: datetime = datetime.now()
        self.lida: bool = False

    def enviarNotificacao(self, usuario_destino: Usuario) -> None:
        print(f"[Notificação para {usuario_destino.nome}]: {self.titulo} - {self.mensagem}")

    def marcarComoLida(self) -> None:
        self.lida = True


# ==========================================
# 11.1.12 AGENDA CALENDÁRIO
# ==========================================
class AgendaCalendario:
    """Organiza eventos, coletas planejadas ou compromissos do usuário."""
    def __init__(self, id_agenda: int) -> None:
        self.idAgenda: int = id_agenda
        self.eventos: List[Dict[str, any]] = [] # Lista interna para gerenciamento

    def adicionarEvento(self, data: str, hora: str, descricao: str, tipo: str) -> None:
        evento = {
            "data": data,
            "hora": hora,
            "descricao": descricao,
            "tipo": tipo,
            "status": "Agendado"
        }
        self.eventos.append(evento)
        print(f"[Agenda] Evento '{descricao}' adicionado para o dia {data}.")

    def editarEvento(self, descricao_procurada: str, nova_data: str, nova_hora: str) -> None:
        """MÉTODO CONCRETO COM LISTA E FOR: Varre a lista de eventos procurando pelo nome."""
        for ev in self.eventos:
            if ev["descricao"] == list_procurada := descricao_procurada:
                ev["data"] = nova_data
                ev["hora"] = nova_hora
                print(f"[Agenda] Evento '{descricao_procurada}' modificado com sucesso.")
                return
        print("[Agenda] Evento não encontrado.")

    def removerEvento(self, descricao_remover: str) -> None:
        """MÉTODO CONCRETO COM LISTA E FOR: Localiza e apaga um evento da agenda."""
        for ev in self.eventos:
            if ev["descricao"] == descricao_remover:
                self.eventos.remove(ev)
                print(f"[Agenda] Evento '{descricao_remover}' removido da sua folha.")
                return

    def listarEventos(self) -> List[Dict[str, any]]:
        """MÉTODO CONCRETO COM LISTA E FOR: Lista cronologicamente os compromissos."""
        print("\n--- SEU CALENDÁRIO DE EVENTOS/COLETAS ---")
        for ev in self.eventos:
            print(f"📅 {ev['data']} às {ev['hora']} | Tipo: {ev['tipo']} | {ev['descricao']} [{ev['status']}]")
        return self.eventos


# ==========================================
# 11.1.4 TELA PRINCIPAL (ORQUESTRAÇÃO DO SISTEMA)
# ==========================================
class TelaPrincipal:
    """Classe de interface responsável por orquestrar e conectar as classes."""
    def __init__(self, id_tela: int, nome_tela: str, descricao: str) -> None:
        self.idTela: int = id_tela
        self.nomeTela: str = nome_tela
        self.descricao: str = description = descricao

    def exibirMenu(self) -> None:
        print(f"\n====================================\n {self.nomeTela.upper()} \n====================================")
        print("1. Acessar Atendimento IA\n2. Acessar Pontos de Reciclagem\n3. Acessar Agenda\n4. Acessar Score")

    def acessarAtendimentoIA(self, atendimento: AtendimentoIA, pergunta: str) -> None:
        print("\n[Navegação] Redirecionando para o Atendimento Automatizado...")
        atendimento.enviarPergunta(pergunta)
        print(atendimento.consultarHistorico())

    def acessarPontosReciclagem(self, base_pontos: List[PontoReciclagem], regiao: str) -> None:
        print(f"\n[Navegação] Buscando pontos de coleta próximos na região: {regiao}")
        pontos_locais = PontoReciclagem.buscarPorRegiao(base_pontos, regiao)
        PontoReciclagem.listarPontos(pontos_locais)

    def acessarAgenda(self, agenda: AgendaCalendario) -> None:
        print("\n[Navegação] Abrindo Calendário Integrado...")
        agenda.listarEventos()

    def acessarScore(self, score_usuario: Score) -> None:
        print("\n[Navegação] Solicitando dados de Pontuação ao Servidor...")
        score_usuario.exibirPontuacao()


# ==========================================
# SIMULAÇÃO DE FLUXO DE EXECUÇÃO REAL
# ==========================================
if __name__ == "__main__":
    # Instanciando Usuário e Perfil
    perfil_rafael = PerfilUsuario(1, "Rua das Palmeiras, 100", "Brasília", "DF", "70000-000")
    usuario_rafael = Usuario(1, "Rafael Augusto", "rafael@email.com", "senha123", "61999999999")
    usuario_rafael.cadastrar(perfil_rafael)
    
    # Validando o Login
    if usuario_rafael.login("rafael@email.com", "senha123"):
        
        # Gerenciamento de Gamificação (Score)
        score_rafael = Score(id_score=10)
        score_rafael.atualizarScore(600) # Vai atingir pontuação para subir de nível 
        
        # Criação de um Banco de Pontos de Reciclagem (Lista)
        banco_pontos = [
            PontoReciclagem(101, "EcoPonto Central", "Av. W3 Sul", "Brasília", "Asa Sul", -15.82, -47.92, "08:00 - 18:00", ["Plástico", "Vidro"]),
            PontoReciclagem(102, "Recicla Norte", "Av. W3 Norte", "Brasília", "Asa Norte", -15.75, -47.89, "09:00 - 17:00", ["Eletrônicos", "Metais"]),
            PontoReciclagem(103, "Posto Sul Coleta", "SQS 214", "Brasília", "Asa Sul", -15.83, -47.93, "24h", ["Papel", "Plástico"])
        ]
        
        # Operações com a Agenda
        agenda_rafael = AgendaCalendario(id_agenda=55)
        agenda_rafael.adicionarEvento("20/05/2026", "14:00", "Descarte de Eletrônicos Velhos", "Coleta")
        agenda_rafael.adicionarEvento("25/05/2026", "09:00", "Mutirão de Limpeza da Quadra", "Comunidade")
        
        # Criação de Atendimento e Histórico
        ia = AtendimentoIA(id_atendimento=999)
        historico = HistoricoConsulta(id_historico=7)
        historico.registrarConsulta("Busca", "Pesquisa por postos de metal na Asa Norte")
        
        # Orquestração via Interface Gráfica simulada (TelaPrincipal)
        dashboard = TelaPrincipal(id_tela=1, nome_tela="Portal Eco-Sustentável", descricao="Painel de Controle Principal do Cidadão")
        dashboard.exibirMenu()
        
        # Testando os acessos unificados da Tela Principal
        dashboard.acessarScore(score_rafael)
        dashboard.acessarAtendimentoIA(ia, "Como faço para descartar um monitor eletrônico quebrado?")
        dashboard.acessarPontosReciclagem(banco_pontos, "Asa Sul")
        dashboard.acessarAgenda(agenda_rafael)
        
        # Exibição do Log final
        historico.listarHistorico()