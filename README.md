# Task-6-25

  Требуется написать функцию, получающую в качестве параметров имя массива и его длину (**n**). Заполнение массива числами
 из файла и определение его фактической длины должно выполняться отдельной подпрограммой. Функция `main` открывает файл,
 вызывает функцию, заполняющую массив числами из файла, обращается к функции печати массива на экран, вызывает функцию,
 преобразующую массив (или вычисляющую его характеристику) и выводит результат (или преобразованный массив) на экран.
 
### Функция преобразования должна удалить из массива учвстки строгого возрастания с длиной не более 3 (расматриваются участки, которые нельзя расширить, т.е. максимальные по включению). Функция должна возвращать количество элементов в получившемся массиве. 
> Так, массив (1 0 2 3 1 -1 -1 2 3 0 0 0 1 2 3 4) должен быть преобразован в (1 1 -1 0 0 0 1 2 3 4). Использовать не более чем **n** перемещений элементов.
  
  
  Память под хранение массива должна выделяться динамически, количество чисел в файле заранее неизвестно. Файл нельзя открывать более одного раза, нельзя возвращаться к началу файла.
 Использовать дополнительные массивы нельзя. Ошибки обработать.
