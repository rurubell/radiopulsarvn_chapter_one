init python:
    None


define kenji = Character( "Кендзи", color="#BBFF88" )
define aiko = Character( "Айко", color="#FF888B" )
define kasumi = Character( "Касуми", color="#88C0FF" )
define vatan = Character( "Ватанабе", color="#009900" )
define zak = Character( "Заказчик", color="#FFC95C" )
define tv = Character( "Телевизор", color="#FFC95C" )



label start:
    image dust = Dust( "./images/other/dust.png" )
    
    image midori_00 = "./images/cg/Green-Haired_Girl/00.png"
    image midori_01 = "./images/cg/Green-Haired_Girl/01.png"
    image midori_02 = "./images/cg/Green-Haired_Girl/02.png"
    image midori_03 = "./images/cg/Green-Haired_Girl/03.png"
    image midori_04 = "./images/cg/Green-Haired_Girl/04.png"
    image midori_05 = "./images/cg/Green-Haired_Girl/05.png"
    
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

    "Кендзи!"
    
    "Я настолько ушел в свои мысли что не сразу сообразил - меня зовут."
    
    scene kenji_bedroom_door
    show aiko_sprite
    
    "В дверях стояла Айко, моя младшая сестра."
    "Ой! Кажется она уставилась в мой монитор!"
    
    hide kenji_bedroom_door
    hide aiko_sprite
    
    scene monitor_with_Midori
    
    "Я повернулся обратно к монитору. Там как и раньше красовалась Мидори, над которой я сегодня как следует поиздевался."
    "Черт! Я бы ни за что не стал, добровольно демонстрировать такое творчество своей младшей сестре! Как не вовремя она зашла! "
    
    ######################
    
    hide monitor_with_Midori
    scene monitor_with_Kenji_desktop
    
    "Я молниеносно закрыл программу для рисования. А после, вновь повернулся к Айко."
    
    hide monitor_with_Kenji_desktop
    scene kenji_bedroom_door
    show aiko_sprite 
    
    "Похоже Айко успела разглядеть Мидори."
    "На несколько секунд повисла неловкая пауза, но затем моя сестра пришла в себя и тихо сказала."
    
    aiko "Ужин готов."
    
    "Посмотрела на меня, нахмурилась и выпалила."
    
    aiko "Только надень на себя хоть что-то!"
    
    "Только сейчас я осознал что сижу в кресле в одних трусах."
    "Пока я разглядывал себя и своё нижнее белье, Айко исчезла."
    
    image Day_Kenji_Home_Bedroom = "./images/bg/Indoor/Kenji_Bedroom/Day/Day_Kenji_Home_Bedroom.png"
    image Day_Kenji_Home_Bedroom_Mask = "./images/bg/Indoor/Kenji_Bedroom/Day/Day_Kenji_Bedroom_Mask.png"
    scene Day_Kenji_Home_Bedroom  with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Bedroom_Mask", At( "dust", center )) as mask
    
    "Не стоило злить свою сестру и опаздывать. Я встал, накинул рубашку, застегнул её через пуговицу."
    "Когда с рубашкой было покончено, я натянул брюки, и пытаясь застегнуть тугую ширинку, сделал несколько шагов по комнате."

    "Спустился по лестнице и вот я уже в большом холле, который к тому же выполняет роль кухни и столовой."
    
    image Day_Kenji_Home_Kitchen_Other = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Other.jpg"
    image Day_Kenji_Home_Kitchen_Mask = "./images/bg/Indoor/Kenji_Home_Kitchen/Day/Day_Kenji_Home_Kitchen_Mask.png"
    scene Day_Kenji_Home_Kitchen_Other with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Kitchen_Mask", At( "dust", center )) as mask
    

    kenji "И что сегодня на завтрак?"
    aiko "На завтрак — мисо-суп, рис и омлет."
    
    "Я сел за стол. Айко же, протёрла его влажной тряпкой. "
    "Поставила на него две деревянные подставки. Протерла их. "
    "Затем аккуратно расставила передо мной тарелки, положила палочки для еды. Все в лучшем виде. "
    
    image Kenji_1st_Day_Breakfast_Food = "./images/cg/Kenji_1st_Day_Breakfast/Food.png"
    scene Kenji_1st_Day_Breakfast_Food with dissolve
    
    "Даже розовые таблетки — ферменты для пищеварения, которые мне прописали много лет назад — не забыты."
    
    image Kenji_1st_Day_Breakfast_Normal_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Normal_Aiko_Say.png"
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Say with moveinright
    
    aiko "Папа и мама звонили."
    
    image Kenji_1st_Day_Breakfast_Normal_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Normal_Aiko_Silent.png"
    image Kenji_1st_Day_Breakfast_TV_Strange_Movie = "./images/cg/Kenji_1st_Day_Breakfast/TV_Strange_Movie.png"
    image Kenji_1st_Day_Breakfast_Confused_Aiko = "./images/cg/Kenji_1st_Day_Breakfast/Confused_Aiko.png"
    image Kenji_1st_Day_Breakfast_TV_News = "./images/cg/Kenji_1st_Day_Breakfast/TV_News.png"
    image Kenji_1st_Day_Breakfast_Surprised_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Surprised_Aiko_Say.png"
    image Kenji_1st_Day_Breakfast_Surprised_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Surprised_Aiko_Silent.png"
    image Kenji_1st_Day_Breakfast_Angry_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Angry_Aiko_Say.png"
    image Kenji_1st_Day_Breakfast_Angry_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Angry_Aiko_Silent.png"
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Say
    
    "Меня от этой новости немного передёрнуло, отца я побаивался. "
    "Но, последнюю неделю я вёл себя хорошо, не думаю что Айко могла про меня наябедничать. "
    "Я ждал, что Айко скажет что-то еще, но она не стала продолжать. Значит — все нормально!"
    
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Silent with moveoutright
    
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
    
    show Kenji_1st_Day_Breakfast_Confused_Aiko with moveinright
    
    "Я перевёл взгляд на сестру. Что за дурацкий канал она врубила с утра пораньше? "
    "Айко была сильно смущена и стояла как истукан с крышкой от кастрюли и черпаком в руках."
    
    hide Kenji_1st_Day_Breakfast_Confused_Aiko with moveoutright
    
    "Хвала богам, пульт лежал на столе и через мгновение был у меня в руках."
    "Я перебирал каналы, пока не нашёл что-то наиболее нейтральное. "
    
    show Kenji_1st_Day_Breakfast_TV_News with dissolve
    hide Kenji_1st_Day_Breakfast_TV_Strange_Movie
    
    "Новости."
    "Выпуск в самом разгаре, обсуждают ближнее зарубежье. Китай, Корея, США. Отлично, самое оно! "
    
    hide Kenji_1st_Day_Breakfast_TV_News with moveoutleft
    
    "Я вновь взялся за палочки для еды, но вдруг Айко остановила меня."
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Say with moveinright
    
    aiko "Ты не забыл?"
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Say
    
    kenji "Не забыл «что»?"
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Silent
    
    aiko "Сегодня четверг, день вывоза электронных приборов. Мама же просила освободить кладовку!"
    
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Say with moveoutright
    
    "Черт! Я помнил про это вчера, но с утра конечно позабыл все на свете."
    "Вот бы еще и Айко забыла! "
    "Барахла в кладовке превеликое множество. Столько работы! Хорошо если за день управлюсь. "
    "Конечно, никто никуда не спешит. Отец и тётя Асука приедут ещё очень не скоро. Если вообще, навестят нас до конца лета. "
    "Поэтому со спокойной совестью можно отмахнуться от забот сегодня, и поднажать в следующий четверг. "
    "Но если вдруг позвонит отец. Не очень хочется слушать его нравоучения. А Айко меня сдаст наверняка."

    "Я отложил палочки для еды в сторону."
    
    kenji "Айко! Ты ещё не налила себе порцию?"
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Say with moveinright
    
    aiko "Что? Нет. Но собираюсь."
    
    show Kenji_1st_Day_Breakfast_Normal_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Say
    
    kenji "Возьми мою, я суп не буду!"
    
    show Kenji_1st_Day_Breakfast_Surprised_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Normal_Aiko_Silent
    
    aiko "Это ещё почему?"
    
    show Kenji_1st_Day_Breakfast_Surprised_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Surprised_Aiko_Say
    
    "Не то, чтобы я вдруг внезапно перестал быть голодным. Но мне требовалось оставить место в желудке для кое-чего другого."
    
    kenji "Мне салата хватит! А вместо супа, достань ка мне из холодильника баночку пива! Там же ещё осталось?"
    
    show Kenji_1st_Day_Breakfast_Angry_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Surprised_Aiko_Silent
    
    aiko "Пиво! С утра?!"
    
    show Kenji_1st_Day_Breakfast_Angry_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Angry_Aiko_Say
    
    kenji "А что такого?"
    
    show Kenji_1st_Day_Breakfast_Angry_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Angry_Aiko_Silent
    
    aiko "Нет, ничего! Суп ты теперь вообще есть не будешь? Может мне тогда начать варить пиво для тебя?"
    
    show Kenji_1st_Day_Breakfast_Angry_Aiko_Silent
    hide Kenji_1st_Day_Breakfast_Angry_Aiko_Say
    
    "Айко была крайне возмущёна."
    
    kenji "Остынь Айко. Мне надо, понимаешь? Это как лекарство. Я же на улицу пойду. А там люди кругом. Это мне для храбрости!"
    
    hide Kenji_1st_Day_Breakfast_Angry_Aiko_Silent with moveoutright
    
    "Конечно Айко не понять меня. "
    "Но мне — тридцатилетнему затворнику, проводящему дни и ночи за компьютером, известно насколько это тяжело встречать по дороге соседей и знакомых, и хриплым голосом желать им доброго дня. "
    "Если я выпью немного алкоголя, дела пойдут гораздо веселее."

    "Айко с угрюмым видом кинула черпак в кастрюлю и пошла к холодильнику."
    
    image Kenji_1st_Day_Breakfast_Fridge_Normal_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Normal_Aiko_Say.png"
    image Kenji_1st_Day_Breakfast_Fridge_Normal_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Normal_Aiko_Silent.png"
    image Kenji_1st_Day_Breakfast_Fridge_Surprised_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Surprised_Aiko_Say.png"
    image Kenji_1st_Day_Breakfast_Fridge_Surprised_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Surprised_Aiko_Silent.png"
    image Kenji_1st_Day_Breakfast_Fridge_Angry_Aiko_Say = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Angry_Aiko_Say.png"
    image Kenji_1st_Day_Breakfast_Fridge_Angry_Aiko_Silent = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Angry_Aiko_Silent.png"
    image Kenji_1st_Day_Breakfast_Fridge_Irritated_Aiko = "./images/cg/Kenji_1st_Day_Breakfast/Fridge_Irritated_Aiko.png"
    
    show Kenji_1st_Day_Breakfast_Fridge_Normal_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Fridge_Normal_Aiko_Silent
    
    aiko "Ну, какое тебе?"
    kenji "Да оно же одинаковое, любое!"
    
    show Kenji_1st_Day_Breakfast_Fridge_Surprised_Aiko_Say
    hide Kenji_1st_Day_Breakfast_Fridge_Normal_Aiko_Say
    
    aiko "Ты чего думаешь, я в сортах пива — спец?"
    
    show Kenji_1st_Day_Breakfast_Fridge_Irritated_Aiko with dissolve
    hide Kenji_1st_Day_Breakfast_Fridge_Surprised_Aiko_Say
    
    "Айко взяла из холодильника одну из банок."
    "Мне показалось, что сейчас она небрежно кинет банку мне, настолько недовольное было у неё выражение лица."
    "Но нет, она этого не сделала, а аккуратно поставила пиво на мою дощечку для еды."
    
    image Kenji_1st_Day_Breakfast_Food_With_Beer = "./images/cg/Kenji_1st_Day_Breakfast/Food_With_Beer.png" 
    show Kenji_1st_Day_Breakfast_Food_With_Beer with dissolve
    hide Kenji_1st_Day_Breakfast_Fridge_Irritated_Aiko
    hide Kenji_1st_Day_Breakfast_Food
    
    "Затем она забрала мою порцию супа и мою ложку для бульона. Села напротив меня."
    "Я взял холодную банку, и дёрнул за открывашку. Затем я схватил розовые таблеточки, запихнул их в рот и запил пивом."
    "При виде этого, по лицу Айко пробежала странная гримаса, но она ничего не сказала и принялась за еду."
    "Я тоже не медлил и торопливо потягивал пиво из банки, закусывая рисом и кусочками амлета."
    "Есть я старался быстро, но и аккуратно чтобы не испачкать стол и не раздосадовать Айко снова."
    
    scene Day_Kenji_Home_Kitchen_Other with dissolve
    show expression AlphaMask( "Day_Kenji_Home_Kitchen_Mask", At( "dust", center )) as mask
    
    
    ""
    
    return
