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
    ContentUnit("text", "The sun came up.", delay=2),
    ContentUnit("text", "П The sun glinted through the window, and warm rays of sunlight wake you up."),
    ContentUnit("text", " But the morning alarm hasn't called yet, it’s better to sleep more...", delay=3),
    ContentUnit("text", "НCan't sleep...", delay=2),
    ContentUnit("text",
                "You get out of a bed with a sense of new energy overfilling your body, but mixed with weakness after yesterday."),
    ContentUnit("text", "Getting ready for the morning procedures, you go to the bathroom."),
    ContentUnit("text",
                " Suddenly, the door nearby opens, and there appears the neighbor Ivan, with a towel over his shoulder."),
    ContentUnit("text",
                " Looking at each other, you freeze for a moment as two cowboys preparing for gunfight."),
    ContentUnit("text", "You decide:")
]
buttons = {"Politely let the neighbor visit the bathroom first.": "II_a_01_00",
           "To rush to the bathroom": "II_a_01_01"}
states["II_a_00_00"] = State(content, buttons)

# II_a_00_00_female
content = [
    ContentUnit("text", "The sun came up.", delay=2),
    ContentUnit("text", "П The sun glinted through the window, and warm rays of sunlight wake you up."),
    ContentUnit("text", " But the morning alarm hasn't called yet, it’s better to sleep more...", delay=3),
    ContentUnit("text", "НCan't sleep...", delay=2),
    ContentUnit("text",
                "You get out of a bed with a sense of new energy overfilling your body, but mixed with weakness after yesterday."),
    ContentUnit("text", "Getting ready for the morning procedures, you go to the bathroom."),
    ContentUnit("text",
                " Suddenly, the door nearby opens, and there appears the neighbor Ivan, with a towel over his shoulder."),
    ContentUnit("text",
                " Looking at each other, you freeze for a moment as two cowboys preparing for gunfight."),
    ContentUnit("text", "You decide:")
]
buttons = {"Politely let the neighbor visit the bathroom first.": "II_a_01_00",
           "To rush to the bathroom": "II_a_01_01"}
states["II_a_00_00_female"] = State(content, buttons)

# II_a_01_00
content = {
    True: [
        ContentUnit("text", "- Good morning, you can go first. I'll wait."),
        ContentUnit("text", " - Ok. Thank you, - replied the neighbor, rubbing his sleepy eyes.")
    ],
    False: [
        ContentUnit("text", "- Good morning, you can go first. I'll wait."),
        ContentUnit("text", " - Ok. Thank you, - replied the neighbor, rubbing her sleepy eyes.")
    ]
}
buttons = {"Next": "II_a_02_00"}
states["II_a_01_00"] = State(content, buttons)

# II_a_01_01
content = {
    True: [
        ContentUnit("text", "Running at breakneck pace and screaming “I'm first!”, you rush towards the bathroom.",
                    delay=2),
        ContentUnit("text",
                    "The confused neighbor remained in the doorway going bug-eyed because of your sudden lunge.",
                    delay=2)
    ],
    False: [
        ContentUnit("text", "Running at breakneck pace and screaming “I'm first!”, you rush towards the bathroom.",
                    delay=2),
        ContentUnit("text",
                    "The confused neighbor remained in the doorway going bug-eyed because of your sudden lunge.",
                    delay=2)
    ]
}
buttons = {"Next": "II_a_02_00"}
states["II_a_01_01"] = State(content, buttons)

# II_a_02_00 TODO: Change text on the button
content = {
    True: [
        ContentUnit("text", "After hygienic procedures, both of you are heading to the cafeteria for breakfast."),
        ContentUnit("photo", photos.urls["cafeteria"]),
        ContentUnit("text", " - Meals are really great here, - you said, shovelling down delicious breakfast."),
        ContentUnit("text", " - Yeah, and during InnoBootCamp our meals are free, - said Ivan."),
        ContentUnit("text",
                    "- Oh, and then, perhaps, we'll have to pay a lot of money for all this yummy, - you complained."),
        ContentUnit("text", "- Not that much... you can choose a meal plan that suits you.")
    ],
    False: [
        ContentUnit("text", "After hygienic procedures, both of you are heading to the cafeteria for breakfast."),
        ContentUnit("photo", photos.urls["cafeteria"]),
        ContentUnit("text", " - Meals are really great here, - you said, shovelling down delicious breakfast."),
        ContentUnit("text", " - Yeah, and during InnoBootCamp our meals are free, - said Ivan."),
        ContentUnit("text",
                    "- Oh, and then, perhaps, we'll have to pay a lot of money for all this yummy, - you complained."),
        ContentUnit("text", "- Not that much... you can choose a meal plan that suits you.")
    ]
}
buttons = {"Look at the cost of eating": "II_a_02_00_eating_plan"}
states["II_a_02_00"] = State(content, buttons)

# II_a_02_00_eating_plan TODO: Change the text
content = [
    ContentUnit("text", "You can eat in 5 different places:"),
    ContentUnit("text",
                '- Canteen "ОМС" on the 1st floor of University\n- "Wrap and Go" ont 1st floor of University\n- Canteen on the 1st floor 1st campus\n- Canteen on the 1st floor 4th campus\n- Cafe "CG" on 1st floor Sport Center "Innopolis"'),
    ContentUnit("text",
                "Students can choose any plan of eating, for example 5 or 7 days."),
    ContentUnit("text",
                "Depends on the plan of eating the cost in week is:"),
    ContentUnit("photo", photos.urls["eating5"]),
    ContentUnit("photo", photos.urls["eating7"])
]
buttons = {"How can I choose the plan of eating?": "II_a_02_00_student_portal"}
states["II_a_02_00_eating_plan"] = State(content, buttons)

# II_a_02_00_student_portal TODO: Change the text
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
buttons = {"Next": "II_a_03_00"}
states["II_a_02_00_student_portal"] = State(content, buttons)

# II_a_03_00
content = [
    ContentUnit("text",
                "The huge crowd has already grouped round the lecture-hall. Now they look otherwise, without yesterday's baggage, but with laptops and backpacks."),
    ContentUnit("text", "At the first lecture lecturer gives you a brief description of the studying process.")
]
buttons = {"Next": "II_a_03_00_1"}
states["II_a_03_00"] = State(content, buttons)

# II_a_03_00_1
content = [
    ContentUnit("text",
                "The bad news go first. The studying period is fixed and there's no interruption on any public or national holidays!"),
    ContentUnit("text",
                " Also, almost all the necessary information on the courses is in something called 'Moodle'.")
]
buttons = {"Next": "II_a_03_00_2"}
states["II_a_03_00_1"] = State(content, buttons)

# II_a_03_00_2
content = {
    True: [
        ContentUnit("text", "- Really, everything is there?? – asked someone from the back rows."),
        ContentUnit("text", "- Yeah, hometasks, lectures and courses assessments. Everything is on the website."),
        ContentUnit("text", "https://moodle.university.innopolis.ru"),
        ContentUnit("text", "Hmm.... And where are the good news? – you think."),
        ContentUnit("text", "- And, finally, before the lecture  I'd like to tell you one more thing.")
    ],
    False: [
        ContentUnit("text", "- Really, everything is there?? – asked someone from the back rows."),
        ContentUnit("text", "- Yeah, hometasks, lectures and courses assessments. Everything is on the website."),
        ContentUnit("text", "https://moodle.university.innopolis.ru"),
        ContentUnit("text", "Hmm.... And where are the good news? – you think."),
        ContentUnit("text", "- And, finally, before the lecture  I'd like to tell you one more thing.")
    ]
}
buttons = {"Next": "II_a_03_00_3"}
states["II_a_03_00_2"] = State(content, buttons)

# II_a_03_00_3
content = [
    ContentUnit("text", "- Tomorrow will be opened diferent student's clubs."),
    ContentUnit("text", "- You can look at the list now if you’d like to."),
    ContentUnit("text", "ТYou decide:"),
]
buttons = {"Look through the list": "II_a_04_00",
           "To leave until later and get ready for a lecture": "II_a_05_00",
           }
states["II_a_03_00_3"] = State(content, buttons)

# II_a_04_00 List of Clubs
content = [
    ContentUnit("text",
                "- 3D Modelling\n- Basketball\n- Volleyball\n- Guitar Lessons\n- Piano Lessons\n- Kendo\n- Club of Video Making and Editing\n- Anime Club\n- Table Tennis\n- Parkour\n- Innosandbox(Start-Ups platform)\n- Client-Server Application Development on C#\n- Russian Military Tradition\n- СModern Dance\n- Sports Robotics\n- Competitive Programming (Beginner and Intermediate Levels)\n- French Language (Beginner and Intermediate Levels)\n- Football\n- Glee Club\n- AI Community\n- Android Developing\n- Art Club\n- Break Dance\n- Capoeira CDO\n- Chinese\n- CinemaClub\n- CTF\n- Cult of Cormen (CC)\n- Dancing (Latina/Standard, Salsa/Bachata)\n- GameDev / Unreal Engine 4\n- Inno Combat Sambo team\n- Mathematics | UI (Under the Integral)\n- Music Club (Guitar Evenings)\n- Photo Club\n- SkateBoardingClub\n- Translators Club")
]
buttons = {"Next": "II_a_05_00"}
states["II_a_04_00"] = State(content, buttons)

# II_a_05_00
content = [
    ContentUnit("text", "Leaving the lecture-hall, you feel the weight of new information in your head.")
]
buttons = {"So, what is the next?": "II_a_06_00"}
states["II_a_05_00"] = State(content, buttons, callback=check_meeting)

# II_a_06_00
content = [
    ContentUnit("text",
                "Well, you remember yesterday’s explanation of the basis of the schedule and you are going with other students to the practice seminar."),
    ContentUnit("text", "There you will be able to analyze the material given on the lecture.")
]
buttons = {"Next": "II_a_07_00"}
states["II_a_06_00"] = State(content, buttons)

# II_a_06_01
content = {
    True: [
        ContentUnit("text", "Waiting for a moment, you're trying to concentrate.", delay=2),
        ContentUnit("text",
                    "-  What's the holdup? Let's go to the seminar, - said Vanya – there you can always clarify things that you didn't understand on the lecture.")
    ],
    False: [
        ContentUnit("text", "Waiting for a moment, you're trying to concentrate.", delay=2),
        ContentUnit("text",
                    "-  What's the holdup? Let's go to the seminar, - said Yana – there you can always clarify things that you didn't understand on the lecture.")
    ]
}
buttons = {"Next": "II_a_07_00"}
states["II_a_06_01"] = State(content, buttons)

# II_a_07_00
content = {
    True: [
        ContentUnit("text",
                    "Making things as clear as a bell on the seminar, you feel great relief, and even joy!"),
        ContentUnit("text",
                    "In order to solidify the given knowledge, instructor gave home tasks, saying: 'Hit the books, ladies and gentleman!'"),
        ContentUnit("text", "- Yes, they know how to motivate, - smiled your friend."),
        ContentUnit("text", "And you went together to the English class."),
        ContentUnit("text", "It is not surprising. University is with English-speaking professors."),
        ContentUnit("text", "It was clear that without a good knowledge of English it will be difficult to study here.")
    ],
    False: [
        ContentUnit("text",
                    "Making things as clear as a bell on the seminar, you feel great relief, and even joy!"),
        ContentUnit("text",
                    "In order to solidify the given knowledge, instructor gave home tasks, saying: 'Hit the books, ladies and gentleman!'"),
        ContentUnit("text", "- Yes, they know how to motivate, - smiled your friend."),
        ContentUnit("text", "And you went together to the English class."),
        ContentUnit("text", "It is not surprising. University is with English-speaking professors."),
        ContentUnit("text", "It was clear that without a good knowledge of English it will be difficult to study here.")
    ]
}
buttons = {"Next": "II_a_08_00"}
states["II_a_07_00"] = State(content, buttons)

# II_a_08_00
content = {
    True: [
        ContentUnit("text", "Going back to your room you didn't find there Ivan."),
        ContentUnit("text",
                    "He returned later. As it turned out, foreigners have to pass an additional procedure."),
        ContentUnit("text",
                    " - I was told that every time, when I cross the border of the Russian Federation, I have to bring my passport and migration card to 319 office. There's the requirement of Migration Service that each foreigner has to go through migration registration within 7 days from the moment of arrival, - has explained Vanja."),
        ContentUnit("text",
                    " - Well, of course, it is if foreigner doesn't want to have huge penalty, I don't want to...")
    ],
    False: [
        ContentUnit("text", "Going back to your room you didn't find there Yana."),
        ContentUnit("text",
                    "She returned later. As it turned out, foreigners have to pass an additional procedure."),
        ContentUnit("text",
                    " - I was told that every time, when I cross the border of the Russian Federation, I have to bring my passport and migration card to 319 office. There's the requirement of Migration Service that each foreigner has to go through migration registration within 7 days from the moment of arrival, - has explained Yana."),
        ContentUnit("text",
                    " - Well, of course, it is if foreigner doesn't want to have huge penalty, I don't want to...")]
}
buttons = {"Next": "II_a_09_00"}
states["II_a_08_00"] = State(content, buttons)

# II_a_09_00
content = {
    True: [
        ContentUnit("text",
                    " Late in the evening after your first day at university, you and your roommate are talking and having tea."),
        ContentUnit("text",
                    " - Yeah, the studying process is serious here. A lot of classes, and they even gave us plenty tasks – a dime a dozen - you said to Ivan."),
        ContentUnit("text",
                    "-  -That’s right! They know their job, and don’t forget about students. Our constant studying will be finally paid off, - heard you in response."),
        ContentUnit("text",
                    "- Repaid? What are you talking about?")
    ],
    False: [
        ContentUnit("text",
                    " Late in the evening after your first day at university, you and your roommate are talking and having tea."),
        ContentUnit("text",
                    " - Yeah, the studying process is serious here. A lot of classes, and they even gave us plenty tasks – a dime a dozen - you said to Yana."),
        ContentUnit("text",
                    "-  -That’s right! They know their job, and don’t forget about students. Our constant studying will be finally paid off, - heard you in response."),
        ContentUnit("text",
                    "- Repaid? What are you talking about?")
    ]
}
buttons = {"Next": "II_a_10_00"}
states["II_a_09_00"] = State(content, buttons)

# II_a_10_00
content = {
    True: [
        ContentUnit("text",
                    " - Do you know the amount of stipend here?"),
        ContentUnit("text", "- Oh, well, surprise me! – teased you in response.")
    ],
    False: [
        ContentUnit("text",
                    " - Do you know the amount of stipend here?"),
        ContentUnit("text", "- Oh, well, surprise me! – teased you in response.")
    ]
}
buttons = {"Next": "II_a_11_00"}
states["II_a_10_00"] = State(content, buttons)

# II_a_11_00
content = {
    True: [
        ContentUnit("text",
                    "- If there is only one “C” or more for the semester you'll have 12 thousand rubles. If you're studying on “A-B” marks the stipend is 18 thousand. If there's only 1 or 2 “B” and the rest marks are “A” - 24."),
        ContentUnit("text", "- And what about an 'A' students? How much do they get? - asked you."),
        ContentUnit("text", "- 36 thousand rubles. And that's just for bachelors."),
        ContentUnit("text", "Your mouth formed an O."),
        ContentUnit("text", "- So I'm going to study well to make gifts to my parents and myself."),
        ContentUnit("text", "You are still sitting open-mouthed and shocked."),
    ],
    False: [
        ContentUnit("text",
                    "- If there is only one “C” or more for the semester you'll have 12 thousand rubles. If you're studying on “A-B” marks the stipend is 18 thousand. If there's only 1 or 2 “B” and the rest marks are “A” - 24."),
        ContentUnit("text", "- And what about an 'A' students? How much do they get? - asked you."),
        ContentUnit("text", "- 36 thousand rubles. And that's just for bachelors."),
        ContentUnit("text", "Your mouth formed an O."),
        ContentUnit("text", "- So I'm going to study well to make gifts to my parents and myself."),
        ContentUnit("text", "You are still sitting open-mouthed and shocked."),
    ]
}
buttons = {"Next": "II_a_12_00"}
states["II_a_11_00"] = State(content, buttons)

# II_a_12_00
content = {
    True: [
        ContentUnit("text", "- Okay, let's focus on homework! I advise you not to be lazy, you know."),
        ContentUnit("text", " Slammed door in the kitchen cheered you up."),
        ContentUnit("text", "- Wait for me! - you shouted to your neighbor, trying quickly finish your tea.")
    ],
    False: [
        ContentUnit("text", "- Okay, let's focus on homework! I advise you not to be lazy, you know."),
        ContentUnit("text", " Slammed door in the kitchen cheered you up."),
        ContentUnit("text", "- Wait for me! - you shouted to your neighbor, trying quickly finish your tea.")

    ]
}
buttons = {"Start next day": "III_a_00_00"}
states["II_a_12_00"] = State(content, buttons)

# III_a_00_00
content = [ContentUnit("text", "Another day at BootCamp,which as always starts with classes."),
           ContentUnit("text", photos.urls["lecture"]),
           ContentUnit("text",
                       "During the break between lecture and seminar(lab Session). A friend who goes with you to classes: - I didn't really understand how it all works. I mean the process of teaching and organizing the course.")]
buttons = {"Neither do I": "III_a_01_00",
           "As I understood there are professors and TA`s...": "III_a_01_01"}
states["III_a_00_00"] = State(content, buttons)

# III_a_01_00
content = [ContentUnit("text", "Intervenes in the conversation friend:"),
           ContentUnit("text",
                       "- There are professors. They conduct lectures, take exams and are responsible for the organization of the course."),
           ContentUnit("text", "- And there are also TA`s?"),
           ContentUnit("text",
                       "- Yeah, Teaching Assistants, they conduct seminars, check our homework and they are the ones to contact with any questions.")
           ]
buttons = {"What about professors? Can I contact them with questions?": "III_a_02_00",
           "And how to get in contact with them?": "III_a_02_01"}
states["III_a_01_00"] = State(content, buttons)

# III_a_01_01 T
content = [
    ContentUnit("text", "Intervenes In the conversation friend"),
    ContentUnit("text",
                "- Yeah, the first  ones conduct lectures, organize the whole system of course and take exams; and the second  onesTA`s (an abbreviation of Teaching Assistant) conduct the seminars, check the homework. And for all problems it is better to turn first to your TA.")
]
buttons = {"And the Professor, isn't there some way to contact them?": "III_a_02_00",
           "It was said that professors have office hours, what are they for?": "III_a_02_02"}
states["III_a_01_01"] = State(content, buttons)

# III_a_02_00
content = [
    ContentUnit("text",
                " - Only if the question to TA remained unresolved. To resolve different issues you can contact professors during their Office Hours actually. Just try not to interrupt them with a lot of letters on email or telegram, they already have plenty work to do."),

]
buttons = {"Next": "III_b_00_00"}
states["III_a_02_00"] = State(content, buttons)

# III_a_02_01
content = [
    ContentUnit("text",
                "-  Through the mail or telegram. Generally it depends on the teacher: some prefer to write to him only through the head of your group; someone answers to messages only during Office hours. "),

]
buttons = {"Дальше": "III_b_00_00"}
states["III_a_02_01"] = State(content, buttons)

# III_a_02_02
content = [
    ContentUnit("text",
                "- They are exactly for solving problems. I mean just try not to interrupt them with a lot of letters on email or telegram, they already have plenty work to do."),
    ContentUnit("text",
                "As I understand it, it depends on the teacher: some prefer to to be contacted only by the elder; someone responds to messages in Office hours. ")
]
buttons = {"Next": "III_b_00_00"}
states["III_a_02_02"] = State(content, buttons)

# III_b_00_00
content = {
    True: [
        ContentUnit("text", "- Well, now it seems more understandable. Thanks, guys.", delay=3),
        ContentUnit("text", "Lunch.", delay=3),
        ContentUnit("text", "There are a lot of people in the canteen, almost no free seats.\n"
                            "You have noticed a table for two, behind him sits one student.")
    ],
    False: [
        ContentUnit("text", "- Well, now it seems more understandable. Thanks, guys.", delay=3),
        ContentUnit("text", "Lunch.", delay=3),
        ContentUnit("text", "There are a lot of people in the canteen, almost no free seats.\n"
                            "You have noticed a table for two, behind him sits one student.")
    ]
}
buttons = {"Decide to join": "III_b_01_00",
           "Continue looking for a free table": "III_b_01_01"}
states["III_b_00_00"] = State(content, buttons)

# III_b_01_00
content = {
    True: [ContentUnit("text", "- Is this seat taken?\n"
                               "- No, have a seat."),
           ContentUnit("text", "- Are you on BootCamp?"),
           ContentUnit("text", "- Yeah."),
           ContentUnit("text",
                       " - I remember two years ago I was exactly like you... It was hard time, I did not have enough sleep during bootcamp, that helped me to realize that here is not so easy to live and study. Have you even seen something in the city?"),

           ],
    False: [
        ContentUnit("text", "- Is this seat taken?\n"
                            "- No, have a seat."),
        ContentUnit("text", "- Are you on BootCamp?"),
        ContentUnit("text", "- Yeah."),
        ContentUnit("text",
                    " - I remember two years ago I was exactly like you... It was hard time, I did not have enough sleep during bootcamp, that helped me to realize that here is not so easy to live and study. Have you even seen something in the city?"),

    ]
}
buttons = {"Nope": "III_b_02_00",
           "Have seen the sports center from the window": "III_b_02_00"}
states["III_b_01_00"] = State(content, buttons)

# III_b_01_01
content = {
    True: [
        ContentUnit("text", "Here is a free table."),
        ContentUnit("text", "After a couple of minutes another student joins you."),
        ContentUnit("text", "- Hi! \n"
                            "- Hi!"),
        ContentUnit("text", "- Are you on BootCamp?"),
        ContentUnit("text", "- Yeah."),
        ContentUnit("text",
                    " - I remember two years ago I was exactly like you... It was hard time, I did not have enough sleep during bootcamp, that helped me to realize that here is not so easy to live and study. Have you even seen something in the city?"),

    ],
    False: [
        ContentUnit("text", "Here is a free table."),
        ContentUnit("text", "After a couple of minutes another student joins you."),
        ContentUnit("text", "- Hi! \n"
                            "- Hi!"),
        ContentUnit("text", "- Are you on BootCamp?"),
        ContentUnit("text", "- Yeah."),
        ContentUnit("text",
                    " - I remember two years ago I was exactly like you... It was hard time, I did not have enough sleep during bootcamp, that helped me to realize that here is not so easy to live and study. Have you even seen something in the city?"),

    ]
}
buttons = {"Nope": "III_b_02_00",
           "Have seen the sports center from the window": "III_b_02_00"}
states["III_b_01_01"] = State(content, buttons)

# III_b_02_00
content = {
    True: [
        ContentUnit("text",
                    "I can hold a small tour around the city, to get familiar with the surroundings. Afterwards you live here. By the way my name is Misha."),
        ContentUnit("text", "- Nice to meet you. I am #name. Is there something to see here?"),
        ContentUnit("text", "Sports complex\n"
                            "Opening hours: 7.00 - 23.00\n"
                            "Address: city Innopolis, Sportivnaya str., 107\n"
                            "There is a swimming pool, large game room, group programs, martial arts, table tennis and much more.\n"
                            "Students have free access!\n"
                            "Link to the chat in telegram: : https://t.me/InnopolisSport"),
        ContentUnit("photo", photos.urls["sport_complex"]),
        ContentUnit("text", "Medical center/clinic\n"
                            "ЧOpening hours:\n"
                            "MON - FRI from 10:00 to 16:00\n"
                            "SAT - 09:30 to 15:30\n"
                            "SUN - closed\n"
                            "hospital - round the clock\n"
                            "Testing: from 9.00 to 11.00 (weekdays)\n"
                            "Address: city Innopolis, street Sports, d. 301, terminal 1/terminal 2\n"
                            "Here: you can get advice of medical specialists and necessary treatment.\n"
                            "All relevant information is available in @Innovlinic_bot \n"
                            "Link to the channel in the telegram: https://telegram.me/joinchat/CCS9pz3TH09k7FgaWZ0tqA"),
        ContentUnit("photo", photos.urls["med_center"]),
        ContentUnit("text", "Pharmacy/pediatrician (children's doctor)\n"
                            "Opening hours of the pharmacy:\n"
                            "MON-FRI 9.00-18.00 (without breaks)\n"
                            "SAT 9:00-17:00 (without lunch)\n"
                            "Sun:9: 00-16:00 (without lunch)\n"
                            "Address: Innopolis University str., 1, campus №4\n"
                            "Here: you can purchase required drugs"),
        ContentUnit("text", "Mail\n"
                            "Opening hours: 9.00 - 17.00\n"
                            "Weekends: Saturday, Sunday\n"
                            "Address: Universitetskaya St., 7, 1 floor (building Technopark them. A. S. Popov)\n"
                            "Here: you can send/receive parcels and letters.\n"
                            "Link to the chat in Telegram: https://telegram.me/joinchat/Cdg7Gj2lr0wP_l4NMkRReg"),
        ContentUnit("photo", photos.urls["techno_park"]),
        ContentUnit("text", "Resort City “Sviyaga Hills”\n"
                            "Address: Verkhneuslonsky district, der. Savinovo\n"
                            "Here, in Summer you can play Golf, go Cycling, rollerblading, Segway, catamarans, boats, etc.\n"
                            "In winter you can go skiing and snowboarding\n"
                            "All year round: play Billiards and bowling, karaoke\n"
                            "For students and employees free ski passes and rental equipment!"),
        ContentUnit("text", "More information can be found in @InnoHelpBot."),
        ContentUnit("text", "Misha: - Well, have you decided to join me?"),
    ],
    False: [
        ContentUnit("text",
                    "I can hold a small tour around the city, to get familiar with the surroundings. Afterwards you live here. By the way my name is Lisa."),
        ContentUnit("text", "- Nice to meet you. I am #name. Is there something to see here?"),
        ContentUnit("text", "Sports complex\n"
                            "Opening hours: 7.00 - 23.00\n"
                            "Address: city Innopolis, Sportivnaya str., 107\n"
                            "There is a swimming pool, large game room, group programs, martial arts, table tennis and much more.\n"
                            "Students have free access!\n"
                            "Link to the chat in telegram: : https://t.me/InnopolisSport"),
        ContentUnit("photo", photos.urls["sport_complex"]),
        ContentUnit("text", "Medical center/clinic\n"
                            "ЧOpening hours:\n"
                            "MON - FRI from 10:00 to 16:00\n"
                            "SAT - 09:30 to 15:30\n"
                            "SUN - closed\n"
                            "hospital - round the clock\n"
                            "Testing: from 9.00 to 11.00 (weekdays)\n"
                            "Address: city Innopolis, street Sports, d. 301, terminal 1/terminal 2\n"
                            "Here: you can get advice of medical specialists and necessary treatment.\n"
                            "All relevant information is available in @Innovlinic_bot \n"
                            "Link to the channel in the telegram: https://telegram.me/joinchat/CCS9pz3TH09k7FgaWZ0tqA"),
        ContentUnit("photo", photos.urls["med_center"]),
        ContentUnit("text", "Pharmacy/pediatrician (children's doctor)\n"
                            "Opening hours of the pharmacy:\n"
                            "MON-FRI 9.00-18.00 (without breaks)\n"
                            "SAT 9:00-17:00 (without lunch)\n"
                            "Sun:9: 00-16:00 (without lunch)\n"
                            "Address: Innopolis University str., 1, campus №4\n"
                            "Here: you can purchase required drugs"),
        ContentUnit("text", "Mail\n"
                            "Opening hours: 9.00 - 17.00\n"
                            "Weekends: Saturday, Sunday\n"
                            "Address: Universitetskaya St., 7, 1 floor (building Technopark them. A. S. Popov)\n"
                            "Here: you can send/receive parcels and letters.\n"
                            "Link to the chat in Telegram: https://telegram.me/joinchat/Cdg7Gj2lr0wP_l4NMkRReg"),
        ContentUnit("photo", photos.urls["techno_park"]),
        ContentUnit("text", "Resort City “Sviyaga Hills”\n"
                            "Address: Verkhneuslonsky district, der. Savinovo\n"
                            "Here, in Summer you can play Golf, go Cycling, rollerblading, Segway, catamarans, boats, etc.\n"
                            "In winter you can go skiing and snowboarding\n"
                            "All year round: play Billiards and bowling, karaoke\n"
                            "For students and employees free ski passes and rental equipment!"),
        ContentUnit("text", "More information can be found in @InnoHelpBot."),
        ContentUnit("text", "Lisa: - Well, have you decided to join me?"),

    ]
}
buttons = {
    "That sounds great": "III_b_03_00",
    "Probably some other time": "III_b_03_01",
    "I prefer to do my homework": "III_b_03_01"
}
states["III_b_02_00"] = State(content, buttons)

# III_b_03_00

content = {
    True: [
        ContentUnit("text",
                    "Cool! Then let’s meet at... Oh, I almost forgot about today’s meeting about the SA. So the tour would be canceled. "),
        ContentUnit("text", "You can join me if you wish. I think it can be useful."),

    ],
    False: [
        ContentUnit("text",
                    "Cool! Then let’s meet at... Oh, I almost forgot about today’s meeting about the SA. So the tour would be canceled. "),
        ContentUnit("text", "You can join me if you wish. I think it can be useful."),
    ]
}
buttons = {
    "I don't really want to": "III_b_04_00",
    "SA? What is it?": "III_b_04_01"
}
states["III_b_03_00"] = State(content, buttons)

# III_b_03_01
content = {
    True: [
        ContentUnit("text", "- Well, as you wish. I was going to a meeting of the SA."),
        ContentUnit("text", "You can join me if you wish. I think it can be useful."),
    ],
    False: [
        ContentUnit("text", "- Well, as you wish. I was going to a meeting of the SA."),
        ContentUnit("text", "You can join me if you wish. I think it can be useful."),

    ]
}
buttons = {
    "I don't really want to": "III_b_04_00",
    "SA? What is it?": "III_b_04_01"
}
states["III_b_03_01"] = State(content, buttons)

# III_b_04_00
content = [
    ContentUnit("text",
                "- Well, you better think twice... the Student Association is a good thing! There you can turn to when you need help in implementing any ideas and generally almost for any questions."),
    ContentUnit("text", "- When does  this meeting start?"),
    ContentUnit("text", "It was so easy to persuade you! It starts in few minutes. Hurry up!")
]
buttons = {
    "Go on the meeting": "III_c_00_00"
}
states["III_b_04_00"] = State(content, buttons)

# III_b_04_01
content = [
    ContentUnit("text",
                "- The student Association is a student government, whose members help other students. There you can turn to when you need help in implementing any ideas and generally almost for any questions."),
    ContentUnit("text", "- When does this meeting start?"),
    ContentUnit("text", "- In few minutes. Hurry up!"),
]
buttons = {
    "Go on the meeting": "III_c_00_00"
}
states["III_b_04_01"] = State(content, buttons)

# III_c_00_00
content = [
    ContentUnit("text", "Meeting SA.", delay=3),
    ContentUnit("text", "President Of The Student Association.\n"
                        "Kamill Gusmanov.\n"
                        "There are fresh ideas or come up with a project that you want to implement? Or do you just have comments, suggestions or need help? Kamill will always listen and try to help."),
    ContentUnit("photo", photos.urls["kamill"]),
    ContentUnit("text", "Vocational and Academic Committee.\n"
                        "Nikita Zhuchkov. \n"
                        "You’d like to go to the conference or the Olympics? Any ideas for the hackathon?\n"
                        "In these cases Nikita will help you."),
    ContentUnit("photo", photos.urls["nikita"]),
    ContentUnit("text", "Sports Committee.\n "
                        "Anton Skudarnov.\n"
                        "Do you like sports? Want to take part in competition or hold your own? Contact Anton."),
    ContentUnit("photo", photos.urls["anton"]),
    ContentUnit("text", "Cultural Committee\n"
                        "Evgeniy Sorokin.\n"
                        "Evgeniy will help you to find like-minded people and develop talents, because he is engaged in the organization of cultural events."),
    ContentUnit("photo", photos.urls["evgeniy"]),
    ContentUnit("text", "Information Committee.\n"
                        "Andrey Pavlenko.\n"
                        "Andrey helps to convey information from the SA to students. Any comments, requests or assistance, but do not know whom to contact? Andrey is happy to help and will redirect you to the right people."),
    ContentUnit("photo", photos.urls["andrey"]),

]
buttons = {"Leave the meeting": "III_c_01_00"}
states["III_c_00_00"] = State(content, buttons)

# III_c_01_00
content = {
    True: [
        ContentUnit("text", "On the way to the room you noticed that Misha has a foreign accent. Decide to ask:\n"
                            "- Misha, where are you from?"),
        ContentUnit("text", "- From Russia, why are you asking?"),
        ContentUnit("text", "- You just got that accent, and I thought…"),
        ContentUnit("text", "Ah, I just returned from a long journey. I spent an academic year in China."),
        ContentUnit("text", "Wow, what were you doing there?"),
        ContentUnit("text", "Studying. The IU has academic exchange, didn't you know?")

    ],
    False: [
        ContentUnit("text", "On the way to the room you noticed that Lisa has a foreign accent. Decide to ask:\n"
                            "- Lisa, where are you from?"),
        ContentUnit("text", "- From Russia, why are you asking?"),
        ContentUnit("text", "- You just got that accent, and I thought…"),
        ContentUnit("text", "Ah, I just returned from a long journey. I spent an academic year in China."),
        ContentUnit("text", "Wow, what were you doing there?"),
        ContentUnit("text", "Studying. The IU has academic exchange, didn't you know?")
    ]
}
buttons = {
    "Is it possible?!": "III_c_02_00",
    "No, I didn't": "III_c_02_01"
}
states["III_c_01_00"] = State(content, buttons)

# III_c_02_00
content = {
    True: [
        ContentUnit("text",
                    "- Of course, it is real! I always dreamed about it. Every bachelor or master student can get this experience,if you study with the marks not lower than 'B' and your English level is 'upper-intermediate' or higher. "),
        ContentUnit("text",
                    "- Detailed information about all of this is on the University website(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
        ContentUnit("text", "- Okay, thanks, Misha."),
        ContentUnit("text", "- You are welcome. Good night."),
        ContentUnit("text", "- Bye."),
    ],
    False: [
        ContentUnit("text",
                    "- Of course, it is real! I always dreamed about it. Every bachelor or master student can get this experience,if you study with the marks not lower than 'B' and your English level is 'upper-intermediate' or higher. "),
        ContentUnit("text",
                    "- Detailed information about all of this is on the University website(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
        ContentUnit("text", "- Okay, thanks, Lisa."),
        ContentUnit("text", "- You are welcome. Good night."),
        ContentUnit("text", "- Bye."),

    ]
}
buttons = {
    "Start next day": "IV_a_00_00"
}
states["III_c_02_00"] = State(content, buttons)

# III_c_02_01
content = [
    ContentUnit("text",
                "- Now you'll know. Every bachelor or master student can get this experience, if you study with the marks not lower than 'B' and your English level is 'upper-intermediate' or higher."),
    ContentUnit("text",
                "- Detailed information about all of this is on the University website(https://university.innopolis.ru/cooperation/global/academic_exchange/)."),
    ContentUnit("text", "- Okay, thanks."),
    ContentUnit("text", "- You are welcome. Good night."),
    ContentUnit("text", "- Bye."),
]
buttons = {
    "Start next day": "IV_a_00_00"
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
