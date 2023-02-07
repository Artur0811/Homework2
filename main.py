import time
import sqlite3 as sql
def op_m(a, b):
    if sorted(a[0]) == sorted(b[0]):
        if a[1] < b[1]:
            return [a, []]
        else:
            return [b, []]
    return [a, b]

def o_gr(graf, max_t, x,  t_n= 0, past = [], ob_p = []):#сам граф - graf\ лимит по времени - max_t\ начало графа - x
    #время на путь - t_n \пройденый путь на данный момент - past\ обязательные точки - ob_p
    if t_n > max_t or len(past) == 26:#если привышен лимит времени и есть 26 точек маршрута (25 - максимальное кол- во точек, которое можно добавить в яндексе)
        b = graf[past[-2]]#значит заканчиваем
        for i in range(len(b)):
            if b[i][0] == past[-1]:# этот цикл для коректировки времени маршрута. последняя точка не должна учитоваться
                return [[past[:-1], t_n- b[i][1]]]
    if past == [] and ob_p == []:# нет обязательных точек и начала маршрута
        roud = []
        v = graf[x]#точки куда могу пойти
        past.append(x)# начальная точка
        for i in range(len(v)):
            if t_n + v[i][1] <= max_t:#перебираю точки в которые могу пойти
                a = o_gr(graf, max_t, x, t_n+v[i][1], past+[v[i][0]], ob_p)#поучаю маршрут
                roud += [*a]
        ma_l = max(list(map(lambda x:len(x[0]), roud)))
        rez = []
        while ma_l > 0:
            a = list(filter(lambda x: len(x[0]) == ma_l, roud))
            ma_l-=1
            if len(rez) + len(a) > 5:
                rez += a
                return rez[:5]
            else:
                rez +=a
        return rez[:5]#возвращаю маршруты
    elif past == [] and ob_p != []:#есть обязательные точки, но нет начала
        past.append(x)#начало маршрута
        t_p = 0#предпологаемое время маршрута через обязательные точки
        while len(ob_p)+1 != len(past):#тут типо делаю маршрут из обязательных точек,  но самый короткий по времени
            v = graf[past[-1]]#предыдущая точка
            mi = ["", 1000]#ближайшая следующая
            for i in range(len(v)):#ищу ближайшую обязательную  точку
                if mi[1] > v[i][1] and v[i][0] not in past and v[i][0] in ob_p:
                    mi[1] = v[i][1]
                    mi[0] = v[i][0]
            t_p += mi[1]#добавляю время до ближайщей точки
            past.append(mi[0])#добавляю ближайшуюточку
        if t_p > max_t:
            return [[]]
        pu =[]
        pu.append([past, t_p])# путь только через обязательные точки
        pu+=o_gr(graf,max_t, x, t_p,past,ob_p)#остальные маршруты
        for i in range(len(pu)):#убираю повторы
            for y in range(i+1, len(pu)):#и если у 2х маршрутов одинаковые точки
                if pu[i] != [] and pu[y] != []:# то оставляю тот, который меньше по времени
                    if len(pu[i][0]) == len(pu[y][0]):
                        c = op_m(pu[i], pu[y])
                        pu[i] = c[0]
                        pu[y] = c[1]
        pu = list(filter(lambda x: x!= [], pu))#удаляю пустые списки
        rez = []
        ma_l = max(list(map(lambda x: len(x[0]), pu)))#максимальная длина
        while ma_l>0 and len(rez)<5:#ищу маршруты
            a= sorted(filter(lambda x:len(x[0]) == ma_l, pu), key=lambda x:x[1])#самые длинные
            if len(rez) + len(a) > 5:#если их больше 5 вывожу
                rez+=a
                return rez[:5]
            else:
                if a != []:#есть маршруты
                    rez += a
            ma_l-=1
        return rez[:5]#вывод

    else:
        if ob_p == []:#не обязательных точек
            mi = ["", 1000]#ближайшая точ
            b = graf[past[-1]]#куда могу пойти
            for i in range(len(b)):#ищу ближайшую точку
                if mi[1] > b[i][1] and b[i][0] not in past:
                    mi[1] = b[i][1]
                    mi[0] = b[i][0]
            if mi[1] == 1000:#на всякий
                return [[past, t_n]]
            return o_gr(graf, max_t, x, t_n+mi[1], past+[mi[0]], ob_p)#добавляю бижайшую точку и иду дальше
        else:#есть обязательные точки
            pu = []
            if len(past) == 25:
                return [[past, t_n]]
            mi = ["", 10000, 0]#ищу точку кторая увеличит время меньше всего
            for i in range(1, len(past)):#рассматриваю разные звенья пути(А, Б)
                g = graf[past[i-1]]
                t = 0
                for y in range(len(g)):#нахожу время до следующей точки
                    if g[y][0] == past[i]:
                        t = g[y][1]
                for y in range(len(g)):#смотрю куда можно пойти
                    if g[y][0] not in past:#новая точка(точка В)(предпологаемый маршрут АВБ)
                        d_t = g[y][1]
                        pr = graf[g[y][0]]
                        for j in pr:#следующая точка в звене (из А в В и из В в Б)
                            if j[0] == past[i]:
                                d_t += j[1]
                                break
                        if mi[1] > d_t-t:#сохраняю точку, которая изменяет время меньше всего
                            mi[0] = g[y][0]
                            mi[1] = d_t-t
                            mi[2] = i
            if max_t >= t_n + mi[1] and mi[1] != 10000:#не превзашол лимит по времени
                pu.append([past[:mi[2]] + [mi[0]] + past[mi[2]:], t_n + mi[1]])#сохраняю маршрут
                pu += o_gr(graf, max_t, x, t_n + mi[1], past[:mi[2]] + [mi[0]] + past[mi[2]:], ob_p)#проверяю могу ли добавить еще точки
                pu += o_gr(graf, max_t, x, t_n + mi[1], past[:mi[2]] + [mi[0]] + past[mi[2]:])#маршрут за самую крайнюю обязательную точку
            return pu#вывод

s = {}
con = sql.connect("C:/Users/Admin/PycharmProjects/pythonProject20/sayt/db.sqlite3")#подключаюсь к базе данных
cur = con.cursor()#ну это наверное нужно
cur.execute('SELECT point1, point2 FROM route')#таблица routeолучаю из нее значения точки(point1) и куда можно пойти(point2)
for i in cur:#проход по данным
    po = i[0]#точка
    zn = i[1].split(";")#пути хранятся как строка 1 значение - точка 2- время ;- разделитель
    mas = []
    for i in range(len(zn)):
        if ',' in zn[i]:
            mas.append([zn[i], int(zn[i+1])])#добавляю точку и время
    s[po] = mas#сохраняю куда можно пойти из точки
cur.close()
con.close()#отключаю подключение

tn = time.time()
a = o_gr(s, 15, "55.826591, 37.638033", ob_p=['55.830932, 37.632602'])
print(time.time()-tn)
for i in a:
    print(a)