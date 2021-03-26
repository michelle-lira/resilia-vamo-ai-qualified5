# QUESTÃO 1 FOI PARTE DA 2: JUNTEI OS CÓDIGOS
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    tempo_chegada1 = 1
    tempo_chegada2 = 2
    tempo_chegada3 = 3
    nome_corredor1 = "Jasmin"
    nome_corredor2 = "Luan"
    nome_corredor3 = "Benjamin"
    
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada2 < tempo_chegada3:
        podio_olimpico = (
                 f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                 f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                 f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n"
        )
    elif tempo_chegada1 < tempo_chegada3 and tempo_chegada3 < tempo_chegada2:
        podio_olimpico = (
                 f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                 f"2 - {nome_corredor3} - {tempo_chegada3} minutos\n"
                 f"3 - {nome_corredor2} - {tempo_chegada2} minutos\n"
        )
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada1 < tempo_chegada3:
        podio_olimpico = (
                 f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                 f"2 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                 f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n"
        )
    elif tempo_chegada2 < tempo_chegada3 and tempo_chegada3 < tempo_chegada1:
        podio_olimpico = (
                 f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                 f"2 - {nome_corredor3} - {tempo_chegada3} minutos\n"
                 f"3 - {nome_corredor1} - {tempo_chegada1} minutos\n"
        )
    elif tempo_chegada3 < tempo_chegada1 and tempo_chegada1 > tempo_chegada2:
        podio_olimpico = (
                 f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n"
                 f"2 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                 f"3 - {nome_corredor2} - {tempo_chegada2} minutos\n"
        )
    elif tempo_chegada3 < tempo_chegada2 and tempo_chegada2 < tempo_chegada1:
        podio_olimpico = (
                 f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n"
                 f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                 f"3 - {nome_corredor1} - {tempo_chegada1} minutos\n"
        )
    
    return podio_olimpico


print(podio_olimpico(1, 2, 3, "Fulano1", "Fulano2", "Fulano3"))
    

