import pandas
import numpy as np
import matplotlib.pyplot as plt
file_base_excel = r"C:\Users\victory\Desktop\\BancoDeDados.xlsx"


#ESTRUTURA OS DADOS PARA O EXCEL
tabela_inicial = pandas.read_excel(file_base_excel)                        #le conteudo excel
dados_atuais = tabela_inicial.values[: , 0:]           #seleciona dados uteis (toda linha, e colunas a partire da segunda, pois a preimeira e etiquetas)    
matrix ={'Data': dados_atuais[:,0], 'Lote': dados_atuais[:,1], 'Nota': dados_atuais[:,2], 'Localização': dados_atuais[:,3]} #estrutura dados em matriz para trabalhalos, fazer calculos etc..
tabela = pandas.DataFrame(matrix)                                                                  #prepara dados para salvalos


#aqui a seguir da para fazer os caclculos requeridos e usar ate numpy para fazer calculos e graficos e dashboards..
print("A média das notas desse lote é de:  ",sum(dados_atuais[:,2])/len(dados_atuais[:,2])) #Media das notas totais

#distr frequencia notas
(unique, counts) = np.unique(dados_atuais[:,2], return_counts=True)
frequencies = np.asarray((unique,counts, counts/len(dados_atuais[:,2]))).T
print('a distribuição de frequencia é: ', frequencies)



############ GUI INTERFACE
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
root = Tk()
root.state('zoomed')
root.title('Customer Feedback Dashboard')

########## ESTRUTURA DE FRAME
frame_boxplot=Frame(root)
frame_scatterplot=Frame(root)
frame_histogram=Frame(root)
frame_estatisticas=LabelFrame(root, text='Estatisticas basiscas', padx=5)


def boxplot(frame_boxplot):    
    plt.rcdefaults()
    visualizador, ax = plt.subplots(figsize=(6, 4), dpi=80)
    #Plota o Grafico BoxPlot
    plt.boxplot(dados_atuais[:,2]) #Vetor com os dados
    plt.title("BoxPlot")
    #plt.show()
    canvas_grafico = FigureCanvasTkAgg(visualizador, master=frame_boxplot).get_tk_widget().grid()         #aqui informo para fazer aparecer o grafico dentro de um canvas, se nao abre numa janela propria de matplotlib

def scatterplot(frame_scatterplot):
    plt.rcdefaults()
    visualizador, ax = plt.subplots(figsize=(6, 4), dpi=80)#Plota o Grafico BoxPlot
    # GRAFICO DE NOTAS segmentado por LOTE de produçao
    x = np.arange(0.0, len(dados_atuais[:,2]), 1.0)
    y = dados_atuais[:,1]
    s = 100  #poderiamos atrelar o size a frequencia

    plt.scatter(x, y, s, c="y", alpha=0.5, marker="o")
    plt.xlabel("Notas")
    plt.ylabel("Lote")
    #plt.show()
    canvas_grafico = FigureCanvasTkAgg(visualizador, master=frame_scatterplot).get_tk_widget().grid()


## parametro para histograma
fig, ax = plt.subplots()
def histograma(frame_histogram):    
    # GRAFICO HISTOGRAMA
    visualizador, ax = plt.subplots(figsize=(6, 4), dpi=80)
    #Plota o Grafico BoxPlot
    labels = ['SP', 'RJ', 'MT', 'BA']

    mediaSP_9876 =tabela.loc[(tabela['Localização'] == 'SP')&(tabela['Lote'] == 9876)].mean()[1]
    mediaRJ_9876 =tabela.loc[(tabela['Localização'] == 'RJ')&(tabela['Lote'] == 9876)].mean()[1]
    mediaMT_9876 =tabela.loc[(tabela['Localização'] == 'MT')&(tabela['Lote'] == 9876)].mean()[1]
    mediaBA_9876 =tabela.loc[(tabela['Localização'] == 'BA')&(tabela['Lote'] == 9876)].mean()[1]

    mediaSP_7654 =tabela.loc[(tabela['Localização'] == 'SP')&(tabela['Lote'] == 7654)].mean()[1]
    mediaRJ_7654 =tabela.loc[(tabela['Localização'] == 'RJ')&(tabela['Lote'] == 7654)].mean()[1]
    mediaMT_7654 =tabela.loc[(tabela['Localização'] == 'MT')&(tabela['Lote'] == 7654)].mean()[1]
    mediaBA_7654 =tabela.loc[(tabela['Localização'] == 'BA')&(tabela['Lote'] == 7654)].mean()[1]

    mediaSP_5132 =tabela.loc[(tabela['Localização'] == 'SP')&(tabela['Lote'] == 5132)].mean()[1]
    mediaRJ_5132 =tabela.loc[(tabela['Localização'] == 'RJ')&(tabela['Lote'] == 5132)].mean()[1]
    mediaMT_5132 =tabela.loc[(tabela['Localização'] == 'MT')&(tabela['Lote'] == 5132)].mean()[1]
    mediaBA_5132 =tabela.loc[(tabela['Localização'] == 'BA')&(tabela['Lote'] == 5132)].mean()[1]
        
    lote9876_mean = [mediaSP_9876, mediaRJ_9876, mediaMT_9876, mediaBA_9876]
    lote7654_mean = [mediaSP_7654, mediaRJ_7654, mediaMT_7654, mediaBA_7654]
    lote5132_mean = [mediaSP_5132, mediaRJ_5132, mediaMT_5132, mediaBA_5132]

    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars 
    #fig, ax = plt.subplots()

    rects1 = ax.bar(x - 3*width/3, lote9876_mean, width, label='Lote 9876')
    rects2 = ax.bar(x , lote7654_mean, width,label='7654')
    rects3 = ax.bar(x + 3*width/3, lote5132_mean,width, label='5132')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('NOTA MEDIA')
    ax.set_title('NOTA por ESTADO e LOTE')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    fig.tight_layout()
    #plt.show()
    canvas_grafico = FigureCanvasTkAgg(visualizador, master=frame_histogram).get_tk_widget().grid()


################## TESTE DE HIPOTESIS
from scipy import stats

N = len(dados_atuais[:,2])
#Gaussian1
a = np.random.randn(N) + 2
#Gaussian2
b = np.random.randn(N)

# calculo do desvio padrao
var_a = a.var(ddof=1)
var_b = b.var(ddof=1)
s = np.sqrt((var_a + var_b)/2)
print('esse é o desvio padrao: ', s)

t = (a.mean() - b.mean())/(s*np.sqrt(2/N))
df = 2*N - 2
p = 1 - stats.t.cdf(t,df=df) #calcula pvalue

print("t = " + str(t))
print("p = " + str(2*p))
### You can see that after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.

## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(a,b)
print("t = " + str(t2))
print("p = " + str(p2))




quadro_texto = Text(frame_estatisticas, bg='#F0F0F0',selectbackground='#F0F0F0', selectforeground='black', insertbackground='#F0F0F0', exportselection=0)
quadro_texto.insert(INSERT, "A média das notas desse lote é de:  "+str(sum(dados_atuais[:,2])/len(dados_atuais[:,2])), END, '\n')
quadro_texto.insert(INSERT, '\n', END)
quadro_texto.insert(INSERT, "A distribuição de frequencia é: "+'\n'+ str(frequencies), END, '\n')
quadro_texto.insert(INSERT, '\n', END)    
quadro_texto.insert(INSERT, 'Esse é o desvio padrao: '+str(s)+'\n', END)
quadro_texto.insert(INSERT, '\n', END)    
quadro_texto.insert(INSERT, 'Esses sao os resultados do t-test:'+'\n', END)
quadro_texto.insert(INSERT, "t = " + str(t)+'\n', END)
quadro_texto.insert(INSERT, "p = " + str(2*p)+'\n', END)
quadro_texto.insert(INSERT, "t = " + str(t2)+'\n', END)
quadro_texto.insert(INSERT, "p = " + str(p2)+'\n' ,END)

quadro_texto.bind("<Key>", lambda a: "break")
quadro_texto.grid(row=0)











boxplot(frame_boxplot)    
scatterplot(frame_scatterplot)    
histograma(frame_histogram)    


########## GRID TKINTER
frame_estatisticas.grid(column=0, row=0)
frame_boxplot.grid(column=0, row=1)
frame_scatterplot.grid(column=1, row=0)
frame_histogram.grid(column=1, row=1)


root.mainloop()














