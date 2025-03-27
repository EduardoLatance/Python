import os

def renomear_arquivos(caminho_pasta, prefixo=None, numerar=False):
    """
    Função para renomear arquivos em uma pasta.
    - caminho_pasta: Diretório onde os arquivos estão localizados.
    - prefixo: String a ser adicionada no início do nome dos arquivos (opcional).
    - numerar: Se True, adiciona um número sequencial antes do nome (ex.: 001_, 002_).
    """

    #Verifica se o caminho da pasta existe
    if  not os.path.exists(caminho_pasta):
        print("Erro: A pasta especificada não existe!")
        return
    
    #Lista todos os arquivos na pasta
    arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f ))]

    if not arquivos:
        print("Nenhum arquivo encontrado na pasta!")
        return
    
    #Contador para numeração sequencial
    contador = 1

    #Percorre cada arquivo na pasta
    for arquivo in arquivos:
        #Separa o nome do arquivo e sua extensão
        nome_base, extensao = os.path.splitext(arquivo)

        #Cria o novo nome do arquivo
        novo_nome = ""

        if numerar:
            #Adiciona um número sequencial com 3 digitos (ex. 001, 002)
            novo_nome += f"{contador:03d}_"
            contador + 1 

        if prefixo:
          #Adiciona o prefixo, se fornecido
          novo_nome += prefixo
        
        #Adiciona o nome original e a extensão
        novo_nome +=nome_base + extensao

        #Caminhos completos do arquivo original e do novo arquivo
        caminho_antigo = os.path.join(caminho_pasta, arquivo)
        caminho_novo = os.path.join(caminho_pasta, novo_nome)

        #Renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> {novo_nome}")

    print("Ronomeação Concluída")

# Exemplo de uso
if __name__ == "__main__":
    # Defina o caminho da pasta onde estão os arquivos
    pasta = "c:/Users/Eduardo/OneDrive/Desktop/GitHub/Automação de Tarefas - Renomear Arquivos"  # Substitua pelo caminho real
    
    # Opções de renomeação
    renomear_arquivos(
        caminho_pasta=pasta,
        prefixo="novo_",  # Adiciona o prefixo "novo_" aos nomes
        numerar=True      # Adiciona numeração sequencial
    )
