Шаги для запуска из консоли:
1. Зайти в виртуальное окружение:
```
source ../venv/bin/activate
```
2. Запустить скрипт
```
python -m pytest issue5/test_year.py
```
Для генерации html-отчёта по тесту введите:
```
python -m pytest issue5/test_year.py --cov=what_is_year_now --cov-report html
```
html-отчёт хранится в папке htmlcov/
