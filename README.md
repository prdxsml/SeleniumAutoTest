Минимальные требования:
```shell
pytest==5.1.1
selenium==3.14.0
```

Разворачивание проекта. Для запуска команды требуется находиться в одной директории с файлом requirements.txt (список внешних зависимостей)
```shell
pip install -r \path\to\requirements.txt
```

Запуск проверки автотестов:
```shell
pytest -v --tb=line --language=en -m need_review test_product_page.py
```

Если что-то пойдет не так, добавляй time.sleep - тестируемый сервер не стабильный!
![time.sleep(3000)](img/time_sleep_3000.jpg)
