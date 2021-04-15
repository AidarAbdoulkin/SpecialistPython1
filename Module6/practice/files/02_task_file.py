# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

f = open("data/sold.txt", "r")
chks = []
for line in f:
    chks += line.rstrip().split(" ")
f.close()

for index, item in enumerate(chks):
    chks[index] = float(item)

print("sum:", sum(chks))
print("max:", max(chks))
print("min", min(chks))
