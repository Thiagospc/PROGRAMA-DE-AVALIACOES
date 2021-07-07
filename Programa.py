from time import sleep
print('<__________Programa de avaliações UFRA__________>')
print()
sleep(1)
# interação com o usuártio
print('Se não tiver alguma das notas a baixo digite 999')
print()
nap1 = float(input('1° NAP: '))
nap2 = float(input('2° NAP: '))
sleep(2)
# ajuda pra substitutiva
if nap1 < nap2:
    nota = nap2
else:
    nota = nap1
# contra usuário loko
if nap1 == 999 or nap2 == 999:
    print('Você necessita das notas para a média!')
elif nap1 > 10 or nap2 > 10:
    print('Notas inválidas, digite notas com valores de 0 a 10.')
else:
    # media
    med = (nap1 + nap2) / 2
    print('Sua média foi {}.'.format(med))
    if med >= 6:
        print('!APROVADO!')
    print()
    # condições para substitutiva
    if med < 6:
        sleep(2)
        sub = float(input('Prova substitutiva: '))
        if sub == 999:
            print('Você necessita das notas para a média!')
        elif sub > 10:
            print('Notas inválidas, digite notas com valores de 0 a 10.')
        else:
            if sub < nap1 and sub < nap2:
                med2 = med
            else:
                med2 = (sub + nota) / 2
            print('Sua média, com a substitutiva, foi {}.'.format(med2))
            if med2 >= 6:
                print('!APROVADO!')
                
                #naf
            elif med2 >= 4 and med2 < 6:
                print('Você precisa tirar {} no NAF'.format(12 - (sub + nota)))
                sleep(2)
                naf = float(input('NAF (RECUPERAÇÃO) :  '))
                med3 = med2 + naf / 2
                print('Sua média foi {}.'.format(med3))
                if med3 >= 6:
                    print('!APROVADO!')
                else:
                    print('!REPROVADO!')
            else:
                print('!REPROVADO!')
print()
print('<__________Programa de avaliações UFRA__________>')
input()
