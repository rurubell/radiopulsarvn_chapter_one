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
    "Наверняка в моем уголовном деле, которое вчера легло на стол важному следователю, кроме очевидного заголовка «Танака Кендзи, извращенец и алкоголик» есть приписка «похититель багажных тележек.»"
    
    play sound "sounds/sounds/Room_Door_Lock.mp3"
    
    "Щёлкнул дверной замок."
    
    show Day_Kenji_Bedroom_Door_With_Border_01 with Dissolve( my_dissolve_02 )
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я обернулся. В дверях стояла Айко."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Уже встал, так рано?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ага... Что, завтрак уже?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко улыбнулась и закивала."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Завтрак, завтрак!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Smile_Silent at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ладно, я сейчас."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Smile_Say at Move( ( 1600, 630 ), ( 1600, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Давай!"
    
    scene Day_Kenji_Home_Bedroom with Dissolve( my_dissolve_02 )
    
    "Айко закрыла дверь."
    
    "Я поднялся и надел свою домашнюю одежду."
    "Проходя мимо зеркала, я с трудом удержался от порыва посмотреть в него."
    "Нет, уж лучше не портить себе настроение ещё больше."
    "Ну ладно хоть очки есть… впрочем, зачем они мне? Я отвратительный и никому не нужный хикикомори."
    "Отнесу эту чёртову тележку, извинюсь перед тёткой Касуми и домой. Посижу дома, пока все не устаканится."
    "Пока все не забудут про моё существование."
    "Пока Касуми не повзрослеет и не выйдет замуж."
    "Пока её тётка не сыграет в ящик."
    
    "А остальные вещи дяди Макото сожгу и закопаю на заднем дворе. Черта с два я ещё раз пойду на площадку для мусора!"
    
    
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
    
    show Aiko_Home_Outfit_Yahoo Smile_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Заседание в клубе извращенцев — отменяется!"
    
    show Aiko_Home_Outfit_Yahoo Smile_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я в ответ только покачал головой. Конечно же, Айко не забыла про вчерашнее."
    "Но мне было совершенно все равно. У меня тут совсем другие заботы, ещё я внимание буду обращать на выходки сестры."
    "Я подвинул мусорную урну к столу и смахнул в неё останки от дисков."
    "Только журавлика оставил. Как никак — искусство!"
    
    hide Aiko_Home_Outfit_Yahoo with Dissolve( my_dissolve_01 )
    show Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Наверное Айко ожидала от меня другого поведения."
    "Наверное думала что я буду плакать навзрыд, роясь в этой куче осколков. Но не тут то было!"
    
    scene Kenji_1st_Day_Breakfast_Food with Dissolve( my_dissolve_05 )
    
    "Айко поставила перед мной дощечку для еды и тарелки и осторожно спросила."
    
    #Мини ЦГ - кухонная плита, на фоне которой стоит Айко
    show Day_Kenji_Home_Kitchen_Gas_Stove_With_Border_01 with Dissolve( my_dissolve_02 )
    ##
    
    show  Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты же правда, никуда не идёшь?"
    
    show  Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Не знаю что ты там себе напридумывала. Но мои дела никто не отменял."
    
    "Я взял палочки для еды."
    
    show  Aiko_Home_Outfit_Hand_Hold_Hand Normal_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А как же пиво?"
    
    show  Aiko_Home_Outfit_Hand_Hold_Hand Normal_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Пиво? Оно же закончилось! Я же вчера все выпил!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Да закончилось..."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
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
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Она все ещё не обслужила себя а стояла возле плиты и наблюдала за мной."
    "Никогда бы не подумал, что то что я иду на улицу по делам и при этом совершенно трезвый — может её так волновать."
    
    kenji "Айко. Я надеюсь, этот «клуб извращенцев», ты не веришь в него взаправду?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Confused_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Айко смутилась и отвела взгляд."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Confused_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Я не знаю… Ты так внезапно куда-то собрался."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Confused_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Что поделать! У меня срочные дела!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты сказал что хочешь с кем-то встретиться. С кем?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Если бы я хотел с кем-то встретиться! На самом деле я уже ничего не хотел."
    
    kenji "Ни с кем мне встречаться не надо!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ммм? Что же это за дело такое?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Какая разница? Просто дело и всё!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Значит всё-таки клуб!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Никакой не клуб, я просто..."
    
    "Я похлопал себя по бедру, пытаясь придумать что-то, что бы показалось правдоподобным."
    "Рука моя нащупала в кармане телефон."
    
    kenji "Я иду фотографировать!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Фотографировать?!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Ну да. Фотографировать."
    
    "Я обрадовался тому, что придумал удачную отговорку и принялся было за рис."
    "Айко опять задала вопрос."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "А что фотографировать?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Suspect_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Как что? Референсы!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Чего?"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Surprised_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    "Я поднял вверх указательный палец, чтобы придать себе значительный вид."
    
    kenji "Референсы это фотографии, с которых я буду что-то срисовывать."
    kenji "Не рисовать же всё из головы! Мне нужны референсы! Я буду смотреть на них, чтобы мои рисунки были правдивее."
    kenji "Поэтому надо их сделать, да побольше!"
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Say at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Рисунки..."
    
    show Aiko_Home_Outfit_Hand_Hold_Hand Sorry_Silent at Move( ( 1560, 630 ), ( 1560, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
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
    
    show Aiko_In_Nightie_PonyTails_Without_FlashLight Suspect_Silent with Dissolve( my_dissolve_02 )
    
    "Странно, но на Айко была надета ночная пижама."
    "Вид у моей сестры был хмурый."
    
    kenji "Эй, Айко? Ты чего? Ты не заболела?"
    
    "Айко не ответила."
    
    hide Aiko_In_Nightie_PonyTails_Without_FlashLight with Dissolve( my_dissolve_01 )
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Вдруг она распахнула полы своей пижамы и скинула её на пол."
    "Под пижамой был надет школьный купальник."
    
    "1111"
    
    #
    
    scene Day_Trash_Place with Dissolve( my_dissolve_05 )
    
    "..."
    
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
    show Kasumi_On_Guard_Rail_With_Border_01 with Dissolve( my_dissolve_02 )
    
    "..."
