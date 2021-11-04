# Новое русское вино

Сайт магазина авторского вина "Новое русское вино". Обладает огромным ассортиментов великолепного вина и коньяка и крутым сайтом, использующим современные технологии.

## Запуск

Для того, чтобы запустить сайт нужно выполнить несколько пунктов:

- Скачайте код
- Запустите сайт командой ```python3 main.py```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Наполнение сайта товаром
Программа принимает на вход excel файл в формате `.xlsx`. Шаблон файла `wine.xlsx` находится в репозитории.
В качестве данных передается таблица с указанием категории вина, его названия, сорта, цены, а так же - картинка, которая в итоге отображается на сайте.
В файле можно указать относится ли какой-либо товар к акционным продуктам. Для этого необходимо в столбце акция указать "Выгодное предложение".

Ниже пример заполнения файла:
Категория | Название | Сорт | Цена | Картинка | Акция
----------|----------|------|------|----------|------
Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
Напитки | Коньяк классический | | 350 | konyak_klassicheskyi.png | 
Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png | 
Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png | 
Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png | 

По-умолчанию программа "ищет" файл в той же самой папке, где находится скрипт `main.py`. В случае если файл с товарами находится в какой-либо другой папке, то необходимо немного модифицировать код запуска:
```
python main.py --path_to_file D:\delivery_wine_01112021\
```
Для того, чтобы программа принимала другое название файла вместо `wine.xlsx`, то при запуске нужно указать следующие параметры:
```
python main.py --file_name new-name.xlsx
```
Ну а если очень хочется сделать сразу и то и другое, то выполните следующую команду:
```
python main.py --path_to_file D:\delivery_wine_01112021\ --file_name new-name.xlsx
```

Программа поддерживает и более короткий синтаксис, поэтому пример ниже будет аналогичен тому, что мы разобрали в предыдущем примере:
```
python main.py -ptf D:\delivery_wine_01112021\ -f new-name.xlsx
```
Для того, чтобы вызвать справку по программе нужно указать параметр `-h` или `--help`:
```
python main.py --help
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
