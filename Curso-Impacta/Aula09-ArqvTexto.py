# open(<nome do arquivo>, <modo que o arquivo sera lido>)
# r = leitura, w = escrita, a = append (inserir na última linha)
# r+ = leitura e escrita
# Para Windows, arquivos binários (fotos) precisa acrescentar um 'b'
# rb, wb, r+b

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    for linha in arquivo:
        print(linha)

    arquivo.close()

def salvar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)

    arquivo.close()

salvar_arquivo('Curso-Impacta/Aula09-Teste.txt', 'Teste de escrita')
ler_arquivo('Curso-Impacta/Aula09-Pessoas.txt')

