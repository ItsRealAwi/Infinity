pythonpath = f'{input("Enter the python path (python.exe):")}'
import os

ppath = os.path.abspath(os.path.dirname(pythonpath))

sitepackages = os.path.join(ppath, 'lib', 'site-packages', 'IAPI')
try:
    os.mkdir(sitepackages)
except FileExistsError:
    pass
import requests

# URL для получения содержимого папки
url = "https://api.github.com/repos/ItsRealAwi/Infinity/contents/IAPI"

# Отправляем запрос
response = requests.get(url)
filesr = {}

if response.status_code == 200:
    files = response.json()
    for file in files:
        if file['type'] == 'file':  # Если это файл, а не папка
            file_url = file['download_url']
            file_name = file['name']
            file_data = requests.get(file_url).content  # Получаем данные файла
            filesr.update({file_name: file_data})
            print({file_name: file_data})
else:
    print(f"Ошибка при запросе: {response.status_code}")
    input()
    exit()

# Запись файлов в папку
for file_name, file_data in filesr.items():
    try:
        file_path = os.path.join(sitepackages, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_data)
        print(f"Файл {file_name} успешно записан.")
    except Exception as e:
        print(f"Ошибка при записи файла {file_name}: {e}")