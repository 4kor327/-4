import math
mv = 0
amount = 0
# mv = mean value
file = open('text.txt', 'r',  encoding='utf-8')
sum_mv = 0
for line in file:
    c = line.strip()
    wl_str, v_str = c.split('\t')
# wl = длина волны, v = значение энергии
    wl_  = float(wl_str.replace(',', '.'))
    v = float(v_str.replace(',', '.'))
    sum_mv += v
    amount += 1
# x = среднее отклонение, y = среднее квадратическое отклонение
file.close()

file = open('text.txt', 'r',  encoding='utf-8')
x = 0
y = 0
for line in file:
    c = line.strip()
    wl_str, v_str = c.split('\t')
# wl = длина волны, v = значение энергии
    wl  = float(wl_str.replace(',', '.'))
    v = float(v_str.replace(',', '.'))
    x += (v - mv)**2
    y += abs(v - mv)
z = y/amount
b = math.sqrt(x/amount)
print('среднее отклонение:', z)
print('среднеквадратическое отколнение:', b)
file.close()


