init python:
    None


define kenji = Character( "Кендзи", color="#BBFF88" )
define aiko = Character( "Айко", color="#FF888B" )
define kasumi = Character( "Касуми", color="#88C0FF" )
define blind_girl = Character( "Девушка", color="#88C0FF" )
define vatanabe = Character( "Ватанабе", color="#009900" )
define zak = Character( "Заказчик", color="#FFC95C" )
define tv = Character( "Телевизор", color="#FFC95C" )



label start:
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
    
    
    #Спрайты
    #Айко в домашней одежде
    image Aiko_Base_Outfit_03_Normal_Say = im.Scale( "./images/sprites/Aiko/Aiko_Base_Outfit_03/Aiko_Base_Outfit_03_Normal_Say.png", 594, 900 ) 
    image Aiko_Base_Outfit_03_Normal_Silent = im.Scale( "./images/sprites/Aiko/Aiko_Base_Outfit_03/Aiko_Base_Outfit_03_Normal_Silent.png", 594, 900 ) 
    image Aiko_Base_Outfit_03_Confused_Silent = im.Scale( "./images/sprites/Aiko/Aiko_Base_Outfit_03/Aiko_Base_Outfit_03_Confused_Silent.png", 594, 900 ) 
    image Aiko_Base_Outfit_03_Angry_Say = im.Scale( "./images/sprites/Aiko/Aiko_Base_Outfit_03/Aiko_Base_Outfit_03_Angry_Say.png", 594, 900 ) 
    image Aiko_Base_Outfit_03_Angry_Silent = im.Scale( "./images/sprites/Aiko/Aiko_Base_Outfit_03/Aiko_Base_Outfit_03_Angry_Silent.png", 594, 900 )
    
    #Айко с ложкой
    image Aiko_With_Big_Spoon_Angry_Say = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Angry_Say.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Angry_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Angry_Silent.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Confused_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Confused_Silent.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Normal_Say = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Normal_Say.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Normal_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Normal_Silent.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Surprised_Say = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Surprised_Say.png", 880, 900 ) 
    image Aiko_With_Big_Spoon_Surprised_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Big_Spoon/Aiko_With_Big_Spoon_Surprised_Silent.png", 880, 900 ) 
    
    #Айко с пивом
    image Aiko_With_Beer_Irritated = im.Scale( "./images/sprites/Aiko/Aiko_With_Beer/Aiko_With_Beer_Irritated.png", 880, 900 ) 
    image Aiko_With_Beer_Normal_Say = im.Scale( "./images/sprites/Aiko/Aiko_With_Beer/Aiko_With_Beer_Normal_Say.png", 880, 900 ) 
    image Aiko_With_Beer_Normal_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Beer/Aiko_With_Beer_Normal_Silent.png", 880, 900 ) 
    image Aiko_With_Beer_Surprised_Say = im.Scale( "./images/sprites/Aiko/Aiko_With_Beer/Aiko_With_Beer_Surprised_Say.png", 880, 900 ) 
    image Aiko_With_Beer_Surprised_Silent = im.Scale( "./images/sprites/Aiko/Aiko_With_Beer/Aiko_With_Beer_Surprised_Silent.png", 880, 900 ) 
    
    #Айко в школьной одежде
    image Aiko_School_Uniform_01_Angry_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_01/Aiko_School_Uniform_Angry_Silent.png", 686, 900 ) 
    image Aiko_School_Uniform_01_Angry_Say = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_01/Aiko_School_Uniform_Angry_Say.png", 686, 900 ) 
    image Aiko_School_Uniform_01_Shy_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_01/Aiko_School_Uniform_01_Shy_Silent.png", 686, 900 ) 
    image Aiko_School_Uniform_02_Normal_Say = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Normal_Say.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Normal_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Normal_Silent.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Surprised_Say = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Surprised_Say.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Surprised_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Surprised_Silent.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Mocking_Say = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Mocking_Say.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Mocking_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Mocking_Silent.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Scared_Say = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Scared_Say.png", 587, 900 ) 
    image Aiko_School_Uniform_02_Scared_Silent = im.Scale( "./images/sprites/Aiko/Aiko_School_Uniform_02/Aiko_School_Uniform_02_Scared_Silent.png", 587, 900 ) 
    
    #Касуми в школьной форме 01
    image kasumi_01_Normal_Say = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Normal_Say.png", 646, 1000 ) 
    image kasumi_01_Normal_Silent = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Normal_Silent.png", 646, 1000 ) 
    image kasumi_01_Concerned_Say = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Concerned_Say.png", 646, 1000 ) 
    image kasumi_01_Concerned_Silent = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Concerned_Silent.png", 646, 1000 ) 
    image kasumi_01_Surprised_Say = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Surprised_Say.png", 646, 1000 ) 
    image kasumi_01_Surprised_Silent = im.Scale( "./images/sprites/Kasumi/Kasumi_01/kasumi_01_Surprised_Silent.png", 646, 1000 ) 
    
        
    #СЦЕНА - ДЕНЬ 1, МИДОРИ
    
    image midori_00 = "./images/cg/DAY_01/Green-Haired_Girl/00.png"
    image midori_01 = "./images/cg/DAY_01/Green-Haired_Girl/01.png"
    image midori_02 = "./images/cg/DAY_01/Green-Haired_Girl/02.png"
    image midori_03 = "./images/cg/DAY_01/Green-Haired_Girl/03.png"
    image midori_04 = "./images/cg/DAY_01/Green-Haired_Girl/04.png"
    image midori_05 = "./images/cg/DAY_01/Green-Haired_Girl/05.png"
    
    show Sea_Midori_Scene with dissolve
    
    "П-привет!"

    "Робко поздоровался я."

    "Меня Кендзи зовут. Танака Кендзи!"
    
    kenji "А тебя?"

    "Девушка не ответила. Впрочем я знал её имя. Звали её — Мидори. И она явно школьница, раз надела школьный купальник."
    "Наверное вырвалась со своими подружками на море, сейчас же лето, каникулы..."

    "На вид Мидори лет шестнадцать, не больше. А это - самый замечательный возраст! "
    "Будь мне сейчас столько лет, я бы с удовольствием побегал вместе с Мидори по морскому берегу."
    "Сыграл с ней в волейбол... Ух! "

    "Но к сожалению, мне уже давно не шестнадцать."

    kenji "Мне тридцать лет Мидори! Тридцать!"

    "Похоже, её совсем не смутили эти слова и она по-прежнему улыбалась мне."
    "Приободрившись я продолжил"

    kenji "А ещё я хиккикомори! Никчёмный тридцатилетний хиккикомори!"

    "Лицо Мидори не дрогнуло. Мне даже показалось что ее улыбка стала чуть добрее, а в глазах заплясали радостные искорки."

    kenji "Конечно Мидори! Будь я самым последним ублюдком на свете, ты бы ни за что не отвернулась от меня!"
    kenji "Я же для тебя самый дорогой человек на свете!"
    kenji "Я твой отец! "
    kenji "Даже больше! Я твой создатель!"
    
    kenji "И ты должна меня простить! Потому что я тебя... Продал!"

    "Мне показалось, или веселья на лице девушки поубавилось? Я поспешил её успокоить."

    kenji "Но ты не бойся! Я продал тебя очень хорошему человеку! Я надеюсь…"
    
    show midori_02 with dissolve
    hide Sea_Midori_Scene
    
    "Я потёр глаза и чуть отодвинулся от монитора. "
    "Да, Мидори вышла очень миленькой. Думаю человек, что заказал её — будет доволен."

    "Вдруг завибрировал телефон. Похоже что мне прислали сообщение! "
    "Писал тот парень что заказал рисунок с Мидори. Вовремя он появился!"

    zak "Йоу чувак!"
    kenji "Привет. Твой рисунок готов. Сейчас перешлю его."

    "Я отправил рисунок заказчику, и принялся ожидать его реакцию. "
    "Если честно, я всегда волнуюсь в такие моменты, хоть и занимаюсь этим уже не первый год."

    zak "Это шедевр чувак!"

    "Я самодовольно улыбнулся. "
    zak "Но..."

    "Черт! Похоже ему что-то не нравится! Неужели я где-то накосячил? Надеюсь он не хочет сбить цену, о которой мы договорились?"
    "Неужели ему больше не нужен этот заказ, и он не будет платить остальную сумму за рисунок? Я озвучил свой вопрос в чате."

    zak "Нет чувак! Не в этом дело! Я заплачу! Но понимаешь, наши с Мидори отношения..."
    zak "Кажется они перешли на новый уровень!"
    kenji "Ваши отношения?!"
    zak "Ага чувак… Раньше, она казалась мне такой чистой и непорочной..."
    zak "А сейчас, я все больше замечаю какая она женственная… Какая притягательная..."

    "О чем он вообще? Единственное чего мне хотелось сейчас — получить свои деньги."

    zak "Какая у нее тонкая шея… А её ямочки на ключицах… Ох..."

    "Похоже этот парень был не в себе. "

    zak "Чувак, ты можешь немного переделать рисунок?"
    kenji "Переделать? Но мы же все обсудили! Я показывал наброски!"
    zak "Я заплачу больше! Сколько ты скажешь! Но только измени его, совсем чуть-чуть!"

    "Я тяжело вздохнул. Опять эти капризы заказчика."

    kenji "И что мне переделать?"
    zak "Ты можешь сделать, чтобы Мидори на этом рисунке выглядела немного погорячее?"
    kenji "Погорячее?"
    zak "Ага! Сделай её немного похотливей что-ли..."
    kenji "Ты хочешь чтобы я раздел её?"
    zak "Нет чувак! Оставь купальник на месте! Так даже интереснее! Может выражение лица поменять?"
    zak "Ну чтобы сразу стало понятно чего она хочет!"

    "А мне казалось, что такой милой девочке как Мидори, хочется побегать со своими подружками по пляжу, без всякой задней мысли. "
    "Однако спорить с этим парнем я не стал. Он заказал Мидори, он её хозяин, а мне только одно остаётся — выполнить все его прихоти. "
    "Я попросил заказчика, чтобы он написал мне через полчаса, а сам принялся за рисунок."

    hide midori_02 with dissolve
    
    "..."
    
    show midori_03 with dissolve
    
    "Да, теперь определённо можно сказать, чего хочет Мидори. "
    "Вот только хочет ли она это в самом деле? Взяла ли Мидори, эту штуку в рот по своей воле, или я её заставил? "
    "Черт! Я слишком много об этом думаю! "
    "Я покачал головой и прошептал."

    kenji "Прости меня Мидори… Я не хотел..."

    zak "Эм… Рисунок отличный. Но Чувак, кажется я понял чего я действительно хочу!"
    kenji "Что опять?"
    zak "Я не мог понять чего я хочу конкретно! Но теперь знаю!" 
    zak "Ты можешь нарисовать ей ахегао личико?"

    "Ну по крайней мере, теперь он точно знал чего хочет. "
    "К несчастью для меня, лицо Мидори опять нуждалось в серьёзной редактуре."
    
    kenji "Надеюсь это все?"
    zak "Всё чувак! Просто сделай ей ахегао личико, и я заплачу сколько ты скажешь."
    
    hide midori_03 with dissolve
    
    "..."
    
    show midori_04 with dissolve
    
    "Пока я перерисовывал физиономию девушки, на душе у меня становилось все гаже. "
    "Я столько времени потратил на первоначальный рисунок, столько труда в него вложил! "
    "Да я почти сроднился с Мидори!"
    "А сейчас мне приходится издеваться над собственным творением ради этого похотливого болвана!"

    "Надо было просто надавить на этого парня и забрать свои деньги. "
    "Пусть несёт рисунок на доработку другому художнику. "
    "Или поступить как истинный джентльмен, и вообще не отдавать ему Мидори. "
    "Ахегао личико, ишь чего захотел! "
    "Эх… Ну почему я такой мягкотелый?"

    "Но ещё хуже было то, что этот парень вновь был чем-то недоволен."

    zak "Чувак… Можешь добавить ещё кое что?"
    kenji "Я нарисовал все что ты хотел, разве нет? Я не могу переделывать этот рисунок вечно!"
    zak "Я знаю чувак! И я перевёл деньги! Ты клевый художник, но пожалуйста доделай этот рисунок."
    zak "Осталось совсем чуть-чуть до совершенства!"

    "Я поспешил проверить состояние своего счета. "
    "А он щедр! Парень заплатил за мою работу в два раза больше оговоренного! "
    "Мне даже стало стыдно, за то, что я так плохо думал о нем."

    zak "Это не займёт много времени. Одна маленькая деталь."
    zak "Я уверен, такому мастеру как ты - это ничего не стоит!"
    kenji "Ну хорошо! Говори, я сделаю!" 

    "Однако, увидев новую порцию пожеланий заказчика, я нервно сглотнул."
    
    hide midori_04 with dissolve
    
    "..."
    
    show midori_05 with dissolve
    
    "Действительно. Времени потребовалось совсем чуть-чуть. Хотя не припомню, чтобы я рисовал такое раньше. "
    "Мидори теперь была по настоящему испорчена. Она была осквернена, окончательно и бесповоротно. "
    "И я сделал это собственными руками!"

    "Я не смотрел этого, популярного сейчас аниме-сериала, где эта девчонка — одна из главных героинь. "
    "Наверняка она там учится на одни пятёрки, и вообще — всем ребятам пример! "
    "Президент кружка чайных церемоний, или кулинарии. Может даже волонтёр в местном храме. "
    "А ведь это героиня популярного сейчас аниме сериала. Я его конечно не смотрел, но подозреваю, что там она отличница, президент кружка чайных церемоний, волонтер в местном храме и вообще — всем ребятам пример!"
    "Если бы она только знала, какую гадость с ней сделал такой никчёмный человек как я..."

    #СЦЕНА - ДЕНЬ 1, АЙКО ЗАХОДИТ В КОНМНАТУ КЕНДЗИ И ВИДИТ МИДОРИ

    "Кендзи!"
    
    scene Day_Kenji_Home_Bedroom with dissolve
    
    "Я настолько ушел в свои мысли что не сразу сообразил - меня зовут."
    
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
    
    show Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( 0.2 )
    ##
    
    show Aiko_Base_Outfit_03_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    "В дверях стояла Айко, моя младшая сестра."
    "Ой! Кажется она уставилась в мой монитор!"
    "Я повернулся обратно к монитору. Там как и раньше красовалась Мидори, над которой я сегодня как следует поиздевался."
    "Черт! Я бы ни за что не стал, добровольно демонстрировать такое творчество своей младшей сестре! Как не вовремя она зашла! "
    "Я молниеносно закрыл программу для рисования. А после, вновь повернулся к Айко."
    
    show Aiko_Base_Outfit_03_Confused_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_Base_Outfit_03_Normal_Silent
    
    "Похоже Айко успела разглядеть Мидори."
    "На несколько секунд повисла неловкая пауза, но затем моя сестра пришла в себя и тихо сказала."
    
    show Aiko_Base_Outfit_03_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_Base_Outfit_03_Confused_Silent
    
    aiko "Завтрак готов."
    
    show Aiko_Base_Outfit_03_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_Base_Outfit_03_Normal_Say
    
    "Посмотрела на меня, нахмурилась и выпалила."
    
    show Aiko_Base_Outfit_03_Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_Base_Outfit_03_Normal_Silent
    
    aiko "Только надень на себя хоть что-то!"
    
    show Aiko_Base_Outfit_03_Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_Base_Outfit_03_Angry_Say
    
    "Только сейчас я осознал что сижу в кресле в одних трусах."
    "Пока я разглядывал себя и своё нижнее белье, Айко исчезла."
    
    hide Aiko_Base_Outfit_03_Angry_Silent with Dissolve( 0.1 )
    hide Day_Kenji_Bedroom_Door_With_Border_01 with dissolve
    
    "Не стоило злить свою сестру и опаздывать. Я встал, накинул рубашку, застегнул её через пуговицу."
    "Когда с рубашкой было покончено, я натянул брюки, и пытаясь застегнуть тугую ширинку, сделал несколько шагов по комнате."
    
    #СЦЕНА - ДЕНЬ 1, ЗАВТРАК С АЙКО
    
    "Спустился по лестнице и вот я уже в большом холле, который к тому же выполняет роль кухни и столовой."
    
    image Day_Kenji_Home_Kitchen_Other = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Other.jpg"
    image Day_Kenji_Home_Kitchen_Mask = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Mask.png"
    scene Day_Kenji_Home_Kitchen_Other with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Kitchen_Mask", At( "dust", center )) as mask
    

    kenji "И что сегодня на завтрак?"
    
    show Aiko_Base_Outfit_03_Normal_Say with Dissolve( 0.2 )
    
    aiko "На завтрак — мисо-суп, рис и омлет."
    
    show Aiko_Base_Outfit_03_Normal_Silent with Dissolve( 0.2 )
    hide Aiko_Base_Outfit_03_Normal_Say
    
    "Я сел за стол. Айко же, протёрла его влажной тряпкой. "
    "Поставила на него две деревянные подставки. Протерла их. "
    "Затем аккуратно расставила передо мной тарелки, положила палочки для еды. Все в лучшем виде. "
    
    image Kenji_1st_Day_Breakfast_Food = "./images/cg/DAY_01/Kenji_1st_Day_Breakfast/Food.png"
    scene Kenji_1st_Day_Breakfast_Food with dissolve
    
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
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    ##
    
    show Aiko_With_Big_Spoon_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    aiko "Папа и мама звонили."
    
    show Aiko_With_Big_Spoon_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Normal_Say
    
    "Меня от этой новости немного передёрнуло, отца я побаивался. "
    "Но, последнюю неделю я вёл себя хорошо, не думаю что Айко могла про меня наябедничать. "
    "Я ждал, что Айко скажет что-то еще, но она не стала продолжать. Значит — все нормально!"
    
    hide Aiko_With_Big_Spoon_Normal_Silent with Dissolve( 0.1 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    
    "Довольно странно, что Айко так просто называла моего отца «папой»."
    "Дело в том, что Айко не была его родной дочкой. "
    "Отец, шесть лет назад женился на вдове, Макото Асуке. С тех пор у меня появилась сестра и новая мама, хотя я предпочитал называть её «тётя Асука». "
    "Вскоре после этого, отцу предложили новую работу в центре города, и жить в захолустном пригороде ему стало крайне неудобно."
    "Они с тетей перебрались в новую квартиру, оставив прежнее жилье в моем полном распоряжении."

    "Моя новая сестра осталась тоже."
    "Говорила — что не хочет менять школу и расставаться со школьными подружками. Я ожидал что она уедет после перехода в среднюю школу, но этого не случилось. "
    "Возможно, потому, что она стала чувствовать себя лишней. Ведь у отца и тёти Асуки появился совместный ребёнок, а у нас с Айко — младший брат. "
    "Впрочем точной причины я не знаю, да и знать не желаю. И я бы сам не хотел, чтобы Айко уезжала, от неё много пользы. "
    "Она неплохо готовит, и за домом следит. Ей даже не лень выращивать цветы в палисаднике и стричь кусты под окнами. "
    "С другой стороны — чуть что не так, она всегда готова нажаловаться на меня родителям. Приходится быть паинькой."

    "Я потянул руки, чтобы взять палочки для еды, но тут моё внимание отвлёк работающий телевизор. "
    "Оттуда раздавалось частое дыхание. "
    
    show Kenji_1st_Day_Breakfast_TV_Strange_Movie with moveinleft
    
    "На экране какой-то тип держал за плечи худенькую девушку в школьной форме. Видимо он пытался её поцеловать."
    "Та, дрожа, издала жалобный писк."
    
    tv "С-сэмпай!"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    show Aiko_With_Big_Spoon_Confused_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    "Я перевёл взгляд на сестру. Что за дурацкий канал она врубила с утра пораньше? "
    "Айко была сильно смущена и стояла как истукан с крышкой от кастрюли и черпаком в руках."
    
    hide Aiko_With_Big_Spoon_Confused_Silent with Dissolve( 0.1 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    
    "Хвала богам, пульт лежал на столе и через мгновение был у меня в руках."
    "Я перебирал каналы, пока не нашёл что-то наиболее нейтральное. "
    
    show Kenji_1st_Day_Breakfast_TV_News with dissolve
    hide Kenji_1st_Day_Breakfast_TV_Strange_Movie
    
    "Новости."
    "Выпуск в самом разгаре, обсуждают ближнее зарубежье. Китай, Корея, США. Отлично, самое оно! "
    
    hide Kenji_1st_Day_Breakfast_TV_News with moveoutleft
    
    "Я вновь взялся за палочки для еды, но вдруг Айко остановила меня."
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    show Aiko_With_Big_Spoon_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    aiko "Ты не забыл?"
    
    show Aiko_With_Big_Spoon_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Normal_Say
    
    kenji "Не забыл «что»?"
    
    show Aiko_With_Big_Spoon_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Normal_Silent
    
    aiko "Сегодня четверг, день вывоза электронных приборов. Мама же просила освободить кладовку!"
    
    hide Aiko_With_Big_Spoon_Normal_Say with Dissolve( 0.1 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    
    "Черт! Я помнил про это вчера, но с утра конечно позабыл все на свете."
    "Вот бы еще и Айко забыла! "
    "Барахла в кладовке превеликое множество. Столько работы! Хорошо если за день управлюсь. "
    "Конечно, никто никуда не спешит. Отец и тётя Асука приедут ещё очень не скоро. Если вообще, навестят нас до конца лета. "
    "Поэтому со спокойной совестью можно отмахнуться от забот сегодня, и поднажать в следующий четверг. "
    "Но если вдруг позвонит отец. Не очень хочется слушать его нравоучения. А Айко меня сдаст наверняка."

    "Я отложил палочки для еды в сторону."
    
    kenji "Айко! Ты ещё не налила себе порцию?"
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    show Aiko_With_Big_Spoon_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    aiko "Что? Нет. Но собираюсь."
    
    show Aiko_With_Big_Spoon_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Normal_Say
    
    kenji "Возьми мою, я суп не буду!"
    
    show Aiko_With_Big_Spoon_Surprised_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Normal_Silent
    
    aiko "Это ещё почему?"
    
    show Aiko_With_Big_Spoon_Surprised_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Surprised_Say
    
    "Не то, чтобы я вдруг внезапно перестал быть голодным. Но мне требовалось оставить место в желудке для кое-чего другого."
    
    kenji "Мне салата хватит! А вместо супа, достань ка мне из холодильника баночку пива! Там же ещё осталось?"
    
    show Aiko_With_Big_Spoon_Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Surprised_Silent
    
    aiko "Пиво! С утра?!"
    
    show Aiko_With_Big_Spoon_Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Angry_Say
    
    kenji "А что такого?"
    
    show Aiko_With_Big_Spoon_Angry_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Angry_Silent
    
    aiko "Нет, ничего! Суп ты теперь вообще есть не будешь? Может мне тогда начать варить пиво для тебя?"
    
    show Aiko_With_Big_Spoon_Angry_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_With_Big_Spoon_Angry_Say
    
    "Айко была крайне возмущёна."
    
    kenji "Остынь Айко. Мне надо, понимаешь? Это как лекарство. Я же на улицу пойду. А там люди кругом. Это мне для храбрости!"
    
    hide Aiko_With_Big_Spoon_Angry_Silent with Dissolve( 0.1 )
    hide Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( 0.2 )
    
    "Конечно Айко не понять меня. "
    "Но мне — тридцатилетнему затворнику, проводящему дни и ночи за компьютером, известно насколько это тяжело встречать по дороге соседей и знакомых, и хриплым голосом желать им доброго дня. "
    "Если я выпью немного алкоголя, дела пойдут гораздо веселее."

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
    
    show Day_Kenji_Home_Kitchen_Fridge_With_Border_01 with Dissolve( 0.2 )
    show Aiko_With_Beer_Normal_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 ) 
    
    aiko "Ну, какое тебе?"
    
    show Aiko_With_Beer_Normal_Silent at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 ) 
    hide Aiko_With_Beer_Normal_Say
    
    kenji "Да оно же одинаковое, любое!"
    
    show Aiko_With_Beer_Surprised_Say at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 ) 
    hide Aiko_With_Beer_Normal_Silent
    
    aiko "Ты чего думаешь, я в сортах пива — спец?"
    
    show Aiko_With_Beer_Irritated at Move( ( 1600, 620 ), ( 1600, 620 ), 0.0, xanchor="center", yanchor="center") with dissolve
    hide Aiko_With_Beer_Surprised_Say
    
    "Айко взяла из холодильника одну из банок. Мне показалось, что сейчас она небрежно кинет банку мне, настолько недовольное было у неё лицо. "
    
    image Kenji_1st_Day_Breakfast_Food_With_Beer = "./images/cg/DAY_01/Kenji_1st_Day_Breakfast/Food_With_Beer.png" 
    scene Kenji_1st_Day_Breakfast_Food_With_Beer with dissolve
    
    "Но нет, она поставила пиво на подставку, забрала мою порцию супа и села напротив."
    "Я взял в руки банку, и дёрнул за открывашку. "
    "Затем я схватил розовую таблеточку, запихнул её в рот и запил пивом. "
    "Увидев это, Айко изобразила гримасу неодобрения, но промолчала, и принялась за еду. "
    "Я тоже не медлил и торопливо потягивал пиво из банки, закусывая салатом. "
    "Есть я старался быстро, но и аккуратно чтобы не испачкать стол и не раздосадовать Айко снова."
    
    scene Day_Kenji_Home_Kitchen_Other with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Kitchen_Mask", At( "dust", center )) as mask
    
    "Когда банка опустела, я почувствовал, что достиг нужной кондиции и двинулся к кладовке."
    "Пора приниматься за дело!"
    
    #СЦЕНА - ДЕНЬ 1, ВЫНОС МУСОРА 
    
    image Day_Kenji_Home_Pantry_Mask = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Mask.png"
    image Day_Kenji_Home_Pantry_Other_00 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_00.jpg"
    image Day_Kenji_Home_Pantry_Other_01 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_01.jpg"
    image Day_Kenji_Home_Pantry_Other_02 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_02.jpg"
    image Day_Kenji_Home_Pantry_Other_03 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_03.jpg"
    
    scene Day_Kenji_Home_Pantry_Other_00 with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Pantry_Mask", At( "dust", center )) as mask
    
    "Всю левую половину кладовки, занимал стеллаж, который тётя Асука планировала освободить и устроить здесь гардероб. "
    "Не знаю, зачем ей это вдруг понадобилось, учитывая, что в доме она не живет несколько лет."
    "Но спорить с ней не хотелось. Барахлу, что лежит на этих полках, действительно, давно место на свалке."

    "А может быть причина не в этом? Не нужен ей никакой гардероб, а хочется тете Асуке избавиться от вещей навевающих неприятные воспоминания? "
    "Дело в том, что всё лежащее на полках некогда принадлежало её бывшему мужу, Макото Кайоши."

    "Макото-сан умер десять лет назад. А точнее — погиб. Он был радиолюбителем, или как это называется? "
    "Сидел вечерами в радиоэфире и болтал с другими, такими же «чокнутыми», как назвала их тётя Асука. "
    "Она вспоминала что ее муж мог просиживать в своей комнате часами и выбегать с радостными криками, в моменты когда ему удавалось принять сигнал совершенно незнакомых ему людей. "
    "Иногда даже от иностранцев."

    "Как это похоже на меня! Я тоже часами сижу за компьютером. "
    "И если вдруг мне напишет какой иностранец, с предложением нарисовать что-то для него или просто с похвалой моей галереи. "
    "Я наверняка буду как Макото-сан, бегать и голосить на весь дом о таком успехе."

    "Еще Макото-сан тратил много денег на оборудование. Чего конечно не одобряла тётя Асука. "
    "В общем как это обычно и бывает - жена не особо была рада увлечениям мужа. "
    "Айко на все это отцовское барахло тоже похоже наплевать. Она совсем его не помнит. "
    "Ну да, фотографий в альбоме и урны с прахом на местном кладбище ей достаточно. Кому нужна груда металлолома?"
    
    image TV_Heap = "images/cg/DAY_01/Kenji_Moves_Trash/TV_Heap/TV_Heap.png"
    image TV_Heap_Dream:
        contains:
            "TV_Heap"
        contains:
            "Dream_Frame"
            
    scene TV_Heap_Dream with dissolve
    
    "Однажды в детстве я проходил с отцом мимо площадки для сбора мусора. Там возвышалась грандиозная пирамида из телевизоров всех форм и размеров."
    "«Дядя Сато помер, телемастер» - пояснил мне отец. "
    "Потом мы с мальчишками устроили настоящую бойню. Расстреляли всю эту кучу камнями, пока не разбили каждый телек вдребезги."
    "Нам конечно здорово влетело, а на асфальте в том месте ещё несколько лет поблескивали кристаллики стекла."
    
    scene Day_Kenji_Home_Pantry_Other_00 with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Pantry_Mask", At( "dust", center )) as mask
    
    "Тогда нам было весело, а мне, сейчас, не очень. Умер человек — и вся его жизнь оказалась на свалке. "
    "Чтобы напоследок, люди по этим вещам могли определить, кто же «помер» в этот раз. Сегодня, выносить чью-то жизнь на помойку предстояло мне."
    
    "О том как погиб муж тёти Асуки мне рассказал дядя Ватанабэ, который жил с нами на одной улице. "
    "Он был другом дяди Макото, и в прошлом, тоже - радиолюбителем."
    
    image Evening_Watanabe_Bike_WorkShop = "./images/bg/Outdoor/Watanabe_Bike_WorkShop/Evening/Watanabe_Bike_WorkShop.png"
    image Evening_Watanabe_Bike_WorkShop_Dream:
        contains:
            "Evening_Watanabe_Bike_WorkShop"
        contains:
            "Dream_Frame"
    
    scene Evening_Watanabe_Bike_WorkShop_Dream with dissolve
    
    image Watanabe_01_Normal_Say = im.Scale( "./images/sprites/Watanabe/Watanabe_01_Normal_Say.png", 622, 1080 )
    image Watanabe_01_Normal_Silent = im.Scale( "./images/sprites/Watanabe/Watanabe_01_Normal_Silent.png", 622, 1080 )
    
    show Watanabe_01_Normal_Say with Dissolve( 0.1 )
    
    vatanabe "Он хотел сделать антенну. Из провода высоковольтной линии что проходит в саду."

    show Watanabe_01_Normal_Silent with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Say
    
    kenji "Он упал с нее?"
    
    show Watanabe_01_Normal_Say with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Silent

    vatanabe "Да нет. Прихлопнуло его, когда свою антенну на фазу забрасывал."
    vatanabe "Если бы упал, тогда, выжил бы, наверное. А так... Руки у него до костей обгорели."
    
    show Watanabe_01_Normal_Silent with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Say

    "Я не поверил. Подсоединить свою антенну к проводу под большим напряжением — это дикость! "

    kenji "Это больше похоже на самоубийство!"
    
    show Watanabe_01_Normal_Say with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Silent
    
    vatanabe "Да что ты! Там всего тридцать пять тысяч вольт, это немного."
    
    show Watanabe_01_Normal_Silent with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Say

    "Немного?! Мне эта цифра показалась неправдоподобно большой. «Всего» тридцать пять тысяч вольт! "
    
    show Watanabe_01_Normal_Say with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Silent

    vatanabe "Если бы у меня была такая возможность, я бы тоже набросил. А Кайоши, не рассчитал чего-то."
    vatanabe "Может конденсаторы плохие ему попались, или ещё чего..."
    vatanabe "Ты не подумай, Кендзи. Мы не сумасшедшие и не самоубийцы. Хотя конечно, авантюра очень рискованная."
    vatanabe "Меня тоже один раз шандарахнуло, но, слава богу — выжил."
    
    show Watanabe_01_Normal_Silent with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Say
    
    kenji "Тоже «набросили»?"

    "Дядя Ватанабэ улыбнулся."
    
    show Watanabe_01_Normal_Say with Dissolve( 0.2 )
    hide Watanabe_01_Normal_Silent

    vatanabe "Да нет! На работе. Я же электрик по призванию. Но там ничего интересного, совершенно бытовая ситуация"
    vatanabe "С тех пор пальцы на правой руке еле двигаются. И вообще, что-то вроде контузии получил. "
    vatanabe "Полгода ходил как пришибленный. Инвалидом стал и вышел досрочно на пенсию."
    vatanabe "Приходится подрабатывать автомехаником теперь. "
    vatanabe "Эх, и как он только умудрился сжечь сцепление? А? Кендзи? Ты не знаешь?"
    
    scene Day_Kenji_Home_Pantry_Other_00 with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Pantry_Mask", At( "dust", center )) as mask
    
    "Я тряхнул головой отгоняя воспоминания. "
    "Что-то залип. Пора и за работу!  "
    "Я решил сразу взяться за самое трудное — два металлических «чемоданчика», покрытые жёлтой эмалью. "
    "То что они из металла — видно по потёртым краям, где из-под краски выглядывала потемневшая сталь. "
    "Причём металл достойной толщины - судя по весу каждого. Один был значительно тяжелее другого, на его передней панели красовались чёрные стрелочные приборы, да несколько тумблеров. "
    "Второй — легче. Но его приборная панель была закрыта крышкой, с замками как на армейской фляге. "
    "Для начала унесу тот, что легче — это будет разминка."
    
    scene Outdoor_Day_Kenji_Home with dissolve
    
    "На улице был типичный июньский полдень. Ужасно яркое солнце, голубое небо и белоснежные облака. Все как обычно. "
    "Дождей за последнюю неделю не наблюдалось и к зною добавился стойкий запах пыли, который перебивал теперь аромат цветов и прочей зелени. "
    "Было тихо — это радовало, мне ни к чему лишние свидетели."
    
    scene Outdoor_Day_Street_03 with dissolve
    
    "Я вышел за ограду и принялся за упражнения со своим новеньким, жёлтеньким и увесистым снарядом. "
    "Поставил его ребром на плечо — острый край пребольно врезался в шею. "
    "Попробовал нести его под мышкой — и тут не вышло, рука моментально вспотела и «чемоданчик» норовил выскользнуть из рук. "
    "Я схватил его обеими руками и понёс, прижимая к груди, но и так было не очень сподручно. "
    
    scene Outdoor_Day_BG_With_Railroad_2 with dissolve
    
    "Пройдя один квартал я сменил тактику, и решил взять свой снаряд за его родные, заводские ручки — покрытые каким-то плотным, зелёным материалом. "
    "Постепенно стали ныть плечи и спина, а также зудеть нога в том месте где она тёрлась о край прибора."
    
    scene Day_Trash_Place with dissolve
    
    "Последние несколько метров я буквально волочил «чемоданчик» по асфальту оставляя блестящий след с чешуйками жёлтой краски. "
    "Похоже я сегодня был первым посетителем. Никакой электроники до меня никто не выбросил. Площадка для мусора была пуста"
    "Теперь здесь лежал только мой прибор."
    "Я пнул его напоследок и отправился домой."
    "На обратном пути мне так же никто не встретился - довольно удачный выдался денёк! "
    
    scene Day_Kenji_Home_Kitchen_Other with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Kitchen_Mask", At( "dust", center )) as mask 
    
    "Я ворвался в дом, распахнул холодильник и немедленно выпил холодного пива. Ох, похоже пол банки выдул за несколько глотков! "
    
    show Aiko_School_Uniform_01_Angry_Silent with Dissolve( 0.2 )
    
    "Айко была на кухне. Глядя на меня она нахмурилась, но ничего не сказала. "
    "Я же улыбнулся во весь рот и продемонстрировал сестре оттопыренный вверх большой палец. "
    
    show Aiko_School_Uniform_01_Shy_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_01_Angry_Silent
    
    "От моего жеста она почему-то смутилась, а я только теперь заметил, что на ней надета летняя школьная форма."
    
    kenji "Ты что, в школу собралась? Разве не каникулы?"
    
    show Aiko_School_Uniform_02_Normal_Say with Dissolve( 0.2 )
    hide Aiko_School_Uniform_01_Shy_Silent with Dissolve( 0.1 )
    
    aiko "Каникулы! Но я иду в школьный бассейн."
    
    show Aiko_School_Uniform_02_Normal_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Say
    
    "Бассейн! Я вспомнил о том, что на земле существуют такие замечательные места. Ах! Я бы сейчас с удовольствием окунулся в прохладную водичку. "
    "И плевать что там народу как сельдей в бочке. Настроение у меня теперь самое располагающее, никакой невроз от тесного общения с людьми не страшен. "
    "Правда в таком состоянии, в общественный бассейн меня не пустят. Я вздохнул и отглотнул еще пива."
    
    show Aiko_School_Uniform_02_Normal_Say with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Silent
    
    aiko "Чего вздыхаешь?"
    
    show Aiko_School_Uniform_02_Normal_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Say
    
    kenji "Разве не понятно? В такую то жару в бассейне поплавать в самый раз!"
    
    show Aiko_School_Uniform_02_Surprised_Say with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Silent
    
    aiko "В нашем школьном?"
    
    show Aiko_School_Uniform_02_Surprised_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Surprised_Say
    
    kenji "Да какая разница. Но сама понимаешь, народа там — тьма."
    
    show Aiko_School_Uniform_02_Normal_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Surprised_Silent
    
    "Айко пожала плечами, и стала чуть серьёзнее. Она знала, чего я боюсь."
    
    show Aiko_School_Uniform_02_Normal_Say with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Silent

    aiko "Можешь съездить к морю. Где-то да найдёшь пустынный пляж."
    
    show Aiko_School_Uniform_02_Normal_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Say
    
    kenji "К морю... да... Но тогда придётся трястись в поезде час или два. В переполненном поезде, Айко!"
    
    show Aiko_School_Uniform_02_Mocking_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Normal_Silent
    
    "На лице Айко появилась ухмылка."
    
    show Aiko_School_Uniform_02_Mocking_Say with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Mocking_Silent
    
    aiko "Ты же принял «лекарство»."
    
    show Aiko_School_Uniform_02_Mocking_Silent with Dissolve( 0.2 )
    hide Aiko_School_Uniform_02_Mocking_Say
    
    kenji "С этим лекарством, сама понимаешь, в воду лезть не стоит. Тем более — в одиночку."
    
    hide Aiko_School_Uniform_02_Mocking_Silent with Dissolve( 0.1 )
    show Aiko_School_Uniform_02_Normal_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    
    "Айко опять пожала плечами и направилась к выходу. Дескать — не мои проблемы."
    
    kenji "Постой Айко! А может быть, завтра, вместе съездим на море? И там найдём этот самый «пустынный» пляж? Я не могу один, вдруг я начну тонуть?"
    
    show Aiko_School_Uniform_02_Surprised_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_02_Normal_Silent
    
    aiko "Думаешь я тебя спасу?"
    
    show Aiko_School_Uniform_02_Surprised_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_02_Surprised_Say
    
    kenji "Ты же член плавательного кружка!"
    
    show Aiko_School_Uniform_01_Angry_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_02_Surprised_Silent
    
    aiko "А ты опять напьёшься?"
    
    show Aiko_School_Uniform_01_Angry_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_01_Angry_Say
    
    kenji "Что значит опять? Это же не ради удовольствия, Айко!"
    
    show Aiko_School_Uniform_01_Angry_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_01_Surprised_Silent
    
    aiko "В таком случае - даже не мечтай!"
    
    show Aiko_School_Uniform_01_Angry_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_01_Angry_Say
    
    kenji "Ну... Айко! Хочешь? Я встану на колени перед тобой, хочешь?"
    
    show Aiko_School_Uniform_02_Scared_Silent at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_01_Angry_Silent
    
    "По лицу Айко пробежала гримасса испуга и отвращения."
    
    show Aiko_School_Uniform_02_Scared_Say at Move( ( 400, 620 ), ( 400, 620 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    hide Aiko_School_Uniform_02_Scared_Silent 
    
    aiko "НЕТ!"
    aiko "То есть да. Уговорил! Завтра поедем, но только без этого!"
    
    hide Aiko_School_Uniform_02_Scared_Say with Dissolve( 0.1 )
    
    "Айко в мгновение ока натянула свои сандалии и исчезла в дверях."
    
    "Как же мне повезло с сестренкой! Мысль о предстоящем отдыхе подбодрила меня и я с энтузиазмом вернулся к работе."
    
    scene Day_Trash_Place with dissolve
    
    #Мини-ЦГ вентилятор Касуми 01
    image Kasumi_Fan_01 = "./images/cg/DAY_01/Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_01.png"
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
    
    show Kasumi_Fan_01_With_Border_01 with Dissolve( 0.2 )
    
    "За время моего отсутствия на площадке появился напольный вентилятор с синими, разлохмаченными от старости лопастями и пожелтевшим пластиком корпуса. "
    
    #Мини ЦГ - рация на асфальте, с откинутой крышкой
    image Radio_Set_On_Ground = "/images/cg/DAY_01/Kenji_Moves_Trash/Radio_Set_On_Ground/Radio_Set_On_Ground.png"
    image Radio_Set_On_Ground_Moved:
        contains:
            "Radio_Set_On_Ground"
            xpos 400
            pause 0.7
            linear 5.0 xpos 750
    
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
    
    show Radio_Set_On_Ground_With_Border_01 with dissolve
    
    "А «мой чемоданчик» похоже был рад знакомству, он приветливо снял шляпу!"
    "Не знаю зачем это кому-то понадобилось, но крышка на нем была вскрыта. "
    
    hide Kasumi_Fan_01_With_Border_01 with Dissolve( 0.1 )
    
    "Под ней оказалась сложная приборная панель — десятки всевозможных крутилок, тумблеров, циферблатов со стрелками и хитрых разъёмов. "
    "Наверное кому-то стало интересно что же такое я сюда притащил. "
    "Хм. Возможно этот кто-то — владелец сломанного вентилятора. Я подошёл к нему поближе. "
    
    #Мини-ЦГ вентилятор Касуми 02
    image Kasumi_Fan_02 = "./images/cg/DAY_01/Kenji_Moves_Trash/Kasumi_Fan/Kasumi_Fan_02.png"
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
    
    hide Radio_Set_On_Ground_With_Border_01 with Dissolve( 0.2 )
    show Kasumi_Fan_02_With_Border_01 with Dissolve( 0.2 )
    
    "Обычный вентилятор, видно что старый, наверняка ему лет двадцать, не меньше. Сейчас таких не делают. Сквозь запах пыльной улицы, моё обоняние уловило «аромат» горелого пластика и сигарет. "
    "Да и весь этот жёлтый налёт на нем, явно сигаретная копоть, налипшая за годы эксплуатации. "
    "Стало немного противно, и в то же время в памяти всколыхнулись воспоминания былых лет."
    
    image smocking_old_man = "./images/cg/DAY_01/Kenji_Moves_Trash/Old_Smocking_Man/smocking_old_man.png"
    image smocking_old_man_dream:
        contains:
            "smocking_old_man"
        contains:
            "Dream_Frame"
    
    scene smocking_old_man_dream with dissolve
    
    "Я вспомнил своего, давно умершего деда, который всю жизнь смолил какие-то американские сигареты. "
    "Весь его дом, и каждая вещь в нем накрепко пропитались застарелым запахом сигаретного дыма."
    
    scene Day_Trash_Place with dissolve
    
    "Я подумал о том, что наверняка, столь активные курильщики — болеют какими-то заболеваниями. "
    "Например Туберкулёз — неприятная и очень заразная болезнь, я слышал о такой. "
    "Я отшагнул подальше от вентилятора и посмотрел на свою левую ладонь."
    
    "Ею я только что прикасался к прибору, принесенному ранее, а до меня его, похоже, трогал чужак. "
    "Вот будет весело, если такой домосед как я, подцепит редкую и смертельную болезнь! А точнее, совсем не весело!"
    "Я поспешил домой. Надо скорее вымыть руки!"
    
    scene Day_Kenji_Home_Pantry_Other_01 with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Pantry_Mask", At( "dust", center )) as mask
    
    "В свой третий поход до мусорки я взял два стареньких радиоприёмника, хотя они были довольно громоздкие — но в то же время совсем не тяжёлые."
    
    scene Day_Kenji_Home_Pantry_Other_02 with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Pantry_Mask", At( "dust", center )) as mask

    kenji "Остальное, думаю, можно оставить и на потом"
    kenji "За день сделано достаточно! Пожалуй еще одну вещь и довольно!"
    
    "Тяжёлого собрата жёлтого чемоданчика, я решил вынести сегодня во что бы то не стало. "
    "А между тем, вторая банка пива подошла к концу. Я сходил на кухню и взял последнюю. Открывать её не стал — положил в карман брюк. "
    "В последнем и самом тяжелом походе мне понадобятся обе руки!"
    
    scene Day_Trash_Place with dissolve
    
    "Поход был действительно трудный! "
    "Когда я наконец дотащил свою ношу до места — у меня ужасно ныли плечи и спина, а в мокрые от пота ладони врезался узор тканевых ручек. "
    
    
    #Мини ЦГ - БП от рации на земле
    image Radio_Set_Power_Supply_On_ground = "./images/cg/DAY_01/Kenji_Moves_Trash/Radio_Set_Power_supply_On_Ground/Radio_Set_Power_Supply_On_ground.png"
    image Radio_Set_Power_Supply_On_ground_Moved:
        contains:
            "Radio_Set_Power_Supply_On_ground"
            xpos 400
            pause 0.7
            linear 5.0 xpos 900
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Radio_Set_Power_Supply_On_ground_Masked = AlphaMask( "Radio_Set_Power_Supply_On_ground_Moved", "border_01_right_mask_moved" )
    
    image Radio_Set_Power_Supply_On_ground_With_Border_01:
        contains:
            "Radio_Set_Power_Supply_On_ground_Masked"
        contains:
            "border_01_right_moved"
    
    show Radio_Set_Power_Supply_On_ground_With_Border_01 with Dissolve( 0.2 )
    ##
    
    
    "Прибор, тоже потерял товарный вид. Дело в том, что бока его были не гладкие, а состояли из сотен мелких рёбер — пластин. "
    "Видимо при работе прибор грелся, и такая конструкция была нужна, для охлаждения. Ребра теперь были все погнуты, особенно те что по краям. "
    "В просветы между ними забилась трава, земля и частички асфальта. Один из циферблатов на передней панели — треснул. "
    
    hide Radio_Set_Power_Supply_On_ground_With_Border_01 with dissolve
    
    "Но мне, конечно, было наплевать. Не на выставку же нёс, в самом деле!"
    
    "Ну вот и всё, пришло время передохнуть!"
    "Я окинул взглядом и оценил вещи принесённые мной. Да я просто герой!"
    "Эх, жалко я Айко не показал, какая эта жёлтая зараза - тяжёлая! Она бы мной гордилась! "
    "Пожалела меня, и позабыла про свои придирки не меньше чем на месяц! И почему я такой не догадливый!"
    
    "С этими мыслями я открыл пиво, которое дожидалось в кармане брюк. "
    "Да уж, взболтал я содержимое банки здорово — пена полезла наружу, липкие струйки потекли по пальцам. "
    "Я тихо ругнулся, сдул пену, вытер руку о штаны, и поставил ногу на тот прибор, что принёс раньше остальных — как на поверженного врага. "
    "Сделал глубокий глоток, затем огляделся по сторонам."
    
    #Мини ЦГ - Касуми идет с тележкой
    image Kasumi_Walks = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi_Walks/Kasumi_Walks.png"
    image Kasumi_Walks_Moved:
        contains:
            "Kasumi_Walks"
            xpos 700
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kasumi_Walks_Masked = AlphaMask( "Kasumi_Walks_Moved", "border_01_right_mask_moved" )
    
    image Kasumi_Walks_With_Border_01:
        contains:
            "Kasumi_Walks_Masked"
        contains:
            "border_01_right_moved"
    
    show Kasumi_Walks_With_Border_01 with Dissolve( 0.2 )
    ##
    
    "Мне навстречу шла девушка, и катила перед собой маленькую тележку для вещей. "
    "Тележка была пуста. "
    "Зачем она это делала, было не понятно, да и способ перемещения тележки странный — гораздо проще везти тележку за собой."
    "А такую маленькую — вообще, лучше было бы сложить, взять подмышку и идти так. "
    "Внезапно девушка остановилась, отвернулась к обочине дороги и замерла."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( 0.1 )
    
    #Мини ЦГ - Касуми стоит с тележкой
    image Kasumi_And_Interesting_Wall = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi_And_Interesting_Wall/Kasumi_And_Interesting_Wall.png"
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
    
    show Kasumi_And_Interesting_Wall_With_Border_01 with Dissolve( 0.2 )
    ##
    
    "Не меньше минуты она стояла перед каменной кладкой, словно рассматривала интереснейшую картину."
    "Я между тем терялся в догадках, чего же такого интересного она там увидела."
    "Когда я проходил это место, то не приметил ничего необычного."
    "Но может быть, девчонке этой надо на площадку для мусора? Я её стесняю, и поэтому она так внезапно принялась изучать эту стену?"
    
    hide Kasumi_And_Interesting_Wall_With_Border_01 with Dissolve( 0.1 )
    show Kasumi_Walks_With_Border_01 with Dissolve( 0.2 )
    
    "Как только я подумал об этом, школьница отвернулась от стены и продолжила свой путь в мою сторону. "
    "Обычно я в таких случаях перехожу на другую сторону улицы или вообще стараюсь побыстрее скрыться с глаз встречного прохожего. "
    "Но в этот раз повышенная концентрация «лекарства» позволила мне и далее с любопытством наблюдать за незнакомкой."
    "Привычный страх перед людьми на время оставил меня полностью."
    
    hide Kasumi_Walks_With_Border_01 with Dissolve( 0.1 )
    
    "Девушка наконец достигла площадки для сбора мусора. И находилась метрах в пяти от меня."
    "Она остановилась и отвесила мне учтивый поклон! Я бы даже сказал - чересчур учтивый!"
    
    #Мини ЦГ - Касуми стоит на четвереньках
    image On_All_Fours = "./images/cg/DAY_01/Trash_Place_Meeting/On_All_Fours/On_All_Fours.png"
    image On_All_Fours_Moved:
        contains:
            "On_All_Fours"
            xpos -500
            pause 0.7
            linear 10.0 xpos -1100
    
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
    
    show On_All_Fours_With_Border_01 with Dissolve( 0.2 )
    ##
    
    "Ее ладони коснулись асфальта, и она встала на четвереньки. "
    "Если честно, мне захотелось воскликнуть от удивления, но я продолжил стоять как вкопанный, только глаза мои опускались все ниже. "
    "Её руки замелькали по асфальту."
    
    hide On_All_Fours_With_Border_01 with Dissolve( 0.1 )
    
    #Мини ЦГ - Руки Касуми на штанине Кендзи
    image Kasumi_Hands_On_Kenji_Leg = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi_Hands_On_Kenji_Leg/Kasumi_Hands_On_Kenji_Leg.png"
    image Kasumi_Hands_On_Kenji_Leg_Moved:
        contains:
            "Kasumi_Hands_On_Kenji_Leg"
            xpos 700
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Kasumi_Hands_On_Kenji_Leg_Masked = AlphaMask( "Kasumi_Hands_On_Kenji_Leg_Moved", "border_01_right_mask_moved" )
    
    image Kasumi_Hands_On_Kenji_Leg_With_Border_01:
        contains:
            "Kasumi_Hands_On_Kenji_Leg_Masked"
        contains:
            "border_01_right_moved"
    
    show Kasumi_Hands_On_Kenji_Leg_With_Border_01 with Dissolve( 0.2 )
    ##
    
    "А через мгновение принялись ощупывать жёлтый чемоданчик и далее - мой кроссовок, штанину..."
    
    kenji "Эй! Ты чего творишь?"
    
    hide Kasumi_Hands_On_Kenji_Leg_With_Border_01 with Dissolve( 0.1 )
    show empty_image with vpunch #Трясем экран
    
    "..."
    
    #Мини ЦГ - Касуми упала на пятую точку
    image Kasumi_Fells = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi_Fells/Kasumi_Fells.png"
    image Kasumi_Fells_Moved:
        contains:
            "Kasumi_Fells"
            xpos -700
            pause 0.7
            linear 5.0 xpos -500
    
    image border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kasumi_Fells_Masked = AlphaMask( "Kasumi_Fells_Moved", "border_01_left_mask_moved" )
    
    image Kasumi_Fells_With_Border_01:
        contains:
            "Kasumi_Fells_Masked"
        contains:
            "border_01_left_moved"
    
    show Kasumi_Fells_With_Border_01 with dissolve
    ##

    "Руки девушки отцепились от моих брюк, а сама она отпрянула так стремительно что не удержалась на ногах и села на асфальт."
    "Но не успел я моргнуть, как она оправилась и встала."
    
    hide Kasumi_Fells_With_Border_01 with Dissolve( 0.1 )
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    
    blind_girl "Простите! Я не заметила вас!"
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    kenji "Не заметила?!"
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "Да, я ничего не вижу."
    
    #Мини-ЦГ лицо Касуми крупным планом
    image DAY_01_Kasumi_Big_Face = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi/Kasumi.png"
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
    
    hide kasumi_01_Normal_Say with Dissolve( 0.1 )
    show kasumi_01_Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( 0.1 )
    show DAY_01_Kasumi_Big_Face_With_Border_01 with dissolve
    
    "Я взглянул на её лицо и холодок пробежал у меня по спине."
    "Солнце ярко высвечивало её загорелое лицо и искрилось в светлых, будто выжженных волосах. "
    "Но наперекор светилу, зрачки её были так широки, что по тонким радужкам невозможно было определить даже цвет глаз. "
    "Этот контраст расширенных, как у кошки в ночи, зрачков и яркого солнца, бьющего прямо в глаза — напугал меня. "
    "Девушка была слепой."
    
    hide DAY_01_Kasumi_Big_Face_With_Border_01 with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent with Dissolve( 0.1 )
    show kasumi_01_Normal_Silent with Dissolve( 0.1 )
    
    kenji "Извини..."

    "Хрипло прошептал я. "
    "Я кашлянул и повторил снова, уже в полный голос."

    kenji "Извини!"
    
    show kasumi_01_Concerned_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silents
    
    "Девушка встревожилась."
    
    show kasumi_01_Concerned_Say with Dissolve( 0.2 )
    hide kasumi_01_Concerned_Silent
    
    blind_girl "Что? Почему? За что?"
    
    show kasumi_01_Concerned_Silent with Dissolve( 0.2 )
    hide kasumi_01_Concerned_Say
    
    kenji "Ну... Я... Не думал что ты..."
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Concerned_Silent

    blind_girl "Всё нормально! Хорошо что я не налетела на вас."
    blind_girl "Вас совсем не было слышно и я думала что тут никого нет."
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    "Наверное, слепые люди полагаются на слух. Нет. Вовсе не наверное, а точно. На что же ещё? Может на обоняние? "
    "Тут словно нужную часть мозга мне врубили и я почувствовал как от слепой девушки просто несёт запахом сигарет. "
    "Она что, курит, и курит настолько много?!"

    "Я помнил какие безобразно коричневые были ногти у моего курящего деда. "
    "Но нет, опустив взгляд, я увидел приятные, робкие пальчики с аккуратно подстриженными, розовыми ноготками. "
    "Её руки покрыты сильным загаром, но возле рукавов матроски, кожа стремительно белела. "
    "На левом запястье надет широкий тканевый напульсник, закрывающий половину предплечья."
    "В нем было множество кармашков, часть из которых была занята универсальной отверткой и десятком бит под нее. "

    "Мой взгляд скользнул выше, пробежал по шее девушки, тоже загорелой, но и тут из-под матроски проглядывали белые участки, точно повторяющие контур выреза. "
    "Видимо школьная форма этим летом была её повседневной одеждой. Я подметил, что воротник выцвел - форма была старой и поношенной. "

    "Лицо её мне показалось очень приятным, давно я так близко не разглядывал старшеклассниц."
    "Но все впечатление портил этот пустой взгляд, в котором казалось навечно застыл испуг."
    
    #Мини-ЦГ ус Касуми крупным планом
    image DAY_01_Kasumi_Big_Face_Mustache = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi/Kasumi.png"
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
    
    show DAY_01_Kasumi_Big_Face_Mustache_With_Border_01 with Dissolve( 0.2 )
    
    "И ещё одна примечательная деталь — белый ободок с проводками, на кончиках которых блестели маленькие шарики из фольги."
    "С этим аксессуаром, голова девушки напоминала муравья или инопланетянина из старых черно-белых фильмов."
    "И зачем ей эти «усы»?"
    
    hide DAY_01_Kasumi_Big_Face_Mustache_With_Border_01 with Dissolve( 0.2 )

    "Всё в этой девушке было странным. Её пугающие, невидящие глаза, этот странный ободок, напульсник с отвёртками, нашивки на школьной форме. "
    "И стойкий запах сигаретного дыма."
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "Получается эта рация ваша?"
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    "Спросила девушка, а её ладонь указала в сторону моих ног."
    
    show Radio_Set_On_Ground_With_Border_01 with dissolve
    
    kenji "Так это рация?"
    
    "Я удивился, при слове рация мне представлялось маленькое, величиной с мобильный телефон — устройство. "
    "А такая громадина, и тоже — рация. Ну надо же!"
    
    hide Radio_Set_On_Ground_With_Border_01 with Dissolve( 0.1 )
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "Ну да. Военная рация, очень хорошая, американская, мощная. В конце шестидесятых годов выпускалась. Ещё на германиевых транзисторах!"
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    "Германиевых? Значит ли это, что транзисторы были из Германии? Какое странное словосочетание. "
    "Интересно, а «япониевый транзистор», есть?"

    kenji "Рация — не совсем моя. Одного родственника"
    kenji "Я просто, вещи его на свалку выношу. Он видимо радио увлекался, или что-то в этом роде."
    kenji "Сам я в этих делах ничего не смыслю."
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "А..."
    blind_girl "Увлекался?"
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    kenji "Ну да. Умер он. Но очень давно. А сейчас понадобилось расчистить немного места в доме. Вот и выбрасываем, и рацию эту тоже."
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "А... А я думала, вы наоборот. Пришли сюда за ней."
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    "Теперь я понял, зачем девушке нужна была тележка. И почему была вскрыта крышка на «рации». "
    "Похоже вещь эта её заинтересовала, и она собралась её забрать себе."
    
    kenji "Нет! Мне этот хлам нафиг не сдался. Если хочешь забрать — бери конечно."
    kenji "Только, как же ты её унесёшь? Думаешь сможешь? Она страшно тяжёлая! И чего она столько весит?"
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent
    
    blind_girl "Вещи тех лет — все такие громоздкие. А это ещё и военная, там все внутри с многократным запасом прочности!"
    
    hide kasumi_01_Normal_Say with Dissolve( 0.2 )
    
    "С этими словами, она присела и потянула руки в сторону рации. Я поспешно убрал ногу и отступил на шаг. "
    
    #Мини ЦГ - Касуми пытается поднять рацию
    image Kasumi_Lifting_Up_RadioSet = "./images/cg/DAY_01/Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Kasumi_Lifting_Up_RadioSet.png"
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
    
    show Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( 0.2 )
    
    "Девушка ощупала боковины прибора, взялась за тканевую ручку и попыталась встать. "
    "Послышался скрежет металла об асфальт, прибор поднялся но совсем чуть-чуть, сантиметров на пять. "
    "Я удивился тому, какие тонкие и изящные у неё руки, и как напряглись мышцы на них, в попытке приподнять рацию."
    
    kenji "Позволь помочь!"

    "Сказал я, встал с другой стороны и взял прибор за другую ручку. "
    
    hide Kasumi_Lifting_Up_RadioSet_With_Border_01 with Dissolve( 0.1 )
    show empty_image with vpunch #Трясем экран 
    
    "Но в тот же момент, руки девушки разжались и прибор глухо хлопнулся на землю. "
    
    show kasumi_01_Surprised_Silent with Dissolve( 0.2 )
    
    "А девушка, задыхаясь выпалила."
    
    show kasumi_01_Surprised_Say with Dissolve( 0.2 )
    hide kasumi_01_Surprised_Silent
    
    blind_girl "И в правду, очень тяжёлый!"
    
    show kasumi_01_Surprised_Silent with Dissolve( 0.2 )
    hide kasumi_01_Surprised_Say

    "Я вспомнил о банке пива в моей руке, и отглотнул немного. А после - сказал."

    kenji "Давай помогу погрузить эту штуковину на тележку. Похоже, тебе её не поднять."
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Surprised_Silent
    
    "Она кивнула."
    
    show kasumi_01_Normal_Say with Dissolve( 0.2 )
    hide kasumi_01_Normal_Silent

    blind_girl "Хорошо. Спасибо."
    
    show kasumi_01_Normal_Silent with Dissolve( 0.2 )
    hide kasumi_01_Normal_Say
    
    "Я взялся за тележку - на вид крайне хлипкую, из алюминиевых трубок, скреплённых пластиковыми уголками и такими же заклёпками. "
    "Рама её была перехвачена двумя плетёными жгутами красного цвета."

    "Я поставил тележку, поднял рацию и аккуратно установил её на раму. Рама выгнулась и затрещала, но выдержала. "
    "Я хорошенько обмотал всю эту конструкцию багажными жгутами, наклонил. Вроде всё держалось."
    
    "123456"
    
    return
