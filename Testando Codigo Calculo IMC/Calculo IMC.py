peso = float(input('Digite o seu peso: (Kg)'))
altura = float(input('Digite a sua altura: (m)'))
imc = peso/(altura**2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do PESO!')
elif 18.5 <= imc < 25:
    print('Você esta no peso IDEAL!')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE!')
elif imc >= 40:
    print('Você esta com OBESIDADE MORBIDA!')
