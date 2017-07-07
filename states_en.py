from state import State
from functions import *
from contentUnit import ContentUnit
import photos
import copy

states: State = {}

# start_state
content = [
    ContentUnit('photo', photos.urls["start day"]),
    ContentUnit("text", '''Hi!
The "InnoBootCamp2017" summer school starts pretty soon.
And to make your life and studying in Innopolis easier we, team of Innopolis students, prepared for you Telegram-bot. The bot will tell you about the student's life in our university in very interesting and accessible format.
To start the game press the button "Start" :)''')
]
buttons = {"Next": "sex_select"}
states["start_state"] = State(content, buttons)

# language_select
content = [
    ContentUnit("text", "Выберите язык "
                        "\nChoose your language"),
]
buttons = {"Русский": "start_state",
           "English": "start_state"
           }
states["language_select"] = State(content, buttons, callback=set_language)

# sex_select

content = [ContentUnit("text",
                       "Choose your gender")]
buttons = {"Male": "I_a_00_00", "Female": "I_a_00_00"}
states["sex_select"] = State(content, buttons, callback=set_sex)

# I_a_00_00 Start Point

content = {
    True: [
        ContentUnit("text",
                    "Congratulations, you got a grant  for education in Innopolis! You are standing on the threshold of a new full of adventures student’s life."),
        ContentUnit("text",
                    "Your story begins here, in Kazan, the big neighbor of innocity, which is still small, but has a promising future.")
    ],
    False: [
        ContentUnit("text",
                    "Congratulations, you got a grant  for education in Innopolis! You are standing on the threshold of a new full of adventures student’s life."),
        ContentUnit("text",
                    "Your story begins here, in Kazan, the big neighbor of innocity, which is still small, but has a promising future.")
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
    ContentUnit("text", "- Burnashev Ilya! \n"
                        "- Here!"),
    ContentUnit("text", "- Daria Naumova! \n"
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
                    "- Yes, that's for sure. Looks like it waited specially for us. I thought leaving Mongolia means leaving the heat. Ha-ha. I was wrong. Come to me, here it is cooler in the shadows.(write your name)")
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
                    "Looking at the clock (17:30), a new neighbor decides to go to the University on the students meeting."),
        ContentUnit("text", "You decide to:")
    ],
    False: [
        ContentUnit("text", " Yes, it’s Yana! The girl from Mongolia! What a coincidence that you are neighbors!"),
        ContentUnit("text",
                    "Looking at the clock (17:30), a new neighbor decides to go to the University on the students meeting."),
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

# I_c_03_01 Cafeteria before meeting
content = {
    True: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        ContentUnit("text",
                    "Saying that you'll try to not be late, having a growling stomach, you went to the canteen."),


        ContentUnit("text", " After a dinner you went:")
    ],
    False: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),
        ContentUnit("text",
                    "Saying that you'll try to not be late, having a growling stomach, you went to the canteen."),


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

# I_c_04_00 Cafeteria after meeting
content = {
    True: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),

        ContentUnit("text", "After a dinner you went to sleep", delay=2),
        ContentUnit("text", "Yes, it was a hard day. When you come in room you laid on the bed and felt asleep")
    ],
    False: [
        ContentUnit("text", "It seems like you haven't eaten forever. Some meal would be perfect."),

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
buttons = {"Next": "III_b_00_00"}
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
    ContentUnit("text", "It is already the fourth day, that you are here… But it feels like…")
]
buttons = {
    "I've been here for a month! ": "IV_a_01_00",
    "As if it’s the first day. I can't get used to everything…": "IV_a_01_01"
}
states["IV_a_00_00"] = State(content, buttons)

# IV_a_01_00
content = {
    True: [
        ContentUnit("text",
                    "Vanya runs into the room. That's really a positive person! He always jokes, I wish there were more such people..."),
        ContentUnit("text",
                    "Vanya: - Hey there! Looks like, you are awake, so let's get up faster, sleepyhead, there are new books!"),
        ContentUnit("text", "- Yes, I know. Let's go."),
        ContentUnit("text",
                    "- Just give me a minute, I need to order a book. If you’d like to take a book, you have to order it, and if it’s not in the someone’s hands, you can immediately pick it up.")
    ],
    False: [
        ContentUnit("text",
                    "Yana runs into the room. That's really a positive person! She always jokes, I wish there were such people.."),
        ContentUnit("text",
                    "Yana: - Hey there! Looks like, you are awake, so let's get up faster, sleepyhead, there are new books!"),
        ContentUnit("text", "- Yes, I know. Let's go."),
        ContentUnit("text",
                    "- Just give me a minute, I need to order a book. If you’d like to take a book, you have to order it, and if it’s not in the someone’s hands, you can immediately pick it up.")]
}
buttons = {
    "What's the portal?": "IV_a_02_00",
    "Damn, this is the first time I've heard about this... How do you everything know?!": "IV_a_02_01"
}
states["IV_a_01_00"] = State(content, buttons)

# IV_a_01_01
content = {
    True: [
        ContentUnit("text",
                    "Vanya runs into the room. That's really a positive person! He always jokes, I wish there were  more such people..."),
        ContentUnit("text",
                    "Vanya: - Hey there! Looks like, you are awake, so let's get up faster, sleepyhead, there are new books! I wanna take «Introduction to Algorithms». It is the most readable book."),
        ContentUnit("text", "- How did you know that it is the most readable one?"),
        ContentUnit("text",
                    "- You still don’t know? Just go to the library site, there’ll be shown which books are available, and which ones have already taken. All the books are divided into categories. So, you can order books there."),

    ],
    False: [
        ContentUnit("text",
                    "Yana runs into the room. That's really a positive person! She always jokes, I wish there were more such people..."),
        ContentUnit("text",
                    "Yana: - Hey there! Looks like, you are awake, so let's get up faster, sleepyhead, there are new books! I wanna take «Introduction to Algorithms». It is the most readable book."),
        ContentUnit("text", "- How did you know that it is the most readable one?"),
        ContentUnit("text",
                    "- You still don’t know? Just go to the library site, there’ll be shown which books are available, and which ones have already taken. All the books are divided into categories. So, you can order books there."),

    ]
}
buttons = {
    "What kind of portal?": "IV_a_02_00",
    "Damn, this is the first time I've heard about this... How do you know everything?!": "IV_a_02_01"
}
states["IV_a_01_01"] = State(content, buttons)

# IV_a_02_00
content = [
    ContentUnit("text", "portal.university.innopolis.ru/reading_hall/", delay=3),
    ContentUnit("text", "- Ok, got it. Thank you so much!"),
    ContentUnit("text",
                "- Hurry up then! You sleep like a log, even a lecture is not a hindrance for you! I wouldn’t advise you to do this during the semester."),

]
buttons = {
    "Next": "IV_b_00_00"
}
states["IV_a_02_00"] = State(content, buttons)

# IV_a_02_01
content = [
    ContentUnit("text",
                "- You have to read telegram chats, there is a lot of useful information there. Check also your official mail a bit more often to understand what’s going on in university. Everyone has his own mailbox with @innopolis.ru domain, so you can use it to communicate with professors. Everything should be official, my friend."),
    ContentUnit("text", "- Ok, got it. Thank you so much!"),
    ContentUnit("text",
                "- Hurry up then! You sleep like a log, even a lecture is not a hindrance for you! I wouldn’t advise you to do this during the semester."),

]
buttons = {
    "Next": "IV_b_00_00"
}
states["IV_a_02_01"] = State(content, buttons)

# IV_b_00_00
content = [
    ContentUnit("text", "Leaving the library:"),
    ContentUnit("text", "- Well, let's go to lunch?"),
    ContentUnit("text", "- Yep", delay=3),
    ContentUnit("text", "In the dining room:"),
    ContentUnit("text",
                "A familiar face sits at the table. Wow, I see Pasha, who was my escort during selection!"),
    ContentUnit("text",
                "- Let's go there. This is Pasha, maybe you know him, he was a volunteer during university selections."),
    ContentUnit("text", "- Okay"),
    ContentUnit("text", "- Hello, Pasha, how are you?"),
    ContentUnit("text",
                "- Whoa, I remember you, you really love to sleep and you're always late because of that. I'm fine, finally changed the meal plan! I took it 3 times a day, 7 days a week, instead of 5. So I don’t care about cooking: I come, I eat and I leave! Is it not a miracle?"),

]
buttons = {
    "Where can I choose it? Either 5 or 7 days per week?": "IV_b_01_00",
    "How did you change it?": "IV_b_01_01",
}
states["IV_b_00_00"] = State(content, buttons)

# IV_b_01_00
content = [
    ContentUnit("text",
                "- Of course, you can. Actually, you can see all the meal plans when you will choose it."),
    ContentUnit("text", "- Where?"),
    ContentUnit("text", "- In your personal account: my.university.innopolis.ru"),
    ContentUnit("text",
                "- Thank you! Listen, I wanted to ask you something. As far as I understood, there is no need to deliver our assignments from hand to hand, so how does it work? I mean how can I provide my assignment solution for professor?"),
    ContentUnit("text",
                "- It is pretty simple. There is a place where you can upload all your assignments and see your grades for each course. This place is called Moodle: moodle.university.innopolis.ru."),

]
buttons = {"Next": "IV_c_00_00"}
states["IV_b_01_00"] = State(content, buttons)

# IV_b_01_01
content = [
    ContentUnit("text", "In your personal account: my.university.innopolis.ru"),
    ContentUnit("text",
                "-  I got another question. I know that rule «Students have fun when there is no exam» doesn't work here, so the exams are distributed throughout the semester."),
]
buttons = {
    "How can I know when these exams will be?": "IV_b_02_00",
    "How much do they weight from the final grade?": "IV_b_02_00",
}
states["IV_b_01_01"] = State(content, buttons)

# IV_b_02_00
content = [
    ContentUnit("text",
                "- There is a some place called Moodle: moodle.university.innopolis.ru. You will find all answers on your possible questions. So just keep calm, my friend!")
]
buttons = {
    "Next": "IV_c_00_00"
}
states["IV_b_02_00"] = State(content, buttons)

# IV_c_00_00
content = [
    ContentUnit("text",
                "The same evening, everyone gathered in your room to chat and eat pizza. It turns out that there are 2 places where you can order it."),
    ContentUnit("text",
                "You noticed that one of your friends has a great hoodie with “Innopolis University” print."),
    ContentUnit("photo", photos.urls["hoody"]),
    ContentUnit("text", "Wow, that hoodie is amazing! I really want this too! You ask:")
]
buttons = {
    "How did you get it?": "IV_c_01_00",
    "You robbed the university? (pointing to a hoodie)": "IV_c_01_01"
}
states["IV_c_00_00"] = State(content, buttons)

# IV_c_01_00
content = [
    ContentUnit("text",
                "- Got what? Ah, I see. I just helped to Student Affairs Department a couple of times, volunteered at University events, and, of course, I participated in some 'Activities'. And voilà – got Innopoints for the hoodie."),
    ContentUnit("text", "- And how many innopoints does it cost? And how did you know that you have enough?"),
    ContentUnit("text",
                "- You really don’t read anything that comes to us via email? I guess this one is 1800 innopoints, but you can always check how many do you have here: uis.university.innopolis.ru/innopoints/products."),
    ContentUnit("text", "- I hear it for the first time…"),
    ContentUnit("text", "A roommate intervened in the dialogue:"),
    ContentUnit("text",
                "- Did you know that an idea of innopoints was invented by students and Student Affairs Department together? Just a minute of the history from me."),

]
buttons = {"How did you know that?": "IV_c_02_00",
           "It's very tiring to ask something all day. And actually, I really wanna sleep.": "IV_c_02_01"}
states["IV_c_01_00"] = State(content, buttons)

# IV_c_01_01
content = [
    ContentUnit("text",
                "- Haha, no! I worked tirelessly: I helped to Student Affairs Department a couple of times, volunteered at University events, and, of course, I participated in some 'Activities'. And voilà – got Innopoints for the hoodie."),
    ContentUnit("text", "- And how many does it cost?"),
    ContentUnit("text", "- I guess this one is 1800 innopoints."),
    ContentUnit("text", "- But how can I order and get items for innopoints?"),
    ContentUnit("text",
                "- There is a site: uis.university.innopolis.ru/innopoints/products.   You can leave an application to get innopoints there. Actually, uis.university.innopolis.ru is very useful place where you can get an actual news about university and city at all."
                "- Damn, that's cool, I will try earn some points for such hoodie!")
]
buttons = {"How did you know that?": "IV_c_02_00",
           "It's very tiring to ask something all day. And actually, I really wanna sleep.": "IV_c_02_01"}
states["IV_c_01_01"] = State(content, buttons)
# IV_c_02_00
content = [
    ContentUnit("text", "- Company’s secret. Hint: communication with people can be very useful.")
]
buttons = {"Go sleep": "IV_c_02_01"}
states["IV_c_02_00"] = State(content, buttons)

# IV_c_02_01
content = [
    ContentUnit("text", "You went to your room, fell into bed and fell asleep.")
]
buttons = {"Start new day": "V_a_00_00"}
states["IV_c_02_01"] = State(content, buttons)

# V_a_00_00
content = [
    ContentUnit("text", "It's your 5th day in summer school"),
    ContentUnit("text", "You wake up early in the morning with a smile on your face."),
    ContentUnit("text", "Nothing means trouble."),
    ContentUnit("text", " Hmm... What do we have today?"),
]
buttons = {
    "Student’s meeting": "V_a_01_00",
    "Exams": "V_a_01_01"
}
states["V_a_00_00"] = State(content, buttons)

# V_a_01_00
content = {
    True: [
        ContentUnit("text", "Sure! The meeting is today. Wait a minute, what meeting..."),
        ContentUnit("text", "Ah! No! It’s exams, of course. Stop. Exams!!!"),
        ContentUnit("text", "Well, that’s okay. You studied well. Everything should go fine."),
        ContentUnit("text",
                    "The morning procedures. Opening the faucet, you get a sudden powerful stream of water. Slushing yourself and half of the room, water abruptly ends. After that there’re sounds of the beast roar and snort from the tap."),
    ],
    False: [
        ContentUnit("text", "Sure! It’s meeting today. Wait a minute, what meeting..."),
        ContentUnit("text", "Ah! No! It’s exams, of course. Stop. Exams!!!"),
        ContentUnit("text", "Well, that’s okay. You studied well. Everything should go fine."),
        ContentUnit("text",
                    "The morning procedures. Opening the faucet, you get a sudden powerful stream of water. Slushing yourself and half of the room, water abruptly ends. After that there’re sounds of the beast roar and snort from the tap."),
    ]
}
buttons = {
    "Close the faucet": "V_a_02_00"
}
states["V_a_01_00"] = State(content, buttons)

# V_a_01_01
content = {
    True: [
        ContentUnit("text", "I remember! There are exams today"),
        ContentUnit("text", "Well, that’s okay. You studied well. Everything should go fine."),
        ContentUnit("text",
                    "The morning procedures. Opening the faucet, you get a sudden powerful stream of water. Drenching half the room with you, water also abruptly ends. Finally, sounds of the beast roar, and snort from the tap."),

    ],
    False: [
        ContentUnit("text", "I remember! There are exams today"),
        ContentUnit("text", "Well, that’s okay. You studied well. Everything should go fine."),
        ContentUnit("text",
                    "The morning procedures. Opening the faucet, you get a sudden powerful stream of water. Drenching half the room with you, water also abruptly ends. Finally, sounds of the beast roar, and snort from the tap."),

    ]
}
buttons = {
    "Turn off the tap.": "V_a_02_00"
}
states["V_a_01_01"] = State(content, buttons)

# V_a_02_00
content = {
    True: [
        ContentUnit("text", "You turn off the tap... start the water again. It goes fine."),
        ContentUnit("text", "After finishing the procedures and a breakfast, you are going to your first exam."),
        ContentUnit("text",
                    "The professor explains  you that there’ll will be 'closed books' exam which means that everything (books, notes, phones, laptops, tablets etc.) should be closed during the exam, except your eyes, of course."),
        ContentUnit("text",
                    "Compliance with the rules is followed by the professor. TAs are monitoring the lecture-hall and keeping their eyes on students."),
    ],
    False: [
        ContentUnit("text", "You turn off the tap... start the water again. It goes fine."),
        ContentUnit("text", "After finishing the procedures and a breakfast, you are going to your first exam."),
        ContentUnit("text",
                    "The professor explains  you that there’ll will be 'closed books' exam which means that everything (books, notes, phones, laptops, tablets etc.) should be closed during the exam, except your eyes, of course."),
        ContentUnit("text",
                    "Compliance with the rules is followed by the professor. TAs are monitoring the lecture-hall and keeping their eyes on students."),
    ]
}
buttons = {
    "Well, okay. I will write by myself.": "V_a_03_00",
    "Well, my friends will not leave me in trouble": "V_a_03_01"
}
states["V_a_02_00"] = State(content, buttons)

# V_a_03_00
content = [
    ContentUnit("text", "However this idea quickly flew out of your head when you heard that..."),
    ContentUnit("text",
                "All students were explained that cheating is also punishable by immediate failure of the exam, like any other behaviour against the rules."),
    ContentUnit("text", " You sit down and start the final exam."),
    ContentUnit("text",
                "After an hour and a half of hard work you turn in the paper, and TAs remind you that the marks you will be able to see later in Moodle."),
    ContentUnit("text",
                "- The third task of the assignment had the vague wording, - someone from the students complained."),
    ContentUnit("text", "- Yes!.. True!.. Exactly... – spoke others."),
    ContentUnit("text",
                "- Okay, we will revise it again, but do not promise anything so far, - replies the professor."),
    ContentUnit("text",
                "- And for everyone who thinks that the assessment is unfair and wishes to challenge it, after the results we will have an appeal, - added teaching assistant."),
    ContentUnit("text", "The students dispersed in all directions. There are 2 hours until the next exam (English)."),
    ContentUnit("text", "You noticed that you left your notes  and headed off to your room."),
    ContentUnit("text", "Entering the room, you’re taking the notebook from the table and moving toward the exit."),
    ContentUnit("text",
                "The strange sound coming from the bathroom stops you. But you're alone in the room..."),
    ContentUnit("text",
                "YOpening the door to the bathroom, you see such a picture. The faucet is broken and the water gushes up to the ceiling."),
    ContentUnit("text", "Your feet are already in the puddle and your skin crawls. What to do?"),
]
buttons = {
    "Write to your friend in Telegrem": "V_a_04_00",
    "To run out and ask for help": "V_a_04_01"
}
states["V_a_03_00"] = State(content, buttons)

# V_a_03_01
content = [
    ContentUnit("text", "Although this idea quickly flew out of your head when you heard that..."),
    ContentUnit("text",
                "All students were explained that cheating is also punishable by immediate failure of the exam, like any other violation."),
    ContentUnit("text", " You sit down and take the final exam."),
    ContentUnit("text",
                "After 1.5 hours of hard work you hand over the forms, and TAs remind you that the marks you will be able to see later in Moodle."),
    ContentUnit("text",
                "- In the third issue of the assignment problem was not clearly formulated, - asked someone from the students."),
    ContentUnit("text", "- Yes!.. True!.. Exactly... – speak others."),
    ContentUnit("text",
                " - Okay, we will revise it again, but so far do not promise anything, - replied the professor."),
    ContentUnit("text",
                "And for everyone who thinks its assessment is unfair and wish to challenge it, after the results we will have an appeal, - added teacher assistant."),
    ContentUnit("text", "The students dispersed in all directions. There are 2 hours until the next exam."),
    ContentUnit("text", "You noticed that you left your notes of the subject in the room and go there."),
    ContentUnit("text", "Entering the room, you take the notebook off the table and heading for the exit."),
    ContentUnit("text",
                "The strange sound coming from the bathroom stops you. But you're alone in the room..."),
    ContentUnit("text",
                "You see that the faucet is broken and water gushes up to the ceiling."),
    ContentUnit("text", "Your feet are already in the puddle and feel shiver. What to do?"),
]
buttons = {
    "Write to your friend in Telegrem": "V_a_04_00",
    "Run out and ask for a help": "V_a_04_01"
}
states["V_a_03_01"] = State(content, buttons)

# V_a_04_00
content = {
    True: [
        ContentUnit("text",
                    "The roommate says you need to contact the dorm administrator, so they will send the technician."),
        ContentUnit("text", "Here is the link of 'Hotel Uni Reception':@hoteluni")
    ],
    False: [
        ContentUnit("text",
                    "The roommate says you need to contact the dorm administrator, so they will send the technician."),
        ContentUnit("text", "Here is the link of 'Hotel Uni Reception':@hoteluni")

    ]
}
buttons = {
    "Write to administration": "V_a_05_00"
}
states["V_a_04_00"] = State(content, buttons)

# V_a_04_01
content = [
    ContentUnit("text", "Stamping out of the room in the hallway, you look around."),
    ContentUnit("text", "No one! Of course, everyone is on the exam!"),
    ContentUnit("text", "You need to ask your friend for help.")
]
buttons = {
    "Write to your friend in Telegrem": "V_a_04_00"
}
states["V_a_04_01"] = State(content, buttons)

# V_a_05_00
content = [
    ContentUnit("text",
                "The plumber has been sent for. Also the administrator told you to close the crane by shutting off water supply valve under the sink."),
    ContentUnit("text", "Of course! Close the crane! You forgot it."),
    ContentUnit("text", "You quickly find the valve and turn it on 90 degrees."),
    ContentUnit("text", "The jet of water is quickly falling down."),
    ContentUnit("text", "Finding a mop, you as soon as possible start to collect the water."),
    ContentUnit("text", "At the end of 5 minutes the plumber has come, and you run to the University."),
    ContentUnit("text", "What a day! Okay with the exams, but also such an adventure!"),
    ContentUnit("text", "It’s good that ”Uni Hotel Reception” responded quickly."),
    ContentUnit("text",
                "In the evening of the same day you tell the neighbors epic story with waterfalls and maelstroms.."),
    ContentUnit("text", "So what? It is okay to stretch a story a little sometimes. =)"),
    ContentUnit("text", "It turns out that there was a reason, why the tap growled at you in the morning."),
    ContentUnit("text", "After watching the movie you and your roommate get news in Moodle."),
    ContentUnit("text", "Looking at the results, you see the marks for exams."),
    ContentUnit("text", "”А”"),
    ContentUnit("text", "That was the end of that crazy Friday."),
]
buttons = {
    "Start new day": "VI_a_00_00",
    "Start from the beginning": "I_a_00_00"
}
states["V_a_05_00"] = State(content, buttons)

# VI_a_00_00
content = {
    True: [
        ContentUnit("text", "Here comes the last day in Bootcamp."),
        ContentUnit("text", "Vanya as always is already awake."),
        ContentUnit("text",
                    "- You are still sleeping! I have been helping with preparation for Ethno Village for almost 2 hours!"),

    ],
    False: [
        ContentUnit("text", "Here comes the last day in Bootcamp"),
        ContentUnit("text", "Yana as always is already awake."),
        ContentUnit("text",
                    "- You are still sleeping! I have been helping with preparation for Ethno Village for almost 2 hours!"),
    ]
}
buttons = {
    "What?": "VI_a_01_00",
    "Are you taking part in it, I did not know?": "VI_a_01_01"
}
states["VI_a_00_00"] = State(content, buttons)

# VI_a_01_00
content = [
    ContentUnit("text",
                "Vanya: - Come on! You forgot about this event, there guys will tell us about their cities and regions and I help with the organization."),
    ContentUnit("text", "- Is it so much fun? Why are you helping"),
    ContentUnit("text",
                "- Yes! Moreover, I will get innopoints for that, I really loved the hoodie and I want to start saving up as soon as possible."),

]
buttons = {
    "Are there a lot of things to spend innopoints on?": "VI_a_02_00",
    "Are innopoints given only for volunteering?": "VI_a_02_01",
    "Oh, yeah, I remember we saw a girl in a hoodie, she said something about it.": "VI_a_02_00"
}
states["VI_a_01_00"] = State(content, buttons)

# VI_a_01_01
content = [
    ContentUnit("text",
                "- Yes! I want to save up for dinner with the Professor, I think it's very interesting! It costs a lot, so I am trying to start to save as early as possible."),
    ContentUnit("text",
                "- What?! You want to take professors out to dinner?! Do you get paid for help? I don't understand..."),
    ContentUnit("text",
                "- Haha, no, of course. For volunteering at events I will be given innopoints, they can be exchanged for dinner with the Professor.")

]
buttons = {
    "Are there a lot of things to spend innopoints on?": "VI_a_02_00",
    "Are innopoints given only for volunteering?": "VI_a_02_01",
    "Oh, yeah, I remember we saw a girl in a hoodie, she said something about it.": "VI_a_02_00"
}
states["VI_a_01_01"] = State(content, buttons)

# VI_a_02_00
content = [
    ContentUnit("text",
                "- Yeah. There are a lot of Souvenirs with symbols of the University: hoodies, mugs, backpacks and much more. Also innopoints can be exchanged for certificates of partners of IU."),
    ContentUnit("text", "- It's time for Breakfast, Sleepyhead!"),
]
buttons = {
    "Go to breakfast": "VI_b_00_00"
}
states["VI_a_02_00"] = State(content, buttons)

# VI_a_02_01
content = [
    ContentUnit("text",
                "- No. For any activity, such as participating in hackathons and sports competitions, public articles and research and so on."),
    ContentUnit("text", "- It's time for Breakfast, Sleepyhead!"),
]
buttons = {
    "Go to breakfast": "VI_b_00_00"
}
states["VI_a_02_01"] = State(content, buttons)

# VI_b_00_00
content = [
    ContentUnit("text", "In the dining room:"),
    ContentUnit("text", "Hearing two students arguing about something..."),
    ContentUnit("text",
                "- As for me, I like living in quintuple room! Separate spacious kitchen and bath! If someone is sleeping you can sit in the kitchen without interrupting the neighbor. And much more fun, there is always someone to help you with your homework."),
    ContentUnit("text",
                "- Yeah, but there's always toilet queue, I guess... And I know whose food exactly is in the fridge if it is not mine. It is, of course, a bit more expensive. Room for five person is approximately 2100 rub/month, and for two - 2400 rubles/month."),
    ContentUnit("text", "- So, after all, did you decide to move to double room?"),
    ContentUnit("text", "- Yes, today I will go to the campus administrator and write an application"),
    ContentUnit("text",
                "- And I'll probably move to an apartment in Zalesny township or in Kazan, because I want to take my cat from the home, but it is impossible if I live in dorm."),
    ContentUnit("text", "..."),
    ContentUnit("text", "- Bon appetit."),
    ContentUnit("text", "- Thanks, you too."),
    ContentUnit("text",
                "- I'm already thinking where to go next summer! Don’t you know when is the end of the spring semester?")
]
buttons = {
    "It seems, May 14 is the last day.": "VI_b_01_00",
    "No, I do not know.": "VI_b_01_01",
}
states["VI_b_00_00"] = State(content, buttons)

# VI_b_01_00
content = [
    ContentUnit("text",
                "Ivan: - Yes, exactly! Long vacations then... Oh, I forgot about internship, so actually not so long vacations."),
    ContentUnit("text", "- And when will it be? And what is it actually?"),
    ContentUnit("text",
                "- Accurate information will be told us by the end of the year, I think. Therefore,it is better not to do exact plans on your summer, at least the beginning of the summer better try to leave free. I know that internships are divided into administrative and scientific. Also we can go to some companies, but only after second year of studying."),

]
buttons = {
    "Alright, let’s see it later.": "VI_b_02_00",
    "What is the difference between administrative and scientific internships?": "VI_b_02_01"
}
states["VI_b_01_00"] = State(content, buttons)

# VI_b_01_01
content = [
    ContentUnit("text",
                "Ivan: - in the middle of  May I think... Yes, exactly May 14 is last day, only because there is more training."),
    ContentUnit("text", "- And when will it be? And what is it actually?"),
    ContentUnit("text",
                "- Accurate information will be told us by the end of the year, I think. Therefore,it is better not to do exact plans on your summer, at least the beginning of the summer better try to leave free. I know that internships are divided into administrative and scientific. Also we can go to some companies, but only after second year of studying."),

]
buttons = {
    "Alright, let’s see it later.": "VI_b_02_00",
    "What is the difference between administrative and scientific internships?": "VI_b_02_01"
}
states["VI_b_01_01"] = State(content, buttons)

# VI_b_02_00
content = [
    ContentUnit("text", "After breakfast, you had only one choice:")
]
buttons = {
    "To go on festival.": "VI_c_00_00"
}
states["VI_b_02_00"] = State(content, buttons)

# VI_b_02_01
content = [
    ContentUnit("text",
                "- On administrative internship students do various projects for the University. And doing scientific one is made to improve your skills in a specific sphere, for example, if you interested in robotics, you can go for an internship in the Professor Mavridis’s lab."),

]
buttons = {
    "Interesting, thank you.": "VI_b_02_00"
}
states["VI_b_02_01"] = State(content, buttons)

# VI_c_00_00
content = [
    ContentUnit("text", "At the festival:"),
    ContentUnit("text", "The fest has just started."),
    ContentUnit("text",
                "There are a lot of people in the reading hall: some in national dresses, someone brought their national treats."),
    ContentUnit("text", "It looks like people here are having fun. Would you join them?"),
]
buttons = {
    "I think so too!": "VI_c_01_00",
    "Are these kind of events are frequent here?": "VI_c_01_00"
}
states["VI_c_00_00"] = State(content, buttons)

# VI_c_01_00
content = [
    ContentUnit("text", "Standing near the student: - Then you'll be happy that holidays here are almost every day."),
    ContentUnit("text", "Halloween(October)"),
    ContentUnit("photo", photos.urls["halloween"]),
    ContentUnit("text", "Student New year (December)"),
    ContentUnit("photo", photos.urls["new_year"]),
    ContentUnit("text", "Student day (January)"),
    ContentUnit("photo", photos.urls["student_day"]),
    ContentUnit("text", "Valentine's day (February)"),
    ContentUnit("photo", photos.urls["valentine_day"]),
    ContentUnit("text", "23/8 (March)"),
    ContentUnit("photo", photos.urls["23/8"]),
    ContentUnit("text", "Independents Weekend Activities (April)"),
    ContentUnit("photo", photos.urls["IAW"]),
    ContentUnit("text", "Slippers of the Year (May)"),
    ContentUnit("photo", photos.urls["slippers"]),
    ContentUnit("text", "One of the most fun days in BootCamp came to an end.")
]
buttons = {
    "Start new day": "VII_a_00_00"
}
states["VI_c_01_00"] = State(content, buttons)

# VII_a_00_00
content = [
    ContentUnit("text", "Catch up with friends in the morning..."),
    ContentUnit("text",
                "- Hey, good morning! Today is a holiday! I don’t feel like sitting in the campus, let's go outside."),
    ContentUnit("text",
                "- Alright. Well, where will we go? I personally would like to see a place for barbecue that they have here."),
    ContentUnit("text", "- And I wanted to buy a couple of books in a bookstore..."),
]
buttons = {
    "See the barbecue place": "VII_a_01_00",
    "Go to the bookstore": "VII_a_01_01"
}
states["VII_a_00_00"] = State(content, buttons)

# VII_a_01_00
content = [
    ContentUnit("text",
                "- Well, let's split up then, we'll see where the barbecue place is, but you can go to the bookstore with Vika, after that meet us at the pizzeria 'Cacio e Vino'."),
    ContentUnit("text", "- Okay"),
    ContentUnit("text", "A few minutes later..."),
    ContentUnit("text",
                "- Where is this place? And don’t you need to ask someone to use the place?."),
    ContentUnit("text",
                "- A second year guy said that we can just write in the chat saying we’ll took it temporarily and that’s all. We're almost there, it is behind the Residential Community, where “Bakhetle” is, just a little bit further."),
    ContentUnit("photo", photos.urls["mangal"])
]
buttons = {
    "Go to the pizzeria": "VII_b_00_00",
}
states["VII_a_01_00"] = State(content, buttons)

# VII_a_01_01
content = [
    ContentUnit("text",
                "- Well then, let's split up, we'll buy books, and you can go to examine the barbecue place, and then we’ll meet at the pizzeria 'Cacio e Vino'"),
    ContentUnit("text", "- On the way to the bookstore..."),
    ContentUnit("text", "- And what do you want to buy there?"),
    ContentUnit("text",
                "- I heard, they got new programming books, want to check if I can buy one. Actually, there are a lot of books you can buy there. By the way, we can already see it from here, it’s called 'House of Books'."),
    ContentUnit("photo", photos.urls["book1"]),
    ContentUnit("text", "You decided:")
]
buttons = {
    "Go to the pizzeria": "VII_b_00_00",
}
states["VII_a_01_01"] = State(content, buttons)

# VII_b_00_00
content = [
    ContentUnit("text", "At the pizzeria at the address: 100 Sportivnaya St."),
    ContentUnit("photo", photos.urls["pizza_out"]),
    ContentUnit("text", "- It’s so comfy here! I love it!"),
    ContentUnit("text",
                "- Yes, and the pizza is delicious. The guys from the second year say they are very happy that such a place appeared where you can come and spend some time with your friends."),
    ContentUnit("photo", photos.urls["pizza_in"]),
]
buttons = {
    "And what about the bar 108?": "VII_b_01_00",
    "Maybe we can go and take a look at the sports areas after that?": "VII_b_01_01"
}
states["VII_b_00_00"] = State(content, buttons)

# VII_b_01_00
content = [
    ContentUnit("text", "- And what about the bar 108? Can’t we have some time there? It has opened earlier."),
    ContentUnit("text",
                "- Yes, it is also great, just without the Italian cuisine. They are, by the way, right on the way to “Bakhetle”, just closer. Convenient.",
                delay=3),
    ContentUnit("text", "You decided to:")
]
buttons = {
    "Go home": "VII_b_02_00"
}
states["VII_b_01_00"] = State(content, buttons)

# VII_b_01_01
content = [
    ContentUnit("text", "- Yeah, let’s go! Cool idea."),
    ContentUnit("text",
                "- I heard, residents of the city can use the tennis court, the basketball and volleyball areas for free."),
    ContentUnit("text", "- I run everyday on the running track there."),
    ContentUnit("text", "- Where is it, guys?"),
    ContentUnit("text",
                "- Haven’t you seen?? Right in front of the RC, but on the other side, relatively close to the sports center."),
    ContentUnit("text",
                "- Well, I'm sorry, I can’t see too much with my vision... You all are standing blurred in front of me..."),
    ContentUnit("text", "You decided to:")
]
buttons = {
    "Go to the courts": "VII_b_02_01",
}
states["VII_b_01_01"] = State(content, buttons)

# VII_b_02_00
content = [
    ContentUnit("text", "On the way home..."),
    ContentUnit("text", "- These are the sport courts."),
    ContentUnit("photo", photos.urls["court"]),
    ContentUnit("photo", photos.urls["track"]),
    ContentUnit("text", "- Look, some people are skateboarding next to the Sport Center "),
    ContentUnit("photo", photos.urls["skates"]),
    ContentUnit("text",
                "- Yeah, look at that fool who came by and threw the gum next to them on the pavement. I worry if they cling to it and fall."),
]
buttons = {
    "Call the guy and ask him to pick up and throw his gum in the trash.": "VII_b_03_00",
    "Who cares...": "VII_b_03_01"
}
states["VII_b_02_00"] = State(content, buttons)

# VII_b_02_01
content = [
    ContentUnit("text", "On the way courts..."),
    ContentUnit("text", "- These are the sport courts."),
    ContentUnit("photo", photos.urls["court"]),
    ContentUnit("photo", photos.urls["track"]),
    ContentUnit("text", "- Look, some people are skateboarding next to the Sport Center "),
    ContentUnit("photo", photos.urls["skates"]),
    ContentUnit("text",
                "- Yeah, look at that fool who came by and threw the gum next to them on the pavement. I worry if they cling to it and fall."),
]
buttons = {
    "Call the guy and ask him to pick up and throw his gum in the trash.": "VII_b_03_00",
    "Who cares...": "VII_b_03_01"
}
states["VII_b_02_01"] = State(content, buttons)

# VII_b_03_00
content = [
    ContentUnit("text",
                "- Well done! He even seems to be ashamed, he apologized and threw it in the trash, fascinating..."),
    ContentUnit("text",
                "You continued to go home.")
]
buttons = {
    "Next": "VII_c_00_00"
}
states["VII_b_03_00"] = State(content, buttons, callback=end)

# VII_b_03_01
content = [
    ContentUnit("text", "- So, let’s take a ball from somebody and play basketball?"),
    ContentUnit("text", "- Why not? Let's do this."),
]
buttons = {
    "Next": "VII_c_00_01"
}
states["VII_b_03_01"] = State(content, buttons)

# VII_c_00_00
content = [
    ContentUnit("text", "A couple of hours later. Evening."),
    ContentUnit("text", "So beautiful evening... Amazing sunsets..."),
    ContentUnit("photo", photos.urls["sunset"]),
]
buttons = {
    "Start from the beginning": "I_a_00_00"
}
states["VII_c_00_00"] = State(content, buttons)

# VII_c_00_01
content = [
    ContentUnit("text", "A couple of hours later. Evening."),
    ContentUnit("text",
                "What a headache ... what are these sounds ... It seems that someone is trying to say ... Ah ... it hurts!"),
    ContentUnit("text", "- Hey, wake up! Get up!"),
    ContentUnit("text", "- My head hurts."),
    ContentUnit("text",
                "- Unsurprisingly ... Looks like your skate flew away from your feet, and your head hit the curb edge, you have to be careful. Not far from here is a medical center, right around the campus, I'll take you there."),
]
buttons = {
    "Accept": "VII_c_01_00",
    "Refuse": "VII_c_01_01"
}
states["VII_c_00_01"] = State(content, buttons, callback=end)

# VII_c_01_00
content = [

    ContentUnit("text", "- Thank you. How could this happen... I’ve been riding for 5 years!"),
    ContentUnit("text",
                "- I think the wheel clung to a huge piece of gum that someone here has thrown! I don’t like these people, it is so clean here!! Why do they spoil everything."),
    ContentUnit("text", "- Meh... This is karma..."),
    ContentUnit("text", "This is the end of your BootCamp. But you got not only a concussion, but also friends :)")
]
buttons = {
    "Start from the beginning": "I_a_00_00"
}
states["VII_c_01_00"] = State(content, buttons)

# VII_c_01_01
content = [
    ContentUnit("text",
                "- Well, as you wish. I hope you are okay. But please, go to the pharmacy, buy something for yourself. Write to @InnoHelpBot, here you can get any information about different places and buses."),
    ContentUnit("text", "- Thanks, I will."),
    ContentUnit("text", "This is the end of your BootCamp. But you got not only a concussion, but also friends :)")
]
buttons = {
    "Start from the beginning": "I_a_00_00"
}
states["VII_c_01_01"] = State(content, buttons)
