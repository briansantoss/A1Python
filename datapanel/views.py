from shutil import rmtree
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from static.machine import treino_ml


@login_required(login_url='login')
def data_panel(request):
    if request.method == 'GET':
        return render(request, 'data_panel/data_panel.html')

    # Apagando o diretório client_data e seu conteúdo
    rmtree(settings.MEDIA_ROOT, ignore_errors=True)

    # Obtendo o novo arquivo enviado no formulário
    dataset_file = request.FILES['file']

    # Salvando a entrada fisicamente no sistema de arquivos e obtendo seu nome
    fs = FileSystemStorage()
    filename = fs.save(dataset_file.name, dataset_file)

    # Lendo o arquivo de dataset padrão
    df = pd.read_csv(settings.DEF_DATASET, sep=",")

    # Construindo o caminho absoluto para o arquivo
    file_path = (settings.MEDIA_ROOT / filename).absolute()

    try:
        df_input = pd.read_csv(file_path, sep=',', quotechar='"')
    except (pd.errors.ParserError, ValueError) as e:
        return render(request, 'data_panel/data_panel.html', {'invalid_csv'})

    if not df.columns.equals(df_input.columns):
        return render(request, 'data_panel/data_panel.html', {'invalid_csv': True})

    acuracia_final = treino_ml(file_path)
    return render(request, 'data_panel/data_panel.html', {'acuracia_final': acuracia_final})
