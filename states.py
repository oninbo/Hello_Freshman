from contentUnit import ContentUnit
from state import State

states: State = {}

# I_a_00_00 Start Point

content = [ContentUnit("text",
                       "Поздравляю, ты получил грант в Иннополисе! Ты стоишь на пороге новой, полной приключений, студенческой жизни"),
           ContentUnit("text",
                       "Твоя история начинается здесь – в Казани, большом соседе пока ещё маленького, но возлагающего большие надежды инногорода.")
           ]
states["I_a_00_00"] = State(content, "I_a_01_00")

# I_a_01_00  Start Point 1
content = [
           ContentUnit("photo","http://sportgyms.ru/uploads/posts/2014-10/1413369414_01.jpg"),
           ContentUnit("text",
                       "Ты приближаешься к остановке «Комбинат здоровье». Прогнозы погоды не соврали, день сегодня выдался жаркий."),
           ContentUnit("text",
                       "Усталость тебя не расстраивает. Ты почти на месте. Грёзы о будущем прерывает навязчивое чувство жажды, но не хочется останавливаться.")
           ]
states["I_a_01_00"] = State(content, "I_a_02_00")

# I_a_02_00 First Choice. Water or Look around
content = [ContentUnit("text","И вот ты на месте. Группы людей уже активно общаются. Похоже, твоего появления никто даже не заметил."),
        ContentUnit("text","Поставив тяжёлые сумки на асфальт, ты решаешь:")
        ]
buttons = {"Оглянуться кругом": "I_a_03_00",
           "Выпить воды": "I_a_03_01"}
states["I_a_02_00"] = State(content, "I_a_03_00", buttons)


def drink():
    print("DRINK")

# I_a_03_00 TO DO:
content = [ContentUnit("text","Интересно, что там делают ребята? Приближаясь к группе, ты начинаешь улавливать фразы:", delay=2),
        ContentUnit("text","- Бурнашев Илья!", delay=1),
        ContentUnit("text", "- Есть!", delay=1),
        ContentUnit("text","- Наумова Дарья!", delay=1),
        ContentUnit("text", "- Есть!", delay=1),
        ContentUnit("text","- Цыдан… Цендендам…", delay=1),
        ContentUnit("text","«Цыдендамбаев Иван – здесь! Из Монголии я», - выдал кто-то из толпы, с трудом сдерживая смех.", delay=1)]
states["I_a_03_00"] = State(content, "I_a_03_00")

# I_a_03_01 TO DO:
content = [
    ContentUnit("text","Да, как же хочется пить… Хорошо, что с собой есть немного воды. До тебя доносятся звуки имён, фамилии и смех ребят.")]
states["I_a_03_01"] = State(content, "I_a_03_01")
states["I_a_03_01"].callback = drink