# импортировать библиотеку
from translate import Translator
# указать язык 
translator = Translator(to_lang="Russian")
# набрать сообщение
text = input('Введите выражение, которое необходимо перевести:\n')

translation = translator.translate(text)
# вывести перевод сообщения
print(translation)



