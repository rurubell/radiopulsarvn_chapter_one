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
    
    kenji "Э? Ты что, в бассейн что-ли собралась? Зачем ты напялила купальник дома?"
    
    "Айко недовольно буркнула."
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Нет, ни в какой бассейн я не иду. Это… ну… референсы!"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Чего?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Сам же сказал, что собрался фотографировать референсы для своих художеств!"
    aiko "А теперь и никуда идти не нужно. Скажи мне спасибо, я сегодня добрая."
    aiko "А на улице будешь фотографировать что не следует, и в полицию попадёшь."
    aiko "Мне, маме и папе такая слава не нужна знаешь ли!"
    aiko "Давай, делай свои фотографии и поскорее покончим с этим. Как мне встать?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Тут то до меня наконец-то дошло, о чем говорила Айко."
    "Конечно же, она видела вчерашний мой рисунок и похоже догадалась за какими референсами я собираюсь пойти."
    "Какие референсы могут понадобиться извращенцу?"
    "Ну конечно же — фотографии молоденьких девчёнок в купальниках, сделанные тайно."
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Say with Dissolve( my_dissolve_01 )
    
    aiko "Так как мне встать?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Suspect_Silent with Dissolve( my_dissolve_01 )
    
    "Я приложил ладонь ко лбу и покачал головой."
    
    kenji "Как цапля встань."
    
    show Aiko_School_Swimsuit_Hands_On_Hips Surprised_Say with Dissolve( my_dissolve_01 )
    
    aiko "Как ц-цапля? Это как?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Никак! Под референсами я имел ввиду совсем другое."
    kenji "Машины, дома, деревья, фонарные столбы. А ты о чем подумала?"
    
    "Айко не нашла слов чтобы ответить мне."
    
    kenji "Ты что же думаешь, я собрался тайно фотографировать молоденьких девченок? Эх Айко… Как же ты испорчена!"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Surprised_Say with Dissolve( my_dissolve_01 )
    
    aiko "А? Чего?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Какие ужасные вещи приходят тебе в голову!"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Angry_Say with Dissolve( my_dissolve_01 )
    
    aiko "Что ты говоришь! Это не я а ты испорчен, это все из-за тебя!"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Angry_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Значит ты надеваешь купальник и предлагаешь себя фотографировать. А испорчен я?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Angry_Say with Dissolve( my_dissolve_01 )
    
    aiko "Да ну тебя!"
    aiko "Чтобы вечером показал мне свой телефон и всё что сфотографировал! Ясно?"
    
    show Aiko_School_Swimsuit_Hands_On_Hips Angry_Silent with Dissolve( my_dissolve_01 )
    
    kenji "А? Чего это ты так раскомандовалась? Сейчас я тебе покажу свой телефон..."
    
    "Я достал телефон из кармана, открыл камеру и нажал на спуск. Послышался звук затвора."
    
    hide Aiko_School_Swimsuit_Hands_On_Hips with Dissolve( my_dissolve_02 )
    show Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_02 )
    
    "Айко отпрыгнула в сторону."
    
    show Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ты чего творишь?"
    
    show Aiko_School_Swimsuit_Hand_Hold_Hand Surprised_Silent at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    kenji "Раз уж ты испортила ценный реквизит, теперь сама станешь реквизитом для сегодняшнего заседания нашего клуба!"
    
    "Я направил телефон на сестру и сделал ещё снимок."
    
    show Aiko_School_Swimsuit_Hand_Hold_Hand Scared_Say at Move( ( 400, 630 ), ( 400, 630 ), 0.0, xanchor="center", yanchor="center") with Dissolve( my_dissolve_01 )
    
    aiko "Ай! Нееет!"
    
    hide Aiko_School_Swimsuit_Hand_Hold_Hand with Dissolve( my_dissolve_01 )
    
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
    "Сказала «Иди и без моей тележки не возвращайся!»."
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
    "Но так сильно колотилось сердце и в горле стоял ком, всё-таки сегодня я «лекарство» от страха не принял."
    "Мне захотелось даже тихонько отойти от Касуми, а потом приблизиться к ней, отбивая шаг каблуками, чтобы она это услышала и первое слово осталось за ней."
    "Но я решил рискнуть, и заговорить первым. "
    "Набрал побольше воздуха в грудь. Вспомнил вчерашние упражнения на устранение гнусавости, напряг нужные мышцы горла, чтобы сформировать «певческий зевок»."
    "Погладил ладонью живот, чтобы узнать насколько хорошо раздулась диафрагма. Приготовился."
    
    kenji "Добргыххх… Кха! Кхе!"
    
    "Похоже я перестарался. Воздух пошёл не в то горло, вырвался через нос и я закашлялся"
    "Да уж, хотел как лучше, но лучше бы я молча бросил в Касуми её тележку и убежал поскорее домой."
    
    show Kasumi_01 Surprised_Silent with Dissolve( my_dissolve_02 )
    
    "Касуми вскочила и повернулась ко мне. Я хватая ртом воздух еле произнёс."
    
    kenji "Ка... Касуми… Добрый день… Это.. Это я… Кендзи!"
    
    show Kasumi_01 Surprised_Say with Dissolve( my_dissolve_01 )
    
    kasumi "А! Танака-сан! Это вы? Что с вами?"
    
    show Kasumi_01 Surprised_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Все… Всё в порядке… Просто я… Муху проглотил!"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Около минуты ушло на то, чтобы я пришел в себя и восстановил способность нормально говорить."
    "Шанс произвести хорошее впечатление при встрече, провалился."
    "Ну ладно, по крайней мере я смог заговорить с Касуми."
    "Пока я откашливался, девушка молчала и ожидала что я скажу."
    
    kenji "Касуми! Вот, как и обещал, твоя тележка. Я починил её."
    
    "Я поставил тележку перед девушкой."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ах, тележка!"
    kasumi "Спасибо вам Танака-сан! Наверное вам не стоило так утруждать себя..."
    kasumi "Сколько вам заплатить за ремонт?"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Заплатить? Нет! Мне ничего не надо!"
    
    "Удивительно, но Касуми злилась на меня. Приняв тележку она вежливо поклонилась."
    "Похоже все мои опасения были напрасны, хоть я вчера и нажрался прилично — особых глупостей не натворил."
    "Или Касуми настолько вежливая, что решила промолчать?"
    "Интересно, зачем она пришла сюда, на площадку для мусора? Её тётка послала искать тележку?"
    
    kenji "Касуми, а ты чего тут делаешь? Ждала, когда я принесу тележку? Я же хотел принести её тебе домой."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Я надеялась что те вещи, что вы вынесли вчера, Танака-сан, они ещё здесь. "
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Вот как... Но когда вчера вечером я шёл обратно, всё уже забрали. А что? Там было ещё что-то стоящее?"
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Кажется я ошиблась, и тот блок питания для рации, он действительно был нужен. Я надеялась, что он остался лежать здесь."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Вот как… Значит ты за ним при шла?"
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ага."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Но как бы ты унесла его домой? Он в два раза тяжелее чем рация."
    kenji "Сидела бы здесь, и ждала того, кто поможет унести его тебе домой?"
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Да, мне его не унести. Но хотя бы оттащила подальше, в кусты. А там, может придумала бы чего."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Надеюсь Касуми не сидит здесь целый день, в ожидании, когда выкинут чего интересного."
    "И не просит случайных прохожих помочь ей унести это до дома? В прочем я вчера сам напросился ей помочь."
    
    kenji "Да наверное так и следовало поступить. Припрятать его в тенёчек."
    kenji "Но ты же сама вчера сказала что у тебя уже есть, дома?"
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Я ошиблась. Я думала что эта рация, она полностью транзисторная, но это не так."
    kasumi "Кажется выходной каскад, он на лампах сделан. Нужно высокое напряжение для выходных ламп, и для накала."
    kasumi " Хотя, для накала у меня может и найдётся что-то. Но где взять анодное напряжение для выходных ламп?"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Вопросы, которые задавала Касуми, сейчас были похлеще тех, какими грешил дядя Ватанабэ."
    "Но вид у девушки был такой серьёзный, что я даже на некоторое время задумался, не знаю ли я случайно, где в самом деле достать «анодное напряжения» для «выходных ламп»"
    "Я чесал и лоб, затылок и подбородок, но безрезультатно. Я не имел ни малейшего представления о чем вообще шла речь."
    
    "А для Касуми, найти это «анодное напряжение» похоже было настолько важно, что она проделала значительный путь до сюда."
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
    
    hide Kasumi_01 with Dissolve( my_dissolve_02 )
    
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
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Не знаю. Я даже не знаю какое там должно быть напряжение"
    kasumi "Это мощная рация, и лампы мощные, генераторные."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Слово «генераторные» звучало весомо. Ух и светят наверное они, эти генераторные лампы."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Таким лампам нужно очень высокое напряжение. Может быть восемьсот вольт, или даже тысяча."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Сколько? Тысяча?!"
    
    "Цифры были ошеломляющие. Не удивительно почему этот аппарат столько весил."
    "Тысяча вольт! Вот это прибор! Да он должен был весить тысячу тонн, как по мне!"
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ну да, тысяча. Столько из бытовых блоков питания никак не получить. Может только сетевое взять и умножить. Но это очень опасно!"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Да уж, опасней некуда. Похоже без этого невероятного блока питания, рация действительно — полный хлам."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Извините Танака-сан, но похоже я зря вас потревожила вчера..."
    kasumi "Хотя… Пусть лежит, может быть я смогу что-то с ней сделать."
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
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
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Вернуть? Как?"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "Гляди! Тут адрес…"
    
    "Я осёкся на половине фразы. Черт! Я снова сказал то, чего не следовало."
    "Но похоже что девушку мои слова не обидели."
    
    "Тут адрес места, куда свозят мусор. Я не знаю точно, но похоже эта улица не так уж и далеко отсюда."
    "Может быть, они смогут отдать нам нужную вещь. Всякое же бывает, вдруг по незнанию выкинули что-то, чего не хотели?"
    
    "Я достал телефон и открыл карту. Да, я был прав — адрес был не так уж и далеко отсюда."
    "Вполне можно было дойти за час или даже меньше."
    
    "Касуми нерешительно спросила."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Вы тоже? Тоже пойдёте со мной, Танака-сан?"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    "Мне конечно же хотелось пойти с Касуми. Как и вчера, захотелось мне побыть с ней побольше, пообщаться и помочь."
    "Даже несмотря на отсутствие алкоголя в организме, её я больше не боялся."
    "Да и бояться нечего, вчера я ничего ужасного не натворил, даже наоборот."
    
    kenji "А как по другому? Если ты и дойдёшь туда Касуми, как ты унесёшь этот блок питания домой?"
    kenji "Он тяжелее чем рация, раза в два, если не больше."
    
    show Kasumi_01 Normal_Say with Dissolve( my_dissolve_01 )
    
    kasumi "Ну… Если вам не трудно… Спасибо…"
    kasumi "А как же вы его унесёте если он такой тяжёлый?"
    
    show Kasumi_01 Normal_Silent with Dissolve( my_dissolve_01 )
    
    kenji "А тележка? Теперь на ней колеса уже не сломать. Довезём на ней!"
    
    "Хотя, не очень то я доверял этой тележке. Если новые колеса и выдержат, слабину может дать хлипкая рама."
    "Вчера, тащить на своём горбу тот громоздкий прибор до мусорной площадке было невыносимо тяжело."
    "Если придётся заниматься этим и сегодня — не думаю что я это осилю."
    "Если получится вернуть этот блок питания обратно и тележка с ним не справится — закажу такси так и быть."
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_05 )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ########################################################
    
    
    
    
    
    
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
    
    
    #Мини ЦГ - Касуми НЕ ХОЧЕТ мороженное с шмелем
    image Kasumi_Do_Not_Want_IceCream_Moved:
        contains:
            "Kasumi_Do_Not_Want_IceCream"
            xpos 750
            #xpos 500
            #pause 0.7
            #linear 5.0 xpos 700
    
    image Kasumi_Do_Not_Want_IceCream_border_01_right_moved:
        contains:
            "border_01_right"
            xpos 900
    
    image Kasumi_Do_Not_Want_IceCream_border_01_right_mask_moved:
        contains:
            "border_01_right_mask"
            xpos 900
    
    image Kasumi_Do_Not_Want_IceCream_Masked = AlphaMask( "Kasumi_Do_Not_Want_IceCream_Moved", "Kasumi_Do_Not_Want_IceCream_border_01_right_mask_moved" )
    
    image Kasumi_Do_Not_Want_IceCream_With_Border_01:
        contains:
            "Kasumi_Do_Not_Want_IceCream_Masked"
        contains:
            "Kasumi_Do_Not_Want_IceCream_border_01_right_moved"
    ##
    
    show Kasumi_Do_Not_Want_IceCream_With_Border_01
    
    "111"
    
    scene Day_Shops_And_Vending_Machines_01 with Dissolve( my_dissolve_05 )
    
    "..."
    
    show DAY_02_Wending_Machines_With_Border_01 with Dissolve( my_dissolve_05 )
    
    "..."
    
