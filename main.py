import pytesseract
from PIL import Image
import re

img = Image.open("Screenshot_1.png")
pytesseract.pytesseract.tesseract_cmd = r'path/to/tesseract.exe' #add your path

file_name = img.filename
file_name = file_name.split(".")[0]

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config, lang='rus+eng')

match = re.search(r'Сумма (\d+,\d+) с\.', text) #regex

# Если найдено, извлекаем сумму
if match:
    amount_str = match.group(1)
    # Преобразуем строку с суммой в числовой формат
    try:
        amount = float(amount_str.replace(",", "."))
        print(f"Извлеченная сумма: {amount} сомони")

        # Сохраняем сумму в файл
        with open(f'{file_name}_amount.txt', 'w') as amount_file:
            amount_file.write(f'Сумма = {amount} сомони')
    except ValueError:
        print("Ошибка преобразования суммы в число")
else:
    print("Строка с суммой не найдена в тексте")

