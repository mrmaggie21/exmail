print('--------------------------')
print('SEPADOR DE EMAIL BY MR.ROBOT')
print('--------------------------')


bol = open('bol.txt', 'w', encoding='utf8')
ig = open('ig.txt', 'w', encoding='utf8')
hotmail = open('hotmail.txt', 'w', encoding='utf8')
outlook = open('outlook.txt', 'w', encoding='utf8')
gmail = open('gmail.txt', 'w', encoding='utf8')
terra = open('terra.txt', 'w', encoding='utf8')
yahoo = open('yahoo.txt', 'w', encoding='utf8')
outros = open('outros.txt', 'w', encoding='utf8')
arquivo = ''
texto = ''
arq = ''
while True:
    try :
        print('Digite o nome do arquivo .txt ')
        arquivo = input('Nome: ')
        arq = open(arquivo, 'rt', encoding='utf8')
        texto = arq.readlines()
        for linha in texto :
            if '@bol' in linha:
                bol.write(linha)

            elif '@ig' in linha:
                ig.write(linha)

            elif '@terra' in linha:
                terra.write(linha)

            elif '@hotmail' in linha:
                hotmail.write(linha)

            elif '@outlook' in linha:
                outlook.write(linha)  

            elif '@gmail' in linha:
                gmail.write(linha)

            elif '@yahoo' in linha:
                yahoo.write(linha)

            else: {
                outros.write(linha)
        }
        print('PRONTINHO!!!!')
        break;
    except FileNotFoundError:
        print('Nome de arquivo invalido')   


    
    
    
    #arq.close()

#
