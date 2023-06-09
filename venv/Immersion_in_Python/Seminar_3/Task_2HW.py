# ✔ В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать
# знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
import re

paper: str = "«Дневной Дозор» — роман российского писателя фантаста Сергея Лукьяненко в соавторстве с Владимиром \
Васильевым, второй из серии произведений, рассказывающих о вымышленном мире Иных. Роман был написан с июня по октябрь \
1999 года и впервые опубликован издательством «АСТ» в 2000 году. Состоит из трёх частей — «Посторонним вход \
разрешён» Сергея Лукьяненко, «Чужой для иных» Владимира Васильева и совместной повести «Иная Сила». Вместе с романами \
«Ночной Дозор», «Сумеречный Дозор», «Последний Дозор», «Новый Дозор», «Шестой Дозор», а также несколькими рассказами \
Лукьяненко и рядом произведений других авторов входит в цикл «Дозоры». \
Действие романа происходит в современных на момент написания Москве, Крыму, Праге. Помимо привычного мира людей, \
существует мир Иных, к которым относятся маги, волшебники, оборотни, вампиры, ведьмы, ведьмаки и прочие произошедшие \
от людей, но не относящие себя к ним существа. Иные делятся на Светлых и Тёмных. Добро больше не вступает в активное \
противоборство со Злом, а находится с ним в динамическом равновесии. Для соблюдения баланса Света и Тьмы любое доброе \
магическое воздействие должно уравновешиваться злым. За соблюдением этого порядка следят специально созданные \
организации Иных — Дозоры. Интересы Светлых представляет Ночной Дозор, интересы Тёмных — Дневной Дозор. \
В первой части романа в результате стычки Дозоров ведьма Алиса Донникова из Дневного Дозора и светлый маг \
Игорь из Ночного временно теряют большую часть своей силы и отправляются восстанавливать её в пионерский лагерь \
«Артек», не зная друг о друге. Не в состоянии распознать Иного, Алиса влюбляется в Игоря, что приводит к поединку \
и её гибели. Во второй части на пути Ночного Дозора возникает «Зеркало» — Виталий Рогоза — порождение Сумрака, \
призванное восстановить баланс сил. Одновременно секта Тёмных планирует возродить могущественного древнего мага. \
В третьей части рассказывается о судебном процессе Инквизиции — организации, призванной контролировать Дозоры. \
Выясняется, что события первых двух частей были не случайны, а спланированы или использованы руководителями Дозоров \
Москвы. В 2000 году на Харьковском международном фестивале фантастики «Звёздный Мост» роман занял первое место в \
номинации «Лучший цикл, сериал и роман с продолжением»; в 2001 году был удостоен премии «Золотой РОСКОН» на конференции \
писателей, работающих в жанре фантастики, «РосКон»."


def get_type_dict(text: str):
    text = re.sub(r'[^а-яА-Я ]+', '', paper).lower()
    list_word = list(set(text.split()))
    result = {}
    for i in list_word:
        if len(i) > 2:
            result.setdefault(i, text.count(i))
    print(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])


get_type_dict(paper)
