Шаги для запуска из консоли:
1. Зайти в виртуальное окружение:
```
source venv/bin/activate
```
2. Запустить скрипт с флагом ELLIPSIS:
```
python -m doctest -v -o ELLIPSIS issue1/dockstring_morse_encode.py
```
Результат: 4 из 5 тестов прошли
5-й тест не прошел из-за отсутствия запятой в словаре
