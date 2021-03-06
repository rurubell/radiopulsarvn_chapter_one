#День второй
label day_02:
    scene black with Dissolve( my_dissolve_05 )
    pause 0.5
    scene Day_Kenji_Home_Bedroom with Dissolve( my_dissolve_05 )
    
    "Всю ночь я не спал а бредил."
    "Меня мучило похмелье и сухость во рту, а когда бред отступал, я спускался на кухню и пил воду из чайника."
    "Под утро вода в чайнике закончилась, и я набрал полный рот ила, который скопился на его дне."
    "Тут уж я проснулся окончательно, и ещё полтора часа до звонка будильника просидел на кровати. "
    "Меня терзало чувства беспокойства и беспомощности."
    "Я ощущал себя больным и несчастным, а имя причины всех моих несчастий вертелось на языке."
    
    kenji "Касуми..."
    
    "Прошептал я про себя."
    
    kenji "Идиот!"
    
    "Конечно! Я был полным идиотом!"
    "Припоминая каждый эпизод своего вчерашнего приключения, я с силой бил себя ладонью об лоб."
    "А когда вспомнил про свои вечерние мысли и желания о новой встрече с Касуми, тут уж вовсе не выдержал и схватил обоими руками себя за волосы."
    "Но легче от этого не стало."
    
    "Я с отвращением смотрел на приготовленные вечером, парадные джинсы и рубаху."
    "На очки, нацепив которые я с воодушевлением кривлялся перед зеркалом."
    
    "Нет! Хватит с меня и вчерашнего."
    "Теперь запрусь дома на месяц! На год!"
    "Как я снова выйду на улицу и взгляну в глаза людям?"
    "Лучше бы я, в самом деле нажрался как заправской алкоголик и уснул на площадке для мусора."
    "А Айко увезла меня домой на тележке..."
    
    "Я снова хлопнул себя по лбу."
    "Как я мог забыть про тележку!"
    "Нет, с самоизоляцией от общества придётся повременить.  Мой благой поступок меня же загнал в ловушку."
    "Да и благим я его назвать уже не мог."
    "Наверняка в моем уголовном деле, которое вчера легло на стол важному следователю, кроме очевидного заголовка \"Танака Кендзи, извращенец и алкоголик\" есть приписка \"похититель багажных тележек.\""
    
    play sound "sounds/sounds/Room_Door_Lock.mp3"
    
    "Щёлкнул дверной замок."
    
    show Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я обернулся. В дверях стояла Айко."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Уже встал, так рано?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ага... Что, завтрак уже?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко улыбнулась и закивала."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Завтрак, завтрак!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ладно, я сейчас."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Давай!"
    
    scene Day_Kenji_Home_Bedroom with Dissolve( my_dissolve_02 )
    
    "Айко закрыла дверь."
    
    "Я поднялся и надел свою домашнюю одежду."
    "Проходя мимо зеркала, я с трудом удержался от порыва посмотреть в него."
    "Нет, уж лучше не портить себе настроение ещё больше."
    "Ну ладно хоть очки есть... впрочем, зачем они мне? Я отвратительный и никому не нужный хикикомори."
    "Отнесу эту чёртову тележку, извинюсь перед тёткой Касуми и домой. Посижу дома, пока все не устаканится."
    "Пока все не забудут про моё существование."
    "Пока Касуми не повзрослеет и не выйдет замуж."
    "Пока её тётка не сыграет в ящик."
    
    "А остальные вещи дяди Макото сожгу и закопаю на заднем дворе. Черта с два я ещё раз пойду на площадку для мусора!"
    
    ##СЦЕНА НА КУХНЕ
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    play environment_sounds "sounds/environment/Kitchen_With_Boiled_Water.mp3" fadein 1
    
    "Я спустился на первый этаж. Айко была здесь и возилась возле плиты."
    
    #Мини ЦГ - Журавлик с осколками стекла
    image Paper_Crane_And_Plastic_Pieces = "images/cg/DAY_02/01a_Kenji_Breakfast/Paper_Crane_And_Plastic_Pieces/Paper_Crane_And_Plastic_Pieces.png"
    image Paper_Crane_And_Plastic_Pieces_Moved:
        contains:
            "Paper_Crane_And_Plastic_Pieces"
            xpos -500
            #xpos -800
            #pause 0.7
            #linear 5.0 xpos -500
    
    image Paper_Crane_And_Plastic_Pieces_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Paper_Crane_And_Plastic_Pieces_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Paper_Crane_And_Plastic_Pieces_Masked = AlphaMask( "Paper_Crane_And_Plastic_Pieces_Moved", "Paper_Crane_And_Plastic_Pieces_border_01_left_mask_moved" )
    
    image Paper_Crane_And_Plastic_Pieces_With_Border_01:
        contains:
            "Paper_Crane_And_Plastic_Pieces_Masked"
        contains:
            "Paper_Crane_And_Plastic_Pieces_border_01_left_moved"
    ##
    
    show Paper_Crane_And_Plastic_Pieces_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Моё внимание привлекла куча битого стекла лежащего на столе вперемешку с обрывками бумаги."
    "Я сразу понял что это. Это были останки тех дисков с порнографией что я обнаружил вчера в комнате отца."
    "На вершине кучи возвышался бумажный журавлик."
    "Сделан он был из обложки того фильма, про путешествие на море, с сестрой."
    
    hide Paper_Crane_And_Plastic_Pieces_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Айко отвернулась от плиты и весело заявила."
    
    #Мини ЦГ - кухонная плита, на фоне которой стоит Айко
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    show Day_Aiko_Home_Outfit_Yahoo Smile_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Заседание в клубе извращенцев — отменяется!"
    
    show Day_Aiko_Home_Outfit_Yahoo Smile_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я в ответ только покачал головой. Конечно же, Айко не забыла про вчерашнее."
    "Но мне было совершенно все равно. У меня тут совсем другие заботы, ещё я внимание буду обращать на выходки сестры."
    "Я подвинул мусорную урну к столу и смахнул в неё останки от дисков."
    "Только журавлика оставил. Как никак — искусство!"
    
    hide Day_Aiko_Home_Outfit_Yahoo with Dissolve( my_dissolve_01 )
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Наверное Айко ожидала от меня другого поведения."
    "Наверное думала что я буду плакать навзрыд, роясь в этой куче осколков. Но не тут то было!"
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Айко поставила перед мной дощечку для еды и тарелки и осторожно спросила."
    
    #Мини ЦГ - кухонная плита, на фоне которой стоит Айко
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    show  Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты же правда, никуда не идёшь?"
    
    show  Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Не знаю что ты там себе напридумывала. Но мои дела никто не отменял."
    
    "Я взял палочки для еды."
    
    show  Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А как же пиво?"
    
    show  Day_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Пиво? Оно же закончилось! Я же вчера все выпил!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Да закончилось..."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко была в растерянности."
    "Наверное подумала что отсутствие пива меня остановит и я никуда не пойду."
    "Но идти надо было, как бы мне не хотелось."
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_02 )
    
    "Я включил телевизор. Опять новости."
    
    show Gennadiy_Lapin_TV with Dissolve( my_dissolve_05 )
    
    "Похоже выпуск только начался, говорили про Японию."
    
    tv "Министр финансов объединил три внешних кредита Японии в один. И вылетел на переговоры в Турцию..."
    
    hide Gennadiy_Lapin_TV with Dissolve( my_dissolve_01 )
    
    "Меня мало интересовали дела министра финансов и я принялся за суп."
    "Когда с супом было покончено и я взялся за рис, моё внимание привлекла Айко."
    
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Она все ещё не обслужила себя а стояла возле плиты и наблюдала за мной."
    "Никогда бы не подумал, что то что я иду на улицу по делам и при этом совершенно трезвый — может её так волновать."
    
    kenji "Айко. Я надеюсь, этот \"клуб извращенцев\", ты не веришь в него взаправду?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Confused_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко смутилась и отвела взгляд."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Confused_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Я не знаю... Ты так внезапно куда-то собрался."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Confused_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что поделать! У меня срочные дела!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты сказал что хочешь с кем-то встретиться. С кем?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Если бы я хотел с кем-то встретиться! На самом деле я уже ничего не хотел."
    
    kenji "Ни с кем мне встречаться не надо!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ммм? Что же это за дело такое?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Какая разница? Просто дело и всё!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Значит всё-таки клуб!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Никакой не клуб, я просто..."
    
    "Я похлопал себя по бедру, пытаясь придумать что-то, что бы показалось правдоподобным."
    "Рука моя нащупала в кармане телефон."
    
    kenji "Я иду фотографировать!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Фотографировать?!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ну да. Фотографировать."
    
    "Я обрадовался тому, что придумал удачную отговорку и принялся было за рис."
    "Айко опять задала вопрос."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А что фотографировать?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Как что? Референсы!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Чего?"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я поднял вверх указательный палец, чтобы придать себе значительный вид."
    
    kenji "Референсы это фотографии, с которых я буду что-то срисовывать."
    kenji "Не рисовать же всё из головы! Мне нужны референсы! Я буду смотреть на них, чтобы мои рисунки были правдивее."
    kenji "Поэтому надо их сделать, да побольше!"
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Рисунки..."
    
    show Day_Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ну да, рисунки. Ты разве забыла кем я работаю?"
    kenji "Я художник, и мне нужны референсы! С ними лучше."
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Айко надолго замолчала. Похоже её убедило моё объяснение."
    "Я отвлёкся на миску с рисом и принялся за еду, а когда закончил завтрак понял что Айко с кухни пропала"
    
    scene Day_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 )
    
    "То что Айко ушла с кухни, мне было на руку."
    "Я сбегал в свою комнату, натянул джинсы, схватил рубаху и вновь спустился на первый этаж."
    " Разложил на столе доску для глажки и хорошенько прогладил воротник и рукава у рубашки."
    " Я убрал доску и утюг на место, натянул рубаху, надел очки и уже собирался выйти на улицу."
    "Но дорогу мне преградила Айко."
    
    show Day_Aiko_Nightie_PonyTails_Without_FlashLight Suspect_Silent with Dissolve( my_dissolve_02 )
    
    "Странно, но на Айко была надета ночная пижама."
    "Вид у моей сестры был хмурый."
    
    kenji "Эй, Айко? Ты чего? Ты не заболела?"
    
    "Айко не ответила."
    
    hide Day_Aiko_Nightie_PonyTails_Without_FlashLight with Dissolve( my_dissolve_01 )
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Вдруг она распахнула полы своей пижамы и скинула её на пол."
    "Под пижамой был надет школьный купальник."
    
    kenji "Э? Ты что, в бассейн что-ли собралась? Зачем ты напялила купальник дома?"
    
    "Айко недовольно буркнула."
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Нет, ни в какой бассейн я не иду. Это... ну... референсы!"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Чего?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Сам же сказал, что собрался фотографировать референсы для своих художеств!"
    aiko "А теперь и никуда идти не нужно. Скажи мне спасибо, я сегодня добрая."
    aiko "А на улице будешь фотографировать что не следует, и в полицию попадёшь."
    aiko "Мне, маме и папе такая слава не нужна знаешь ли!"
    aiko "Давай, делай свои фотографии и поскорее покончим с этим. Как мне встать?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Тут то до меня наконец-то дошло, о чем говорила Айко."
    "Конечно же, она видела вчерашний мой рисунок и похоже догадалась за какими референсами я собираюсь пойти."
    "Какие референсы могут понадобиться извращенцу?"
    "Ну конечно же — фотографии молоденьких девчёнок в купальниках, сделанные тайно."
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Так как мне встать?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Я приложил ладонь ко лбу и покачал головой."
    
    kenji "Как цапля встань."
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Surprised_Say with Dissolve( my_dissolve_01 )
    
    aiko "Как ц-цапля? Это как?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Никак! Под референсами я имел ввиду совсем другое."
    kenji "Машины, дома, деревья, фонарные столбы. А ты о чем подумала?"
    
    "Айко не нашла слов чтобы ответить мне."
    
    kenji "Ты что же думаешь, я собрался тайно фотографировать молоденьких девченок? Эх Айко... Как же ты испорчена!"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Surprised_Say with Dissolve( my_dissolve_01 )
    
    aiko "А? Чего?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Какие ужасные вещи приходят тебе в голову!"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Angry_Say with Dissolve( my_dissolve_01 )
    
    aiko "Что ты говоришь! Это не я а ты испорчен, это все из-за тебя!"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Angry_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Значит ты надеваешь купальник и предлагаешь себя фотографировать. А испорчен я?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Angry_Say with Dissolve( my_dissolve_01 )
    
    aiko "Да ну тебя!"
    aiko "Чтобы вечером показал мне свой телефон и всё что сфотографировал! Ясно?"
    
    show Day_Aiko_School_Swimsuit_Hands_On_Hips Angry_Silent with Dissolve( my_dissolve_01 )
    
    kenji "А? Чего это ты так раскомандовалась? Сейчас я тебе покажу свой телефон..."
    
    "Я достал телефон из кармана, открыл камеру и нажал на спуск. Послышался звук затвора."
    
    hide Day_Aiko_School_Swimsuit_Hands_On_Hips with Dissolve( my_dissolve_02 )
    show Day_Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Айко отпрыгнула в сторону."
    
    show Day_Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты чего творишь?"
    
    show Day_Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Раз уж ты испортила ценный реквизит, теперь сама станешь реквизитом для сегодняшнего заседания нашего клуба!"
    
    "Я направил телефон на сестру и сделал ещё снимок."
    
    show Day_Aiko_School_Swimsuit_Hand_Hold_Hand Scared_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ай! Нееет!"
    
    hide Day_Aiko_School_Swimsuit_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    
    "Айко бросилась наутёк, вверх по лестнице. Только её ночнушка осталась лежать на полу."
    "Похоже она заметила свои оплошность."
    "С верхнего этажа послышался её крик полный досады."
    
    #Мини ЦГ - звук голоса Айко с верхнего этажа
    image Aiko_Cries_From_Second_Floor:
        contains:
            "empty_image"
        
        contains:
            ypos 250
            xpos 30
            "Emo_What_Horizontal_Flipped"
    ##
    
    show Aiko_Cries_From_Second_Floor with Dissolve( my_dissolve_01 )
    
    aiko "Только попробуй утащить туда мою ночнушку! Я тебя убью!"
    
    ##КОНЕЦ СЦЕНЫ НА КУХНЕ, КЕНДЗИ ВЫХОДИТ НА УЛИЦУ И ИДЕТ К КАСУМИ (ОТНОСИТЬ ТЕЛЕЖКУ)
    
    play environment_sounds "sounds/environment/City_Suburb_Day_01.mp3" fadein 1 fadeout 1
    scene Outdoor_Day_Kenji_Home with Dissolve( my_dissolve_05 )
    
    "Я вышел на улицу, точнее не вышел а прокрался."
    "Аккуратно выглянул из-за двери и убедился что свидетелей нет."
    "Сегодня пятница, рабочий день, как и вчера. Может быть моё новое приключение никто и не увидит?"
    
    "Но полностью остаться незамеченным не выйдет."
    "Перед Касуми и её тёткой предстать во всей красе всё же придётся"
    "Можно, конечно, незаметно пробраться к ним во двор, поставить туда эту несчастную тележку и смыться."
    
    "Я достал тележку, сложил её и быстрым шагом отправился в сторону дома Касуми."
    "На этот раз моё путешествие не было таким мучительным как вчера днём."
    "В руках только алюминиевая тележка, которая ничего не весила."
    "Никакой тяжести, только на душе было тяжко."
    
    
    play environment_sounds "sounds/environment/City_Suburb_Day_03.mp3" fadein 1 fadeout 1
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    pause 0.5
    
    "Я добрался до площадки для мусора быстро как ветер."
    "Но тут увидел то, от чего пришлось замереть как вкопанному."
    
    #Мини ЦГ - Касуми сидит на дорожном отбойнике
    image Kasumi_On_Guard_Rail = "images/cg/DAY_02/02a_Way_To_Dump/Kasumi_Sit_On_Road_Guard_Rail/Kasumi_On_Guard_Rail.png"
    image Kasumi_On_Guard_Rail_Moved:
        contains:
            "Kasumi_On_Guard_Rail"
            xpos 550
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_On_Guard_Rail_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Kasumi_On_Guard_Rail_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kasumi_On_Guard_Rail_Masked = AlphaMask( "Kasumi_On_Guard_Rail_Moved", "Kasumi_On_Guard_Rail_border_01_right_mask_moved" )
    
    image Kasumi_On_Guard_Rail_With_Border_01:
        contains:
            "Kasumi_On_Guard_Rail_Masked"
        contains:
            "Kasumi_On_Guard_Rail_border_01_right_moved"
    ##
    show Kasumi_On_Guard_Rail_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "На обочине дороги, на отбойнике сидела Касуми."
    "Я на всякий случай потёр глаза, но девушка не пропала значит сидела здесь взаправду. Интересно, что она тут делала?"
    "Сегодня электронику никто не выбросит, значит ловить ей здесь нечего."
    "Неужели она ждёт меня? Может тётка её сюда послала?"
    "Сказала \"Иди и без моей тележки не возвращайся!\"."
    "Надеюсь Касуми не ночевала здесь?"
    
    "Вообще, то что я встретил здесь свою вчерашнюю знакомую, меня сильно воодушевило."
    "Даже если она злится на меня за вчерашнее, с этой девчёнкой я найду общий язык."
    "Верну ей её имущество и пусть возвращается домой."
    "И не надо идти в тот страшный район где живёт Касуми, на её улицу, к её дому, её тётке попадаться на глаза."
    "Всё разрешилось гораздо проще чем я думал."
    
    "Я на цыпочках подошёл поближе к Касуми, внимательно огляделся вокруг."
    "Не прячется ли в кустах её тётка, или может быть полицейский патруль."
    
    hide Kasumi_On_Guard_Rail_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Наверное надо было подойти к Касуми открыто, громко топая подошвами по асфальту, чтобы она меня заметила."
    "Но раз уж подкрался как мышь, ничего не поделать."
    "Надо сказать её что-то, лучше всего поздороваться, пожелать доброго дня..."
    "Но так сильно колотилось сердце и в горле стоял ком, всё-таки сегодня я \"лекарство\" от страха не принял."
    "Мне захотелось даже тихонько отойти от Касуми, а потом приблизиться к ней, отбивая шаг каблуками, чтобы она это услышала и первое слово осталось за ней."
    "Но я решил рискнуть, и заговорить первым. "
    "Набрал побольше воздуха в грудь. Вспомнил вчерашние упражнения на устранение гнусавости, напряг нужные мышцы горла, чтобы сформировать \"певческий зевок\"."
    "Погладил ладонью живот, чтобы узнать насколько хорошо раздулась диафрагма. Приготовился."
    
    kenji "Добргыххх... Кха! Кхе!"
    
    "Похоже я перестарался. Воздух пошёл не в то горло, вырвался через нос и я закашлялся"
    "Да уж, хотел как лучше, но лучше бы я молча бросил в Касуми её тележку и убежал поскорее домой."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Касуми вскочила и повернулась ко мне. Я хватая ртом воздух еле произнёс."
    
    kenji "Ка... Касуми... Добрый день... Это.. Это я... Кендзи!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say with Dissolve( my_dissolve_01 )
    
    kasumi "А! Танака-сан! Это вы? Что с вами?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Все... Всё в порядке... Просто я... Муху проглотил!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Около минуты ушло на то, чтобы я пришел в себя и восстановил способность нормально говорить."
    "Шанс произвести хорошее впечатление при встрече, провалился."
    "Ну ладно, по крайней мере я смог заговорить с Касуми."
    "Пока я откашливался, девушка молчала и ожидала что я скажу."
    
    kenji "Касуми! Вот, как и обещал, твоя тележка. Я починил её."
    
    "Я поставил тележку перед девушкой."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ах, тележка!"
    kasumi "Спасибо вам Танака-сан! Наверное вам не стоило так утруждать себя..."
    kasumi "Сколько вам заплатить за ремонт?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Заплатить? Нет! Мне ничего не надо!"
    
    "Удивительно, но Касуми злилась на меня. Приняв тележку она вежливо поклонилась."
    "Похоже все мои опасения были напрасны, хоть я вчера и нажрался прилично — особых глупостей не натворил."
    "Или Касуми настолько вежливая, что решила промолчать?"
    "Интересно, зачем она пришла сюда, на площадку для мусора? Её тётка послала искать тележку?"
    
    kenji "Касуми, а ты чего тут делаешь? Ждала, когда я принесу тележку? Я же хотел принести её тебе домой."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Я надеялась что те вещи, что вы вынесли вчера, Танака-сан, они ещё здесь. "
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Вот как... Но когда вчера вечером я шёл обратно, всё уже забрали. А что? Там было ещё что-то стоящее?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Кажется я ошиблась, и тот блок питания для рации, он действительно был нужен. Я надеялась, что он остался лежать здесь."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Вот как... Значит ты за ним при шла?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ага."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Но как бы ты унесла его домой? Он в два раза тяжелее чем рация."
    kenji "Сидела бы здесь, и ждала того, кто поможет унести его тебе домой?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Да, мне его не унести. Но хотя бы оттащила подальше, в кусты. А там, может придумала бы чего."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Надеюсь Касуми не сидит здесь целый день, в ожидании, когда выкинут чего интересного."
    "И не просит случайных прохожих помочь ей унести это до дома? В прочем я вчера сам напросился ей помочь."
    
    kenji "Да наверное так и следовало поступить. Припрятать его в тенёчек."
    kenji "Но ты же сама вчера сказала что у тебя уже есть, дома?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Я ошиблась. Я думала что эта рация, она полностью транзисторная, но это не так."
    kasumi "Кажется выходной каскад, он на лампах сделан. Нужно высокое напряжение для выходных ламп, и для накала."
    kasumi " Хотя, для накала у меня может и найдётся что-то. Но где взять анодное напряжение для выходных ламп?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Вопросы, которые задавала Касуми, сейчас были похлеще тех, какими грешил дядя Ватанабэ."
    "Но вид у девушки был такой серьёзный, что я даже на некоторое время задумался, не знаю ли я случайно, где в самом деле достать \"анодное напряжения\" для \"выходных ламп\""
    "Я чесал и лоб, затылок и подбородок, но безрезультатно. Я не имел ни малейшего представления о чем вообще шла речь."
    
    "А для Касуми, найти это \"анодное напряжение\" похоже было настолько важно, что она проделала значительный путь до сюда."
    "Для меня, такая её увлечённость — большая удача."
    "Теперь, когда я вручил тележку этой слепой девчёнке, я мог со спокойной совестью вернуться домой."
    "Жаль конечно, что Касуми пришла сюда не для того, чтобы встретить меня ещё раз, а за этим жёлтым ящиком."
    
    "Или нет? Может она в самом деле пришла сюда ради встречи со мной?"
    "Уборщики улиц от графика не отстают и не стоит надеяться, что выброшенные вещи спокойно переночуют и с утра их можно будет забрать обратно."
    
    "А Касуми, казалось, ждала чего-то. Теперь, когда она получила обратно свою тележку, ей уже можно было бы попрощаться со мной."
    "У меня не было при себе ни блока питания, ни выходного напряжения с анодными лампами. "
    "Вообще ничего из того что ей нужно."
    
    "Я смотрел в лицо Касуми, и пытался понять что у неё на уме."
    "Наверное она единственная девушка из тех что я встречал, в глаза которой я мог смотреть прямо и без страха, зная что она ничего не видит."
    "Может поэтому и говорить с Касуми было не страшно, даже несмотря на то, что я был трезв."
    
    "С утра я проклинал себя за то, что вчера встретился и заговорил с Касуми."
    "Пока я шёл сюда, я обдумывал сотни фраз для извинения перед ней и её тёткой."
    "И вдруг - всё разрешилось само собой."
    "Более того — похоже я зря укорял себя за своё вчерашнее поведение. Кажется, я не вёл себя плохо."
    "А если и вёл? Говорят, девочкам нравятся плохие парни!"
    "В прочем, я и хороший поступок совершил. Отнёс ей рацию, починил тележку."
    "Может быть Касуми пришла сюда чтобы ещё раз встретиться со мной? Может быть я ей, понравился?"
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_02 )
    
    "Я испугался своих мыслей и помотал головой в разные стороны. "
    "Но всё-таки Касуми похоже не собиралась уходить, не прощалась со мной."
    "Наверное ждала, чтобы я сказал что-то, а не молчал."
    
    "Да, действительно, слишком долго мы молчали. Надо сказать хоть что-то, Касуми ещё подумает чего."
    "Конечно я мог попрощаться, пожелать всего хорошего и смыться, и наверное, это было бы самым правильным поступком, и утром я мог о таком только мечтать. "
    "Но теперь я осмелел, мои утренние страхи развеялись и я захотел большего."
    
    "В любом случае, надо было прервать это утомительное молчание."
    "Конечно, где взять эти, как их там, ламповые аноды для напряжённого выхода — это явно не мне вопросы."
    "К сожалению, вчера я так и не осилить ни одной книжки по нужной теме. Может быть, сейчас нашлась тема для разговора."
    "Ну а раз нет, просто спрошу. Касуми все равно знает что я в этой теме полный ноль. Может ей нравится делиться своими знаниями?"
    
    kenji "Так что, эту рацию без блока питания, никак не включить?"
    
    "Касуми встрепенулась, пожала плечами и ответила."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Не знаю. Я даже не знаю какое там должно быть напряжение"
    kasumi "Это мощная рация, и лампы мощные, генераторные."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Слово \"генераторные\" звучало весомо. Ух и светят наверное они, эти генераторные лампы."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Таким лампам нужно очень высокое напряжение. Может быть восемьсот вольт, или даже тысяча."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Сколько? Тысяча?!"
    
    "Цифры были ошеломляющие. Не удивительно почему этот аппарат столько весил."
    "Тысяча вольт! Вот это прибор! Да он должен был весить тысячу тонн, как по мне!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ну да, тысяча. Столько из бытовых блоков питания никак не получить. Может только сетевое взять и умножить. Но это очень опасно!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Да уж, опасней некуда. Похоже без этого невероятного блока питания, рация действительно — полный хлам."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Извините Танака-сан, но похоже я зря вас потревожила вчера..."
    kasumi "Хотя... Пусть лежит, может быть я смогу что-то с ней сделать."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Я раздумывал о том, что же можно в такой ситуации придумать."
    "К сожалению, в кладовке больше ничего похожего на тот блок питания ну точно не лежало."
    "Такая габаритная вещь, там бы от меня не спряталась."
    
    "Я задумчиво смотрел то на Касуми, то по сторонам."
    "Оглядывал кусты вокруг мусорной площадки, не припрятал ли там кто этот блок питания."
    
    #Мини ЦГ - Табличка на столбе
    image Trash_Place_Post_Plate = "images/cg/DAY_02/02a_Way_To_Dump/Trash_Place_Post_Plate/Trash_Place_Post_Plate.png"
    image Trash_Place_Post_Plate_Moved:
        contains:
            "Trash_Place_Post_Plate"
            xpos 550
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Trash_Place_Post_Plate_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Trash_Place_Post_Plate_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Trash_Place_Post_Plate_Masked = AlphaMask( "Trash_Place_Post_Plate_Moved", "Trash_Place_Post_Plate_border_01_right_mask_moved" )
    
    image Trash_Place_Post_Plate_With_Border_01:
        contains:
            "Trash_Place_Post_Plate_Masked"
        contains:
            "Trash_Place_Post_Plate_border_01_right_moved"
    ##
    show Trash_Place_Post_Plate_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "И тут мой взгляд задержался на синей табличке, которая висела на столбе рядом с корзинами под мусор."
    "На табличке было написано расписание мусорщиков по дням, но кроме этого — адрес пункта сбора мусора."
    "В моей голове созрел план."
    
    kenji "Эй, Касуми! А что если нам вернуть этот блок питания."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Вернуть? Как?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Гляди! Тут адрес..."
    
    "Я осёкся на половине фразы. Черт! Я снова сказал то, чего не следовало."
    "Но похоже что девушку мои слова не обидели."
    
    "Тут адрес места, куда свозят мусор. Я не знаю точно, но похоже эта улица не так уж и далеко отсюда."
    "Может быть, они смогут отдать нам нужную вещь. Всякое же бывает, вдруг по незнанию выкинули что-то, чего не хотели?"
    
    hide Trash_Place_Post_Plate_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Я достал телефон и открыл карту. Да, я был прав — адрес был не так уж и далеко отсюда."
    "Вполне можно было дойти за час или даже меньше."
    
    "Касуми нерешительно спросила."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Вы тоже? Тоже пойдёте со мной, Танака-сан?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Мне конечно же хотелось пойти с Касуми. Как и вчера, захотелось мне побыть с ней побольше, пообщаться и помочь."
    "Даже несмотря на отсутствие алкоголя в организме, её я больше не боялся."
    "Да и бояться нечего, вчера я ничего ужасного не натворил, даже наоборот."
    
    kenji "А как по другому? Если ты и дойдёшь туда Касуми, как ты унесёшь этот блок питания домой?"
    kenji "Он тяжелее чем рация, раза в два, если не больше."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ну... Если вам не трудно... Спасибо..."
    kasumi "А как же вы его унесёте если он такой тяжёлый?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "А тележка? Теперь на ней колеса уже не сломать. Довезём на ней!"
    
    "Хотя, не очень то я доверял этой тележке. Если новые колеса и выдержат, слабину может дать хлипкая рама."
    "Вчера, тащить на своём горбу тот громоздкий прибор до мусорной площадке было невыносимо тяжело."
    "Если придётся заниматься этим и сегодня — не думаю что я это осилю."
    "Если получится вернуть этот блок питания обратно и тележка с ним не справится — закажу такси так и быть."
    
    #КОНЕЦ СЦЕНЫ НА ПЛОЩАДКЕ ДЛЯ СБОРА МУСОРА
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_05 )
    
    "Дорога, что вела к пункту сбора мусора — пролегала через наш, местный деловой центр."
    "Хотя деловым центром называть его было как-то глупо. Все дела они делались далеко, в центре города а не в захолустных пригородах."
    "В нашем же деловом центре стояли кофейни и лапшичные, мелкие магазинчики, почтовые отделения и тому подобная дребедень."
    
    "Но в любом случае — пусть даже это и захолустный пригород, однако дела здесь кое-какие велись, и было гораздо оживлённее чем на улицах где жили я и Касуми."
    
    show That_Fucking_Cat
    
    "Обычно появление в этой части города я избегал, как и любой порядочный домосед."
    "Можно было конечно сделать крюк, обойти опасное место. Но как объяснить такой манёвр Касуми?"
    "Конечно, она ничего не видит, и можно её просто обмануть. Но вдруг догадается?"
    
    hide That_Fucking_Cat with Dissolve( my_dissolve_03 )
    
    "Но не так сильно меня волновало то, где мы будем идти. Мой страх перед людьми - он заметно уменьшился."
    "Находясь рядом с Касуми, я будто приобретал особый социальный статус, я словно стал как все."
    "Я был прилично одет и наверняка не производил впечатление безработного домоседа."
    "А Касуми рядом со мной — словно моя подружка, или даже девушка!"
    "В былые времена, если я вдруг оказывался на улице, и встречался с гуляющими парочками — я старался разминуться с ними во что бы то не стало."
    "И чувствовал что смотрят они на меня, как на последнего червя если не хуже."
    "Сейчас, рядом с девушкой, я сам ощущал себя настоящим хозяином улицы."
    "Теперь никто не мог сказать про меня плохого, или посмотреть косо."
    
    "И действительно, косо на меня никто не смотрел."
    "Немногочисленные встречные прохожие либо проходили мимо меня не обращая внимания, либо с интересом и как мне показалось, с уважением разглядывали меня и Касуми."
    "Тогда я делал горделивую осанку и элегантным жестом поправлял очки на мокром от пота носу. Конечно, ноги мои слегка тряслись, но я не подавал и вида."
    "В другой день, если бы я оказался на этих улицах трезвый, я бы согнулся в три погибели под взглядами людей и спрятался бы в клумбе с цветами."
    "А потом, строил планы по  отступлению из клумбы в ближайший алкогольный магазин."
    "Сейчас такого произойти не могло, мой новый статус давал мне право ходить по улицам безнаказанно."
    
    "Хотелось мне этот статус как-то закрепить. Как-то показать людям, что мы с Касуми настоящая парочка."
    "Хоть мы и шли рядом, но всё же не вели себя как знакомые парень и девушка на прогулке."
    "Обычно парочки хохочут и щебечут о всяком. Му же шли в полном молчании."
    "Касуми почти механически отмеряла улицу шагами, и изредка спрашивала где мы идём, а я не находил смелости чтобы заговорить с ней о чём-то."
    
    "Завести разговор мне мешало не только трусость, но и незнание подходящей темы. Не о погоде же говорить, в самом деле!"
    "Впрочем, внезапно нашёлся способ и заговорить и показать окружающим что мы с Касуми по настоящему близкие люди."
    
    #Стрелка, указывающая на автоматы по продажи мороженного
    image Day_Shops_And_Vending_Machines_01_Pointer:
        contains:
            "Pointer_01"
            rotate 45/2
            xpos 250
            ypos 400
            alpha 0.0
            pause 0.5
            alpha 1.0
            pause 0.5
            repeat
    
    show Day_Shops_And_Vending_Machines_01_Pointer
    
    "Я заметил автоматы по продаже мороженного. Надо предложить его Касуми, в такую жару она не откажется."
    
    hide Day_Shops_And_Vending_Machines_01_Pointer
    
    kenji "Касуми? Ты не хочешь... Не хочешь мороженное?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Мороженное?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Ага, мороженное. Здесь продают. Что-то я так уморился на этой жаре."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Но блок питания..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Похоже что Касуми мороженного не очень то и хотелось."
    
    kenji "Да ничего с ним не случится! Время ещё совсем раннее, успеем!"
    
    "Хотя, вероятность что с ним ничего не случится была мала."
    "Даже если его уже раздавили под прессом и мы идём зря, наверняка Касуми будет считать меня виноватым, за то что мы задержались по такому незначительному поводу."
    "Но в любом случае, пусть злится сколько угодно, потом. А сейчас мне хотелось провести с ней этот ритуал покупки мороженного парня для девушки."
    "Хотелось чтобы все увидели какой я замечательный. Может быть меня заметят мои знакомые, и скажут, что неправду говорят про Кендзи."
    "Никакой он не хикикомори, гляньте — преспокойно ходит по улицам, хорошеньких девушек мороженным угощает."
    
    "Касуми некоторое время нерешительно помолчала. Фразу, которую она сказала я очень ждал."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Но... У меня нет с собой денег..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Да брось! Конечно я заплачу за тебя. Какое тебе купить?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Спасибо, Танака-сан... Клубничное."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_01 )
    
    #Мини ЦГ - Торговые автоматы с мороженным
    image DAY_02_Wending_Machines = "images/cg/DAY_02/02a_Way_To_Dump/Wending_Machines/Wending_Machines.png"
    image DAY_02_Wending_Machines_Moved:
        contains:
            "DAY_02_Wending_Machines"
            xpos -520
            #xpos -800
            #pause 0.7
            #linear 5.0 xpos -500
    
    image DAY_02_Wending_Machines_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -700
    
    image DAY_02_Wending_Machines_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -700
    
    image DAY_02_Wending_Machines_Masked = AlphaMask( "DAY_02_Wending_Machines_Moved", "DAY_02_Wending_Machines_border_01_left_mask_moved" )
    
    image DAY_02_Wending_Machines_With_Border_01:
        contains:
            "DAY_02_Wending_Machines_Masked"
        contains:
            "DAY_02_Wending_Machines_border_01_left_moved"
    ##
    
    show DAY_02_Wending_Machines_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Клубничное мороженное в наличие было."
    "Вообще, мороженное с таким вкусом довольно популярное. Я даже удивился, что Касуми любит такое."
    "Её строгому и загадочному виду такой вкус мало подходил."
    
    "Я сам мороженное не ел лет десять. Поэтому некоторое время рассматривал яркие этикетки, и пытался найти хоть что-то знакомое, но тщетно."
    "Для себя я выбрал шоколадное мороженное с орешками."
        
    "Автомат выплюнул два брикета. Я подал один Касуми, а сам принялся за свой."
    
    show Day_Kasumi_School_Uniform_Eat_Ice_Cream Normal_Silent at Move( ( 450, 600 ), ( 450, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 )
    
    "Откусывая холодные кусочки, я с неудовольствием поглядывал по сторонам."
    "Всех прохожих как ветром сдуло."
    "Не то чтобы я так хотел, чтобы люди смотрели на нас. Но всё-таки!"
    "Для кого я режиссировал эту сценку? Такой момент и останется никем не замеченным!"
    "Да... Такой момент..."
    "Я полез в карман штанов за телефоном. Не пропадать же зря моменту."
    "Раз это никто не видит, я сделаю фотографию."
    
    "Неприлично, конечно, фотографировать незрячего человека против его воли, но что делать."
    "Я оглянулся, и удостоверился что свидетелей не было."
    
    #Мини - ЦГ экран телефона
    image DAY_02_Wending_Machines_Shooter_Moved:
        contains:
            "DAY_02_Wending_Machines_Shooter"
            xpos -520
            #xpos -800
            #pause 0.7
            #linear 5.0 xpos -500
            
    image DAY_02_Wending_Machines_Shooter_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -700-10
    
    image DAY_02_Wending_Machines_Shooter_Moved_Masked = AlphaMask( "DAY_02_Wending_Machines_Shooter_Moved", "DAY_02_Wending_Machines_Shooter_border_01_left_mask_moved" )
    ##
    
    show Day_Kasumi_School_Uniform_Eat_Ice_Cream Normal_Silent_With_Bug
    show DAY_02_Wending_Machines_Shooter_Moved_Masked with Dissolve( my_dissolve_02 ) 
    
    "Направил видоискатель телефона на Касуми, мирно жующую мороженное возле автомата."
    
    #Мини ЦГ - вид на Касуми из телефона
    
    "Ой что это?"
    "На мороженном Касуми лежало какое-то чёрное пятно."
    "Я потёр экран телефона, но пятно не исчезло. Похоже что это был не дефект телефона."
    "На мороженном сидело какое-то насекомое!"
    
    hide DAY_02_Wending_Machines_Shooter_Moved_Masked with Dissolve( my_dissolve_02 ) 
    
    kenji "Ой! Касуми! У тебя на мороженном сидит... Жук!"
    
    show Day_Kasumi_School_Uniform_Hold_Ice_Cream Normal_Say_with_Bug at Move( ( 450, 600 ), ( 450, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    hide Day_Kasumi_School_Uniform_Eat_Ice_Cream with Dissolve( my_dissolve_01 ) 
    
    kasumi "А?"
    
    show Day_Kasumi_School_Uniform_Hold_Ice_Cream Normal_Silent_With_Bug with Dissolve( my_dissolve_01 )
    
    "Касуми похоже не совем поняла о чем я говорю."
    "А на мороженном оказалось сидел не жук а пчела. Она по недоброму загудела, подтверждая мои слова."
    "Тогда Касуми отвела руку с мороженным максимально далеко от себя и зажмурилась."
    
    hide Day_Kasumi_School_Uniform_Hold_Ice_Cream with Dissolve( my_dissolve_03 )
    show Kasumi_Do_Not_Want_IceCream at Move( ( 550, 600 ), ( 550, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    kasumi "Ай! Танака-сан!"
    kenji "Сейчас я его!"
    
    hide Kasumi_Do_Not_Want_IceCream with Dissolve( my_dissolve_03 )
    
    "Я выхватил мороженное из протянутой руки Касуми."
    
    show Bee_On_Ice_Cream with Dissolve( my_dissolve_03 ) 
    
    "Замахал ладонью возле пчелы, пытаясь её согнать."
    "Но чёртово насекомое и не думало улетать, а только недовольно жужжало."
    "Тогда я отвесил пчеле хороший щелбан."
    
    hide Bee_On_Ice_Cream
    show Bee_Fly_away
    
    "Щелбан сработал."
    "Пчела стремительно улетела в неизвестном направлении, кувыркаясь в воздухе и обиженно жужжа."
    "К большой моей радости, обратно она не вернулась."
    
    hide Bee_Fly_away with Dissolve( my_dissolve_03 )
    
    "В руке у меня теперь было два стаканчика мороженного."
    "Моё, и мороженное Касуми, которое осквернил шмель."
    
    kenji "Мороженное... Тебе новое купить, Касуми?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 450, 600 ), ( 450, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    kasumi "Нет. Не нужно."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent
    
    kenji "Будешь старое?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say
    
    kasumi "Нет."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent
    
    "Наверное Касуми брезговала есть мороженное, на котором сидела пчела."
    "Хотя мне самому, пчёлы казались милыми и чистоплотными животными и я их не брезговал, как мух, например."
    "Или ей не хотелось есть мороженное, которое я трогал своими руками?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say
    
    kasumi "Блок питания... Может быть нам уже пойти за ним? Танака-сан?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent
    
    "Похоже Касуми не волновало ни мороженное ни шмели, а хотелось поскорее заполучить обратно этот прибор."
    "Если честно, мне своё мороженное тоже ни капельки не хотелось доедать. Кажется я уже окончательно пережил возраст любви к сладкому."
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_05 )
    
    "Урна для мусора обнаружилась неподалёку и я выкинул свой стаканчик."
    "Хотел было отправить и стаканчик Касуми, но что-то меня остановило."
    
    #Мини ЦГ - Мороженное - священный грааль
    image Holy_Grail = "images/cg/DAY_02/02a_Way_To_Dump/Holy_Grail/Holy_Grail.png"
    image Holy_Grail_Moved:
        contains:
            "white_image"
        
        contains:
            "Holy_Grail"
            xpos 550
    
    image Holy_Grail_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 700
    
    image Holy_Grail_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 700
    
    image Holy_Grail_Masked = AlphaMask( "Holy_Grail_Moved", "Holy_Grail_border_01_right_mask_moved" )
    
    image Holy_Grail_With_Border_01:
        contains:
            "Holy_Grail_Masked"
        contains:
            "Holy_Grail_border_01_right_moved"
    ##
    show Holy_Grail_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Мороженное которое только что облизывала Касуми, касалась его своими губами и языком, на нём остались её слюни."
    "Я поближе поднёс его к своим глазам."
    "Мой нос защекотал аромат клубники, а мозг заполнили неприличные мысли."
    "Я крутил стаканчик в руках, изучал следы девичьих зубов и языка на его поверхности и облизывался."
    "Вот оно, мороженное Касуми, в моих руках."
    "А ведь я могу без проблем лизнуть его."
    "Это же будет самый настоящий косвенный поцелуй!"
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_03 )
    
    "Прямо сейчас, в присутствии Касуми, и она мне ничего не скажет!"
    "Где-то на периферии сознания пронеслась мысль - \"не ешь, подумай!\""
    "Но мысли этой я не внял."
    "Я воровато оглянулся. На улице — никого."
    "Тогда я открыл рот как можно шире и запихнул туда мороженное Касуми."
    
    scene Shops_And_Vending_Machines_Winter with Dissolve( my_dissolve_05 )
    
    "Чёрт!"
    "Всё-таки его надо было лизнуть а не жрать куском."
    "Таинственный для меня, нецелованого хикикомори, момент первого косвенного поцелуя был испорчен."
    "Вместо этого я получил жутко холодный кусок снега во рту и адскую боль в зубах, словно у меня вдруг выпали все пломбы."
    "Корчась от боли, я пытался прожевать ледяной комок."
    
    kasumi "Танака-сан?"
    
    "Видимо Касуми начало беспокоить моё отсутствие."
    "Я повернулся и вопросительно промычал."
    
    kenji "М-мм?"
    
    show Day_Kasumi_Xmas_Elf Concerned_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Мы идём?"
    
    show Day_Kasumi_Xmas_Elf Concerned_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Угх... Угху-ху!"
    
    "Я закашлялся."
    "Выплюнул недоеденный комок мороженного, как кот выплёвывает комок шерсти."
    "Добрые пол минуты кашлял и давился собственными слюнями."
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_05 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Танака-сан! Что с вами?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Муха... Чёрт бы её побрал... Кажется ещё одну чуть не проглотил."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Пожалуйста, осторожнее, Танака-сан."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Похоже что враньё, повторённое дважды — Касуми не насторожило."
    "Но вообще, в связи с жарой, мошки в воздух поднялось достаточно. Можно было и поверить."
    "Язык от холода был ватным, зубы нестерпимо болели."
    "В носу свербило от запаха клубники, и я посадил несколько бледно-розовых пятен на свои джинсы и рубаху."
    "Ну и ладно! Оно того стоило!"
    "Это был самый настоящий косвенный поцелуй!"
    "Ах... Надеюсь Касуми не учует что от меня разит клубникой, и не подумает чего лишнего!"
    
    scene black_image with Dissolve( my_dissolve_05 )
    
    "Прошло около часа времени, когда мы наконец добрались до места."
    
    window hide
    scene Trash_Place_In_Kenji_Mind_Animated with Dissolve( my_dissolve_05 )
    window hide
    pause 1.0
    window show
    
    "Я воображал себе, что мы выйдем на настоящий полигон, с пирамидами из мусора размером с дом."
    "С могучими прессами, давящими автомобили как консервные банки."
    "С горами горящих покрышек."
    "Но нет."
    
    scene Day_First_Trash_Place
    
    "Перед нами были широкие раздвижные ворта, просторный двор, заставленый техникой и какие-то ангары."
    "И ни души."
    "Ну что-же, ничего не оставалось как зайти на территорию и поискать людей. Касуми решила остаться, и подождать меня возле ворот."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Я здесь постою Танака-сан? Ладно?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Хорошо. Надеюсь я быстро найду как попасть внутрь."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_03 )
    
    ##Мини-ЦГ - Дверь в ангар
    image First_Trash_Place_Door = "images/cg/DAY_02/03a_First_Trash_Place/First_Trash_Place_Door/First_Trash_Place_Door.png"
    image First_Trash_Place_Door_Moved:
        contains:
            "First_Trash_Place_Door"
            xpos -600
    
    image First_Trash_Place_Door_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -900
    
    image First_Trash_Place_Door_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -900
    
    image First_Trash_Place_Door_Masked = AlphaMask( "First_Trash_Place_Door_Moved", "First_Trash_Place_Door_border_01_left_mask_moved" )
    
    image First_Trash_Place_Door_With_Border_01:
        contains:
            "First_Trash_Place_Door_Masked"
        contains:
            "First_Trash_Place_Door_border_01_left_moved"
    ##
    
    show First_Trash_Place_Door_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Ничего особенного искать не пришлось. В ангар вела единственная дверь и она была заперта."
    "Я заглянул в окошко на двери, но в мутном стекле отражалась только улица и ничего нельзя было разобрать."
    "Возли двери распологалось какое-то подобие домофона и дверного звонка. Я нажал на кнопку."
    
    #Мини ЦГ - звук голоса Мусорщика из домофона
    image First_Trashman_Voice_Through_intercom:
        contains:
            "empty_image"
        
        contains:
            ypos 395
            xpos 507
            "Emo_What"
    ##
    
    show First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    "Запиликал звонок, а через несколько секунд домофон зашипел и в его динамике послышался мужской голос."
    
    someones_voice "Алло? Йоши? Это ты?"
    
    hide First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    kenji "Йоши? Нет... Добрый день... Я пришел... Этот адрес был указан на табличке, на мусорной площадке..."
    
    "Я продиктовал адрес нашей мусорной площадки."
    
    show First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    someones_voice "Да, мы обслуживаем её. Чего вы хотите?"
    
    hide First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    kenji "Понимаете. Я по ошибке, выкинул очень ценную вещь. Я бы хотел вернуть её!"
    
    show First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    someones_voice "Вернуть? Как давно вы её выкинули?"
    
    hide First_Trashman_Voice_Through_intercom with Dissolve( my_dissolve_01 )
    
    kenji "Вчера!"
    
    "Динамик домофона перестал шипеть, вновь заиграла мелодия звонка а в двери щёлкнул замок."
    "Я открыл дверь и вошёл внутрь."
    
    show DAY_First_Trash_Place_Room with Dissolve( my_dissolve_05 )
    
    "Тут мне в нос ударила жуткая смесь из запаха лапши быстрого приготовления, сигарет, грязных носков и ещё черт знает чего."
    "Ну прямо как в комнату студенческого общежития попал!"
    "Комнатка была маленькая и тесная."
    "С грязными стенами, с неприличными плакатами на них, с кучей всякого непонятного барахла и обшарпанной мебелью."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent with Dissolve( my_dissolve_03 )
    
    "Посреди комнаты стоял лысый, пожилой мужчина, очевидно с ним я говорил по домофону."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Я думал что Йоши пришел, этот парень у нас водителем работает..."
    trash_man_01 "Там девчонка с тобой, да? Не понравится ей наш беспорядок..."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Она сказала что подождёт на улице."
    
    "Мужчина повеселел."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Это ладно!"
    trash_man_01"Вообще, в первый раз слышу, чтобы к нам кто-то обращался по такому поводу."
    trash_man_01 "Наверное лучше бы спросить у начальства, можем ли мы вернуть что-то обратно. Объект то у нас режимный."
    
    hide Day_First_Trash_Place_Man_Hands_Down with Dissolve( my_dissolve_01 )
    show Day_First_Trash_Place_Man_With_Phone Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Он взял в руки телефон и видимо кому-то решил позвонить."
    "Но похоже - передумал."
    
    hide Day_First_Trash_Place_Man_With_Phone with Dissolve( my_dissolve_01 )
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "А впрочем — ладно. Ты только опиши мне сначала, что ты хочешь забрать."
    trash_man_01 "Чтобы я точно понял, что эта вещь твоя и ты не решил забрать что-то чужое и ценное."
    trash_man_01 "Хотя, кто ценности выбрасывает в мусорку, правда?"
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Я назвал приметы разыскиваемого прибора."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Говоришь вчера выбросил? Вчера меня на работе не было, позвоню ка я тому парню, которого меняю, и спрошу, что да как."
    
    hide Day_First_Trash_Place_Man_Hands_Down with Dissolve( my_dissolve_01 )
    show Day_First_Trash_Place_Man_With_Phone Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Он вновь взялся за телефон."
    "Последовала продолжительная пауза, но наконец на том конце подняли трубку."
    
    show Day_First_Trash_Place_Man_With_Phone Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Эй ... привет... Послушай, тут какой-то парень пришел, говорит вчера выбросил по ошибке ценную вещь..."
    trash_man_01 "Да, на нашу площадку... Вчера должны были привезти электронику..."
    trash_man_01 "В каком боксе? А... Нет? Не было? А... Ну ладно..."
    
    hide Day_First_Trash_Place_Man_With_Phone with Dissolve( my_dissolve_01 )
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Служащий мусорки закончил разговор по телефону и растеряно посмотрел на меня."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Похоже что Йоши не привозил вчера мусор."
    trash_man_01 "Странно... Может он перепутал чего? Сейчас я позвоню самому Йоши, и спрошу что да как..."
    
    hide Day_First_Trash_Place_Man_Hands_Down with Dissolve( my_dissolve_01 )
    show Day_First_Trash_Place_Man_With_Phone Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Он опять поднёс телефон к уху и послышались гудки."
    "Вдруг, я услышал крик. Кричала Касуми."
    
    kasumi "Ай!"
    
    hide Day_First_Trash_Place_Man_With_Phone with Dissolve( my_dissolve_03 )
    
    "Что там могло произойти?"
    "Я немедленно поспешил наружу."
    
    scene Day_First_Trash_Place with Dissolve( my_dissolve_05 )
    
    "Касуми стояла там же, где я её оставил, но вид у ней был испуганный."
    "Я и сам испугался."
    
    #Мини-ЦГ - Касуми облитая водой
    image Wet_Casumi_Moved:
        contains:
            "Wet_Casumi"
            xpos -500
    
    image Wet_Casumi_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -700
    
    image Wet_Casumi_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -700
    
    image Wet_Casumi_Masked = AlphaMask( "Wet_Casumi_Moved", "Wet_Casumi_border_01_left_mask_moved" )
    
    image Wet_Casumi_With_Border_01:
        contains:
            "Wet_Casumi_Masked"
        contains:
            "Wet_Casumi_border_01_left_moved"
    ##
    show Wet_Casumi_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Одежда девушки была насквозь мокрой, с прядей её волос, с юбки капала вода."
    "А под ней даже образовалась небольшая лужица."
    "Я сделал шаг в сторону Касуми, и вдруг почувствовал что наступил на что-то мягкое."
    "Что-то хлопнуло, а из под подошвы моего ботинка полетели брызги воды и жёлтые шкурки, прямо как от лопнувшего воздушного шарика."
    "Вокруг Касуми, валялось много таких шкурок."
    
    hide Wet_Casumi_With_Border_01 with Dissolve( my_dissolve_03 )
    
    #Мини ЦГ - Желтые Ошметки на Асфальте
    image Yellow_Something = "images/cg/DAY_02/03a_First_Trash_Place/Yellow_Something/Yellow_Something.png"
    image Yellow_Something_Moved:
        contains:
            "Yellow_Something"
            xpos 650
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Yellow_Something_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Yellow_Something_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Yellow_Something_Masked = AlphaMask( "Yellow_Something_Moved", "Yellow_Something_border_01_right_mask_moved" )
    
    image Yellow_Something_With_Border_01:
        contains:
            "Yellow_Something_Masked"
        contains:
            "Yellow_Something_border_01_right_moved"
    ##
    
    show Yellow_Something_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Что это?"
    "Откуда это взялось?"
    
    hide Yellow_Something_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Я завертел головой, оглядывая улицу."
    
    #Мини-ЦГ - Бегущие Хулиганы
    image Runnig_Hooligans = "images/cg/DAY_02/03a_First_Trash_Place/Running_Hooligans/Runnig_Hooligans.png"
    image Runnig_Hooligans_Moved:
        contains:
            "Runnig_Hooligans"
            xpos -500
    
    image Runnig_Hooligans_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -700
    
    image Runnig_Hooligans_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -700
    
    image Runnig_Hooligans_Masked = AlphaMask( "Runnig_Hooligans_Moved", "Runnig_Hooligans_border_01_left_mask_moved" )
    
    image Runnig_Hooligans_With_Border_01:
        contains:
            "Runnig_Hooligans_Masked"
        contains:
            "Runnig_Hooligans_border_01_left_moved"
    ##
    show Runnig_Hooligans_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "Виновники нашлись быстро — от нас, с топотом убегала группа детей."
    "Это что? Они облили Касуми?"
    
    kenji "Вот уроды!"
    
    #Нарисовать анимированные полоски вокруг кадра, как в манге ИнишалДи и т.
    
    scene Day_First_Trash_Place_Kenji_Run with Dissolve( my_dissolve_02 )
    
    "С этими словами я бросился в погоню."
    "Убегали хулиганы резво, и на перекрестке бросились врассыпную."
    
    scene First_Trash_Place_Street_Kenji_Run with Dissolve( my_dissolve_02 )
    
    "Я оценил обстановку и бросился за рослым, тучным пареньком."
    "Хоть я и так себе бегун, но моя жертва была ещё хуже. Он пыхтел как паравоз и испуганно оглядывался назад."
    "Догнать его было не сложно, и вскоре я схватил пацана за руку."
    
    scene First_Trash_Place_Street with Dissolve( my_dissolve_02 )
    show Day_Hooligan_Hide_Hands Surprised_Say with Dissolve( my_dissolve_02 )
    
    hooligan "Эй! Вы чего!"
    
    show Day_Hooligan_Hide_Hands Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Ты чего творишь, подлец!"
    
    show Day_Hooligan_Hide_Hands Surprised_Say with Dissolve( my_dissolve_02 )
    
    hooligan "Я? Нет! Произошла ошибка! Меня... Меня подставили!"
    
    show Day_Hooligan_Hide_Hands Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Что?"
    
    "Я сильнее сжал руку мальчика."
    
    show Day_Hooligan_Hide_Hands Surprised_Say with Dissolve( my_dissolve_02 )
    
    hooligan "Ай! Мне деньги заплатили! Я не хотел сам..."
    
    show Day_Hooligan_Hide_Hands Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Деньги заплатили? Чего ты мелешь! Сейчас вызовем полицию, пусть скажут твоим родителям, что ты натворил!"
    
    "Услышав такое, мальчик с силой рванул руку, но я её не выпускал."
    
    show Pain
    show Day_Hooligan_Hide_Hands Angry_Silent with hpunch
    
    "Тогда он пнул меня в колено."
    
    kenji "Ах ты подлюга!"
    
    "Удар был болезненный, но я стойко вытерпел боль и продолжал держать хулигана за руку."
    
    hide Day_Hooligan_Hide_Hands with Dissolve( my_dissolve_01 )
    show Day_Hooligan_With_Bomb Angry_Silent with Dissolve( my_dissolve_01 )
    
    "Однако следующая его атака оказалась удачной."
    
    scene First_Trash_Place_Blured_Animated with Dissolve( my_dissolve_01 )
    
    "Мне в лицо прилетел жёлтый снаряд, наполненный водой."
    "Перед глазами всё поплыло, очки слетели и от неожиданности руку мальчика я выпустил."
    "Пока я несколько секунд пытался вернуть зрение, хулиган времени не терял и смылся."
    
    scene First_Trash_Place_Street with Dissolve( my_dissolve_05 )
    
    "Хорошо хоть, очки спасли меня. Без них, удар мог оказаться сильнее."
    "Гнаться за мальчиком было бесполезно. Его след простыл."
    
    
    #Мини ЦГ - Рогатка хулигана на земле
    image Hooligans_Catapult = "images/cg/DAY_02/03a_First_Trash_Place/Hooligans_Catapult/Hooligans_Catapult.png"
    image Hooligans_Catapult_Moved:
        contains:
            "white_image"
        
        contains:
            "Hooligans_Catapult"
            ypos -50
            xpos 500
            pause 0.7
            ease 5.0 xpos 750
    
    image Hooligans_Catapult_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 1000
    
    image Hooligans_Catapult_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 1000
    
    image Hooligans_Catapult_Masked = AlphaMask( "Hooligans_Catapult_Moved", "Hooligans_Catapult_border_01_right_mask_moved" )
    
    image Hooligans_Catapult_With_Border_01:
        contains:
            "Hooligans_Catapult_Masked"
        contains:
            "Hooligans_Catapult_border_01_right_moved"
    ##
    
    show Hooligans_Catapult_With_Border_01 with Dissolve( my_dissolve_03 )
    
    
    "На асфальте осталась только его оружие — пластмассовая рогатка для водяных бомбочек."
    "Видимо он выронил её, когда сбежал."
    
    show Pain
    hide Hooligans_Catapult_With_Border_01 with hpunch
    
    "Я со злостью пнул рогатку и она улетела в кусты, а нога отозвалась сильной болью в колене."
    
    scene Day_First_Trash_Place with Dissolve( my_dissolve_05 )
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Когда я доковылял обратно к будке служащего мусорки — он сам уже стоял на улице, рядом с Касуми."
    "В руках у девушки было полотенце, которое она прижимала к груди."
    
    kenji "Черт! Почти поймал одного, но он выскользнул. А я... Споткнулся..."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Да уж! Хулиганьё! Совести нет у них! Напали на инвалида!"
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Видимо он уже понял, что Касуми слепая."
    
    "Я погладил больное, распухшее колено. И тут подметил, что на стене, прямо возле ворот, висит камера."
    
    kenji "Это у вас что? Видеосъемка? А запись идёт?"
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Ага! Записываем. Что, хочешь хулиганов опознать? Вообще, хорошая идея."
    trash_man_01 "Правда я не знаю как с этой аппаратурой работать. Сейчас позвоню начальству, спрошу..."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Он полез в карман штанов за телефоном, но его остановила Касуми."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Say at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Не надо. Зачем нам эта запись. В полицию с ней идти? Нет. Не нужно!"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Касуми ты чего? Ну надо же наказать эту шпану!"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Gloomy_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Касуми фыркнула и нахмурилась."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Gloomy_Say at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Не стоит тратить время, Танака-сан."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Gloomy_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я повернулся к служащему, и покачал головой. Он отправил телефон обратно в карман."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Я тут Йоши успел позвонить. Он в самом деле не приезжал, и не оставлял вчерашний мусор здесь."
    trash_man_01 "Видишь ли, у нас здесь только временное хранение. А вчера значит, мусора было немного."
    trash_man_01 "Он всё за один рейс забрал. Ну и поехал сразу на главный полигон. Там где завод по переработке мусора..."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Значит кранты ему... Блоку питания..."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Зачем же кранты? Не кранты! Сегодня пятница, а мусор перерабатывают по выходным. В будние дни они его только накапливают."
    trash_man_01 "Если сегодня побываешь у них, получишь свою вещь обратно."
    trash_man_01 "Там на проходной, тоже круглые сутки ребята сидят. Можно и вечером подойти. Скажешь им что да как, они вам отдадут ваш прибор."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Он протянул мне картонную визитку."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Вот, тут адрес полигона. Правда это место не в нашем районе уже. И вообще, за городом. Но на поезде остановок пять — шесть."
    trash_man_01 "Удачи ребята! А ты смотри парень, за девчонкой своей хорошо, вдруг ещё чем обольют."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я поджал губы чтобы не расплыться в глупой улыбке, когда услышал про \"свою девчонку\"."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Say at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "А... а полотенце?"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent at Move( ( 1300, 600 ), ( 1300, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Похоже касуми решила вернуть обратно полотенце, которым она прикрывалась."
    "Я не разглядел ничего, когда погнался за хулиганами, но похоже что школьная форма капитально намокла и просвечивала."
    "Это что же получается, я сейчас увижу нижнее белье Касуми? И... и этот мужик, тоже?"
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Не нужно! Нам каждую неделю новое выдают! Оставь себе."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Silent at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Вовремя!"
    "Я уже тянулся руками к пуговицам своей рубашки, чтобы снять её и накрыть ей Касуми."
    "Похоже что конкурса мокрых футболок сегодня не будет."
    
    show Day_First_Trash_Place_Man_Hands_Down Normal_Say at Move( ( 600, 600 ), ( 600, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    trash_man_01 "Ладно ребята! Удачи вам!"
    
    hide Day_First_Trash_Place_Man_Hands_Down with Dissolve( my_dissolve_02 )
    hide Day_Kasumi_School_Uniform_Wet_Hold_Towel with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Я поклонился ему, а он подмигнул мне, и скрылся в дверях своей каморки. Мы остались на улице одни."
    "Касуми по прежнему прижимала к груди полотенце, наверное она понимала, что её мокрая матроска просвечивала."
    "На плечах, показались очертания бретелек её бюстгальтера, а на спине, из под мокрой ткани проступили её тонкие лопатки."
    "Показалось, что девушка чуточку съёжилась, стала сутулиться."
    "Но лицо Касуми оставалось спокойным."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Танака-сан... Это сильно заметно? Что одежда у меня сырая?"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Да нет, не очень... Может, если совсем близко подойти..."
    
    "Я посмотрел на лужу под ногами девушки."
    "Асфальт стремительно высыхал, и только жёлтые, резиновые ошмётки лежали на нём тут и там."
    "Касуми нерешительно переступила ногами, послышался чавкающий звук а из её ботинка выплеснулось немного воды."
    
    kenji "Ой, да у тебя все ноги промокли!"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ничего..."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Касуми опять нерешительно переступила ногами."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Танака-сан... Вы можете снять ободок с моей головы? Кажется детектор с ума сошёл, пищит не умолкая."
    kasumi "Там разъем на проводе, его нужно разомкнуть."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Видимо руки у Касуми были связаны полотенцем, и она ничего не могла сделать."
    
    hide Day_Kasumi_School_Uniform_Wet_Hold_Towel with Dissolve( my_dissolve_03 )
    
    ##Мини ЦГ - Мокрая Касуми в пол-оборота, в ободке
    image Wet_Kasumi_HalfTurned_With_HeadBand = "images/cg/DAY_02/03a_First_Trash_Place/Wet_Kasumi_HalfTurned/With_HeadBand.png"
    image Wet_Kasumi_HalfTurned_With_HeadBand_Moved:
        contains:
            "Wet_Kasumi_HalfTurned_With_HeadBand"
            xpos -300
    
    image Wet_Kasumi_HalfTurned_With_HeadBand_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_With_HeadBand_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_With_HeadBand_Masked = AlphaMask( "Wet_Kasumi_HalfTurned_With_HeadBand_Moved", "Wet_Kasumi_HalfTurned_With_HeadBand_border_01_left_mask_moved" )
    
    image Wet_Kasumi_HalfTurned_With_HeadBand_With_Border_01:
        contains:
            "Wet_Kasumi_HalfTurned_With_HeadBand_Masked"
        contains:
            "Wet_Kasumi_HalfTurned_With_HeadBand_border_01_left_moved"
    ##
    show Wet_Kasumi_HalfTurned_With_HeadBand_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Конечно, для меня такая просьба была неожиданной. Уж слишком интимная эта процедура, снять с головы Касуми её ободок."
    "Но наверное неприятно, когда в ухе что-то пищит не переставая, надо бы помочь поскорее."
    "Я осторожно приблизил руку к голове девушки и потянул за ободок, стараясь руками не задеть волос Касуми."
    
    
    ##Мини ЦГ - Мокрая Касуми в пол-оборота, ободок снят, тянется провод
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01 = "images/cg/DAY_02/03a_First_Trash_Place/Wet_Kasumi_HalfTurned/Without_HeadBand_01.png"
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01_Moved:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_01"
            xpos -300
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01_Masked = AlphaMask( "Wet_Kasumi_HalfTurned_Without_HeadBand_01_Moved", "Wet_Kasumi_HalfTurned_Without_HeadBand_01_border_01_left_mask_moved" )
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_01_With_Border_01:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_01_Masked"
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_01_border_01_left_moved"
    ##
    show Wet_Kasumi_HalfTurned_Without_HeadBand_01_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Wet_Kasumi_HalfTurned_With_HeadBand_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Возможно что от волнения я снял ободок не очень аккуратно, и зацепил несколько волос, но Касуми ничего не сказала."
    
    "За ободком тянулся тоненький провод и чем дальше тянул я ободок на себя, всё больше провода тянулось след за ним, из под ворота матроски."
    
    ##Мини ЦГ - Мокрая Касуми в пол-оборота, ободок снят, тянется провод, видно разъем
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02 = "images/cg/DAY_02/03a_First_Trash_Place/Wet_Kasumi_HalfTurned/Without_HeadBand_02.png"
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02_Moved:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_02"
            xpos -300
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02_Masked = AlphaMask( "Wet_Kasumi_HalfTurned_Without_HeadBand_02_Moved", "Wet_Kasumi_HalfTurned_Without_HeadBand_02_border_01_left_mask_moved" )
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_02_With_Border_01:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_02_Masked"
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_02_border_01_left_moved"
    ##
    show Wet_Kasumi_HalfTurned_Without_HeadBand_02_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Wet_Kasumi_HalfTurned_Without_HeadBand_01_With_Border_01 with Dissolve( my_dissolve_01 )
    
    "Наконец показался разьем, к которому был пристегнут ободок. Дрожащими руками, я принялся его отстёгивать."
    "Я был очень взволнован."
    "Это, возможно, был первый мой шанс прикоснуться к Касуми за всё это время."
    "Руки мои были в нескольких сантиметров от её шеи, даже показалось что тыльной стороной ладони я почувствовал её дыхание."
    "Возможно Касуми тоже волновалась в этот момент, и тяжело дышала."
    "Или нет?"
    "Я ничего не слышал, слышал только бешеный стук собственного сердца. Надеюсь Касуми его не слышит!"
    
    ##Мини ЦГ - Мокрая Касуми в пол-оборота, разъем висит
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03 = "images/cg/DAY_02/03a_First_Trash_Place/Wet_Kasumi_HalfTurned/Without_HeadBand_03.png"
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03_Moved:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_03"
            xpos -300
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03_Masked = AlphaMask( "Wet_Kasumi_HalfTurned_Without_HeadBand_03_Moved", "Wet_Kasumi_HalfTurned_Without_HeadBand_03_border_01_left_mask_moved" )
    
    image Wet_Kasumi_HalfTurned_Without_HeadBand_03_With_Border_01:
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_03_Masked"
        contains:
            "Wet_Kasumi_HalfTurned_Without_HeadBand_03_border_01_left_moved"
    ##
    show Wet_Kasumi_HalfTurned_Without_HeadBand_03_With_Border_01 with Dissolve( my_dissolve_02 )
    hide Wet_Kasumi_HalfTurned_Without_HeadBand_02_With_Border_01 with Dissolve( my_dissolve_01 )
   
    "Ободок был успешно отсоединён, вторая половинка штекера повисла на груди Касуми."
    
    kenji "Готово!"
    
    scene Day_First_Trash_Place with Dissolve( my_dissolve_02 )
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Say with Dissolve( my_dissolve_02 )
    
    kasumi "Спасибо, Танака-сан!"
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Ободок, его тебе обратно, на голову одеть, Касуми?"
    kasumi "Нет... Если вам не трудно, Танака-сан. Не могли бы вы его подержать некоторое время?"
    
    "Держать ободок, который практически ничего не весил, мне было не трудно."
    "Я поднёс эту вещицу поближе к глазам, чтобы рассмотреть. Даже подумал о том, чтобы понюхать её."
    "Но нет! Это может кто-то увидеть!"
    "Я внимательно посмотрел в окно будки, где сидел служащий мусорки. В окне ничего не было видно."
    "Но черт знает, вдруг он наблюдает за нами! Захотелось поскорее покинуть это злосчастное место."
    
    kenji "Тебе бы просушить одежду, Касуми! Обувь особенно."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Да... но он... Служащий сказал, что перерабатывать мусор будут уже завтра..."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Касуми замолчала."
    "Несмотря на то, что её облили с ног до головы водой, мысли о том чтобы вернуть блок питания её не покинули."
    
    kenji "Ну да. Можно на поезде съездить. Станция не так уж и далеко."
    kenji "Они наверное круглые сутки там дежурят. В любое время можно. Но как же ты пойдёшь в таком виде?"
    
    "Касуми кивнула."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Да, пожалуй... Сегодня жарко, форма высохнет и так. А вот ботинки — нет."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Silent with Dissolve( my_dissolve_01 )
    
    "И нижнее белье, пожалуй тоже, стоит Касуми поменять."
    "Я вспомнил, как в детстве с мальчишками плавал в местной речке."
    "Плавки под одеждой, часа два сохли, несмотря на жаркую погоду."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Придётся домой сходить... Ну хоть сможете отдать тележку моей тёте лично в руки, Танака-сан."
    
    show Day_Kasumi_School_Uniform_Wet_Hold_Towel_Without_HairBand Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Мне, встречаться с тёткой Касуми не очень то и хотелось. Но что оставалось делать?"
    "Не мог же я пригласить Касуми к себе домой, чтобы просушить одежду?"
    "Вообще, я думал об этом."
    "В аниме, или комиксах я сотни раз видел такую ситуацию, когда девушка попадает под дождь, а заботливый главный герой приглашает её к себе домой."
    "Сушит одежду в сушилке, а на замену предлагает вещи своей сестры, или даже свои собственные, всякое бывает."
    "Но то речь о ровесниках, школьниках.У нас с Касуми всё немного по другому."
    
    scene Day_Kasumi_Home with Dissolve( my_dissolve_05 )
    
    "Через час мы оказались на месте."
    "Одежда Касуми ещё на половине пути просохла и потеряла свойство просвечивать. То, что Касуми недавно окатили водой — теперь бы никто и не узнал."
    "Девушка прекратила укрываться полотенцем, и просто несла его в руках. Я вернул ей \"ёмкостное реле\"."
    
    "Во дворе дома всё было как и вчера. Разве что в этот раз мне пришлось таки ступить на его землю."
    "Всю сегодняшнюю похмельную ночь и утро, этот двор представлялся мне как место собственной казни."
    "А сейчас — вроде ничего, не очень то и страшно."
    
    "Нет, страшновато конечно, но сейчас то я знаю, никто нарочно на меня зла не держит."
    "Надеюсь моя маскировка сработает, и я тётке Касуми покажусь не настолько пропащим человеком, насколько я им являюсь."
    
    "Во дворике стоял особый, приятный запах, которыми благоухают помидорные кусты."
    "Но как только мы поднялись на крыльцо, я уже почувствовал аромат сигарет."
    "Вообще, сигаретный дым сочетается с помидорным запахом, так мне показалось."
    
    "Касуми между тем открыла входную дверь и мне пришлось войти влед за ней в темноту дома."
    
    scene black_image with Dissolve( my_dissolve_05 )
    
    kenji "Простите за беспокойство!"
    
    "Сказать я это попытался как можно громче, чтобы те, кто находился дома, расслышали что к ним пришел гость."
    "Но от волнения что-то опять случилось с моим голосом, и он прозвучал еле - еле."
    "Да и шумно было в доме, из прохода в комнату, доносилось бубнение работающего телевизора."
    "Как я и предполагал, пахло сигаретами в доме Касуми ничуть не хуже чем в той каморке, в которой я встретился со служащим мусорки."
    "В тёмной прихожей, я и Касуми сняли обувь."
    
    scene Day_Kasumis_Home_Aunt_Room with Dissolve( my_dissolve_05 )
    
    "После я вышел на свет, в небольшую комнату."
    
    #Мини-ЦГ - Бэк за спрайтом тётки
    image Kasumis_Aunt_Sprite_SubBG_Moved:
        contains:
            "black_image"
            alpha 0.6
    
    image Kasumis_Aunt_Sprite_SubBG_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -1000
    
    image Kasumis_Aunt_Sprite_SubBG_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -1000
    
    image Kasumis_Aunt_Sprite_SubBG_Masked = AlphaMask( "Kasumis_Aunt_Sprite_SubBG_Moved", "Kasumis_Aunt_Sprite_SubBG_border_01_left_mask_moved" )
    
    image Kasumis_Aunt_Sprite_SubBG_With_Border_01:
        contains:
            "Kasumis_Aunt_Sprite_SubBG_Masked"
        contains:
            "Kasumis_Aunt_Sprite_SubBG_border_01_left_moved"
    ##
    show Kasumis_Aunt_Sprite_SubBG_With_Border_01 with Dissolve( my_dissolve_02 )
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "На кресле, напротив телевизора, сидела пожилая женщина с короткими седыми волосами. Одета она была в домашнее кимоно."
    
    "Женщина эта, была словно с иллюстраций про вредный образ жизни."
    "Во рту она держала сигарету, а в руках — стакан с тёмной жидкостью, очевидно алкоголем."
    "На небольшом столике перед ней, стояла бутылка сливового портвейна и тарелка с сушёными морепродуктами."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "Касуми? Кто это с тобой?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Простите за беспокойство..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    kasumi "Это Танака-сан, тётя. Я же говорила вчера"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Тётка Касуми, задумалась, пожевывая сигарету."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "А, конечно, Касуми говорила мне. Говорила, что вы помогли ей. Большое спасибо!"
    kasumis_aunt "Хорошо что находятся люди, которые помогают племяннице в её делах. Ах да, моё имя. Миура Усаги."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Тётка Касуми подняла стакан, словно хотела показать, что выпьет его в мою честь."
    "Выпивка в стакане весело заплескалась и забулькала."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Вы опять пьёте... Хотя бы при постороннем человеке..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "Прости Касуми, но откуда же я знала что ты приведёшь гостя? А это вино! Если бы оно простояло в холодильнике ещё ночь, у него вкус был бы как у уксуса!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Какой достойный повод, чтобы выпить..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Smile_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "В ответ тётка улыбнулась и подмигнула мне. А я внезапно ощутил такую лёгкость, словно сам выпил кружку этого винца."
    
    "Вот женщина, которую вчера и сегодня я так боялся."
    "Я представлял её себе как властную, строгую женщину. Которая примется изучать меня и выпытывать, чего это я брожу по улицам, к девчонкам молодым пристаю."
    "Но нет, у тётки Касуми характер добрый и весёлый. И не только не строгая она, а ещё и порокам подвержена похлеще чем я."
    
    "Вспомнились давние события, когда я учился еще в младшей школе."
    "Когда по пятницам, к отцу приходили коллеги по работе, и хорошенько поддавали."
    "И стоило мне оказаться рядом с ними в то время -  меня одаривали деньгами и сладостями и хвалили мои посредственные успехи в школе."
    "По моему, люди становятся намного лучше, когда выпьют."
    "И даже когда тётка Касуми таки заинтересовалось моей персоной, меня это нисколько не напрягло."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "И кто же твой новый знакомый, Касуми? Вы ещё в школе учитесь? Или в университете, студент?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Кажется моя маскировка сработала! Звание студента мне очень подходило."
    
    kenji "Да, Усаги-сан, я студент."
    
    "Я озвучил название своего учебного заведения. Я не соврал, я в самом деле когда-то закончил его. Семь лет назад."
    "Это был достаточно известный университет, хоть и не Токийский но тоже неплохой."
    "На тётку Касуми он произвёл сильное впечатление."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "О! Когда я училась в школе, в этот университет смогли попасть только пара ребят из нашего выпуска! А на кого вы там учитесь?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Филологический факультет. Я переводчик."
    
    "Тётка Касуми удивилась ещё больше."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "Ого! Переводчик! С китайского?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "С английского!"
    
    "От удивления, тётка Касуми чуть не выронила стакан. Пусть говорят, что Английский - легкий язык."
    "Но здесь, в Японии, владение английским вызывало уважение."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "Английский! Вот это да! Ох, в школе мы тоже учили английский. Правда уже и не помню почти ничего... Может только..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Она замолчала и задумалась. Видимо попыталась вспомнить хоть какую-то реплику на иностранном языке."
    "Голос Касуми перерезал тишину."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Тётя! Пожалуйста..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Женщина решила послушаться свою племянницу, и промолчала. Налила себе ещё стаканчик портвейна и осушила его."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "Что же ты не сказала мне, Касуми? Что приведёшь домой такого успешного молодого человека? Я бы хоть подготовилась."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я просиял, услышав, какими титулами наградила меня тётка Касуми."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Как же, смогли ли вы хоть день продержаться без выпивки?"
    kasumi "Вчера вас не было дома, и я уже хотела воспользоваться случаем и предложить Танаки-сану выпить чаю."
    kasumi "А сегодня, так получилось, нам срочно надо было попасть домой."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back_Without_Headband Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Может быть Касуми стеснялась своей тётки, хотя она и не подавала вида."
    "Она могла бы оставить меня на улице, во дворе. Но наверное это было невежливо."
    "В то же время и мне невежливо вот так, вламываться в дом к людям когда они не готовы принимать гостей."
    "Но судя по всему, тётка Касуми заядлый алкоголик. И была пьяна уже достаточно, чтобы не стыдиться своих пороков перед посторонними людьми."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumis_aunt "А вот чаю, пожалуй, стоит выпить!"
    
    scene Day_Kasumis_Home_Aunt_Room with Dissolve( my_dissolve_05 )
    
    "Никто не стал возражать. Меня усадили перед столом, с которого тётка Касуми убрала свою выпивку и закуску."
    "Обслуживала нас по видимому Касуми, она скрылась за дверь, очевидно на кухне.Оттуда Раздавался звон посуды и шипение закипающего чайника."
    "Я же, совершенно расслабился и чувствовал себя в своей тарелке."
    "Может никотина в стенах и воздухе этого дома накопилось столько, что он начал на меня действовать?"
    
    "Пока длилось молчание, я оглядывал комнату. Видно было, что тётка Касуми мало занимается домашней работой."
    "Под ногами, нет нет да и попадалась мне грязь. Кое-где мебель была покрыта пылью, которую похоже не замечали."
    "Обои — пожелтели от времени, покрылись пятнами вокруг электрических розеток."
    "Стул на котором я сидел — шатался, стол похоже тоже. Да и скатерть на нём была не совсем чистая."
    
    "Но, глядеть на всё это мне было только приятно."
    "А что если бы Касуми была дочерью состоятельных родителей, которые встретили меня в ухоженном особняке?"
    "Да на меня бы там посмотрели как на насекомое и за порог не пустили."
    
    "А здесь всё наоборот. Я сам жил в приличном и ухоженном доме. Конечно, благодаря Айко он не терял свой товарный вид, а платил за всё это удовольствие отец."
    "Но чёрт с ними! Сейчас я себя чувствовал может и не как аристократ в лачуге обычных людей."
    "Но никак не хуже чем первый среди равных, это точно."
    
    #Мини-ЦГ Касуми с подносом
    image Kasumi_With_Tray = "images/cg/DAY_02/04a_Kasumis_Home/Kasumi_With_Tray/Kasumi_With_Tray.png"
    image Kasumi_With_Tray_Moved:
        contains:
            "Kasumi_With_Tray"
            xpos -600
    
    image Kasumi_With_Tray_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -900
    
    image Kasumi_With_Tray_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -900
    
    image Kasumi_With_Tray_Masked = AlphaMask( "Kasumi_With_Tray_Moved", "Kasumi_With_Tray_border_01_left_mask_moved" )
    
    image Kasumi_With_Tray_With_Border_01:
        contains:
            "Kasumi_With_Tray_Masked"
        contains:
            "Kasumi_With_Tray_border_01_left_moved"
    ##
    show Kasumi_With_Tray_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Касуми расставила перед нами три чашки и чайник, небольшой поднос с рисовым печеньем."
    "Я рассеяно наблюдал, как она ощупывала нутро чайных чашек. Похоже ей не понравилась их чистота."
    
    scene Day_Kasumis_Home_Aunt_Room with Dissolve( my_dissolve_02 )
    
    "Не знаю, кто в этом доме моет посуду, сама ли Касуми или её тётка."
    "Но чашки и в самом деле были вымыты неважно, и все покрыты тёмным налётом от предыдущих чаепитий."
    "Да уж! У меня дома, Айко бы такого безобразия не допустила!"
    
    "Касуми тихонько покачала головой и разлила чай по чашкам."
    "Но сама за стол не села, опять скрылась в дверях комнаты."
    
    show Kasumis_Aunt_Sprite_SubBG_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Похоже Касуми за чем-то пошла в свою комнату..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Тётка Касуми, поднесла чашку чая к губам, отпила чуть - чуть, поморщилась, запустила в подол кимоно руку и достала оттуда маленькую блестящую фляжку."
    "Налила несколько капель из фляжки в чашку, отчего чай в ней потемнел."
    "Затем обратилась ко мне."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Танака-сан, а сколько вам лет?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Я спешно принялся придумывать себе возраст."
    "Надо было и не слишком малый взять, и уложиться в срок обучения в университете."
    
    kenji "Двадцать.. два..."
    
    "Тётка Касуми довольно улыбнулась, и потянула руку с фляжкой в сторону моей чашки с чаем."
    "Я уловил это движение и замахал руками в знак протеста."
    
    kenji "Ой! Спасибо! Не нужно! Я не пью!"
    
    "Судя по запаху, который теперь витал над столом, во фляжке у неё был крепкий коньяк, а может виски."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Надо же! Похвально! Я не одобряю вредные привычки!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Она принялась пить чай по своему рецепту."
    "Я тоже хотел было приняться за чай, но Касуми всё не было. Её тётка похоже поняла мои мысли."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Не волнуйтесь, Касуми сейчас придёт."
    kasumis_aunt "Наверное опять чудит над чем-то в своей комнате. Вечно у неё какие-то дела!"
    kasumis_aunt"И мне даже ничего не говорит! Хотя... если и говорит, я ни слова понять не могу..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Я тоже, в разговорах с Касуми мало чего понимал, поэтому закивал, соглашаясь."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Может она вам сказала, что ей понадобилась?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Я решил не утаивать то происшествие, что произошло на улице."
    
    kenji "Какие-то хулиганы обрызгали Касуми водой. Жаль я в это время был далеко, не углядел. Эх! Поймать бы их, да в полицию бы!"
    
    "Тётка отхлебнула из чашки, и задумчиво произнесла."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Да... Как уже достали эти хулиганы... И чего они пристали к этой бедной девочке? Чем она им мешает? То водой обольют, то подножку поставят..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Так это что, не в первый раз?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Не в первый... Причём Касуми и не говорит ничего. Соседи передали. Видели  как мальчишки помладше нападают на неё."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Вот ведь сволочи!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Да зачем же вы так про них, Танака-сан. Знаете, я думаю — все они хорошие, добрые ребята."
    kasumis_aunt "А делают это, потому что их попросили. Может быть даже заплатили."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Я вспомнил слова того упитанного хулигана, которого мне удалось поймать."
    "Он же в самом деле говорил что ему за это дело заплатили. Он что, не врал?"
    
    kenji "Как? Кто такое может делать. У Касуми есть враги?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Есть."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "И вы их знаете?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Я знаю? Конечно знаю!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Кто же это?"
    
    "Женщина воровато оглянулась по сторонам. Прошептала."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Рептилоиды!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Я был ошарашен таким ответом, и не знал как мне реагировать."
    "Тётка, воспользовавшись паузой достала из под стола бутылку вина, налила и выпила ещё стаканчик."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Да, да, рептилоиды. Это они пакостят! Это они следят за мной и Касуми."
    kasumis_aunt "Мне кажется, они даже поливают какой-то гадостью мои помидоры."
    kasumis_aunt "Да что там помидоры! Они воздействуют излучением напрямую в мозг! И есть только один способ этого избежать!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Тётка Касуми указала на бутылку вина, стоящую под столом."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "А всё почему, Танака-сан? Потому что я много знаю про них! Про все их подлые делишки, и про их ужасные планы."
    kasumis_aunt "Я знаю очень много. И поэтому они охотятся за мной!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Серьёзный тон, с которым тётка Касуми рассказывала эти небылицы, меня напугал."
    "Надеюсь у тётки Касуми не началась белая горячка? Надеюсь она не заподозрит во мне — шпиона от рептилоидов!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Только не передавайте Касуми мои слова, Танака-сан! Не знаю почему, но не любит она когда я завожу такие разговоры."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Нет, нет! Что вы!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Я просила Касуми, не выходить на улицу, раз такое дело. Но она всё равно."
    kasumis_aunt "Железки какие-то приносит, собирает что-то непонятное..."
    kasumis_aunt "Но хоть польза есть от этого. Если что дома ломается — Касуми чинит в минуту. Даже в розетки не боится лезть."
    kasumis_aunt "Жаль не всё ей по зубам. С вентилятором этим, возилась, возилась... А толку не вышло..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Потому что обмотки сгорели! "
    kasumi "Что я могу сделать? Перемотать? Там всё лаком залито, не получится. Только выбросить."
    kasumi "А всё из-за того, что вы уронили его на пол включенный и уснули. Вот и сгорел он."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Касуми появилась перед столом совершенно внезапно."
    
    #Мини-ЦГ Тётка и Касуми за столом
    image Kasumi_And_Aunt_Tea_Tine = "images/cg/DAY_02/04a_Kasumis_Home/Tea_Time/Tea_Time.png"
    image Kasumi_And_Aunt_Tea_Tine_Moved:
        contains:
            "Kasumi_And_Aunt_Tea_Tine"
            xpos -900
            pause 1.0
            linear 10 xpos -300
    
    image Kasumi_And_Aunt_Tea_Tine_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Kasumi_And_Aunt_Tea_Tine_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Kasumi_And_Aunt_Tea_Tine_Masked = AlphaMask( "Kasumi_And_Aunt_Tea_Tine_Moved", "Kasumi_And_Aunt_Tea_Tine_border_01_left_mask_moved" )
    
    image Kasumi_And_Aunt_Tea_Tine_With_Border_01:
        contains:
            "Kasumi_And_Aunt_Tea_Tine_Masked"
        contains:
            "Kasumi_And_Aunt_Tea_Tine_border_01_left_moved"
    ##
    scene Day_Kasumis_Home_Aunt_Room with Dissolve( my_dissolve_02 ) 
    show Kasumi_And_Aunt_Tea_Tine_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "Она села напротив меня, а тётка подала ей чашку чая и поближе к ней подвинула поднос с печеньем."
    
    kasumi "Я надеюсь вы по ошибке не налили мне в чай эту гадость, тётя?"
    
    "Тётка Касуми тихо засмеялась."
    
    kasumis_aunt "Ну что ты, дорогая, это было всего раз и совершенно случайно!"
    
    "Похоже тётка Касуми иногда допивается до такого состояния, что забывает перед сном выключать бытовые приборы. И подливает свое зелье во все чашки что видит.."
    "Да уж..."
    "На некоторое время разговоры притихли, раздавался только хруст печенья, бульканье чая и бормотание телевизора."
    "Молчание прервала тётка Касуми."
    
    kasumis_aunt "А! Да! Касуми! Что-то с телеком! Показывает только двадцать каналов."
    kasumi "Вы опять открывали окно? Я же говорила много раз, не трогать антенну."
    kasumis_aunt "Да я помидоры выкладывала на подоконник, чтобы дозревали. А потом обратно всё задвинула!"
    
    "Я заметил что на оконной занавеске, была закреплена антенна, очевидно самодельная, сделанная из проволоки."
    
    kasumi "Вы наверное погнули её! А тут, чтобы второй мультиплексор ловило, надо точно настраивать. Потом сделаю, вечером."
    kasumis_aunt "Эх мультиплексор... Сегодня должны были показать замечательную передачу. "
    kasumis_aunt "Говорят — в правительстве Японии завелись инопланетяне... Какую только чушь не показывают, правда, Касуми?"
    
    "Тётка Касуми снова достала фляжку с коньяком из под кимоно. Но в этот раз не налила его в чай а принялась пить прямо из горла."
    
    scene Day_Kasumis_Home_Aunt_Room with Dissolve( my_dissolve_03 )  
    
    "Касуми же хлопнула чашкой по столу и встала."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Пожалуй нам пора! Танака-сан? Или хотите ещё чаю?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Нет! Большое спасибо!"
    
    "Я тоже поднялся со своего стула."
    "Тётка Касуми припрятала фляжку и спросила с удивлением."
    
    show Kasumis_Aunt_Sprite_SubBG_With_Border_01 with Dissolve( my_dissolve_02 )
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Уже уходите?"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kasumi "Да. У нас дело."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent at Move( ( 1500, 600 ), ( 1500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "У вас? Танака-сан, надеюсь Касуми вас не мучает своими просьбами?"
    kasumis_aunt "Большое спасибо, что помогли ей вчера! Но вы же не можете делать это вечно!"
    kasumis_aunt "Касуми! Надеюсь ты не доставляешь много хлопот Танаке-сану? Сама знаешь, в таком приличном университете, наверное и летом надо уделять внимание учёбе."
    kasumis_aunt "А ты со своими пустяками..."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Касуми промолчала, а я замахал руками."
    
    kenji "Нет! Нет! Что вы! У меня сейчас полно свободного времени."
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Say at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumis_aunt "Ну и славно. По правде сказать, я очень довольна что Касуми теперь не шляется по улицам одна. Я так за неё беспокоюсь!"
    
    show Day_Kasumi_Aunt_Home_Outfit_Sit_On_ArmChair_With_Glass Normal_Silent at Move( ( 400, 600 ), ( 400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "С этими словами она потянулась руками под стол, и принялась выискивать там бутылку с портвейном."
    
    scene black_image with Dissolve( my_dissolve_03 )
    
    kasumi "Как же, беспокоитесь вы..."
    
    scene Day_Kasumi_Home with Dissolve( my_dissolve_05 ) 
    
    "Вышли на улицу и я с удовольствием вдохнул знойный летний воздух с ароматом помидорных кустов."
    "Пусть и не страшился я больше тётки Касуми, сидеть с ней да разговаривать о разном не очень то и хотелось."
    "Здесь, на улице, наедине с Касуми — лучше."
    
    "Может я нанюхался дыма, или тётка Касуми таки успела мне плеснуть чего в чашку, но состояние у меня вдруг стало такое, словно я выпил баночку пива."
    "Я чувствовал себя как студент сдавший трудный и важный экзамен, последний в сессии, после которого — летние каникулы."
    
    "А экзаменатор оказался не строгим и дотошным а весёлым, ставящим хорошие отметки за просто так. А я ещё боялся чего то!"
    "Да я теперь не только не боялся! Не просто чувствовал себя в доме Касуми, как среди равных, нет."
    "Я чувствовал превосходство!"
    
    "Над этой пожилой женщиной, сидящей в грязном кимоно, пьющей дешёвый алкоголь, смотрящей третьесортные телепередачи и ведущей охоту на рептилоидов."
    "Да и над Касуми тоже, превосходство чувствовал. Вспомнилось, как она торопливо ощупывала грязные чашки и как украдкой отряхивала ступни от грязи, когда надевала обувь в прихожей."
    
    "Видно, что Касуми стесняется своей пьющей тётки, и беспорядка в доме."
    "Конечно, Касуми ни в чём не виновата, даже наоборот... Да и мне самому, неловко от всего этого, и жалко Касуми."
    "Но каким же приятным было это чувство жалости!"
    
    "Вот значит как дело обернулось!"
    "Единственный человек, который мог заступиться за Касуми. Единственный, кто мог раскусить меня как безработного хикикомори и запретить мне общаться с этой слепой девчонкой — принял своего врага с распростёртыми объятиями."
    "Да и какой же я хикикомори? Я же студент, престижного университета и одного из сложнейших факультетов между прочим!"
    
    "Пусть это было уже давно, но разве я соврал?"
    "Нет!"
    "Подумаешь - что столько просидел дома, я может быть просто поздно повзрослел! И вот сейчас самое время, выйти в люди и стать полноправным членом общества."
    
    scene Day_Another_Station with Dissolve( my_dissolve_05 ) 
    
    "Пока я предавался мечтам, мы вышли на железнодорожный вокзал, а точнее на местную маленькую станцию."
    "Перрон был пуст. Направление всё-таки не популярное — за город. Сейчас все ещё на работе, и возвращаться обратно в пригороды начнут только к вечеру."
    
    "Поезда мы ждали молча."
    
    "Я не знал, о чём можно завести разговор, да и нужно ли?"
    "Вчера и утром, я в моменты такого молчания пытался придумать какую-то интересную тему для разговора."
    "А что сейчас? Сейчас мне это не казалось обязательным."
    "Зачем?"
    
    "Куда спешить, обязательно ли из кожи вон лезть, чтобы показаться весёлым и интересным?"
    
    "Теперь я думал о будущем."
    "Хотя бы о завтрашнем дне."
    "Надо наверное сходить куда-то с Касуми, пригласить её, может в кафешку какую. Или  помочь с другими её делами?"
    "Ходит же она в магазин, за своими железками, например?"
    
    "Или даже пригласить домой, глянуть на то, что ещё осталось из вещей дяди Макото."
    "В прочем, домой это потом, чуть позже."
    
    "В голове я проигрывал мои будущие победы на личном фронте."
    "Каким я буду галантным и обходительным, как буду производить впечатление на Касуми своими поступками. Или даже знаниями!"
    "Да, надо непременно почитать хоть что-то по теме радиотехники."
    "Может даже съездить в город, и найти там эту книгу, что я видел вечером на сайте книжного магазина?"
    
    "Я глупо улыбался и с умилением глядел на Касуми."
    
    #Мини-ЦГ - Касуми стоит в тени, на платформе
    image Kasumi_On_Platform = "images/cg/DAY_02/05a_Train_station/Kasumi_On_Platform/Kasumi_On_Platform.png"
    image Kasumi_On_Platform_Moved:
        contains:
            "Kasumi_On_Platform"
            xpos -600
    
    image Kasumi_On_Platform_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -900
    
    image Kasumi_On_Platform_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -900
    
    image Kasumi_On_Platform_Masked = AlphaMask( "Kasumi_On_Platform_Moved", "Kasumi_On_Platform_border_01_left_mask_moved" )
    
    image Kasumi_On_Platform_With_Border_01:
        contains:
            "Kasumi_On_Platform_Masked"
        contains:
            "Kasumi_On_Platform_border_01_left_moved"
    ##
    show Kasumi_On_Platform_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Она стояла на краю платформы, смотрела куда-то в сторону уходящих путей."
    "В тени, лицо Касуми было таинственным, глаза она чуть прикрыла, и мне почему-то казалось что она улыбается."
    "Совсем незаметно."
    "Как Мона Лиза."
    
    scene Day_Another_Station with Dissolve( my_dissolve_03 ) 
    
    "Мне ужасно захотелось сделать фотографию Касуми."
    "Отличный ракурс, и свет получался. Такой удачный кадр бы вышел."
    "В прошлый раз, шмель помешал, и про фотографию я совсем забыл."
    "А теперь случай удачный подвернулся, чтобы сделать снимок — на перроне никого."
    
    show Crazy_Phone_01
    
    "Я достал из кармана телефон, осторожно, чтобы не создавать лишнего шума и не отвлекать Касуми."
    "Выбрал серийную съёмку и навёл видоискатель на цель."
    
    scene Crazy_Another_Station
    show Crazy_Phone_02
    hide Crazy_Phone_01
    
    someones_cry "Караул! На помощь! Извращенец!"
    
    "Внезапный крик резанул по ушам, у меня потемнело в глазах от страха и неожиданности."
    
    show Crazy_Phone_03
    hide Crazy_Phone_02
    
    someones_cry "Спасите! Это извращенец!"
    
    "Только сейчас я понял, что эти громкие крики доносились из моего телефона."
    "Он трепыхался в моих дрожащих и мокрых от пота ладонях."
    
    show Crazy_Phone_04
    hide Crazy_Phone_03
    
    kenji_phone "Извращенец! Педофил! Вызовите полицию!"
    
    "Что за чертовщина с моим телефоном?! Какого хрена из него доносятся эти крики?"
    "Я принялся давить на качельку громкости, чтобы убавить звук, но не тут то было."
    "Я жал на кнопку выключения, но телефон продолжал верещать на всю улицу."
    
    show Crazy_Phone_05
    hide Crazy_Phone_04
    
    kenji_phone "Педофи-ил! Поли-иция!"
    
    scene Day_Another_Station with Dissolve( my_dissolve_01 ) 
    
    "Не с первого раза, но у меня получилось сорвать заднюю крышку телефона и выцарапать аккумулятор."
    "Телефон мгновенно умолк."
    "В ушах у меня звенело и билось сердце. А Касуми отскочила от меня на добрые два метра."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    "Вид у неё был испуганный."
    "Как только мне удалось справиться с телефоном, она, заикаясь спросила."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumi "Та... нака... сан... Что это... было?!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kenji "Это... это..."
    
    "И в самом деле, что это чёрт возьми такое?!"
    "Впрочем, вопли эти мне были знакомы."
    "Такие звуки издавал \"отпугиватель извращенцев\" - брелочек, который носили с собой ученицы младшей школы."
    "Такие брелочки цепляли к ключам, сумочкам. И если вдруг какой извращенец поймает маленькую девчонку в тихом месте, зажмет ей рот."
    "Или если от страха её голос перехватит — нажмёт девочка кнопочку и  брелочек заорёт на всю улицу. А извращенец — сбежит."
    
    "Я сам видел такие, правда когда в школе учился — таких у наших девчонок не было, не изобрели ещё."
    "А вот у Айко таких штук  навалом."
    
    "Не понял я правда, почему эти звуки доносились из моего телефона. Что за шутки?"
    
    kenji "Это брелок..."
    
    "Было совершенно непонятно, какого черта телефон так заверещал."
    "А Касуми наверное и вовсе не поняла, что это тут у меня и вопросительно молчала."
    
    kenji "Это брелок... сестры!"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Say at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kasumi "Сестры?! Это что? Который защитный, для детей? От хулиганов?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Surprised_Silent at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    "Похоже Касуми знала про существование таких штуковин."
    
    kenji "Ага! Кажется я... я перепутал и взял с собой ключи от дома, не свои... сестры. А тут брелок этот..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    kasumi "Ох... Это было так внезапно..."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_01 ) 
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    "Конечно внезапно. Я сам чуть концы не отдал от этих воплей."
    "По рукам и ногам бегали мурашки, рубашка прилипла к вспотевшей спине."
    "В дрожащих руках я сжимал телефон и аккумулятор от него."
    "Собирать телефон я не решился и сложил его в разобранном виде в карман."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 ) 
    
    kasumi "Как же вы не заметили, Танака-сан? С такими вещами надо аккуратнее, не слышал ли кто..."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    "Да уж, этого я тоже боялся."
    "Конечно, телефон он и есть телефон, кричит не так громко как брелочек. Но всё равно, мог кто и услышать."
    "Я оглядывался по сторонам, но никого постороннего не увидел."
    "Похоже что свидетелем этого вопля остались только я и Касуми. И это хорошо."
    "Не хотелось бы разъяснять посторонним или полиции, что да как, и что это просто случайность."
    
    kenji "Да уж. Хорошо что на перроне никого нет."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 ) 
    
    kasumi "А у вас... Есть сестра, Танака-сан?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    kenji "Ага! Правда она мне не родная, сводная."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 ) 
    
    kasumi "Не родная?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    "Я рассказал Касуми про Айко. Про её и своего отца."
    "Правда умолчал некоторые подробности о нашей жизни, в основном связанные с моим безвылазным сидением дома."
    "Наверное не стоило мне рассказывать и другие подробности. Мог бы сказать что Айко — моя родная сестра. Это бы пошло на пользу моему образу студента!"
    
    "Если моей сестре так мало лет, ну разве мой возраст может быть больше двадцати?"
    "Впрочем, когда то, может быть даже очень скоро, Айко придётся познакомить с Касуми. И неправда раскроется."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 ) 
    
    kasumi "Так вот значит кем вам приходится Макото-сан... А ваша сестра, она не была против, что вы выносите старые вещи её отца?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    kenji "Айко то? Маленькая была она совсем, когда он погиб. Не помнит его. Поэтому начихать ей на его вещи. Пока я мусор выносил, она смылась из дома, с подружками."
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_01 ) 
    
    kasumi "С подружками?"
    
    show Day_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 ) 
    
    kenji "Ага."
    
    "Хорошо бы, чтобы я сейчас вдруг не встретился с Айко и её подружками. Впрочем на поезде ей ехать некуда."
    "Разве что на море, но на пляж — это совсем в другую сторону."
    
    hide Day_Kasumi_School_Uniform_Hands_Behind_Back with Dissolve( my_dissolve_03 ) 
    
    "А то что Касуми спросила про Айко и её отца. Наверное сама Касуми переживает из-за смерти своих родителей."
    "Может, конечно, как и у Айко, умерли они очень давно и она их не помнит совсем."
    "Вдруг, замигали семафоры на путях, зашипел, засвистел рупор в дальнем конце перрона."
    "Похоже там что-то объявляли, но нечего не было слышно. Однако, судя по расписанию это был наш поезд."
    
    scene Day_Shaked_Train with Dissolve( my_dissolve_05 ) 
    
    "Всю дорогу в поезде, меня занимали мысли о странном поведении моего телефона."
    "Надо же, так учудил и прямо в такой момент! Ну просто закон подлости какой-то!"
    "Я рылся в карманах, доставал поочерёдно разные запчасти телефона но никак не решался поставить аккумулятор на место и включить его."
    "Вдруг этот мистический глюк проявится снова, и я опять напугаю Касуми?"
    
    "Вообще, этот неприятный случай свалился на меня как ведро холодной воды. Я потерял значительную долю своей бравады и уверенности."
    "Может мы и знакомы с Касуми уже два дня, и так хорошо ладим, но черт его знает, что она может подумать?"
    "Вдруг не поверила, что я в самом деле взял ключи сестры. Вдруг сейчас гадает, откуда у меня этот брелочек? Где я его взял?"
    
    scene Day_Sakura_Station with Dissolve( my_dissolve_05 )
    
    "На остановке где мы вышли — я был впервые."
    "Хотя я вообще не часто езжу в поездах а в этом направлении ехал и вовсе в первый раз."
    
    "Всё здесь было не знакомо, даже воздух тут был свежее и не такой пыльный, как в городе."
    "Я естественно не знал, куда нам надо идти. Точнее, я несколько раз просмотрел маршрут на карте, и вроде как идти требовалось совсем не далеко."
    "Однако карта и реальная жизнь это совсем разные вещи. Да и воспользоваться её прямо сейчас я не решался."
    "Не решался включить телефон и посмотреть точно, куда же нам нужно."
    
    scene Day_Open_Landscape_Static with Dissolve( my_dissolve_05 )
    
    "Впрочем, найти дорогу к нужному месту оказалось совсем несложно."
    "Ещё из поезда, я приметил пару тонких металлических дымовых труб именно в той стороне куда нам надо."
    "Наверняка эти трубы выбрасывали дым от сжигаемого мусора. Это был хороший ориентир."
    "Кроме того — за городом улицы переплетались не в такой запутанный клубок как в городе."
    "И мы шли по одной лишь улице, никуда не сворачивая."
    
    scene Trash_Factory_Gate_Static with Dissolve( my_dissolve_05 )
    
    "Через некоторое время, мы практически вплотную подошли к дымовым трубам."
    "Местность, примерно совпадала с тем что я видел на карте."
    "Бетонный забор, вдоль которого мы шли всё это время, расступился."
    "Ворот здесь не было, только шлагбаум и стеклянная пустая будка охранника."
    "Похоже, что и в этот раз Касуми решила не идти со мной. Оставлять её одну конечно не хотелось."
    "Чёрт его знает, что опять может произойти. Но вряд ли в этой глуши водятся хулиганы."
    "Я внимательно осмотрел пустынную улицу, в поисках подозрительных личностей. Но никого не было."
    "Тогда я оставил Касуми а сам прошёл за шлагбаум."
    
    "Как и ранее, на предыдущем полигоне для мусора, я не увидел ни гор металлолома, ни прессов."
    "Просторная асфальтовая площадка и длинное, трёхэтажное здание с множеством ворот для проезда большой техники."
    "Возможно это был гараж."
    
    "Снаружи здания я никого не заметил, и решил проникнуть внутрь через ворота."
    
    show black_image with Dissolve( my_dissolve_05 )
    scene Day_Trash_Factory_WorkShop_Static 
    show black_image
    
    "После яркого солнечного света на улице, было трудно что-то разобрать в полумраке."
    "Наверное надо было подождать возле шлагбаума. Может быть человек что охраняет вход отлучился ненадолго."
    
    "Вдруг проникать сюда без спросу нельзя? Ещё подумают что я вор или террорист?"
    
    show Day_Dr_Diy_With_Welding_Wires Blacked
    
    "Как бы чего не вышло..."
    
    hide black_image with Dissolve( my_dissolve_05 )
    
    "Темнота немного отступила и я увидел перед собой некую фигуру. Какое-то странное существо стояло перед мной и трясло длинными щупальцуми."
    "Я невольно попятился."
    
    dr_diy_voice "Так вот ты где! Голубчик!"
    dr_diy_voice "Это ты правильно! С такими умениями - тебе сюда!"
    
    "Кажется это существо говорило со мной."
    
    "Я уже готов был дать дёру, но глаза мои похоже совсем привыкли к темноте, и существо это оказалось обычным человеком."
    
    show Day_Dr_Diy_With_Welding_Wires Happy_Silent with Dissolve( my_dissolve_03 )
    
    "Парень в белом халате, примерно моего возраста. Он улыбался во весь рот, и выглядел не очень то и страшным."
    "Правда в руках он держал какие-то непонятные предметы и вид с этими штуковинами у него был грозный."
    
    show Day_Dr_Diy_With_Welding_Wires Happy_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Переменкой сможешь варить?"
    
    show Day_Dr_Diy_With_Welding_Wires Happy_Silent with Dissolve( my_dissolve_01 )
    
    "Похоже этот парень в белом халате говорил со мной. Смотрел он прямо на меня."
    
    kenji "А... мм?"
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Инвертор сдох, только трансформатор остался. Надо на дымососе трещину залатать а-то завтра все надышимся."
    dr_diy "Но железо тонкое, а у нас только троечка. Сможешь тройкой варить?"
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Язык мой почему-то заплетался."
    
    kenji "Н... нет..."
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Всмысле нет? Как нет? И чего ты так смотришь испуганно?"
    
    show Day_Dr_Diy_With_Welding_Wires Angry_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Дебе держак что-ли не нравится? Да ты... Да этим держаком еще мой дед варил!"
    
    show Day_Dr_Diy_With_Welding_Wires Angry_Silent with Dissolve( my_dissolve_01 )
    
    "Парень нахмурился, он почему-то разозлился. Надо было поскорее собирать волю в кулак и говорить членораздельно."
    
    kenji "Н... ет. Я... вы меня с кем-то путаете."
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Так ты не сварщик что-ли?"
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Нет!"
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "А в темноте шаришся прямо как настоящий сварщик!"
    
    show Day_Dr_Diy_With_Welding_Wires Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Нет, я не настоящий."
    
    hide Day_Dr_Diy_With_Welding_Wires with Dissolve( my_dissolve_01 )
    show Day_Dr_Diy_Cross_Arms Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Жалко! Я уже весь день тебя жду. А точнее не тебя, раз ты не сварщик."
    dr_diy "И если ты не сварщик, кто ты тогда?"
    
    show Day_Dr_Diy_Cross_Arms Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Я рассказал про выброшенный прибор, и про свои сегодняшние похождения."
    
    show Day_Dr_Diy_Cross_Arms Normal_Say with Dissolve( my_dissolve_01 )
    
    dr_diy "Хм... Вот значит как... "
    dr_diy "Всё правильно, мусор на переработку отправляется только завтра."
    dr_diy "И повезло тебе, что ты пришел за электроникой. Она у нас в отдельном помещении хранится а не в общей куче. Не думаю что ты захочешь туда лезть."
    dr_diy "Пойдём покажу. Там есть человек который поможет тебе."
    
    scene black_image with Dissolve( my_dissolve_03 )
    
    "Парень в белом халате, повел меня по помещениям мусорозавода."
    "Идти пришлось недолго, скоро мы оказались там, где складировали электронику."
    
    scene Ewaste_Warehouse_Static with Dissolve( my_dissolve_05 )
    
    "По крайней мере, электроники тут было хоть завались. Мы уперлись в глухую стену из компьютеров."
    
    show Day_Dr_Diy_Cross_Arms Normal_Say at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    dr_diy "Эй Наоки! Принимай гостя!"
    
    show Day_Dr_Diy_Cross_Arms Normal_Silent at Move( ( 1400, 600 ), ( 1400, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    show Day_Kreosan_Hands_Down Normal_Silent at Move( ( 500, 600 ), ( 500, 600 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    "Из за стены компьютеров показался человек, очевидно это и был Наоки, который заведовал складом."
    
    hide Day_Dr_Diy_Cross_Arms with Dissolve( my_dissolve_03 ) 
    hide Day_Kreosan_Hands_Down with Dissolve( my_dissolve_01 )
    show Day_Kreosan_Hands_Down Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Парень, что привел меня сюда, объяснил ситуацию Наоки а сам ушел. Наверное торопился встретить своего сварщика."
    "Наоки пожал мне руку."
    
    show Day_Kreosan_Hands_Down Normal_Say with Dissolve( my_dissolve_01 )
    
    kreosan "Это хорошо, что ты выбросил именно электронику! У нас тут под неё настоящий склад, можем месяцами хранить!"
    kreosan "С другим мусором так не церемонятся. А тут всякое бывает, что-то на запчасти, что-то любители раритетов берут или покупают."
    kreosan "В общем — рассказывай что у тебя за прибор."
    
    show Day_Kreosan_Hands_Down Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Я описал прибор. Слушая мои слова, парень заведовавший складом, неуверенно отвел взгляд."
    
    show Day_Kreosan_Hands_Down Confused_Say with Dissolve( my_dissolve_01 )
    
    kreosan "Блок питания для рации говоришь, жёлтый..."
    
    show Day_Kreosan_Hands_Down Confused_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Ага! Там ещё один циферблат сломан, и потёрт он. Слегка..."
    
    show Day_Kreosan_Hands_Down Confused_Say with Dissolve( my_dissolve_01 )
    
    kreosan "Да... Есть такой прибор... Но видишь ли, вещь особая, военная..."
    
    show Day_Kreosan_Hands_Down Confused_Silent with Dissolve( my_dissolve_01 )
    
    "Он почему-то осекся. Меня его поведение немного напугало. Чего-то он темнил!"
    "Оно и ясно что вещь военная, и что с того? Неужели хочет денег с меня взять?"
    "Вообще, не очень то и хотелось платить за этот прибор. Но, что поделать, выбора нет, всё ради Касуми!"
    "Жаль её здесь нет, увидела бы, какой благородный поступок ради неё я сейчас совершу."
    
    kenji "Ну да, военная. Но и старая. И не работает уже, наверное. Кому эта дрянь нужна?"
    
    show Day_Kreosan_Hands_Down Confused_Say with Dissolve( my_dissolve_01 )
    
    kreosan "Да военная и старая! А раньше применяли нестандартные материалы. Благородные металлы, и даже - драгоценные..."
    
    show Day_Kreosan_Hands_Down Confused_Silent with Dissolve( my_dissolve_01 )
    
    "Ба! Драгоценные металлы? Что он хочет этим сказать? Сколько он хочет с меня взять?"
    "Какова доля драгоценностей в этом тяжеленном ящике? Там что, слитки золото внутри?"
    "Нет, это хорошо что Касуми здесь не присутствует. Я не богат, и моей щедрости есть предел."
    
    kenji "Благородные? И даже золото?"
    
    show Day_Kreosan_Hands_Down Confused_Say with Dissolve( my_dissolve_01 )
    
    kreosan "И золото тоже, но это не главное. Часто применяли опасные материалы. И в общем... долго объяснять, вот лучше сам погляди..."
    
    show Day_Kreosan_Hands_Down Confused_Silent at Move( ( 1400, 550 ), ( 1400, 550 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 ) 
    
    "Он кивком головы указал мне в сторону своего стола. Я подошёл к столу поближе."
    "Если честно, я не сразу понял чего он от меня хотел. Я думал что на столе увижу прайс лист или что-то в этом роде."
    "Но на столе было другое, там был настоящий хаос."
        
    #Мини-ЦГ - Разобранный БП на столе
    image Broken_RadioSet_Power_Supply = "images/cg/DAY_02/06a_Trash_Factory/Broken_RadioSet_Power_Supply/Broken_RadioSet_Power_Supply.png"
    image Broken_RadioSet_Power_Supply_Moved:
        contains:
            "Broken_RadioSet_Power_Supply"
            xpos -800
            pause 1.0
            ease 5.0 xpos -300
    
    image Broken_RadioSet_Power_Supply_border_01_left_moved:
        contains:
            "border_01_left"
            xpos -800
    
    image Broken_RadioSet_Power_Supply_border_01_left_mask_moved:
        contains:
            "border_01_left_mask"
            xpos -800
    
    image Broken_RadioSet_Power_Supply_Masked = AlphaMask( "Broken_RadioSet_Power_Supply_Moved", "Broken_RadioSet_Power_Supply_border_01_left_mask_moved" )
    
    image Broken_RadioSet_Power_Supply_With_Border_01:
        contains:
            "Broken_RadioSet_Power_Supply_Masked"
        contains:
            "Broken_RadioSet_Power_Supply_border_01_left_moved"
    ##
    show Broken_RadioSet_Power_Supply_With_Border_01 with Dissolve( my_dissolve_03 )
    
    "Обрывки проводов, осколки микросхем, пригоршни радиодеталей и винтиков и ещё много чего."
    "А посреди всего этого, лежал жёлтый блок питания. Тот самый, с разбитым мной циферблатом и сломанными тумблерами."
    "Верхняя крышка его была снята и он был абсолютно пуст. А то что лежало вокруг него, очевидно в прошлом было его потрохами."
    
    show Day_Kreosan_Hands_Down Confused_Say at Move( ( 1400, 550 ), ( 1400, 550 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 ) 
    
    kreosan "Ты уж извини нас! Вещь была военная и старая."
    kreosan "А в те годы всякое бывало, иногда применялись ядовитые или радиоактивные материалы, полоний например или цезий."
    kreosan "У нас особый приказ по таким случаям — утилизировать немедленно, и если чего опасного найдём — принять меры."
    kreosan "Даже дозиметр для таких случаев имеется. Вот если бы ты вчера пришел, ещё бы успел забрать..."
    
    scene Evening_Shaked_Train with Dissolve( my_dissolve_05 )
    
    "День сменился на вечер, пока мы шли обратно к станции и ждали поезд."
    "Несмотря на мои опасения, Касуми похоже не особо и огорчилось тому, что прибор уничтожен. На лице её не читалось ни капли огорчения."
    "Я уж думал, что придётся мне ободрять её своими силами, после такой неудачи. Но похоже что нет."
    "Да и чем я мог её ободрить? Починить я этот блок питания не мог, другого у меня не было."
    "Теперь, когда сегодняшнее приключение закончилось, пусть и неудачей, ко мне осторожно подкатывало беспокойство."
    "Что же теперь?"
    
    "Прибора нет, а если бы даже и был то ничего особо не разрешилось."
    "Хоть мы и прошли с Касуми за два дня плечом к плечу такое расстояние, но не заметил я что стали мы с ней близки."
    "Вот вернёмся домой, Касуми опять засядет дома за свои радиоприёмники. А мне что делать? Искать её по всем улицам и свалкам, чтобы вновь встретиться?"
    "Нет, так нельзя! Нужно сделать что-то! Нужно проявить инициативу!"
    
    "Точно! Пора пригласить её куда-то. Может в кафе? Или в кино?"
    "Нет, кино пожалуй ей не понравится."
    "Можно просто прогуляться с ней по городу. Можно на море съездить. С Касуми вдвоём не страшно."
    "Только хочет ли Касуми на море? Что вообще можно предложить Касуми?"
    "Эх, жаль я так и не разобрался во всей этой радиоэлектронике. Сейчас бы мигом что-то придумал!"
    "А так, ничего кроме банального кафе или просто прогулки мне в голову не приходило."
    
    "Ну и ладно!"
    "Так и скажу!"
    "Пусть сразу поймёт что это будет свидание, надо же хоть когда-то сделать прямой намёк! И если что — пусть сразу откажет, и я не буду больше страдать."
    "Хожу тут и не ведаю, как она вообще ко мне относится. Тележки чиню, тяжеленные вещи таскаю, от хулиганов спасаю а может всё зря?"
    
    "Вот только сказать такое — не просто. Особенно такому трусу как мне. Как же это сделать?"
    "Начну например так \"А что если нам сходить\"..."
    "Нет. Не пойдёт. Надо быть увереннее, никаких \"А что если...\"."
    
    "Сказать \"может завтра сходим куда?\""
    "Нет, надо обойтись без \"может\". И лучше я сначала спрошу не занята ли Касуми завтра."
    "Да! Точно! В фильмах по крайней мере делают именно так."
    
    "Скажу \"Ты не слишком занята завтра?\" Нет, скажу проще \"Ты не занята завтра?\""
    "Но наверное нельзя говорить так сразу. Надо начала сказать \"Касуми\" и уже потом \"А ты не занята завтра?\""
    "Точно! Сначала скажу \"Касуми...\""
    "Только говорить надо твёрдо и чётко, это очень важный момент!"
    "Я мысленно произнес первую фразу \"Ка су ми\". Затем набрал побольше воздуха в грудь, но вовремя вспомнил о том как облажался утром."
    "Тогда я убавил давление в лёгких на половину. Немного помассировал горло, мысленно сосчитал до трёх..."
    
    show Evening_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Танака-сан!"
    
    show Evening_Kasumi_School_Uniform_Hands_Behind_Back Normal_Silent with Dissolve( my_dissolve_01 )
    
    "От неожиданности я поперхнулся."
    "Хорошо хоть — не раскашлялся, но дыхание перехватило основательно и ответил я почти шёпотом."
    
    kenji "Да?"
    
    show Evening_Kasumi_School_Uniform_Hands_Behind_Back Normal_Say with Dissolve( my_dissolve_03 )
    
    kasumi "Танака-сан! Вы..."
    kasumi "Вы не заняты завтра?"
    
    scene Outdoor_Evening_Kenji_Home with Dissolve( my_dissolve_05 )
    
    "Я даже и не заметил как ноги донесли меня до дома. Как же быстро я шёл! Ух, и как теперь колотилось моё сердце!"
    "Одновременно с биением сердца в ушах, в моей голове играл оркестр. Играл одновременно знакомую и незнакомую мелодию. Играл мне — как победителю."
    
    "Словно я первый пробежал марафон или взобрался на вершину неприступной горы. Или совершил какой-то другой подвиг."
    
    "Касуми конечно, не предложила сходить в ресторан или кино. Я слабо слышал и осознавал её слова, но похоже ей требовалась помощь."
    "Но разве таким не может быть свидание?"
    
    "Наверное Касуми просто не знает, как вести себя с парнями. Да даже если ей просто нужна помощь, и я слишком много о себе думаю, но всё же, она выбрала меня!"
    "Я вспомнил, как Касуми робко спрашивала меня, свободен ли я завтра, и на моём лице засияла улыбка."
    "Наверное как и я, она долго собиралась чтобы спросить о таком. Так мне показалось."
    
    "Пока я шёл домой, я собрал и включил свой телефон. Время он показал уже позднее, хотя сегодня я пришел раньше чем вчера."
    "В такие часы Айко обычно заканчивает готовить ужин."
    
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_05 ) 
    
    "Именно так и оказалось. Айко была на кухне."
    
    #МиниЦГ - Айко фон - мойка
    image Kenji_Home_Kitchen_Washing = "images/cg/DAY_02/07a_Kenji_Evening_Meal/Kenji_Home_Kitchen_Washing/Kenji_Home_Kitchen_Washing.png"
    image Kenji_Home_Kitchen_Washing_Moved:
        contains:
            "Kenji_Home_Kitchen_Washing"
            xpos 500
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kenji_Home_Kitchen_Washing_Masked = AlphaMask( "Kenji_Home_Kitchen_Washing_Moved", "border_01_right_mask_moved" )
    
    image Kenji_Home_Kitchen_Washing_With_Border_01:
        contains:
            "Kenji_Home_Kitchen_Washing_Masked"
        contains:
            "border_01_right_moved"
    
    show Kenji_Home_Kitchen_Washing_With_Border_01 with Dissolve( my_dissolve_03 )
    ##
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Она стояла возле мойки и очевидно собиралась мыть посуду."
    "С одной стороны, присутствие Айко на кухне было очень кстати — я здорово проголодался. С другой стороны, сейчас начнутся её разговоры про клубы извращенцев и прочие небылицы."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Пришел?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ага... Есть чего пожевать?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Сейчас!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Похоже, что Айко забыла про события, что произошли утром. Она без лишних вопросов заставила стол тарелками с едой."
    
    scene Second_Day_Kenjis_Evening_Meal with Dissolve( my_dissolve_05 )
    
    "А затем опять, молча, принялась за вымытую посуду."
    "Правда вела она себя странно. Иногда отворачивалась от мойки, и посматривала на меня как-то испуганно, с недоверием."
    
    "Но лишних вопросов я задавать не стал. Чтобы не сидеть в тишине, я включил телевизор. Всё тот же новостной канал."
    "Правда выпуска новостей сейчас не было, начиналась какая-то авторская передача."
    
    show Ponasenkov_TV with Dissolve( my_dissolve_03 )
    
    tv "Здравствуйте дорогие друзья и враги..."
    
    "С экрана на меня смотрел какой-то зализанный франт, на лице его сияла улыбка до ушей. Физиономия его мне была неприятна."
    
    scene Second_Day_Kenjis_Evening_Meal with Dissolve( my_dissolve_03 )
    
    "Но наверное я сам сейчас выглядел не лучше. Мысли о Касуми и нашем последнем разговоре - невольно вызывали глупую улыбку на моем лице и я щурился как кот на солнышке."
    
    show Kenji_Home_Kitchen_Washing_With_Border_01 with Dissolve( my_dissolve_03 )
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Тебе... кажется письмо пришло..."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко стояла возле мойки и смотрела на меня. О чём это она? Письмо?"
    "Какое ещё письмо? От отца что-ли? Зачем ему понадобилось писать письма?"
    
    kenji "В смысле письмо? Бумажное? От папы что-ли?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ага, бумажное. Нет не от него. И это и не письмо, скорее записка... Была в дверь вставлена. Может ошиблись? Имени не написано."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Если имени не написано, с чего решила что именно мне? Может в самом деле ошиблись?"
    kenji"Может подружки тебе написали? Кто мне то письма писать будет, а тем более записки?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ну не знаю... Я подумала... Вот сам посмотри..."
    
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_03 ) 
    
    "Айко передала мне маленький, сложенный пополам листочек. Похоже что листок был вырван из школьной тетради — он был разлинован в клетку."
    "На такой бумаге записку могли написать ну никак не мне!"
    "Я развернул записку, в ней, мелким и аккуратным почерком было написано."
    
    scene Kenji_Home_Kitchen_With_Letter with Dissolve( my_dissolve_03 ) 
    
    "Эй ты, чучело! Отвали от Касуми!"
    "И подпись - Её парень"
    
    show Kenji_Home_Kitchen_With_Letter_Scary_Animated
    
    "Я с удивлением поднёс листок так близко к глазам, что почуял запах бумаги и чернил."
    "Здесь говорилось про Касуми, это первое что я понял, и уже от одного её имени у меня ёкнуло сердце."
    "И только после, я понял что я чучело, а у Касуми есть парень!"
    "Вот так новости! Мне словно кто-то пинка под зад отвесил, такое было ощущение."
    "Я приблизил листок в плотную к носу и буквы расплылись перед глазами. Листочек шуршал и лихорадочно трясся."
    "Похоже что тряслись мои руки."
    
    scene Kenji_Home_Kitchen_With_Letter with Dissolve( my_dissolve_03 ) 
    
    aiko "Значит тебе эта записка..."
    
    show Kenji_Home_Kitchen_Washing_With_Border_01 with Dissolve( my_dissolve_03 )
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я отодвинул записку от лица и перевёл глаза на Айко."
    "Чёрт! Наверное я отреагировал слишком явно. Она догадалась что записка адресована мне."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Это что же выходит? Это ты чучело?"
    
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_02 )
    
    "И в самом деле — чучелом был я."
    "Вообще, ругательство было странное, девчачье какое-то. Но в то же время било прямо в точку."
    "Если бы оскорбили, сказав что у меня проблемы с ориентацией, это бы, конечно, звучало жёстче. Но в то же время, я бы такое оскорбление воспринял легче чем \"чучело\"."
    "Потому что в глубине души я чувствовал, что я чучело и есть. Отвратительное, тридцатилетнее, безработное чучело, которому в обществе не место."
    
    show Ponasenkov_TV with Dissolve( my_dissolve_03 )
    
    tv "Букашка! Ничтожество!"
    
    "Ещё парочку ругательств добавил парень из телевизора."
    
    scene Evening_Kenji_Home_Kitchen with Dissolve( my_dissolve_02 )
    
    "Но больнее всех ругательств, было видеть подпись автора записки."
    "Оказывается у Касуми есть парень! Я не просто чучело, а чучело, который лезет к чужим девушкам."
    
    show Aiko_With_Kenjis_Phone_Kasumi_Only_Moved with Dissolve( my_dissolve_01 )
    
    aiko "Это Касуми? Это она?!"
    
    "Перед моими глазами вдруг возникла Касуми."
    
    show Aiko_With_Kenjis_Phone_Silent_Moved with Dissolve( my_dissolve_02 )
    
    "Точнее её фото на моём телефоне. Айко размахивала им перед моим носом."
    "Похоже что перед тем как сойти с ума, мой телефон умудрился таки сделать снимок."
    
    show Aiko_With_Kenjis_Phone_Say_Moved with Dissolve( my_dissolve_02 )
    
    aiko "Вот это вот Касуми?"
    
    scene Evening_Kenji_Home_Kitchen with vpunch
    
    kenji "Отдай!"
    
    "Я выхватил телефон из рук сестры, и запихнул его в карман."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_03 )
    
    "Похоже что рявкнул я громко, Айко отскочила в дальний угол комнаты."
    "Пару секунд она испуганно глядела на меня, но быстро пришла в себя."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Значит ты преследуешь её? Эту девушку?"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Чего?"
    
    "Похоже бурная фантазия Айко вновь сработала не туда."
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Я же говорила, сидел бы ты дурень дома!"
    aiko "Вот видишь, её парень заметил тебя. Хорошо что не сообщил в полицию, а сначала предупредил."
    aiko "А ты мне сказал, что будешь фотографировать эти... ре-фе-ренсы. Обманывать нехорошо!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ну ничего! Будет тебе урок!"
    
    show Evening_Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко самодовольно улыбнулась."
    "Мне после получения этой чертовой записки белый свет был не мил. Смотреть же на улыбающуюся физиономию Айко было неприятно до тошноты."
    "Я совершенно не представлял, что ей ответить, как оправдаться. Да я и не хотел ни перед кем оправдываться."
    "Мне хотелось только одного — остаться наедине с самим собой. Поэтому я поспешил покинуть кухню."
    
    scene black_image with Dissolve( my_dissolve_03 )
    
    kenji "Да иди ты к черту!"
    aiko "Ой! Кендзи..."
    
    "Кажется Айко хотела сказать ещё что-то, но я не услышал."
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "Я пулей поднялся на второй этаж, скрылся в своей комнате и запер за собой дверь."
    "Затем я развернул записку которая лежала в руках, перечитал её вновь. Каким же всё-таки аккуратным почерком обладал её отправитель."
    "В голове сразу возник образ парня Касуми."
    
    show Kasumis_Aunt_Sprite_SubBG_With_Border_01 with Dissolve( my_dissolve_02 )
    show Kasumis_BoyFriend_Moved with Dissolve( my_dissolve_02 )
    
    "Наверняка в очках, наверняка с аристократическими чертами лица и манерами. Такого почерка у простачка не будет."
    "Наверняка он очень умный, щёлкает как орешки все районные олимпиады по физике и математике, и метит в престижный университет."
    "Может быть как и Касуми — ученик старших классов и радиолюбитель. А может быть и студент, только не как я а настоящий."
    
    "Да и если честно, парень Касуми мог быть каким угодно. Он мог быть в сто раз уродливее меня."
    "Но я на сто процентов был уверен, что он младше. Гораздо младше меня, именно настолько, чтобы быть парнем Касуми."
    
    "Это только мне нельзя. Тридцатилетнему безработному затворнику."
    "Это только с меня будет спрос, что я делаю, зачем подкатил к молодой девушке. А с него — никакого спросу."
    "Даже если он как и я хиккикомори."
    
    show Kasumis_BoyFriend_With_Hat_Moved with Dissolve( my_dissolve_02 )
    hide Kasumis_BoyFriend_Moved with Dissolve( my_dissolve_01 )
    
    "Или может как Касуми — он инвалид, и может быть вместе с ней, ходит в одну спецшколу?"
    
    "Мысль о том, что парень Касуми, возможно, инвалид принесла мне немного облегчения."
    "Всё-таки не очень красиво обижаться на инвалидов и отбивать у них девушек."
    "Но с другой стороны, говорить мне \"эй ты\", \"отвали\" и называть \"чучелом\"!"
    "Такое трудно простить даже инвалиду!"
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_03 )
    
    "Я вновь перечитал записку. Внимательно рассмотрел каждую букву."
    "Да, почерк красивый, даже не верится что обладатель такого будет писать в столь грубой форме. Мог и помягче объяснить."
    "Откуда я вообще должен был понять, что у Касуми есть парень? На ней же не написано!"
    
    "И вообще, почему записка?"
    "Образ приятного на внешность, интеллигентного парня вновь всплыл в моём мозгу."
    "Ну не мог такой человек решить эту проблему с помощью записки!"
    "Такой отброс общества и трус как я — мог бы. Но не такой как он!"
    "Настоящий парень Касуми, чем он тогда лучше меня?"
    "Почему он не встретился со мной лицом к лицу и не сказал прямо? Почему написал эту оскорбительную записку?"
    
    kenji "Может он боится меня?"
    
    "Эта мысль так меня обрадовала, что я озвучил её сам себе."
    "Точно! Боится меня, боится прямой встречи со мной!"
    "Вот и написал записочку, дескать, чеши Кендзи своей дорогой, и от девчонки моей отстань."
    "Вот только почему он так сделал? Почему испугался меня?"
    "Конечно, где-то в глубине сознания вертелась мысль о том, что я настолько убогий и он просто не хочет марать об меня руки."
    
    "Но мысль эта казалась мне неправдоподобной. Гораздо более правдивой мне казалась другая мысль."
    "Что парень Касуми — ничем не лучше меня. А может даже хуже!"
    "Такой-же, никчёмный хикикомори, может и возрастом меня не обошёл."
    "Вот и боится показаться мне на глаза, чтобы не оказалось так, что я по всем параметрам его лучше."
    
    kenji "Э... Нет братец! Так дело не пойдёт!"
    
    "Конечно, Касуми не видит ничегошеньки, парнем её может стать любой ублюдок."
    "Небось там такое страшилище, что я на его фоне просто Апполон!"
    "Нельзя отдавать ему Касуми, нет. Надо встретиться с ним и решить разговор как настоящие мужчины!"
    "Если уж он действительно ровня Касуми — так и быть, уйду с дороги. А если нет — уйти придётся ему!"
    
    "Но встречаться с парнем Касуми не очень то и хотелось."
    "Была большая вероятность, что окажется он во всём лучше меня."
    "Да и как встретить его? За два дня я его и не видел ни разу!"
    
    kenji "Да уж! Что это за парень то такой? Какой-то тип два дня подряд гуляет с его девчонкой, а он только записочки шлёт и сам не появляется."
    kenji "Как же его встретить? А? А-ха... А-ха-ха-ха-ха!"
    
    "Ещё одна радостная мысль пронеслась в моём мозгу и заставила меня расхохотаться."
    "Я подумал о том, что парень Касуми — и не парень ей вовсе. И вообще никто!"
    "А может быть, как Айко говорит - настоящий её преследователь. Фанат! Сталкер!"
    "Ходит за ней по пятам, следит. Любит наверное её, и ждёт момента к ней подкатить да не решается."
    "А тут понимаешь ли, рядом с ней нарисовался высокопримативный крупный самец."
    
    "Я подошёл к зеркалу, покрутился перед ним. Взъерошил волосы, поправил очки и воротник рубашки."
    "Я казался сам себе очень даже ничего. Да и тётка Касуми подвердила! Хоть и были её глаза залиты алкоголем но кажется я ей понравился."
    "И не разу она не сказала про парня Касуми. Это как же так?"
    "Встречается её племянница с парнем, а потом приводит домой какого-то незнакомца."
    
    "Да и сама Касуми? Кто ей помог вчера и сегодня?"
    "Я!"
    "Кого она попросила о помощи завтра?"
    "Меня!"
    "Точно! Завтра у нас самое настоящее свидание! Какой ещё парень? Да это я!"
    "Я настоящий парень Касуми а не этот трусишка, строчащий записочки!"
    "Я вновь расхохотался."
    
    #Мини ЦГ - дверь в комнату Кендзи, за которой стоит Айко
    image Evening_Kenji_Bedroom_Door = "images/bg/Indoor/Kenji_Bedroom/Evening/Evening_Kenji_Bedroom_Door.png"
    image Evening_Kenji_Bedroom_Door_Moved:
        contains:
            "Evening_Kenji_Bedroom_Door"
            xpos 500
    
    image border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Evening_Kenji_Bedroom_Door_Masked = AlphaMask( "Evening_Kenji_Bedroom_Door_Moved", "border_01_right_mask_moved" )
    
    image Evening_Kenji_Bedroom_Door_With_Border_01:
        contains:
            "Evening_Kenji_Bedroom_Door_Masked"
        contains:
            "border_01_right_moved"
    
    show Evening_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    "Внезапно в дверь постучали, я мигом утих."
    
    kenji "Э... Кто там?"
    
    #Мини ЦГ - звук голоса Айко из-за двери
    image Aiko_Voice_Through_Door:
        contains:
            "empty_image"
        
        contains:
            ypos 395
            xpos 1450
            "Emo_What"
    ##
    
    show Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    aiko "Кендзи? Что у тебя там? Чего ты так хохочешь?"
    
    hide Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    kenji "Ой Айко отстань. Анекдот вспомнил!"
    
    "Айко помолчала несколько секунд, а после спросила."
    
    show Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    aiko "С тобой всё в порядке? Может не надо было мне эту записку тебе показывать?"
    aiko "Зачем же ты фотографировал эту девчонку. Теперь её парень злится на тебя."
    
    hide Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    kenji "Айко! Нет у ней никакого парня. Я её парень! Я с ней встречаюсь! А это какой-то самозванец!"
    
    "Похоже Айко мне не верила, она молча стояла за дверью."
    
    kenji "И завтра у нас свидание!"
    
    show Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    aiko "И ты пойдёшь?"
    
    hide Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    kenji "Пойду конечно, по твоему я кто?"
    
    show Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    aiko "Не ходил бы ты..."
    
    hide Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    kenji "Чего?!"
    
    show Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    aiko "У меня плохое предчувствие... не ходил бы ты."
    
    hide Aiko_Voice_Through_Door with Dissolve( my_dissolve_01 )
    
    kenji "Ох Айко, ещё бы я верил в твоё предчувствие. Не говори мне ерунды. Я могу идти куда хочу!"
    
    scene Evening_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "Айко вздохнула. Послышались её шаги в коридоре а после щёлкнул замок двери в её комнату."
    "На какое-то там предчувствие Айко мне было совершенно наплевать. Меня самого мучило то плохое, то хорошее предчувствие."
    "Весь вечер я думал о том, есть ли у Касуми парень и если да, то какой он."
    
    scene Night_Kenji_Bedroom with Dissolve( my_dissolve_05 )
    
    "К тому моменту, когда я лёг спать, записка превратилась в изодранную и измятую бумажку, с подтёкшими чернилами."
    "Но даже лежа в кровати я то и дело брал её в руки и пытался прочесть в темноте."
    
    jump day_03
