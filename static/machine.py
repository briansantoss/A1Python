from sklearn.model_selection import train_test_split            ### Treino
from sklearn.metrics import accuracy_score                      ### Acurácia
from sklearn.tree import DecisionTreeClassifier                 ### Árvore de Decisão
from sklearn.metrics import confusion_matrix                    ### Matriz de Confusão
from sklearn.feature_selection import SelectKBest, f_classif    ### Seleção de dados

import pandas as pd

df = pd.read_csv("seattle-weather.csv") ### IMPORTAR O ARQUIVO

### INITIAL
print("Dados: ")
df.info()        ### Verificar as Informações do DataSet

print("\n\n")
print(df.head()) ### Printado algumas colunas

#df.isnull().sum()         ### NÃO TEM FALTA DE DADOS
#df.duplicated().sum()     ### NÃO TEM DADOS DUPLICADOS

### VERIFICATION
print("\n\nValores Padrão de Weather: ")
print(df['weather'].unique())

df['weather'] = df['weather'].map({'sun': 0, 'drizzle': 1, 'rain': 2, 'fog' : 3, 'snow' : 4})  ### STRING PARA INT

print("\nValores Alterados de Weather: ")
print(df['weather'].unique())

df = df[['precipitation', 'temp_max', 'temp_min', 'wind', 'weather']]  ### DEIXANDO AS COLUNAS DE TIPO INT/FLOAT


### TRAIN
X = df.drop('weather', axis=1)   ### PEGANDO TODOS OS DADOS MENOS A WEATHER
y = df['weather']                ### APENAS A WEATHER, QUE VAI SER O RESULTADO

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=5) ### 40% DE TEST, VARIAÇÃO = 5

clf = DecisionTreeClassifier(random_state=1) ### DECISION TREE
clf.fit(X_train, y_train)

y_prev = clf.predict(X_test)

print("\n\nACURÁCIA INICIAL: ")
print(accuracy_score(y_test, y_prev))

print("\nMATRIZ DE CONFUSÃO INICIAL: ")
print(confusion_matrix(y_test, y_prev))


### FILTER
top = SelectKBest(f_classif, k='all').fit(X, y)
print("\n\nVALORES RELEVANTES: ")
print(top.scores_)

df = df[['precipitation', 'temp_max', 'weather']]  ### DEIXANDO AS COLUNAS COM MAIS RELEVANCIA


### AFTER

X = df.drop('weather', axis=1)
y = df['weather']
print("")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=5)

clf = DecisionTreeClassifier(random_state=1) ### DECISION TREE
clf.fit(X_train, y_train)

y_prev = clf.predict(X_test)

### RETURN
print("\n\nACURÁCIA FINAL: ")
print(accuracy_score(y_test, y_prev))

print("\nMATRIZ DE CONFUSÃO FINAL: ")
print(confusion_matrix(y_test, y_prev))
