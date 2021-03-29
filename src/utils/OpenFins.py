from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical
import numpy as np

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
print(PerfilGeral)

X = PerfilGeral [:,1:]
y = PerfilGeral[:,:1]
y = y.astype(int)
y = to_categorical(y)

# Dividindo o dataset em dados de treino e de teste.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)

# Normalização dos dados.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#  EXECUÇÃO DA REDE PARA OBTENÇÃO DE UM MODELO(APREDIZAGEM) PARA PREDIÇÕES
classifier = Sequential()
classifier.add(Dense(units = 22, kernel_initializer = 'uniform', activation = 'relu', input_dim = 9))
classifier.add(Dropout(p = 0.1))
classifier.add(Dense(units = 22, kernel_initializer = 'uniform', activation = 'relu'))
# classifier.add(Dropout(p = 0.1))
classifier.add(Dense(units = 3, kernel_initializer = 'uniform', activation = 'softmax'))
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
classifier.fit(X_train, y_train, batch_size = 32, epochs = 100)

#MELHORIAS PARA AUMENTAR A ACURÁCIA DA REDE

#implementação da rede com Keras e novas "configurações"
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
def build_classifieres():
    classifier = Sequential()
    classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu', input_dim = 9))
    classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 3, kernel_initializer = 'uniform', activation = 'softmax'))
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return classifier
classifieres = KerasClassifier(build_fn = build_classifieres, batch_size = 32, epochs = 100)
accuracies = cross_val_score(estimator = classifieres, X = X_train, y = y_train, cv = 10, n_jobs = -1)
a= accuracies.mean()
print(a)

# FAZENDO UMA PREDIÇÃO SIMPLES, DE UM CLIENTE FICTÍCIO, APÓS O TREINAMENTO DO REDE.
print(' ')
print(' ')
print('PREDIÇÃO DO PERFIL DO CLIENTE')
print(' ')
Client_01 = classifier.predict(sc.transform(np.array([[66,51,10,66,104,0.33,645,3997,25]])))
for i in Client_01:
    if i[0] > 0.5:
            print('Cliente JOÃO possui: PERFIL O1')
            print('............')
            print('LIBERAR CRÉDTIO DE ATÉ 1.000 REAIS')
    if i[1] > 0.5:
            print('Cliente JOÃO possui: PERFIL O2')
            print('............')
            print('LIBERAR CRÉDTIO DE ATÉ 5.000 REAIS')
    if i[2] > 0.5:
            print('Cliente JOÃO possui: PERFIL O1')
            print('............')
            print('LIBERAR CRÉDTIO DE ATÉ 20.000 REAIS')