init python:
    renpy.music.register_channel( "environment_sounds", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений
    renpy.music.register_channel( "environment_sounds_dream", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений (во время воспоминаний)

define kenji = Character( "Кендзи", color="#BBFF88" )
define aiko = Character( "Айко", color="#FF888B" )
define aiko_voice = Character( "Голос", color="#FF888B" )
define kasumi = Character( "Касуми", color="#88C0FF" )
define blind_girl = Character( "Девушка", color="#88C0FF" )
define watanabe = Character( "Ватанабе", color="#009900" )
define zak = Character( "Заказчик", color="#FFC95C" )
define tv = Character( "Телевизор", color="#FFC95C" )


label splashscreen:
    pause 1.0
    show Splash with Dissolve( my_dissolve_05 )
    pause 5.0
    hide Splash with Dissolve( my_dissolve_05 )
    pause 1.0
    return


label start:
    image white_image = "./images/other/colored/white.png"
    image black_image = "./images/other/colored/black.png"
    image black_image_alpha_50pc:
        contains:
            "black_image"
            alpha 0.5
    
    
    #Пыль
    image dust = Dust( "./images/other/dust.png" )
    #Рамка для флешбеков
    image Dream_Frame = "./images/cg/Misc/Dream_Frame/Dream_Frame.png"
    #пустая картинка
    image empty_image = "./images/other/empty.png"
    
    
    #Рамки для мини-цг
    image border_01_right = "./images/other/borders/01_Right/border.png"
    image border_01_right_mask = "./images/other/borders/01_Right/mask.png"
    image border_01_left = "./images/other/borders/01_Left/border.png"
    image border_01_left_mask = "./images/other/borders/01_Left/mask.png"
    
    image Midori_01 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_01.png"
    
    stop music fadeout 1
    play environment_sounds "./sounds/environment/Sea.mp3" fadein 2 fadeout 1
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
    "Наверное, вырвалась со своими подружками на море, сейчас же лето, каникулы..."

    "На вид Мидори лет шестнадцать, не больше. А это самый замечательный возраст! "
    "Будь мне сейчас столько же, я бы с удовольствием побегал вместе с Мидори по морскому берегу."
    "Сыграл бы с ней в волейбол... Ух! "

    "Но, к сожалению, мне уже давно не шестнадцать."

    kenji "Мне тридцать лет, Мидори! Тридцать!"

    "Похоже, её совсем не смутили эти слова и она по-прежнему улыбалась мне."
    "Приободрившись, я продолжил."

    kenji "А ещё я хиккикомори! Никчёмный тридцатилетний хиккикомори!"

    "Лицо Мидори не дрогнуло. Мне даже показалось, что ее улыбка стала чуть добрее, а в глазах заплясали радостные искорки."

    kenji "Конечно, Мидори! Будь я самым последним ублюдком на свете, ты бы ни за что не отвернулась от меня!"
    kenji "Я же для тебя самый дорогой человек на свете!"
    kenji "Я твой отец!"
    kenji "Даже больше! Я твой создатель!"
    
    kenji "И ты должна меня простить! Потому что я тебя... продал!"

    "Мне показалось, или веселья на лице девушки поубавилось? Я поспешил её успокоить."

    kenji "Но ты не бойся! Я продал тебя очень хорошему человеку! Я надеюсь…"
    
    #ЦГ - Мидори в графическом редакторе
    image Midori_Sea_BG_Non_Animated = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Midori_Sea_BG.jpg"
    image Midori_GE_Interface = "./images/cg/DAY_01/01a_Green-Haired_Girl/GE_Interface.png"
    image Midori_02 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_02.png"
    image Midori_In_GE_01:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_02"
        contains:
            "Midori_GE_Interface"
    
    
    scene Midori_In_GE_01 with Dissolve( my_dissolve_05 )
    play environment_sounds "./sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    
    "Я потёр глаза и чуть отодвинулся от монитора. "
    "Да, Мидори вышла очень миленькой. Думаю, человек, что заказал её, будет доволен."

    play sound "./sounds/sounds/Mobile_Phone_Vibration.mp3"
    "Вдруг завибрировал телефон. Похоже, мне прислали сообщение! "
    "Писал тот парень, что заказал рисунок с Мидори. Вовремя он появился!"

    zak "Йоу, чувак!"
    kenji "Привет. Твой рисунок готов. Сейчас перешлю его."

    "Я отправил рисунок заказчику и стал дожидаться его реакции. "
    "Если честно, я всегда волнуюсь в такие моменты, хоть и занимаюсь этим уже не первый год."

    zak "Это шедевр, чувак!"

    "Я самодовольно улыбнулся. "
    zak "Но..."

    "Черт! Похоже, ему что-то не нравится! Неужели я где-то накосячил? Надеюсь, он не хочет сбить обговоренную цену"
    "Неужели ему больше не нужен этот заказ, и он не будет платить остальную сумму за рисунок? Я озвучил свой вопрос в чате."

    zak "Нет, чувак! Не в этом дело! Я заплачу! Но понимаешь, наши с Мидори отношения…"
    zak "Кажется, они перешли на новый уровень!"
    kenji "Ваши отношения?!"
    zak "Ага, чувак… Раньше она казалась мне такой чистой и непорочной…"
    zak "А сейчас я все больше замечаю, какая она женственная… Какая притягательная…"

    "Единственное, чего мне хотелось сейчас — получить свои деньги, а этот парень нес какую-то чушь."

    zak "Какая у нее тонкая шея… А её ямочки на ключицах… Ох…"

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

    "Мне самому казалось, что такой милой девочке, как Мидори, хочется побегать со своими подружками по пляжу, без всякой задней мысли. "
    "Однако спорить с этим парнем я не стал. Он заказал Мидори, он её хозяин, а мне остаётся только одно — выполнить все его прихоти. "
    "Я попросил заказчика написать мне через полчаса, а сам принялся за рисунок."

    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_03 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_03.png"
    image Midori_In_GE_02:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_03"
        contains:
            "Midori_GE_Interface"
    
    "..."
    
    scene Midori_In_GE_02 with Dissolve( my_dissolve_05 )
    
    "Да, теперь определённо можно сказать, чего хочет Мидори. "
    "Вот только хочет ли она этого на самом деле? Взяла ли Мидори эту штуку в рот по своей воле, или это я её заставил? "
    "Черт! Я слишком много об этом думаю! "
    "Я покачал головой и прошептал."

    kenji "Прости меня, Мидори… Я не хотел..."

    zak "Эм… Рисунок отличный. Но, чувак, кажется я понял, чего действительно хочу!"
    kenji "Что опять?"
    zak "Я не мог понять, чего конкретно хочу! Но теперь знаю!" 
    zak "Ты можешь нарисовать ей ахегао-личико?"

    "Ну, по крайней мере, теперь я точно знал, что нужно сделать. "
    "К несчастью для меня, лицо Мидори опять нуждалось в серьёзной редактуре."
    
    kenji "Надеюсь, это все?"
    zak "Всё, чувак! Просто сделай ей ахегао, и я заплачу, сколько ты скажешь."
    
    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_04 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_04.png"
    image Midori_In_GE_03:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_04"
        contains:
            "Midori_GE_Interface"
    
    "..."
    
    scene Midori_In_GE_03 with Dissolve( my_dissolve_05 )
    
    "Пока я перерисовывал физиономию девушки, на душе у меня становилось все гаже. "
    "Я столько времени потратил на первоначальный рисунок, столько труда в него вложил! "
    "Да я почти сроднился с Мидори!"
    "А сейчас мне приходится издеваться над собственным творением ради этого похотливого болвана!"

    "Надо было просто надавить на этого парня и забрать свои деньги. "
    "Пусть несёт рисунок на доработку другому художнику. "
    "Или поступить как истинный джентльмен и вообще не отдавать ему Мидори. "
    "Ахегао-личико, ишь чего захотел! "
    "Эх… Ну почему я такой мягкотелый?"

    "Но ещё хуже было то, что этот парень вновь был чем-то недоволен."

    zak "Чувак… Можешь добавить ещё кое-что?"
    kenji "Я нарисовал всё, что ты хотел, разве нет? Я не могу переделывать этот рисунок вечно!"
    zak "Я знаю, чувак! И я перевёл деньги! Ты клевый художник, но пожалуйста, доделай этот рисунок."
    zak "Осталось совсем чуть-чуть до совершенства!"

    "Я поспешил проверить состояние своего счета. "
    "А он щедр! Парень заплатил за мою работу в два раза больше оговоренного. "
    "Мне даже стало стыдно за то, что я так плохо думал о нем."

    zak "Это не займёт много времени. Одна маленькая деталь."
    zak "Я уверен, это ничего не стоит такому мастеру, как ты!"
    kenji "Ну хорошо! Говори, я сделаю." 

    "Однако, увидев новую порцию пожеланий заказчика, я нервно сглотнул."
    
    scene black with Dissolve( my_dissolve_05 )
    
    image Midori_05 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori/Midori_05.png"
    image Midori_In_GE_04:
        contains:
            "Midori_Sea_BG_Non_Animated"
        contains:
            "Midori_05"
        contains:
            "Midori_GE_Interface"
    
    "..."
    
    scene Midori_In_GE_04 with Dissolve( my_dissolve_05 )
    
    "Действительно. Времени потребовалось совсем чуть-чуть. Хотя не припомню, чтобы я рисовал такое раньше. "
    "Мидори теперь была по-настоящему испорчена. Она была осквернена, окончательно и бесповоротно. "
    "И я сделал это собственными руками!"

    "А ведь это героиня популярного сейчас аниме-сериала."
    "Я его, конечно, не смотрел, но подозреваю, что Мидори там — отличница, президент кружка чайных церемоний, волонтер в местном храме."
    "И вообще, всем ребятам пример!"
    "Если бы она только знала, какую гадость с ней сделал такой никчёмный человек, как я..."

    #СЦЕНА - ДЕНЬ 1, АЙКО ЗАХОДИТ В КОНМНАТУ КЕНДЗИ И ВИДИТ МИДОРИ

    aiko_voice "Кендзи!"
    
    scene Day_Kenji_Home_Bedroom with Dissolve( my_dissolve_05 )
    
    "Я настолько ушел в свои мысли, что не сразу сообразил — меня зовут."
    
    #Мини ЦГ - дверь в комнату Кендзи, на фоне которого стоит Айко
    image Day_Kenji_Bedroom_Door = "./images/bg/Indoor/Kenji_Bedroom/Day/Day_Kenji_Bedroom_Door.png"
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
    
    show Aiko_Base_Outfit_03 Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "В дверях стояла Айко, моя младшая сестра."
    "Ой! Кажется, она уставилась в мой монитор!"
    "Я повернулся обратно к экрану. Там, как и раньше, красовалась Мидори, над которой я сегодня как следует поиздевался."
    "Черт! Я бы ни за что не стал добровольно демонстрировать такое творчество своей младшей сестре! Как не вовремя она зашла! "
    "Я молниеносно закрыл программу для рисования и вновь повернулся к Айко."
    
    show Aiko_Base_Outfit_03 Confused_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Похоже, Айко успела разглядеть Мидори."
    "На несколько секунд повисла неловкая пауза, а затем моя сестра пришла в себя и тихо сказала."
    
    show Aiko_Base_Outfit_03 Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Завтрак готов."
    
    show Aiko_Base_Outfit_03 Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Посмотрела на меня, нахмурилась и выпалила."
    
    show Aiko_Base_Outfit_03 Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Только надень на себя хоть что-то!"
    
    show Aiko_Base_Outfit_03 Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Только сейчас я осознал, что сижу на стуле в одних трусах."
    "Пока я разглядывал себя и своё нижнее белье, Айко исчезла."
    
    hide Aiko_Base_Outfit_03 with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Не стоило злить свою сестру и опаздывать. Я встал, накинул рубашку, застегнул её через пуговицу."
    "Натянул брюки и, пытаясь застегнуть тугую ширинку, сделал несколько шагов по комнате."
    
    #СЦЕНА - ДЕНЬ 1, ЗАВТРАК С АЙКО
    
    "Спустился по лестнице и вот я уже в большом холле, который к тому же выполняет роли кухни и столовой."
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    play environment_sounds "./sounds/environment/Kitchen_With_Boiled_Water.mp3" fadein 1

    kenji "И что сегодня на завтрак?"
    
    show Aiko_Base_Outfit_03 Normal_Say with Dissolve( my_dissolve_02 )
    
    aiko "Мисо-суп, рис и омлет."
    
    hide Aiko_Base_Outfit_03 with Dissolve( my_dissolve_02 )
    
    "Я сел за стол, пока Айко протирала его влажной тряпкой. "
    "Потом она поставила на него две деревянные подставки. Протерла и их. "
    "Затем аккуратно расставила передо мной тарелки, положила палочки для еды. Всё в лучшем виде. "
    
    play sound "./sounds/sounds/Plate_On_Table.mp3"
    image Kenji_1st_Day_Breakfast_Food = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/Food.png"
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Даже розовые таблетки — ферменты для пищеварения, которые мне прописали много лет назад — не забыты."
    
    #Мини ЦГ - кухонная плита, на фоне которой стоит Айко
    image Day_Kenji_Home_Kitchen_Gas_Stove = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Gas_Stove.jpg"
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
    
    show Aiko_With_Big_Spoon Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Папа и мама звонили."
    
    show Aiko_With_Big_Spoon Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Меня от этой новости немного передёрнуло — отца я побаивался. "
    "Но последнюю неделю я вёл себя хорошо. Не думаю, что Айко могла на меня наябедничать. "
    "Я ждал, пока Айко скажет что-то еще, но она не стала продолжать. Значит, все нормально!"
    
    hide Aiko_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Довольно странно, что Айко так просто называла моего отца «папой»."
    "Дело в том, что Айко не была его родной дочкой. "
    "Моя мать умерла, когда я был еще совсем маленьким, и все это время меня воспитывал один отец."
    "А шесть лет назад он женился на вдове, Макото Асуке. С тех пор у меня появились сестра и новая мама, хотя я предпочитаю называть её «тётя Асука». "
    "Вскоре после этого отцу предложили новую работу в центре города, и жить в захолустном пригороде ему стало крайне неудобно."
    "Они с тетей перебрались в новую квартиру, оставив прежнее жилье в моем полном распоряжении."

    "Моя новая сестра тоже осталась."
    "Говорила, что не хочет менять школу и расставаться со школьными подружками. Я ожидал, что она уедет после перехода в среднюю школу, но этого не случилось. "
    "Возможно, потому что она не хотела чувствовать себя лишней. Ведь у отца и тёти Асуки появился совместный ребёнок, наш с Айко младший брат. "
    "Впрочем, точной причины я не знал, да и знать не желал. И я бы сам не хотел, чтобы Айко уезжала — от неё много пользы. "
    "Она неплохо готовит, за домом следит. Ей даже не лень выращивать цветы в палисаднике и стричь кусты под окнами. "
    "С другой стороны, чуть что не так, она всегда готова нажаловаться на меня родителям. Приходится быть паинькой."

    "Я потянулся к палочкам для еды, но тут моё внимание привлёк работающий телевизор. "
    "Оттуда раздавалось частое дыхание. "
    
    ##Мини ЦГ - Телевизор с фильмом
    image TV_Strange_Movie_Moved:
        contains:
            "TV_Strange_Movie"
            xpos -700
    
    image TV_Strange_Movie_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image TV_Strange_Movie_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image TV_Strange_Movie_Masked = AlphaMask( "TV_Strange_Movie_Moved", "TV_Strange_Movie_border_01_left_mask_moved" )
    
    image TV_Strange_Movie_With_Border_01:
        contains:
            "TV_Strange_Movie_Masked"
        contains:
            "TV_Strange_Movie_border_01_left_moved"
    ##
    
    show TV_Strange_Movie_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "На экране какой-то тип держал за плечи худенькую девушку в школьной форме. Видимо, он пытался её поцеловать."
    "Та, дрожа, издала жалобный писк."
    
    tv "С-сэмпай!"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Aiko_With_Big_Spoon Confused_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я перевёл взгляд на сестру. Что за дурацкий канал она врубила с утра пораньше? "
    "Айко была сильно смущена и стояла как истукан с крышкой от кастрюли и черпаком в руках."
    
    hide Aiko_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Хвала богам, пульт лежал на столе и через мгновение был у меня в руках."
    "Я перебирал каналы, пока не нашёл что-то наиболее нейтральное. "
    
    ##Мини ЦГ - Телевизор с новостями
    image TV_News_Moved:
        contains:
            "TV_News"
            xpos -700
    
    image TV_News_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image TV_News_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image TV_News_Masked = AlphaMask( "TV_News_Moved", "TV_News_border_01_left_mask_moved" )
    
    image TV_News_With_Border_01:
        contains:
            "TV_News_Masked"
        contains:
            "TV_News_border_01_left_moved"
    ##
    
    show TV_News_With_Border_01 with Dissolve( my_dissolve_05 )
    hide TV_Strange_Movie_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Новости."
    "Выпуск в самом разгаре, обсуждают ближнее зарубежье. Китай, Корея, США. Отлично, самое оно! "
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Я вновь взялся за палочки для еды, но вдруг Айко остановила меня."
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Aiko_With_Big_Spoon Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты не забыл?"
    
    show Aiko_With_Big_Spoon Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Не забыл что?"
    
    show Aiko_With_Big_Spoon Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Сегодня четверг, день вывоза электронных приборов. Мама же просила освободить кладовку!"
    
    hide Aiko_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Черт! Я помнил об этом вчера, но с утра, конечно, позабыл всё на свете."
    "Вот бы еще и Айко забыла! "
    "Барахла в кладовке превеликое множество. Столько работы! Хорошо, если за день управлюсь. "
    "Конечно, никто никуда не спешит. Отец и тётя Асука приедут ещё очень не скоро. Если вообще навестят нас до конца лета. "
    "Поэтому сегодня можно со спокойной совестью отмахнуться от забот, а в следующий четверг поднажать. "
    "Но если вдруг позвонит отец… Не очень хочется слушать его нравоучения. А Айко меня сдаст наверняка."

    "Я отложил палочки для еды в сторону."
    
    kenji "Айко! Ты ещё не налила себе порцию?"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Aiko_With_Big_Spoon Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Что? Нет. Но собираюсь."
    
    show Aiko_With_Big_Spoon Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Возьми мою, я суп не буду!"
    
    show Aiko_With_Big_Spoon Surprised_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Это ещё почему?"
    
    show Aiko_With_Big_Spoon Surprised_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Не то чтобы я внезапно перестал быть голодным. Но мне требовалось оставить место в желудке для кое-чего другого."
    
    kenji "Мне салата хватит! А вместо супа достань-ка мне из холодильника баночку пива! Там же ещё осталось?"
    
    show Aiko_With_Big_Spoon Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Пиво! С утра?!"
    
    show Aiko_With_Big_Spoon Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "А что такого?"
    
    show Aiko_With_Big_Spoon Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Нет, ничего! Суп ты теперь вообще есть не будешь? Может, мне тогда начать варить пиво для тебя?"
    
    show Aiko_With_Big_Spoon Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко была крайне возмущёна."
    
    kenji "Остынь, Айко. Мне надо, понимаешь? Это как лекарство. Я же на улицу пойду. А там люди кругом. Это мне для храбрости!"
    
    hide Aiko_With_Big_Spoon with Dissolve( my_dissolve_01 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Конечно, Айко не понять меня. "
    "Но мне, тридцатилетнему затворнику, проводящему дни и ночи за компьютером, известно, насколько это тяжело — встречать по дороге соседей и знакомых и хриплым голосом желать им доброго дня. "
    "Если я немного выпью, дела пойдут гораздо веселее."

    "Айко с угрюмым видом кинула черпак в кастрюлю и пошла к холодильнику."
    
    #Мини ЦГ - холодильник на фоне которой стоит Айко
    image Day_Kenji_Home_Kitchen_Fridge = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Fridge.jpg"
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
    show Aiko_With_Beer Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    aiko "Ну, какое тебе?"
    
    show Aiko_With_Beer Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Да оно же одинаковое, любое!"
    
    show Aiko_With_Beer Surprised_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    aiko "Ты чего думаешь, я в сортах пива — спец?"
    
    hide Aiko_With_Beer with Dissolve( my_dissolve_02 )
    show Aiko_With_Beer Irritated at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Айко взяла из холодильника одну из банок. Мне показалось, что сейчас она небрежно кинет ее, настолько недовольное было у неё лицо. "
    
    image Kenji_1st_Day_Breakfast_Food_With_Beer = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/Food_With_Beer.png" 
    scene Kenji_1st_Day_Breakfast_Food_With_Beer with Dissolve( my_dissolve_05 )
    
    "Но нет, она поставила пиво на подставку, забрала мою порцию супа и села напротив."
    
    play sound "./sounds/sounds/Opening_Beer_Can.mp3"
    
    "Я взял в руки банку и дёрнул за открывашку. "
    "Затем я схватил розовую таблеточку, запихнул её в рот и запил пивом. "
    "Увидев это, Айко изобразила гримасу неодобрения, но промолчала и принялась за еду. "
    "Я тоже не медлил и торопливо опустошал банку, закусывая салатом. "
    "Есть я старался быстро, но аккуратно, чтобы не испачкать стол и не раздосадовать Айко снова."
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    
    "Когда банка опустела, я почувствовал, что достиг нужной кондиции и двинулся к кладовке."
    "Пора приниматься за дело!"
    
    #СЦЕНА - ДЕНЬ 1, ВЫНОС МУСОРА 
    
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    play environment_sounds "./sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    
    "Всю левую половину кладовки занимал стеллаж, который тётя Асука планировала освободить, чтобы устроить в нем гардероб. "
    "Не знаю, зачем ей это вдруг понадобилось, учитывая, что в доме она вот уже несколько лет не живет."
    "Но спорить с ней не хотелось. Барахлу на этих полках действительно давно место на свалке."

    "А может быть, причина не в этом? Может, тёте Асуке не нужен никакой гардероб, и она просто хочет избавиться от вещей, навевающих неприятные воспоминания? "
    "Дело в том, что всё содержимое стелажа раньше принадлежало её бывшему мужу, Макото Кайоши."

    "Макото-сан умер десять лет назад. А точнее, погиб. Он был радиолюбителем, или как это называется? "
    "Сидел вечерами в радиоэфире и болтал с другими такими же «чокнутыми», как назвала их тётя Асука. "
    "Она вспоминала, что ее муж мог просиживать в своей комнате часами и выбегать с радостными криками, когда ему удавалось принять сигнал совершенно незнакомых людей. "
    "Иногда даже от иностранцев."

    "Как это похоже на меня! Я тоже часами сижу за компьютером. "
    "И если вдруг мне напишет иностранец с предложением нарисовать что-то для него или просто с похвалой моей галереи…"
    "Я наверняка буду, как Макото-сан, бегать и голосить на весь дом о таком успехе."

    "Еще Макото-сан тратил много денег на оборудование. Чего, конечно, не одобряла тётя Асука. "
    "В общем, как это обычно и бывает, жене не особо нравились увлечения мужа. "
    "А вещи, которым он посвящал времени больше, чем ей, радости не вызывали и подавно."
    "Айко, похоже, тоже наплевать на все это отцовское барахло. Она совсем его не помнит. "
    "Ну да, фотографий в альбоме и урны с прахом на местном кладбище ей достаточно. Кому нужна груда металлолома?"
    
    ##ЦГ - Гора телевизоров
    image TV_Heap = "images/cg/DAY_01/03a_Kenji_Moves_Trash/TV_Heap/TV_Heap.png"
    image TV_Heap_Dream:
        contains:
            "TV_Heap"
        contains:
            "Dream_Frame"
    #
    
    play environment_sounds_dream "./sounds/environment/Pantry_Day_Dream.mp3" fadein 1 fadeout 1
    stop environment_sounds fadeout 1
    scene TV_Heap_Dream with Dissolve( my_dissolve_05 )
    
    "Однажды в детстве я проходил с отцом мимо площадки для сбора мусора. Там возвышалась грандиозная пирамида из телевизоров всех форм и размеров."
    "«Дядя Сато помер, телемастер» — пояснил мне отец. "
    "Потом мы с мальчишками устроили настоящую бойню. Расстреляли всю эту кучу камнями, пока не разбили каждый телек вдребезги."
    "Нам, конечно, здорово влетело, а на асфальте в том месте ещё несколько лет поблескивали кристаллики стекла."
    
    play environment_sounds "./sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    stop environment_sounds_dream fadeout 1
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    
    "Тогда мне было весело, а сейчас уже не очень. Умер человек — и вся его жизнь оказалась на свалке. "
    "Чтобы напоследок люди по этим вещам могли определить, кто же «помер» в этот раз. А сегодня выносить чью-то жизнь на помойку предстояло мне."
    
    "О том, как погиб муж тёти Асуки, мне рассказал дядя Ватанабэ, который жил с нами на одной улице. "
    "Он был другом дяди Макото, и в прошлом тоже радиолюбителем."
    
    image Evening_Watanabe_Bike_WorkShop = "./images/bg/Outdoor/Watanabe_Bike_WorkShop/Evening/Watanabe_Bike_WorkShop.png"
    image Evening_Watanabe_Bike_WorkShop_Dream:
        contains:
            "Evening_Watanabe_Bike_WorkShop"
        contains:
            "Dream_Frame"
    
    play environment_sounds_dream "./sounds/environment/Pantry_Day_Dream.mp3" fadein 1 fadeout 1
    stop environment_sounds fadeout 1
    scene Evening_Watanabe_Bike_WorkShop_Dream with Dissolve( my_dissolve_05 )
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Он хотел сделать антенну. Из провода высоковольтной линии, что проходит в саду."

    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "В саду, прямо за нашим домом, действительно стояла опора ЛЭП. Высокая, метров пятнадцать, не меньше."
    kenji "Он упал с нее?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Да нет. Прихлопнуло его, когда свою антенну на фазу забрасывал."
    watanabe "Если бы упал, тогда выжил бы, наверное. А так... Руки у него до костей обгорели."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Я не поверил. Подсоединить свою антенну к проводу под большим напряжением — это дикость! "

    kenji "Это больше похоже на самоубийство!"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да ты что! Там всего тридцать пять тысяч вольт, это немного."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Немного?! Мне эта цифра показалась неправдоподобно большой. «Всего» тридцать пять тысяч вольт! "
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Если бы у меня была такая возможность, я бы тоже набросил. А Кайоши не рассчитал чего-то."
    watanabe "Может, конденсаторы плохие ему попались, или ещё чего..."
    watanabe "Ты не подумай, Кендзи. Мы не сумасшедшие и не самоубийцы. Хотя, конечно, авантюра очень рискованная."
    watanabe "Меня тоже один раз шандарахнуло, но, слава богу, выжил."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Тоже «набросили»?"
    
    hide Watanabe_01 with Dissolve( my_dissolve_01 )
    show Watanabe_02 Normal_Silent with Dissolve( my_dissolve_01 )

    "Дядя Ватанабэ улыбнулся."
    
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Да нет! На работе. Я же электрик по призванию. Но там ничего интересного, совершенно бытовая ситуация"
    watanabe "С тех пор пальцы на правой руке еле двигаются. И вообще, что-то вроде контузии получил. "
    watanabe "Полгода ходил как пришибленный. Инвалидом стал и вышел досрочно на пенсию."
    watanabe "Приходится подрабатывать автомехаником теперь. "
    watanabe "Эх, и как он только умудрился сжечь сцепление? А, Кендзи? Ты не знаешь?"
    
    play environment_sounds "./sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    stop environment_sounds_dream fadeout 1
    scene Day_Kenji_Home_Pantry_01 with Dissolve( my_dissolve_05 )
    
    "Я тряхнул головой, отгоняя воспоминания. "
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
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 2 fadeout 1
    scene Outdoor_Day_Kenji_Home with Dissolve( my_dissolve_05 )
    
    "На улице был типичный июньский полдень. Ужасно яркое солнце, голубое небо и белоснежные облака. Всё как обычно. "
    "Дождей за последнюю неделю не наблюдалось, и к зною добавился стойкий запах пыли, который перебивал теперь аромат цветов и прочей зелени. "
    "Людей на улице не было — это радовало, мне ни к чему лишние свидетели."
    
    "Я вышел за ограду и принялся за упражнения со своим новеньким, жёлтеньким и увесистым снарядом. "
    "Поставил его ребром на плечо — острый край пребольно врезался в шею. "
    "Попробовал нести его под мышкой — и тут не вышло, рука моментально вспотела и «чемоданчик» норовил выскользнуть."
    "Я схватил его обеими руками и понёс, прижимая к груди, но и так было не очень сподручно. "
    
    scene Outdoor_Day_Street_03 with Dissolve( my_dissolve_05 )
    
    "Пройдя один квартал, я сменил тактику и решил взять свой снаряд за его родные, заводские ручки, покрытые каким-то плотным зелёным материалом. "
    "Постепенно стали ныть плечи и спина, а ещё зудеть нога в том месте, где она тёрлась о край прибора."
    
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    play sound "./sounds/sounds/Metal_Item_Drag_And_Fall.mp3"
    
    "Последние несколько метров я буквально волочил «чемоданчик» по асфальту, оставляя блестящий след с чешуйками жёлтой краски. "
    "Похоже, я сегодня был первым посетителем. Никакой электроники до меня никто не выбросил. Площадка для мусора была пуста"
    
    #Мини ЦГ - рация на асфальте
    image Radio_Set_On_Ground_Closed = "./images/cg/DAY_01/03a_Kenji_Moves_Trash/Radio_Set_On_Ground_Closed/Radio_Set_On_Ground_Closed.png"
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
    "На обратном пути я вновь никто не встретил. Довольно удачный выдался денёк! "
    
    play environment_sounds "./sounds/environment/Kitchen.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    
    "Я ворвался в дом, распахнул холодильник и сразу же выпил холодного пива. Ох, похоже, полбанки выдул за несколько глотков! "
    
    show Aiko_School_Uniform_01 Angry_Silent with Dissolve( my_dissolve_02 )
    
    "Айко была на кухне. Она нахмурилась, глядя на меня, но ничего не сказала. "
    "Я же улыбнулся во весь рот и продемонстрировал сестре оттопыренный вверх большой палец. "
    
    show Aiko_School_Uniform_01 Shy_Silent with Dissolve( my_dissolve_02 )
    
    "От моего жеста она почему-то смутилась, а я только теперь заметил, что на ней надета летняя школьная форма."
    
    kenji "Ты что, в школу собралась? Разве сейчас не каникулы?"
    
    hide Aiko_School_Uniform_01 Shy_Silent with Dissolve( my_dissolve_01 )
    show Aiko_School_Uniform_02 Normal_Say with Dissolve( my_dissolve_01 )
    
    aiko "Каникулы! Но я иду в школьный бассейн."
    
    show Aiko_School_Uniform_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Бассейн! Я вспомнил о том, что на земле существуют такие замечательные места. Ах! Я бы сейчас с удовольствием окунулся в прохладную водичку. "
    "И плевать, что там народу как сельдей в бочке. Настроение у меня теперь самое располагающее, никакой невроз от тесного общения с людьми не страшен. "
    "Правда, в таком состоянии в общественный бассейн меня не пустят. Я вздохнул и отглотнул еще пива."
    
    show Aiko_School_Uniform_02 Normal_Say with Dissolve( my_dissolve_02 )
    
    aiko "Чего вздыхаешь?"
    
    show Aiko_School_Uniform_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Разве не понятно? В такую то жару в бассейне поплавать в самый раз!"
    
    show Aiko_School_Uniform_02 Surprised_Say with Dissolve( my_dissolve_02 )
    
    aiko "В нашем школьном?"
    
    show Aiko_School_Uniform_02 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да какая разница. Но сама понимаешь, народу там — тьма."
    
    show Aiko_School_Uniform_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Айко пожала плечами и стала чуть серьёзнее. Она знала, чего я боюсь."
    
    show Aiko_School_Uniform_02 Normal_Say with Dissolve( my_dissolve_02 )

    aiko "Можешь съездить к морю. Где-то да найдёшь пустынный пляж."
    
    show Aiko_School_Uniform_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "К морю... да... Но тогда придётся трястись в поезде час или два. В переполненном поезде, Айко!"
    
    show Aiko_School_Uniform_02 Mocking_Silent with Dissolve( my_dissolve_02 )
    
    "На лице Айко появилась ухмылка."
    
    show Aiko_School_Uniform_02 Mocking_Say with Dissolve( my_dissolve_02 )
    
    aiko "Ты же принял «лекарство»."
    
    show Aiko_School_Uniform_02 Mocking_Silent with Dissolve( my_dissolve_02 )
    
    kenji "С этим лекарством, сама понимаешь, в воду лезть не стоит. Тем более в одиночку."
    
    #hide Aiko_School_Uniform_02 with Dissolve( my_dissolve_01 )
    show Aiko_School_Uniform_02 Normal_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко опять пожала плечами и направилась к выходу. Дескать, это не её проблемы."
    
    kenji "Постой, Айко! А может быть, завтра вместе съездим на море и там найдём этот самый пустынный пляж? Я не могу один — вдруг я начну тонуть?"
    
    show Aiko_School_Uniform_02 Surprised_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Думаешь, я тебя спасу?"
    
    show Aiko_School_Uniform_02 Surprised_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ты же член плавательного кружка!"
    
    hide Aiko_School_Uniform_02 with Dissolve( my_dissolve_01 )
    show Aiko_School_Uniform_01 Angry_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А ты опять напьёшься?"
    
    show Aiko_School_Uniform_01 Angry_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что значит «опять»? Это же не ради удовольствия, Айко!"
    
    show Aiko_School_Uniform_01 Angry_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "В таком случае даже не мечтай!"
    
    show Aiko_School_Uniform_01 Angry_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ну… Айко! Я встану на колени перед тобой, хочешь?"
    
    hide Aiko_School_Uniform_01 with Dissolve( my_dissolve_01 )
    show Aiko_School_Uniform_02 Scared_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "По лицу Айко пробежала гримаса испуга и отвращения."
    
    show Aiko_School_Uniform_02 Scared_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "НЕТ!"
    aiko "То есть да. Уговорил! Завтра поедем, но только без этого!"
    
    play sound "./sounds/sounds/Aiko_Run_Away_From_Kitchen.mp3"
    hide Aiko_School_Uniform_02 with vpunch
    
    "Айко в мгновение ока изчезла, скрывшись за дверью в прихожую."
    "Как же мне повезло с сестрёнкой! Мысль о предстоящем отдыхе приободрила меня, и я с энтузиазмом вернулся к работе."
    
    play environment_sounds "./sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Pantry_02 with Dissolve( my_dissolve_05 )
    show Day_Kenji_Home_Pantry_Blink_03_Animated with Dissolve( my_dissolve_02 )
    
    "В следующий свой поход я решил не брать тяжелого собрата желтого чемоданчика. Я оставил его на потом."
    "Вместо него я взял моток провода, который лежал на верхней полке."
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 2 fadeout 2
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    #Мини-ЦГ вентилятор Касуми 01
    image Kasumi_Fan_01 = "./images/cg/DAY_01/03a_Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_01.png"
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
    "Не знаю, зачем это кому-то понадобилось, но крышка на нем была вскрыта. "
    
    hide Kasumi_Fan_01_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Под ней оказалась сложная приборная панель — десятки всевозможных крутилок, тумблеров, циферблатов со стрелками и хитрых разъёмов. "
    "Может быть, крышка спала сама? Прибор нагрелся под солнцем и она слетела?"
    "Я потрогал его. Да, горячий."
    "Но, должно быть, кому-то просто стало интересно, что же такое я сюда притащил. "
    "Хм... Возможно, этот кто-то — владелец сломанного вентилятора. Я подошёл поближе. "
    
    #Мини-ЦГ вентилятор Касуми 02
    image Kasumi_Fan_02 = "./images/cg/DAY_01/03a_Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_02.png"
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
    "Да и весь этот жёлтый налёт на нем… явно сигаретная копоть, налипшая за годы эксплуатации. "
    "Стало немного противно, и в то же время в памяти всколыхнулись воспоминания былых лет."
    
    image smocking_old_man = "./images/cg/DAY_01/03a_Kenji_Moves_Trash/Old_Smocking_Man/smocking_old_man.png"
    image smocking_old_man_dream:
        contains:
            "smocking_old_man"
        contains:
            "Dream_Frame"
    
    
    play environment_sounds_dream "./sounds/environment/City_Suburb_Day_Dream.mp3" fadein 1
    stop environment_sounds fadeout 2
    scene smocking_old_man_dream with Dissolve( my_dissolve_05 )
    
    "Я вспомнил своего давно умершего деда, который всю жизнь смолил какие-то американские сигареты. "
    "Весь его дом и каждая вещь в нем накрепко пропитались застарелым запахом сигаретного дыма."
    "Столь активные курильщики наверняка болеют какими-то заболеваниями. "
    "Например, туберкулёзом — неприятной и очень заразной болезнью, я слышал о такой. "
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 2
    stop environment_sounds_dream fadeout 2
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Я отшагнул подальше от вентилятора и посмотрел на свою левую ладонь."
    "Я только что прикасался к прибору, который принес ранее. А до меня его, похоже, трогал кто-то чужой. "
    "Вот будет весело, если такой домосед, как я, подцепит редкую и смертельную болезнь! А точнее — совсем не весело!"
    "Я поспешил домой. Надо скорее вымыть руки!"
    
    play environment_sounds "./sounds/environment/Pantry_Day.mp3" fadein 1 fadeout 1
    scene Day_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    show Day_Kenji_Home_Pantry_Blink_04_Animated with Dissolve( my_dissolve_02 )
    
    "В свой третий поход до мусорки я взял два стареньких радиоприёмника. Они были довольно громоздкие, но в то же время совсем не тяжёлые."
    
    scene Day_Kenji_Home_Pantry_Other_04 with Dissolve( my_dissolve_05 )

    kenji "Остальное, думаю, можно оставить и на потом."
    kenji "За день сделано достаточно! Пожалуй, еще одну вещь и довольно."
    
    "Я решил во что бы то ни стало вынести сегодня тяжёлого собрата жёлтого чемоданчика. "
    "А между тем вторая банка пива подошла к концу. Я сходил на кухню и взял новую. Открывать её не стал — положил в карман брюк. "
    "В последнем и трудном походе мне понадобятся обе руки!"
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 2 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Поход был действительно трудный! "
    "Когда я наконец дотащил свою ношу до места, у меня ужасно ныли плечи и спина, тряслись руки и не разгибались пальцы. "
    
    
    #Мини ЦГ - БП от рации на земле
    image Radio_Set_Power_Supply_On_ground = "./images/cg/DAY_01/03a_Kenji_Moves_Trash/Radio_Set_Power_supply_On_Ground/Radio_Set_Power_Supply_On_ground.png"
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
    "Видимо, при работе прибор грелся, и такая конструкция была нужна для охлаждения. Ребра теперь были все погнуты, особенно те, что по краям. "
    "В просветы между ними забилась трава, земля и частички асфальта. Один из циферблатов на передней панели треснул. "
    
    hide Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Но мне, конечно, было наплевать. Не на выставку же нёс, в самом деле!"
    
    "Ну вот и всё, пришло время передохнуть!"
    "Я окинул взглядом вещи, которые принес, и оценил их вес. Да я просто герой!"
    "Эх, жалко я Айко не показал, какая эта жёлтая зараза тяжёлая. Она бы мной гордилась! "
    "Пожалела бы меня и позабыла бы про свои придирки как минимум на месяц! И почему я такой недогадливый!"
    
    play sound "/sounds/sounds/Open_Beer_Can_Loud.mp3"
    
    "С этими мыслями я открыл пиво, которое дожидалось в кармане брюк. "
    "Да уж, взболтал я содержимое банки здорово — пена полезла наружу, липкие струйки потекли по пальцам. "
    "Я тихо ругнулся, сдул пену, вытер руку о штаны и поставил ногу на тот прибор, что принёс раньше остальных — как на поверженного врага. "
    "Сделал глубокий глоток и огляделся по сторонам. Я был не один."
    
    #Мини ЦГ - Касуми идет с тележкой
    image Kasumi_Walks = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Walks/Kasumi_Walks.png"
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
    
    "Мне навстречу шла девушка. Она катила перед собой маленькую тележку для вещей. "
    "Тележка была пуста. "
    "Зачем она это делала, было непонятно, да и способ перемещения тележки странный — гораздо проще везти ее за собой."
    "А такую маленькую вообще лучше было бы сложить, взять под мышку и идти так. "
    "Внезапно девушка остановилась, отвернулась от дороги и замерла."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_01 )
    
    #Мини ЦГ - Касуми стоит с тележкой
    image Kasumi_And_Interesting_Wall = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_And_Interesting_Wall/Kasumi_And_Interesting_Wall.png"
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
    
    "Не меньше минуты она стояла перед каменной кладкой, словно рассматривала интереснейшую картину."
    "Я между тем терялся в догадках, чего же такого интересного она там увидела."
    "Я не приметил ничего необычного, когда проходил это место."
    "Может быть, девчонке этой надо на площадку для мусора? А я её стесняю, и поэтому она так внезапно принялась изучать эту стену?"
    
    hide Kasumi_And_Interesting_Wall_With_Border_01 with Dissolve( my_dissolve_01 )
    show Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Как только я подумал об этом, школьница отвернулась от стены и продолжила свой путь в мою сторону. "
    "Обычно я в таких случаях перехожу на другую сторону улицы или вообще стараюсь побыстрее скрыться с глаз встречного прохожего. "
    "Но в этот раз повышенная концентрация «лекарства» позволила мне и дальше с любопытством наблюдать за незнакомкой."
    "Привычный страх перед людьми на время понлостью оставил меня."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Девушка наконец достигла площадки для сбора мусора. И оказалась метрах в пяти от меня!"
    "Она остановилась и отвесила мне учтивый поклон. Я бы даже сказал, чересчур учтивый!"
    
    #Мини ЦГ - Касуми стоит на четвереньках
    image On_All_Fours = "./images/cg/DAY_01/04a_Trash_Place_Meeting/On_All_Fours/On_All_Fours.png"
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
    
    "Ее ладони коснулись асфальта, и она встала на четвереньки. "
    "Если честно, мне захотелось воскликнуть от удивления, но я продолжил стоять как вкопанный, только глаза мои опускались все ниже. "
    "Её руки замелькали по асфальту."
    
    hide On_All_Fours_With_Border_01 with Dissolve( my_dissolve_01 )
    
    #Мини ЦГ - Руки Касуми на штанине Кендзи
    image Kasumi_Hands_On_Kenji_Leg = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Hands_On_Kenji_Leg/Kasumi_Hands_On_Kenji_Leg.png"
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
    play sound "./sounds/sounds/Body_Fall_On_Ground.mp3"
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
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Простите! Я не заметила вас!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не заметила?!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Да, я ничего не вижу."
    
    #Мини-ЦГ лицо Касуми крупным планом
    image DAY_01_Kasumi_Big_Face = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi/Kasumi.png"
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
    
    hide kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    show kasumi_01 Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show DAY_01_Kasumi_Big_Face_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Я взглянул на лицо девушки, и у меня по спине пробежал холодок."
    "Солнце ярко высвечивало её лицо и искрилось на прядях волос. "
    "Но наперекор светилу, зрачки её были так широки, что по тонким радужкам невозможно было определить даже цвет глаз. "
    "Этот контраст расширенных, как у кошки в ночи, зрачков и яркого солнца, бьющего прямо в глаза, напугал меня. "
    "Девушка была слепой."
    
    hide DAY_01_Kasumi_Big_Face_With_Border_01 with Dissolve( my_dissolve_02 )
    hide kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Извини…"

    "Хрипло прошептал я. "
    "Я кашлянул и повторил снова, уже в полный голос."

    kenji "Извини!"
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Девушка встревожилась."
    
    show kasumi_01 Concerned_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Что? Почему? За что?"
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну… Я… Не думал, что ты…"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Всё нормально! Хорошо, что я не налетела на вас."
    blind_girl "Вас совсем не было слышно и я думала, что тут никого нет."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Наверное, слепые люди полагаются на слух. Нет, вовсе не наверное, а даже точно. На что же ещё? Может, на обоняние? "
    "Тут мне словно врубили нужную часть мозга, и я почувствовал, что от девушки сильно несёт сигаретами. "
    "Она что, курит, и курит настолько много?!"
    
    "Но, несмотря на запах, девушка не походила на заядлого курильщика."
    "В руках у нее не было ни зажигалки, ни спичек, ни сигарет."
    "Мой взгляд пробежался по фигуре девушки, и я подметил, что форма её порядком поношенная и выцветшая."
    "А загар на руках и шее незнакомки точно повторял контуры вырезов одежды."
    "Видимо, школьная форма этим летом была её повседневной одеждой."

    "Лицо её мне показалось приятным. Давно я так близко не разглядывал старшеклассниц."
    "Но всё впечатление портил этот пустой взгляд, в котором, казалось, навечно застыл испуг."
    
    #Мини-ЦГ ус Касуми крупным планом
    image DAY_01_Kasumi_Big_Face_Mustache = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi/Kasumi.png"
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
    "С этим аксессуаром голова девушки напоминала голову муравья или инопланетянина из старых черно-белых фильмов."
    "И зачем ей эти «усы»?"
    
    hide DAY_01_Kasumi_Big_Face_Mustache_With_Border_01 with Dissolve( my_dissolve_02 )

    "Всё в этой девушке было странным. Её пугающие, невидящие глаза и этот непонятный ободок на голове."
    "И стойкий запах сигаретного дыма."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Получается, эта рация ваша?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Спросила девушка, и её ладонь указала в сторону моих ног."
    
    show Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_05 )
    
    kenji "Так это рация?"
    
    "Я удивился. При слове «рация» мне представлялось маленькое, величиной с мобильный телефон, устройство. "
    "А такая громадина, и тоже — рация. Ну надо же!"
    
    hide Radio_Set_On_Ground_With_Border_01 with Dissolve( my_dissolve_01 )
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Ну да. Военная рация, очень хорошая, американская, мощная. В конце шестидесятых годов выпускалась. Ещё на германиевых транзисторах!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Германиевых? Значит ли это, что транзисторы были из Германии? Какое странное словосочетание. "
    "Интересно, а «япониевый» транзистор есть?"

    kenji "Рация не совсем моя. Одного родственника"
    kenji "Я просто его вещи на свалку выношу. Он, видимо, радио увлекался, или что-то в этом роде."
    kenji "Сам я в этих делах ничего не смыслю."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А..."
    blind_girl "Увлекался?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну да. Умер он. Но очень давно. А сейчас понадобилось расчистить немного места в доме. Вот и выбрасываем, и рацию эту тоже."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А... А я думала, вы наоборот. Пришли сюда за ней."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Теперь я понял, зачем девушке нужна была тележка. И почему была вскрыта крышка на «рации». "
    "Похоже, вещь эта её заинтересовала, и она собралась забрать её себе."
    
    kenji "Нет! Мне этот хлам нафиг не сдался. Если хочешь забрать — бери, конечно."
    kenji "Только как же ты её унесёшь? Думаешь, сможешь? Она страшно тяжёлая!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Все вещи тех лет такие громоздкие. А эта ещё и военная, там всё внутри с многократным запасом прочности!"
    
    hide kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
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
    
    play sound "./sounds/sounds/S/ubmarine_Creaking.mp3"
    show Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Послышался скрежет металла об асфальт, прибор поднялся… Но совсем чуть-чуть, сантиметров на пять. "
    "Моя случайная знакомая тянула лямку прибора изо всех сил, но такая тяжесть была ей не по зубам."
    
    kenji "Давай я помогу!"

    "Сказал я, встал с другой стороны и взял прибор за вторую ручку. "
    
    stop sound fadeout 0.5
    hide Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( my_dissolve_01 )
    play sound "./sounds/sounds/Metal_Item_Fall.mp3"
    show empty_image with vpunch #Трясем экран 
    
    "Но в тот же момент руки девушки разжались, и прибор глухо хлопнулся на землю. "
    
    show kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "А девушка, задыхаясь, выпалила."
    
    show kasumi_01 Surprised_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "И вправду, очень тяжёлый!"
    
    show kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )

    "Я вспомнил о банке пива в руке и отглотнул немного. А после сказал."

    kenji "Давай я помогу погрузить эту штуковину на тележку. Похоже, тебе её не поднять."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Она кивнула."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Если… Если вам не трудно…"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    #Мини ЦГ - тележка Касуми (пустая)
    image Kasumi_Cart = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Cart/Kasumi_Cart.png"
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
    image Kasumi_Cart_And_Radio_Set = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Cart_And_Radio_Set/Kasumi_Cart_And_Radio_Set.png"
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
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Спасибо! Большое вам спасибо за помощь!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Похоже, это она так прощалась со мной. Действительно, чем мог, я помог. Больше говорить было не о чем. "
    "И тут какая-то дурацкая грусть окутала мое охмелевшее сознание. "
    "Грустно оттого, что девушка уходит, и я её, наверное, больше никогда не увижу."
    
    "И… так жалко её. Неужели она действительно справится с этой тяжёлой ношей одна? Доберётся ли в целости до дома? А вдруг что-то случится в пути?"
    "Хотелось проводить ее, побыть ещё рядом. Да и хорошенькая она на вид. И вообще, я бы сказал, что она мне понравилась. "
    "Хотя, говорят, что когда здорово выпил, любой крокодил за красавицу сойдёт."
    "А выпил я сегодня действительно здорово, да и жара приморила изрядно."

    "Надо остановить её! Сказать что-то! Но что? "
    "Я осмотрелся, взгляд упал на остальные принесённые мной вещи."
    
    kenji "Постой! А эта рация… Она не из двух частей состоит?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Двух частей?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну да. Тут ещё что-то. Похоже, дополнение к ней. Цвет и габариты — всё такое же."
    kenji "Я вынес это в последнюю очередь. Посмотри сама..."
    
    "Я прикусил язык. Чёрт! Зачем я это сказал, вот ведь идиот! Но девушка не повела и ухом."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А как? Как оно выглядит? Точь-в-точь как эта? Может, просто ещё одна?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не думаю..."
    
    show Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_02 )

    "Я описал ей всё в подробностях. "
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А! Это блок питания для рации."
    blind_girl "Обычно она работала от аккумулятора. Ну, от танкового или ещё какого."
    blind_girl "А этот блок питания нужен для того, чтобы питать её от сети. Дома, от розетки, например."
    
    hide Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( my_dissolve_02 )
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Значит, он тебе тоже нужен?"
    
    "Её последние слова меня воодушевили. Но когда я услышал ответ, то все мои надежды мигом рухнули."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Нет! У меня есть. Дома. Правда не такой, обычный, но мощный!"
    blind_girl "Можно напряжение любое выставить. Он подойдёт."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А... Ну ладно."
    
    hide kasumi_01 with Dissolve( my_dissolve_02 )

    "Я был раздосадован. Ничего не вышло. Девушка поклонилась мне на прощание, я молча поклонился в ответ. "
    "Конечно, она этого не видела и надо было попрощаться словами. Но черт с ней! "
    "Я внезапно разозлился. Пусть чешет своей дорогой! Надо было и вовсе смыться домой ещё когда только заприметил её вдалеке."

    "Я залпом допил оставшееся пиво. Смял банку и кинул в контейнер для металлической тары. "
    "Хоть я и был пьян — но банка прилетела точно в цель!"
    
    #ЦГ - взрыв тележки Касуми
    image Kasumi_BOOM = "./images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/Kasumi_Boom.png"
    image Kasumi_BOOM_animation_frame_00 = "./images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_00.png"
    image Kasumi_BOOM_animation_frame_01 = "./images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_01.png"
    image Kasumi_BOOM_animation_frame_02 = "./images/cg/DAY_01/04a_Trash_Place_Meeting/BOOM/frame_02.png"
    
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
    play sound "./sounds/sounds/TNT.mp3"
    stop environment_sounds fadeout 1
    play environment_sounds_dream "./sounds/environment/City_Suburb_Day_Dream.mp3" fadein 2 fadeout 1
    
    "Ба-бах!"
    blind_girl "Ай!"
    
    show Kasumi_BOOM with Dissolve(0.2)
    hide Kasumi_BOOM_animation
    
    "Я обернулся. Похоже эта школьница наехала тележкой на мину!" 
    "Нет, конечно, это была полнейшая глупость, никакой мины тут быть не должно. "
    "Однако тележка сильно кренилась на левый бок, а одно из её колес, кружилось волчком в стороне. Всё-таки не была она рассчитана на такой вес."
    
    stop environment_sounds_dream fadeout 10
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 10 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Я был несказанно рад такому повороту событий и немедленно поспешил к месту аварии."
    
    #Мини ЦГ - тележка и рация, валяются
    image Radio_Set_And_Cart_On_The_Ground = "./images/cg/DAY_01/04a_Trash_Place_Meeting/Radio_Set_And_Cart_On_The_Ground/Radio_Set_And_Cart_On_The_Ground.png"
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
    show kasumi_01 Surprised_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Вид у девушки был совершенно растерянный. Её тележка валялась в стороне, и судя по всему пришла в полную негодность"
    
    show kasumi_01 Surprised_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    blind_girl "Что с моей тележкой?"
    
    show kasumi_01 Surprised_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "С тревогой в голосе спросила она."
    "Я глянул на то место, где раньше располагались колеса. Там остались только чёрные втулки с обломанными спицами."
    
    kenji "Кранты ей похоже."
    
    hide Radio_Set_And_Cart_On_The_Ground_With_Border_01 with Dissolve( my_dissolve_02 )
    hide kasumi_01 Surprised_Silent wit Dissolve( my_dissolve_01 )
    show kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Я стащил рацию и подал тележку девушке."
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Она немедленно принялась изучать тележку, пытаясь определить ее состояние. "
    "Мне почему-то стало смешно от выражения её лица, когда она наконец нащупала места крепления колес. "
    "Пришлось проглотить идиотский смешок, который чуть было не вырвался наружу."

    kenji "Что теперь делать будешь?"
    
    show kasumi_01 Concerned_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "Не знаю..."
    blind_girl "Эта тележка тёти. Я обещала что верну в целости."
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    "Она вздохнула."

    "Неужели тётка будет отчитывать эту несчастную слепую девчонку из-за какой-то тележки? "
    "Вполне возможно она добрая женщина, и её племяннице просто стыдно что она угробила не свою вещь."
    "Но, в моей голове родился образ омерзительной старой карги, которая по возвращению, ухватит мою случайную знакомую за волосы и потащит по улице, крича о жутком преступлении, которое та совершила."

    "Какие идиотские мысли. Похоже доза пива, выпитая залпом, ударила таки мне в голову. "
    "Злость испытываемая ранее, внезапно улетучилась и подступила непонятная эйфория. Я посмотрел на девушку, и задал неожиданный вопрос."

    kenji "А как тебя зовут?"
    
    show kasumi_01 Surprised_Say with Dissolve( my_dissolve_02 )
    
    blind_girl "А? Меня..."
    
    show kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Девушка сильно заволновалась. Похоже вопрос и в самом деле неожиданный. Но мне было плевать."

    kenji "Кендзи. Танака Кендзи!"

    "Сказал я и театрально ткнул себя пальцем в грудь."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    blind_girl "Накамура... Касуми."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Кротко ответила девушка. Свою, бесполезную теперь, тележку она всё ещё не выпускала из рук."

    kenji "Сколько тебе лет?"

    "Вот это да! Я даже удивился собственной дерзости!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Шесть... Шестнадцать!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Отлично. Накамура Касуми, шестнадцать лет! Язык развязался и я не в силах удержать внезапную словоохотливость задвинул впечатляющую речь: "
    
    kenji "Послушай Касуми, я знаю, людям с твоими, эм... проблемами неприятно слышать такое, но вид у тебя совершенно потерянный."
    kenji "Ты уж извини! Я понимаю, что тебе хочется казаться сильной и независимой. И показать всем что ты прекрасно обходишься, ну... ты меня поняла."
    kenji "Но вся эта чехарда с никчемной тележкой, у меня вызывает только жалость."
    kenji "Давай-ка я сам возьму в руки эту несчастную рацию и отнесу туда, куда тебе нужно."
    kenji "А ты выбрось эту тележку на свалку. Это теперь больше похоже на ходунки для стариков. Тёте твоей, нужны ходунки, Касуми?"
    
    hide kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    show Kasumi_03 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Касуми смотрела куда-то всторону и молчала. "

    kenji "Или может мне лучше и вовсе унести эту рацию домой? Обратно к себе."
    kenji "Чего это я так разбрасываюсь вещами. А, Касуми? За сколько это барахло можно толкнуть на барахолке?"
    
    hide Kasumi_03 Normal_Silent with Dissolve( my_dissolve_02 )
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Нет! Простите, Танака-сан! Но мне очень нужна эта вещь."
    kasumi "Пожалуйста! Помогите мне донести её до дома!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я был рад этим словам, но кажется она догадалась, что я напрашивался в попутчики."
    "Впрочем мне уже было все равно. "
    "Я подозревал, что веду себя очень странно, и наверное, в такой ситуации, правильнее было бы вызвать такси для бедной девочки, и избавить ее от своего присутствия."
    "Но мне жутко не хотелось с ней расставаться."

    "Я поднял рацию за её родные ручки."

    kenji "Эй, Касуми? Ты где живёшь?"
    
    "Касуми назвала свой адрес. Это было далеко отсюда, дальше раз в пять чем до моего дома."

    kenji "Э? Так далеко? Почему ты выносишь мусор именно сюда? У вас что там, своего места для хлама нет, поблизости?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Есть. Совсем недалеко."
    kasumi "Но надо идти через канал, а весной, пешеходный мост подмыло после сильного дождя."
    kasumi "Ремонт затянулся и теперь там не пройти. "
    kasumi "Недалеко есть автомобильная дамба. Но я не хожу там. Очень шумно - мне трудно ориентироваться."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Ну надо же! А ведь я тоже некомфортно себя чувствую в шумных местах! И наверняка Касуми не любит большие скопления людей. "
    "Ну прямо как я! Или вообще людей не жалует... "
    "Особенно навязчивых алкашей!"
    "От этой мысли я чуть приуныл."

    kenji "Ну что, идём? Да брось ты свою тележку! Хана ей!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет. Я попробую её починить! Колеса от неё, они где?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Я недовольно проворчал."

    kenji "Ну одно колесо, оно вроде как здесь лежит. А второго нет."
    
    show kasumi_01 Concerned_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет?"
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да, улетело, и теперь его нет. Хочешь пойти поискать?"
    

    "Я опять говорил с ней неприлично резким тоном. Услышав мои слова, Касуми тихо вздохнула."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Нет. Если улетело, то пусть. Но я всё равно возьму тележку с собой. Ладно?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Это ещё что за вопрос? Делай со своей тележкой что хочешь."
    
    scene Outdoor_Day_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )

    "Мы двинулись, я пристроился справа, встав между моей новой знакомой и обочиной дороги."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Простите Танака-сан... Но... не могли бы вы встать с другой стороны от меня?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Я удивленно промычал."

    kenji "Ммм?"

    "Касуми подняла правую руку и указала на свое ухо."
    
    ##Мини ЦГ - Касуми в профиль
    image Kasumi_Profile = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Profile/Kasumi_Profile.png"
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
    
    hide kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    show kasumi_01 Normal_Silent at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Kasumi_Profile_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Я увидел что в него вставлен белый наушник."
    
    show kasumi_01 Normal_Say at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    kasumi "Я вас плохо буду слышать. Лучше встаньте слева."
    
    show kasumi_01 Normal_Silent at Move( ( 1200, 600 ), ( 1200, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Я уж было подумал что Касуми ещё и глухая, а в ухе у неё не что иное, как слуховой аппарат. "
    "Но нет, она же говорит встать с другой стороны!"
    
    hide Kasumi_Profile_With_Border_01 with Dissolve( my_dissolve_02 )
    hide kasumi_01 with Dissolve( my_dissolve_02 )
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "В левом ухе никаких наушников не было. Я стал разглядывать мою новую знакомую в профиль. "
    "Так, не было видно её необычных глаз и казалось со мной рядом шла совершенно обычная девчонка."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Вы смотрите на моё ухо, Танака-сан?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Вдруг спросила Касуми"

    kenji "Я? Нет! Зачем мне это нужно?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Говорят, можно чувствовать кожей взгляды людей. Я подумала, почему-то что вы смотрите именно туда."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Неправильно подумала!"
    
    "Пробурчал  я, и решил сменить тему."

    kenji "Чего это ты слушаешь в наушнике? Радио?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Нет."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Касуми подняла руку и коснулась своего ободка с «усами»."

    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Это."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А что это такое?"

    "Мне было и правда интересно."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Это что-то вроде ёмкостного реле."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Черт! Мне бы лучше подошёл ответ уровня - «это устройство для связи с внеземными цивилизациями»."
    "Что такое «ёмкостное реле» я даже представить себе не мог. Звучало как термин из учебника физики. "
    "Но не припомню чтобы школьный или институтский преподаватель физики щеголял на уроке с этим ёмкостным реле на голове. "
     
    #ЦГ - Портреты Ньютона и Галилео
    image Scientists = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Scientists/Scientists.png"
    image Galileo_And_Newton:
        contains:
            "Scientists"
        contains:
            "Dream_Frame"
    ##
    
    play environment_sounds_dream "./sounds/environment/City_Suburb_Day_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    show Galileo_And_Newton with Dissolve( my_dissolve_05 )
    
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
    
    "Даже такие интересные личности как Эдисон и Тесла — ни разу это самое «реле» не одели. Удивительно!"
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    hide Edison_And_Tesla with Dissolve( my_dissolve_05 )
    
    kenji "А зачем оно? Для чего?"

    "Спросил я. И мне подумалось, следующий ответ будет ещё непонятнее. "
    "Что-нибудь вроде «чтобы измерять угловой коэффициент пролетающих мимо нейтрино» или что-то в таком духе."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Оно реагирует на предметы. Чтобы было проще ориентироваться в пространстве."
    kasumi "Когда рядом с антеннами что-то есть, в наушнике пищит."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Хм... Здорово придумано, сама сделала?"

    "Касуми покачала головой."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Не совсем. Мне помогли собрать."
    kasumi "Но вообще, он не очень точный, в сухую погоду ещё неплохо работает. А в сырую или в туман — с ума сходит."
    kasumi "Пищит по любому поводу. Приходится отключать его. Но тогда он тоже помогает, как усы у кошки."
    kasumi "Хотя — в плохую погоду, на улицу я и не выхожу."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Интересно, кто помогал Касуми со сборкой этого приспособления? Должно быть её отец. "
    
    image Old_Kasumis_Dad = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Old_Kasumi_Dad.png"
    image Old_Kasumis_Dad_Dream:
        contains:
            "Old_Kasumis_Dad"
        contains:
            "Dream_Frame"
        
    image Young_Kasumi_Dad = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Young_Kasumi_Dad.png"
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
    
    play environment_sounds_dream "./sounds/environment/City_Suburb_Day_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    scene Old_Kasumis_Dad_Dream with Dissolve( my_dissolve_05 )
    
    "Я представил его себе как интеллигентного, худощавого, в толстых очках и с пышной зачёсанной набок шевелюрой. "
    "Похожего на профессора по физике в университете, где я учился. "
    
    scene Young_Kasumi_Dad_Dream with Dissolve( my_dissolve_05 )
    
    "Но профессор был старый, а отец Касуми, он должен быть моложе. Если Касуми всего шестнадцать лет — ему максимум, слегка за сорок. "
    "Вероятно он тоже радиолюбитель, как Макото-сан. Такой же увлечённый. "
    "Небось за своей радиостанцией и забыл что его незрячая дочь шатается одна по улицам неизвестно где. "
    "И наверное это он такой заядлый курильщик."
    
    play sound "./sounds/sounds/Morse_Code.mp3" fadein 1
    scene Dad_In_Room_Dream with Dissolve( my_dissolve_05 )
    
    "Я представил как её отец, сидит за рацией, крутит всякие крутилки, щёлкает тумблерами, да смолит сигарету. "
    "Затем подходит к открытому окну и задумчиво смотрит на городской пейзаж. "
    
    stop sound fadeout 3
    scene Kasumi_And_Pervert_Dream with Dissolve( my_dissolve_05 )
    
    "И видит свою дочь, а рядом с ней, какого-то небритого, лохматого и нетрезвого извращенца. "
    
    play environment_sounds "./sounds/environment/City_Suburb_Day.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    scene Outdoor_Day_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )

    "Я поёжился. Посмотрел на мятую рубаху и неопрятные брюки. Провёл ладонью по щетине и растрёпанной шевелюре. "
    "Слава богу, волосы на затылке, которые по утрам стояли дыбом — теперь улеглись. Видимо намокли от пота и перестали топорщиться. "
    "Хоть какой-то плюс, правда - небольшой. "
    "Вообще хорошо, что Касуми меня не видит, если бы она внезапно прозрела — убежала бы в миг с криками. "
    "А так, я кажусь ей вполне обычным человеком, если не брать во внимание запах алкоголя."
    "На всякий случай я понюхал и свои подмышки. Вроде приемлемо. "
    "По крайней мере запах сигарет, исходивший от Касуми, ощущается явно сильнее. Надо же как пропахла!"

    kenji "Касуми. А эта рация? Она тебе для чего?"
    kenji "Ты тоже как и мой погибший дядя — радиолюбитель? Или рацию ты хочешь кому-то отдать?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Что значит кому-то отдать? Нет! Эта рация нужна мне самой."
    kasumi "И да, Танака-сан, я наверное всё-таки радиолюбитель."
    
    show kasumi_01 Concerned_Say with Dissolve( my_dissolve_02 )

    kasumi "А ваш дядя? Почему он погиб?"
    
    show kasumi_01 Concerned_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Мой дядя?"

    "Я пересказал историю, которую слышал от дяди Ватанабэ и в конце рассказа добавил:"

    kenji "Кажется он обманул меня."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Почему-же обманул?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А ты веришь в эту ерунду? Это самоубийство какое-то, провод под напряжением — вместо антенны. Чушь полная!"

    "Касуми пожала плечами."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Я однажды использовала вместо антенны нашу, бытовую сеть. Домашнюю."
    kasumi "Там правда всего сто десять вольт, а не несколько тысяч."
    kasumi "Но тоже немного опасно, конденсатор надо подобрать тщательно. Это не чушь!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Опять этот конденсатор! Везде конденсатор! "
    "Похоже этот конденсатор — нечто вроде философского камня в среде радиолюбителей. "
    "А я про него ничего не знаю!"

    kenji "А зачем тогда вообще закидывать провод туда, где такое большое напряжение?"
    kenji "Раз ты говоришь, что в розетке всего сто десять вольт. Вот бы и втыкался туда!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Но тогда сигнал, дальше домашней сети не выйдет. Там же трансформатор, слабая выйдет антенна."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Точно! И как я забыл про трансформатор!"
    
    "Но, если честно, про трансформатор я никогда и не вспоминал. Да и вообще, слово это произносил в своей жизни впервые."

    kenji "Почему нельзя было просто привязать свою антенну к металлической опоре? Она же вон какая огромная?"
    kenji "Чего ему не хватало?"
    
    hide kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    show Kasumi_03 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Касуми отвернулась и поджала губы. Мне показалось, что она едва сдержала смешок. "
    "Ну да, подозреваю, что говорю я полнейшую ерунду."
    
    hide Kasumi_03 Normal_Silent with Dissolve( my_dissolve_01 )
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Она же заземлена. Не получится из неё антенна!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я вспомнил ту металлическую опору, что стояла в нашем саду. "
    "Каждая из четырёх её лап, была толстыми болтами прикручена к железобетонной плите. "
    "Она точно не соприкасалась с землёй!"

    kenji "Нет! Нет на ней никакого заземления!"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Не может быть! Должно быть вы просто не заметили, Танака-сан."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Нет! Я прекрасно вижу! Ничего там не было!"
    
    "Воскликнул я. А через секунду понял, насколько неприятную для собеседницы вещь сказал."
    "Но Касуми будто бы и не заметила ничего. На мгновение она задумалась."
    
    hide kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    show Kasumi_School_Uniform_Hmm Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Она наверное... Она наверное заземлена сверху!"
    
    hide Kasumi_School_Uniform_Hmm Normal_Say with Dissolve( my_dissolve_01 )
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Заземлена сверху... Эта фраза совершенно добила меня. Да, черт возьми, Кендзи - сверху! "
    "Ха — ха! Плевать, что земля - она внизу. Тут как пить дать, дело не обошлось без конденсатора. "
    "Впрочем куда же без него, а Кендзи? Как тебя вообще земля носит, без конденсатора то?"
    
    "Наверное дальше спорить не имело смысла. Я совершенно ничего не смыслил в этих делах."
    "На некоторое время мы замолчали"
    
    scene Outdoor_Day_Street_01 with Dissolve( my_dissolve_05 )
    
    "Я взглянул на небо. Судя по солнцу, сейчас уже часов пять дня. Я достал телефон из брюк и посмотрел время. Пять часов, десять минут. "
    "Ещё час и улицы наводнят люди, возвращающиеся с работы."
    
    "Пока на улицах никто не встретился нам, однако мы прошли больше чем половину пути, полагаю, здесь уже жили люди, которые могли знать Касуми. "
    "Кто-то из них, выглянет в окно, увидит что к ней привязался какой-то мутный тип. Позвонит её отцу..."
    
    #ЦГ - Але тут педофилы
    image Here_Is_A_Pedo_01 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/01.png"
    image Here_Is_A_Pedo_02 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/02.png"
    image Here_Is_A_Pedo_03 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/03.png"
    image Here_Is_A_Pedo_04 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/04.png"
    image Here_Is_A_Pedo_05 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/05.png"
    image Here_Is_A_Pedo_06 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Here_Is_A_Pedo/06.png"
    
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
    
    kenji "Касуми? А твои родители? Они дома?"
    
    show Kasumi_03 Normal_Silent with Dissolve( my_dissolve_02 )

    "Моя спутница опустила голову, и немного отвернулась от меня. Я что задал неудобный вопрос?"
    
    show Kasumi_03 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Мои родители... У меня... Нет родителей!"
    
    show Kasumi_03 Normal_Silent with Dissolve( my_dissolve_02 )

    "Да и в самом деле неудачный вопрос."

    kenji "Извини... Что спросил про такое."

    "Касуми пожала плечами."
    
    hide Kasumi_03 Normal_Silent with Dissolve( my_dissolve_02 )
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Ничего. Я наверное, к этому уже привыкла."
    
    scene Outdoor_Day_Kasumi_Street with Dissolve( my_dissolve_05 )
    
    "Пару кварталов мы прошли молча. Не знаю о чем думала Касуми, меня же донимали мысли о её отце. "
    "А скорее, о том несуществующем человеке, которого я сам придумал. Мне даже стало жалко эту вымышленную личность."

    "Узнать бы у Касуми о судьбе её родителей, но это не то, что должен спрашивать такой малознакомый человек, как я. "
    "Всё же я поинтересовался, хоть и не напрямую."

    kenji "А здесь, ты с кем живёшь, Касуми?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "С тётей."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Значит это её тётка столько курит! Хотелось спросить, как же эта женщина так пристрастилась к сигаретам. "
    "Но это был бы уже не просто неудобный, а крайне свинский вопрос. "
    "Я глубоко вдохнул, стараясь уловить побольше этого, «аромата» исходившего от моей спутницы. "
    "Интересно, а как по настоящему пахнет Касуми?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Почему вы вздыхаете? Танака-сан?"
    kasumi "Вам жаль меня? Из-за родителей?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да нет я... Нет, мне конечно жаль что их нет, Касуми. Но вздохнул я... Я просто переводил дух. Устал."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Мы почти на месте!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я не так хорошо знал этот район города. Впрочем я вообще мало знал окрестности вдали от дома, как и полагалось порядочному хиккикомори."
    "Мы шли по узенькой улочке. Я опасливо озирался по сторонам, обшаривая взглядом окна и балконы."
    "Особенно я боялся увидеть тетку Касуми. Хоть и совершенно не имел представления, как она выглядит."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Мой дом слева, второй за перекрестком. Он желтого цвета, с синей черепицей."
    kasumi "Чтобы не утруждать вас, Танака-сан, я не буду проводить свои обычные, эм... Ритуалы."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ритуалы?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Ну, мне нужно найти важные ориентиры, вы же понимаете. Кажется, сейчас я немного дезориентирована."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А, ну да."
    
    scene Day_Kasumi_Home with Dissolve( my_dissolve_05 )

    "Действительно, как только мы прошли перекресток, и первый дом за ним я увидел маленький домик выкрашенный бледно-желтой краской."
    "Площадка перед домом была посыпана гравием и усеяна разбитой тратуарной плиткой, забор и ворота отсутствовали. "
    "По краям участка росли помидорные кусты."

    kenji "Кажется пришли! Это у тебя во дворе растут помидоры, Касуми?"

    "Касуми не ответила, но повернулась в сторону своего дома, вытянула руки и пошла вперед. "
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Как только ее ноги ступили на гравий, она положила свою тележку на землю и повернулась ко мне. Похоже теперь она сориентировалась."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Танака-сан! Вы так помогли мне!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Она учтиво мне поклонилась."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Большое вам спасибо! Может быть вы хотите выпить чая?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Да, конечно! Я бы выпил чая с Касуми, если бы знал, что на этом всё, и больше никогда я её не увижу. "
    "Но ещё в пути у меня созрел хитрый план."

    kenji "Нет, Касуми!"

    "Похоже что мои слова ее удивили."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Не хотите?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не очень. Я лучше пойду поскорее домой."

    "Касуми выглядела растерянной. Я поставил рацию на землю, возле бетонного столбика."

    kenji "Рация. Я здесь оставлю её. Донесёшь до дома? Касуми?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Тётя поможет мне!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    kenji "Хорошо. А тележку твою, я конфискую."
    
    show kasumi_01 Surprised_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Но зачем? Что значит конфискуете? Это не моя, тётина. Что я ей скажу?"
    
    show kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Не боись. Завтра верну в целости."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Я поднял тележку и повесил на плечо."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Завтра?"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Во сколько могу её занести? В час дня, например?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "В час дня..."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Рассеянно произнесла девушка. А потом, словно встрепенулась."
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Да, как вам будет удобно!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А ты будешь дома?"
    
    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Да! Буду дома."
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну и отлично..."

    "Касуми ещё раз поклонилась мне."

    show kasumi_01 Normal_Say with Dissolve( my_dissolve_02 )

    kasumi "Прощайте, Танака-сан!"
    
    show kasumi_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Пока!"
    
    hide kasumi_01 with Dissolve( my_dissolve_02 )

    "Ответил я ей. Хотелось ещё добавить «до завтра», но мне показалось, что это будет слишком."
    
    play environment_sounds "./sounds/environment/City_Evening.mp3" fadein 1 fadeout 1
    scene Outdoor_Evening_BG_With_Railroad_2 with Dissolve( my_dissolve_05 )
    
    "Около семи часов вечера я вернулся на площадку для сбора мусора. Она опустела — все уже забрали уборщики."
    "Подоспел к площадке я вовремя, чипсы, которые я купил на обратном пути от дома Касуми — я уже доел, и мне надо было избавиться от упаковки."

    "На улицах стало оживлённее, всё чаще мимо проезжали машины, мопеды, мелькали велосипедисты. "
    "Собачники повели своих питомцев на прогулку. На детских площадках появились дети и присматривающие за ними мамочки. "
    "Я как мог, увиливал от идущих мне навстречу людей. Переходил улицу, чтобы встать с другой стороны. Проскакивал в узких, безлюдных переулках. От одной группы смеющихся старшеклассниц и вовсе спрятался в кустах! "
    "Сейчас, конечно, самое правильное решение - укрыться поскорее в доме, но мне за  сегодня нужно сделать еще одно дельце. "
    
    
    #Спрайты Айко в мобильном телефоне
    image Kenji_MObile_Phone = "./images/cg/DAY_01/06a_Watanabe/Kenji_Mobile_Phone/Kenji_Mobile_Phone.png"
    image Kenji_MObile_Phone_Mask = "./images/cg/DAY_01/06a_Watanabe/Kenji_Mobile_Phone/Kenji_Mobile_Phone_Mask.png"
    
    image Aiko_Base_Outfit_03_Normal_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Normal_Say"
    
    image Aiko_Base_Outfit_03_Normal_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Normal_Silent"
    
    image Aiko_Base_Outfit_03_Surprised_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Surprised_Say"
    
    image Aiko_Base_Outfit_03_Surprised_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Surprised_Silent"
            
    image Aiko_Base_Outfit_03_Angry_Say_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Angry_Say"
    
    image Aiko_Base_Outfit_03_Angry_Silent_Mobile:
        contains:
            xpos 1350
            ypos 100
            "Aiko_Base_Outfit_03_Angry_Silent"
    
    image Aiko_Base_Outfit_03_Normal_Say_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Normal_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Normal_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    image Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Surprised_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Surprised_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    image Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Angry_Say_Mobile", "Kenji_MObile_Phone_Mask" )
    image Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked = AlphaMask( "Aiko_Base_Outfit_03_Angry_Silent_Mobile", "Kenji_MObile_Phone_Mask" )
    #
    
    play sound "./sounds/sounds/Mobile_Phone_Vibration.mp3"
    show Kenji_MObile_Phone with Dissolve( my_dissolve_02 )
    show Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )

    "У меня зазвонил телефон, это была Айко."
    
    show Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked

    aiko "Кендзи? Ты где?"
    
    show Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked

    "Голос её был взволнован."

    kenji "Я? Да практически возле дома. Но приду чуть позже."
    
    show Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked
    
    aiko "Я думала, ты так напился, что не смог найти путь домой. Ты что, выпил всё своё пиво?"
    
    show Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked
    
    kenji "Ну да..."

    "Айко возмущенно завопила:"
    
    show Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked

    aiko "Ты алкоголик!"
    
    show Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked
    
    kenji "Постой Айко! Три банки пива это не три бутылки сакэ, ты не путай! Чего ты так раскричалась?"

    "Но ей конечно было всё одно, что сакэ, что пиво. Я действительно, редко выпивал за день больше одной или двух банок. Если пил вообще."
    
    show Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked

    aiko "В магазин утром пойдёшь сам! И завтрак в дорогу сам себе готовить будешь!"
    
    show Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked
    
    kenji "Завтрак в дорогу? Зачем? Ты меня из дома завтра погонишь?"
    
    show Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked
    
    aiko "Ты же на море собрался, разве нет?"
    
    show Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked
    
    kenji "Ах, точно! Я совсем забыл. Прости, Айко, но похоже, с поездкой на море придётся повременить."
    
    show Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked
    
    aiko "Что так?"
    
    show Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Say_Mobile_Masked
    
    kenji "Дела. Мне надо... Встретиться кое с кем."
    
    show Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Surprised_Silent_Mobile_Masked
    
    aiko "Этот кто-то, тоже алкоголик?"
    
    show Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked
    
    kenji "Айко, бросай свои шуточки! Надеюсь ты не обиделась, что на море мы завтра не едем?"
    
    show Aiko_Base_Outfit_03_Normal_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Angry_Silent_Mobile_Masked
    
    aiko "Мне то что. Я могу в любой день пойти в бассейн. А могу даже поехать на пляж без тебя, с подружками."
    
    show Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Normal_Say_Mobile_Masked

    "Я вздохнул. Айко помолчала какое-то время и спросила."

    show Aiko_Base_Outfit_03_Normal_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked

    aiko "Куда ты сейчас?"
    
    show Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Normal_Say_Mobile_Masked
    
    kenji "Мне надо зайти к дяде Ватанабэ."
    
    show Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Aiko_Base_Outfit_03_Normal_Silent_Mobile_Masked
    
    aiko "Да? Ладно. Но я позвоню ему, и скажу чтобы он тебе не наливал!"
    
    hide Aiko_Base_Outfit_03_Angry_Say_Mobile_Masked with Dissolve( my_dissolve_01 )
    hide Kenji_MObile_Phone with Dissolve( my_dissolve_02 )
    
    kenji "Айко!"

    "Айко бросила трубку. Я выругался про себя и убрал телефон в карман. "
    "Теперь меня занимали мысли о алкоголиках. А точнее, стал ли я уже одним из них или Айко как всегда — преувеличивала. "
    "Настоящих алкоголиков я знал немного. Да, пожалуй, всего одного. Это был тот самый, умерший телемастер из моего детства, дядя Сато. "
    "Тот, в чью честь воздвигли пирамиду из его же телевизоров. "
    "Он пил «по настоящему», мои нынешние пивные посиделки — капля в море сакэ, которое выпил дядя Сато. "
    "Я же саке на дух не переносил, как и любой другой крепкий алкоголь. "
    "Нет. Мне быть алкоголиком не грозит, ну кто же может стать алкашом, употребляя только пиво?"
    
    play environment_sounds "./sounds/environment/City_Industrial_Day.mp3" fadein 1 fadeout 1
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    "Размышляя над этим, я и не заметил как добрался до дома Ватанабэ. На мою радость его гараж, и одновременно — мастерская был открыт. "
    "Дядя Ватанабэ ещё не закончил работать. "
    "Я подошёл ближе и поздоровался с ним."
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "А, привет Кендзи! Гляди. Парень десять тысяч накрутил, а звёздочка распредвала — не съедена."
    watanabe "И цепь не растянулась, ни на миллиметр! И натяжитель держит."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Что такое \"цепь\" и \"звездочка\" мне может быть было понятно"
    "Но что за зверь такой \"распредвал\" я не знал совершенно"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Но что-то гремит. Я думал — ну точно распредвал, что ещё может?"
    watanabe "Столько времени потратил чтобы генератор снять. Плотно он засел!"
    watanabe "Чуть на съёмнике резьбу не съело! Прокладку порвал! А внутри — всё целёхонькое!"
    watanabe "Что же тогда гремит то, Кендзи?"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Как обычно, дядя Ватанабэ задавал мне вопросы на которые я не знал ответа. И он сам это понимал, но такая уж у него была привычка."
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А!"
    watanabe "Айко звонила. Говорит, ты нажрался как свинья и шатаешься по городу!"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Айко! Вот чертовка!"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ты правда пьяный?"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Три банки пива выпил, только и всего. А Айко как всегда на своей волне, ну вы же знаете."
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Три банки! Не смертельно, но солидно. Что празднуешь?"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Да я мусор выносил. Кладовку освобождаю. Тётя Асука просила, чтобы я вещи дяди Макото выбросил."
    kenji "Вещи тяжёлые, рация там и ещё что-то к ней. Уморился."
    
    show Watanabe_01 Sad_Say with Dissolve( my_dissolve_02 )

    watanabe "А..."
    
    show Watanabe_01 Sad_Silent with Dissolve( my_dissolve_02 )

    "Голос его внезапно стал сиплым."
    
    show Watanabe_01 Sad_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Асука ко мне приходила, спрашивала не хочу ли я забрать чего."
    watanabe "Но мне бы своё барахло выбросить. Так и лежит, пыль собирает, с тех пор как эти дела забросил."
    
    show Watanabe_01 Sad_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Радио?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ну да."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А почему забросили?"
    
    hide Watanabe_01 with Dissolve( my_dissolve_01 )
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Почему забросил..."
    
    show Watanabe_02 Normal_Silent with Dissolve( my_dissolve_02 )

    "Он задумался."
    
    hide Watanabe_02 with Dissolve( my_dissolve_01 )
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_01 )

    watanabe "А что же мне, до скончанья веков этим заниматься?"
    watanabe "Ты вот тоже, Кендзи, небось скоро забросишь компьютеры свои, найдёшь девчонку себе, женишься. Давно пора."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Почему-то при словах «найдёшь девчонку», я подумал о Касуми. Меня эта мысль немного смутила, даже слегка потеплели уши. "
    "А дядя Ватанабэ продолжал:"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Теперь там все по другому - наши времена прошли." 
    watanabe "А Кайоши, он даже был «радиопульсаром»! Он мне потом признался." 
    watanabe "Если бы в школьные годы узнал — я бы ему рожу начистил. А потом уже, так..."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Он махнул рукой."
    kenji "Радио... Пульс... Пульсаром? Что значит, был «радиопульсаром»?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да это местное тайное общество, можно сказать, радиолюбительская «масонская ложа»!"
    watanabe "А по мне — так просто хулиганы они."
    watanabe "Каждый из нас их ненавидел, но каждый, мне кажется, если бы была возможность — моментально вступил к ним в клуб." 
    watanabe "Клуб — секретный! Никто не знал, кто в нём, и как туда попасть."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Дядя Ватанабэ замолчал и о чем-то задумался. Я не вытерпел и спросил:"

    kenji "А что они делали?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Нам мешали! Правила вводили дурацкие. У каждого, дескать должен быть позывной."
    watanabe "Он и на самом деле должен быть. Но нам, пацаном разве прикажешь."
    watanabe "Кто их не слушал — того они вышибали из эфира. Были у них способы, глушилка, например."
    watanabe "Ещё и цензура, про что можно говорить в эфире, про что нельзя. Была даже листовка у меня, свод правил для вещания."
    watanabe "Вот такие были эти ребята."
    watanabe "Говорят, они строили что-то вроде «глушащей пушки», очень мощной. Можно было направить в любую сторону и глушить всех кто там есть."
    watanabe "Но вроде как не достроили. А потом мы уже из школы выпустились."
    watanabe "И «радиопульсар» тоже поредел, много видимо ребят из нашего выпуска там было. Теперь его, клуба этого, и нет вовсе."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А как это, глушат?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Да как глушат?"
    watanabe "Включил рацию, а там неслышно ни хрена, значит глушат. Вот как!"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    "Я конечно ничего не понял, но дальше распрашивать не стал - не мое в общем-то дело, что там у них и как. "
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А что это за штуковина у тебя, Кендзи?"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "А это..."
    
    "Я вспомнил про тележку Касуми."
    
    kenji "Я ведь по делу пришел, дядя Ватанабэ. Починить надо..."

    "Я показал ему на культи, которые остались у тележки вместо колес. "
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "А зачем? Тут проще новую купить, Кендзи."
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Купить... Это не моя тележка!"
    
    hide Watanabe_01 with Dissolve( my_dissolve_01 )
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Ты значит, когда мусор выносил, у кого-то тележку позаимствовал, и угробил?"
    
    show Watanabe_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну... Почти что так."
    
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Ну так купи и отдай им новую! Сколько такая хрень стоит? Три — пять тысяч йен, не больше"
    
    show Watanabe_02 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Нет, дядя Ватанабэ. Мне бы починить её, ну можно же?"
    
    hide Watanabe_02 with Dissolve( my_dissolve_01 )
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    watanabe "Да где я тебе найду колеса такие?"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )
    
    kenji "Ну, не обязательно прямо такие. От чего другого может подойдет?"

    "Ватанабэ покряхтел и скрылся в своей мастерской - гараже."
    
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
    
    play sound "./sounds/sounds/Metal_Parts.mp3"
    show Watanabe_Garage_Sounds
    "Из глубины гаража донеслись гремящие звуки, кашель, тихая ругань. Спустя минуту дядя Ватанабэ вышел ко мне. "
    hide Watanabe_Garage_Sounds
    
    ##Мини-ЦГ - велосипед Айко
    image Aiko_Bike = "./images/cg/DAY_01/06a_Watanabe/Aiko_Bike/Aiko_Bike.png"
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
    
    "В руках он нёс детский велосипед. Я воскликнул."
    
    kenji "О! Это же старый велик Айко!"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Ага! Твой отец мне его отдал когда-то. Кажись — нашёлся донор!"
    
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    "Дядя Ватанабэ снял какие-то металлические кольца с краёв оси тележки, выкинул то что осталось от прежних колес и примерил новые."
    
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Не подходят ни хрена! У тележки — ось толще!"
    
    show Watanabe_02 Normal_Silent with Dissolve( my_dissolve_02 )

    kenji "И что? Никак?"
    
    show Watanabe_02 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Почему никак? Щас рассверлим!"
    
    scene Evening_Watanabe_Bike_WorkShop with Dissolve( my_dissolve_05 )
    
    "Он схватил тележку, велосипед и колеса и вновь скрылся в гараже."
    
    show Watanabe_Garage_Sounds
    play sound "./sounds/sounds/Drill.mp3"
    "Послышалось жужжание и скрежет сверлильного станка. А через минуту дядя Ватанабе показался с тележкой."
    hide Watanabe_Garage_Sounds
    
    ##Мини ЦГ - Тележка с новыми колесами
    image Kasumi_Cart_With_New_Wheels_Evening = "./images/cg/DAY_01/06a_Watanabe/Kasumi_Cart_With_New_Wheels/Kasumi_Cart_With_New_Wheels_Evening.png"
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
    
    watanabe "Ну вроде всё."

    "Он протянул тележку мне."
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )

    watanabe "Эти колёса в сто раз лучше будут. Крепкие! Уже не сломаешь!"
    
    show Watanabe_01 Normal_Silent with Dissolve( my_dissolve_02 )

    "Я покатал тележку по земле, колеса крутились, но туго. "
    
    hide Kasumi_Cart_With_New_Wheels_Evening_With_Border_01 with Dissolve( my_dissolve_05 )

    kenji "Сколько с меня?"
    
    show Watanabe_01 Normal_Say with Dissolve( my_dissolve_02 )
    
    watanabe "Нисколько! Только помоги мне закатить мотоциклы в гараж. Но смотри, держи под наклоном, чтобы масло не вытекло!"
    
    play environment_sounds "./sounds/environment/City_Evening.mp3" fadein 1 fadeout 1
    scene Outdoor_Evening_Kenji_Home with Dissolve( my_dissolve_05 )

    "Покончив с этим я отправился домой."
    "И десяти минут не прошло как я был возле дома. Тележку я в дом заносить не стал, спрятав её за палисадником с цветами. "
    "Земля в палисаднике была влажная, видимо Айко совсем недавно поливала цветы. Я вошёл в дом."
    
    play environment_sounds "./sounds/environment/Kitchen.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 ) 
    
    "Айко на кухне не было. Я включил телевизор и задумался о своём ужине. Очень хотелось есть. "
    "За сегодняшний день я съел только тарелку салата да пачку чипсов. А уже поздно — восьмой час. "
    "В такое время я всегда был дома и ужинал вместе с Айко."
    "Можно было конечно сбегать наверх, в её комнату и попросить приготовить мне чего. Но не хотелось попадаться Айко на глаза."
    "Я решил заварить себе рамэн. "
    
    image Instant_Noodles = "./images/cg/DAY_01/07a_Kenji_Evening_Meal/Instant_Noodles/Instant_Noodles.png"
    scene Instant_Noodles with Dissolve( my_dissolve_05 )
    
    "Телевизор по прежнему показывал новости. Шел блок про незначительные события."

    tv "А ведь слоновья нога до сих пор плавит бетон четвертого энергоблока..."

    "Но я не особо вникал, мой трезвеющий мозг занимали мысли о Касуми. "
    "Вернее беспокойные мысли связанные с нашими дневными похождениями."
    "Правильно ли я сделал, что навязался в помощники? Не видел ли нас вместе кто-то из знакомых? "
    "Может быть не стоило забирать у неё тележку, что она сейчас скажет своей тётке? "
    "Не был ли слишком навязчив и груб?"

    "Я помнил как Касуми вела себя - слишком сдержанной она была, неулыбчивой. Наверное несладко ей живётся, будучи слепой сиротой. "
    "Говорят — такие люди тянутся к тем кто делает для них добро. А я для неё столько сделал! "
    "Но она всё равно... "
    "Может жизнь её так потрепала, что она просто боится всех? "
    "Ну прямо как я! "
    "Или нет? Касуми не показалась мне уж очень застенчивой. И она точно не выпивает «для храбрости». "

    "Я вновь в голове прокрутил сцену встречи с ней, поход к её дому. Вспомнил, какой сдержанной была Касуми. Не помню чтобы она весело смеялась. "
    "А я шутил? Надеюсь что нет! Шутки небось у меня, подвыпившего — дурацкие. "
    "Как она называла меня, тоже вспомнил — «Танака-сан». "
    "Ну да, про мой возраст она наверняка догадалась. А как ведут себя молодые девчонки с незнакомыми, взрослыми мужчинами? Скорее всего именно так! "
    "Может потому что я был пьян, она так реагировала? Наверно несло алкоголем от меня исправно! "
    "А от неё куревом! Все мы не без недостатков, получается."
    "Хотя я уверен - Касуми не курит! Она хорошая! "
    "Просто ангел!"
    
    kenji "Прости меня, Касуми, за все!"

    "Вполголоса пробормотал я. "

    aiko "Пришел!"
    
    ##Мини ЦГ - Айко в дверях кухни
    image Evening_Kenji_Kitchen_Door = "./images/bg/Indoor/Kenji_Home_Kitchen/Evening/Door.png"
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
    show Aiko_Base_Outfit_03 Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    "Я и не заметил как на кухню пробралась Айко. Она внимательно смотрела на меня."
    "Наверное хочет определить, насколько я пьян! А я уже практически трезв. "
    "Надеюсь она не слышала моих извинений!"
    
    show Aiko_Base_Outfit_03 Suspect_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 

    aiko "Где ты был?"
    
    show Aiko_Base_Outfit_03 Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    kenji "Как где? У дяди Ватанабэ! Я же говорил, а до этого — вещи из кладовки выносил. Где же мне ещё быть?"
    
    show Aiko_Base_Outfit_03 Suspect_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 ) 
    
    aiko "Что-то долго ты выносил вещи на свалку!"
    
    show Aiko_Base_Outfit_03 Suspect_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Не хотелось рассказывать Айко про Касуми."

    kenji "Ну да, выносил чуть не до шести часов. Что тут такого?"
    kenji "И вообще, это что за допрос? Я жутко устал! Отстань, Айко!"
    
    show Aiko_Base_Outfit_03 Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Айко вздохнула."
    
    show Aiko_Base_Outfit_03 Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    aiko "Ладно, извини. Всё-таки я волновалась за тебя."
    aiko "Ушёл и с концами. И пиво всё выпил!" 
    aiko "Я думала, вдруг в канаве утонешь. Помнишь, как тот алкоголик, про которого рассказывал папа?"
    
    show Aiko_Base_Outfit_03 Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Меня снова чуть покоробило, когда Айко назвала моего отца «папой». "
    "А алкоголик утонувший в канаве, ни кто иной как дядя Сато. Именно так он отправился на тот свет. "
    "Свалился пьяный в придорожную канаву и захлебнулся в ней."

    kenji "Да сейчас в канаве и не утонуть. Они же все пересохли!"
    
    show Aiko_Base_Outfit_03 Smile_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    "Айко улыбнулась."
    
    show Aiko_Base_Outfit_03 Smile_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )

    aiko "Ну да!"
    
    show Aiko_Base_Outfit_03 Smile_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    kenji "Кстати! Раз уж речь о утопленниках и канавах! Ты сейчас не идёшь в душ Айко?"
    
    show Aiko_Base_Outfit_03 Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    aiko "А? Нет! Почему спрашиваешь?"
    
    show Aiko_Base_Outfit_03 Normal_Silent at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    kenji "Мне туда надо! Срочно! Кажись я здорово употел пока с барахлом из кладовки возился!"
    kenji "Айко, пожалуйста, наполни ванную водой!"
    
    show Aiko_Base_Outfit_03 Normal_Say at Move( ( 300, 600 ), ( 300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    aiko "Хорошо!"
    
    hide Aiko_Base_Outfit_03 with Dissolve( my_dissolve_01 )
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 ) 

    "Айко убежала вверх по лестнице. Видимо она немедленно решила исполнить мою просьбу."
    "Я между тем закончил свой ужин, сложил посуду в мойку и отправился на второй этаж. "
    
    image Evening_Kenji_Bedroom = "./images/bg/Indoor/Kenji_Bedroom/Evening/Base.jpg"
    play environment_sounds "./sounds/environment/Shower.mp3" fadein 1 fadeout 1
    scene Kenji_Home_Bathroom with Dissolve( my_dissolve_05 )
    
    "Ванна была полна чуть более чем на половину. "
    "Я тщательно выскоблил себя мочалкой. Правда руки и шея здорово сгорели на солнышке и мочалкой к ним было не прикоснуться. "
    "Лицо сильно загорело и покрылось пятнами. Я смотрел на себя в зеркало, и с неудовольствием отмечал какой клоунский у меня вид. "
    "Красные, обгоревшие нос и скулы, тёмные синяки под глазами, щетина. "
    "Жуть. "
    "А может лучше так, чем бледное как смерть, лицо безвылазного домоседа?"
    
    "Я взял бритву и тщательно побрился, подровнял виски. Но собственное отражение в зеркале мне не нравилось всё равно. "
    "Без бороды, вид у меня стал совершенно беспомощный. Наверное надо было её просто укоротить машинкой для стрижки, а не сбривать полностью. "
    "Хотя какая разница, я же собираюсь понравиться человеку который не знает ничего о моём внешнем виде. И не узнает."
    "Впрочем нет. Я собираюсь понравиться человеку, который наверняка видит прекрасно и рассмотрит меня с особым пристрастием. "
    "Этот человек — тётка Касуми. "
    "Придётся постараться и придать себе более презентабельный внешний вид. "
    "Хорошо одеться, но неброско. Надеюсь у меня в запасах есть дезодорант и одеколон. "
    "Ну а если нет, наверняка в комнате отца и тёти Асуки должно что-то остаться. "
    "Надо только не перестараться, у Касуми наверняка нюх отменный!"
    "Или нет - учитывая что от неё за версту тянет сигаретным дымом? Хотя, говорят, не чувствовать свой запах — основа нюха!"
    
    ##ЦГ - Касуми с руками Кензи у нее на плечах
    image Dreams_About_Kasumi = "./images/cg/DAY_01/08a_Kenji_Bath_Time/Dreams_About_Kasumi/Dreams_About_Kasumi.png"
    image Dreams_About_Kasumi_Moved:
        contains:
            ypos -300
            "Dreams_About_Kasumi"
            pause 0.5
            ease 5.0 ypos -500
        
        contains:
            "Dream_Frame"
    play environment_sounds_dream "./sounds/environment/Shower_Dream.mp3" fadein 1
    stop environment_sounds fadeout 1
    show Dreams_About_Kasumi_Moved with Dissolve( my_dissolve_05 )
    
    "Я снова задумался о том, как пахнет Касуми."
    "Закрыл глаза, представил, как она стоит прямо перед мною. Я положил ладони ей на плечи и слегка наклонился чтобы почуять запах кожи, в том месте, где её шея выглядывает из под ворота матроски."

    "Мысль, о том что я выгляжу как идиот, кольнула меня."
    
    stop environment_sounds_dream fadeout 1
    play environment_sounds "./sounds/environment/Shower.mp3" fadein 1 fadeout 1
    hide Dreams_About_Kasumi_Moved with Dissolve( my_dissolve_05 )
    
    "Я открыл глаза и опустил руки. "
    "Конечно, никакого запаха Касуми я не мог почувствовать даже если бы и в самом деле взял её за плечи и уткнулся носом в шею."
    "Только удушающий аромат сигаретного дыма."
    
    "Я забрался в ванную. Обожжённые солнцем руки, невыносимо жгла вода и я положил их на бортики ванны. "
    "Опираться спиной на заднюю стенку ванны тоже было неприятно — болела спина. "
    "Я потёр ладонями плечи и подумал о том, какие они, на ощупь, плечи Касуми. "
    "Мне очень захотелось прикоснуться к ним своими руками наяву, так же как минуту назад в своем воображении. Или провести ладонью по её голове. "
    "Да просто, хотя бы притронуться к рукавам её формы, или краю юбки. "
    "Если сделать это осторожно она же не заметит? Будет ли ещё такая возможность?"

    "Почему-то в тот момент, когда мы шли с ней, я не думал о таком. Да и телесных контактов с Касуми я не припомню. "
    "Только как её руки вцепились в мою ногу. А больше ничего. "

    "Я слышал, когда парень и девушка идут рядом, иногда их тыльные стороны ладоней случайно соприкасаются. "
    "Но с Касуми у меня такого не было. Наверное я старался держать дистанцию. "
    "Или было, но я в тот момент не заметил и не придал значения? "

    "Я закончил гигиенические процедуры душем и вышел из ванной."
    
    play environment_sounds "./sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "В своей комнате, я приступил к подбору одежды для завтрашнего мероприятия. "
    "У меня есть отличные джинсы для особых случаев, им уже лет пять, не меньше, но они в отличном состоянии, так редко я их одеваю. "
    "В пару к джинсам, я решил назавтра одеть рубашку в клетку. Рубаха была на вид бледноватой, как будто на солнце выгорела, но мне нравился ее неброский вид."

    "От выбранной одежды слегка попахивало запахом вещевого ящика, где она столько пролежала. "
    "Джинсы можно было одевать хоть прямо сейчас. А рубаху наверное стоило погладить.  "
    "Утюг и доска для глажки находились на кухне, где и стиральная машина. "
    "Надо бы подгадать момент когда Айко не будет на кухне. А то ещё подумает чёрт знает что. Что за встреча, к которой я так тщательно готовлюсь?"

    "Мне в голову пришла свежая идея. Я придумал способ маскировки некоторых недостатков своей внешности. "
    
    #Мини ЦГ - очки Кендзи
    image Kenji_Glasses = "./images/cg/DAY_01/08a_Kenji_Bath_Time/Kenji_Glasses/Kenji_Glasses.png"
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
    "Нет, у меня хорошее зрение, пусть оно и немного подсажено сидением за компьютером сутки напролёт. "
    "Это очки без диоптрий, в чёрной пластмассовой оправе. Специальные. "
    "Говорят — спасают от излучения испускаемого монитором. На самом деле это очки отца, но и мне подошли идеально."
    
    hide Kenji_Glasses_With_Border_01 with Dissolve( my_dissolve_05 )

    "Я одел очки и подошёл к зеркалу. "

    "Да, так определённо лучше! Отливающие синевой стекла скрыли мои синяки под глазами. Да и массивная оправа, перетягивала на себя всё внимание. "
    "Я даже помолодел! Стал выглядеть как студент выпускного курса. "
    "Удача, что я вспомнил про очки! Браво мне!"

    "Больше я ничего путного, что касалось моего внешнего вида, придумать не смог. "
    "Джинсы, рубашка, очки — что ещё надо? Все нормальные люди носят такое, а я хочу произвести впечатление нормального человека."

    "Теперь меня больше беспокоило то, как произвести хорошее впечатление на Касуми. "
    "Во что я буду одет для неё совершенно не важно. "
    "Завтра алкоголем и потом от меня нести не будет это плюс. "
    "Что ещё может быть важно? Наверное мой голос?"

    "Мне вдруг стало жутко интересно как он звучит. Я порылся в списке приложений телефона. "
    "Нашёл то, что позволяет записывать звук. Нажал на запись и произнёс:"

    kenji "Касуми... Привет, это я! Кендзи!"
    
    "Затем я нажал на воспроизведение, то что я услышал, повергло меня в шок! "
    "Пронзительный и гнусавый, совершенно неприятный мне голос. "
    "Какой ужас! И я так говорил всё это время? И тогда, с Касуми? "
    "Это полный крах! Я был по настоящему подавлен. Я столько лет прожил с таким голосом и даже не знал, какой он противный на слух. "
    "И с этим уже невозможно ничего поделать!"

    "Или нет? Наверное проблема не во мне! "
    "Точно! Это у телефона микрофон плохой! "
    "Мне нужен хороший, настоящий микрофон! Если я запишу с ним свой голос, он прозвучит как надо!"

    "И такой микрофон у нас дома был! Микрофон для караоке."

    "Мне нужно было в комнату отца и тёти Асуки! Это комната на первом этаже, соседняя с кухней. "
    
    scene Evening_Kenji_Parents_Room with Dissolve( my_dissolve_05 )
    
    "На виду необходимая мне вещь не лежала.  "
    "Я открыл один из ящичков под телевизором. Он был доверху набит дисками. Они лежали ровными пачками - видимо Айко постаралась. "
    "Я вынул диски из ящика и расставил на полу. Я надеялся что за ними, в дальнем углу обнаружу микрофон. "
    "Но ничего подобного — тут были только диски. "

    "Зато одна находка меня сильно заинтересовала. "
    "Последняя пачка дисков практически наполовину состояла из фильмов для взрослых! Это явно отцовские! "
    "Я взял один фильм, чтобы рассмотреть поближе. "
    "Дизайн был совершенно идиотский, да и коробка видавшая виды — вся потёртая и в трещинах."

    aiko "Ты чего тут делаешь?"
    
    #Мини ЦГ - дверь в комнату родителей Кендзи
    image Kenji_Parents_Room_Door = "./images/bg/Indoor/Kenji_Parents_Room/Evening/enji_Parents_Room_Door.jpg"
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
    show Aiko_In_Nightie Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я обернулся. В дверях комнаты стояла Айко. Похоже что она собиралась спать и переоделась в пижаму."
    "Она перевела взгляд на мои руки, державшие диск с порнушкой."
    "Ба! Вот так ситуация! Надо как-то оправдаться!"

    kenji "Я искал тут кое что!"
    
    show Aiko_In_Nightie Suspect_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Искал?"
    
    show Aiko_In_Nightie Suspect_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Почти шёпотом спросила Айко, и добавила:"
    
    show Aiko_In_Nightie Suspect_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    aiko "И нашёл?"
    
    show Aiko_In_Nightie Suspect_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что значит нашёл?"

    "Я поспешил избавится от компроментирующего диска, положив его на пол."

    kenji "Ничего не нашёл! Я искал не это!"
    
    show Aiko_In_Nightie Suspect_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты понимаешь, что ты извращенец? Это же для извращенцев кино!"
    
    show Aiko_In_Nightie Suspect_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Ну как всегда! Эту ретро порнографию я не стал бы смотреть ни за какие коврижки. А тут такое!"

    kenji "Что значит извращенец? С чего ты так решила?"
    kenji "Я не виноват что здесь валяется эта фигня."
    kenji "И вообще, это же моего отца! Он что тоже извращенец?"
    kenji "Или нет, может это твоего отца вещь, а Айко? И он был извращенцем? Неужели так?"
    
    show Aiko_In_Nightie Sorry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Наверное зря я приплёл сюда покойного отца Айко. После этой фразы она опустила голову, и произнесла жалобно:"
    
    show Aiko_In_Nightie Sorry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    aiko "Я хотела выкинуть! Когда убиралась здесь. Но потом забыла. Не хотела чтобы ты нашёл, а ты всё-таки нашёл!"
    
    show Aiko_In_Nightie Sorry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Да не нужна мне вся эта ерунда... Мне нужен... Микрофон для караоке! Вот зачем я полез сюда! Я ищу микрофон!"
    
    show Aiko_In_Nightie Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты врёшь!"
    aiko "Наверное ждал когда я усну, чтобы взять это."
    aiko "Я поняла какие у тебя завтра «дела»."
    aiko "Ты небось вступил в какой-то клуб извращенцев. И вы, в этом вашем клубе будете смотреть эти непристойности!"
    
    show Aiko_In_Nightie Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )

    "Да уж, неплохо у Айко фантазия работает! Теперь я ещё и в клуб извращенцев вступил. "
    "Странно, что не в клуб — «алкоголиков и извращенцев»! Теперь её уж точно не переубедить! "
    "Раз уж я взял эту гадость в руки мне не отвертеться! Остаётся только прогнать её поскорее из комнаты, а самому продолжить поиски."
    "Я театрально засмеялся:"

    kenji "Ха-ха! Ты меня раскусила! Да! Завтра у меня встреча в клубе извращенцев!"
    kenji "Я возьму эти диски с собой, и завтра мы будем смотреть все фильмы! Здорово а?"
    
    ##ЦГ - диск с порнущкой про сестру
    image Trip_To_Sea_With_Cute_Little_Sis = "./images/cg/DAY_01/09a_Porn_In_Parents_Room/Trip_To_Sea_With_Cute_Little_Sis/Trip_To_Sea_With_Cute_Little_Sis.png"
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
    show Aiko_In_Nightie Scared_Shy_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Лицо Айко исказила гримаса страха. Её уши и щеки, а потом и всё лицо залила густая краснота."
    "Я откинул диск в сторону и вскочил."

    kenji "Айко, я..."
    
    show Aiko_In_Nightie Scared_Shy_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Неееет!"
    
    play sound "./sounds/sounds/Aiko_Run_Away_From_Parents_Room.mp3"
    hide Aiko_In_Nightie with Dissolve( my_dissolve_01 )
    hide Kenji_Parents_Room_Door_With_Border_01 with hpunch
    
    "Айко встрепенулась, резко дёрнулась в сторону двери и исчезла за ней. "
    "Раздался топот босых ног по лестнице, а затем я услышал как захлопнулась дверь ее комнаты."

    "Черт! А что если Айко расскажет отцу? Наверное ему не понравится такое!"
    "А впрочем! Это же его вещи! Это он виноват, а не я! А мне между прочим тридцать лет. Стыдить меня просмотром порнушки - это бред."

    "Я приободрил себя этими мыслями, сложил пачки дисков обратно в ящик и выдвинул следующий. "
    "Тут меня ожидала удача! В ящике лежала толстая книжка — каталог песен, и коробка с микрофоном. "

    "Больше мне в комнате родителей делать было нечего, и я поспешил к себе. "
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "Я распутал микрофонный шнур, поднёс штекер микрофона к разьёму на компьютере."

    kenji "Чёрт!"

    "Штекер оказался намного больше гнезда. Этот микрофон был совершенно не совместим с моим компьютером. "
    "Полный провал! "
    "Я порылся в коробке, может быть там есть что-то вроде переходника? Нет, коробка была пуста."

    "Но возможно, эта неудача была моим спасением. "
    "По правде сказать, я ужасно боялся, что и с этим «нормальным» микрофоном мой голос не станет лучше. "

    "Увы. Я не обладал обворожительным, бархатным баритоном с хрипотцой. Говорят, от такого тащатся все девушки. "
    "Теперь мне совершенно ясно, почему у меня никогда не было подруги. "
    "Сейчас я бы пожертвовал любой деталью своей внешности которая мне казалась «нормальной». "
    "Пусть у меня будут кривые зубы, маленький подбородок или даже лысина. "
    "Но уверенный, красивый голос дал бы мне шанс на знакомство! Миллион шансов! Как жаль, что у меня нет и одного. "

    "Я сложил микрофон обратно в коробку, сел на стул и уставился в потолок. "
    "Мне подумалось, что наверное в интернете полно уроков, для того чтобы устранить гнусавость. "
    "Я включил компьютер и посмотрел парочку. "
    "Естественно везде говорилось об упражнениях, которые надо выполнять вслух. "
    "Хотелось приступить прямо сейчас, но за тонкой стенкой, всего в нескольких метрах от меня была Айко. "
    "Я надеялся что она успокоилась после недавнего происшествия, позабыла, что я извращенец — любитель фильмов для взрослых и сейчас уже спокойно спит."

    kenji "А ведь у девчонок все иначе! Им гнусавость даже идёт!"
    
    "Вполголоса воскликнул я. "
    
    #"Спрайты" одноклассников Кендзи
    image Kenji_Classmate_Girl = im.Scale( "./images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Girl.png", 726, 1100 )
    image Kenji_Classmate_Girl_In_armor = im.Scale( "./images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Girl_In_armor.png", 726, 1100 )
    image Kenji_Classmate_Boy = im.Scale( "./images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Boy.png", 836, 1100 )
    image Kenji_Classmate_Boy_In_Armor = im.Scale( "./images/cg/DAY_01/10a_Makoto's_Books/Kenji_Classmates/Kenji_Classmate_Boy_In_Armor.png", 836, 1100 )
    
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

    "Я вспомнил одну свою однокурсницу. Она — сильно гнусавила! "
    "Наверное благодаря пронзительному голосу её постоянно назначали старостой группы. "
    "Она могла докричаться до любого в аудитории, при любом уровне шума."

    "Я вспомнил её внешность. Она была довольно симпатичная. Небольшого роста, с длинными чёрными волосами."
    "Также я хорошо помнил что она носила очки в тонкой оправе. Но летом переходила на контактные линзы."

    "Говорят, девчонка эта многим нравилась. И у меня тоже была к ней некоторая симпатия. Естественно я это скрывал. "
    "Однажды весной, она принесла мне домой материалы для тестов, когда меня свалила простуда."
    "Это был невероятно удачный случай предложить ей встречаться или что-то в этом духе, но у меня не хватило храбрости."
    "Тяжело живется таким трусам как я."

    "А потом я узнал что у нее есть парень! Мне тогда показался странным ее выбор."
    
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
    
    "Во первых — он был толстый как бочка! Когда на улице было тепло с него ручьями тёк пот и пахло чем-то неприятным. "
    "У него была совершенно карикатурная, жёсткая кудрявая шевелюра, сросшиеся брови и невероятных размеров угри на носу."
    "Довершали образ нелепые очки в толстой роговой оправе. "
    
    "Несмотря на свой тучный вид, роста он был не великого - я не припомню парней меньше него. "
    "И самое главное — он страшно гнусавил, говорил очень торопливо, глотая слова. "

    "И этот человек — был парнем нашей миленькой старосты! "
    "Каждую переменку они встречались и весело щебетали в коридоре, а во время большой перемены он неизменно вёл её к аппарату по продаже напитков и покупал сок."
    "В качестве ответной благодарности она угощала его домашним бенто. "
    "После учебы этот парень всегда провожал её до дома."
    "Кто-то даже говорил, что видел как они целовались и лица тех, кто слышал эту новость, невольно искажались отвращением."

    "Я как-то спросил своего соседа по парте: «Почему наша миленькая староста встречается с этим страшилищем?»."
    
    hide Kenji_Classmate_Girl with Dissolve( my_dissolve_01 )
    hide Kenji_Classmate_Boy with Dissolve( my_dissolve_01 )
    show Kenji_Classmate_Girl_In_armor at Move( ( 1600, 520 ), ( 1600, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Kenji_Classmate_Boy_In_Armor at Move( ( 300, 520 ), ( 300, 520 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Помню он ответил мне, что они вместе играли в одну игрушку, ММО или что-то в этом роде."
    "Улекались одним делом в общем..."
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )

    "Я резко встал из-за стола. Вот что мне было нужно! Увлечение! Общее с Касуми увлечение! "
    "А уж чем увлекается она, мне известно. Жаль я сам в этом деле полный ноль, но ничего! Я приложу усилия и удивлю её! "
    "Ха-ха! Все эти конденсаторы, транзисторы, ёмкостные реле — я их как орешки перещёлкаю!"
    
    "Я выскочил из комнаты. Мне снова надо было на нижний этаж - в кладовку. "
    
    play environment_sounds "./sounds/environment/Pantry_Evening.mp3" fadein 1
    image Evening_Kenji_Home_Pantry_Other_03 = "./images/bg/Indoor/Kenji_Home_Pantry/Evening/Evening_Kenji_Home_Pantry_Other_03.jpg"
    scene Evening_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    
    "Я окинул взглядом стеллаж, на котором лежали книги. Старые книги дяди Макото, посвящённые радио и прочим сопутствующим вещам. "
    "Вот то что мне нужно! Я ещё не успел разложить их по коробкам и они занимали целую полку стеллажа."
    
    image Tube_Amplifiers_Book_Cover = "./images/cg/DAY_01/10a_Makoto's_Books/Tube_Amplifiers/Tube_Amplifiers_Book_Cover.png"
    image Tube_Amplifiers_Book_Content = "./images/cg/DAY_01/10a_Makoto's_Books/Tube_Amplifiers/Tube_Amplifiers_Book_Content.png"
    
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
    
    play sound "./sounds/sounds/Open_Book.mp3"
    hide Tube_Amplifiers_Book_Cover_CG with Dissolve( my_dissolve_02 )
    show Tube_Amplifiers_Book_Content_CG with Dissolve( my_dissolve_02 )
    
    "Какие-то тексты и схемы на пожелтевших от времени страницах. "
    "В которых я совершенно ничего не понимал."
    
    play sound "./sounds/sounds/Thick_Book_Fall.mp3"
    scene Evening_Kenji_Home_Pantry_Other_03 with Dissolve( my_dissolve_05 )
    
    "Я кинул книгу в лежащий на полу, пустой ящик. Первый блин комом, но разве меня это остановит? Как бы не так!"

    "Из разноцветной стопки книг, я выцепил другую, тоненькую книжку."
    
    image Pan_Stretching = "./images/cg/DAY_01/10a_Makoto's_Books/Pan_Stretching/Pan_Stretching.png"
    image Pan_Stretching_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Pan_Stretching"
    
    show Pan_Stretching_CG with Dissolve( my_dissolve_05 )
    
    "«Расширение панорамы с помощью лыжной мази»"
    "Я перечитал название несколько раз. Но похоже эта книга здесь оказалась случайно и не имела к электронике никакого отношения. "
    
    hide Pan_Stretching_CG with Dissolve( my_dissolve_05 )
    play sound "./sounds/sounds/Thin_Book_Fall.mp3"
    
    "Я не стал открывать её и сразу бросил в ящик."
    
    
    "Третья книга которая попалась мне на глаза не имела никакого названия."
    
    image KT315_Gondola_Cover = "./images/cg/DAY_01/10a_Makoto's_Books/KT315_Gondola/KT315_Gondola_Cover.png"
    image KT315_Gondola_Cover_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "KT315_Gondola_Cover"
    
    image KT315_Gondola_Content = "./images/cg/DAY_01/10a_Makoto's_Books/KT315_Gondola/KT315_Gondola_Content.png"
    image KT315_Gondola_Content_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "KT315_Gondola_Content"
    
    show KT315_Gondola_Cover_CG with Dissolve( my_dissolve_05 )
    
    "Что это вообще за ерунда?"
    "Я открыл её и перелистал."
    
    play sound "./sounds/sounds/Open_Book.mp3"
    hide KT315_Gondola_Cover_CG with Dissolve( my_dissolve_02 )
    show KT315_Gondola_Content_CG with Dissolve( my_dissolve_02 )
    
    "Это о чем вообще?"
    "Что за бред сумашедшего?"
    
    hide KT315_Gondola_Content_CG with Dissolve( my_dissolve_05 )
    
    kenji "Нет спасибо."

    play sound "./sounds/sounds/Thick_Book_Fall.mp3"
    "Сказал я в вполголоса и швырнул непонятную книгу вслед за остальными."
    
    image Electronics_For_Dummies_book_light = "./images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/book_light.png"
    
    play environment_sounds_dream "./sounds/sounds/Aah.mp3" fadein 1
    show black_image_alpha_50pc with Dissolve( my_dissolve_02 )
    show Electronics_For_Dummies_book_light with Dissolve( my_dissolve_02 )
    
    "И вот наконец!"
    
    show Electronics_For_Dummies with Dissolve( my_dissolve_05 )
    hide Electronics_For_Dummies_book_light with Dissolve( my_dissolve_02 )
    
    "То что надо! Яркая, глянцевая суперобложка и приятный аромат свежей типографии, а не замшелой бумаги. "
    "Название согревает сердце и душу: «Электроника. Пособие для слабоумных хиккикомори»!"
    "О да! Слезы радости заблестели на моих глазах..."
    
    
    play sound "./sounds/sounds/Aah_Stop_Tape.mp3" fadein 1
    stop environment_sounds_dream fadeout 1
    hide Electronics_For_Dummies with Dissolve( my_dissolve_02 )
    hide black_image_alpha_50pc with Dissolve( my_dissolve_02 )
    
    "Конечно нет. Не было у меня в руках такой книги. Здесь вообще нет книг. Только бесполезная макулатура! "
    "Зачем пишут эту отвратительную заумь и кто читает эту хрень? Неужели Касуми в этом море непонятной информации чувствует себя как рыба в воде? Как ей это удается?"
    "Может будь здесь хоть одна книга для новичков и я бы смог разобраться? Почему здесь только громоздкие, неподъемные для моего слабого мозга энциклопедии. "

    kenji "Интернет!"

    "Копаясь в куче дурацких книг, я напрочь забыл про интернет."
    "Я пулей бросился обратно в свою комнату."
    
    play environment_sounds "./sounds/environment/Bedroom.mp3" fadein 1 fadeout 1
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    kenji "Интернет! Интернет! Интернет!"

    "Радостно нашёптывал я, щёлкая по клавишам компьютера."
    "Мое сердце затрепетало, когда я увидел результаты поиска."

    "Я зашёл на страницу интернет магазина, продающего именно то что мне нужно: «Радиоэлектроника для начинающих». "
    
    image Electronics_For_Beginners_Manga_Cover = "./images/cg/DAY_01/10a_Makoto's_Books/Internet_Book/Electronics_For_Beginners_Manga_Cover.png"
    image Electronics_For_Beginners_Manga_Cover_CG:
        contains:
            "black_image"
            alpha 0.5
        
        contains:
            "Electronics_For_Beginners_Manga_Cover"
    
    show Electronics_For_Beginners_Manga_Cover_CG with Dissolve( my_dissolve_05 )
    
    "Да, таких книг сотни, но эта особенная — это был комикс. "
    "На обложке, мультяшная, жизнерадостная школьница с большими глазами приветливо махала мне руками. "
    "А вокруг неё все эти транзисторы, конденсаторы и ещё чёрт знает что. Вот что мне было нужно!"
    
    hide Electronics_For_Beginners_Manga_Cover_CG with Dissolve( my_dissolve_05 )

    "Я глянул на цену — пять тысяч йен. Да, дороговато"
    "Но ещё больше если с немедленной доставкой до дома - пятнадцать тысяч."
    "Но мне не жалко таких денег, эта книга должна была стать моей!"

    "Но увы, как только я перешёл к заказу, на сайте высветилась предательская, красная надпись. "
    "«Извините, но сейчас данный товар отсутствует, последний раз он был в наличии...». Я взглянул на дату — два года назад!"

    "Я обследовал другие интернет магазины, что выдал мне поисковик. Но тщетно. Нигде этой книги не было в наличии. "

    "Я прошерстил интернет, в попытке не купить, а скачать эту книгу, но и тут меня ожидала неудача."

    "Раздосадованный и опустошенный я выключил компьютер. На часах была половина первого. "
    "Я включил будильник в телефоне на десять, скинул с себя в верхнюю одежду и лёг в кровать."
    "Уснул я практически мгновенно."
    
    window hide
    
    play environment_sounds "./sounds/environment/Suburb_Night.mp3" fadein 1
    scene Night_Street_01 with Dissolve( my_dissolve_05 )
    
    pause 2.0
    
    image End_Splash_Logo_JP = im.Scale( "./images/other/logo_jp.png", 900, 506 )
    image End_Splash_Text = VBox(
        Text( "{b}{color=#FFE680}РадиоПульсар ПреДемо{/color}{/b}" ),
        #Text( "" ),
        Text( "{color=#FFE680}Сценарий:{/color} Дим Осторожно, Puankar, rurubell" ),
        Text( "{color=#FFE680}Картинки, код:{/color} rurubell" ),
        Text( "" ),
        Text( "{b}{color=#FFE680}Спасибо{/color}{/b}" ),
        Text( "{color=#FFE680}yakui-lover{/color} - за помощь с кодом" ),
        Text( "{color=#FFE680}noteblock, Russian J-12{/color} - за обсуждение сюжета и персонажей" ),
        Text( "{color=#FFE680}fOkusnik{/color} - за попытку всех переубедить" ),
        Text( "Пользователям имиджборд {color=#FFE680}2ch.hk{/color} и {color=#FFE680}iichan.hk{/color}" ),
        Text( "" ),
        Text( "Музыка и звуки взяты с сайтов {color=#FFE680}wav-library.net, download-sounds.ru, youtube.com{/color}" ),
        )
    
    image end_splash:
        contains:
            "empty_image"
        
        contains:
            xpos 50
            ypos 500
            "End_Splash_Text"
       
        contains:
            xpos 1000
            ypos 500
            "End_Splash_Logo_JP"
            alpha 0.4
    
    show end_splash with Dissolve( my_dissolve_05 )
    
    pause
    
    return
