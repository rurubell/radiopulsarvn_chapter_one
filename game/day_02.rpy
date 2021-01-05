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
    
    "..."
    
