# Set, Strings, Decorators, List Comprehentions, Functions

# Set

# Сет це ще одна множинність, яка зберігає унікальне значення. Тобто, там не може бути повторень
# Тобто сети нам потрібні для того щоб уникнути дублікти і залишити лиш унікальні значення

list = [1,2,1,2,3]

# Цей список, ми можемо конвертнути в set

set_one = set(list)
print(set_one)

# Вивід буде: {1,2,3}. Ми получаємо лише унікалні значення

# Щоб створити нам новий set, якщо ми зразу його заповнюємо, ми відкриваємо фігурні дужки, так само як і при створенні словника,
# але зразу вписуємо значення. Можемо ми і вписувати дублікати, вони збергіатися там не будуть

set1 = {1,3,5,4,3,5,7}
print(set1)

# Якщо ми вкажемо просто пустий set, і обернемо ми це у type, то нам вернеться dict.
# Таким чином, ми можемо створити пустий словник, але не set

set1 = {}
print(type(set1))

# Вивід буде: <class 'dict'>
# Якщо все таки нам потрібен пустий set, ми використовуємо функцію set()

set2 = set()
print(type(set2))

# Вивід буде: <class 'set'>
# Щоб наш сет, є певна кількість методів для set. Щоб добавити щось у нас set, існує метод add

set2.add(1)
set2.add(1)
set2.add(2)
set2.add(3)
print(set2)

# Вивід буде {1, 2, 3} Не забуваємо, що тут ми получаємо унікальні значення, тобто без повторень

# Є такий метод, як issuperset

set_full = {1,2,3,5}
set_new_full = {2,3}
print(set_full.issuperset(set_new_full))

# Тут ми зрівнюємо ці методи. Ми питаємо, чи являється один set super-сетом для іншого.
# Тобто, є ж в другому те все саме, що і в першому. Вертається нам False або True.

# Протилежним для нього буде метод issubset. Чи являється set частиною іншого set-а

print(set_full.issubset(set_new_full))

# Якщо ми перевірятимемо, від другого перевіряли перший, нам вернеться True

print(set_new_full.issubset(set_full))

# Є такий метод, як isdisjoint. Він вертає True, якщо ці на сети не мають спільних елементів
# В нашому випадку вернеться False, тому що вони мають спільні елементи: 2 і 3

print(set_full.isdisjoint(set_new_full))

# Якщо вони повністю різні, получаємо True

set_join = {1, 3, 5}
join_set = {11, 33, 55}
print(set_join.isdisjoint(join_set))

# Метод union дозволяє нам об`єднювати сети
# На виході ми получаємо новий сет, який складається із двох цих сетів

print(set_join.union(join_set))

# Вивід буде: {1, 33, 3, 5, 55, 11}

# Метод intersection буде вертати сети спільних елементів цих двух сетів

inter_set = {1, 9, 11}
set_inter = {11, 9, 17}

print(inter_set.intersection(set_inter))

# Вивід буде: {9, 11}. Ми получаємо елементи, які присутні там і там

# Метод difference буде вертати те, чого не буде в другому сеті

print(inter_set.difference(set_inter))

# Вивід буде: {1}. Тому що в сеті set_inter нема 1. Все решта там присутнє

# Метод symmetric_difference буде дивитися на те, чого нема в одному сеті, по відношеню до другого і
# по-відношенню від другого в першому. Тобто видає, чого нема в другому і того, чого нема в першому.
# Тобто, по відношенню один з одним

print(set_inter.symmetric_difference(inter_set))

# Вивід буде {1, 17}. Тобто, в сеті set_inter нема 1, в сеті inter_set нема 17

# Ми можемо обновляти один сет іншим. Для цього слугує метод update

set_inter.update(inter_set)
print(set_inter)

# Вивід буде {17, 1, 9, 11}. В цьому випадку, у нас міняється set_inter. Не забуваємо про унікальні значення

# Метод remove дозволяє нам видалити щось по-значенню. Зараз у нас видалиться 17

set_inter.remove(17)
print(set_inter)

# Якщо ми попробуємо видалити того, чого не існує, то получимо помилку

# За допомогою метода pop, ми можемо видалити, випадковий елемент. Тут, в сетах індексів нема. В сетах,
# довільний порядок. Тут нема індексів і ми не можемо звернутися до конкретного індекса до сета.
# Видалений елемент запишеться нам у змінну deleted_pop

deleted_pop = set_inter.pop()
print(deleted_pop)
print(set_inter)



# String

# Стрічки, в будь якій мові програмування, відіграють величезну роль, тому що багато чого у нас є зв`язано з стрічками

string = 'Hello'
string1 = "World"

# Бувають такі випадки, коли нам треба вставити подвійні лапки у подвійних лапках. Нам тоді треба екранувати їх

string2 = " Hello \" World"
print(string2)

# Вивід буде: Hello " World. Це так само відноситься до одинарних, коли треба записати в одинарних

# Конкатинація

name = "Dmytrii"
age = 21
weight = 70.5

# string = 'Hello, my name is' + name + 'I am' + age + 'and my weight' + weight + 'kg'

# В даному випадку, у нас буде помилка. В python недопустимо до string добавляти int значення.
# Нам це потрібно конвертувати значення int в string

string1 = 'Hello, my name is ' + name + 'I am ' + str(age) + ' and my weight ' + str(weight) + 'kg'
print(string1)

# Зараз це все працюватиме, але зе не є зручно

# Є другий варіант. Там де нам потрібно вставити стрічку, ми вказуємо %s, там де потрібно вставити число ставимо %d (digit)
# і аналогічно для числа з плаваючою точкою %f (float) В кінці ставимо знак відсотка і в кортежі прописуємо змінні, в якому
# порядку вони будуть йти

string2 = 'Hello, my name %s is. I am %d and my weight %f kg' %(name, age, weight)
print(string2)

# Цей варіант був один із найперших в python і також він є незручним.
# Є ще третій варіант У строки є метод format. Замість знаків відсотка, ми просто пишемо
# фігурні дужки і у методі format ми вказуємо по черзі змінні, які у нас будуть йти

string3 = 'Hello, my name is {} I am {} and my weight is {}'.format(name, age, weight)
print(string3)

# Є четвертий, похожий приклад.

string4 = 'Hello, my name is {name} I am {age} and my weight is {weight}'.format(name=name, age=age, weight = weight)
print(string4)

# Останній варіант є найкращим. Ми просто залишаємо фігурні дужки для змінних, видаляємо метод format і перед стрічкою
# ставимо англійську букву f. Це як ${} (template string) в js

string5 = f'Hello, my name is {name} I am {age} and my weight is {weight}'
print(string5)

# Ми у методі format можемо вставити і інші

string6 = 'Hello, my name is {}, i am {} and my weight is {}'.format('Ronnie', 45, 71)
print(string6)

# Методи стрічок

# Знайти індекс де знаходиться певна буква

print('hello world'.index('w'))

# Літера w знаходиться у нас під шостим індексом, тому і вивід буде 6. Якщо

# Ми можемо шукати і цілий фрагмент, частину слова, але вернеться нам індекс першої букви. Вивід буде 2

print('hello world'.index('llo'))

# Ми можемо вказати індекс, з якого по-який будемо шукати. Якщо нічого не знайде, то падає exception

print('hello world'.index('llo',2))

# За допомогою метода count ми можемо порахувати певну кількість символів. Наприклад, ми рахуємо скільки у нас є
# букв l. Ми отримаємо у відповідь 3

print('hello world'.count('l'))

# Метод capitlize допомагає нам зробити першу букву стрічки у верхньому регістрі

print('hello world'.capitalize())

# Щоб зробити всі букви великі для цього слугує метод upper

print('hello world'.upper())

# Протилежний до методу upper є метод lower (всі букви у малому регістрі)

print('HELLO world'.lower())

# Якщо нам треба щось перевірити, всі методи починаються із префікса is
# Метод isupper дозволяє нам перевірити, чи вся стрічка у нас з великих літер. Вертає boolean тип

print('Hello world'.isupper())

# Протилежний до методу isupper є метод islower (чи всі букви з маленької літери). Вертає boolean тип

print('hello world'.islower())

# Метод isalpha вертає нам boolean тип, перевіряючи чи складається наша стрічка лише із букв

print('hello world'.isalpha())

# Можемо перевірити чи починається наша стрічка з певної літери. Для цього слугує метод startswith. Вертає boolean тип

print('hello world'.startswith('a'))

# Так само ми можемо перевірити чи закінчується наша стрічка на певну літеру. Для цього слугує метод endwith. Вертає boolean тип

print('hello world'.endswith('world'))

# Іноді буває, що у нас праворуч і ліворуч залишаються пробіли. Щоб їх забрати, з обох боків, існує метод strip

print(['   hello world  '.strip()])
print('  hello world  '.strip())

# Так само ми можемо говорити, по якому критерію забирати пробіли. Наприклад, ми хочемо забрати по a

print(['aa   hello world aaa'.strip('a')])
print('aa   hello world aaa'.strip('a'))

# З обох боків, пробіли залишаться, але a пропадуть

# Існують методи rstrip та lstrip. Вони допомагають забрати пробіли з правої чи лівої сторони або по-якісь іншій умові

print(['aa   hello world aaa'.rstrip()])
print('aa   hello world aaa'.rstrip())
print(['aa   hello world aaa'.lstrip()])
print('aa   hello world aaa'.lstrip())

# Метод split дозволяє нам розбити стрічку

print('1234'.split(','))

# Метод partition працює майже так само, як split, але ділить стрічку на 3 частини і вертає нам кортеж
# В нашому варіанта, нашим сепаратором буде name i вивід буде: ('', 'name', ' is name')
# Сепаратор являється завжди середнім елементом.

print('name is name'.partition('name'))

# Якщо сепаратор не знайдений, вернеться третій кортеж, який вміщує 2 пусті стрічки, за
# якими йде і сама стрічка. Вивід буде: ('hello world', '', '')

print('hello world'.partition('2'))

# Ми можемо join(ити) певний масив

l = ['1', '2', '3']
string_of_list = ''.join(l)
print(string_of_list)

# Метод isspace вертає тип boolean і перевіряє чи є пробіли. Пуста стрічка буде false

print(''.isspace())

print(min(1, 2, 6, 8, -15, -15.1))
print(max(1, 2, 6, 8, -15, -15.1))

# Ми можемо передавати зразу і список

print(max([1, 2, 6, 8, -15, -15.1]))

# Сортування вже йде самого списку

print(sorted([1, 2, 6, 8, -15, -15.1], reverse=True))

# Підведення в степінь: pow() or **

print(pow(25, 14))
print(25 ** 14)




# List Comprehensions

# List Comprehensions використовується для створення нових списків з інших ітеративних елементів,
# таких як кортежи, рядки, масиви, списки тощо. Це простий і компактний синтаксис для створення
# списку з рядка або іншого списку.

# Ми можемо генерувати наш список з циклом, який знаходиться в самому тому списку

one_list = [i for i in range(5)]
print(one_list)

# Вивід буде: [0, 1, 2, 3, 4]

# Ми можемо що завгодно ітерувати і записувати що завгодно. List Comprehensions не тільки для
# списків. Він так само заміняє filter і map як в js, але в python інші методи. Ось приклад:

# Наприклад, нам потрібно генерувати числа з 0 до 4, але ми хочемо записувти лише парні числа
# Ми просто після цикла запишемо умову

s = [item for item in range(5) if item % 2 == 0]
print(s)

# Вивід буде: [0, 2, 4]

# Ми можемо і добавляти значення. Типу, що кожне окреме число при діленні на 2 буде 0 і
# до того значення добавляти певне значення

s_n = [one+20 for one in range(5) if one % 2 == 0]
print(s_n)

# Вивід буде: [20, 22, 24]

# Ми можемо використовувати і подвійні цикли

ist1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
my_result = [i for j in ist1 for i in j]
print(my_result)

# Вивід буде: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_result = [i for j in ist1 for i in j] запис однакова до:

# for j in ist1:
#     for i in j:
#         my_result.append(i)
# print(my_result);

# Ми можемо робити List Comprehensions із словників
# Наприклад, у нашому словнику погано написані ключі, нам треба повернути це
# до нижнього регістру
#
# Ми говоримо, що ключ буде рівний малому регістру із значення і звичайним циклом ітеруємо ключ/значення
# з нашого словника з його вмісту і в результаті получаємо нормальний об`єкт

dict_compr = {'name': 'max', 'aGe': 13}
res_compr = {k.lower():v for k,v in dict_compr.items()}
print(res_compr)





# Functions

# Функції у python прописуються через ключове слово def (defined), дальше йде назва функції. Можуть бути присутні атрибути

def func():
    print('hello')


func() # Виклик функції

# У JS у нас працювало у функціях hosting, коли вони вспливали наверх. В python такого нема,
# виклик функції треба писати після самої функції

# Функції можуть бути з параметрами


def func2(a,b,c):
    print(a,b,c)


func2(1,2,3)

# Після функції прийнято добавляти 2 пробіли і перед нею також
# Ми можемо і добавляти значення по-замовчуваню


def func3(a,b,c = 3):
    print(a,b,c)


func3(1,2)

# Ми можемо трійку і не записувати, нам вона і так виведеться. Якщо у виклиці функції, записати на місці трійки
# якесь інше число, то воно зміниться на нове

# Ми можемо в якості параметрів добавити наступне:

def func4(a,b,c, *args):
    print(a,b,c,args)


func4(1,2,3,64,74,75)

# Вивід буде: 1 2 3 (64, 74, 75)
# args - це довільна назва, головне перед назвою поставити знак зірочки. Це означатиме, що після третього елемента,
# всі наступні будуть записуватися в кортеж. Це похоже, як arguments в js.

# Є ще така річ, як **kwargs - іменовані значення


def func5(a,b,c, **kwargs):
    print(a,b,c, kwargs)


func5(5, 11, 19, name = 'Dmytrii', status = True)

# Вивід буде: 5 11 19 {'name': 'Dmytrii', 'status': True}.
# Як бачимо, получаємо у відповідь ключ/значення

# Ми можемо за допомогою цих подвійних зірочок розпакувати словник


def func6 (a,b,c, *args, **kwargs):
    print(a,b,c, args, kwargs)
def_dict = {'name': 'Dmytrii'}


func6(1,2,3,6,75,94, **def_dict)

# Вивід буде: 1 2 3 (6, 75, 94) {'name': 'Dmytrii'}


# Такий же варіант із списком. В цьому випадку, *l - аналог ...l (spread оператору) в js


def func7(a,b,c):
    print(a,b,c)
l = [5,6,7]


func7(*l)

# Вивід буде: 5,6,7

# Так само, в функція в python існує return


def func8(a, b, c):
    print(a, b, c)
    return a
l = [5,6,7]
a = func8(*l)
print(a)

# Вивід буде 5



# Декоратори

# Нам треба декорувати функцію func9. Наприклад, функція func9 нам виводить hello i нам треба обгорнути це слово. Типу
# print('***')
# print('Hello')
# print('***')
# Писати так у кожній функції це не продуктивно, нам треба щось універсальне. Для цього і є декоратори

# Декоратор являється собою функцією (decor, у нашому випадку). Він у себе буде приймати якусь f функцію. Всередині цієї
# функції буде ще одна функція inner, яка в себе приймає args і kwargs (args і kwargs заміняють будь-які вписані значення,
# в тому числі словники, прості якісь параметри. По-суті, 2 поля все заміняють).
# Дальше ми пишемо в що будемо обгортати (зірочки) і між ними ми викликаємо функцію, яку будемо передавати в цей
# print(декоратор). Ми її викликаємо, в неї передаємо наші args і kwargs. args і kwargs потрібні для того щоб, якшо у нашій
# функції func9 треба буде передавати якісь парамтери, вони прийдуть сюди: def inner(*args, **kwargs) і перейдуть саме сюди:
# f(*args, **kwargs)
#
# Щоб з`єнати нам це разом: над нашою функцією func9, яку хочемо декорувати, ставимо просто собачку і назву функції
# декоратора і викликаємо нашу функцію. Наш декоратор має повертати нашу внутрішню функцію: return inner. Без її виклику,
# просто функцію

def decor(f):
    def inner(*args, **kwargs):
        print('***')
        f(*args, **kwargs)
        print('***')
    return inner

@decor
def func9():
    print('Hello')
func9()

# Вивід буде: ***
#             Hello
#             ***

# Цей декоратор можна використовувати на будь якій функції

@decor
def func10(name):
    print(f'Hello {name}')
func10('Dmytrii')

# Вивід буде: ***
#             Dmytrii
#             ***

# Ми можемо ставити декоратор над декоратором

@decor
@decor
def func11(name):
    print(f'Hello {name}')
func11('Dmytrii')

# Вивід буде: ***
#             ***
#             Dmytrii
#             ***
#             ***