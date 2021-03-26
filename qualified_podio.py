# QUESTÃO 1 QUALIFIED: PODIO OLIMPICO VERSÃO 1
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    """Função para retornar a chegada de 3 corredores em ordem crescente"""
    tempo_chegada1 = 1
    tempo_chegada2 = 2
    tempo_chegada3 = 3
    
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada2 < tempo_chegada3:
        podio_olimpico = (
                 f"1 - {tempo_chegada1} minutos\n"
                 f"2 - {tempo_chegada2} minutos\n"
                 f"3 - {tempo_chegada3} minutos\n"
        )
    elif tempo_chegada1 < tempo_chegada3 and tempo_chegada3 < tempo_chegada2:
        podio_olimpico = (
                 f"1 - {tempo_chegada1} minutos\n"
                 f"2 - {tempo_chegada3} minutos\n"
                 f"3 - {tempo_chegada2} minutos\n"
        )
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada1 < tempo_chegada3:
        podio_olimpico = (
                 f"1 - {tempo_chegada2} minutos\n"
                 f"2 - {tempo_chegada1} minutos\n"
                 f"3 - {tempo_chegada3} minutos\n"
        )
    elif tempo_chegada2 < tempo_chegada3 and tempo_chegada3 < tempo_chegada1:
        podio_olimpico = (
                 f"1 - {tempo_chegada2} minutos\n"
                 f"2 - {tempo_chegada3} minutos\n"
                 f"3 - {tempo_chegada1} minutos\n"
        )
    elif tempo_chegada3 < tempo_chegada1 and tempo_chegada1 > tempo_chegada2:
        podio_olimpico = (
                 f"1 - {tempo_chegada3} minutos\n"
                 f"2 - {tempo_chegada1} minutos\n"
                 f"3 - {tempo_chegada2} minutos\n"
        )
    elif tempo_chegada3 < tempo_chegada2 and tempo_chegada2 < tempo_chegada1:
        podio_olimpico = (
                 f"1 - {tempo_chegada3} minutos\n"
                 f"2 - {tempo_chegada2} minutos\n"
                 f"3 - {tempo_chegada1} minutos\n"
        )
    return podio_olimpico


print(podio_olimpico(1, 2, 3))
