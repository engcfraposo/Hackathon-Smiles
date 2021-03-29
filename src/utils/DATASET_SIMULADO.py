import numpy as np



#Variáveis obtidas nas APIs open banking e as cadastradas pelo cliente em nossa plataforma.
'''
PERFIS DE CONCESSÃO DE CRÉDITO 

PERFIL 1 - inadimplente

• Indicador de Endividamento:
- acima de 70%
• Indicador de Poupança:
- abaixo de 10%
• Indicador de Liquidez:
- acima de 80%
• Indicador de Cobertura:
- 1 mês ou menos
• Indicador de Riqueza:
- menor que 0,3
• Score:
- abaixo de 500
• Faixa Salarial:
- até 2 salários mínimos 
• Tempo de Empresa:
- até 1 ano

PERFIL 2 - regular

• Indicador de Endividamento:
- entre 20% a 70%
• Indicador de Poupança:
- entre 10% a 20%
• Indicador de Liquidez:
- entre 60% a 80% 
• Indicador de Cobertura:
- 1 mês a 6 meses
• Indicador de Riqueza:
- entre 0,3 a 0,5
• Score:
- entre 500 a 700
• Faixa Salarial:
- entre 2 a 5 salários mínimos 
• Tempo de Empresa:
- entre 1 a 3 anos

PERFIL 3 - bom pagador

• Indicador de Endividamento:
- até 20% 
• Indicador de Poupança:
-  20% ou mais
• Indicador de Liquidez:
- até 60% 
• Indicador de Cobertura:
- 6 meses ou mais 
• Indicador de Riqueza:
- entre 0,5 e 1
• Score:
- entre 700 a 1000
• Faixa Salarial:
- entre 6 ou mais salários mínimos 
• Tempo de Empresa:
- entre 3 anos ou mais
'''

PerfilI = np.zeros((1, 1000))

idade = np.random.randint(25,89, size=(1, 1000))
Iendiv = np.random.randint(70, 100, size=(1, 1000))
Poup = np.random.randint(9, size=(1, 1000))
Liqui = np.random.randint(81,100, size=(1, 1000))
Cobert = np.random.randint(30, size=(1, 1000))/100
Riqueza = np.random.randint(30, size=(1, 1000))
Score = np.random.randint(499, size=(1, 1000))
Faixa_Salarial  = np.random.randint(1045,2090, size=(1, 1000))
TempoEmpresa= np.random.randint(12, size=(1, 1000))
list = (idade, Iendiv, Poup, Liqui, Cobert, Riqueza, Score, Faixa_Salarial, TempoEmpresa)
for i in list:
    PerfilI= np.vstack((PerfilI,i))
PerfilI = PerfilI.T


PerfilR = np.ones((1, 1000))
idade = np.random.randint(25,89, size=(1, 1000))
Iendiv = np.random.randint(20, 70, size=(1, 1000))
Poup = np.random.randint(10,20, size=(1, 1000))
Liqui = np.random.randint(60, 80, size=(1, 1000))
Cobert = np.random.randint(30, 180, size=(1, 1000))
Riqueza = np.random.randint(30, 50, size=(1, 1000))/100
Score = np.random.randint(500, 700, size=(1, 1000))
Faixa_Salarial  = np.random.randint(2090,5225, size=(1, 1000))
TempoEmpresa= np.random.randint(12, 36, size=(1, 1000))
list = (idade, Iendiv, Poup, Liqui, Cobert, Riqueza, Score, Faixa_Salarial, TempoEmpresa)
for i in list:
    PerfilR= np.vstack((PerfilR,i))
PerfilR = PerfilR.T


PerfilBP = np.ones((1, 1000))+1
idade = np.random.randint(25,89, size=(1, 1000))
Iendiv = np.random.randint(20, size=(1, 1000))
Poup = np.random.randint(20, 100, size=(1, 1000))
Liqui = np.random.randint(60, size=(1, 1000))
Cobert = np.random.randint(72, 288, size=(1, 1000))
Riqueza = np.random.randint(50, 100, size=(1, 1000))/100
Score = np.random.randint(700,1000, size=(1, 1000))
Faixa_Salarial  = np.random.randint(6270, 31350, size=(1, 1000))
TempoEmpresa= np.random.randint(36, 240, size=(1, 1000))
list = (idade, Iendiv, Poup, Liqui, Cobert, Riqueza, Score, Faixa_Salarial, TempoEmpresa)
for i in list:
    PerfilBP= np.vstack((PerfilBP,i))
PerfilBP = PerfilBP.T


PerfilGeral = np.zeros((1,10))
PerfilGeral= np.vstack((PerfilGeral,PerfilI))
PerfilGeral= np.vstack((PerfilGeral,PerfilR))
PerfilGeral= np.vstack((PerfilGeral,PerfilBP))
PerfilGeral = PerfilGeral[1:]

X = PerfilGeral [:,1:]
y = PerfilGeral [:,:1]

print(PerfilGeral)