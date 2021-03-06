import pytest
import morse


@pytest.mark.parametrize('s,exp', [
    ('-....-', '-'),                                                        # Тест на -
    ('.-.-.-', '.'),                                                        # Тест на .
    ('. .', 'EE'),                                                          # Тест на два одинаковых символа
    ('.... .....', 'H5'),                                                   # Тест на расшифровку похожих символов
    (' ', ' '),                                                             # Ошибка - при decode все пробелы удаляются
    ('--..--', ','),                                                        # Ошибка - закодирована запятая с пробелом
    ('.... .. --..--   -.. . ...- . .-.. --- .--. . .-.', 'HI, DEVELOPER'),
])
def test_decode(s, exp):
    mes = morse.decode(s)
    assert exp == mes

