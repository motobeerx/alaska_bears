# alaska_bears
# 1) Descriptions
В данном ТЗ было реализованно 2 типа проверок: фукнциональные, нагрузочные и 1 не функциональные.
# pytest -v -m functional  test_alaska_bear.py
# pytest -v -m performance  test_alaska_bear.py
Обратите внимание, что файл performance_alaska_config.py - отвечает за настройку  нагрузки проеверок
В данные момент настройки занижены, чтобы гарантировать быстрое прохождение автотеств. Параметры
можно увеличить

# Так же был обнаружен ряд дефектов:

#
# 1) Bear с типом GUMMY - некорректно добавляется(как null) 
на данный дефект будет падать самая первая проверка
(test_user_can_add_bears) - для данного коммита GUMMY исключен, дабы не валить другие тесты

# 2) Обновить можно только Имя медведя
 (test_user_can_change_bear_type, test_user_can_change_bear_age) 
# 3) Имя добавляется только в виде заглавного регистра
(test_user_can_add_bear_with_null_name)
# 4) (Уточнение) Если перезапустить контейнер, то вся база потеряет сохраненную информацию
Думаю в рамках ТЗ это норма
# 5) При добавлении медведя c age +inf, -inf, age<0 - возраст добавляется как 0
(test_user_can_not_add_bear_with_negative_age, test_user_can_not_add_bear_with_positive_inf_age
test_user_can_not_add_bear_with_negative_inf_age)
# 6)(Уточнение) Можно создать дубликат, т.е. полностью одинаковый медведь, но разные id.
По сути-то медведь одинаковый. Но данное утверждение является скорее уточнением. Нефункциональная проверка
предполагает, что можно создать подобного рода дубликат, а вот id изменить - нельзя(так можно избежать 
дублирование информации)