Вы кладоискатель и Вам необходимо проникнуть в старый замок, окруженный со всем сторон стенами. У вас есть некоторое кол-во взрывчатки (даже не буду спрашивать, откуда она у вас), однако ее запаса не хватит, чтобы взорвать стену в любом месте. Необходимо найти самое уязвимое место в стене.
В качестве входных данных вы получите многострочную строку, состоящую из '0' и '#' - вид стены сверху. '#' будут показывать каменную часть стены замка, а '0' - пустоты. Относительное расположение вас и стены следующее: вы смотрите на массив с нижней его части.
Ваша задача - найти координаты места, где стена наиболее узкая (как показано на рисунке ниже). Ширина стены - это высота столбцов массива (многострочной строки). Если таких мест несколько - выберите самое левое из них и верните его индекс по-горизонтали (самый левый столбец имеет индекс 0).

Входные данные: многострочная строка, схематически отображающая каменную стену.

Выходные данные: индекс наиболее уязвимого места стены.

Пример:
stone_wall('''
##########
####0##0##
00##0###00
''') == 4

Как это используется: Для архитектурного анализа.

Предусловия :
3x3 <= размер строки <= 10x10