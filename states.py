from contentUnit import ContentUnit
from state import  State
states: State = {}

# I_a_00_00 Start Point
text = ["Поздравляю, ты получил грант в Иннополисе! Ты стоишь на пороге новой, полной приключений, студенческой жизни.",
        "Твоя история начинается здесь – в Казани, большом соседе пока ещё маленького, но возлагающего большие надежды инногорода."
        ]
photos = None
keys = {"дальше":"I_a_01_00"}
content = ContentUnit(text,photos,keys, None)
children = ["I_a_01_00"]
states["I_a_00_00"] = State(content,children,"I_a_01_00")

# I_a_01_00  Start Point 1
text = ["Ты приближаешься к остановке «Комбинат здоровье». Прогнозы погоды не соврали, день сегодня выдался жаркий.",
        "Усталость тебя не расстраивает. Ты почти на месте. Грёзы о будущем прерывает навязчивое чувство жажды, но не хочется останавливаться."
        ]
photos = None
keys = {"дальше":"I_a_02_00"}
content = ContentUnit(text,photos,keys, None)
children = ["I_a_02_00"]
states["I_a_01_00"] = State(content, children,"I_a_02_00")

# I_a_02_00 First Choice. Water or Look around
text = ["И вот ты на месте. Группы людей уже активно общаются. Похоже, твоего появления никто даже не заметил.",
        "Поставив тяжёлые сумки на асфальт, ты решаешь."
        ]
photos = None
keys = {"оглянуться кругом":"I_a_03_00",
        "выпить воды": "I_a_03_01"}
content = ContentUnit(text,photos,keys, None)
children = ["I_a_03_00","I_a_03_01"]
states["I_a_02_00"] = State(content,children,"I_a_03_00")

#I_a_03_00 TO DO:
text = ["Интересно, что там делают ребята? Приближаясь к группе, ты начинаешь улавливать фразы:",
        "- Бурнашев Илья!"
        "- Есть!",
        "- Наумова Дарья!"
        "- Есть!",
        "- Цыдан… Цендендам…",
        "«Цыдендамбаев Иван – здесь! Из Монголии я», - выдал кто-то из толпы, с трудом сдерживая смех."]
photos = None
keys = {"дальше":"I_a_02_00"}
content = ContentUnit(text,photos,keys, None)
children = ["I_a_03_00","I_a_03_01"]
states["I_a_03_00"] = State(content,children,"I_a_03_00")

#I_a_03_01 TO DO:
text = ["Да, как же хочется пить… Хорошо, что с собой есть немного воды. До тебя доносятся звуки имён, фамилии и смех ребят."]
photos = None
keys = {"дальше":"I_a_02_00"}
content = ContentUnit(text,photos,keys, None)
children = ["I_a_03_00","I_a_03_01"]
states["I_a_03_01"] = State(content,children,"I_a_03_01")

