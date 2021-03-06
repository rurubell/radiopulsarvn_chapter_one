#День первый


label day_01:
    image Midori_01 = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_01.png"
    
    stop music fadeout 1
    play environment_sounds "sounds/environment/Sea.mp3" fadein 2 fadeout 1
    scene Midori_Sea_BG with Dissolve( my_dissolve_05 )
    window hide
    pause 1.0
    
    show Midori_01 with Dissolve( my_dissolve_05 )
    
    window show
    
    "Передо мной стояла девушка и улыбалась."
    "Я робко поздоровался."
    
    "П-привет!"

    "Меня Кендзи зовут. Танака Кендзи!"
    
    kenji "А тебя?"

    "Девушка не ответила. Впрочем, я знал её имя. Мидори. И она явно школьница, раз надела школьный купальник."
    "Наверное, вырвалась с подружками на море, сейчас же лето, каникулы..."
    
    "На вид Мидори лет шестнадцать, не больше. А это самый замечательный возраст!"
    "Будь мне сейчас столько же, я бы с удовольствием побегал вместе с Мидори по морскому берегу."
    "Сыграл бы с ней в волейбол... Ух! "

    "Но, к сожалению, мне уже давно не шестнадцать."

    kenji "Мне тридцать лет, Мидори! Тридцать!"

    "Похоже, её совсем не смутили эти слова, и она по-прежнему улыбалась мне."
    "Приободрившись, я продолжил."

    kenji "А ещё я хиккикомори! Никчёмный тридцатилетний хиккикомори!"
    
    "Лицо Мидори не дрогнуло. Мне даже показалось, что её улыбка стала чуть добрее, а в глазах заплясали радостные искорки."
    
    kenji "Конечно, Мидори! Будь я хоть самым последним ублюдком на свете, ты бы ни за что не отвернулась от меня!"
    kenji "Я же для тебя самый дорогой человек на свете!"
    kenji "Я твой отец!"
    kenji "Даже больше. Я твой создатель!"
    
    kenji "И ты должна меня простить! Потому что я тебя... продал!"
    
    "Мне кажется, или веселья на лице девушки поубавилось? Я поспешил её успокоить."
    
    kenji "Но ты не бойся! Я продал тебя очень хорошему человеку! Надеюсь..."
    
    #ЦГ - Мидори в графическом редакторе
    image Midori_Sea_BG_Non_Animated = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Midori_Sea_BG.png"
    image Midori_GE_Interface = "images/cg/DAY_01/01a_Green-Haired_Girl/GE_Interface.png"
    image Midori_02 = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_02.png"
    image Midori_In_GE_01:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_02"
        contains:
            "Midori_GE_Interface"
    
    
    scene Midori_In_GE_01 with Dissolve( my_dissolve_05 )
    play environment_sounds "sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    
    "Я потёр глаза и чуть отодвинулся от монитора."
    "Да, Мидори вышла очень миленькой. Думаю, заказчик будет доволен."
    
    play sound "sounds/sounds/Mobile_Phone_Vibration.mp3"
    "Вдруг завибрировал телефон. Похоже, мне прислали сообщение!"
    "Писал тот парень, что заказал рисунок с Мидори. Вовремя он появился!"

    zak "Йоу, чувак!"
    kenji "Привет. Твой рисунок готов, сейчас перешлю."
    
    "Я отправил картинку заказчику и стал дожидаться его реакции."
    "Если честно, я всегда волнуюсь в такие моменты, хоть и занимаюсь этим уже не первый год."

    zak "Это шедевр, чувак!"

    "Я самодовольно улыбнулся. "
    zak "Но..."
    
    "Чёрт! Похоже, ему что-то не нравится! Неужели я где-то накосячил? Надеюсь, он не хочет сбить обговорённую цену."
    "А вдруг ему больше не нужен этот заказ и он не будет платить остальную сумму за рисунок? Я озвучил свой вопрос в чате."
    
    zak "Нет, чувак! Не в этом дело! Я заплачу! Но понимаешь, наши с Мидори отношения..."
    zak "Кажется, они перешли на новый уровень!"
    kenji "Ваши отношения?!"
    zak "Ага, чувак... Раньше она казалась мне такой чистой и непорочной..."
    zak "А сейчас я всё больше замечаю, какая она женственная... Какая притягательная..."
    
    "Единственное, чего мне хотелось сейчас — получить свои деньги, а этот парень нёс какую-то чушь."
    
    zak "Какая у неё тонкая шея... А её ямочки на ключицах... Ох..."
    
    "Похоже, он был не в себе. "

    zak "Чувак, ты можешь немного переделать рисунок?"
    kenji "Переделать? Но мы же все обсудили! Я показывал наброски!"
    zak "Я заплачу больше! Сколько ты скажешь! Но только измени его, совсем чуть-чуть!"

    "Я вздохнул. Опять эти капризы заказчика."

    kenji "И что мне переделать?"
    zak "Ты можешь сделать, чтобы Мидори на этом рисунке выглядела немного погорячее?"
    kenji "Погорячее?"
    zak "Ага! Сделай её похотливей, что ли..."
    kenji "Ты хочешь, чтобы я раздел её?"
    zak "Нет, чувак! Оставь купальник на месте! Так даже интереснее! Может, выражение лица поменять?"
    zak "Ну, чтобы сразу стало понятно, чего она хочет!"
    
    "Самому мне казалось, что такой милой девочке, как Мидори, хочется побегать с подружками по пляжу без всякой задней мысли."
    "Однако спорить с этим парнем я не стал. Он заказал Мидори, он её хозяин, а мне остаётся только одно — выполнить все его прихоти."
    "Я попросил заказчика написать мне через полчаса, а сам принялся за рисунок."

    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_03 = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_03.png"
    image Midori_In_GE_02:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_03"
        contains:
            "Midori_GE_Interface"
    
    pause 0.5
    
    scene Midori_In_GE_02 with Dissolve( my_dissolve_05 )
    
    "Да, теперь определённо можно сказать, чего хочет Мидори."
    "Вот только хочет ли она этого на самом деле? Взяла ли Мидори эту штуку в рот по своей воле, или я её заставил?"
    "Чёрт! Я слишком много об этом думаю! "
    "Я покачал головой и прошептал."
    
    kenji "Прости меня, Мидори... Я не хотел..."
    
    zak "Эм... Рисунок отличный. Но чувак, кажется, я понял, чего действительно хочу!"
    kenji "Что опять?"
    zak "Я всё не мог понять, чего не хватает! Но теперь знаю!"
    zak "Ты можешь нарисовать ей ахегао-личико?"
    
    "Ну, по крайней мере, теперь я точно знал, что нужно сделать."
    "К несчастью для меня, лицо Мидори опять нуждалось в серьёзной редактуре."
    
    kenji "Надеюсь, это всё?"
    zak "Всё, чувак! Просто сделай ей ахегао, и я заплачу, сколько ты скажешь."
    
    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_04 = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_04.png"
    image Midori_In_GE_03:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_04"
        contains:
            "Midori_GE_Interface"
    
    pause 0.5
    
    scene Midori_In_GE_03 with Dissolve( my_dissolve_05 )
    
    "Пока я перерисовывал физиономию девушки, на душе у меня становилось всё гаже. "
    "Я столько времени потратил на первоначальный рисунок, столько труда в него вложил! "
    "Да я почти сроднился с Мидори!"
    "А сейчас мне приходится издеваться над собственным творением ради этого похотливого болвана!"

    "Надо было просто надавить на этого парня и забрать свои деньги. "
    "Пусть несёт рисунок на доработку другому художнику. "
    "Или поступить как истинный джентльмен и вообще не отдавать ему Мидори. "
    "Ахегао-личико, ишь чего захотел! "
    "Эх... Ну почему я такой мягкотелый?"
    
    "Но все стало только хуже — этот парень вновь был чем-то недоволен."
    
    zak "Чувак... Можешь добавить ещё кое-что?"
    kenji "Я нарисовал всё, что ты хотел, разве нет? Я не могу переделывать этот рисунок вечно!"
    zak "Я знаю, чувак! И я перевёл деньги! Ты клёвый художник, но пожалуйста, доделай этот рисунок."
    zak "Осталось совсем чуть-чуть до совершенства!"
    
    "Я поспешил проверить состояние своего счёта."
    "А он щедр! Парень заплатил за работу в два раза больше оговорённого. "
    "Мне даже стало стыдно за то, что я так плохо думал о нём."
    
    zak "Это не займёт много времени. Одна маленькая деталь."
    zak "Я уверен, это ничего не стоит такому мастеру, как ты!"
    kenji "Ну хорошо! Говори, я сделаю."
    
    "Однако, увидев новую порцию пожеланий заказчика, я нервно сглотнул."
    
    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_05 = "images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_05.png"
    image Midori_In_GE_04:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_05"
        contains:
            "Midori_GE_Interface"
    
    pause 0.5
    
    scene Midori_In_GE_04 with Dissolve( my_dissolve_05 )
    
    "Действительно. Времени потребовалось совсем чуть-чуть. Хотя не припомню, чтобы я рисовал такое раньше. "
    "Мидори теперь была по-настоящему испорчена. Она была осквернена, окончательно и бесповоротно. "
    "И я сделал это собственными руками!"

    "А ведь это героиня популярного сейчас аниме-сериала."
    "Я его, конечно, не смотрел, но подозреваю, что Мидори там — отличница, президент кружка чайных церемоний, волонтёр в местном храме."
    "И вообще, всем ребятам пример!"
    "Если бы она только знала, какую гадость с ней сделал такой никчёмный человек, как я..."

    #СЦЕНА - ДЕНЬ 1, АЙКО ЗАХОДИТ В КОНМНАТУ КЕНДЗИ И ВИДИТ МИДОРИ

    aiko_voice "Кендзи!"
    
    scene Day_Kenji_Home_Bedroom with Dissolve( my_dissolve_05 )
    
    "Я настолько ушел в свои мысли, что не сразу сообразил — меня зовут."
    
    #Мини ЦГ - дверь в комнату Кендзи, на фоне которого стоит Айко
    image Day_Kenji_Bedroom_Door = "images/bg/Indoor/Kenji_Bedroom/Day/Day_Kenji_Bedroom_Door.png"
    image Day_Kenji_Bedroom_Door_Moved:
        contains:
            "Day_Kenji_Bedroom_Door"
            xpos 500
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Day_Kenji_Bedroom_Door_Masked = AlphaMask( "Day_Kenji_Bedroom_Door_Moved", "border_01_right_mask_moved" )
    
    image Day_Kenji_Bedroom_Door_With_Border_01:
        contains:
            "Day_Kenji_Bedroom_Door_Masked"
        contains:
            "border_01_right_moved"
    
    show Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "В дверях стояла Айко, моя младшая сестра."
    "Ой! Кажется, она уставилась в мой монитор!"
    "Я повернулся обратно к экрану. Там, как и раньше, красовалась Мидори, над которой я сегодня как следует поиздевался."
    "Чёрт! Я бы ни за что не стал добровольно демонстрировать такое творчество своей младшей сестре! Как не вовремя она зашла! "
    "Я молниеносно закрыл программу для рисования и вновь повернулся к Айко."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Confused_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Похоже, Айко успела разглядеть Мидори."
    "На несколько секунд повисла неловкая пауза, а затем моя сестра пришла в себя и тихо сказала:"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Завтрак готов."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Посмотрела на меня, нахмурилась и выпалила."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Angry_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Только надень на себя хоть что-то!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Angry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Только сейчас я осознал, что сижу на стуле в одних трусах."
    "Пока я разглядывал себя и своё нижнее белье, Айко исчезла."
    
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Не стоило злить сестру и опаздывать. Я встал, накинул рубашку, застегнул её через пуговицу."
    "Натянул брюки и, пытаясь справиться с тугой ширинкой, сделал несколько шагов по комнате."
    
    #СЦЕНА - ДЕНЬ 1, ЗАВТРАК С АЙКО
    
    "Спустился по лестнице, и вот я уже в большом холле, который к тому же выполняет роли кухни и столовой."
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    play environment_sounds "sounds/environment/Kitchen_With_Boiled_Water.mp3" fadein 1
    play music "sounds/music/track_05.mp3"

    kenji "И что сегодня на завтрак?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say with Dissolve( my_dissolve_02 )
    
    aiko "Суп, рис и омлет."
    
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand with Dissolve( my_dissolve_02 )
    
    "Я сел за стол, пока Айко протирала его влажной тряпкой. "
    "Потом она поставила на него две деревянные подставки. Протерла и их. "
    "Затем аккуратно расставила передо мной тарелки, положила палочки для еды. Всё в лучшем виде. "
    
    play sound "sounds/sounds/Plate_On_Table.mp3"
    image Kenji_1st_Day_Breakfast_Food = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/Food.png"
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Даже розовые таблетки — ферменты для пищеварения, которые мне прописали много лет назад — не забыты."
    
    #Мини ЦГ - кухонная плита, на фоне которой стоит Айко
    image Day_Kenji_Home_Kitchen_Gas_Stove = "images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Gas_Stove.png"
    image Day_Kenji_Home_Kitchen_Gas_Stove_Moved:
        contains:
            "Day_Kenji_Home_Kitchen_Gas_Stove"
            xpos 500
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Day_Kenji_Home_Kitchen_Gas_Stove_Masked = AlphaMask( "Day_Kenji_Home_Kitchen_Gas_Stove_Moved", "border_01_right_mask_moved" )
    
    image Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01:
        contains:
            "Day_Kenji_Home_Kitchen_Gas_Stove_Masked"
        contains:
            "border_01_right_moved"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Папа и мама звонили."
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Меня от этой новости немного передёрнуло — отца я побаивался. "
    "Но последнюю неделю я вёл себя хорошо. Не думаю, что Айко могла на меня наябедничать. "
    "Я ждал, пока Айко скажет что-то ещё, но она не стала продолжать. Значит, всё нормально!"
    
    hide Day_Aiko_Home_Outfit_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Довольно странно, что Айко так просто называла моего отца «папой»."
    "Дело в том, что Айко не была его родной дочкой. "
    "Моя мать умерла, когда я был ещё совсем маленьким, и всё это время меня воспитывал один отец."
    "А шесть лет назад он женился на вдове, Макото Наоки. С тех пор у меня появились сестра и новая мама, хотя я предпочитаю называть её «тётя Наоки». "
    "Вскоре после этого отцу предложили новую работу в центре города, и жить в захолустном пригороде ему стало крайне неудобно."
    "Они с тётей перебрались в новую квартиру, оставив прежнее жильё в моём полном распоряжении."
    
    "Моя новая сестра тоже осталась."
    "Говорила, что не хочет менять школу и расставаться со школьными подружками. Я ожидал, что она уедет после перехода в среднюю школу, но этого не случилось. "
    "Возможно, потому что она не хотела чувствовать себя лишней. Ведь у отца и тёти Наоки появился совместный ребёнок, наш с Айко младший брат. "
    "Впрочем, точной причины я не знал, да и знать не желал. И я бы сам не хотел, чтобы Айко уезжала — от неё много пользы. "
    "Она неплохо готовит, за домом следит. Ей даже не лень выращивать цветы в палисаднике и стричь кусты под окнами. "
    "С другой стороны, чуть что не так, она всегда готова нажаловаться на меня родителям. Приходится быть паинькой."

    "Я потянулся к палочкам для еды, но тут моё внимание привлёк работающий телевизор. "
    "Оттуда раздавалось частое дыхание. "
    
    show TV_Chad_Movie with Dissolve( my_dissolve_05 )
    
    "На экране какой-то тип держал за плечи худенькую девушку в школьной форме. Видимо, он пытался её поцеловать."
    "Та, дрожа, издала жалобный писк."
    
    tv "С-сэмпай!"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_With_Big_Spoon Confused_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я перевёл взгляд на сестру. Что за дурацкий канал она врубила с утра пораньше? "
    "Айко была сильно смущена и стояла как истукан с крышкой от кастрюли и черпаком в руках."
    
    hide Day_Aiko_Home_Outfit_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Хвала богам, пульт лежал на столе и через мгновение был у меня в руках."
    "Я перебирал каналы, пока не нашёл что-то наиболее нейтральное. "
    
    show TV_News_Kim_Chen_In with Dissolve( my_dissolve_05 )
    hide TV_Chad_Movie
    
    "Новости."
    "Выпуск в самом разгаре, обсуждают ближнее зарубежье. Китай, Корея, США. Отлично, самое оно! "
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Я вновь взялся за палочки для еды, но вдруг Айко остановила меня."
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты не забыл?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Не забыл что?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Сегодня четверг, день вывоза электронных приборов. Мама же просила освободить кладовку!"
    
    hide Day_Aiko_Home_Outfit_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Чёрт! Я помнил об этом вчера, но с утра, конечно, позабыл всё на свете."
    "Вот бы ещё и Айко забыла! "
    "Барахла в кладовке превеликое множество. Столько работы! Хорошо, если за день управлюсь. "
    "Конечно, никто никуда не спешит. Отец и тётя Наоки приедут ещё очень нескоро. Если вообще навестят нас до конца лета. "
    "Поэтому сегодня можно со спокойной совестью отмахнуться от забот, а в следующий четверг поднажать. "
    "Но если вдруг позвонит отец... Не очень хочется слушать его нравоучения. А Айко меня сдаст наверняка."
    
    "Я отложил палочки в сторону."
    
    kenji "Айко! Ты ещё не налила себе порцию?"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Что? Нет. Но собираюсь."
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Возьми мою, я суп не буду!"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Surprised_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Это ещё почему?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Surprised_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Не то чтобы я внезапно перестал быть голодным. Но мне требовалось оставить место в желудке для кое-чего другого."
    
    kenji "Мне риса хватит! А вместо супа достань-ка мне из холодильника баночку пива! Там же ещё осталось?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Angry_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Пиво! С утра?!"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Angry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "А что такого?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Angry_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Нет, ничего! Суп ты теперь вообще есть не будешь? Может, мне тогда начать варить пиво для тебя?"
    
    show Day_Aiko_Home_Outfit_With_Big_Spoon Angry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко была крайне возмущена."
    
    kenji "Остынь, Айко. Мне надо, понимаешь? Это как лекарство. Я же на улицу пойду. А там люди кругом. Это мне для храбрости!"
    
    hide Day_Aiko_Home_Outfit_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Конечно, Айко не понять меня. "
    "Но мне, тридцатилетнему затворнику, проводящему дни и ночи за компьютером, известно, насколько это тяжело — встречать по дороге соседей и знакомых и хриплым голосом желать им доброго дня. "
    "Если я немного выпью, дела пойдут гораздо веселее."

    "Айко с угрюмым видом кинула черпак в кастрюлю и пошла к холодильнику."
    
    #Мини ЦГ - холодильник на фоне которой стоит Айко
    image Day_Kenji_Home_Kitchen_Fridge = "images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Fridge.png"
    image Day_Kenji_Home_Kitchen_Fridge_Moved:
        contains:
            "Day_Kenji_Home_Kitchen_Fridge"
            xpos 700
    
    image Day_Kenji_Home_Kitchen_Fridge_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 800
    
    image Day_Kenji_Home_Kitchen_Fridge_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 800
    
    image Day_Kenji_Home_Kitchen_Fridge_Masked = AlphaMask( "Day_Kenji_Home_Kitchen_Fridge_Moved", "Day_Kenji_Home_Kitchen_Fridge_border_01_right_mask_moved" )
    
    image Day_Kenji_Home_Kitchen_Fridge_With_Border_01:
        contains:
            "Day_Kenji_Home_Kitchen_Fridge_Masked"
        contains:
            "Day_Kenji_Home_Kitchen_Fridge_border_01_right_moved"
    ##
    
    show Day_Kenji_Home_Kitchen_Fridge_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_Right_Palm_Up_Open Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    aiko "Ну, какое тебе?"
    
    show Day_Aiko_Home_Outfit_Right_Palm_Up_Open Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Да оно же одинаковое, любое!"
    
    show Day_Aiko_Home_Outfit_Right_Palm_Up_Open Surprised_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    aiko "Ты чего думаешь, я в сортах пива — спец?"
    
    hide Day_Aiko_Home_Outfit_Right_Palm_Up_Open with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_With_Beer Disgusting_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Айко взяла из холодильника одну из банок. Мне показалось, что сейчас она небрежно кинет её, настолько недовольное было у неё лицо. "
    
    image Kenji_1st_Day_Breakfast_Food_With_Beer = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/Food_With_Beer.png" 
    scene Kenji_1st_Day_Breakfast_Food_With_Beer with Dissolve( my_dissolve_05 )
    
    "Но нет, она поставила пиво на подставку, забрала мою порцию супа и села напротив."
    
    play sound "sounds/sounds/Opening_Beer_Can.mp3"
    
    "Я взял банку в руки и дёрнул за открывашку. "
    "Затем я схватил розовую таблеточку, запихнул её в рот и запил пивом. "
    "Увидев это, Айко изобразила гримасу неодобрения, но промолчала и принялась за еду. "
    "Я тоже не медлил и торопливо опустошал банку, закусывая рисом. "
    "Есть я старался быстро, но аккуратно, чтобы не испачкать стол и не раздосадовать Айко снова."
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    
    "Когда банка опустела, я почувствовал, что достиг нужной кондиции, и двинулся к кладовке."
    
    stop music fadeout 2
    "Пора приниматься за дело!"
    
    #СЦЕНА - ДЕНЬ 1, ВЫНОС МУСОРА 
    
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    play environment_sounds "sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    
    "Всю левую половину кладовки занимал стеллаж, который тётя Наоки планировала освободить, чтобы устроить в нём гардероб. "
    "Не знаю, зачем ей это вдруг понадобилось, учитывая, что в доме она вот уже несколько лет не живёт."
    "Но спорить с ней не хотелось. Барахлу на этих полках действительно давно место на свалке."

    "А может быть, причина не в этом? Может, тёте Наоки не нужен никакой гардероб, и она просто хочет избавиться от вещей, навевающих неприятные воспоминания? "
    "Дело в том, что всё содержимое стеллажа раньше принадлежало её бывшему мужу, Макото Кайоши."
    
    "Макото-сан умер десять лет назад. А точнее, погиб. Он был радиолюбителем, или как это там называется... "
    "Сидел вечерами в радиоэфире и болтал с другими такими же «чокнутыми», как назвала их тётя Наоки. "
    "Она вспоминала, что её муж мог просиживать в своей комнате часами и выбегать с радостными криками, когда ему удавалось принять сигнал совершенно незнакомых людей. "
    "Иногда даже от иностранцев."

    "Как это похоже на меня! Я тоже часами сижу за компьютером. "
    "И если вдруг мне напишет иностранец с предложением нарисовать что-то для него или просто с похвалой моей галереи..."
    "Я наверняка буду, как Макото-сан, бегать и голосить на весь дом о таком успехе."
    
    "Ещё Макото-сан тратил много денег на оборудование. Чего, конечно, не одобряла тётя Наоки. "
    "В общем, как это обычно и бывает, жене не особо нравились увлечения мужа. "
    "А вещи, которым он посвящал времени больше, чем ей, радости не вызывали и подавно."
    "Айко, похоже, тоже наплевать на всё это отцовское барахло. Она совсем его не помнит. "
    "Ну да, фотографий в альбоме и урны с прахом на местном кладбище ей достаточно. Кому нужна груда металлолома?"
    
    ##ЦГ - Гора телевизоров
    image TV_Heap = "images/cg/DAY_01/03a_Kenji_Moves_Trash/TV_Heap/TV_Heap.png"
    image TV_Heap_Dream:
        contains:
            "TV_Heap"
        contains:
            "Dream_Frame"
    #
    
    play environment_sounds_dream "sounds/environment/Pantry_Day_Dream.mp3" fadein 1 fadeout 1
    stop environment_sounds fadeout 1
    scene TV_Heap_Dream with Dissolve( my_dissolve_05 )
    
    "Однажды в детстве я проходил с отцом мимо площадки для сбора мусора. Там возвышалась грандиозная пирамида из телевизоров всех форм и размеров."
    "«Дядя Сато помер, телемастер» — пояснил мне отец. "
    "Потом мы с мальчишками устроили настоящую бойню. Расстреляли всю эту кучу камнями, пока не разбили каждый телек вдребезги."
    "Нам, конечно, здорово влетело, а на асфальте в том месте ещё несколько лет поблескивали кристаллики стекла."
    
    play environment_sounds "sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    stop environment_sounds_dream fadeout 1
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    
    "Тогда мне было весело, а сейчас уже не очень. Умер человек — и вся его жизнь оказалась на свалке. "
    "Чтобы напоследок люди по этим вещам могли определить, кто же «помер» в этот раз." 
    "А сегодня выносить чью-то жизнь на помойку предстояло мне."
    
    "О том, как погиб муж тёти Наоки, мне рассказал дядя Ватанабэ, который жил с нами на одной улице. "
    "Он был другом дяди Макото, и в прошлом тоже радиолюбителем."
    
    image Evening_Watanabe_Bike_WorkShop = "images/bg/Outdoor/Watanabe_Bike_WorkShop/Evening/Watanabe_Bike_WorkShop.png"
    image Evening_Watanabe_Bike_WorkShop_Dream:
        contains:
            "Evening_Watanabe_Bike_WorkShop"
        contains:
            "Dream_Frame"
    
    play environment_sounds_dream "sounds/environment/Pantry_Day_Dream.mp3" fadein 1 fadeout 1
    stop environment_sounds fadeout 1
    scene Evening_Watanabe_Bike_WorkShop_Dream with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_07.mp3"
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Он хотел сделать антенну. Из провода высоковольтной линии, что проходит в саду."

    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    "В саду, прямо за нашим домом, действительно стояла опора ЛЭП. Высокая, метров пятнадцать, не меньше."
    kenji "Он упал с нее?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Да нет. Прихлопнуло его, когда свою антенну на фазу забрасывал."
    watanabe "Если бы упал, тогда выжил бы, наверное. А так... Руки у него до костей обгорели."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Я не поверил. Подсоединить свою антенну к проводу под большим напряжением — это дикость! "

    kenji "Это больше похоже на самоубийство!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да ты что! Там всего тридцать пять тысяч вольт, это немного."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Немного?! Мне это число показалась неправдоподобно большим. «Всего» тридцать пять тысяч вольт! "
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Если бы у меня была такая возможность, я бы тоже набросил. А Кайоши не рассчитал чего-то."
    watanabe "Может, конденсаторы плохие ему попались, или ещё чего..."
    watanabe "Ты не подумай, Кендзи. Мы не сумасшедшие и не самоубийцы. Хотя, конечно, авантюра очень рискованная."
    watanabe "Меня тоже один раз шандарахнуло, но, слава богу, выжил."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Тоже «набросили»?"
    
    hide Evening_Watanabe_Work_Uniform_Cross_Arms with Dissolve( my_dissolve_01 )
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_01 )

    "Дядя Ватанабэ улыбнулся."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Да нет! На работе. Я же электрик по призванию. Но там ничего интересного, совершенно бытовая ситуация"
    watanabe "С тех пор пальцы на правой руке еле двигаются. И вообще, что-то вроде контузии получил. "
    watanabe "Полгода ходил как пришибленный. Инвалидом стал и вышел досрочно на пенсию."
    watanabe "Приходится подрабатывать автомехаником теперь. "
    watanabe "Эх, и как он только умудрился сжечь сцепление? А, Кендзи? Ты не знаешь?"
    
    play environment_sounds "sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    stop environment_sounds_dream fadeout 1
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    
    "Я тряхнул головой, отгоняя воспоминания. "
    
    stop music fadeout 3
    
    "Что-то я залип. Пора и за работу!  "
    
    show Day_Kenji_Home_Pantry_Blink_01_Animated with Dissolve( my_dissolve_05 )
    
    "Я решил сразу взяться за самое трудное — два металлических «чемоданчика», покрытые жёлтой эмалью. "
    "То, что они из металла, видно по потёртым краям, где из-под краски выглядывает потемневшая сталь. "
    "Причём металл достойной толщины, судя по их весу."
    
    hide Day_Kenji_Home_Pantry_Blink_01_Animated with Dissolve( my_dissolve_02 )
    show Day_Kenji_Home_Pantry_Blink_01a_Animated with Dissolve( my_dissolve_02 )
    
    "Один был значительно тяжелее другого. На его передней панели красовались чёрные стрелочные приборы и несколько тумблеров. "
    
    hide Day_Kenji_Home_Pantry_Blink_01a_Animated with Dissolve( my_dissolve_02 )
    show Day_Kenji_Home_Pantry_Blink_02_Animated with Dissolve( my_dissolve_02 )
    
    "Второй — легче. Его приборная панель была закрыта крышкой, с замками, как на армейской фляге. "
    "Для начала унесу тот, что легче — это будет разминка."
    
    play environment_sounds "sounds/environment/City_Suburb_Day_01.mp3" fadein 1 fadeout 1
    scene Outdoor_Day_Kenji_Home with Dissolve( my_dissolve_05 )
    
    "На улице был типичный июньский полдень. Ужасно яркое солнце, голубое небо и белоснежные облака. Всё как обычно. "
    "Дождей за последнюю неделю не наблюдалось, и к зною добавился стойкий запах пыли, который перебивал теперь аромат цветов и прочей зелени. "
    "Людей на улице не было — это радовало, мне ни к чему лишние свидетели."
    
    "Я вышел за ограду и принялся за упражнения со своим новеньким, жёлтеньким и увесистым, снарядом. "
    "Поставил его ребром на плечо — острый край пребольно врезался в шею. "
    "Попробовал нести под мышкой — и тут не вышло, рука моментально вспотела и «чемоданчик» норовил выскользнуть."
    "Я схватил его обеими руками и понёс, прижимая к груди, но и так было не очень сподручно. "
    
    scene Outdoor_Day_Street_05 with Dissolve( my_dissolve_05 )
    
    "Пройдя один квартал, я сменил тактику и решил взять свой снаряд за его родные, заводские ручки, покрытые каким-то плотным зелёным материалом. "
    "Постепенно стали ныть плечи и спина, а ещё зудеть нога в том месте, где она тёрлась о край прибора."
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 1 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    play sound "sounds/sounds/Metal_Item_Drag_And_Fall.mp3"
    
    "Последние несколько метров я буквально волочил «чемоданчик» по асфальту, оставляя блестящий след с чешуйками жёлтой краски. "
    "Похоже, я сегодня был первым посетителем. Никакой электроники до меня никто не выбросил, и площадка для мусора пустела."
    
    #Мини ЦГ - рация на асфальте
    image Radio_Set_On_Ground_Closed = "images/cg/DAY_01/03a_Kenji_Moves_Trash/Radio_Set_On_Ground_Closed/Radio_Set_On_Ground_Closed.png"
    image Radio_Set_On_Ground_Closed_Moved:
        contains:
            "Radio_Set_On_Ground_Closed"
            xpos 400
            pause 0.7
            ease 5.0 xpos 750
    
    image Radio_Set_On_Ground_Closed_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Radio_Set_On_Ground_Closed_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Radio_Set_On_Ground_Closed_Masked = AlphaMask( "Radio_Set_On_Ground_Closed_Moved", "Radio_Set_On_Ground_Closed_border_01_right_mask_moved" )
    
    image Radio_Set_On_Ground_Closed_With_Border_01:
        contains:
            "Radio_Set_On_Ground_Closed_Masked"
        contains:
            "Radio_Set_On_Ground_Closed_border_01_right_moved"
    ##
    
    show Radio_Set_On_Ground_Closed_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Теперь здесь лежал только мой прибор."
    "Я пнул его напоследок и отправился домой."
    "На обратном пути я вновь никого не встретил. Довольно удачный выдался денёк! "
    
    play environment_sounds "sounds/environment/Kitchen.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_05.mp3"
    "Я ворвался в дом, распахнул холодильник и сразу же выпил холодного пива. Ох, похоже, полбанки выдул за несколько глотков! "
    
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Angry_Silent with Dissolve( my_dissolve_02 )
    
    "Айко была на кухне. Она нахмурилась, глядя на меня, но ничего не сказала. "
    "Я же улыбнулся во весь рот и продемонстрировал сестре оттопыренный большой палец. "
    
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Shy_Silent with Dissolve( my_dissolve_02 )
    
    "От моего жеста она почему-то смутилась, а я только теперь заметил, что на ней надета летняя школьная форма."
    
    kenji "Ты что, в школу собралась? Разве сейчас не каникулы?"
    
    hide Day_Aiko_School_Uniform_Hands_On_The_Sides Shy_Silent with Dissolve( my_dissolve_01 )
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Say with Dissolve( my_dissolve_01 )
    
    aiko "Каникулы! Но я иду в школьный бассейн."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Бассейн! Я вспомнил о том, что на земле существуют такие замечательные места. Ах! Я бы сейчас с удовольствием окунулся в прохладную водичку. "
    "И плевать, что там народу как сельдей в бочке. Настроение у меня теперь самое располагающее, никакой невроз от тесного общения с людьми не страшен. "
    "Правда, в таком состоянии в общественный бассейн меня не пустят. Я вздохнул и отхлебнул ещё пива."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Say with Dissolve( my_dissolve_02 )
    
    aiko "Чего вздыхаешь?"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Разве не понятно? В такую-то жару в бассейне поплавать в самый раз!"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Surprised_Say with Dissolve( my_dissolve_02 )
    
    aiko "В нашем школьном?"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Surprised_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да нет же, в любом. Но сама понимаешь, народу там — тьма."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Айко пожала плечами и стала чуть серьёзнее. Она знала, чего я боюсь."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Say with Dissolve( my_dissolve_02 )

    aiko "Можешь съездить к морю. Где-то да найдёшь пустынный пляж."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "К морю... да... Но тогда придётся трястись в поезде час или два. В переполненном поезде, Айко!"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Mocking_Silent with Dissolve( my_dissolve_02 )
    
    "На лице Айко появилась ухмылка."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Mocking_Say with Dissolve( my_dissolve_02 )
    
    aiko "Ты же принял «лекарство»."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Mocking_Silent with Dissolve( my_dissolve_02 )
    
    kenji "С этим лекарством, сама понимаешь, в воду лезть не стоит. Тем более в одиночку."
    
    #hide Day_Aiko_School_Uniform_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Normal_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко опять пожала плечами и направилась к выходу. Дескать, это не её проблемы."
    
    kenji "Постой, Айко! А может быть, завтра вместе съездим на море и там найдём этот самый пустынный пляж? Я не могу один — вдруг я начну тонуть?"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Surprised_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Думаешь, я тебя спасу?"
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Surprised_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ты же член плавательного кружка!"
    
    hide Day_Aiko_School_Uniform_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Angry_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А ты опять напьёшься?"
    
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Angry_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что значит «опять»? Это же не ради удовольствия, Айко!"
    
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Angry_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "В таком случае даже не мечтай!"
    
    show Day_Aiko_School_Uniform_Hands_On_The_Sides Angry_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ну... Айко! Я встану на колени перед тобой, хочешь?"
    
    hide Day_Aiko_School_Uniform_Hands_On_The_Sides with Dissolve( my_dissolve_01 )
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Scared_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "По лицу Айко пробежала гримаса испуга и отвращения."
    
    show Day_Aiko_School_Uniform_Hand_Hold_Hand Scared_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "НЕТ!"
    aiko "То есть да. Уговорил! Завтра поедем, но только без этого!"
    
    play sound "sounds/sounds/Aiko_Run_Away_From_Kitchen.mp3"
    hide Day_Aiko_School_Uniform_Hand_Hold_Hand with vpunch
    
    "Айко в мгновение ока изчезла, скрывшись за дверью в прихожую."
    "Как же мне повезло с сестрёнкой! Мысль о предстоящем отдыхе приободрила меня, и я с энтузиазмом вернулся к работе."
    
    stop music fadeout 2
    play environment_sounds "sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Pantry_02 with Dissolve( my_dissolve_05 )
    show Day_Kenji_Home_Pantry_Blink_03_Animated with Dissolve( my_dissolve_02 )
    
    "В следующий свой поход я решил не брать тяжелого собрата жёлтого чемоданчика — оставил его на потом."
    "Вместо него я взял моток провода, который лежал на верхней полке."
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 2 fadeout 2
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    #Мини-ЦГ вентилятор Касуми 01
    image Kasumi_Fan_01 = "images/cg/DAY_01/03a_Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_01.png"
    image Kasumi_Fan_01_Moved:
        contains:
            "Kasumi_Fan_01"
            xpos -700
    
    image Kasumi_Fan_01_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1100
    
    image Kasumi_Fan_01_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1100
    
    image Kasumi_Fan_01_Masked = AlphaMask( "Kasumi_Fan_01_Moved", "Kasumi_Fan_01_border_01_left_mask_moved" )
    
    image Kasumi_Fan_01_With_Border_01:
        contains:
            "Kasumi_Fan_01_Masked"
        contains:
            "Kasumi_Fan_01_border_01_left_moved"
    ##
    
    show Kasumi_Fan_01_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "За время моего отсутствия на площадке появился напольный вентилятор с разлохмаченными от старости синими лопастями и пожелтевшим корпусом из пластика. "
    
    #Мини ЦГ - рация на асфальте, с откинутой крышкой
    image Radio_Set_On_Ground = "/images/cg/DAY_01/03a_Kenji_Moves_Trash/Radio_Set_On_Ground/Radio_Set_On_Ground.png"
    image Radio_Set_On_Ground_Moved:
        contains:
            "Radio_Set_On_Ground"
            xpos 400
            pause 0.7
            ease 5.0 xpos 750
    
    image Radio_Set_On_Ground_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Radio_Set_On_Ground_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Radio_Set_On_Ground_Masked = AlphaMask( "Radio_Set_On_Ground_Moved", "Radio_Set_On_Ground_border_01_right_mask_moved" )
    
    image Radio_Set_On_Ground_With_Border_01:
        contains:
            "Radio_Set_On_Ground_Masked"
        contains:
            "Radio_Set_On_Ground_border_01_right_moved"
    ##
    
    show Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "А мой «чемоданчик», похоже, был рад знакомству — он приветливо снял шляпу!"
    "Не знаю почему, но его крышка была вскрыта. "
    
    hide Kasumi_Fan_01_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Под ней оказалась сложная приборная панель: десятки всевозможных крутилок, тумблеров, циферблатов со стрелками и хитрых разъёмов. "
    "Может быть, крышка спала сама? Прибор нагрелся под солнцем и она слетела?"
    "Я потрогал его. Да, горячий."
    "Но, должно быть, кому-то просто стало интересно, что же такое я сюда притащил. "
    "Хм... Возможно, этот кто-то — владелец сломанного вентилятора. Я подошёл поближе. "
    
    #Мини-ЦГ вентилятор Касуми 02
    image Kasumi_Fan_02 = "images/cg/DAY_01/03a_Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_02.png"
    image Kasumi_Fan_02_Moved:
        contains:
            "Kasumi_Fan_02"
            xpos -850
    
    image Kasumi_Fan_02_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1100
    
    image Kasumi_Fan_02_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1100
    
    image Kasumi_Fan_02_Masked = AlphaMask( "Kasumi_Fan_02_Moved", "Kasumi_Fan_02_border_01_left_mask_moved" )
    
    image Kasumi_Fan_02_With_Border_01:
        contains:
            "Kasumi_Fan_02_Masked"
        contains:
            "Kasumi_Fan_02_border_01_left_moved"
    ##
    
    hide Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_02 )
    show Kasumi_Fan_02_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Обычный вентилятор. Видно, что старый — наверняка ему лет двадцать, не меньше. Сейчас таких не делают."
    "Сквозь запах пыльной улицы моё обоняние уловило «аромат» горелого пластика и сигарет. "
    "Да и весь этот жёлтый налёт на нём... явно сигаретная копоть, налипшая за годы эксплуатации. "
    "Стало немного противно, и в то же время в памяти всколыхнулись воспоминания былых лет."
    
    image smocking_old_man = "images/cg/DAY_01/03a_Kenji_Moves_Trash/Old_Smocking_Man/smocking_old_man.png"
    image smocking_old_man_dream:
        contains:
            "smocking_old_man"
        contains:
            "Dream_Frame"
    
    
    play environment_sounds_dream "sounds/environment/City_Suburb_Day_03_Dream.mp3" fadein 1
    stop environment_sounds fadeout 2
    scene smocking_old_man_dream with Dissolve( my_dissolve_05 )
    
    "Я вспомнил своего давно умершего деда, который всю жизнь смолил какие-то американские сигареты. "
    "Весь его дом и каждая вещь в нём накрепко пропитались застарелым запахом сигаретного дыма."
    "Столь активные курильщики наверняка постоянно чем-то болеют. "
    "Например, туберкулёзом — неприятной и очень заразной болезнью, я слышал о такой. "
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 2
    stop environment_sounds_dream fadeout 2
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Я отошёл подальше от вентилятора и посмотрел на свою левую ладонь."
    "Я только что прикасался к прибору, который недавно принёс. А до меня его, похоже, трогал кто-то чужой. "
    "Вот будет весело, если такой домосед, как я, подцепит редкую и смертельную болезнь! А точнее — совсем не весело!"
    "Я поспешил домой. Надо скорее вымыть руки!"
    
    play environment_sounds "sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    show Day_Kenji_Home_Pantry_Blink_04_Animated with Dissolve( my_dissolve_02 )
    
    "В свой третий поход до мусорки я взял два стареньких радиоприёмника. Они были довольно громоздкие, но в то же время совсем не тяжёлые."
    
    scene Day_Kenji_Home_Pantry_Other_04 with Dissolve( my_dissolve_05 )

    kenji "Остальное, думаю, можно оставить и на потом."
    kenji "За день сделано достаточно! Пожалуй, ещё одну вещь и довольно."
    
    "Я решил во что бы то ни стало вынести сегодня тяжёлый чемоданчик. "
    "А между тем вторая банка пива подошла к концу. Я сходил на кухню и взял новую. Открывать её не стал — положил в карман брюк. "
    "В трудном последнем походе мне понадобятся обе руки!"
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 2 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Поход был действительно трудный! "
    "Когда я наконец дотащил свою ношу до места, у меня ужасно ныли плечи и спина, тряслись руки и не разгибались пальцы. "
    
    
    #Мини ЦГ - БП от рации на земле
    image Radio_Set_Power_Supply_On_ground = "images/cg/DAY_01/03a_Kenji_Moves_Trash/Radio_Set_Power_supply_On_Ground/Radio_Set_Power_Supply_On_ground.png"
    image Radio_Set_Power_Supply_On_ground_Moved:
        contains:
            "Radio_Set_Power_Supply_On_ground"
            xpos 400
            pause 0.7
            ease 5.0 xpos 900
    
    image Radio_Set_Power_Supply_On_ground_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Radio_Set_Power_Supply_On_ground_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Radio_Set_Power_Supply_On_ground_Masked = AlphaMask( "Radio_Set_Power_Supply_On_ground_Moved", "Radio_Set_Power_Supply_On_ground_border_01_right_mask_moved" )
    
    image Radio_Set_Power_Supply_On_ground_With_Border_01:
        contains:
            "Radio_Set_Power_Supply_On_ground_Masked"
        contains:
            "Radio_Set_Power_Supply_On_ground_border_01_right_moved"
    ##
    
    show Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Прибор тоже потерял товарный вид. Дело в том, что бока его были не гладкими, а состояли из сотен мелких рёбер — пластин. "
    "Видимо, при работе прибор грелся, и такая конструкция была нужна для охлаждения. Рёбра теперь были все погнуты, особенно те, что по краям. "
    "В просветы между ними забились трава, земля и частички асфальта. Один из циферблатов на передней панели треснул. "
    
    hide Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Но мне, конечно, было наплевать. Не на выставку же нёс, в самом деле!"
    
    "Ну вот и всё, пришло время передохнуть!"
    "Я окинул взглядом вещи, которые принёс, и оценил их вес. Да я просто герой!"
    "Эх, надо было Айко показать, какая эта жёлтая зараза тяжёлая. Она бы мной гордилась! " 
    "Пожалела бы меня и позабыла про свои придирки как минимум на месяц! И почему я такой недогадливый?" 
    
    play sound "/sounds/sounds/Open_Beer_Can_Loud.mp3"
    
    "С этими мыслями я открыл пиво, которое ожидало своего часа в кармане брюк. "
    "Да уж, взболтал я содержимое банки здорово — пена полезла наружу, липкие струйки потекли по пальцам. "
    "Я тихо ругнулся, сдул пену, вытер руку о штаны и поставил ногу на тот прибор, что принёс раньше остальных — как на поверженного врага. "
    "Сделал большой глоток и огляделся по сторонам. Я был не один."
    
    #Мини ЦГ - Касуми идет с тележкой
    image Kasumi_Walks = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Walks/Kasumi_Walks.png"
    image Kasumi_Walks_Moved:
        contains:
            "Kasumi_Walks"
            xpos 700
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Walks_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Kasumi_Walks_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kasumi_Walks_Masked = AlphaMask( "Kasumi_Walks_Moved", "Kasumi_Walks_border_01_right_mask_moved" )
    
    image Kasumi_Walks_With_Border_01:
        contains:
            "Kasumi_Walks_Masked"
        contains:
            "Kasumi_Walks_border_01_right_moved"
    ##
    show Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_02 )
    
    play music "sounds/music/track_03.mp3" fadein 2
    
    "Мне навстречу шла девушка. Она катила перед собой маленькую тележку для вещей. "
    "Тележка была пуста. "
    "Зачем она это делала, было непонятно, да и способ перемещения тележки странный — гораздо проще везти её за собой."
    "А такую маленькую вообще лучше бы сложить, взять под мышку и идти так. "
    "Внезапно девушка остановилась, отвернулась от дороги и замерла."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_01 )
    
    #Мини ЦГ - Касуми стоит с тележкой
    image Kasumi_And_Interesting_Wall = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_And_Interesting_Wall/Kasumi_And_Interesting_Wall.png"
    image Kasumi_And_Interesting_Wall_Moved:
        contains:
            "Kasumi_And_Interesting_Wall"
            xpos -600
            #xpos -900
            #pause 0.7
            #linear 5.0 xpos -600
    
    image border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kasumi_And_Interesting_Wall_Masked = AlphaMask( "Kasumi_And_Interesting_Wall_Moved", "border_01_left_mask_moved" )
    
    image Kasumi_And_Interesting_Wall_With_Border_01:
        contains:
            "Kasumi_And_Interesting_Wall_Masked"
        contains:
            "border_01_left_moved"
    
    show Kasumi_And_Interesting_Wall_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    "Не меньше минуты она стояла перед каменной кладкой, словно рассматривая интереснейшую картину."
    "Я между тем терялся в догадках, чего же такого интересного она там увидела."
    "Я не приметил ничего необычного, когда проходил это место."
    "Может быть, девчонке этой надо на площадку для мусора? А я её стесняю, и поэтому-то она так внезапно принялась изучать эту стену?"
    
    hide Kasumi_And_Interesting_Wall_With_Border_01 with Dissolve( my_dissolve_01 )
    show Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Как только я подумал об этом, школьница отвернулась от стены и продолжила свой путь в мою сторону. "
    "Обычно я в таких случаях перехожу на другую сторону улицы или вообще стараюсь побыстрее скрыться с глаз встречного прохожего. "
    "Но в этот раз повышенная концентрация «лекарства» позволила мне и дальше с любопытством наблюдать за незнакомкой."
    "Привычный страх перед людьми на время полностью оставил меня."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Девушка наконец достигла площадки для сбора мусора. И оказалась метрах в пяти от меня!"
    "Она остановилась и отвесила мне учтивый поклон. Я бы даже сказал, чересчур учтивый!"
    
    #Мини ЦГ - Касуми стоит на четвереньках
    image On_All_Fours = "images/cg/DAY_01/04a_Trash_Place_Meeting/On_All_Fours/On_All_Fours.png"
    image On_All_Fours_Moved:
        contains:
            "On_All_Fours"
            xpos -500
            pause 0.7
            ease 10.0 xpos -1100
    
    image border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image On_All_Fours_Masked = AlphaMask( "On_All_Fours_Moved", "border_01_left_mask_moved" )
    
    image On_All_Fours_With_Border_01:
        contains:
            "On_All_Fours_Masked"
        contains:
            "border_01_left_moved"
    
    show On_All_Fours_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    "Её ладони коснулись земли, и она встала на четвереньки. "
    "Если честно, мне захотелось воскликнуть от удивления, но я продолжил молча стоять как вкопанный, только глаза мои опускались всё ниже. "
    "Её руки замелькали по асфальту..."
    
    hide On_All_Fours_With_Border_01 with Dissolve( my_dissolve_01 )
    
    #Мини ЦГ - Руки Касуми на штанине Кендзи
    image Kasumi_Hands_On_Kenji_Leg = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Hands_On_Kenji_Leg/Kasumi_Hands_On_Kenji_Leg.png"
    image Kasumi_Hands_On_Kenji_Leg_Moved:
        contains:
            "Kasumi_Hands_On_Kenji_Leg"
            xpos 600
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Hands_On_Kenji_Leg_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kasumi_Hands_On_Kenji_Leg_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kasumi_Hands_On_Kenji_Leg_Masked = AlphaMask( "Kasumi_Hands_On_Kenji_Leg_Moved", "Kasumi_Hands_On_Kenji_Leg_border_01_right_mask_moved" )
    
    image Kasumi_Hands_On_Kenji_Leg_With_Border_01:
        contains:
            "Kasumi_Hands_On_Kenji_Leg_Masked"
        contains:
            "Kasumi_Hands_On_Kenji_Leg_border_01_right_moved"
    
    show Kasumi_Hands_On_Kenji_Leg_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    "А через мгновение принялись ощупывать жёлтый чемоданчик и дальше — мой кроссовок, штанину..."
    
    kenji "Эй! Ты чего творишь?"
    
    hide Kasumi_Hands_On_Kenji_Leg_With_Border_01 with Dissolve( my_dissolve_01 )
    play sound "sounds/sounds/Body_Fall_On_Ground.mp3"
    show empty_image with vpunch #Трясем экран
    
    "..."
    
    #Мини ЦГ - Касуми упала на пятую точку
    image Kasumi_Fells_Moved:
        contains:
            "Kasumi_Fells"
            xpos -600
            pause 0.7
            ease 5.0 xpos -500
    
    image Kasumi_Fells_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Kasumi_Fells_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kasumi_Fells_Masked = AlphaMask( "Kasumi_Fells_Moved", "Kasumi_Fells_border_01_left_mask_moved" )
    
    image Kasumi_Fells_With_Border_01:
        contains:
            "Kasumi_Fells_Masked"
        contains:
            "Kasumi_Fells_border_01_left_moved"
    
    show Kasumi_Fells_With_Border_01 with Dissolve( my_dissolve_05 )
    ##

    "Руки девушки отцепились от моих брюк, а сама она отпрянула так стремительно, что не удержалась на ногах и села на асфальт."
    "Но не успел я моргнуть, как она оправилась и встала."
    
    hide Kasumi_Fells_With_Border_01 with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Простите! Я не заметила вас!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не заметила?!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Да, я ничего не вижу."
    
    #Мини-ЦГ лицо Касуми крупным планом
    image DAY_01_Kasumi_Big_Face = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi/Kasumi.png"
    image DAY_01_Kasumi_Big_Face_Moved:
        contains:
            "DAY_01_Kasumi_Big_Face"
            ypos -300
            xpos -500
            #pause 0.7
            #linear 10.0 xpos -500
    
    image DAY_01_Kasumi_Big_Face_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -700
    
    image DAY_01_Kasumi_Big_Face_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -700
    
    image DAY_01_Kasumi_Big_Face_Masked = AlphaMask( "DAY_01_Kasumi_Big_Face_Moved", "DAY_01_Kasumi_Big_Face_border_01_left_mask_moved" )
    
    image DAY_01_Kasumi_Big_Face_With_Border_01:
        contains:
            "DAY_01_Kasumi_Big_Face_Masked"
        contains:
            "DAY_01_Kasumi_Big_Face_border_01_left_moved"
    ##
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show DAY_01_Kasumi_Big_Face_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Я взглянул на лицо девушки, и у меня по спине пробежал холодок."
    "Солнце ярко высвечивало её лицо и искрилось на прядях волос. "
    "Но наперекор светилу, зрачки её были так широки, что по тонким радужкам невозможно было определить даже цвет глаз. "
    "Этот контраст расширенных, как у кошки в ночи, зрачков и яркого солнца, бьющего прямо в глаза, напугал меня. "
    "Девушка была слепой."
    
    hide DAY_01_Kasumi_Big_Face_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Извини..."

    "Хрипло прошептал я. "
    "Я кашлянул и повторил снова, уже в полный голос."

    kenji "Извини!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Девушка встревожилась."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Что? Почему? За что?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну... Я... Не думал, что ты..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Всё нормально! Хорошо, что я не налетела на вас."
    blind_girl "Вас совсем не было слышно и я думала, что тут никого нет."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Наверное, слепые люди полагаются на слух. Нет, вовсе не наверное, а даже точно. На что же ещё? Может, на обоняние? "
    "Тут мне словно врубили нужную часть мозга, и я почувствовал, что от девушки сильно несёт сигаретами. "
    "Она что, курит, и курит настолько много?!"
    
    "Но, несмотря на запах, девушка не походила на заядлого курильщика."
    "В руках у неё не было ни зажигалки, ни спичек, ни сигарет."
    "Мой взгляд пробежался по фигуре девушки, и я подметил, что форма её порядком поношенная и выцветшая."
    "А загар на руках и шее незнакомки точно повторял контуры вырезов одежды."
    "Видимо, она проносила школьную форму всё лето."

    "Лицо её мне показалось приятным. Давно я так близко не разглядывал старшеклассниц."
    "Но всё впечатление портил этот пустой взгляд, в котором, казалось, навечно застыл испуг."
    
    #Мини-ЦГ ус Касуми крупным планом
    image DAY_01_Kasumi_Big_Face_Mustache = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi/Kasumi.png"
    image DAY_01_Kasumi_Big_Face_Mustache_Moved:
        contains:
            "DAY_01_Kasumi_Big_Face_Mustache"
            #ypos -300
            xpos -1000
            #pause 0.7
            #linear 10.0 xpos -500
    
    image DAY_01_Kasumi_Big_Face_Mustache_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image DAY_01_Kasumi_Big_Face_Mustache_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image DAY_01_Kasumi_Big_Face_Mustache_Masked = AlphaMask( "DAY_01_Kasumi_Big_Face_Mustache_Moved", "DAY_01_Kasumi_Big_Face_Mustache_border_01_left_mask_moved" )
    
    image DAY_01_Kasumi_Big_Face_Mustache_With_Border_01:
        contains:
            "DAY_01_Kasumi_Big_Face_Mustache_Masked"
        contains:
            "DAY_01_Kasumi_Big_Face_Mustache_border_01_left_moved"
    ##
    
    show DAY_01_Kasumi_Big_Face_Mustache_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "И ещё одна примечательная деталь — белый ободок с проводками, на кончиках которых блестели маленькие шарики из фольги."
    "С этим аксессуаром голова девушки напоминала голову муравья или инопланетянина из старых чёрно-белых фильмов."
    "И зачем ей эти «усы»?"
    
    hide DAY_01_Kasumi_Big_Face_Mustache_With_Border_01 with Dissolve( my_dissolve_02 )

    "Всё в этой девушке было странным. Её пугающие, невидящие глаза и этот непонятный ободок на голове."
    "И стойкий запах сигаретного дыма."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Получается, эта рация ваша?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Спросила девушка, и её ладонь указала в сторону моих ног."
    
    show Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_05 )
    
    kenji "Так это рация?"
    
    "Я удивился. При слове «рация» мне представлялось маленькое, величиной с мобильный телефон, устройство. "
    "А такая громадина, и тоже — рация. Ну надо же!"
    
    hide Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_01 )
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Ну да. Военная рация, очень хорошая, американская, мощная. В конце шестидесятых годов выпускалась. Ещё на германиевых транзисторах!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Германиевых? Значит ли это, что транзисторы были из Германии? Какое странное словосочетание. "
    "Интересно, а «япониевый» транзистор есть?"

    kenji "Рация не совсем моя. Одного родственника"
    kenji "Я просто его вещи на свалку выношу. Он, видимо, радио увлекался, или что-то в этом роде."
    kenji "Сам я в этих делах ничего не смыслю."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А..."
    blind_girl "Увлекался?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну да. Умер он. Но очень давно. А сейчас понадобилось расчистить немного места в доме. Вот и выбрасываем, и рацию эту тоже."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А... А я думала, вы наоборот. Пришли сюда за ней."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Теперь я понял, зачем девушке нужна была тележка. И почему была вскрыта крышка на «рации». "
    "Похоже, вещь эта её заинтересовала, и она собралась забрать её себе."
    
    kenji "Нет! Мне этот хлам нафиг не сдался. Если хочешь забрать — бери, конечно."
    kenji "Только как же ты её унесёшь? Думаешь, сможешь? Она страшно тяжёлая!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Все вещи тех лет такие громоздкие. А эта ещё и военная, там всё внутри с многократным запасом прочности!"
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    "С этими словами она присела и потянула руки в сторону рации. Я поспешно убрал ногу и отступил на шаг. "
    "Девушка ощупала боковины прибора, взялась за тканевую ручку и попыталась встать. "
    
    #Мини ЦГ - Касуми пытается поднять рацию
    image Kasumi_Lifting_Up_RadioSet_Moved:
        contains:
            "Kasumi_Lifting_Up_RadioSet"
            xpos 700
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Lifting_Up_RadioSet_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kasumi_Lifting_Up_RadioSet_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kasumi_Lifting_Up_RadioSet_Masked = AlphaMask( "Kasumi_Lifting_Up_RadioSet_Moved", "Kasumi_Lifting_Up_RadioSet_border_01_right_mask_moved" )
    
    image Kasumi_Lifting_Up_RadioSet_With_Border_01:
        contains:
            "Kasumi_Lifting_Up_RadioSet_Masked"
        contains:
            "Kasumi_Lifting_Up_RadioSet_border_01_right_moved"
    ##
    
    #play sound "sounds/sounds/Submarine_Creaking.mp3"
    show Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Послышался скрежет металла об асфальт, прибор поднялся... Но совсем чуть-чуть, сантиметров на пять. "
    "Моя случайная знакомая тянула лямку прибора изо всех сил, но такая тяжесть была ей не по зубам."
    
    kenji "Давай я помогу!"

    "Сказал я, встал с другой стороны и взял «рацию» за вторую ручку. "
    
    stop sound fadeout 0.5
    hide Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( my_dissolve_01 )
    play sound "sounds/sounds/Metal_Item_Fall.mp3"
    show empty_image with vpunch #Трясем экран 
    
    "Но в тот же момент руки девушки разжались, и прибор глухо хлопнулся на землю. "
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "А девушка, задыхаясь, выпалила."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "И вправду, очень тяжёлый!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )

    "Я вспомнил о банке пива в руке и отхлебнул немного. А после сказал:"

    kenji "Давай я помогу погрузить эту штуковину на тележку. Похоже, тебе её не поднять."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Она кивнула."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Если... Если вам не трудно..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    #Мини ЦГ - тележка Касуми (пустая)
    image Kasumi_Cart = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Cart/Kasumi_Cart.png"
    image Kasumi_Cart_Moved:
        contains:
            "Kasumi_Cart"
            xpos 600
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Cart_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kasumi_Cart_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kasumi_Cart_Masked = AlphaMask( "Kasumi_Cart_Moved", "Kasumi_Cart_border_01_right_mask_moved" )
    
    image Kasumi_Cart_With_Border_01:
        contains:
            "Kasumi_Cart_Masked"
        contains:
            "Kasumi_Cart_border_01_right_moved"
    ##
    
    show Kasumi_Cart_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Я взялся за тележку — на вид крайне хлипкую, из алюминиевых трубок, скреплённых пластиковыми уголками и такими же заклёпками. "
    "Рама её была перехвачена двумя плетёными жгутами красного цвета."

    "Я поставил тележку, поднял рацию и аккуратно установил её на раму. Рама выгнулась и затрещала, но выдержала. "
    
    #Мини ЦГ - тележка Касуми (с радиостанцией)
    image Kasumi_Cart_And_Radio_Set = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Cart_And_Radio_Set/Kasumi_Cart_And_Radio_Set.png"
    image Kasumi_Cart_And_Radio_Set_Moved:
        contains:
            "Kasumi_Cart_And_Radio_Set"
            xpos 600
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Cart_And_Radio_Set_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kasumi_Cart_And_Radio_Set_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kasumi_Cart_And_Radio_Set_Masked = AlphaMask( "Kasumi_Cart_And_Radio_Set_Moved", "Kasumi_Cart_And_Radio_Set_border_01_right_mask_moved" )
    
    image Kasumi_Cart_And_Radio_Set_With_Border_01:
        contains:
            "Kasumi_Cart_And_Radio_Set_Masked"
        contains:
            "Kasumi_Cart_And_Radio_Set_border_01_right_moved"
    ##
    
    show Kasumi_Cart_And_Radio_Set_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Kasumi_Cart_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Я хорошенько обмотал всю эту конструкцию багажными жгутами, наклонил. Похоже, всё держалось."

    kenji "Ну, вроде как готово!"

    "Девушка протянула руки в мою сторону. Я отступил. Захотелось словами указать ей, в каком направлении двигаться, но я сдержался. "
    "Она поводила руками и наконец нашла длинную ручку тележки. Затем ощупала стоящую на ней рацию и жгуты."
    
    hide Kasumi_Cart_And_Radio_Set_With_Border_01 with Dissolve( my_dissolve_02 )

    kenji "Я хорошо всё закрепил."

    "Сказал я, словно подбадривая её."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Спасибо! Большое вам спасибо за помощь!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Похоже, это она так прощалась со мной. Действительно, чем мог, я помог. Больше говорить было не о чем. "
    "И тут какая-то дурацкая грусть окутала моё охмелевшее сознание. "
    "Грустно оттого, что девушка уходит, и я её, наверное, больше никогда не увижу."
    
    "И... так жалко её. Неужели она действительно справится с этой тяжёлой ношей одна? Доберётся ли в целости до дома? А вдруг что-то случится в пути?"
    "Хотелось проводить её, побыть ещё рядом. Да и хорошенькая она на вид. И вообще, я бы сказал, что она мне понравилась. "
    "Хотя, говорят, что когда здорово выпил, любой крокодил за красавицу сойдёт."
    "А выпил я сегодня действительно здорово, да и жара приморила изрядно."

    "Надо остановить её! Сказать что-то! Но что? "
    "Я осмотрелся, взгляд упал на остальные принесённые мной вещи."
    
    kenji "Постой! А эта рация... Она не из двух частей состоит?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Двух частей?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну да. Тут ещё что-то. Похоже, дополнение к ней. Цвет и габариты — всё такое же."
    kenji "Я вынес это в последнюю очередь. Посмотри сама..."
    
    "Я прикусил язык. Чёрт! Зачем я это сказал, вот ведь идиот! Но девушка не повела и ухом."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А как? Как оно выглядит? Точь-в-точь как эта? Может, просто ещё одна?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не думаю..."
    
    show Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_02 )

    "Я описал ей всё в подробностях. "
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А! Это блок питания для рации."
    blind_girl "Обычно она работала от аккумулятора. Ну, от танкового или ещё какого."
    blind_girl "А этот блок питания нужен для того, чтобы питать её от сети. Дома, от розетки, например."
    
    hide Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_02 )
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Значит, он тебе тоже нужен?"
    
    "Её последние слова меня воодушевили. Но когда я услышал ответ, все мои надежды мигом рухнули."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Нет! У меня есть. Дома. Правда, не такой, обычный, но мощный!"
    blind_girl "Можно напряжение любое выставить. Он подойдёт."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А... Ну ладно."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_02 )

    stop music fadeout 3
    "Я был раздосадован. Ничего не вышло. Девушка поклонилась мне на прощание, я молча поклонился в ответ. "
    "Конечно, она этого не видела и надо было попрощаться словами. Но чёрт с ней! "
    "Я внезапно разозлился. Пусть чешет своей дорогой! Надо было и вовсе смыться домой, ещё когда только заприметил её вдалеке."

    "Я залпом допил оставшееся пиво, смял банку и кинул в контейнер для металлической тары. "
    "Хоть я и был пьян, банка прилетела точно в цель!"
    
    #ЦГ - взрыв тележки Касуми
    image Kasumi_BOOM = "images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/Kasumi_Boom.png"
    image Kasumi_BOOM_animation_frame_00 = "images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_00.png"
    image Kasumi_BOOM_animation_frame_01 = "images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_01.png"
    image Kasumi_BOOM_animation_frame_02 = "images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_02.png"
    
    image Kasumi_BOOM_animation:
        contains:
            "Kasumi_BOOM_animation_frame_00"
            0.1
            "Kasumi_BOOM_animation_frame_01"
            0.1
            "Kasumi_BOOM_animation_frame_02"
            0.1
            repeat
        contains:
            "white_image"
            pause 0.5
            linear 1.0 alpha 0.0
    ##
    
    show Kasumi_BOOM_animation
    play sound "sounds/sounds/TNT.mp3"
    stop environment_sounds fadeout 1
    play environment_sounds_dream "sounds/environment/City_Suburb_Day_03_Dream.mp3" fadein 2 fadeout 1
    
    "Ба-бах!"
    blind_girl "Ай!"
    
    show Kasumi_BOOM with Dissolve(0.2)
    hide Kasumi_BOOM_animation
    
    "Я обернулся. Похоже, эта школьница наехала тележкой на мину!" 
    "Нет, конечно. Это была полнейшая глупость, никакой мины тут быть не должно. "
    "Однако тележка сильно кренилась на левый бок, а одно из её колёс кружилось волчком в стороне. Всё-таки не была она рассчитана на такой вес."
    
    stop environment_sounds_dream fadeout 10
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 10 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Я был несказанно рад такому повороту событий и немедленно поспешил к месту аварии."
    
    #Мини ЦГ - тележка и рация, валяются
    image Radio_Set_And_Cart_On_The_Ground = "images/cg/DAY_01/04a_Trash_Place_Meeting/Radio_Set_And_Cart_On_The_Ground/Radio_Set_And_Cart_On_The_Ground.png"
    image Radio_Set_And_Cart_On_The_Ground_Moved:
        contains:
            "Radio_Set_And_Cart_On_The_Ground"
            xpos 400
            pause 0.7
            ease 5.0 xpos 700
    
    image Radio_Set_And_Cart_On_The_Ground_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 800
    
    image Radio_Set_And_Cart_On_The_Ground_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 800
    
    image Radio_Set_And_Cart_On_The_Ground_Masked = AlphaMask( "Radio_Set_And_Cart_On_The_Ground_Moved", "Radio_Set_And_Cart_On_The_Ground_border_01_right_mask_moved" )
    
    image Radio_Set_And_Cart_On_The_Ground_With_Border_01:
        contains:
            "Radio_Set_And_Cart_On_The_Ground_Masked"
        contains:
            "Radio_Set_And_Cart_On_The_Ground_border_01_right_moved"
    ##
    
    show Radio_Set_And_Cart_On_The_Ground_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    play music "sounds/music/track_09.mp3"
    "Вид у девушки был совершенно растерянный. Её тележка валялась в стороне, и, судя по всему, пришла в полную негодность"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    blind_girl "Что с моей тележкой?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "С тревогой в голосе спросила она."
    "Я глянул на то место, где раньше располагались колеса. Там остались только чёрные втулки с обломанными спицами."
    
    kenji "Кранты ей, похоже."
    
    hide Radio_Set_And_Cart_On_The_Ground_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent wit Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Я стащил рацию и подал тележку девушке."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Она сразу же принялась изучать тележку, пытаясь определить её состояние. "
    "Мне почему-то стало смешно от выражения её лица, когда она наконец нащупала место крепления колёс. "
    "Пришлось проглотить идиотский смешок, который чуть было не вырвался наружу."

    kenji "Что теперь делать будешь?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Не знаю..."
    blind_girl "Эта тётина тележка. Я обещала, что верну её в целости."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Она вздохнула."

    "Неужели тётка будет отчитывать эту несчастную слепую девчонку из-за какой-то тележки? "
    "Вполне возможно, она добрая женщина, и её племяннице просто стыдно, что она угробила чужую вещь."
    "Но в моей голове родился образ омерзительной старой карги, которая по возвращении девушки ухватит её за волосы и потащит по улице, крича о жутком преступлении, которое та совершила."

    "Какие идиотские мысли. Похоже, доза пива, выпитая залпом, ударила-таки мне в голову. "
    "Злость, испытываемая ранее, внезапно улетучилась, и подступила непонятная эйфория. Я посмотрел на девушку и задал неожиданный вопрос."

    kenji "А как тебя зовут?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А? Меня..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Девушка сильно заволновалась. Похоже, вопрос и в самом деле неожиданный. Но мне было плевать."

    kenji "Кендзи. Танака Кендзи!"

    "Сказал я и театрально ткнул себя пальцем в грудь."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Накамура... Касуми."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Кротко ответила девушка. Свою теперь уже бесполезную тележку она всё ещё не выпускала из рук."

    kenji "Сколько тебе лет?"

    "Вот это да! Я даже удивился собственной дерзости!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Шес... шестнадцать!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Отлично. Накамура Касуми, шестнадцать лет! Язык развязался и я, не в силах удержать внезапную словоохотливость, задвинул впечатляющую речь: "
    
    kenji "Послушай, Касуми, я понимаю, людям с твоими, эм... проблемами неприятно слышать такое, но вид у тебя совершенно потерянный."
    kenji "Ты уж извини! Я понимаю, что тебе хочется казаться сильной и независимой. И показать всем, что ты прекрасно обходишься, ну... ты меня поняла."
    kenji "Но вся эта чехарда с никчёмной тележкой у меня вызывает только жалость."
    kenji "Давай-ка я сам возьму в руки эту несчастную рацию и отнесу туда, куда тебе нужно."
    kenji "А ты выбрось эту тележку на свалку. Это теперь больше похоже на ходунки для стариков. Тёте твоей нужны ходунки, Касуми?"
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Касуми смотрела куда-то в сторону и молчала. "

    kenji "Или, может, мне лучше и вовсе унести эту рацию домой? Обратно к себе."
    kenji "Чего это я так разбрасываюсь вещами. А, Касуми? За сколько эту штуковину можно толкнуть на барахолке?"
    
    hide Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Нет! Простите, Танака-сан! Мне очень нужна эта вещь."
    kasumi "Пожалуйста, помогите мне донести её до дома!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я был рад этим словам, но, кажется, она догадалась, что я напрашивался в попутчики."
    "Впрочем, мне уже было всё равно. "
    "Я подозревал, что веду себя очень странно и, наверное, в такой ситуации правильнее было бы вызвать для бедной девочки такси и избавить ее от своего присутствия."
    "Но мне жутко не хотелось с ней расставаться."

    "Я поднял рацию за её родные ручки."

    kenji "Эй, Касуми, ты где живёшь?"
    
    "Касуми назвала адрес. Это было далеко отсюда. Раз в пять дальше, чем до моего дома."

    kenji "Э? Так далеко? Почему ты выносишь мусор именно сюда? У вас что там, своего места для хлама нет поблизости?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Есть. Совсем недалеко."
    kasumi "Но надо идти через канал, а весной пешеходный мост подмыло после сильного дождя."
    kasumi "Ремонт затянулся и теперь там не пройти. "
    kasumi "Недалеко есть автомобильная дамба. Но я не хожу там. Очень шумно — мне трудно ориентироваться."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Ну надо же! А ведь я тоже некомфортно себя чувствую в шумных местах! И наверняка Касуми не любит большие скопления людей. "
    "Ну прямо как я! Или вообще людей не жалует... "
    "Особенно навязчивых алкашей!"
    "От этой мысли я чуть приуныл."

    kenji "Ну что, идём? Да брось ты свою тележку! Хана ей!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет. Я попробую её починить! Колеса от неё, где они?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Я недовольно проворчал."

    kenji "Ну, одно колесо здесь лежит. А второго нет."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да, улетело, и теперь его нет. Хочешь пойти поискать?"
    

    "Я опять говорил с ней неприлично резким тоном. Услышав мои слова, Касуми тихо вздохнула."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Нет. Если улетело, то пусть. Но я всё равно возьму тележку с собой. Ладно?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Это ещё что за вопрос? Делай со своей тележкой что хочешь."
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 2
    scene Outdoor_Day_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )

    stop music fadeout 2
    "Мы двинулись. Я пристроился справа, встав между моей новой знакомой и обочиной дороги."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Простите, Танака-сан... но... не могли бы вы идти с другой стороны от меня?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    kenji "А? Зачем?"

    "Касуми подняла правую руку и указала на своё ухо."
    
    ##Мини ЦГ - Касуми в профиль
    image Kasumi_Profile = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Profile/Kasumi_Profile.png"
    image Kasumi_Profile_Moved:
        contains:
            "Kasumi_Profile"
            ypos -200
            xpos -700
            #pause 0.7
            #linear 10.0 xpos -500
    
    image Kasumi_Profile_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Kasumi_Profile_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Kasumi_Profile_Masked = AlphaMask( "Kasumi_Profile_Moved", "Kasumi_Profile_border_01_left_mask_moved" )
    
    image Kasumi_Profile_With_Border_01:
        contains:
            "Kasumi_Profile_Masked"
        contains:
            "Kasumi_Profile_border_01_left_moved"
    ##
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Kasumi_Profile_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Я увидел, что в него вставлен белый наушник."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    kasumi "Я буду плохо вас слышать. Лучше встаньте слева."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Я уже подумал было, что Касуми ещё и глухая, а в ухе у неё слуховой аппарат. "
    "Но нет, она же просит встать с другой стороны!"
    
    hide Kasumi_Profile_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "В левом ухе никаких наушников не было. Я стал разглядывать мою новую знакомую в профиль. "
    "Так не было видно её необычных глаз, поэтому казалось, что со мной рядом шла совершенно обычная девчонка."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Вы смотрите на моё ухо, Танака-сан?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Вдруг спросила Касуми."

    kenji "Я? Нет! Зачем мне это нужно?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Говорят, можно чувствовать кожей взгляды людей. Мне почему-то показалось, что вы смотрите именно туда."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Неправильно показалось!"
    
    "Пробурчал я и решил сменить тему."

    kenji "Чего это ты слушаешь в наушнике? Радио?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Касуми подняла руку и коснулась своего ободка с «усами»."

    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Это."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А что это такое?"

    "Мне и правда было интересно."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Это что-то вроде ёмкостного реле."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Чёрт! Мне бы больше подошёл ответ уровня «это устройство для связи с внеземными цивилизациями»."
    "Что такое «ёмкостное реле» я даже представить себе не мог. Звучало как термин из учебника физики. "
    "Но не припомню, чтобы школьный или институтский преподаватель физики щеголял на уроке с этим ёмкостным реле на голове. "
     
    #ЦГ - Портреты Ньютона и Галилео
    image Scientists = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Scientists/Scientists.png"
    image Galileo_And_Newton:
        contains:
            "Scientists"
        contains:
            "Dream_Frame"
    ##
    
    play environment_sounds_dream "sounds/environment/City_Suburb_Day_03_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    show Galileo_And_Newton with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_02.mp3"
    "Я вспомнил портреты великих учёных, которые висели в коридоре нашего университета. "
    "Галилео и Ньютон — оба на портретах были одеты в костюмы и никаких штуковин на голове у них не было. "
    
    #ЦГ - Портреты Эдисона и Теслы
    image Edison_And_Tesla:
        contains:
            "Scientists"
            ease 1.0 xpos -1920
            
        contains:
            "Dream_Frame"
    ##
    
    show Edison_And_Tesla
    hide Galileo_And_Newton
    
    "Даже такие интересные личности, как Эдисон и Тесла, ни разу это самое «реле» не надели. Удивительно!"
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    hide Edison_And_Tesla with Dissolve( my_dissolve_05 )
    
    kenji "А зачем оно? Для чего?"

    "Спросил я. И сразу подумал, что, должно быть, следующий ответ будет ещё непонятнее. "
    "Что-нибудь вроде «для измерения углового коэффициента пролетающих мимо нейтрино» или что-то в таком духе."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Оно реагирует на предметы. Чтобы было проще ориентироваться в пространстве."
    kasumi "Когда рядом с антеннами что-то есть, в наушнике пищит."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Хм... Здорово придумано. Сама сделала?"

    "Касуми покачала головой."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Не совсем. Мне помогли его собрать."
    kasumi "Но вообще-то оно не очень точное. В сухую погоду ещё неплохо работает, а в сырую или в туман с ума сходит."
    kasumi "Пищит по любому поводу. Приходится отключать его. Но тогда оно тоже помогает — как усы у кошки."
    kasumi "Хотя в плохую погоду на улицу я и не выхожу."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Интересно, кто помогал Касуми со сборкой этого приспособления? Должно быть, её отец. "
    
    image Old_Kasumis_Dad = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Old_Kasumi_Dad.png"
    image Old_Kasumis_Dad_Dream:
        contains:
            "Old_Kasumis_Dad"
        contains:
            "Dream_Frame"
        
    image Young_Kasumi_Dad = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Young_Kasumi_Dad.png"
    image Young_Kasumi_Dad_Dream:
        contains:
            "Young_Kasumi_Dad"
        contains:
            "Dream_Frame"

            
    image Dad_In_Room_Dream:
        contains:
            "Dad_In_Room"
        contains:
            "Dream_Frame"
    
    image Kasumi_And_Pervert_Dream:
        contains:
            "Kasumi_And_Pervert"
        contains:
            "Dream_Frame"
    
    play environment_sounds_dream "sounds/environment/City_Suburb_Day_03_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    scene Old_Kasumis_Dad_Dream with Dissolve( my_dissolve_05 )
    
    "Я представил его себе интеллигентным, худощавым, в толстых очках и с пышной, зачёсанной набок шевелюрой. "
    "Похожим на профессора физики в университете, где я учился. "
    
    scene Young_Kasumi_Dad_Dream with Dissolve( my_dissolve_05 )
    
    "Но профессор был старый, отец Касуми должен быть моложе. Если ей всего шестнадцать лет, то ему максимум слегка за сорок. "
    "Вероятно, он тоже радиолюбитель, как Макото-сан. Такой же увлечённый. "
    "Небось за своей радиостанцией и забыл, что его незрячая дочь шатается одна по улицам неизвестно где. "
    "И, наверное, это он такой заядлый курильщик."
    
    play sound "sounds/sounds/Morse_Code.mp3" fadein 1
    scene Dad_In_Room_Dream with Dissolve( my_dissolve_05 )
    
    "Я представил, как её отец сидит за рацией, крутит всякие крутилки, щёлкает тумблерами да смолит сигарету. "
    "Затем подходит к открытому окну и задумчиво смотрит на городской пейзаж. "
    
    stop sound fadeout 3
    scene Kasumi_And_Pervert_Dream with Dissolve( my_dissolve_05 )
    
    "И видит свою дочь, а рядом с ней — какого-то небритого, лохматого и нетрезвого извращенца. "
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    scene Outdoor_Day_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )

    "Я поёжился. Посмотрел на мятую рубаху и неопрятные брюки. Провёл ладонью по щетине и растрёпанной шевелюре. "
    "Слава богу, волосы на затылке, которые с утра стояли дыбом, теперь улеглись. Видимо, намокли от пота и потому перестали топорщиться. "
    "Хоть какой-то плюс. Правда, небольшой. "
    "Вообще хорошо, что Касуми меня не видит. Если бы она внезапно прозрела — вмиг убежала бы с криками. "
    "А так, если не брать во внимание запах алкоголя, я кажусь ей вполне приличным человеком."
    "На всякий случай я понюхал и свои подмышки. Вроде приемлемо. "
    "По крайней мере, запах сигарет, исходящий от Касуми, ощущается явно сильнее. Надо же, как пропахла!"
    
    stop music fadeout 2
    
    kenji "Касуми. А эта рация — она тебе для чего?"
    kenji "Ты тоже, как и мой погибший дядя, радиолюбитель? Или рацию ты хочешь кому-то отдать?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Что значит «кому-то отдать»? Нет! Эта рация нужна мне самой."
    kasumi "И да, Танака-сан, я, наверное, радиолюбитель."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Say with Dissolve( my_dissolve_02 )

    kasumi "А ваш дядя... Почему он погиб?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Мой дядя?"

    "Я пересказал историю, которую слышал от дяди Ватанабэ, и в конце рассказа добавил:" 

    kenji "Кажется, он обманул меня."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Почему же обманул?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А ты веришь в эту ерунду? Это самоубийство какое-то, провод под напряжением — вместо антенны. Чушь полная!"

    "Касуми пожала плечами."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Я однажды использовала вместо антенны нашу, бытовую сеть. Домашнюю."
    kasumi "Там, правда, всего сто десять вольт, а не несколько тысяч."
    kasumi "Но тоже немного опасно, конденсатор надо подобрать тщательно. Это не чушь!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Опять этот конденсатор! Везде конденсатор! "
    "Похоже, этот конденсатор — что-то вроде философского камня в среде радиолюбителей. "
    "А я про него ничего не знаю!"

    kenji "Зачем тогда вообще закидывать провод туда, где такое большое напряжение?"
    kenji "Раз ты говоришь, что в розетке всего сто десять вольт. Вот и втыкался бы туда!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Но тогда сигнал не выйдет дальше домашней сети. Там же трансформатор, слабая выйдет антенна."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Точно! И как я забыл про трансформатор!"
    
    "Если честно, про трансформатор я никогда и не вспоминал. Да и вообще впервые в жизни произносил это слово."

    kenji "Почему нельзя было просто привязать свою антенну к металлической опоре? Она же вон какая огромная."
    kenji "Чего ему не хватало?"
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Касуми отвернулась и поджала губы. Мне показалось, что она едва сдержала смешок. "
    "Ну да, похоже, я говорю полнейшую ерунду."
    
    hide Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Она же заземлена. Не получится из неё антенна!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я вспомнил ту металлическую опору, что стояла в нашем саду. "
    "Каждая из четырёх её лап была толстыми болтами прикручена к железобетонной плите. "
    "Она точно не соприкасалась с землёй!"

    kenji "Нет! Нет на ней никакого заземления!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Не может быть! Должно быть, вы просто не заметили, Танака-сан."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Нет! Я прекрасно вижу! Ничего там не было!"
    
    "Воскликнул я. А через секунду понял, насколько неприятную для собеседницы вещь сказал."
    "Но Касуми будто бы и не заметила ничего. На мгновение она задумалась."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hmm Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Она, наверное... она, наверное, заземлена сверху!"
    
    hide Day_Kasumi_School_Uniform_Hmm Normal_Say with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Заземлена сверху... Эта фраза совершенно добила меня. Да, чёрт возьми, Кендзи, сверху! "
    "Ха-ха! Плевать, что земля — она внизу. Тут, как пить дать, дело не обошлось без конденсатора. "
    "Впрочем, куда же без него, а, Кендзи? Как тебя вообще земля носит, без конденсатора-то?"
    
    "Наверное, дальше спорить не имело смысла. Я совершенно ничего не понимал в этих делах."
    "На некоторое время мы замолчали."
    
    scene Outdoor_Day_Street_01 with Dissolve( my_dissolve_05 )
    
    "Я взглянул на небо. Судя по солнцу, сейчас уже часов пять дня. Я достал телефон из брюк и посмотрел на время. Пять часов, десять минут. "
    "Ещё час и улицы наводнят люди, возвращающиеся с работы."
    
    "Пока что нам никто не встретился, хотя мы прошли уже больше половины пути. Здесь, думаю, уже жили люди, которые могли знать Касуми. "
    "Кто-то из них выглянет в окно, увидит, что к ней привязался какой-то мутный тип. Позвонит её отцу..."
    
    #ЦГ - Але тут педофилы
    image Here_Is_A_Pedo_01 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/01.png"
    image Here_Is_A_Pedo_02 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/02.png"
    image Here_Is_A_Pedo_03 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/03.png"
    image Here_Is_A_Pedo_04 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/04.png"
    image Here_Is_A_Pedo_05 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/05.png"
    image Here_Is_A_Pedo_06 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/06.png"
    
    image Here_Is_A_Pedo:
        contains:
            "Here_Is_A_Pedo_01"
        
        contains:
            pause 0.2
            "Here_Is_A_Pedo_02"
        
        contains:
            pause 0.4
            "Here_Is_A_Pedo_03"
        
        contains:
            pause 0.6
            "Here_Is_A_Pedo_04"
        
        contains:
            pause 0.8
            "Here_Is_A_Pedo_05"
        
        contains:
            pause 1.0
            "Here_Is_A_Pedo_06"
    
    show Here_Is_A_Pedo
    
    "..."
    
    hide Here_Is_A_Pedo with Dissolve( my_dissolve_05 )
    
    kenji "Касуми? А твои родители — они дома?"
    
    show Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_02 )

    "Моя спутница опустила голову и немного отвернулась от меня. Я что, задал неудобный вопрос?"
    
    show Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Мои родители... У меня... нет родителей."
    
    show Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_02 )

    "Да, и в самом деле неудачный вопрос."

    kenji "Извини... что спросил про такое."

    "Касуми пожала плечами."
    
    hide Day_Kasumi_School_Uniform_Cross_Arms_Half_Turn Normal_Silent with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Ничего. Я наверное, к этому уже привыкла."
    
    play environment_sounds "sounds/environment/City_Suburb_Day_04.mp3" fadein 1
    scene Outdoor_Day_Kasumi_Street with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_04.mp3"
    "Пару кварталов мы прошли молча. Не знаю, о чём думала Касуми, но меня донимали мысли о её отце."
    "А скорее, о том несуществующем человеке, которого я сам придумал. Мне даже стало жалко эту вымышленную личность."

    "Узнать бы у Касуми о судьбе её родителей. Но это не то, о чём может спрашивать такой малознакомый человек, как я. "
    "Всё же я поинтересовался, хоть и не напрямую."

    kenji "А с кем ты живёшь, Касуми?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "С тётей."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Значит, это её тётка столько курит! Хотелось спросить, как же эта женщина так пристрастилась к сигаретам. "
    "Но это был бы уже не просто неудобный, а крайне свинский вопрос. "
    "Я глубоко вдохнул, стараясь уловить побольше этого «аромата», исходившего от моей спутницы. "
    "Интересно, а как по-настоящему пахнет Касуми?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Почему вы вздыхаете, Танака-сан?"
    kasumi "Вам жаль меня? Из-за родителей?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да нет, я... то есть мне, конечно, жаль, что их нет, Касуми. Но вздохнул я... просто переводил дух. Устал."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Мы почти на месте!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я не так хорошо знал этот район города. Впрочем, я вообще мало знал мест вдали от дома, как и полагается порядочному хиккикомори."
    "Мы шли по узенькой улочке. Я опасливо озирался по сторонам, обшаривая взглядом окна и балконы."
    "Особенно я боялся увидеть тётку Касуми, хоть и совершенно не имел представления, как она выглядит."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Мой дом слева, второй за перекрёстком. Он жёлтого цвета, с синей черепицей."
    kasumi "Чтобы не утруждать вас, Танака-сан, я не буду проводить свои обычные, эм... ритуалы."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ритуалы?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Ну, мне нужно найти важные ориентиры, вы же понимаете. Кажется, сейчас я немного дезориентирована."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А, ну да."
    
    scene Day_Kasumi_Home with Dissolve( my_dissolve_05 )

    stop music fadeout 3
    
    "Действительно, как только мы прошли перекрёсток и первый дом за ним, я увидел маленький домик, выкрашенный бледно-жёлтой краской."
    "Площадка перед домом была посыпана гравием и усеяна разбитой тротуарной плиткой. Забор и ворота отсутствовали. "
    "По краям участка росли помидорные кусты."

    kenji "Кажется, пришли! Это у тебя во дворе растут помидоры, Касуми?"

    "Касуми не ответила. Вместо этого она повернулась в сторону своего дома, вытянула руки и пошла вперёд. "
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Как только её ноги ступили на гравий, она положила тележку на землю и повернулась ко мне. Похоже, теперь она сориентировалась."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Танака-сан! Вы так помогли мне!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Она учтиво мне поклонилась."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Большое вам спасибо! Может быть, вы хотите выпить чая?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Да, конечно! Я бы выпил чая с Касуми, если бы знал, что больше никогда её не увижу. "
    "Но ещё в пути у меня созрел хитрый план."

    kenji "Нет, Касуми!"

    "Похоже, мои слова ее удивили."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Не хотите?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не очень. Я лучше пойду поскорее домой."

    "Касуми выглядела растерянной. Я поставил рацию на землю, возле бетонного столбика."

    kenji "Рация. Я её здесь оставлю. Донесёшь до дома? Касуми?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Тётя мне поможет!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    kenji "Хорошо. А тележку твою я конфискую."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Но зачем? Что значит конфискуете? Это не моя, тётина. Что я ей скажу?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не боись. Завтра верну в целости."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Я поднял тележку и повесил на плечо."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Завтра?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Во сколько я могу её занести? В час дня, например?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "В час дня..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )

    "Рассеянно произнесла девушка. А потом словно встрепенулась."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Да, как вам будет удобно!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А ты будешь дома?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Да! Буду дома."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну и отлично..."

    "Касуми ещё раз поклонилась мне."

    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Прощайте, Танака-сан!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Пока!"
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_02 )

    "Ответил я ей. Хотелось ещё добавить «до завтра», но мне показалось, что это будет слишком."
    
    play environment_sounds "sounds/environment/City_Evening.mp3" fadein 1 fadeout 1
    scene Outdoor_Evening_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_07.mp3"
    
    "Около семи часов вечера я вернулся на площадку для сбора мусора. Она опустела — всё уже забрали уборщики."
    "Подоспел к площадке я вовремя. На обратном пути от дома Касуми я купил чипсы, которые уже успел доесть, и теперь нужно было избавиться от упаковки."

    "На улицах стало оживлённее, всё чаще мимо проезжали машины, мопеды, мелькали велосипедисты. "
    "Собачники повели своих питомцев на прогулку. На детских площадках появились дети и присматривающие за ними мамочки. "
    "Я как мог увиливал от идущих мне навстречу людей. Переходил улицу, чтобы встать с другой стороны. Проскакивал в узких безлюдных переулках. От одной группы смеющихся старшеклассниц и вовсе спрятался в кустах. "
    "Сейчас, конечно, самое правильное решение — укрыться поскорее в доме, но мне за сегодня нужно сделать ещё одно дельце. "
   
    
    #Спрайты Айко в мобильном телефоне
    image Kenji_MObile_Phone = "images/cg/DAY_01/06a_Watanabe/Kenji_Mobile_Phone/Kenji_Mobile_Phone.png"
    image Kenji_MObile_Phone_Mask = "images/cg/DAY_01/06a_Watanabe/Kenji_Mobile_Phone/Kenji_Mobile_Phone_Mask.png"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent"
            
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent"
    
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked = AlphaMask( "Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    #
    
    play sound "sounds/sounds/Mobile_Phone_Vibration.mp3"
    show Kenji_MObile_Phone with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )

    "У меня зазвонил телефон. Это была Айко."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked

    aiko "Кендзи, ты где?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked

    "Голос её был взволнован."

    kenji "Я? Да практически возле дома. Но приду чуть позже."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked
    
    aiko "Я думала, ты так напился, что не смог найти дорогу домой. Ты что, выпил всё своё пиво?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked
    
    kenji "Ну да..."

    "Айко возмущенно завопила:"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked

    aiko "Ты алкоголик!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked
    
    kenji "Постой, Айко! Три банки пива — это не три бутылки водки, ты не путай! Чего ты так раскричалась?"

    "Но ей, конечно, было всё одно, что водка, что пиво. Я действительно редко выпивал за день больше одной или двух банок. Если пил вообще."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked

    aiko "В магазин утром пойдёшь сам! И завтрак в дорогу тоже сам себе готовить будешь!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked
    
    kenji "Завтрак в дорогу? Зачем? Ты меня из дома завтра погонишь?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked
    
    aiko "Ты же на море собрался, разве нет?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked
    
    kenji "Ах, точно! Я совсем забыл. Прости, Айко, но, похоже, с поездкой на море придётся повременить."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked
    
    aiko "Почему?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Say_Mobile_Masked
    
    kenji "Дела. Мне надо... Встретиться кое с кем."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Surprised_Silent_Mobile_Masked
    
    aiko "Этот кто-то — тоже алкоголик?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked
    
    kenji "Айко, бросай свои шуточки! Надеюсь, ты не обиделась, что на море мы завтра не едем?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Silent_Mobile_Masked
    
    aiko "Мне-то что? Я могу в любой день пойти в бассейн. А могу даже поехать на пляж без тебя, с подружками."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile_Masked

    "Я вздохнул. Айко помолчала какое-то время и спросила:"

    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked

    aiko "Куда ты сейчас?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Say_Mobile_Masked
    
    kenji "Мне надо зайти к дяде Ватанабэ."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Normal_Silent_Mobile_Masked
    
    aiko "Да? Ладно. Но я позвоню ему и скажу, чтобы он тебе не наливал!"
    
    hide Day_Aiko_Home_Outfit_Hand_Hold_Hand_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Kenji_MObile_Phone with Dissolve( my_dissolve_02 )
    
    kenji "Айко!"

    "Айко бросила трубку. Я выругался про себя и убрал телефон в карман. "
    "Теперь меня занимали мысли об алкоголиках. А точнее, стал ли я уже одним из них. Или Айко, как всегда, преувеличивала?"
    "Настоящих алкоголиков я знал немного — пожалуй, всего одного. Это был тот самый умерший телемастер из моего детства, дядя Сато. "
    "Тот, в чью честь воздвигли пирамиду из его же телевизоров. "
    "Он пил «по-настоящему». Мои нынешние пивные посиделки — капля в море водки, которую выпил дядя Сато. "
    "Я же водку на дух не переносил, как и любой другой крепкий алкоголь. "
    "Нет. Мне быть алкоголиком не грозит. Ну кто же может стать алкашом, употребляя только пиво?"
    
    play environment_sounds "sounds/environment/City_Industrial_Day.mp3" fadein 1 fadeout 1
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    stop music fadeout 3
    
    "Размышляя над этим, я и не заметил, как добрался до дома Ватанабэ. На мою радость, его гараж, и одновременно — мастерская, был открыт. "
    "Дядя Ватанабэ ещё не закончил работать. "
    "Я подошёл ближе и поздоровался с ним."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "А, привет, Кендзи! Гляди. Парень десять тысяч накрутил, а звёздочка распредвала не съедена."
    watanabe "И цепь не растянулась, ни на миллиметр! И натяжитель держит."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Что такое «цепь» и «звёздочка» мне, может быть, было понятно."
    "Но что за зверь такой этот «распредвал», я не знал совершенно."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Но что-то гремит. Я думал — ну точно распредвал, что ещё может?"
    watanabe "Столько времени потратил, чтобы генератор снять. Плотно он засел!"
    watanabe "Чуть на съёмнике резьбу не съело! Прокладку порвал! А внутри — всё целёхонькое!"
    watanabe "Что же тогда гремит-то, Кендзи?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Как обычно, дядя Ватанабэ задавал мне вопросы, на которые я не знал ответа. И он сам это понимал, но такая уж у него была привычка."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А!"
    watanabe "Айко звонила. Говорит, ты нажрался как свинья и шатаешься по городу!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Айко! Вот чертовка!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ты правда пьяный?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Три банки пива выпил, только и всего. А Айко как всегда на своей волне. Ну, вы же знаете."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Три банки! Не смертельно, но солидно. Что празднуешь?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да я мусор выносил. Кладовку освобождаю. Тётя Наоки просила, чтобы я вещи дяди Макото выбросил."
    kenji "Вещи тяжёлые, рация там и ещё что-то к ней. Уморился."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Sad_Say with Dissolve( my_dissolve_02 )

    watanabe "А..."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Sad_Silent with Dissolve( my_dissolve_02 )

    "Голос его внезапно стал сиплым."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Sad_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Наоки ко мне приходила, спрашивала, не хочу ли я забрать чего."
    watanabe "Но мне бы своё барахло выбросить. Так и лежит, пыль собирает, с тех пор как эти дела забросил."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Sad_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Радио?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ну да."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А почему забросили?"
    
    hide Evening_Watanabe_Work_Uniform_Cross_Arms with Dissolve( my_dissolve_01 )
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Почему забросил..."
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Silent with Dissolve( my_dissolve_02 )

    "Он задумался."
    
    hide Evening_Watanabe_Work_Uniform_Head_Scratching with Dissolve( my_dissolve_01 )
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_01 )

    watanabe "А что же мне, до скончания веков этим заниматься?"
    watanabe "Ты вот тоже, Кендзи, небось скоро забросишь компьютеры свои, найдёшь девчонку, женишься. Давно пора."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Почему-то при словах «найдёшь девчонку» я подумал о Касуми. Меня эта мысль немного смутила, даже слегка потеплели уши. "
    "А дядя Ватанабэ продолжал."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Теперь там всё по-другому, наши времена прошли." 
    watanabe "А Кайоши... Он даже был «радиопульсаром»! Он мне потом признался."
    watanabe "Узнай я в школьные годы, рожу бы ему начистил. А после уже, так..."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Он махнул рукой."
    kenji "Радио... пульс... пульсаром? Что значит — «был радиопульсаром»?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да это местное тайное общество. Можно сказать, радиолюбительская «масонская ложа»!"
    watanabe "А по мне — так просто хулиганы они."
    watanabe "Мы все их ненавидели, но каждый, мне кажется, моментально вступил бы к ним в клуб, появись у него такая возможность." 
    watanabe "Клуб — секретный! Никто не знал, кто в нём и как туда попасть."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Дядя Ватанабэ замолчал и о чём-то задумался. Я не вытерпел и спросил:"

    kenji "А что они делали?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Нам мешали! Правила вводили дурацкие. Дескать, никаких позывных в эфире, строгая анонимность."
    watanabe "А нам разве прикажешь? Но если кто их не слушал - того вышибали из эфира."
    watanabe "Были у них способы, глушилка, например. Глушить могли целыми днями, и даже неделями!"
    watanabe "Ещё и цензура была. Про что можно говорить в эфире, про что нельзя. Была даже листовка у меня — свод правил для вещания."
    watanabe "Вот такие были эти ребята. И Кайоши среди них, значит."
    watanabe "Но а потом мы из школы выпустились, и сильно поредел радиопульсар. А потом и совсем исчез."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да... А глушат, это как?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да как глушат?"
    watanabe "Включил рацию, а там не слышно ни хрена, значит, глушат. Вот как!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я ничего не понял, но дальше распрашивать не стал. Не моё это дело, что там у них и как. "
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А что это за штуковина у тебя, Кендзи?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А, это..."
    
    "Я вспомнил про тележку Касуми."
    
    kenji "Я ведь по делу пришел, дядя Ватанабэ. Починить надо..."

    "Я показал ему на культи, которые остались у тележки вместо колес. "
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А зачем? Тут проще новую купить, Кендзи."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Купить... Дело в том, что это не моя тележка."
    
    hide Evening_Watanabe_Work_Uniform_Cross_Arms with Dissolve( my_dissolve_01 )
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Ты, значит, когда мусор выносил, у кого-то тележку позаимствовал, а потом угробил?"
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну... Почти что так."
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Ну так купи и отдай им новую! Сколько такая хрень стоит? Три или четыре тысячи йен, не больше."
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Нет, дядя Ватанабэ. Мне бы починить её, ну, можно же?"
    
    hide Evening_Watanabe_Work_Uniform_Head_Scratching with Dissolve( my_dissolve_01 )
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Да где я тебе найду колёса такие?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну, не обязательно же прямо такие. От чего другого, может, тоже подойдёт?"

    "Ватанабэ покряхтел и скрылся в своей мастерской-гараже."
    
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    #Мини ЦГ - звук из гаража Ватанабэ
    image Watanabe_Garage_Sounds:
        contains:
            "empty_image"
        
        contains:
            ypos 250
            xpos 700
            "Emo_What_Horizontal_Flipped"
    ##
    
    play sound "sounds/sounds/Metal_Parts.mp3"
    show Watanabe_Garage_Sounds
    
    "Из глубины гаража донеслись гремящие звуки, кашель, тихая ругань. Спустя минуту дядя Ватанабэ вернулся. "
    
    hide Watanabe_Garage_Sounds
    
    ##Мини-ЦГ - велосипед Айко
    image Aiko_Bike = "images/cg/DAY_01/06a_Watanabe/Aiko_Bike/Aiko_Bike.png"
    image Aiko_Bike_Moved:
        contains:
            "Aiko_Bike"
            xpos 600
    
    image Aiko_Bike_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Aiko_Bike_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Aiko_Bike_Masked = AlphaMask( "Aiko_Bike_Moved", "Aiko_Bike_border_01_right_mask_moved" )
    
    image Aiko_Bike_With_Border_01:
        contains:
            "Aiko_Bike_Masked"
        contains:
            "Aiko_Bike_border_01_right_moved"
    ##
    
    show Aiko_Bike_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "В руках он нёс детский велосипед. Я воскликнул:"
    
    kenji "О! Это же старый велик Айко!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ага! Твой отец мне его отдал когда-то. Кажись, нашёлся донор!"
    
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    "Дядя Ватанабэ снял какие-то металлические кольца с краёв оси тележки, выкинул то, что осталось от прежних колёс, и примерил новые."
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Не подходят ни хрена! У тележки ось толще!"
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Silent with Dissolve( my_dissolve_02 )

    kenji "И что? Никак?"
    
    show Evening_Watanabe_Work_Uniform_Head_Scratching Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Почему никак? Щас рассверлим!"
    
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    "Он схватил тележку, велосипед и колёса и вновь скрылся в гараже."
    
    show Watanabe_Garage_Sounds
    play sound "sounds/sounds/Drill.mp3"
    "Послышалось жужжание и скрежет сверлильного станка. А через минуту дядя Ватанабе показался с тележкой."
    hide Watanabe_Garage_Sounds
    
    ##Мини ЦГ - Тележка с новыми колесами
    image Kasumi_Cart_With_New_Wheels_Evening = "images/cg/DAY_01/06a_Watanabe/Kasumi_Cart_With_New_Wheels/Kasumi_Cart_With_New_Wheels_Evening.png"
    image Kasumi_Cart_With_New_Wheels_Evening_Moved:
        contains:
            "Kasumi_Cart_With_New_Wheels_Evening"
            xpos -800
            #pause 0.7
            #linear 10.0 xpos -500
    
    image Kasumi_Cart_With_New_Wheels_Evening_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Kasumi_Cart_With_New_Wheels_Evening_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kasumi_Cart_With_New_Wheels_Evening_Masked = AlphaMask( "Kasumi_Cart_With_New_Wheels_Evening_Moved", "Kasumi_Cart_With_New_Wheels_Evening_border_01_left_mask_moved" )
    
    image Kasumi_Cart_With_New_Wheels_Evening_With_Border_01:
        contains:
            "Kasumi_Cart_With_New_Wheels_Evening_Masked"
        contains:
            "Kasumi_Cart_With_New_Wheels_Evening_border_01_left_moved"
    ##
    
    show Kasumi_Cart_With_New_Wheels_Evening_With_Border_01 with Dissolve( my_dissolve_05 )
    
    watanabe "Ну, вроде всё."

    "Он протянул тележку мне."
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Эти колёса в сто раз лучше будут. Крепкие! Уже не сломаешь!"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Silent with Dissolve( my_dissolve_02 )

    "Я покатал тележку по земле. Колёса крутились, хоть и туго. "
    
    hide Kasumi_Cart_With_New_Wheels_Evening_With_Border_01 with Dissolve( my_dissolve_05 )

    kenji "Сколько с меня?"
    
    show Evening_Watanabe_Work_Uniform_Cross_Arms Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Нисколько! Только помоги мне закатить мотоциклы в гараж. Но смотри, держи под наклоном, чтобы масло не вытекло!"
    
    play environment_sounds "sounds/environment/City_Evening.mp3" fadein 1 fadeout 1
    scene Outdoor_Evening_Kenji_Home with Dissolve( my_dissolve_05 )

    "Покончив с этим, я отправился домой."
    "И десяти минут не прошло, как я был возле дома. Тележку я в дом заносить не стал, спрятав её за палисадником с цветами. "
    "Земля в палисаднике была влажная — видимо, Айко совсем недавно поливала цветы. Я вошёл в дом."
    
    play environment_sounds "sounds/environment/Kitchen.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 ) 
    
    "Айко на кухне не было. Я включил телевизор и задумался о своём ужине. Очень хотелось есть. "
    "За сегодняшний день я съел только тарелку салата да пачку чипсов. А уже поздно — восьмой час. "
    "В такое время я всегда был дома и ужинал вместе с Айко."
    "Можно было, конечно, сбегать наверх, в её комнату, и попросить приготовить мне чего. Но не хотелось попадаться Айко на глаза."
    "Я решил заварить себе рамен. "
    
    image Instant_Noodles = "images/cg/DAY_01/07a_Kenji_Evening_Meal/Instant_Noodles/Instant_Noodles.png"
    scene Instant_Noodles with Dissolve( my_dissolve_05 )
    
    "Телевизор по-прежнему показывал новости. Шёл блок про незначительные события."

    tv "А ведь слоновья нога до сих пор плавит бетон четвертого энергоблока..."

    play music "sounds/music/track_03.mp3"
    
    "Но я не особо вникал, мой трезвеющий мозг занимали раздумья о Касуми. "
    "Вернее, беспокойные мысли, связанные с нашими дневными похождениями."
    "Правильно ли я сделал, что навязался в помощники? Не видел ли нас вместе кто-то из знакомых? "
    "Может быть, не стоило забирать у неё тележку. Что она сейчас скажет своей тётке? "
    "Не был ли слишком навязчив и груб?"

    "Я помнил, как Касуми вела себя — слишком сдержанной она была, неулыбчивой. Наверное, несладко ей живётся, будучи слепой сиротой. "
    "Говорят, такие люди тянутся к тем, кто делает для них добро. А я для неё столько сделал! "
    "Но она всё равно... "
    "Может, жизнь её так потрепала, что она просто боится всех? "
    "Ну прямо как я! "
    "Или нет? Касуми не показалась мне уж очень застенчивой. И она точно не выпивает «для храбрости». "

    "Я вновь прокрутил в голове сцену встречи с ней, поход к её дому. Вспомнил, какой спокойной была Касуми. Не помню, чтобы она весело смеялась. "
    "А я шутил? Надеюсь, что нет! Шутки у меня, подвыпившего, небось, дурацкие. "
    "Как она называла меня, тоже вспомнил — «Танака-сан». "
    "Ну да, про мой возраст она наверняка догадалась. А как ведут себя молодые девчонки с незнакомыми взрослыми мужчинами? Скорее всего, именно так! "
    "Может, она так реагировала, потому что я был пьян? Наверное, несло алкоголем от меня исправно! "
    "А от неё куревом! Все мы не без недостатков, получается."
    "Хотя я уверен, Касуми не курит. Она хорошая! "
    "Просто ангел!"
    
    kenji "Прости меня, Касуми, за всё!"

    "Вполголоса пробормотал я. "

    aiko "Пришёл!"
    
    ##Мини ЦГ - Айко в дверях кухни
    image Evening_Kenji_Kitchen_Door = "images/bg/Indoor/Kenji_Home_Kitchen/Evening/Door.png"
    image Evening_Kenji_Kitchen_Door_Moved:
        contains:
            "Evening_Kenji_Kitchen_Door"
            xpos -800
            #pause 0.7
            #linear 10.0 xpos -500
    
    image Evening_Kenji_Kitchen_Door_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Evening_Kenji_Kitchen_Door_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Evening_Kenji_Kitchen_Door_Masked = AlphaMask( "Evening_Kenji_Kitchen_Door_Moved", "Evening_Kenji_Kitchen_Door_border_01_left_mask_moved" )
    
    image Evening_Kenji_Kitchen_Door_With_Border_01:
        contains:
            "Evening_Kenji_Kitchen_Door_Masked"
        contains:
            "Evening_Kenji_Kitchen_Door_border_01_left_moved"
    ##
    
    show Evening_Kenji_Kitchen_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    "Я и не заметил, как на кухню пробралась Айко. Она внимательно смотрела на меня."
    "Наверное, хочет определить, насколько я пьян! А я уже практически трезвый. "
    "Надеюсь, она не слышала моих извинений!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 

    aiko "Где ты был?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    kenji "Как где? У дяди Ватанабэ, я же говорил! А до этого вещи из кладовки выносил. Где же мне ещё быть?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    aiko "Что-то долго ты выносил вещи!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Не хотелось рассказывать Айко про Касуми."

    kenji "Ну да, выносил чуть не до шести часов. Что тут такого?"
    kenji "И вообще, это что за допрос? Я жутко устал! Отстань, Айко!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Айко вздохнула."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    aiko "Ладно, извини. Всё-таки я волновалась за тебя."
    aiko "Ушёл и с концами. И пиво всё выпил!" 
    aiko "Я думала, вдруг в канаве утонешь. Помнишь, как тот алкоголик, про которого рассказывал папа?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Меня снова чуть покоробило, когда Айко назвала моего отца «папой». "
    "А алкоголик, утонувший в канаве — не кто иной, как дядя Сато. Именно так он отправился на тот свет. "
    "Свалился пьяным в придорожную канаву и захлебнулся в ней."

    kenji "Да сейчас в канаве и не утонуть. Они же все пересохли!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Айко улыбнулась."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    aiko "Ну да!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    kenji "Кстати, раз уж речь зашла об утопленниках и канавах! Ты сейчас не идёшь в душ, Айко?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    aiko "А? Нет! Почему спрашиваешь?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    kenji "Мне туда надо! Срочно! Кажись, я здорово употел, пока с барахлом из кладовки возился!"
    kenji "Айко, пожалуйста, наполни ванну водой!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    aiko "Хорошо!"
    
    hide Evening_Aiko_Home_Outfit_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 ) 

    "Айко убежала вверх по лестнице. Видимо, она немедленно решила исполнить мою просьбу."
    "Я между тем закончил свой ужин, сложил посуду в мойку и отправился на второй этаж. "
    
    image Evening_Kenji_Bedroom = "images/bg/Indoor/Kenji_Bedroom/Evening/Base.png"
    play environment_sounds "sounds/environment/Shower.mp3" fadein 1 fadeout 1
    scene Kenji_Home_Bathroom with Dissolve( my_dissolve_05 )
    
    stop music fadeout 3
    
    "Ванна была полна чуть больше, чем наполовину. "
    "Я тщательно выскоблил себя мочалкой. Правда, руки и шея здорово сгорели на солнышке, и мочалкой к ним было не прикоснуться. "
    "Лицо от жары покрылось пятнами. Я смотрел на себя в зеркало и с неудовольствием отмечал, какой клоунский у меня вид. "
    "Красные, обгоревшие нос и скулы, тёмные синяки под глазами, щетина. "
    "Жуть. "
    "А может, лучше так, чем бледное как смерть лицо безвылазного домоседа?"
    
    "Я взял бритву и тщательно побрился, подровнял виски. Но собственное отражение в зеркале мне всё равно не нравилось. "
    "Без бороды вид у меня стал совершенно беспомощный. Наверное, надо было её просто укоротить машинкой для стрижки, а не сбривать полностью. "
    "Хотя какая разница. Я же собираюсь понравиться человеку, который ничего не знает о моём внешнем виде. И не узнает."
    "Впрочем, нет. Я собираюсь понравиться человеку, который наверняка видит прекрасно и рассмотрит меня с особым пристрастием. "
    "Этот человек — тётка Касуми. "
    "Придётся постараться и придать себе более презентабельный внешний вид. "
    "Хорошо одеться, но неброско. Надеюсь, у меня в запасах есть дезодорант и одеколон. "
    "Ну а если нет, наверняка в комнате отца и тёти Наоки что-то осталось. "
    "Надо только не перестараться, у Касуми наверняка нюх отменный!"
    "Или нет — учитывая, что от неё за версту тянет сигаретным дымом? Хотя, говорят, не чувствовать собственный запах — основа нюха!"
    
    ##ЦГ - Касуми с руками Кензи у нее на плечах
    image Dreams_About_Kasumi = "images/cg/DAY_01/08a_Kenji_Bath_Time/Dreams_About_Kasumi/Dreams_About_Kasumi.png"
    image Dreams_About_Kasumi_Moved:
        contains:
            ypos -300
            "Dreams_About_Kasumi"
            pause 0.5
            ease 5.0 ypos -500
        
        contains:
            "Dream_Frame"
    play environment_sounds_dream "sounds/environment/Shower_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    show Dreams_About_Kasumi_Moved with Dissolve( my_dissolve_05 )
    
    "Я снова задумался о том, как пахнет Касуми."
    "Закрыл глаза, представил, как она стоит прямо передо мной. Я положил ладони ей на плечи и слегка наклонился, чтобы почуять запах кожи в том месте, где её шея выглядывает из-под ворота матроски."

    "Мысль о том, что я выгляжу как идиот, кольнула меня."
    
    stop environment_sounds_dream fadeout 1
    play environment_sounds "sounds/environment/Shower.mp3" fadein 1 fadeout 1
    hide Dreams_About_Kasumi_Moved with Dissolve( my_dissolve_05 )
    
    "Я открыл глаза и опустил руки. "
    "Конечно, никакого запаха Касуми я не мог почувствовать, даже если бы и в самом деле взял её за плечи и уткнулся носом в шею."
    "Только удушающий аромат сигаретного дыма."
    
    "Я забрался в ванную. Вода невыносимо жгла сгоревшие на солнце руки, и я положил их на бортики ванны. "
    "Опираться на заднюю стенку ванны тоже было неприятно — болела спина. "
    "Я потёр ладонями плечи и подумал о том, какие они на ощупь, плечи Касуми. "
    "Мне очень захотелось прикоснуться к ним наяву, так же, как минуту назад в своём воображении. Или провести ладонью по её голове. "
    "Хотя бы просто притронуться к рукавам её формы или краю юбки. "
    "Если сделать это осторожно, она же не заметит? Будет ли ещё такая возможность?"

    "Почему-то в тот момент, когда мы с ней шли, я не думал о таком. Да и телесных контактов с Касуми я не припомню. "
    "Только как её руки вцепились в мою ногу. А больше ничего. "

    "Я слышал, что когда парень и девушка идут рядом, иногда тыльные стороны их ладоней случайно соприкасаются. "
    "Но с Касуми у меня такого не было. Наверное, я старался держать дистанцию. "
    "Или было, но я в тот момент не заметил или не придал значения? "

    "Я закончил гигиенические процедуры и вышел из ванной."
    
    play environment_sounds "sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_05.mp3"
    
    "В своей комнате я приступил к подбору одежды для завтрашнего мероприятия. "
    "У меня есть отличные джинсы для особых случаев. Им уже лет пять, не меньше, но они в прекрасном состоянии — так редко я их надеваю. "
    "В пару к джинсам я решил надеть рубашку в клетку. Рубаха была на вид бледноватой, как будто на солнце выгорела, но мне нравился её неброский вид."

    "Джинсы можно было надевать хоть сейчас, а рубашку, наверное, стоило погладить.  "
    "Утюг и доска для глажки были на кухне, там же, где и стиральная машина. "
    "Надо бы подгадать момент, когда Айко не будет на кухне. А то ещё подумает чёрт знает что. Что за встреча, к которой я так тщательно готовлюсь?"

    "Мне в голову пришла свежая идея. Я придумал способ маскировки некоторых недостатков своей внешности. "
    
    #Мини ЦГ - очки Кендзи
    image Kenji_Glasses = "images/cg/DAY_01/08a_Kenji_Bath_Time/Kenji_Glasses/Kenji_Glasses.png"
    image Kenji_Glasses_Moved:
        contains:
            "Kenji_Glasses"
            xpos 650
    
    image Kenji_Glasses_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kenji_Glasses_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kenji_Glasses_Masked = AlphaMask( "Kenji_Glasses_Moved", "Kenji_Glasses_border_01_right_mask_moved" )
    
    image Kenji_Glasses_With_Border_01:
        contains:
            "Kenji_Glasses_Masked"
        contains:
            "Kenji_Glasses_border_01_right_moved"
    ##
    
    show Kenji_Glasses_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Этот способ — очки. "
    "Нет, у меня хорошее зрение, пусть оно и подсажено немного сидением за компьютером сутки напролёт. "
    "Это очки без диоптрий, в чёрной пластмассовой оправе. Специальные. "
    "Говорят, спасают от излучения, испускаемого монитором. На самом деле это очки отца, но и мне подошли идеально."
    
    hide Kenji_Glasses_With_Border_01 with Dissolve( my_dissolve_05 )

    "Я надел очки и подошёл к зеркалу. "

    "Да, так определённо лучше! Отливающие синевой стекла скрыли синяки под глазами. Да и массивная оправа перетягивала на себя всё внимание. "
    "Я даже помолодел! Стал выглядеть как студент выпускного курса. "
    "Удача, что я вспомнил про очки! Браво мне!"

    "Больше ничего путного насчёт своего внешнего вида я придумать не смог. "
    "Джинсы, рубашка, очки — что ещё надо? Все нормальные люди носят такое, а я хочу произвести впечатление нормального человека."

    "Теперь меня больше беспокоило то, как произвести хорошее впечатление на Касуми. "
    "Для неё совершенно неважно, во что я буду одет. "
    "Завтра алкоголем и по́том от меня нести не будет — это плюс. "
    "Что ещё может быть важно? Наверное, мой голос?"

    "Мне вдруг стало жутко интересно, как он звучит. Я порылся в списке приложений телефона. "
    "Нашёл то, что позволяет записывать звук. Нажал на запись и произнёс:"

    kenji "Касуми... Привет, это я! Кендзи!"
    
    "Затем я нажал на воспроизведение. То, что я услышал, повергло меня в шок. "
    "Пронзительный и гнусавый, очень неприятный мне голос. "
    "Какой ужас! И я так говорил всё это время? И тогда, с Касуми? "
    "Это полный крах! Я был по-настоящему подавлен. Я столько лет прожил с таким голосом и даже не знал, какой он противный. "
    "И с этим уже ничего не поделать!"

    "Или нет? Наверное, проблема не во мне! "
    "Точно! Это у телефона микрофон плохой! "
    "Мне нужен хороший, настоящий микрофон. Если я запишу с ним свой голос, он прозвучит как надо!"

    "И такой микрофон у нас дома был. Микрофон для караоке."

    "Мне нужно было в комнату отца и тёти Наоки! Это на первом этаже, по соседству с кухней. "
    
    scene Evening_Kenji_Parents_Room with Dissolve( my_dissolve_05 )
    
    "На виду необходимая мне вещь не лежала.  "
    "Я открыл один из ящичков под телевизором. Он был доверху набит дисками. Те лежали ровными пачками — видимо, Айко постаралась. "
    "Я вынул диски из ящика и расставил на полу. Я надеялся, что за ними, в дальнем углу, обнаружу микрофон. "
    "Но ничего подобного — только диски тут и были. "

    "Зато одна находка меня сильно заинтересовала. "
    "Последняя пачка дисков почти полностью состояла из фильмов для взрослых! Это явно отцовские! "
    "Я взял один фильм, чтобы рассмотреть поближе. "
    "Дизайн был совершенно идиотский, да и коробка видавшая виды — вся потёртая и в трещинах."

    aiko "Ты чего тут делаешь?"
    
    #Мини ЦГ - дверь в комнату родителей Кендзи
    image Kenji_Parents_Room_Door = "images/bg/Indoor/Kenji_Parents_Room/Evening/enji_Parents_Room_Door.png"
    image Kenji_Parents_Room_Door_Moved:
        contains:
            "Kenji_Parents_Room_Door"
            xpos 500
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kenji_Parents_Room_Door_Masked = AlphaMask( "Kenji_Parents_Room_Door_Moved", "border_01_right_mask_moved" )
    
    image Kenji_Parents_Room_Door_With_Border_01:
        contains:
            "Kenji_Parents_Room_Door_Masked"
        contains:
            "border_01_right_moved"
    ##
    
    show Kenji_Parents_Room_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    show Evening_Aiko_Nightie_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я обернулся. В дверях комнаты стояла Айко. Похоже, она собиралась спать и переоделась в пижаму."
    "Она перевела взгляд на мои руки, державшие диск с порнушкой."
    "Ба! Вот так ситуация! Надо как-то оправдаться!"

    kenji "Я искал тут кое-что!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Искал?"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Почти шёпотом спросила Айко."
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    aiko "И нашёл?"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что значит «нашёл»?"

    "Я поспешил избавится от компроментирующего диска, положив его на пол."

    kenji "Ничего я не нашёл! Я искал не это!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты понимаешь, что ты извращенец? Это же для извращенцев кино!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Suspect_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Как всегда! Эту ретропорнографию я не стал бы смотреть ни за какие коврижки. А тут такое!"

    kenji "Что значит «извращенец»? С чего ты так решила?"
    kenji "Я не виноват, что здесь валяется эта фигня."
    kenji "И вообще, это же моего отца! Он что, тоже извращенец?"
    kenji "Или нет, может, это твоего отца вещь, а, Айко? И он был извращенцем? Неужели так?"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Sorry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Наверное, зря я приплёл сюда покойного отца Айко. После этой фразы она опустила голову и произнесла жалобно:"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Sorry_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    aiko "Я хотела выкинуть! Когда убиралась здесь. Но потом забыла. Не хотела, чтобы ты нашёл, а ты всё-таки нашёл!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Sorry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Да не нужна мне вся эта ерунда! Мне нужен... микрофон для караоке! Вот зачем я полез сюда! Я ищу микрофон!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Angry_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты врёшь!"
    aiko "Наверное, ждал, когда я усну, чтобы взять это."
    aiko "Я поняла, какие у тебя завтра «дела»."
    aiko "Ты небось вступил в какой-то клуб извращенцев. И вы в этом вашем клубе будете смотреть эти непристойности!"
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Angry_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Да уж, неплохо у Айко фантазия работает. Теперь я ещё и в клуб извращенцев вступил! "
    "Странно, что не в клуб алкоголиков и извращенцев. Теперь её уж точно не переубедить! "
    "Раз уж я взял эту гадость в руки, мне не отвертеться! Остаётся только прогнать её поскорее из комнаты, а самому продолжить поиски."
    "Я театрально засмеялся."

    kenji "Ха-ха! Ты меня раскусила! Да! Завтра у меня встреча в клубе извращенцев!"
    kenji "Я возьму эти диски с собой, и завтра мы будем смотреть все фильмы! Здорово, а?"
    
    ##ЦГ - диск с порнущкой про сестру
    image Trip_To_Sea_With_Cute_Little_Sis = "images/cg/DAY_01/09a_Porn_In_Parents_Room/Trip_To_Sea_With_Cute_Little_Sis/Trip_To_Sea_With_Cute_Little_Sis.png"
    image Trip_To_Sea_With_Cute_Little_Sis_cg:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            xpos 473
            ypos 100
            "Trip_To_Sea_With_Cute_Little_Sis"
    #
    
    show Trip_To_Sea_With_Cute_Little_Sis_cg with Dissolve( my_dissolve_05 )

    "Я взял другой диск из кучи. Прочёл название фильма на обложке."

    kenji "Путешествие к морю с хорошенькой младшей сестрой..."

    "Господи! Неужели отец и такое смотрит? Или чьё это вообще? Почему мне попалось в руки именно это? "
    
    scene Evening_Kenji_Parents_Room with Dissolve( my_dissolve_02 ) 
    show Kenji_Parents_Room_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    show Evening_Aiko_Nightie_Hand_Hold_Hand Scared_Shy_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Лицо Айко исказила гримаса страха. Её уши и щеки залила густая краснота."
    "Я откинул диск в сторону и вскочил."

    kenji "Айко, я..."
    
    show Evening_Aiko_Nightie_Hand_Hold_Hand Scared_Shy_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Неееет!"
    
    play sound "sounds/sounds/Aiko_Run_Away_From_Parents_Room.mp3"
    hide Evening_Aiko_Nightie_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    hide Kenji_Parents_Room_Door_With_Border_01 with hpunch
    
    "Айко встрепенулась, резко дёрнулась в сторону двери и исчезла за ней. "
    "Раздался топот босых ног по лестнице, а затем я услышал, как захлопнулась дверь её комнаты."

    "Чёрт! А что, если Айко расскажет отцу? Наверное, ему не понравится такое!"
    "А впрочем, это же его вещи! Это он виноват, а не я! А мне, между прочим, тридцать лет. Стыдить меня просмотром порнушки — это бред."

    "Я приободрил себя этими мыслями, сложил пачки дисков обратно в ящик и выдвинул следующий. "
    "Тут меня ожидала удача! В ящике лежали коробка с микрофоном и толстая книжка — каталог песен. "

    "Больше мне в комнате родителей делать было нечего, и я поспешил к себе. "
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "Я распутал микрофонный шнур и поднёс штекер микрофона к разьёму на компьютере."

    kenji "Чёрт!"

    "Штекер оказался намного больше гнезда. Этот микрофон был совершенно несовместим с моим компьютером. "
    "Полный провал! "
    "Я порылся в коробке — может быть, там есть что-то вроде переходника? Нет, коробка была пуста."

    "Но, возможно, эта неудача была моим спасением. "
    "По правде сказать, я ужасно боялся, что и с этим «нормальным» микрофоном мой голос не станет звучать лучше. "

    "Увы. Я не обладал обворожительным, бархатным баритоном с хрипотцой. Говорят, от такого тащатся все девушки. "
    "Теперь мне совершенно ясно, почему у меня никогда не было подруги. "
    "Сейчас я бы пожертвовал любой деталью своей внешности, которая мне казалась нормальной. "
    "Пусть у меня будут кривые зубы, маленький подбородок или даже лысина. "
    "Но уверенный, красивый голос дал бы мне шанс на знакомство! Миллион шансов! Как жаль, что у меня нет и одного. "

    "Я сложил микрофон обратно в коробку, сел на стул и уставился в потолок. "
    "Мне подумалось, что, наверное, в интернете полно уроков для того, чтобы устранить гнусавость. "
    "Я включил компьютер и посмотрел парочку. "
    "Естественно, везде говорилось об упражнениях, которые надо выполнять вслух. "
    "Хотелось приступить прямо сейчас, но за тонкой стенкой, всего в нескольких метрах от меня, была Айко. "
    "Я надеялся, что она успокоилась после недавнего происшествия, позабыла, что я извращенец, и сейчас уже спокойно спит."

    kenji "А ведь у девчонок всё иначе! Им гнусавость даже идёт!"
    
    "Вполголоса воскликнул я. "
    
    #"Спрайты" одноклассников Кендзи
    image Kenji_Classmate_Girl = im.Scale( "images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Girl.png", 726, 1100 )
    image Kenji_Classmate_Girl_In_armor = im.Scale( "images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Girl_In_armor.png", 726, 1100 )
    image Kenji_Classmate_Boy = im.Scale( "images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Boy.png", 836, 1100 )
    image Kenji_Classmate_Boy_In_Armor = im.Scale( "images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Boy_In_Armor.png", 836, 1100 )
    
    #Мини - ЦГ полупрозрачный черный бэк справа
    image Kenji_Clasmate_Girl_BG_Right_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Kenji_Clasmate_Girl_BG_Right_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kenji_Clasmate_Girl_BG_Right_Masked = AlphaMask( "black_image", "Kenji_Clasmate_Girl_BG_Right_border_01_right_mask_moved" )
    
    image Kenji_Clasmate_Girl_BG_Right:
        contains:
            alpha 0.5
            "Kenji_Clasmate_Girl_BG_Right_Masked"
        contains:
            "Kenji_Clasmate_Girl_BG_Right_border_01_right_moved"
    ##
    
    show Kenji_Clasmate_Girl_BG_Right with Dissolve( my_dissolve_02 )
    show Kenji_Classmate_Girl at Move( ( 1600, 520 ), ( 1600, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Я вспомнил одну свою однокурсницу. Она сильно гнусавила! "
    "Наверное, благодаря пронзительному голосу её постоянно назначали старостой группы. "
    "Она могла докричаться до любого в аудитории — и неважно, насколько было шумно."

    "Я вспомнил её внешность. Она была довольно симпатичная. Небольшого роста, с длинными чёрными волосами."
    "Также я хорошо помнил, что она носила очки в тонкой оправе, а летом переходила на контактные линзы."

    "Говорят, девчонка эта многим нравилась. И у меня тоже была к ней некоторая симпатия. Естественно, я это скрывал. "
    "Однажды весной она принесла мне домой материалы для тестов, когда меня свалила простуда."
    "Это был невероятно удачный случай предложить ей встречаться или что-то в этом духе, но мне не хватило храбрости."
    "Тяжело живётся таким трусам, как я."

    "А потом я узнал, что у неё есть парень! Мне тогда показался странным её выбор."
    
    #Мини - ЦГ полупрозрачный черный бэк слева
    image Kenji_Clasmate_Boy_BG_Left_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Kenji_Clasmate_Boy_BG_Left_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kenji_Clasmate_Boy_BG_Left_Masked = AlphaMask( "black_image", "Kenji_Clasmate_Boy_BG_Left_border_01_left_mask_moved" )
    
    image Kenji_Clasmate_Boy_BG_Left:
        contains:
            alpha 0.5
            "Kenji_Clasmate_Boy_BG_Left_Masked"
        contains:
            "Kenji_Clasmate_Boy_BG_Left_border_01_left_moved"
    ##
    
    show Kenji_Clasmate_Boy_BG_Left with Dissolve( my_dissolve_02 )
    show Kenji_Classmate_Boy at Move( ( 300, 520 ), ( 300, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Начать хоть с того, что он был толстый как бочка! Когда на улице было тепло, с него ручьями тёк пот и пахло чем-то неприятным. "
    "У него была совершенно карикатурная кудрявая шевелюра, сросшиеся брови и невероятных размеров угри на носу."
    "Довершали образ нелепые очки в толстой роговой оправе. "
    
    "Несмотря на свой тучный вид, роста он был небольшого — я не припомню парней меньше него. "
    "И самое главное — он и сам страшно гнусавил, говорил очень торопливо, глотая слова. "

    "И этот человек был парнем нашей миленькой старосты! "
    "Каждую переменку они встречались и весело щебетали в коридоре, а во время большой перемены он неизменно вёл её к аппарату по продаже напитков и покупал сок."
    "В качестве благодарности она угощала его домашним бенто. "
    "После учёбы этот парень всегда провожал её до дома."
    "Кто-то даже говорил, что видел, как они целовались. Лица тех, кто слышал эту новость, невольно искажались гримасой отвращения."

    "Я как-то спросил своего соседа по парте: «Почему наша миленькая староста встречается с этим страшилищем?»."
    
    hide Kenji_Classmate_Girl with Dissolve( my_dissolve_01 )
    hide Kenji_Classmate_Boy with Dissolve( my_dissolve_01 )
    show Kenji_Classmate_Girl_In_armor at Move( ( 1600, 520 ), ( 1600, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Kenji_Classmate_Boy_In_Armor at Move( ( 300, 520 ), ( 300, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Помню, он ответил мне, что они вместе играли в одну игрушку, ММО или что-то в этом роде."
    "Улекались одним делом, в общем..."
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )

    "Я резко встал из-за стола. Вот что мне было нужно! Увлечение! Общее с Касуми увлечение! "
    "А уж чем увлекается она, мне известно. Жаль, я сам в этом деле полный ноль, но ничего! Я приложу усилия и удивлю её! "
    "Ха-ха! Все эти конденсаторы, транзисторы, ёмкостные реле — я их как орешки перещёлкаю!"
    
    stop music fadeout 2
    
    "Я выскочил из комнаты. Мне снова надо было на нижний этаж — в кладовку. "
    
    play environment_sounds "sounds/environment/Pantry_Evening.mp3" fadein 1
    image Evening_Kenji_Home_Pantry_Other_03 = "images/bg/Indoor/Kenji_Home_Pantry/Evening/Evening_Kenji_Home_Pantry_Other_03.png"
    scene Evening_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    
    "Я окинул взглядом стеллаж, на котором лежали книги. Старые книги дяди Макото, посвящённые радио и прочим сопутствующим вещам. "
    "Вот то, что мне нужно! Я ещё не успел разложить их по коробкам, и они занимали целую полку стеллажа."
    
    image Tube_Amplifiers_Book_Cover = "images/cg/DAY_01/10a_Makoto's_Books/Tube_Amplifiers/Tube_Amplifiers_Book_Cover.png"
    image Tube_Amplifiers_Book_Content = "images/cg/DAY_01/10a_Makoto's_Books/Tube_Amplifiers/Tube_Amplifiers_Book_Content.png"
    
    image Tube_Amplifiers_Book_Cover_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Tube_Amplifiers_Book_Cover"

    image Tube_Amplifiers_Book_Content_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Tube_Amplifiers_Book_Content"

    show Tube_Amplifiers_Book_Cover_CG with Dissolve( my_dissolve_05 )
    
    "Я вытянул первую попавшуюся. На обложке красовалась надпись «Ламповые усилители»"
    "Название мне сразу не понравилось, но я на всякий случай полистал её. "
    
    play sound "sounds/sounds/Open_Book.mp3"
    hide Tube_Amplifiers_Book_Cover_CG with Dissolve( my_dissolve_02 )
    show Tube_Amplifiers_Book_Content_CG with Dissolve( my_dissolve_02 )
    
    "Какие-то тексты и схемы на пожелтевших от времени страницах. "
    "Я совершенно ничего не понимал."
    
    play sound "sounds/sounds/Thick_Book_Fall.mp3"
    scene Evening_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    
    "Я кинул книгу в стоявший на полу пустой ящик. Первый блин комом, но разве меня это остановит? Как бы не так!"

    "Из разноцветной стопки я выцепил другую тоненькую книжку."
    
    image Pan_Stretching = "images/cg/DAY_01/10a_Makoto's_Books/Pan_Stretching/Pan_Stretching.png"
    image Pan_Stretching_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Pan_Stretching"
    
    show Pan_Stretching_CG with Dissolve( my_dissolve_05 )
    
    "«Расширение панорамы с помощью лыжной мази»"
    "Я перечитал название несколько раз. Но, похоже, эта книга здесь оказалась случайно и не имела к электронике никакого отношения. "
    
    hide Pan_Stretching_CG with Dissolve( my_dissolve_05 )
    play sound "sounds/sounds/Thin_Book_Fall.mp3"
    
    "Я не стал открывать её и сразу бросил в ящик."
    
    
    "Третья книга, которая попалась мне на глаза, никакого названия не имела."
    
    image KT315_Gondola_Cover = "images/cg/DAY_01/10a_Makoto's_Books/KT315_Gondola/KT315_Gondola_Cover.png"
    image KT315_Gondola_Cover_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "KT315_Gondola_Cover"
    
    image KT315_Gondola_Content = "images/cg/DAY_01/10a_Makoto's_Books/KT315_Gondola/KT315_Gondola_Content.png"
    image KT315_Gondola_Content_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "KT315_Gondola_Content"
    
    show KT315_Gondola_Cover_CG with Dissolve( my_dissolve_05 )
    
    "Что это вообще за ерунда?"
    "Я открыл её и перелистал."
    
    play sound "sounds/sounds/Open_Book.mp3"
    hide KT315_Gondola_Cover_CG with Dissolve( my_dissolve_02 )
    show KT315_Gondola_Content_CG with Dissolve( my_dissolve_02 )
    
    "Это о чем вообще?"
    "Что за бред сумашедшего?"
    
    hide KT315_Gondola_Content_CG with Dissolve( my_dissolve_05 )
    
    kenji "Нет, спасибо."

    play sound "sounds/sounds/Thick_Book_Fall.mp3"
    "Сказал я вполголоса и швырнул непонятную книгу вслед за остальными."
    
    image Electronics_For_Dummies_book_light = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/book_light.png"
    
    play environment_sounds_dream "sounds/sounds/Aah.mp3" fadein 1
    show black_image_alpha_50pc with Dissolve( my_dissolve_02 )
    show Electronics_For_Dummies_book_light with Dissolve( my_dissolve_02 )
    
    "И вот, наконец!"
    
    show Electronics_For_Dummies with Dissolve( my_dissolve_05 )
    hide Electronics_For_Dummies_book_light with Dissolve( my_dissolve_02 )
    
    "То, что надо! Яркая глянцевая суперобложка и приятный аромат свежей типографии, а не замшелой бумаги. "
    "Название согревает сердце и душу: «Электроника. Пособие для слабоумных хиккикомори»!"
    "О да! Слёзы радости заблестели на моих глазах..."
    
    
    play sound "sounds/sounds/Aah_Stop_Tape.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    hide Electronics_For_Dummies with Dissolve( my_dissolve_02 )
    hide black_image_alpha_50pc with Dissolve( my_dissolve_02 )
    
    "Конечно, нет. Не было у меня в руках такой книги. Здесь вообще нет книг. Только бесполезная макулатура! "
    "Зачем пишут эту отвратительную заумь? Кто читает эту хрень? Неужели Касуми в этом море непонятной информации чувствует себя как рыба в воде? Как ей это удаётся?"
    "Может быть, есть хоть одна книга для новичков? Почему здесь только громоздкие, неподъёмные для моего слабого мозга энциклопедии? "

    kenji "Интернет!"

    "Копаясь в куче дурацких книг, я напрочь забыл про интернет."
    "Я пулей бросился обратно в свою комнату."
    
    play environment_sounds "sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    play music "sounds/music/track_03.mp3"
    
    kenji "Интернет! Интернет! Интернет!"

    "Радостно нашёптывал я, щёлкая по клавишам компьютера."
    "Моё сердце затрепетало, когда я увидел результаты поиска."

    "Я зашёл на страницу интернет-магазина, продающего именно то, что мне нужно: «Радиоэлектроника для начинающих». "
    
    image Electronics_For_Beginners_Manga_Cover = "images/cg/DAY_01/10a_Makoto's_Books/Internet_Book/Electronics_For_Beginners_Manga_Cover.png"
    image Electronics_For_Beginners_Manga_Cover_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Electronics_For_Beginners_Manga_Cover"
    
    show Electronics_For_Beginners_Manga_Cover_CG with Dissolve( my_dissolve_05 )
    
    "Да, таких книг сотни, но мне попалась особенная — это был комикс. "
    "На обложке мультяшная, жизнерадостная школьница с большими глазами приветливо махала мне руками. "
    "А вокруг неё все эти транзисторы, конденсаторы и ещё чёрт знает что. Именно это мне и было нужно!"
    
    hide Electronics_For_Beginners_Manga_Cover_CG with Dissolve( my_dissolve_05 )

    "Я глянул на цену — пять тысяч йен. Да, дороговато."
    "Но ещё больше, если с немедленной доставкой до дома — пятнадцать тысяч."
    "Но мне не жалко таких денег, эта книга должна была стать моей!"

    "Но увы, как только я перешёл к заказу, на сайте высветилась предательская красная надпись. "
    "«Извините, но сейчас данный товар отсутствует, последний раз он был в наличии...». Я взглянул на дату — два года назад!"

    "Я обследовал другие интернет-магазины, что выдал мне поисковик. Но тщетно. Ни у кого этих книг не осталось. "

    "Я прошерстил интернет в попытках скачать копию, но и тут меня ожидала неудача."
    
    stop music fadeout 2

    "Раздосадованный и опустошённый, я выключил компьютер. На часах была половина первого. "
    "Я завёл будильник в телефоне на десять часов, скинул с себя верхнюю одежду и лёг в кровать."
    
    jump day_02
