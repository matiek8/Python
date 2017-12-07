"""
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробеловили символами конца строки. Определите, сколько различных слов содержится в этом тексте.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.


Вывод программы:
19
"""

import sys
import re

print(len(set(re.findall('[^ \n]+', sys.stdin.read()))))