from contentUnit import ContentUnit
from state import State

states: State = {}

def restart_button(player, message):
    player.friendship = False
    player.meeting = False

# I_a_00_00 Start Point

content = [ContentUnit("text",
                       "Поздравляю, ты получил грант в Иннополисе! Ты стоишь на пороге новой, полной приключений, студенческой жизни"),
           ContentUnit("text",
                       "Твоя история начинается здесь – в Казани, большом соседе пока ещё маленького, но возлагающего большие надежды инногорода.")
           ]
buttons = {"дальше": "I_a_01_00"}
states["I_a_00_00"] = State(content, buttons, "I_a_01_00", callback=restart_button)

# I_a_01_00  Start Point 1
content = [ContentUnit("text",
                       "Ты приближаешься к остановке «Комбинат здоровье». Прогнозы погоды не соврали, день сегодня выдался жаркий."),
           ContentUnit("photo", "http://sportgyms.ru/uploads/posts/2014-10/1413369414_01.jpg"),
           ContentUnit("text",
                       "Усталость тебя не расстраивает. Ты почти на месте. Грёзы о будущем прерывает навязчивое чувство жажды, но не хочется останавливаться.")
           ]
buttons = {"дальше": "I_a_02_00"}
states["I_a_01_00"] = State(content, buttons, "I_a_02_00")

# I_a_02_00 First Choice. Water or Look around
content = [ContentUnit("text",
                       "И вот ты на месте. Группы людей уже активно общаются. Похоже, твоего появления никто даже не заметил."),
           ContentUnit("text", "Поставив тяжёлые сумки на асфальт, ты решаешь.")
           ]
buttons = {"оглянуться кругом": "I_a_03_00",
           "выпить воды": "I_a_03_01"}
states["I_a_02_00"] = State(content, buttons, "I_a_03_00")

# I_a_03_00
content = [
    ContentUnit("text", "Интересно, что там делают ребята? Приближаясь к группе, ты начинаешь улавливать фразы:"),
    ContentUnit("text", "- Бурнашев Илья!"
                        "- Есть!"),
    ContentUnit("text", "- Наумова Дарья!"
                        "- Есть!"),
    ContentUnit("text", "- Цыдан… Цендендам…"),
    ContentUnit("text",
                "«Цыдендамбаев Иван – здесь! Из Монголии я», - выдал кто-то из толпы, с трудом сдерживая смех.")]
buttons = {"дальше": "I_a_04_02"}
states["I_a_03_00"] = State(content, buttons, "I_a_04_02")

# I_a_03_01
content = [
    ContentUnit("text",
                "Да, как же хочется пить… Хорошо, что с собой есть немного воды. До тебя доносятся звуки имён, фамилии и смех ребят.",
                delay=0),
    ContentUnit("text", "Оказывается, автобус приедет через 30 минут. Ты решаешь:")
]
buttons = {"Передохнуть под тенью дерева": "I_a_04_00",
           "Познакомиться с кем-нибудь": "I_a_04_01"}
states["I_a_03_01"] = State(content, buttons, "I_a_04_00")

# I_a_04_00
content = [
    ContentUnit("text", "Прислонившись к стволу, ты тихо закрываешь глаза…", delay=0),
    ContentUnit("text",
                "Пшшшшшш!!! Ты просыпаешься от звуков приехавшего автобуса и топота ребят, бегущих в его сторону, желая скорее занять места.")
]
buttons = {"Сесть в автобус": "I_b_00_00"}
states["I_a_04_00"] = State(content, buttons, "I_b_00_00")

# I_a_04_01
content = [
    ContentUnit("text", "- Ну и жара, сегодня, правда? - сказал ты, желая завести разговор с парнем неподалёку."),
    ContentUnit("text",
                "Да это ещё цветочки! Вот у нас в Монголии такой зной бывает, что яичницу на камнях готовь, – пошутил он в ответ."
                ""
                "Как тебя звать? (впиши свое имя)")
]

buttons = None
states["I_a_04_01"] = State(content, buttons, "I_a_05_00")

# I_a_04_02
content = [ContentUnit("text",
                       "Проверка по списку, точно. В надежде, что твоя очередь не прошла, ты подходишь к столпотворению студентов."
                       "Координатор находит тебя в списке."),
           ContentUnit("text", "Оказывается, автобус приедет через 30 минут. Ты решаешь:")]
buttons = {"Передохнуть под тенью дерева": "I_a_04_00",
           "Познакомиться с кем-нибудь": "I_a_04_01"}
states["I_a_04_02"] = State(content, buttons, "I_a_04_01")


# I_a_05_00  First Meeting with Vanya

def set_name(player, message):
    player.name = message.text
    player.current_state.content[0] = ContentUnit("text", player.name + ", - сообщил ты, смеясь над шуткой.", delay=0)
    player.friendship = True
    print(str(player.id) + " name: " + player.name)


content = [
    ContentUnit("text", "#name, - сообщил ты, смеясь над шуткой.", delay=0),
    ContentUnit("text", "Очень приятно, Иван, - бросил новый знакомый, улыбаясь в ответ.", delay=0),
    ContentUnit("text", "В это время уже подъезжал автобус.", delay=0)
]
buttons = {"Сесть в автобус": "I_b_00_00"}
states["I_a_05_00"] = State(content, buttons, "I_b_00_00", callback=set_name)


# I_b_00_00 Arrival
def set_surname(player, message):
    player.surname = message.text
    print(str(player.id) + " surname:" + player.surname)


content = [
    ContentUnit("text", "Прошло 45 минут.  Ты с ребятами проходишь в дверь одного из блоков университетского кампуса."),
    ContentUnit("text", "Ну и столпотворение! Селёдкам в банке можно только позавидовать… "
                        "Эх, тянет мысли на еду. Проголодался. Перекусить бы…"),
    ContentUnit("text", "Но нет, нужно ещё пройти регистрацию и добраться до комнаты.", delay=0),
    ContentUnit("text", "Долгая очередь…", delay=0),
    ContentUnit("text", "Душно очень, открытые окна не помогают, и снова хочется пить."),
    ContentUnit("text",
                "Красные от жары охранники прижимаются к стене, стараясь освободить место постоянному потоку новых студентов."),
    ContentUnit("text",
                "Измотанные старшекурсники-волонтёры из всех сил стараются, выдавая студентам ключи и другие вещи. Со всех сторон летят вопросы, но из-за шума услышать ответы очень тяжело."),
    ContentUnit("text",
                "Подойдя, наконец, к стойке регистрации (стол обычный) ты называешь свою фамилию(впиши свою фамилию)")]
buttons = None
states["I_b_00_00"] = State(content, buttons, "I_c_00_00")


# I_c_00_00
def check_friendship(player, message):
    if (player.friendship):
        player.current_state = states["I_c_01_00"]
    else:
        player.current_state = states["I_c_01_01"]


content = [
    ContentUnit("text", "Взяв вещи, ты поднимаешься наверх и поворачиваешь в длинный коридор"),
    ContentUnit("text", "Наконец-то ты пришёл! 313ая."),
    ContentUnit("text", "Ты входишь в комнату."),
    ContentUnit("text", "Тяжелое падение на мягкую кровать…"),
    ContentUnit("text", "Глубокий выдох…", delay=0),
    ContentUnit("text", "Да, это был тяжелый день."),
    ContentUnit("text", "Стой! Тебе послышалось?"
                        "Кто-то вошёл в твою комнату"),
    ContentUnit("text", "Ты приподнимаешь голову и видишь невысокого парня с темными волосами.")
]
buttons = {"Дальше": "I_c_01_00"}
states["I_c_00_00"] = State(content, buttons, "I_c_01_00", callback=set_surname)

# I_c_01_00
content = [
    ContentUnit("text", "Да это же Ваня! Тот парень из Монголии! Вот так совпадение, вы с ним соседи!"),
    ContentUnit("text",
                "Посмотрев на часы (5:30), новый сосед решает пойти в университет на встречу со студентами.Ты решаешь:")
]
buttons = {"Пойти вместе с ним на встречу.": "I_c_03_00",
           "Пойти в столовую перекусить перед встречей": "I_c_03_01",
           "Пойти спать.": "I_c_03_02"}
states["I_c_01_00"] = State(content, buttons, "I_c_03_00", callback=check_friendship)

# I_c_01_01
content = [
    ContentUnit("text", "- Ну и жара, сегодня, правда? - сказал ты, желая завести разговор с парнем."),
    ContentUnit("text",
                "Да это ещё цветочки! Вот у нас в Монголии такой зной бывает, что яичницу на камнях готовь, – пошутил он в ответ."
                ""
                "Как тебя звать? (впиши свое имя)")
]
buttons = None
states["I_c_01_01"] = State(content, buttons, "I_c_02_00")

# I_c_02_00
content = [
    ContentUnit("text", "#name, - сообщил ты, смеясь над шуткой.", delay=0),
    ContentUnit("text", "Очень приятно, Иван, - бросил новый знакомый, улыбаясь в ответ.", delay=0),
    ContentUnit("text",
                "Посмотрев на часы (5:30), новый сосед решает пойти в университет на встречу со студентами. Ты решаешь:",
                delay=0)
]
buttons = {"Пойти вместе с ним на встречу.": "I_c_03_00",
           "Пойти в столовую перекусить перед встречей": "I_c_03_01",
           "Пойти спать.": "I_c_03_02"}
states["I_c_02_00"] = State(content, buttons, "I_c_03_00", callback=set_name)


# I_c_03_00 Meeting
def set_meeting(player, message):
    player.meeting = True


content = [
    ContentUnit("text",
                "Вы приходите на встречу с 10 минутным запасом, усаживаетесь на зелёные ступени и готовитесь слушать."),
    ContentUnit("text", "--ИНФОРМАЦИЯ О ВСТРЕЧЕ--", delay=2),
    ContentUnit("text", "После встречи ты решил пойти:")
]
buttons = {"В столовую": "I_c_04_00",
           "Спать": "I_c_03_02"}
states["I_c_03_00"] = State(content, buttons, "I_a_04_00", callback=set_meeting)

# I_c_03_01 Cafeteria before meeting
content = [
    ContentUnit("text", "Ты не ел уже, кажется, целую вечность. Перекусить сейчас точно не помешает."),
    ContentUnit("text",
                "Сказав, что ты постараешься успеть до начала встречи, параллельно урча своим голодным желудком, ты отправился в столовую."),
    ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
    ContentUnit("text", "После сытного ужина ты пошёл:")
]
buttons = {"На назначенную встречу": "I_c_04_01",
           "Спать": "I_c_03_02"}
states["I_c_03_01"] = State(content, buttons, "I_a_04_01")

# I_c_03_02 Sleep
content = [
    ContentUnit("text", "Да, это был тяжелый день. Зайдя в комнату, ты завалился на кровать и уснул")
]
buttons = {"Start next day": "II_a_00_00"}
states["I_c_03_02"] = State(content, buttons, "II_a_00_00")

# I_c_04_00 Cafeteria after meeting
content = [
    ContentUnit("text", "Ты не ел уже, кажется, целую вечность. Перекусить сейчас точно не помешает."),
    ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
    ContentUnit("text", "После сытного ужина ты пошел спать", delay=2),
    ContentUnit("text", "Да, это был тяжелый день. Зайдя в комнату, ты завалился на кровать и уснул")
]
buttons = {"Start next day": "II_a_00_00"}
states["I_c_04_00"] = State(content, buttons, "II_a_00_00")

# I_c_04_01 Meeting late
content = [
    ContentUnit("text", "Ты опоздал на назначенную встречу…", delay=2),
    ContentUnit("text", "Но, похоже, ты ещё не всё пропустил."),
    ContentUnit("text", "Тихо подсев сбоку ты начал слушать, что говорит куратор."),
    ContentUnit("text", "--Неполная информация на встрече—", delay=2),
    ContentUnit("text", "Черт! После встречи вам и так полагался бесплатный ужин..."
                        "Будет тебе уроком на будущее!", delay=3),
    ContentUnit("text", "После встречи ты пошел спать."),
    ContentUnit("text", "Да, это был тяжелый день. Зайдя в комнату, ты завалился на кровать и уснул")

]
buttons = {"Start next day": "II_a_00_00"}
states["I_c_04_01"] = State(content, buttons, "II_a_00_00", callback=set_meeting)

# II_a_00_00
content = [
    ContentUnit("text", "Наступило утро.", delay=2),
    ContentUnit("text", "Пронзая окна, тёплые лучи солнечного света будят тебя."),
    ContentUnit("text", "Но будильник ещё не звонил, поспать бы ещё…", delay=3),
    ContentUnit("text", "Не спится…", delay=2),
    ContentUnit("text", "Ты встаешь с кровати с чувством бодрости, смешанным со слабостью после вчерашнего дня."),
    ContentUnit("text", "Собравшись на утренние процедуры, ты направляешься в уборную."),
    ContentUnit("text", "Внезапно, распахивается дверь неподалёку, и из неё выходит Ваня, с полотенцем на плече."),
    ContentUnit("text",
                "Встретившись взглядами, вы замираете на мгновение, как два ковбоя, готовящиеся к перестрелке."),
    ContentUnit("text", "Ты решаешь:")
]
buttons = {"Вежливо пропустить соседа первым в уборную.": "II_a_01_00",
           "Ринуться первым в уборную": "II_a_01_01"}
states["II_a_00_00"] = State(content, buttons, "II_a_01_00")

# II_a_01_00
content = [
    ContentUnit("text", "-Доброе утро, проходи. Я подожду."),
    ContentUnit("text", "-Доброе, спасибо, - ответил сосед, потирая сонные глаза.")
]
buttons = {"Дальше": "II_a_02_00"}
states["II_a_01_00"] = State(content, buttons, "II_a_02_00")

# II_a_01_01
content = [
    ContentUnit("text", "Сломя голову, крича: «Я первый!», ты летишь в сторону уборную.", delay=2),
    ContentUnit("text", "Сосед остался в дверном проёме, в замешательстве выпучив глаза на твой внезапный марш бросок.",
                delay=2)
]
buttons = {"Дальше": "II_a_02_00"}
states["II_a_01_01"] = State(content, buttons, "II_a_02_00")

# II_a_02_00
content = [
    ContentUnit("text", "Закончив гигиенические процедуры, вы вместе направляетесь в столовую на завтрак."),
    ContentUnit("text", "-Классно здесь кормят, - сказал ты, уминая вкуснейший завтрак."),
    ContentUnit("text", "-Ага, ещё и бесплатно пока мы на летней школе, ответил Ваня"),
    ContentUnit("text",
                "-О, а потом, наверное, кучу денег нужно будет отдавать за всю эту вкуснятину, - пожаловался ты."),
    ContentUnit("text", "-Не то чтобы много… Можно ведь выбрать план питания, подходящий именно тебе."),
    ContentUnit("text", "- Да? Как же? – поинтересовался ты."),
    ContentUnit("text", "- В студенческом кабинете, очень удобная штука. Можешь найти по этой ссылке."),
    ContentUnit("text", "https://my.university.innopolis.ru/"),
    ContentUnit("text", "Убрав за собой поднос, ты направился на свою первую лекцию в Иннополисе. Круто!")
]
buttons = {"Дальше": "II_a_03_00"}
states["II_a_02_00"] = State(content, buttons, "II_a_03_00")

# II_a_03_00
content = [
    ContentUnit("text",
                "У лектория уже собралась куча народу. Теперь ребята смотрятся иначе, без вчерашнего багажа, но с портфелями, тетрадями."),
    ContentUnit("text", "На первой лекции вас вводят в курс дела перед началом обучения."),
    ContentUnit("text",
                "Начинают с «плохих» новостей, сообщив, что обучение фиксировано в определённых рамках и не прерывается ни на какие государственные или национальные праздники!"),
    ContentUnit("text",
                "А потом сказали, что почти вся необходимая информация по курсам находится в каком-то «Мудле»."),
    ContentUnit("text", "- Что, прямо всё-всё там? – спросил кто-то с последних рядов"),
    ContentUnit("text", "- Да, и домашние задания, и лекции, и оценки по курсам. Всё есть на сайте"),
    ContentUnit("text", "https://moodle.university.innopolis.ru"),
    ContentUnit("text", "Хм.… А где же хорошие новости, - подумал ты."),
    ContentUnit("text", "- И, наконец, перед началом лекции хочу сообщить вам ещё кое-что."),
    ContentUnit("text", "- С завтрашнего дня открываются различные кружки и клубы по интересам для студентов."),
    ContentUnit("text", "- Ознакомиться со списком можете прямо сейчас, если хотите."),
    ContentUnit("text", "Ты решаешь:"),

]
buttons = {"Просмотреть список клубов": "II_a_04_00",
           "Оставить на потом и приготовиться слушать лекцию.": "II_a_05_00",
           }
states["II_a_03_00"] = State(content, buttons, "II_a_05_00")

# II_a_04_00 List of Clubs
content = [
    ContentUnit("text", "--СПИСОК КЛУБОВ--")
]
buttons = {"Дальше": "II_a_05_00"}
states["II_a_04_00"] = State(content, buttons, "II_a_05_00")




# II_a_05_00

content = [
    ContentUnit("text", "Выходя из лектория, ты ощущаешь груз новой информации в голове.")
]
buttons = {"А куда дальше?": "II_a_06_00"}
states["II_a_05_00"] = State(content, buttons, "II_a_06_00")

# II_a_06_00
def check_meeting(player, message):
    if player.meeting == True:
        player.current_state = states["II_a_06_00"]
    else:
        player.current_state = states["II_a_06_01"]
content = [
    ContentUnit("text",
                "Что ж, ты помнишь, как вчера объяснили основу расписания и направляешься с ребятами на практический семинар"),
    ContentUnit("text", "Там тебе удастся лучше усвоить пройденный на лекции материал.")
]
buttons = {"Дальше": "II_a_07_00"}
states["II_a_06_00"] = State(content, buttons, "II_a_07_00",callback=check_meeting)

# II_a_06_01
content = [
    ContentUnit("text", "Остановившись на мгновение, ты пытаешься собраться с мыслями.", delay=2),
    ContentUnit("text",
                "- Чего стоишь, пойдём на семинар, - произнёс Ваня, - там всегда можно уточнить то, что не понял на лекции.")
]
buttons = {"Дальше": "II_a_07_00"}
states["II_a_06_01"] = State(content, buttons, "II_a_07_00")

# II_a_07_00
content = [
    ContentUnit("text",
                "'"'Уложив по полочкам'"' новые знания на семинаре, ты почувствовал большое облегчение, и, даже, радость!"),
    ContentUnit("text",
                "А чтобы знания окрепли ещё сильнее, студентам выдали домашнюю работу для практики, со словами: «Грызите гранит науки, господа!»"),
    ContentUnit("text", "- Да, умеют они мотивировать, - усмехнулся твой друг."),
    ContentUnit("text", "И вы вместе направились на занятие по английскому языку."),
    ContentUnit("text", "Не удивительно. Университет с англоговорящими профессорами."),
    ContentUnit("text", "Сразу было понятно, что без хороших знаний английского здесь не обойтись.")
]
buttons = {"Дальше": "II_a_08_00"}
states["II_a_07_00"] = State(content, buttons, "II_a_08_00")

# II_a_08_00 TODO: CHANGE RESTART BUTTON TO NEXT DAY

content = [
    ContentUnit("text", "Вечером после первого учебного дня вы с соседом общаетесь за чашкой чая."),
    ContentUnit("text", "- Даа, студентов здесь учат по-настоящему. Столько занятий, да ещё и заданий надавали – пруд пруди, - сказал ты Ване."),
    ContentUnit("text", "-А, то! Они своё дело знают, да и студентов не обижают. За все труды награда воздаётся, - услышал ты в ответ."),
    ContentUnit("text", "- Ну, сказанул! «Награда воздаётся»! Как будто они нас манной небесной одарят за учёбу… - удивился ты."),
    ContentUnit("text", "- Манную кашу я не люблю, - сказал Ваня, - но ты слышал, какую они стипендию студентам выдают?"),
    ContentUnit("text", "- Ой, ну удиви меня! – подразнил ты в ответ"),
    ContentUnit("text", "- От 12 до 24 тысяч рублей. А для отличников все 36. И это только бакалаврам."),
    ContentUnit("text", "Рот у тебя от удивления открылся сам."),
    ContentUnit("text", "- Так что я буду учиться хорошо, потом родителям и себе подарки сделаю"),
    ContentUnit("text", "Ты всё ещё замираешь от удивления."),
    ContentUnit("text", "- Ладно, это потом, а сейчас – домашка! И тебе советую не лениться, сам понимаешь."),
    ContentUnit("text", "Хлопнувшая дверь на кухне взбодрила тебя."),
    ContentUnit("text", "- Подожди меня! - крикнул ты соседу в след, стараясь быстрее допить свой чай."),
]
buttons = {"Restart 2nd day":"II_a_00_00",
           "Restart 1st day":"I_a_00_00"}
states ["II_a_08_00"] = State(content, buttons, "II_a_00_00")

#

