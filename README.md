
* asm acc neum mc tick struct trap mem cstr prob1 spi

## asm дизайн программирования
* Сами инструкции не отличаются от регистра, за исключением описания символов. Например, LD #1 равно LD #1
* Первая функция — _start, то есть вход.
* Директивы выполняются последовательно. Командная операция определяется следующим образом:

-'ld параметр'-загрузка. Его роль заключается в том, чтобы загрузить данные из памяти в регистр

-'st параметр'-разгрузка. Выгрузить значение из регистра в память

-'add параметр'--добавляет указанное значение в регистр

-'параметр sub '-удалить указанное значение из регистра

-< < Параметр mul > >--умножает регистр на указанное значение

-'параметр div '-деление регистра на указанное

-< < Параметр смп > >--сравнивает значение регистра с указанным значением и устанавливает значение состояния

-'jmp-параметр'-безоговорочно переносится на целевой адрес, указанный в инструкции, и с этого адреса начинается выполнение. Целевой адрес может быть получен либо непосредственно из инструкции, либо из регистра или памяти, заданных в инструкции.

-< < Параметр jz > >--простая условная команда переноса--равный перенос

-'js параметр'-одноусловная команда переноса-результат предыдущей операции отрицательный перенос

-< < Параметр jnz > >--инструкция простого условного переноса--неравный перенос (с JNE)

-`hlt `-- команда держит процессор в подвешенном состоянии

-"push"-вход в стек. Задавить слово данных из регистра, регистра сегмента в стек

-"pop"-выход из стека. Отправка элемента топа стека в определенный регистр

-'параметр call'--вызов программы

-< < ret > >--возвращение

-'inv'--обратная величина числа регистров для получения

* Содержание, появившееся после точки с запятой, будет считаться комментарием

* Поддержка кодирования символов. Символы хранятся в памяти в цифровой форме:

```

'':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 
'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 
 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 
'Y':51, 'Z':52, '':53, '0':54, '1':55, '2':56, '3':57, '4':58, '5':59, '6':60, 
'7':61, '8':62, '9':63, '!':64, ',':65,'.':66, '-':67, '*':68, '?':69, '+':70, 
'/':71, '@':72, '\0':73, '\n':74

```

* Этикетки органов управления:

-'section.data'-метка, обозначающая начало области данных. После этого вы можете объявить переменную, но не написать код.
-'section.text'-метка, обозначающая начало кода

* Функция & метка:

* Функция определяется следующим образом: '<имя функции>''
* Определим метку следующим образом: '.<именная метка>:'
* Функция отличается от метки тем, что метка начинается с ".". Когда мы хотим перейти к определенному тегу, нам нужно использовать его следующим образом: jmp.label_name

* Поиск адреса (формат параметра):

* Чисто числовые: если параметр чисел, то он считается адресом. То есть ld 29 — означает, что значение 30-й ячейки загружается в накопитель
* Просто значение: если параметр имеет "#" и за ним следует число, то этот параметр считается значением. То есть ld #29-это загрузка 29 в батарею
* Переменная: если параметр является переменной, определенной в разделе данных, то в качестве переменной рассматривается адрес.
* Символы: кодируются в цифрах в соответствии с таблицей символов. Например, ld'A' = ld#27

* Определение NZVC:

* N = 1
* Z = 2
* V = 4
* С = 8

* Определение переменных:
* Определяется следующим образом: « <Name:Value>'. Это значение может быть числом или строкой. Если это строка, то у нее будет столько же ячеек, сколько и количество символов.

## память

Команды и память данных.
Память — это список, состоящий из ячеек. Клетки реализуются классом Cell.

* Или число — то есть данные.  Машинная позиция-32 бита. ** В ячейке сохраняется только один символ. В соответствии с таблицей символов, определенной в ИСА, этот символ также имеет числовую форму**
* Или инструкция, представленная как класс — Instruction. ** В объектах класса instruction хранит типы инструкций и параметры**

Дизайн стека.

Последняя **1/4** часть — это порт IO, который используется только для IO.

### командная система

* Машинный бит — 32 бита.
* Регистры:

* IP-счетчик
* коммуникация —
* Регистры
* Заимствовано из стека
* Сохранить результат любой функции
* Сохранение результатов любых математических операций
* BR — служит буфером для временного хранения данных. Например, он используется для хранения результатов функции в инструкции ret.
* AR — указанный адрес ячейки, с которой они взаимодействуют, то есть регистр. Также заявляете? « Адрес » стека.
* PS — условный код.
* SP — указатель стека.

## кодирование команды

Машинный код хранится в формате CSV

Вся программа разделена на 4 части. Различают по указанной метке,

-Первая часть инструкций, перед тегом FUNCTION-набор инструкций. Каждая строка содержания команды разделена на три столбца "":
-Первый столбец-индекс команд
-Второй столбец-команды
-параметры третьей колонки (при наличии)
-Вторая часть-это функции, а то, что после FUNCTION и до LABEL, является выполняемой функцией. Функция содержимого функции разделяет каждую строку на два столбца с ":":
-в первой колонке указаны наименования
-Второй столбец-индекс команд
— Третья часть — это этикетки, то, что было после LABEL и до VARIABLE, — это этикетки. Каждая строка этикетки разделена на три столбца с надписью ":":
-Первый столбец-это имя функции
-вторая колонка-наименование этикетки
-Третий столбец-индекс команд
-Четвертая часть-переменная, то, что следует за тегом VARIABLE, является переменной. Переменные разделены на три столбца ":":
-первый столбец представляет собой название переменной
-вторая колонка-значения
-третья колонка-длина строки (если таковая имеется).

Пример:

```
0 LD'H' 
1 ST OUTPUT 
2 LD'e ' 
 3 ST OUTPUT 
4 LD'l' 
5 ST OUTPUT 
6 LD'l' 
7 ST OUTPUT 
8 LD'o ' 
9 ST OUTPUT 
10 LD',' 
11 ST OUTPUT 
12 LD'w ' 
13 ST OUTPUT 
14 LD'o ' 
15 ST OUTPUT 
16 LD'r ' 
17 ST OUTPUT 
18 LD'l' 
19 ST OUTPUT 
20 LD'd ' 
21 ST OUTPUT 
22 HLT 
FUNCTION
_START: 0
LABEL
_START:. LOOP: 0
VARIABLE

```


## переводчик

Выполнить команду: `translator.py<input_file><target_file>"`'

Подтверждение базовой ошибки:

* Не могут быть определены две переменные с одноименным названием
* Не использовать « Input » или « Output » в качестве названия переменной
* Проверка правильности определения параметров пользователем. Например, можно определить параметры для инструкций без них.
* Проверка формата переменных.
* Информация об ошибке покажет неправильное место.

Функция переводчика:

1.Проверьте некоторые этикетки. данные
2. Чтение переменных и сохранение их в
3. Проверить часть этикеток
   4.Чтение кода
* Если строка является меткой, то она сохраняет свое местоположение, включая ее функциональность и имя на славянском языке label_in_fun.
* Если строка является функцией, то она сохраняет свое место и имя в function_point
* Если строка является инструкцией, то ее местоположение, тип и параметры сохраняются в строке результата
  5.Когда он читает строку, он автоматически игнорирует комментарии
6. Перед любой обработкой 1-4 инструкции преобразуются в прописные буквы.
7. На основе результатов, переменных, label_in_fun и function_point генерируют выводные файлы.

## компьютерное моделирование

Выполнить команду: `machine.py<target_file><inputfile>".`'

Процессор:

* Операция с одним и тем же объектом не выполняется в одной шкале.
* Выполнять операции с различными объектами в течение одного цикла.

## реализация алгоритма:
* prob1: /asm/prob1.asm
* cat:/asm/cat.asm
* hello:/asm/hello.asm

## Ручное испытание:

* Машинное тестирование: test_machine.py
* Тест перевода: test_translator.py

##CI Автотест:
Адрес https://github.com/810q/asm1.git
После отправки кода (ветки master) автоматически запускается детектирование Python application, автоматически выполняется test_machine.py, test_translator.py, детектирование проходит

