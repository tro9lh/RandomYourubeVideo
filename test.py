import datetime

start = datetime.datetime.now()
def rec(a,b):
    if b == 0:
        return 1
    else:
        return a * rec(a, b-1)

a, b = 9999, 800
print(rec(a,b))
stop = datetime.datetime.now()
print('Время выполнения для n записей - ', (stop - start))
start1 = datetime.datetime.now()
print(a**b)
stop2 = datetime.datetime.now()
print('Время выполнения для n записей - ', (stop2 - start1))


<input type="button" class="btn btn-primary" value="Refresh Page" onClick="window.location.reload()">

<img src="PixelArt.png" alt="NEXT" onClick="window.location.reload()">
