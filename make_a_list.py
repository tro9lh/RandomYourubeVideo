from defs import get_random_video_ru, get_random_video, most_popular_video_a_year_ago
import datetime

n = int(input('Введите количество случайных видеозаписей: '))
f = open('text.txt', 'w')
start = datetime.datetime.now()

for i in range(n):
    temp = get_random_video()
    if temp:
        f.write(str(temp)+'\n')


f.close()
stop = datetime.datetime.now()
print('Время выполнения для n записей - ', (stop - start))
"""
n = int(input('введите количество лет: '))
print(most_popular_video_a_year_ago(n))
"""
