from contentUnit import ContentUnit
from state import State

states: State = {}

# I_a_00_00 Start Point

content = [ContentUnit("text",
                       "Поздравляю, ты получил грант в Иннополисе! Ты стоишь на пороге новой, полной приключений, студенческой жизни"),
           ContentUnit("text",
                       "Твоя история начинается здесь – в Казани, большом соседе пока ещё маленького, но возлагающего большие надежды инногорода.")
           ]
buttons = {"дальше": "I_a_01_00"}
states["I_a_00_00"] = State(content, buttons, "I_a_01_00")

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
states["I_b_00_00"] = State(content, buttons,"I_c_00_00" )

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
buttons = {"Дальше":"I_c_01_00"}
states["I_c_00_00"] = State(content, buttons,"I_c_01_00",callback=set_surname )


#I_c_01_00 TODO
content = [
    ContentUnit("text", "Да это же Ваня! Тот парень из Монголии! Вот так совпадение, вы с ним соседи!"),
    ContentUnit("text","Посмотрев на часы (5:30), новый сосед решает пойти в университет на встречу со студентами.Ты решаешь:"
                       ""
                       "ЗДЕСЬ ВВЕДИТЕ /start")
]
buttons = {"Пойти вместе с ним на встречу.":"I_c_01_00",
           "Пойти в столовую перекусить перед встречей":"I_c_01_00",
           "Пойти спать.":"I_c_01_00"}
states["I_c_01_00"] = State(content, buttons,"I_c_01_00", callback=check_friendship)

#I_c_01_01
content = [
    ContentUnit("text", "- Ну и жара, сегодня, правда? - сказал ты, желая завести разговор с парнем."),
    ContentUnit("text",
                "Да это ещё цветочки! Вот у нас в Монголии такой зной бывает, что яичницу на камнях готовь, – пошутил он в ответ."
                ""
                "Как тебя звать? (впиши свое имя)")
]
buttons = None
states["I_c_01_01"] = State(content, buttons,"I_c_02_00")

#I_c_02_00
content = [
    ContentUnit("text", "#name, - сообщил ты, смеясь над шуткой.", delay=0),
    ContentUnit("text", "Очень приятно, Иван, - бросил новый знакомый, улыбаясь в ответ.", delay=0),
    ContentUnit("text", "Посмотрев на часы (5:30), новый сосед решает пойти в университет на встречу со студентами. Ты решаешь:"
                        "ЗДЕСЬ ВВЕДИТЕ /start", delay=0)
]
buttons = {"Пойти вместе с ним на встречу.":"I_c_02_00",
           "Пойти в столовую перекусить перед встречей":"I_c_02_00",
           "Пойти спать.":"I_c_02_00"}
states["I_c_02_00"] = State(content, buttons, "I_c_02_00", callback=set_name)