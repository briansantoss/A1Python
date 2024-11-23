from sklearn.model_selection import train_test_split            # Treino
from sklearn.metrics import accuracy_score                      # Acurácia
from sklearn.tree import DecisionTreeClassifier                 # Árvore de Decisão
from sklearn.metrics import confusion_matrix                    # Matriz de Confusão
from sklearn.feature_selection import SelectKBest, f_classif    # Seleção de dados
from django.conf import settings
import pandas as pd


def treino_ml(file_path):
    df_def = pd.read_csv(settings.DEF_DATASET)
    df_input = pd.read_csv(file_path)  # IMPORTAR O ARQUIVO

    # INITIAL
    print("Dados: ")
    df_input.info()        # Verificar as Informações do DataSet

    print("\n\n")
    print(df_input.head())  # Printado algumas colunas

    # df.isnull().sum()         # NÃO TEM FALTA DE DADOS
    # df.duplicated().sum()     # NÃO TEM DADOS DUPLICADOS

    # VERIFICATION
    print("\n\nValores Padrão de Weather: ")
    print(df_def['weather'].unique())

    df_input['weather'] = df_input['weather'].map({'sun': 0, 'drizzle': 1, 'rain': 2, 'fog': 3, 'snow': 4})  # STRING PARA INT

    print("\nValores Alterados de Weather: ")
    print(df_input['weather'].unique())

    df = df_input[['precipitation', 'temp_max', 'temp_min', 'wind', 'weather']]  # DEIXANDO AS COLUNAS DE TIPO INT/FLOAT

    # TRAIN
    x = df.drop('weather', axis=1)   # PEGANDO TODOS OS DADOS MENOS A WEATHER
    y = df['weather']                # APENAS A WEATHER, QUE VAI SER O RESULTADO

    # 40% DE TEST, VARIAÇÃO = 5
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.40, random_state=5)
    clf = DecisionTreeClassifier(random_state=1)  # DECISION TREE
    clf.fit(x_train, y_train)

    y_prev = clf.predict(x_test)

    print("\n\nACURÁCIA INICIAL: ")
    print(accuracy_score(y_test, y_prev))

    print("\nMATRIZ DE CONFUSÃO INICIAL: ")
    print(confusion_matrix(y_test, y_prev))

    # FILTER
    top = SelectKBest(f_classif, k='all').fit(x, y)
    print("\n\nVALORES RELEVANTES: ")
    print(top.scores_)

    df = df[['precipitation', 'temp_max', 'weather']]  # DEIXANDO AS COLUNAS COM MAIS RELEVANCIA

    # AFTER

    x = df.drop('weather', axis=1)
    y = df['weather']


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.40, random_state=5)

    clf = DecisionTreeClassifier(random_state=1)  # DECISION TREE
    clf.fit(x_train, y_train)

    y_prev = clf.predict(x_test)

    acuracia_final = accuracy_score(y_test, y_prev)

    # RETURN
    print("\n\nACURÁCIA FINAL: ")
    print(acuracia_final)

    print("\nMATRIZ DE CONFUSÃO FINAL: ")
    print(confusion_matrix(y_test, y_prev))

    return acuracia_final
