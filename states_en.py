from state import State
from functions import *
from contentUnit import ContentUnit
import photos
import copy

states: State = {}

# language_select
content = [
    ContentUnit("text", "Выберите язык "
                        "\nChoose your language"),
]
buttons = {"Русский": "sex_select",
           "English": "sex_select"
           }
states["language_select"] = State(content, buttons, callback=set_language)

# sex_select

content = [ContentUnit("text",
                       "Choose your sex")]
buttons = {"Male": "I_a_00_00", "Female": "I_a_00_00"}
states["sex_select"] = State(content, buttons, callback=set_sex)

# I_a_00_00 Start Point

content = {
    True: [
        ContentUnit("text",
                    "Congratulations, you received a grant in Innopolis! You are standing on the threshold of a new full of adventures student’s life."),
        ContentUnit("text",
                    "Your story begins here, in Kazan, the big neighbor of innocity, which is still small, but it has a promising future.")
    ],
    False: [
        ContentUnit("text",
                    "Congratulations, you received a grant in Innopolis! You are standing on the threshold of a new full of adventures student’s life."),
        ContentUnit("text",
                    "Your story begins here, in Kazan, the big neighbor of innocity, which is still small, but it has a promising future.")
    ]
}
buttons = {"Next": "I_a_01_00"
           }
states["I_a_00_00"] = State(content, buttons)

# I_a_01_00  Start Point 1
content = [ContentUnit("text",
                       "You are approaching the bus stop 'Комбинат Здоровье'(Combinat Zdorovie). Weather forecasts did not lie, today is a hot day."),
           ContentUnit("photo", photos.urls["kombinat"]),
           ContentUnit("text",
                       "Fatigue does not upset you. You're almost there. The haunting feeling of thirst interrupts dreams of the future but you don't want to stop.")
           ]
buttons = {"Next": "I_a_02_00"}
states["I_a_01_00"] = State(content, buttons)

# I_a_02_00 First Choice. Water or Look around
content = [ContentUnit("text",
                       "And here you are on the spot. Groups of people are already communicating actively. Looks like noone have noticed how you came."),
           ContentUnit("text", "Putting heavy bags on the pavement, you decide to:")
           ]
buttons = {"Look around": "I_a_03_00",
           "Drink water": "I_a_03_01"}
states["I_a_02_00"] = State(content, buttons)

# I_a_03_00
content = [
    ContentUnit("text",
                " You wonder what these guys are doing. Approaching the group, you are starting to catch some phrases:"),
    ContentUnit("text", "- Burnashev Ilya!"
                        "- Here!"),
    ContentUnit("text", "- Daria Naumova!"
                        "- Here!"),
    ContentUnit("text", "- Tsidan... Tsaddendum..."),
    ContentUnit("text",
                "'Tsydendambaev Ivan is here! I am from Mongolia', - gave someone in the crowd, barely holding back his laughter.")]
buttons = {"Next": "I_a_04_02"}
states["I_a_03_00"] = State(content, buttons)

# I_a_03_01
content = [
    ContentUnit("text",
                "Yes, you are so thirsty... Well, you have a bottle of water with you. You can hear the sounds of the names and the laughter of people.",
                delay=0),
    ContentUnit("text", "It turns out that the bus will arrive within 30 minutes. You decide to:")
]
buttons = {"Take a break in the shade of tree": "I_a_04_00",
           "Make a friend": "I_a_04_01"}
states["I_a_03_01"] = State(content, buttons)

# I_a_04_00
content = [
    ContentUnit("text", "Leaning against the trunk, you quietly close your eyes..."),
    ContentUnit("text",
                "Pssssssh!!! You wake up from the sounds of the arrived bus and the clatter of students running in its direction to take best places."),
    ContentUnit("photo", photos.urls["shuttle"]),
]
buttons = {"Go in bus": "I_b_00_00"}
states["I_a_04_00"] = State(content, buttons)

# I_a_04_01
meeting_content = {
    True: [
        ContentUnit("text",
                    "- It's a hot today, isn't it? - You said, wanting to start a conversation with a guy nearby."),
        ContentUnit("text",
                    " - And it’s still not that bad! Sometimes in Mongolia we have such intense heat that we could cook eggs on the stones, – he joked in response. What is yout name?(write your name)")
    ],
    False: [
        ContentUnit("text",
                    "- It's a hot today, isn't it? - You said, wanting to start a conversation with a girl nearby."),
        ContentUnit("text",
                    "- Yes, that's for sure. Looks like it waited specially for us. I thought leaving Mongolia means leaving the heat. Ha-ha. I was wrong. Come to me, here it is cooler in the shadows.")
    ]
}

buttons = None
states["I_a_04_01"] = State(meeting_content, buttons, default_children="I_a_05_00", callback=set_name)

# I_a_04_02
content = [ContentUnit("text",
                       " Of course! Check of the presence list. With hope that you are not late, you are going to the crowd of students."),
           ContentUnit("text", "It turns out that the bus will arrive within 30 minutes. You decide to:")]
buttons = {"Take a break in the shade of tree": "I_a_04_00",
           "Make a friend": "I_a_04_01"}
states["I_a_04_02"] = State(content, buttons)

# I_a_05_00  First Meeting with Vanya
say_name_content = {
    True: [
        ContentUnit("text", "- My name is #name, - you told, laughing at a joke."),
        ContentUnit("text", "- Nice to meet you. My name is Ivan, - said your new friend, smiling in response."),
        ContentUnit("text", "At this time, the bus was driving up."),
        ContentUnit("photo", photos.urls["shuttle"]),
    ],
    False: [
        ContentUnit("text", "- My name is #name, - told you hiding from the heat in the shade of a tree."),
        ContentUnit("text", "- Nice to meet you. My name is Yana, - replied your new friend."),
        ContentUnit("text", "At this time, the bus was driving up."),
        ContentUnit("photo", photos.urls["shuttle"]),
    ]
}
buttons = {"Go in bus": "I_b_00_00"}
states["I_a_05_00"] = State(say_name_content, buttons)

# I_b_00_00 Arrival
content = {
    True: [
        ContentUnit("text",
                    "It's been 45 minutes. You with other guys walk in the door of one of the blocks of the university campus."),
        ContentUnit("photo", photos.urls["korpus"]),
        ContentUnit("text", "What a pandemonium! Even sardines in a can feel better..."
                            "Eh, thoughts of food. You are hungry. Some meal would be nice right now..."),
        ContentUnit("text", "No, you still need to register and get to the room."),
        ContentUnit("text", " Long queue…"),
        ContentUnit("text", "Душно очень, открытые окна не помогают, и снова хочется пить."),
        ContentUnit("text",
                    "But it is cooler here than on the street. Air conditioners are diligently doing their job."),
        ContentUnit("text",
                    "Exhausted upperclassmen volunteers are working hard, giving keys and other stuff to the students. All around there're thousands of questions, but It is very hard to hear the answers because of the noise."),
        ContentUnit("text",
                    "Finally, coming to the front desk you call your surname: (write your surname)")
    ],
    False: [
        ContentUnit("text",
                    "It's been 45 minutes. You with other guys walk in the door of one of the blocks of the university campus."),
        ContentUnit("photo", photos.urls["korpus"]),
        ContentUnit("text", "What a pandemonium! Even sardines in a can feel better..."
                            "Eh, thoughts of food. You are hungry. Some meal would be nice right now..."),
        ContentUnit("text", "No, you still need to register and get to the room."),
        ContentUnit("text", " Long queue…"),
        ContentUnit("text", "Душно очень, открытые окна не помогают, и снова хочется пить."),
        ContentUnit("text",
                    "But it is cooler here than on the street. Air conditioners are diligently doing their job."),
        ContentUnit("text",
                    "Exhausted upperclassmen volunteers are working hard, giving keys and other stuff to the students. All around there're thousands of questions, but It is very hard to hear the answers because of the noise."),
        ContentUnit("text",
                    "Finally, coming to the front desk you call your surname: (write your surname)")
    ]
}
buttons = None
states["I_b_00_00"] = State(content, buttons, default_children="I_c_00_00", callback=set_surname)

# I_c_00_00
content = {
    True: [
        ContentUnit("text", "Taking things, you go upstairs and turn in the long hallway"),
        ContentUnit("photo", photos.urls["koridor"]),
        ContentUnit("text", " Finally you came! 313."),
        ContentUnit("text", "You walk into a room."),
        ContentUnit("photo", photos.urls["kitchen"]),
        ContentUnit("text", "A heavy fall on the soft bed..."),
        ContentUnit("photo", photos.urls["bedroom"]),
        ContentUnit("text", "A deep breath…"),
        ContentUnit("text", "Yes, it was a hard day."),
        ContentUnit("text", "Stop! Did you hear that? Someone came into your room."),
        ContentUnit("text", "You turn your head and see not tall person with dark hair.")
    ],
    False: [
        ContentUnit("text", "Taking things, you go upstairs and turn in the long hallway"),
        ContentUnit("photo", photos.urls["koridor"]),
        ContentUnit("text", " Finally you came! 313."),
        ContentUnit("text", "You walk into a room."),
        ContentUnit("photo", photos.urls["kitchen"]),
        ContentUnit("text", "A heavy fall on the soft bed..."),
        ContentUnit("photo", photos.urls["bedroom"]),
        ContentUnit("text", "A deep breath…"),
        ContentUnit("text", "Yes, it was a hard day."),
        ContentUnit("text", "Stop! Did you hear that? Someone came into your room."),
        ContentUnit("text", "It was not tall dark-haired girl with brown eyes and a birthmark on her neck."),

    ]
}
buttons = {"Next": "I_c_01_00"}
states["I_c_00_00"] = State(content, buttons, callback=check_friendship)

# I_c_01_00
content = {
    True: [
        ContentUnit("text", "Yes, it’s Ivan! The boy from Mongolia! What a coincidence that you are neighbors!"),
        ContentUnit("text",
                    "Looking at the clock (5:30), a new neighbor decides to go to the University on the students meeting."),
        ContentUnit("text", "You decide to:")
    ],
    False: [
        ContentUnit("text", " Yes, it’s Yana! The girl from Mongolia! What a coincidence that you are neighbors!"),
        ContentUnit("text",
                    "Looking at the clock (5:30), a new neighbor decides to go to the University on the students meeting."),
        ContentUnit("text", "You decide to:")
    ]
}
buttons = {"Go on meeting with friend": "I_c_03_00",
           "Go to canteen and eat something": "I_c_03_01",
           "Go to sleep": "I_c_03_02"}
states["I_c_01_00"] = State(content, buttons)

# I_c_01_01
buttons = None
meeting_content = copy.deepcopy(meeting_content)
meeting_content[False][-1] = ContentUnit("text",
                                         " Yes, that's for sure. Looks like it waited specially for us. I thought leaving Mongolia means leaving the heat. Ha-ha. I was wrong. What is yout name?(write your name)")
states["I_c_01_01"] = State(meeting_content, buttons, default_children="I_c_02_00", callback=set_name)

# I_c_02_00
buttons = {"Go on meeting with friend": "I_c_03_00",
           "Go to canteen and eat something": "I_c_03_01",
           "Go to sleep": "I_c_03_02"}
say_name_content = copy.deepcopy(say_name_content)
for key in say_name_content.keys():
    del say_name_content[key][-1]
say_name_content[False][0] = ContentUnit("text", "My name is #name, - you told, laughing at a joke.")
states["I_c_02_00"] = State(say_name_content, buttons)

# I_c_03_00 Meeting
content = [
    ContentUnit("text",
                "You come to the meeting with 10 minutes to spare. You take а seat on a green stage and get ready to listen."),
    ContentUnit("photo", photos.urls["stairs"]),
    ContentUnit("text",
                "Students are reported that with any issues CONNECTED WITH NON-EDUCATIONAL PART (choosing the meal plan, participation in a hackathon, organising an event etc.) that may arise at University, they are free to contact @StudentAffairs_bot in Telegram or 319 office, so-called “island of hope”. If there's a question connected with educational process, lessons, courses, diplomas and everything that is connected with studying feel free to contact Department of Education (education@innopolis.ru, 460 office).",
                delay=2),
]

buttons = {"Next": "I_c_03_00_dyuster"}
states["I_c_03_00"] = State(content, buttons)

content = {
    True: [
        ContentUnit("text", "You are late on the meeting.", delay=2),
        ContentUnit("text", "НBut it seems like you haven’t missed all the meeting."),
        ContentUnit("photo", photos.urls["stairs"]),
        ContentUnit("text", "ТQuietly taking place at the side and began to listening to the curator."),
        ContentUnit("text",
                    "Students are reported that with any issues CONNECTED WITH NON-EDUCATIONAL PART (choosing the meal plan, participation in a hackathon, organising an event etc.) that may arise at University, they are free to contact @StudentAffairs_bot in Telegram or 319 office, so-called “island of hope”. If there's a question connected with educational process, lessons, courses, diplomas and everything that is connected with studying feel free to contact Department of Education (education@innopolis.ru, 460 office).",
                    delay=2),
    ],
    False: [
        ContentUnit("text", "Ты опоздала на назначенную встречу…", delay=2),
        ContentUnit("text", "Но, похоже, ты ещё не всё пропустила."),
        ContentUnit("photo", photos.urls["stairs"]),
        ContentUnit("text", "Тихо подсев сбоку ты начала слушать, что говорит куратор."),
        ContentUnit("text",
                    "Students are reported that with any issues CONNECTED WITH NON-EDUCATIONAL PART (choosing the meal plan, participation in a hackathon, organising an event etc.) that may arise at University, they are free to contact @StudentAffairs_bot in Telegram or 319 office, so-called “island of hope”. If there's a question connected with educational process, lessons, courses, diplomas and everything that is connected with studying feel free to contact Department of Education (education@innopolis.ru, 460 office).",
                    delay=2),
    ]
}

buttons = {"Next": "I_c_03_00_dyuster"}
states["I_c_04_01"] = State(content, buttons, callback=set_late)

# I_c_03_00_dyuster Meeting
content = [
    ContentUnit("text", " Also, there are such persons:", delay=1),
    ContentUnit("text", "Head of Department of Student Affairs, Enrollment and Admission - Yuriy Dyuster,", delay=1),
    ContentUnit("photo", photos.urls["dyuster"])
]

buttons = {"Next": "I_c_03_00_stanko"}
states["I_c_03_00_dyuster"] = State(content, buttons)

# I_c_03_00_stanko Meeting
content = [
    ContentUnit("text", "Vice-rector for Education - Tatiana Stanko,", delay=1),
    ContentUnit("photo", photos.urls["stanko"])
]

buttons = {"Next": "I_c_03_00_tormasov"}
states["I_c_03_00_stanko"] = State(content, buttons)

# I_c_03_00_tormasov Meeting
content = [
    ContentUnit("text", "As well as the rector of Innopolis University - Alexander Tormasov.", delay=1),
    ContentUnit("photo", photos.urls["tormasov"]),
    ContentUnit("text", "Together, they wish for all the students successful start in studying at university.")
]

buttons = {"Next": "I_c_03_00_end"}
states["I_c_03_00_tormasov"] = State(content, buttons, callback=check_late)

# I_c_03_00_end Meeting
content = {
    True: [
        ContentUnit("text", "At the end you were explained that the education process is divided in 3 parts.", delay=1),
        ContentUnit("text",
                    "- Theory (lectures);\n- Practice (seminars);\n- Independent work (self-study and homework).",
                    delay=2),
        ContentUnit("text",
                    "And almost always the lecture is followed by the seminar on the same topic to consolidate knowledge.",
                    delay=2),
        ContentUnit("text", "After the meeting you decide to go:")
    ],
    False: [
        ContentUnit("text", "At the end you were explained that the education process is divided in 3 parts.", delay=1),
        ContentUnit("text",
                    "- Theory (lectures);\n- Practice (seminars);\n- Independent work (self-study and homework).",
                    delay=2),
        ContentUnit("text",
                    "And almost always the lecture is followed by the seminar on the same topic to consolidate knowledge.",
                    delay=2),
        ContentUnit("text", "After the meeting you decide to go:")
    ]
}

buttons = {"To canteen": "I_c_04_00",
           "Sleep": "I_c_03_02"}
states["I_c_03_00_end"] = State(content, buttons)

content = {
    True: [
        ContentUnit("text", "After the meeting, you and so get a free dinner... \n"
                            "Let that be a lesson for you"),
        ContentUnit("text", "After the meeting you went to sleep"),
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")

    ],
    False: [
        ContentUnit("text", "After the meeting, you and so get a free dinner... \n"
                            "Let that be a lesson for you"),
        ContentUnit("text", "After the meeting you went to sleep"),
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")

    ]
}
buttons = {"Start next day": "II_a_00_00"}
states["I_c_04_01_end"] = State(content, buttons, callback=check_sex)

# I_c_03_01 Cafeteria before meeting TODO: Delete Comments
content = {
    True: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        ContentUnit("text",
                    "Saying that you'll try to not be late, having a growling stomach, you went to the canteen."),

        # ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
        ContentUnit("text", " After a dinner you went:")
    ],
    False: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        ContentUnit("text",
                    "Saying that you'll try to not be late, having a growling stomach, you went to the canteen."),

        # ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
        ContentUnit("text", " After a dinner you went:")
    ],
}
buttons = {"On the meeting": "I_c_04_01",
           "Sleep": "I_c_03_02"}
states["I_c_03_01"] = State(content, buttons)

# I_c_03_02 Sleep
content = {
    True: [
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")
    ],
    False: [
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")
    ]
}
buttons = {"Start next day": "II_a_00_00"}
states["I_c_03_02"] = State(content, buttons, callback=check_sex)

# I_c_04_00 Cafeteria after meeting TODO: Delete Comments
content = {
    True: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        # ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
        ContentUnit("text", "After a dinner you went to sleep", delay=2),
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")
    ],
    False: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        # ContentUnit("text", "--ИНФОРМАЦИЯ О СТОЛОВОЙ--", delay=2),
        ContentUnit("text", "After a dinner you went to sleep", delay=2),
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")
    ]
}
buttons = {"Start next day": "II_a_00_00"}
states["I_c_04_00"] = State(content, buttons, callback=check_sex)

# II_a_00_00
content = [
    ContentUnit("text", "Наступило утро.", delay=2),
    ContentUnit("text", "Пронзая окна, тёплые лучи солнечного света будят тебя."),
    ContentUnit("text", "Но будильник ещё не звонил, поспать бы ещё…", delay=3),
    ContentUnit("text", "Не спится…", delay=2),
    ContentUnit("text", "Ты встаешь с кровати с чувством бодрости, смешанным со слабостью после вчерашнего дня."),
    ContentUnit("text", "Собравшись на утренние процедуры, ты направляешься в уборную."),
    ContentUnit("text", "Внезапно распахивается дверь неподалёку, и из неё выходит сосед Ваня с полотенцем на плече."),
    ContentUnit("text",
                "Встретившись взглядами, вы замираете на мгновение, как два ковбоя, готовящиеся к перестрелке."),
    ContentUnit("text", "Ты решаешь:")
]
buttons = {"Вежливо пропустить соседа первым в уборную": "II_a_01_00",
           "Ринуться первым в уборную": "II_a_01_01"}
states["II_a_00_00"] = State(content, buttons)

# II_a_00_00_female
content = [
    ContentUnit("text", "Наступило утро.", delay=2),
    ContentUnit("text", "Пронзая окна, тёплые лучи солнечного света будят тебя."),
    ContentUnit("text", "Но будильник ещё не звонил, поспать бы ещё…", delay=3),
    ContentUnit("text", "Не спится…", delay=2),
    ContentUnit("text", "Ты встаешь с кровати с чувством бодрости, смешанным со слабостью после вчерашнего дня."),
    ContentUnit("text", "Собравшись на утренние процедуры, ты направляешься в уборную."),
    ContentUnit("text", "Внезапно распахивается дверь неподалёку, и из неё выходит соседка Яна с полотенцем на плече."),
    ContentUnit("text",
                "Встретившись взглядами, вы замираете на мгновение, как два ковбоя, готовящиеся к перестрелке."),
    ContentUnit("text", "Ты решаешь:")
]
buttons = {"Вежливо пропустить соседку первой в уборную": "II_a_01_00",
           "Ринуться первой в уборную": "II_a_01_01"}
states["II_a_00_00_female"] = State(content, buttons)

# II_a_01_00
content = {
    True: [
        ContentUnit("text", "- Доброе утро, проходи. Я подожду."),
        ContentUnit("text", "- Доброе, спасибо, - ответил сосед, потирая сонные глаза.")
    ],
    False: [
        ContentUnit("text", "- Доброе утро, проходи. Я подожду."),
        ContentUnit("text", "- Доброе, спасибо, - ответила соседка, потирая сонные глаза.")
    ]
}
buttons = {"Дальше": "II_a_02_00"}
states["II_a_01_00"] = State(content, buttons)

# II_a_01_01
content = {
    True: [
        ContentUnit("text", "Сломя голову, крича: «Я первый!», ты летишь в сторону уборную.", delay=2),
        ContentUnit("text",
                    "Сосед остался в дверном проёме, в замешательстве выпучив глаза на твой внезапный марш-бросок.",
                    delay=2)
    ],
    False: [
        ContentUnit("text", "Сломя голову, крича: «Я первая!», ты летишь в сторону уборную.", delay=2),
        ContentUnit("text",
                    "Соседка осталась в дверном проёме, в замешательстве выпучив глаза на твой внезапный марш-бросок.",
                    delay=2)
    ]
}
buttons = {"Дальше": "II_a_02_00"}
states["II_a_01_01"] = State(content, buttons)

# II_a_02_00
content = {
    True: [
        ContentUnit("text", "Закончив гигиенические процедуры, вы вместе направляетесь в столовую на завтрак."),
        ContentUnit("photo", photos.urls["cafeteria"]),
        ContentUnit("text", "- Классно здесь кормят, - сказал ты, уминая вкуснейший завтрак."),
        ContentUnit("text", "- Ага, ещё и бесплатно пока мы на летней школе, - ответил Ваня"),
        ContentUnit("text",
                    "- О, а потом, наверное, кучу денег нужно будет отдавать за всю эту вкуснятину, - пожаловался ты."),
        ContentUnit("text", "- Не то чтобы много… Можно ведь выбрать план питания, подходящий именно тебе.")
    ],
    False: [
        ContentUnit("text", "Закончив гигиенические процедуры, вы вместе направляетесь в столовую на завтрак."),
        ContentUnit("photo", photos.urls["cafeteria"]),
        ContentUnit("text", "- Классно здесь кормят, - сказала ты, уминая вкуснейший завтрак."),
        ContentUnit("text", "- Ага, ещё и бесплатно пока мы на летней школе, - ответила Яна"),
        ContentUnit("text",
                    "- О, а потом, наверное, кучу денег нужно будет отдавать за всю эту вкуснятину, - пожаловалась ты."),
        ContentUnit("text", "- Не то чтобы много… Можно ведь выбрать план питания, подходящий именно тебе.")
    ]
}
buttons = {"Просмотреть планы питания и их стоимость": "II_a_02_00_eating_plan"}
states["II_a_02_00"] = State(content, buttons)

# II_a_02_00_eating_plan
content = [
    ContentUnit("text", "Есть возможность питаться в 5 точках:"),
    ContentUnit("text",
                '- Столовая "ОМС" на 1 этаже Университета\n- Киоск "Wrap and Go" на 1 этаже Университета\n- Столовая на 1 этаже 1-го корпуса\n- Столовая на 1 этаже 4-го корпуса\n- Кафе "CG" на 1 этаже Спортивного комплекса "Иннополис"'),
    ContentUnit("text",
                "Студенты могут выбрать абсолютно любой план питания с возможностью питаться, как 5 дней, так и 7 дней в неделю."),
    ContentUnit("text",
                "В зависимсти от плана питания и количества дней питания в неделю стоимость составляет:"),
    ContentUnit("photo", photos.urls["eating5"]),
    ContentUnit("photo", photos.urls["eating7"])
]
buttons = {"А как выбрать план питания?": "II_a_02_00_student_portal"}
states["II_a_02_00_eating_plan"] = State(content, buttons)

# II_a_02_00_student_portal
content = {
    True: [
        ContentUnit("text", "- Да? Как же? – поинтересовался ты."),
        ContentUnit("text", "- В личном кабинете, очень удобная штука. Можешь найти по этой ссылке."),
        ContentUnit("text", "https://my.university.innopolis.ru/"),
        ContentUnit("text", "Убрав за собой поднос, ты направился на свою первую лекцию в Иннополисе. Круто!")
    ],
    False: [
        ContentUnit("text", "- Да? Как же? – поинтересовалась ты."),
        ContentUnit("text", "- В личном кабинете, очень удобная штука. Можешь найти по этой ссылке."),
        ContentUnit("text", "https://my.university.innopolis.ru/"),
        ContentUnit("text", "Убрав за собой поднос, ты направилась на свою первую лекцию в Иннополисе. Круто!")
    ]
}
buttons = {"Дальше": "II_a_03_00"}
states["II_a_02_00_student_portal"] = State(content, buttons)

# II_a_03_00
content = [
    ContentUnit("text",
                "У лектория уже собралась куча народа. Теперь ребята смотрятся иначе, без вчерашнего багажа, но с ноутбуками, рюкзаками."),
    ContentUnit("text", "На первой лекции вас вводят в курс дела перед началом обучения.")
]
buttons = {"Дальше": "II_a_03_00_1"}
states["II_a_03_00"] = State(content, buttons)

# II_a_03_00_1
content = [
    ContentUnit("text",
                "Начинают с «плохих» новостей, сообщив, что обучение фиксировано в определённых рамках и не прерывается ни на какие государственные или национальные праздники!"),
    ContentUnit("text",
                "А потом сказали, что почти вся необходимая информация по курсам находится в каком-то «Мудле».")
]
buttons = {"Дальше": "II_a_03_00_2"}
states["II_a_03_00_1"] = State(content, buttons)

# II_a_03_00_2
content = {
    True: [
        ContentUnit("text", "- Что, прямо всё-всё там? – спросил кто-то с последних рядов"),
        ContentUnit("text", "- Да, и домашние задания, и лекции, и оценки по курсам. Всё есть на сайте"),
        ContentUnit("text", "https://moodle.university.innopolis.ru"),
        ContentUnit("text", "Хм.… А где же хорошие новости, - подумал ты."),
        ContentUnit("text", "- И, наконец, перед началом лекции хочу сообщить вам ещё кое-что.")
    ],
    False: [
        ContentUnit("text", "- Что, прямо всё-всё там? – спросил кто-то с последних рядов"),
        ContentUnit("text", "- Да, и домашние задания, и лекции, и оценки по курсам. Всё есть на сайте"),
        ContentUnit("text", "https://moodle.university.innopolis.ru"),
        ContentUnit("text", "Хм.… А где же хорошие новости, - подумала ты."),
        ContentUnit("text", "- И, наконец, перед началом лекции хочу сообщить вам ещё кое-что.")
    ]
}
buttons = {"Дальше": "II_a_03_00_3"}
states["II_a_03_00_2"] = State(content, buttons)

# II_a_03_00_3
content = [
    ContentUnit("text", "- С завтрашнего дня открываются различные кружки и клубы по интересам для студентов."),
    ContentUnit("text", "- Ознакомиться со списком можете прямо сейчас, если хотите."),
    ContentUnit("text", "Ты решаешь:"),
]
buttons = {"Просмотреть список клубов": "II_a_04_00",
           "Оставить на потом и приготовиться слушать лекцию": "II_a_05_00",
           }
states["II_a_03_00_3"] = State(content, buttons)

# II_a_04_00 List of Clubs
content = [
    ContentUnit("text",
                "- 3D Modelling\n- Баскетбол\n- Волейбол\n- Занятия гитарой\n- Занятия фортепиано\n- Кендо\n- Клуб видео-съемки и монтажа\n- Клуб Любителей Аниме\n- Настольный теннис\n- Паркур\n- Песочиница инноваций (Innosandbox)\n- Разработка клиент-серверного приложения С#\n- Русская воинская традиция\n- Современные танцы\n- Спортивная робототехника\n- Спортивное программирование (группа начинающих и продолжающих)\n- Французский язык\n- Футбол\n- Хоровое пение\n- AI Community\n- Android Developing\n- Art Club\n- Break Dance\n- Capoeira CDO\n- Chinese\n- CinemaClub\n- CTF\n- Cult of Cormen (CC)\n- Dancing (Латина/Стандарт, Сальса/Бачата)\n- GameDev / Unreal Engine 4\n- Inno Combat Sambo team\n- Mathematics | UI (Под интергралом)\n- Music Club (Гитарник)\n- Photo Club\n- SkateBoardingClub\n- Translators Club")
]
buttons = {"Дальше": "II_a_05_00"}
states["II_a_04_00"] = State(content, buttons)

# II_a_05_00
content = [
    ContentUnit("text", "Выходя из лектория, ты ощущаешь груз новой информации в голове.")
]
buttons = {"А куда дальше?": "II_a_06_00"}
states["II_a_05_00"] = State(content, buttons, callback=check_meeting)

# II_a_06_00
content = [
    ContentUnit("text",
                "Что ж, ты помнишь, как вчера объяснили основу расписания и направляешься с ребятами на практический семинар"),
    ContentUnit("text", "Там тебе удастся лучше усвоить пройденный на лекции материал.")
]
buttons = {"Дальше": "II_a_07_00"}
states["II_a_06_00"] = State(content, buttons)

# II_a_06_01
content = {
    True: [
        ContentUnit("text", "Остановившись на мгновение, ты пытаешься собраться с мыслями.", delay=2),
        ContentUnit("text",
                    "- Чего стоишь, пойдём на семинар, - произнёс Ваня, - там всегда можно уточнить то, что не понял на лекции.")
    ],
    False: [
        ContentUnit("text", "Остановившись на мгновение, ты пытаешься собраться с мыслями.", delay=2),
        ContentUnit("text",
                    "- Чего стоишь, пойдём на семинар, - произнесла Яна, - там всегда можно уточнить то, что не понял на лекции.")
    ]
}
buttons = {"Дальше": "II_a_07_00"}
states["II_a_06_01"] = State(content, buttons)

# II_a_07_00
content = {
    True: [
        ContentUnit("text",
                    '"Уложив по полочкам" новые знания на семинаре, ты почувствовал большое облегчение, и даже радость!'),
        ContentUnit("text",
                    "А чтобы знания окрепли ещё сильнее, студентам выдали домашнюю работу для практики, со словами: «Грызите гранит науки, господа!»"),
        ContentUnit("text", "- Да, умеют они мотивировать, - усмехнулся твой друг."),
        ContentUnit("text", "И вы вместе направились на занятие по английскому языку."),
        ContentUnit("text", "Неудивительно. Университет с англоговорящими профессорами."),
        ContentUnit("text", "Сразу было понятно, что без хороших знаний английского здесь не обойтись.")
    ],
    False: [
        ContentUnit("text",
                    '"Уложив по полочкам" новые знания на семинаре, ты почувствовала большое облегчение, и даже радость!'),
        ContentUnit("text",
                    "А чтобы знания окрепли ещё сильнее, студентам выдали домашнюю работу для практики, со словами: «Грызите гранит науки, господа!»"),
        ContentUnit("text", "- Да, умеют они мотивировать, - усмехнулась твоя подруга."),
        ContentUnit("text", "И вы вместе направились на занятие по английскому языку."),
        ContentUnit("text", "Неудивительно. Университет с англоговорящими профессорами."),
        ContentUnit("text", "Сразу было понятно, что без хороших знаний английского здесь не обойтись.")
    ]
}
buttons = {"Дальше": "II_a_08_00"}
states["II_a_07_00"] = State(content, buttons)

# II_a_08_00
content = {
    True: [
        ContentUnit("text", "Вернувшись в свой номер ты не нашёл там Вани."),
        ContentUnit("text",
                    "Он вернулся позже. Как оказалось, иностранцам при поступлении нужно проводить дополнительную процедуру."),
        ContentUnit("text",
                    "- Мне сказали, что каждый раз при пересечении границы РФ в течение 7 дней с момента приезда нужно приносить паспорт с миграционной картой в 319 кабинет для постановки на миграционный учет, - объяснил Ваня"),
        ContentUnit("text", " - Ну это, конечно, если я не хочу платить огромные штрафы, а я не хочу...")
    ],
    False: [
        ContentUnit("text", "Вернувшись в свой номер ты не нашла там Яны."),
        ContentUnit("text",
                    "Она вернулась позже. Как оказалось, иностранцам при поступлении нужно проводить дополнительную процедуру."),
        ContentUnit("text",
                    "- Мне сказали, что каждый раз при пересечении границы РФ в течение 7 дней с момента приезда нужно приносить паспорт с миграционной картой в 319 кабинет для постановки на миграционный учет, - объяснила Яна"),
        ContentUnit("text", " - Ну это, конечно, если я не хочу платить огромные штрафы, а я не хочу...")
    ]
}
buttons = {"Дальше": "II_a_09_00"}
states["II_a_08_00"] = State(content, buttons)

# II_a_09_00
content = {
    True: [
        ContentUnit("text", "Поздним вечером после первого учебного дня вы с соседом общаетесь за чашкой чая."),
        ContentUnit("text",
                    "- Даа, студентов здесь учат по-настоящему. Столько занятий, да ещё и заданий надавали – пруд пруди, - сказал ты Ване."),
        ContentUnit("text",
                    "- А то! Они своё дело знают, да и студентов не обижают. За все труды награда воздаётся, - услышал ты в ответ."),
        ContentUnit("text",
                    "- Ну, сказанул! «Награда воздаётся»! Как будто они нас манной небесной одарят за учёбу… - удивился ты.")
    ],
    False: [
        ContentUnit("text", "Поздним вечером после первого учебного дня вы с соседкой общаетесь за чашкой чая."),
        ContentUnit("text",
                    "- Даа, студентов здесь учат по-настоящему. Столько занятий, да ещё и заданий надавали – пруд пруди, - сказала ты Яне."),
        ContentUnit("text",
                    "- А то! Они своё дело знают, да и студентов не обижают. За все труды награда воздаётся, - услышала ты в ответ."),
        ContentUnit("text",
                    "- Ну, сказанула! «Награда воздаётся»! Как будто они нас манной небесной одарят за учёбу… - удивилась ты.")
    ]
}
buttons = {"Дальше": "II_a_10_00"}
states["II_a_09_00"] = State(content, buttons)

# II_a_10_00
content = {
    True: [
        ContentUnit("text",
                    "- Манную кашу я не люблю, - сказал Ваня, - но ты слышал, какую они стипендию студентам выдают?"),
        ContentUnit("text", "- Ой, ну удиви меня! – подразнил ты в ответ")
    ],
    False: [
        ContentUnit("text",
                    "- Манную кашу я не люблю, - сказала Яна, - но ты слышала, какую они стипендию студентам выдают?"),
        ContentUnit("text", "- Ой, ну удиви меня! – подразнила ты в ответ")
    ]
}
buttons = {"Дальше": "II_a_11_00"}
states["II_a_10_00"] = State(content, buttons)

# II_a_11_00
content = {
    True: [
        ContentUnit("text",
                    "- Если есть “С” за семестр 12 тысяч, хорошистам платят 18, а если всего 1-2 оценки “В”, а остальные “отлично” -  24."),
        ContentUnit("text", "- А отличники сколько получают? - спросил ты."),
        ContentUnit("text", "- А для отличников все 36. И это только бакалаврам."),
        ContentUnit("text", "Рот у тебя от удивления открылся сам."),
        ContentUnit("text", "- Так что я буду учиться хорошо, потом родителям и себе подарки сделаю"),
        ContentUnit("text", "Ты всё ещё замираешь от удивления."),
    ],
    False: [
        ContentUnit("text",
                    "- Если есть “С” за семестр 12 тысяч, хорошистам платят 18, а если всего 1-2 оценки “В”, а остальные “отлично” -  24."),
        ContentUnit("text", "- А отличники сколько получают? - спросила ты."),
        ContentUnit("text", "- А для отличников все 36. И это только бакалаврам."),
        ContentUnit("text", "Рот у тебя от удивления открылся сам."),
        ContentUnit("text", "- Так что я буду учиться хорошо, потом родителям и себе подарки сделаю"),
        ContentUnit("text", "Ты всё ещё замираешь от удивления.")
    ]
}
buttons = {"Дальше": "II_a_12_00"}
states["II_a_11_00"] = State(content, buttons)

# II_a_12_00
content = {
    True: [
        ContentUnit("text", "- Ладно, это потом, а сейчас – домашка! И тебе советую не лениться, сам понимаешь."),
        ContentUnit("text", "Хлопнувшая дверь на кухне взбодрила тебя."),
        ContentUnit("text", "- Подожди меня! - крикнул ты соседу вслед, стараясь быстрее допить свой чай.")
    ],
    False: [
        ContentUnit("text", "- Ладно, это потом, а сейчас – домашка! И тебе советую не лениться, сама понимаешь."),
        ContentUnit("text", "Хлопнувшая дверь на кухне взбодрила тебя."),
        ContentUnit("text", "- Подожди меня! - крикнула ты соседке вслед, стараясь быстрее допить свой чай.")
    ]
}
buttons = {"Начать новый день": "III_a_00_00"}
states["II_a_12_00"] = State(content, buttons)

# III_a_00_00
content = [ContentUnit("text", "Еще один день в BootCamp,который как всегда начинается с занятий."),
           ContentUnit("text", photos.urls["lecture"]),
           ContentUnit("text",
                       "Во время перерыва между лекцией и семинаром(lab Session), приятель, который ходит с тобой на занятия, спросил: - Я что-то не очень разобрался как тут устроено все в плане преподавания и организации курса.")]
buttons = {"Да и я тоже": "III_a_01_00",
           "Вроде существуют профессора и ТА и…": "III_a_01_01"}
states["III_a_00_00"] = State(content, buttons)

# III_a_01_00
content = [ContentUnit("text", "В разговор вмешивается подруга:"),
           ContentUnit("text",
                       "- Есть профессора. Они ведут лекции, принимают экзамены и отвечают за организацию всего курса"),
           ContentUnit("text", "- А еще есть ТА?"),
           ContentUnit("text",
                       "- Да, Teaching Assistant, он ведет семинары, проверяет домашки и именно к нему нужно обращаться по любым вопросам.")
           ]
buttons = {"А к профессору разве нельзя обращаться с вопросами?": "III_a_02_00",
           "А как выходить с ними на контакт?": "III_a_02_01"}
states["III_a_01_00"] = State(content, buttons)

# III_a_01_01 T
content = [
    ContentUnit("text", "В разговор вмешивается подруга:"),
    ContentUnit("text",
                "- Ага, первые ведут лекции, организовывают всю систему курса и принимают экзамены; а вторые ТА (аббревиатура от Teaching Assistant) ведут семинары, проверяют домашку. И по каким-то проблемам лучше обращаться сначало к ТА.")
]
buttons = {"А с профессором разве нельзя как-нибудь связаться?": "III_a_02_00",
           "Говорили, что у профессоров есть office hours, они для чего?": "III_a_02_02"}
states["III_a_01_01"] = State(content, buttons)

# III_a_02_00
content = [
    ContentUnit("text",
                " - Только если вопрос к ТА остался нерешенным. Вообще у них есть office hours, как раз для решения разных вопросов. Просто не стоит закидывать профессоров письмами на почте или в телеграме, у них и так много дел."),

]
buttons = {"Дальше": "III_b_00_00"}
states["III_a_02_00"] = State(content, buttons)

# III_a_02_01
content = [
    ContentUnit("text",
                "-  Через почту или телеграм. Вообще это зависит от преподавателя: кто-то предпочитает, чтобы ему писал только староста; кто-то отвечает на сообщения только в Office hours."),

]
buttons = {"Дальше": "III_b_00_00"}
states["III_a_02_01"] = State(content, buttons)

# III_a_02_02
content = [
    ContentUnit("text",
                "- Они как раз для решения возникших проблем. Я имею в виду, что не стоит заваливать профессоров письмами, они ведь не могут каждому студенту ответить."),
    ContentUnit("text",
                "Приятель: - Как я понял, это зависит от преподавателя: кто-то предпочитает, чтобы ему писал только староста; кто-то отвечает на сообщения только в Office hours.")
]
buttons = {"Дальше": "III_b_00_00"}
states["III_a_02_02"] = State(content, buttons)

# III_b_00_00
content = {
    True: [
        ContentUnit("text", "Приятель: - Ну теперь хоть понятно. Спасибо, ребята. Пойдем на обед.", delay=3),
        ContentUnit("text", "Обед.", delay=3),
        ContentUnit("text", "Очень много людей, почти нет свободных мест.\n"
                            "Замечаешь столик для двоих, за ним сидит студент.")
    ],
    False: [
        ContentUnit("text", "Приятель: - Ну теперь хоть понятно. Спасибо, ребята. Пойдем на обед.", delay=3),
        ContentUnit("text", "Обед.", delay=3),
        ContentUnit("text", "Очень много людей, почти нет свободных мест.\n"
                            "Замечаешь столик для двоих, за ним сидит студентка.")
    ]
}
buttons = {"Решаешь подсесть": "III_b_01_00",
           "Ищешь свободный столик": "III_b_01_01"}
states["III_b_00_00"] = State(content, buttons)

# III_b_01_00
content = {
    True: [ContentUnit("text", "- Здесь не занято?\n"
                               "- Нет, присаживайся"),
           ContentUnit("text", "Студент: - Ты на BootCamp?"),
           ContentUnit("text", "- Ага."),
           ContentUnit("text",
                       " - Помню и я два года назад только поступил… Во время bootcamp почти не спал, сразу понял, что здесь не так уж просто учиться. Ты сам то город хоть видел?"),

           ],
    False: [
        ContentUnit("text", "- Здесь не занято?\n"
                            "- Нет, присаживайся"),
        ContentUnit("text", "Студентка: - Ты на BootCamp?"),
        ContentUnit("text", "- Ага."),
        ContentUnit("text",
                    " - Помню и я два года назад только поступила… Во время bootcamp почти не спала, сразу поняла, что здесь не так уж просто учиться. Ты сама то город хоть видела?"),

    ]
}
buttons = {"Неа": "III_b_02_00",
           "Только спорткомплекс из окна": "III_b_02_00"}
states["III_b_01_00"] = State(content, buttons)

# III_b_01_01
content = {
    True: [
        ContentUnit("text", "Вот и свободный стол"),
        ContentUnit("text", "Через пару минут к тебе подсаживается другой студент."),
        ContentUnit("text", "- Привет! \n"
                            "- Привет!"),
        ContentUnit("text", " Студент: - Ты на BootCamp?"),
        ContentUnit("text", "- Ага."),
        ContentUnit("text",
                    " -Помню и я два года назад только поступил… Во время bootcamp почти не спал, сразу понял, что здесь не так уж просто учиться. Ты сам то город хоть видел?"),

    ],
    False: [
        ContentUnit("text", "Вот и свободный стол"),
        ContentUnit("text", "Через пару минут к тебе подсаживается другая студентка."),
        ContentUnit("text", "- Привет!"
                            "- Привет!"),
        ContentUnit("text", "Студентка: - Ты на BootCamp?"),
        ContentUnit("text", "- Ага."),
        ContentUnit("text",
                    " - Помню и я два года назад только поступила… Во время bootcamp почти не спала, сразу поняла, что здесь не так уж просто учиться. Ты сама то город хоть видела?"),

    ]
}
buttons = {"Неа": "III_b_02_00",
           "Только спорткомплекс из окна": "III_b_02_00"}
states["III_b_01_01"] = State(content, buttons)

# III_b_02_00
content = {
    True: [
        ContentUnit("text",
                    "- Могу провести небольшую экскурсию, хоть познакомишься с окрестностями. Тебе ведь жить здесь. Меня кстати Миша зовут."),
        ContentUnit("text", "- Меня #name. Тут есть с чем знакомить?"),
        ContentUnit("text", "Спорткомплекс\n"
                            "Часы работы: 7.00 - 23.00\n"
                            "Адрес: г. Иннополис,  ул. Спортивная, д. 107\n"
                            "Здесь есть: бассейн, большой игровой зал, групповые программы, единоборства, настольный теннис и много другое.\n"
                            "Посещение студентам бесплатно!\n"
                            "Ссылка на чат в телеграме: : https://t.me/InnopolisSport"),
        ContentUnit("photo", photos.urls["sport_complex"]),
        ContentUnit("text", "Медцентр/поликлиника\n"
                            "Часы работы:\n"
                            "ПН - ПТ с 10:00 до 16:00\n"
                            "СБ -   	с 09:30 до 15:30\n"
                            "ВС -  выходной\n"
                            "поликлиника - круглосуточно\n"
                            "Сдача анализов: с 9.00 до 11.00 (будние)\n"
                            "Адрес: г. Иннополис, ул. Спортивная, д.301, терминал 1/терминал 2\n"
                            "Здесь: можно получить консультацию врачей-специалистов и необходимое лечение.\n"
                            "Всю актуальную информацию доступна в @Innovlinic_bot \n"
                            "Ссылка на канал в телеграме: https://telegram.me/joinchat/CCS9pz3TH09k7FgaWZ0tqA"),
        ContentUnit("photo", photos.urls["med_center"]),
        ContentUnit("text", "работы аптеки:\n"
                            "ПН-ПТ 9.00-18.00 (без обеда)\n"
                            "СБ 9:00-17:00 (без обеда)\n"
                            "ВС 9:00-16:00 (без обеда)\n"
                            "Адрес: г. Иннополис, ул. Университетская, д.1, кампус №4\n"
                            "Здесь: можно приобрести необходимые препараты"),
        ContentUnit("text", "Почта\n"
                            "Часы работы: 9.00 - 17.00\n"
                            "Выходные дни: суббота, воскресенье\n"
                            "Адрес: ул. Университетская, 7, 1 этаж (здание Технопарка им. А.С. Попова)\n"
                            "Здесь: можно отправить/получить посылки и письма.\n"
                            "Ссылка на чат в Telegram: https://telegram.me/joinchat/Cdg7Gj2lr0wP_l4NMkRReg"),
        ContentUnit("photo", photos.urls["techno_park"]),
        ContentUnit("text", "Город-Курорт “Свияга Хиллз”\n"
                            "Адрес: Верхнеуслонский район, дер. Савиново\n"
                            "Здесь: Летом можно поиграть в гольф, покататься на велосипеде, роликах, сигвеях, катамаранах, лодках и др.\n"
                            "Зимой можно покататься на лыжах и сноуборде.\n"
                            "Круглый год: поиграть в бильярд и боулинг, спеть в караоке.\n"
                            "Для студентов и сотрудников бесплатный прокат скипасов и снаряжения!"),
        ContentUnit("text", "Больше информации можно найти в @InnoHelpBot."),
        ContentUnit("text", "Миша: - Ну так что?"),
    ],
    False: [
        ContentUnit("text",
                    "Могу провести небольшую экскурсию, хоть познакомишься с окрестностями. Тебе ведь жить здесь. Меня кстати Лиза зовут."),
        ContentUnit("text", "- Меня #name. Тут есть с чем знакомить?"),
        ContentUnit("text", "Спорткомплекс \n"
                            "Часы работы: 7.00 - 23.00\n"
                            "Адрес: г. Иннополис,  ул. Спортивная, д. 107\n"
                            "Здесь есть: бассейн, большой игровой зал, групповые программы, единоборства, настольный теннис и много другое.\n"
                            "Посещение студентам бесплатно!\n"
                            "Ссылка на чат в телеграме: : https://t.me/InnopolisSport"),
        ContentUnit("text", "Медцентр/поликлиника\n"
                            "Часы работы: \n"
                            "ПН - ПТ с 10:00 до 16:00\n"
                            "СБ -   	с 09:30 до 15:30\n"
                            "ВС -  выходной\n"
                            "поликлиника - круглосуточно\n"
                            "Сдача анализов: с 9.00 до 11.00 (будние)\n"
                            "Адрес: г. Иннополис, ул. Спортивная, д.301, терминал 1/терминал 2\n"
                            "Здесь: можно получить консультацию врачей-специалистов и необходимое лечение.\n"
                            "Всю актуальную информацию доступна в @Innovlinic_bot\n"
                            "Ссылка на канал в телеграме: https://telegram.me/joinchat/CCS9pz3TH09k7FgaWZ0tqA "),
        ContentUnit("text", "работы аптеки:\n"
                            "ПН-ПТ 9.00-18.00 (без обеда)\n"
                            "СБ 9:00-17:00 (без обеда)\n"
                            "ВС 9:00-16:00 (без обеда)\n"
                            "Адрес: г. Иннополис, ул. Университетская, д.1, кампус №4\n"
                            "Здесь: можно приобрести необходимые препараты"),
        ContentUnit("text", "Почта\n"
                            "Часы работы: 9.00 - 17.00\n"
                            "Выходные дни: суббота, воскресенье\n"
                            "Адрес: ул. Университетская, 7, 1 этаж (здание Технопарка им. А.С. Попова)\n"
                            "Здесь: можно отправить/получить посылки и письма\n"
                            "Ссылка на чат в Telegram: https://telegram.me/joinchat/Cdg7Gj2lr0wP_l4NMkRReg"),
        ContentUnit("text", "Город-Курорт “Свияга Хиллз”\n"
                            "Адрес: Верхнеуслонский район, дер. Савиново\n"
                            "Здесь: Летом можно поиграть в гольф, покататься на велосипеде, роликах, сигвеях, катамаранах, лодках и др.\n"
                            "Зимой можно покататься на лыжах и сноуборде\n"
                            "Круглый год: поиграть в бильярд и боулинг, спеть в караоке\n"
                            "Для студентов и сотрудников бесплатный прокат скипасов и снаряжения!"),
        ContentUnit("text", "Больше информации можно найти в @InnoHelpBot."),
        ContentUnit("text", "Лиза: - Ну так что?"),

    ]
}
buttons = {
    "Было бы здорово.": "III_b_03_00",
    "Наверное, как-нибудь в другой раз.": "III_b_03_01",
    "Времени, как ты говоришь, почти нет, так что я лучше позанимаюсь.": "III_b_03_01"
}
states["III_b_02_00"] = State(content, buttons)

# III_b_03_00

content = {
    True: [
        ContentUnit("text",
                    "Класс! Тогда давай часов в пяя… Совсем забыл сегодня же собрание СА. Так что с прогулкой не выйдет. "),
        ContentUnit("text", "Можешь тоже туда пойти, думаю, будет полезно."),

    ],
    False: [
        ContentUnit("text",
                    "Класс! Тогда давай часов в пяя… Совсем забыла сегодня же собрание СА. Так что с прогулкой не выйдет."),
        ContentUnit("text", "Можешь тоже туда пойти, думаю, будет полезно."),
    ]
}
buttons = {
    "Что-то мне не хочется": "III_b_04_00",
    "СА? Что это?": "III_b_04_01"
}
states["III_b_03_00"] = State(content, buttons)

# III_b_03_01
content = {
    True: [
        ContentUnit("text", "- Ну как хочешь. Я еще собирался на собрание СА. "),
        ContentUnit("text", "Можешь тоже туда пойти, думаю, будет полезно."),
    ],
    False: [
        ContentUnit("text", "Ну как хочешь. Я еще собиралась на собрание СА."),
        ContentUnit("text", "Можешь тоже туда пойти, думаю, будет полезно."),

    ]
}
buttons = {
    "Что-то мне не хочется": "III_b_04_00",
    "СА? Что это?": "III_b_04_01"
}
states["III_b_03_01"] = State(content, buttons)

# III_b_04_00
content = [
    ContentUnit("text",
                "- Ну и зря… Студенческая Ассоциация- полезная штука! Туда можно обращаться, когда нужна помощь в реализации каких-либо идей и вообще почти по любым вопросам"),
    ContentUnit("text", "- Когда, ты говоришь, это собрание?"),
    ContentUnit("text", "Несложно было тебя уговорить! Уже вот-вот начнется. Идем скорее.")
]
buttons = {
    "Отправиться на собрание": "III_c_00_00"
}
states["III_b_04_00"] = State(content, buttons)

# III_b_04_01
content = [
    ContentUnit("text",
                "- Студенческая Ассоциация - это такой орган студенческого самоуправления, участники которого помогают другим студентам. Туда можно обращаться, когда нужна помощь в реализации каких-либо идей и вообще почти по любым вопросам."),
    ContentUnit("text", "- Когда, ты говоришь, это собрание?"),
    ContentUnit("text", "- Уже вот-вот начнется. Идем скорее."),
]
buttons = {
    "Отправиться на собрание": "III_c_00_00"
}
states["III_b_04_01"] = State(content, buttons)

# III_c_00_00
content = [
    ContentUnit("text", "Собрание СА.", delay=3),
    ContentUnit("text", "Председатель Студенческой Ассоциации.\n"
                        "Камилл Гусманов.\n"
                        "Есть свежие идеи или придумал проект, который хочешь реализовать? Или у тебя просто есть замечания, пожелания или нужна помощь? Камилл всегда выслушает и постарается помочь"),
    ContentUnit("photo", photos.urls["kamill"]),
    ContentUnit("text", "Профессионально-академический комитет.\n"
                        "Никита Жучков. \n"
                        "Хочешь поехать на конференцию или олимпиаду? Есть идеи для хакатона?\n"
                        " В этих делах тебе поможет Никита."),
    ContentUnit("photo", photos.urls["nikita"]),
    ContentUnit("text", "Спортивный комитет.\n "
                        "Антон Скударнов.\n"
                        "Любишь спорт? Хочешь поучаствовать в соревнованиях или провести свои? Обращайся к Антону."),
    ContentUnit("photo", photos.urls["anton"]),
    ContentUnit("text", "Культурно-массовый комитет. \n"
                        "Евгений Сорокин.\n"
                        "Евгений поможет найти единомышленников и развить таланты, потому что именно он занимается организацией культурно-массовых мероприятий."),
    ContentUnit("photo", photos.urls["evgeniy"]),
    ContentUnit("text", "Информационный комитет.\n"
                        "Андрей Павленко.\n"
                        "Андрей помогает донести информацию от СА до студентов. Есть замечания, пожелания или помощь, но не знаешь к кому обратиться? Андрей с радостью подскажет и перенаправит к нужным людям."),
    ContentUnit("photo", photos.urls["andrey"]),

]
buttons = {"Покинуть собрание СА": "III_c_01_00"}
states["III_c_00_00"] = State(content, buttons)

# III_c_01_00
content = {
    True: [
        ContentUnit("text", "По пути в комнату ты заметил, что у Мишы есть иностранный акцент. Решаешь спросить:\n"
                            "- Миша, а ты откуда?"),
        ContentUnit("text", "- Из России, а что?"),
        ContentUnit("text", "- Просто у тебя такой акцент, и я подумал…"),
        ContentUnit("text", "Аа, я просто весь прошлый учебный год провел в Китае, видимо поэтому"),
        ContentUnit("text", "Ого, а что ты там делал?"),
        ContentUnit("text", "Учился. В УИ же есть академический обмен, ты не знал?")

    ],
    False: [
        ContentUnit("text", "По пути в комнату ты заметила, что у Лизы есть иностранный акцент. Решаешь спросить:\n"
                            "- Лиза, а ты откуда?"),
        ContentUnit("text", "- Из России, а что?"),
        ContentUnit("text", "- Просто у тебя такой акцент, и я подумала…"),
        ContentUnit("text", "Аа, я просто весь прошлый учебный год провела в Китае, видимо поэтому"),
        ContentUnit("text", "Ого, а что ты там делала?"),
        ContentUnit("text", "Училась. В УИ же есть академический обмен, ты не знала?")
    ]
}
buttons = {
    "А это реально?!": "III_c_02_00",
    "Нет": "III_c_02_01"
}
states["III_c_01_00"] = State(content, buttons)

# III_c_02_00
content = {
    True: [
        ContentUnit("text",
                    "- Вполне реально, всегда мечтал об этом. Подать может каждый обучающийся очно на бакалавра или магистра, при условии того, что ты учишься на оценки не ниже 'B' и английский уровня 'upper-intermediate' и выше. "),
        ContentUnit("text",
                    "- Подробная информация о всем этом есть на сайте университета(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
        ContentUnit("text", "- Окей, спасибо."),
        ContentUnit("text", "- Обращайся. Доброй ночи."),
        ContentUnit("text", "- Пока."),
        ContentUnit("text", "Вот и подошел к концу еще один день.")
    ],
    False: [
        ContentUnit("text",
                    "Вполне реально, всегда мечтала об этом. Подать может каждый обучающийся очно на бакалавра или магистра, при условии того, что ты учишься на оценки не ниже 'В' и английский уровня 'upper-intermediate' и выше. "),
        ContentUnit("text",
                    "- Подробная информация о всем этом есть на сайте университета(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
        ContentUnit("text", "- Окей, спасибо."),
        ContentUnit("text", "- Обращайся. Доброй ночи."),
        ContentUnit("text", "- Пока."),
        ContentUnit("text", "Вот и подошел к концу еще один день.")

    ]
}
buttons = {
    "Начать новый день": "IV_a_00_00"
}
states["III_c_02_00"] = State(content, buttons)

# III_c_02_01
content = [
    ContentUnit("text",
                "- Вот теперь будешь знать. Подать может каждый обучающийся очно на бакалавра или магистра, при условии того, что ты учишься на оценки не ниже 'В' и английский уровня 'upper-intermediate' и выше."),
    ContentUnit("text",
                "- Подробная информация о всем этом есть на сайте университета(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
    ContentUnit("text", "- Окей, спасибо."),
    ContentUnit("text", "- Обращайся. Доброй ночи."),
    ContentUnit("text", "- Пока."),
    ContentUnit("text", "Вот и подошел к концу еще один день.")
]
buttons = {
    "Начать новый день": "IV_a_00_00"
}
states["III_c_02_01"] = State(content, buttons)

# IV_a_00_00
content = [
    ContentUnit("text", "Уже четвертый день пошел, как ты здесь… А, такое чувство будто…")
]
buttons = {
    "Я тут уже месяц нахожусь, не меньше!": "IV_a_01_00",
    "Как будто первый день, не могу привыкнуть до сих пор ко всему…": "IV_a_01_01"
}
states["IV_a_00_00"] = State(content, buttons)

# IV_a_01_00
content = {
    True: [
        ContentUnit("text",
                    "В комнату вбегает Ванек. Вот это действительно позитивный человек!! Всегда шуткует, побольше бы таких людей…"),
        ContentUnit("text", "- Хей! Я смотрю ты проснулся, давай вставай быстрее соня, там новые книги завезли!!"),
        ContentUnit("text", "- Да, я знаю. Пошли."),
        ContentUnit("text",
                    "- Только дай мне минутку, я закажу ее на портале, пока её никто не взял и пойдем. Нужно сначала заказать книгу и, если она не на руках у кого-то, можно сразу пойти и забрать.")
    ],
    False: [
        ContentUnit("text",
                    "В комнату вбегает Яна. Вот это действительно позитивный человек!! Всегда шуткует, побольше бы таких людей…"),
        ContentUnit("text", "- Хей! Я смотрю ты проснулась, давай вставай быстрее соня, там новые книги завезли!!"),
        ContentUnit("text", "- Да, я знаю. Пошли."),
        ContentUnit("text",
                    "- Только дай мне минутку, я закажу ее на портале, пока её никто не взял и пойдем. Нужно сначала заказать книгу и, если она не на руках у кого-то, можно сразу пойти и забрать.")
    ]
}
buttons = {
    "Что за портал?": "IV_a_02_00",
    "Блин, я впервые об этом слышу... Откуда ты все знаешь?!": "IV_a_02_01"
}
states["IV_a_01_00"] = State(content, buttons)

# IV_a_01_01
content = {
    True: [
        ContentUnit("text",
                    "В комнату вбегает Ванек. Вот это действительно позитивный человек!! Всегда шуткует, побольше бы таких людей…"),
        ContentUnit("text",
                    "- Хей! Я смотрю ты проснулся, давай вставай быстрее соня, там новые книги завезли!!  Я хочу взять «Алгоритмы. Построение и анализ.Introduction to Algorithms.». Она самая читаемая, пока учеба не началась надо бы поизучать."),
        ContentUnit("text", "- Откуда ты знаешь, что она самая читаемая??"),
        ContentUnit("text",
                    "- Ты что до сих пор не вкурсе… Просто заходишь на портал библиотеки, очень удобный, между прочим, там показано какие книги есть, какие уже взяли. Все книги разбиты по категориям. Очень удобно!  Книги ты там же заказываешь."),

    ],
    False: [
        ContentUnit("text",
                    "В комнату вбегает Яна. Вот это действительно позитивный человек!! Всегда шуткует, побольше бы таких людей…"),
        ContentUnit("text",
                    "- Хей! Я смотрю ты проснулась, давай вставай быстрее соня, там новые книги завезли!!  Я хочу взять «Алгоритмы. Построение и анализ.Introduction to Algorithms.». Она самая читаемая, пока учеба не началась надо бы поизучать."),
        ContentUnit("text", "- Откуда ты знаешь, что она самая читаемая??"),
        ContentUnit("text",
                    "- Ты что до сих пор не вкурсе… Просто заходишь на портал библиотеки, очень удобный, между прочим, там показано какие книги есть, какие уже взяли. Все книги разбиты по категориям. Очень удобно!  Книги ты там же заказываешь."),

    ]
}
buttons = {
    "Что за портал?": "IV_a_02_00",
    "Блин, я впервые об этом слышу... Откуда ты все знаешь?!": "IV_a_02_01"
}
states["IV_a_01_01"] = State(content, buttons)

# IV_a_02_00
content = [
    ContentUnit("text", "portal.university.innopolis.ru/reading_hall/", delay=3),
    ContentUnit("text", "- Ладно, буду иметь в виду. Спасибо."),
    ContentUnit("text",
                "- Тогда поторопись! Спишь как сурок до обеда, даже лекции тебе не помеха! Не советую так тебе в течение семестра делать."),

]
buttons = {
    "Дальше": "IV_b_00_00"
}
states["IV_a_02_00"] = State(content, buttons)

# IV_a_02_01
content = [
    ContentUnit("text",
                "- А вот надо чатики в telegram-е хоть иногда просматривать, там много полезного можно прочесть и свою официальную почту чаще проверять (улыбнулся). У нас у каждого есть свой почтовый ящик @innopolis.ru. Он, кстати, в будущем будет использоваться для связи с профессорами. Всё должно быть официально, мой друг, официально."),
    ContentUnit("text", "- Ладно, буду иметь в виду. Спасибо."),
    ContentUnit("text",
                "- Тогда поторопись! Спишь как сурок до обеда, даже лекции тебе не помеха! Не советую так тебе в течение семестра делать."),

]
buttons = {
    "Дальше": "IV_b_00_00"
}
states["IV_a_02_01"] = State(content, buttons)

# IV_b_00_00
content = [
    ContentUnit("text", "Выходя из библиотеки:"),
    ContentUnit("text", "- Ну что, пошли обедать?"),
    ContentUnit("text", "- Пойдем", delay=3),
    ContentUnit("text", "В столовой:"),
    ContentUnit("text",
                "Хм, знакомое лицо за столом сидит. Ха, это же Паша, который был у меня на отборах сопровождающим!"),
    ContentUnit("text", "- Пошли сядем вон туда. Это Паша, может ты его знаешь, он был у меня на отборах. Волонтерил"),
    ContentUnit("text", "- Пошли"),
    ContentUnit("text", "- Привет, Паш, как дела?"),
    ContentUnit("text",
                "- О, какие люди, тебя я помню, соня, потому что любишь поспать и везде опаздываешь из-за этого (Все рассмеялись). Дела у меня отлично, наконец-то поменял план питания."),

]
buttons = {
    "Можно выбрать план на 5 или 7 дней, верно?": "IV_b_01_00",
    "А как ты его поменял?": "IV_b_01_01",
}
states["IV_b_00_00"] = State(content, buttons)

# IV_b_01_00
content = [
    ContentUnit("text",
                "- Конечно можно, тебя что насильно тут будут 7 раз в неделю кормить? Вообще все планы питания ты увидишь, когда выбирать будешь. Правда поменять можно только раз в месяц."),
    ContentUnit("text", "- Где увижу?"),
    ContentUnit("text", "- В личном кабинете: my.university.innopolis.ru"),
    ContentUnit("text",
                "- Спасибо! Слушай, у меня вопрос, я так понимаю здесь домашки не передаются из рук в руки от студента к преподавателю. Как это все вообще работает?"),
    ContentUnit("text",
                "- Все очень просто. Есть такая штука, как мудл: moodle.university.innopolis.ru  Туда заливаются домашки, там ты свои оценки можешь посмотреть, ну и там же записываются на курсы по выбору, если у вас такие будут."),

]
buttons = {"Дальше": "IV_c_00_00"}
states["IV_b_01_00"] = State(content, buttons)

# IV_b_01_01
content = [
    ContentUnit("text", "- В личном кабинете: my.university.innopolis.ru"),
    ContentUnit("text",
                "- У меня еще один вопрос. Я знаю, что тут вроде не работает правило «От сессии до сессии живут студенты весело». И что, соответственно, экзамены распределены по всему семестру."),
]
buttons = {
    "А как вообще узнать, когда они, эти экзамены?": "IV_b_02_00",
    "Сколько они весят от общей оценки?": "IV_b_02_00",
}
states["IV_b_01_01"] = State(content, buttons)

# IV_b_02_00
content = [
    ContentUnit("text",
                "- Есть такая штука, как мудл: moodle.university.innopolis.ru  Там будут лежать ответы на все твои вопросы, не переживай.")
]
buttons = {
    "Дальше": "IV_c_00_00"
}
states["IV_b_02_00"] = State(content, buttons)

# IV_c_00_00
content = [
    ContentUnit("text",
                "Вечером все собрались у вас в комнате, поболтать и поесть пиццу. Оказывается, тут есть аж 2 места, где можно ее заказать."),
    ContentUnit("text",
                "Ты замечаешь, что одна из ваших подруг сидит в толстовке с надписью “Innopolis University”"),
    ContentUnit("photo", photos.urls["hoody"]),
    ContentUnit("text", "Офигенная толстовка, кстати говоря. Тоже такую хочу! Ты спрашиваешь:")
]
buttons = {
    "Где ты такую достала?": "IV_c_01_00",
    "Ты обокрала университет? (указывая на толстовку)": "IV_c_01_01"
}
states["IV_c_00_00"] = State(content, buttons)

# IV_c_01_00
content = [
    ContentUnit("text",
                "- Что достала? Ах, ты про толстовку. Ну я просто помогла пару раз отделу поддержки и развития студентов, поволонтерила на кое-каких мероприятиях, ну и, конечно, ходила на “Activities”.  И voilà – уже накопила Иннопоинты на толстовочку."),
    ContentUnit("text", "- И сколько иннопоинтов стоит? И откуда ты узнала, что тебе их хватает?"),
    ContentUnit("text",
                "- Ну ты реально вообще ничего не читаешь, что приходит нам, в рассылках (рассмеялась она). Эта, по-моему, 1800 иннопоинтов, а посмотреть сколько их у тебя сейчас можно на «юисе» uis.university.innopolis.ru/innopoints/products"),
    ContentUnit("text", "- Впервые слышу…"),
    ContentUnit("text", "В диалог вмешался roommate:"),
    ContentUnit("text",
                "- Вы знали, что иннопоинты студенты придумали и разработали эту идею вместе с отделом по поддержке и развитию студентов. Вот так вот. Если бы тогда не возникла у них такая идея, не было бы сейчас иннопоинтов. Минутка истории от меня."),

]
buttons = {"Спросить откуда инфа.": "IV_c_02_00",
           "Это очень утомительно весь день что-то у кого-то спрашивать. И вообще я спать хочу.": "IV_c_02_01"}
states["IV_c_01_00"] = State(content, buttons)

# IV_c_01_01
content = [
    ContentUnit("text",
                "- Ахаха! Нет! Я работала, не покладая рук, волонтерила и все такое. Вот и накопила себе на толстовку."),
    ContentUnit("text", "- И сколько стоит?"),
    ContentUnit("text", "- По-моему, 1800 иннопоинтов."),
    ContentUnit("text", "- А как вообще заказывать и получать вещи за иннопоинты?"),
    ContentUnit("text",
                "- На «юисе» uis.university.innopolis.ru/innopoints/products   Я там же и заявку на получение иннопоинтов подавала. Вообще на самом «юисе» uis.university.innopolis.ru много информации есть, там и новости пишут, например, про музыкальную комнату. "
                "- Блин, круто, тоже заработаю себе на такую.")
]
buttons = {"Спросить откуда инфа.": "IV_c_02_00",
           "Это очень утомительно весь день что-то у кого-то спрашивать. И вообще я спать хочу.": "IV_c_02_01"}
states["IV_c_01_01"] = State(content, buttons)
# IV_c_02_00
content = [
    ContentUnit("text", "- А это ты откуда знаешь?"),
    ContentUnit("text", "- Секрет фирмы. Hint: общайся с людьми – это бывает полезно.")
]
buttons = {"Отправиться спать": "IV_c_02_01"}
states["IV_c_02_00"] = State(content, buttons)

# IV_c_02_01
content = [
    ContentUnit("text", "Ты ушел в свою комнату, завалился на кровать и уснул")
]
buttons = {"Начать новый день": "V_a_00_00"}
states["IV_c_02_01"] = State(content, buttons)

# V_a_00_00
content = [
    ContentUnit("text", "Наступил твой 5ый день в летней школе."),
    ContentUnit("text", "Ты просыпаешься ранним утром с улыбкой на лице."),
    ContentUnit("text", "Ничего не предвещает беды."),
    ContentUnit("text", "Хм… Что у нас сегодня?"),
]
buttons = {
    "Собрание студентов": "V_a_01_00",
    "Экзамены": "V_a_01_01"
}
states["V_a_00_00"] = State(content, buttons)

# V_a_01_00
content = {
    True: [
        ContentUnit("text", "Точно! Собрание. Погоди, какое собрание…"),
        ContentUnit("text", "А! Нет! Экзамены, ну конечно. Стоп. Экзамены!!!"),
        ContentUnit("text", "Ну ничего, ты готовился. Всё должно пройти отлично."),
        ContentUnit("text",
                    "Утренние процедуры. Открыв кран, ты получаешь внезапный мощный поток воды. Окатив половину комнаты вместе с тобой, вода также внезапно заканчивается. Затем следуют звуки звериного рыка и хлюпанье из крана."),
    ],
    False: [
        ContentUnit("text", "Точно! Собрание. Погоди, какое собрание…"),
        ContentUnit("text", "А! Нет! Экзамены, ну конечно. Стоп. Экзамены!!!"),
        ContentUnit("text", "Ну ничего, ты готовилась. Всё должно пройти отлично."),
        ContentUnit("text",
                    "Утренние процедуры. Открыв кран, ты получаешь внезапный мощный поток воды. Окатив половину комнаты вместе с тобой, вода также внезапно заканчивается. Затем следуют звуки звериного рыка и хлюпанье из крана."),
    ]
}
buttons = {
    "Закрыть кран": "V_a_02_00"
}
states["V_a_01_00"] = State(content, buttons)

# V_a_01_01
content = {
    True: [
        ContentUnit("text", "Вспомнил! Сегодня же экзамены!"),
        ContentUnit("text", "Ну ничего, ты готовился. Всё должно пройти отлично."),
        ContentUnit("text",
                    "Утренние процедуры. Открыв кран, ты получаешь внезапный мощный поток воды. Окатив половину комнаты вместе с тобой, вода также внезапно заканчивается. Затем следуют звуки звериного рыка и хлюпанье из крана."),

    ],
    False: [
        ContentUnit("text", "Вспомнила! Сегодня же экзамены!"),
        ContentUnit("text", "Ну ничего, ты готовилась. Всё должно пройти отлично."),
        ContentUnit("text",
                    "Утренние процедуры. Открыв кран, ты получаешь внезапный мощный поток воды. Окатив половину комнаты вместе с тобой, вода также внезапно заканчивается. Затем следуют звуки звериного рыка и хлюпанье из крана."),

    ]
}
buttons = {
    "Закрыть кран": "V_a_02_00"
}
states["V_a_01_01"] = State(content, buttons)

# V_a_02_00
content = {
    True: [
        ContentUnit("text", "Ты закрываешь кран... Открываешь снова. Вода пошла нормально."),
        ContentUnit("text", "Закончив процедуры и позавтракав, ты пошёл на первый экзамен."),
        ContentUnit("text",
                    "Вам объясняют, что под экзаменом с «закрытыми книгами» (closed book) имеется в виду экзамен с закрытыми учебниками, записями, телефонами и, в общем, всем закрытым.… Кроме собственных глаз."),
        ContentUnit("text",
                    "За соблюдением правил следит профессор. ТА не брезгуют ходить по аудитории и не упускают из виду ни единого студента."),
    ],
    False: [
        ContentUnit("text", "Ты закрываешь кран... Открываешь снова. Вода пошла нормально."),
        ContentUnit("text", "Закончив процедуры и позавтракав, ты пошла на первый экзамен."),
        ContentUnit("text",
                    "Вам объясняют, что под экзаменом с «закрытыми книгами» (closed book) имеется в виду экзамен с закрытыми учебниками, записями, телефонами и, в общем, всем закрытым.… Кроме собственных глаз."),
        ContentUnit("text",
                    "За соблюдением правил следит профессор. ТА не брезгуют ходить по аудитории и не упускают из виду ни единого студента."),
    ]
}
buttons = {
    "Ну и ладно. Напишу самостоятельно.": "V_a_03_00",
    "Ну, друзья в беде не оставят": "V_a_03_01"
}
states["V_a_02_00"] = State(content, buttons)

# V_a_03_00
content = [
    ContentUnit("text", "И правильно, ведь иначе…"),
    ContentUnit("text",
                "Всем студентам объяснили, что списывание также карается немедленным провалом экзамена, как и любое другое нарушение."),
    ContentUnit("text", "Ты спокойно (или не очень) садишься и приступаешь к экзамену."),
    ContentUnit("text",
                "Через 1,5 часа напряженной работы вы сдаете бланки, и вам напоминают, что оценки вы сможете узнать позже в Moodle."),
    ContentUnit("text",
                "- А в третьем номере текст задания был недостаточно ясно сформулирован, - возмущается кто-то из студентов."),
    ContentUnit("text", " - Да!.. Правда!.. Точно... – отзываются другие."),
    ContentUnit("text", "- Хорошо, мы с ТА пересмотрим его ещё раз, но пока ничего не обещаем, - отвечает профессор."),
    ContentUnit("text",
                "А для всех, кто посчитают несправедливой свою оценку и пожелают её оспорить, после объявления результатов у нас проводится апелляция, – добавил ТА."),
    ContentUnit("text", "Ребята разошлись кто куда. До следующего экзамена (по английскому) остается 2 часа."),
    ContentUnit("text", "Ты вспоминаешь, что твои записи по предмету лежат в комнате и направляешься туда."),
    ContentUnit("text", "Зайдя в комнату, ты забираешь тетрадь со стола и направляешься к выходу."),
    ContentUnit("text",
                "Тебя останавливает странный звук, доносящийся из уборной. Но ведь кроме тебя в комнате никого нет…"),
    ContentUnit("text",
                "Открыв дверь в ванную, ты видишь картину маслом. Со смесителя сорвало кран, и вода хлещет до самого потолка."),
    ContentUnit("text", "Твои ноги уже стоят в луже, а по спине бегают мурашки. Что же сделать?"),
]
buttons = {
    "Написать в Телеграме соседу": "V_a_04_00",
    "Выбежать и попросить помощи": "V_a_04_01"
}
states["V_a_03_00"] = State(content, buttons)

# V_a_03_01
content = [
    ContentUnit("text", "Хотя эта идея быстро вылетела из головы, когда…"),
    ContentUnit("text",
                "Всем студентам объяснили, что списывание также карается немедленным провалом экзамена, как и любое другое нарушение."),
    ContentUnit("text", "Ты спокойно (или не очень) садишься и приступаешь к экзамену."),
    ContentUnit("text",
                "Через 1,5 часа напряженной работы вы сдаете бланки, и вам напоминают, что оценки вы сможете узнать позже в Moodle."),
    ContentUnit("text",
                "- А в третьем номере текст задания был недостаточно ясно сформулирован, - возмущается кто-то из студентов."),
    ContentUnit("text", " - Да!.. Правда!.. Точно... – отзываются другие."),
    ContentUnit("text", "- Хорошо, мы с ТА пересмотрим его ещё раз, но пока ничего не обещаем, - отвечает профессор."),
    ContentUnit("text",
                "А для всех, кто посчитают несправедливой свою оценку и пожелают её оспорить, после объявления результатов у нас проводится апелляция, – добавил ТА."),
    ContentUnit("text", "Ребята разошлись кто куда. До следующего экзамена (по английскому) остается 2 часа."),
    ContentUnit("text", "Ты вспоминаешь, что твои записи по предмету лежат в комнате и направляешься туда."),
    ContentUnit("text", "Зайдя в комнату, ты забираешь тетрадь со стола и направляешься к выходу."),
    ContentUnit("text",
                "Тебя останавливает странный звук, доносящийся из уборной. Но ведь кроме тебя в комнате никого нет…"),
    ContentUnit("text",
                "Открыв дверь в ванную, ты видишь картину маслом. Со смесителя сорвало кран, и вода хлещет до самого потолка."),
    ContentUnit("text", "Твои ноги уже стоят в луже, а по спине бегают мурашки. Что же сделать?"),
]
buttons = {
    "Написать в Телеграме соседу": "V_a_04_00",
    "Выбежать и попросить помощи": "V_a_04_01"
}
states["V_a_03_01"] = State(content, buttons)

# V_a_04_00
content = {
    True: [
        ContentUnit("text",
                    "Сосед говорит, что тебе нужно написать администратору корпуса, чтобы он отправил техническую заявку. А по заявке приходят специалисты и всё чинят."),
        ContentUnit("text", "Ссылка на Телеграм администраторов 'Hotel Uni Reception':@hoteluni")
    ],
    False: [
        ContentUnit("text",
                    "Соседка говорит, что тебе нужно написать администратору корпуса, чтобы он отправил техническую заявку. А по заявке приходят специалисты и всё чинят."),
        ContentUnit("text", "Ссылка на Телеграм администраторов 'Hotel Uni Reception':@hoteluni")

    ]
}
buttons = {
    "Написать администрации": "V_a_05_00"
}
states["V_a_04_00"] = State(content, buttons)

# V_a_04_01
content = [
    ContentUnit("text", "Выбежав в коридор, ты смотришь по сторонам"),
    ContentUnit("text", "Никого! Ну конечно, все на экзаменах!"),
    ContentUnit("text", "Надо всё-таки срочно попросить у соседа помощи")
]
buttons = {
    "Написать в Телеграме соседу": "V_a_04_00"
}
states["V_a_04_01"] = State(content, buttons)

# V_a_05_00
content = [
    ContentUnit("text",
                "Написали, что вызвали сантехника. Также тебе сказали перекрыть кран, повернув вентиль под раковиной."),
    ContentUnit("text", "Ну конечно! Воду перекрыть!"),
    ContentUnit("text", "Ты быстро находишь вентиль и поворачиваешь на 90 градусов."),
    ContentUnit("text", "Струя фонтана быстро идёт на спад."),
    ContentUnit("text", "Быстро найдя тряпку, ты начинаешь собирать воду."),
    ContentUnit("text", "Через 5 минут приходит рабочий, а ты убегаешь в университет."),
    ContentUnit("text", "Ну и денек! Ладно, экзамены, но ещё и такие приключения!"),
    ContentUnit("text", "Хорошо, что Hotel Uni Reception быстро отреагировал."),
    ContentUnit("text", "Вечером того же дня ты рассказываешь соседям эпичную историю с водопадами и водоворотами…"),
    ContentUnit("text", "Ну а что? Можно и приукрасить немножко иногда. =)"),
    ContentUnit("text", "Да, оказывается, неспроста утром кран рычал на тебя."),
    ContentUnit("text", "После просмотра фильма вам с ребятами приходят новости в Moodle."),
    ContentUnit("text", "Посмотрев результаты, ты видишь оценку."),
    ContentUnit("text", " Оценка А."),
    ContentUnit("text", "Вот так закончилась эта сумасшедшая пятница."),
]
buttons = {
    "Начать новый день": "VI_a_00_00",
    "Начать с начала": "I_a_00_00"
}
states["V_a_05_00"] = State(content, buttons)

# VI_a_00_00
content = {
    True: [
        ContentUnit("text", "Вот и наступил шестой день в BootCamp"),
        ContentUnit("text", "Ваня уже как всегда не спит."),
        ContentUnit("text",
                    "- Там уже вовсю идет подготовка к Ethno Village, а ты еще только встаешь с кровати! Я уже несколько часов на ногах!"),

    ],
    False: [
        ContentUnit("text", "Вот и наступил шестой день в BootCamp"),
        ContentUnit("text", "Яна уже как всегда не спит."),
        ContentUnit("text",
                    "- Там уже вовсю идет подготовка к Ethno Village, а ты еще только встаешь с кровати! Я уже несколько часов на ногах!"),
    ]
}
buttons = {
    "А? Что?": "VI_a_01_00",
    "А ты что тоже участвуешь?": "VI_a_01_01"
}
states["VI_a_00_00"] = State(content, buttons)

# VI_a_01_00
content = [
    ContentUnit("text",
                "- Доброе утро! Сегодня же мероприятие, ребята будут рассказывать про свои города и регионы, а я помогаю с организацией."),
    ContentUnit("text", "- Неужели это так весело? Почему ты помогаешь?"),
    ContentUnit("text",
                "- Да! Тем более за это дают иннопоинты, мне так понравилась толстовка, уже начинаю на нее копить!"),

]
buttons = {
    "Много на что их можно потратить?": "VI_a_02_00",
    "Эти иннопоинты только за волонтерство дают?": "VI_a_02_01",
    "Аа, вспомнил, видели девушку в толстовке, она говорила что-то про это.": "VI_a_02_00"
}
states["VI_a_01_00"] = State(content, buttons)

# VI_a_01_01
content = [
    ContentUnit("text",
                "- Да! Хочу накопить на ужин с профессором, по-моему, это очень интересно! Стоит много, поэтому начинаю копить как можно раньше."),
    ContentUnit("text", "- Что?! Ты хочешь сводить профессора на ужин?! Тебе платят за помощь? Ничего не понимаю…"),
    ContentUnit("text",
                "- Хаха, нет, конечно. За волонтерство на мероприятиях дают иннопоинты, их можно обменять на ужин с профессором.")

]
buttons = {
    "Много на что их можно потратить?": "VI_a_02_00",
    "Эти иннопоинты только за волонтерство дают?": "VI_a_02_01",
    "Аа, вспомнил, видели девушку в толстовке, она говорила что-то про это.": "VI_a_02_00"
}
states["VI_a_01_01"] = State(content, buttons)

# VI_a_02_00
content = [
    ContentUnit("text",
                "- Ага. Там куча сувениров с символов университета: толстовки, кружки, рюкзаки и еще много всего. Еще можно обменять на сертификаты партнеров УИ."),
    ContentUnit("text", "- Пора на завтрак, соня!"),
]
buttons = {
    "Отправиться на завтрак": "VI_b_00_00"
}
states["VI_a_02_00"] = State(content, buttons)

# VI_a_02_01
content = [
    ContentUnit("text",
                "- Нет. За любую активность, например за участие в хакатонах и спортивных соревнованиях, за публичные статьи и научные исследования, или участие в других внеакадемических активностях."),
    ContentUnit("text", "- Пора на завтрак, соня!"),
]
buttons = {
    "Отправиться на завтрак": "VI_b_00_00"
}
states["VI_a_02_01"] = State(content, buttons)

# VI_b_00_00
content = [
    ContentUnit("text", "В столовой:"),
    ContentUnit("text", "Слышишь, как два студента о чем-то довольно бурно спорят.."),
    ContentUnit("text",
                "- А мне нравится жить в пятерке! Отдельная просторная кухня и ванна! Если кто-то спит можно не мешая ему сидеть на кухне. И намного веселее, всегда найдется кто поможет с домашкой."),
    ContentUnit("text",
                "- Да ну, очередь в туалет наверное, постоянно… Зато я точно знаю, чьи продукты в холодильнике, если они не мои. Стоит, конечно, чуток дороже. Пятиместка - примерно 2100 руб./месяц, а двухместка - 2400 рублей/месяц."),
    ContentUnit("text", "- Значит, все-таки переезжаешь в двушку?"),
    ContentUnit("text", "- Да, сегодня же пойду к администратору корпуса и напишу заявление."),
    ContentUnit("text",
                "- А я наверное в квартиру в Залесный или в Казань перееду, кота из дома заберу, а то ведь с ним в общежитии нельзя."),
    ContentUnit("text", "..."),
    ContentUnit("text", "- Приятного аппетита."),
    ContentUnit("text", "- Спасибо, тебе тоже."),
    ContentUnit("text",
                "- Я вот уже подумываю, куда поехать следующим летом! Ты не знаешь когда заканчивается весенний семестр?")
]
buttons = {
    "Кажется, 14 мая": "VI_b_01_00",
    "Нет, не знаю": "VI_b_01_01",
}
states["VI_b_00_00"] = State(content, buttons)

# VI_b_01_00
content = [
    ContentUnit("text", "- Да точно! Длинные каникулы выходят… совсем забыл еще же стажировка."),
    ContentUnit("text", "- И когда она будет? И что это вообще такое?"),
    ContentUnit("text",
                "- Точную информацию нам должны сказать к концу года, думаю. Поэтому не стоит пока делать точные планы, хотя бы начало лета постараться оставить свободным. Я знаю, что они подразделяются на административные и научные, и в компании мы можем идти только после второго курса."),

]
buttons = {
    "Понятно": "VI_b_02_00",
    "А чем отличаются административные и научные?": "VI_b_02_01"
}
states["VI_b_01_00"] = State(content, buttons)

# VI_b_01_01
content = [
    ContentUnit("text", "- Кажется в середине мая… Да точно 14 мая последний день, только ведь там еще стажировка."),
    ContentUnit("text", "- И когда она будет? И что это вообще такое?"),
    ContentUnit("text",
                "- Точную информацию нам должны сказать к концу года, думаю. Поэтому не стоит пока делать точные планы, хотя бы начало лета постараться оставить свободным. Я знаю, что они подразделяются на административные и научные, и в компании мы можем идти только после второго курса."),

]
buttons = {
    "Понятно": "VI_b_02_00",
    "А чем отличаются административные и научные?": "VI_b_02_01"
}
states["VI_b_01_01"] = State(content, buttons)

# VI_b_02_00
content = [
    ContentUnit("text", "После завтрака у вас был только один вариант:")
]
buttons = {
    "Отправиться на праздник": "VI_c_00_00"
}
states["VI_b_02_00"] = State(content, buttons)

# VI_b_02_01
content = [
    ContentUnit("text",
                "При административной делают разные проекты для университета. А научные для того чтобы прокачаться в какой-то определенной области, например, если тебе нравится робототехника, можно пойти на стажировку в лабораторию к профессору Мавридису. Мне студенты рассказали."),

]
buttons = {
    "Ясно.": "VI_b_02_00"
}
states["VI_b_02_01"] = State(content, buttons)

# VI_c_00_00
content = [
    ContentUnit("text", "На празднике:"),
    ContentUnit("text", "Вот уже начался праздник."),
    ContentUnit("text",
                "В читальном зале собралось много людей: некоторые в национальной одежде, кто-то принес национальные угощения."),
    ContentUnit("text", "Кажется здесь должно быть весело, пойдем туда?"),
]
buttons = {
    "И мне так кажется": "VI_c_01_00",
    "И часто тут такие мероприятия?": "VI_c_01_00"
}
states["VI_c_00_00"] = State(content, buttons)

# VI_c_01_00
content = [
    ContentUnit("text", "Стоящий рядом студент: - Вас должно обрадовать, что здесь праздник почти каждый день"),
    ContentUnit("text", "Halloween(Октябрь)"),
    ContentUnit("photo", photos.urls["halloween"]),
    ContentUnit("text", "Студенческий Новый год (декабрь)"),
    ContentUnit("photo", photos.urls["new_year"]),
    ContentUnit("text", "День Студента (январь)"),
    ContentUnit("photo", photos.urls["student_day"]),
    ContentUnit("text", "День всех влюбленных(февраль)"),
    ContentUnit("photo", photos.urls["valentine_day"]),
    ContentUnit("text", "23/8(март)"),
    ContentUnit("photo", photos.urls["23/8"]),
    ContentUnit("text", "Independents Activities Weekend (апрель)"),
    ContentUnit("photo", photos.urls["IAW"]),
    ContentUnit("text", "Slipper of the Year(май)"),
    ContentUnit("photo", photos.urls["slippers"]),
    ContentUnit("text", "Подошел к концу один из самых веселых дней в BootCamp.")
]
buttons = {
    "Начать новый день": "VII_a_00_00"
}
states["VI_c_01_00"] = State(content, buttons)

# VII_a_00_00
content = [
    ContentUnit("text", "Встретившись с друзьями утром…"),
    ContentUnit("text", "- Хэй, доброе утро! Сегодня выходной! Так не хочется сидеть в кампусе, пойдемте погуляем."),
    ContentUnit("text",
                "- Можно. Ну что, куда пойдем? Я лично хочу пойти посмотреть, что за место для барбекю тут есть."),
    ContentUnit("text", "- А я хотела купить пару книг в книжном…"),
]
buttons = {
    "Пойти посмотреть место для барбекю": "VII_a_01_00",
    "Пойти в книжный магазин": "VII_a_01_01"
}
states["VII_a_00_00"] = State(content, buttons)

# VII_a_01_00
content = [
    ContentUnit("text",
                "- Ну давайте тогда разделимся, мы посмотрим где тут шашлыки можно жарить, а вы с Викой можете пока сходить в книжный, потом встретимся в Пиццерии 'Cacio e Vino'"),
    ContentUnit("text", "- Давайте"),
    ContentUnit("text", "Пару минут спустя…"),
    ContentUnit("text",
                "- А где находится то это место? И как вообще там жарить шашлыки, нужно с кем-то договориться же наверняка."),
    ContentUnit("text",
                "- Парень со второго курса сказал, что в чатике просто пишешь, бронируешь, говоришь, я на это время занял и все. Мы уже почти пришли, оно за Жилым Комплексом, как Бахетле, только чуть-чуть дальше."),
    ContentUnit("photo", photos.urls["mangal"]),
    ContentUnit("text", "Ознакомвшись с местом и заприметив его на будущее, Вы:")
]
buttons = {
    "Отправились в пиццерию": "VII_b_00_00",
}
states["VII_a_01_00"] = State(content, buttons)

# VII_a_01_01 TODO: Add Photo
content = [
    ContentUnit("text",
                "- Ну давайте тогда разделимся, мы купим книги, а вы можете пока сходить посмотреть место для барбекю, потом встретимся в Пиццерии 'Cacio e Vino'"),
    ContentUnit("text", "По пути в книжный…"),
    ContentUnit("text", "- А что ты купить хочешь там?"),
    ContentUnit("text",
                "- Там вроде завезли новые книги по программированию, хочу посмотреть, может куплю. А так там в общем-то много чего можно купить почитать для души. Вон он уже, кстати, отсюда видно, «Дом Книги»."),
    ContentUnit("text", "#Здесь фото магазина"),
    ContentUnit("text", "Походив по магазину и заприметив его на будущее, Вы:")
]
buttons = {
    "Отправились в пиццерию": "VII_b_00_00",
}
states["VII_a_01_01"] = State(content, buttons)

# VII_b_00_00 TODO: Add Photo
content = [
    ContentUnit("text", "В пиццерии по адресу: ул. Спортивная, 100"),
    ContentUnit("text", "#Здесь фото снаружи"),
    ContentUnit("text", "- Тут так уютненько! Мне очень нравится!"),
    ContentUnit("text",
                "- Да и пицца вкусная. Ребята со второго курса говорят, что очень рады, что появилось место, где можно вот так прийти и посидеть с друзьями."),
    ContentUnit("text", "#Здесь фото внутри"),
]
buttons = {
    "А как же бар 108?": "VII_b_01_00",
    "Может сходим потом, посмотрим на спортивные корты?": "VII_b_01_01"
}
states["VII_b_00_00"] = State(content, buttons)

# VII_b_01_00
content = [
    ContentUnit("text", "- А как же бар 108? Там что нельзя посидеть? Он раньше открылся."),
    ContentUnit("text",
                "- Да, там тоже классно, просто итальянской кухни нет. Они кстати, прямо по пути в Бахетле, только ближе находятся. Удобно.",
                delay=3),
    ContentUnit("text", "Наевшись досыта вы отправились:")
]
buttons = {
    "Домой": "VII_b_02_00"
}
states["VII_b_01_00"] = State(content, buttons)

# VII_b_01_01
content = [
    ContentUnit("text", "- Дааа, давайте! Классная мысль."),
    ContentUnit("text",
                "- Я слышал, там для жителей города бесплатно можно заниматься и на теннисном корте, и на баскетбольной, волейбольной площадках."),
    ContentUnit("text", "- А я там рядом каждый день бегаю на беговой дорожке."),
    ContentUnit("text", "- А где это вообще, ребят?"),
    ContentUnit("text",
                "- Ты ни разу не видел?? Прямо напротив ЖК, только на другой стороне, относительно недалеко от спортивного комплекса."),
    ContentUnit("text",
                "- Ну блин, извините, с моим зрением много не увидишь… Ты то передо мной стоишь размытый весь…"),
    ContentUnit("text", "Наевшись досыта вы отправились:")
]
buttons = {
    "На спортивные корты": "VII_b_02_01",
}
states["VII_b_01_01"] = State(content, buttons)

# VII_b_02_00 TODO: Add Photo
content = [
    ContentUnit("text", "По пути домой..."),
    ContentUnit("text", "- Вон там спортивные корты."),
    ContentUnit("text", "#Здесь фото кортов или дорожки"),
    ContentUnit("text", "- Смотрите, а рядом с СК катаются на скейтах."),
    ContentUnit("text",
                "- Ага, а вон какой дурак, проходя мимо, выкинул жвачку прямо рядом с ними, на асфальт. Как бы они не зацепились за нее и не упали."),
]
buttons = {
    "Попросить парня выкинуть свою жвачку в мусорку": "VII_b_03_00",
    "Кинул и кинул, кому какое дело": "VII_b_03_01"
}
states["VII_b_02_00"] = State(content, buttons)

# VII_b_02_01 TODO: Add Photo
content = [
    ContentUnit("text", "По пути на корты...."),
    ContentUnit("text", "- Вон там спортивные корты."),
    ContentUnit("text", "#Здесь фото кортов или дорожки"),
    ContentUnit("text", "- Смотрите, а рядом с СК катаются на скейтах."),
    ContentUnit("text",
                "- Ага, а вон какой дурак, проходя мимо, выкинул жвачку прямо рядом с ними, на асфальт. Как бы они не зацепились за нее и не упали."),
]
buttons = {
    "Попросить парня выкинуть свою жвачку в мусорку": "VII_b_03_00",
    "Кинул и кинул, кому какое дело": "VII_b_03_01"
}
states["VII_b_02_01"] = State(content, buttons)

# VII_b_03_00
content = [
    ContentUnit("text",
                "- А ты молодец! Ему вроде даже самому как-то стыдно стало, прям извинился и выкинул в мусорку, надо же…"),
    ContentUnit("text",
                "Насмотревшись на скейтеров, с чувством собственного удовлетворения вы продолжили свой путь в корпус.")
]
buttons = {
    "Дальше": "VII_c_00_00"
}
states["VII_b_03_00"] = State(content, buttons, callback=end)

# VII_b_03_01
content = [
    ContentUnit("text", "- Ну что, может возьмем у кого-нибудь мячик да поиграем в баскет?"),
    ContentUnit("text", "- Why not? Давайте."),
]
buttons = {
    "Дальше": "VII_c_00_01"
}
states["VII_b_03_01"] = State(content, buttons)

# VII_c_00_00 TODO: Add Photo
content = [
    ContentUnit("text", "Пару часов спустя вечером."),
    ContentUnit("text", "Как же здесь красиво по вечерам… Потрясающие закаты…"),
    ContentUnit("photo", photos.urls["sunset"]),
]
buttons = {
    "Начать с начала": "I_a_00_00"
}
states["VII_c_00_00"] = State(content, buttons)

# VII_c_00_01
content = [
    ContentUnit("text", "Пару часов спустя. Вечером."),
    ContentUnit("text",
                "Как же болит голова… Что это за звуки… Кажется кто-то что-то пытается сказать… Ай… Как же больно!"),
    ContentUnit("text", "- Эй, очнись!! Давай поднимайся!"),
    ContentUnit("text", "- Голова болит."),
    ContentUnit("text",
                "- Ну еще бы… Видимо скейт вылетел у тебя из-под ног, и твоя голова ударилась о край бордюра, надо быть осторожнее. Тут недалеко есть медцентр, прямо за кампусами, я тебя провожу."),
]
buttons = {
    "Согласиться": "VII_c_01_00",
    "Отказаться": "VII_c_01_01"
}
states["VII_c_00_01"] = State(content, buttons, callback=end)

# VII_c_01_00 TODO: Add Photo
content = [
    ContentUnit("text", "#Здесь фото медцентра и карты"),
    ContentUnit("text", "- Спасибо. Как это могло произойти… 5 лет уже катаюсь ведь!"),
    ContentUnit("text",
                "- Кажется колесико зацепилось за огромный кусок жвачки, который кто-то здесь бросил! Не люблю таких людей, здесь же такая чистота!! Зачем все портить."),
    ContentUnit("text", "- М-да… Вот она карма…"),
    ContentUnit("text", "Вот так вот он закончился Ваш BootCamp. С сотрясением, но в компании друзей :)")
]
buttons = {
    "Начать с начала": "I_a_00_00"
}
states["VII_c_01_00"] = State(content, buttons)

# VII_c_01_01
content = [
    ContentUnit("text",
                "- Ну как знаешь, надеюсь у тебя ничего серьезного. Сходи хотя бы в аптеку. В @InnoHelpBot можно посмотреть информацию о режимах работы и контактные телефоны учреждений в нашем городе, в том числе и об аптеке."),
    ContentUnit("text", "- Спасибо, схожу."),
    ContentUnit("text", "Вот так вот он закончился Ваш BootCamp. С сотрясением, но в компании друзей :)")
]
buttons = {
    "Начать с начала": "I_a_00_00"
}
states["VII_c_01_01"] = State(content, buttons)
