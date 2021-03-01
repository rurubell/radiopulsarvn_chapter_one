init python:
    renpy.music.register_channel( "environment_sounds", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений
    renpy.music.register_channel( "environment_sounds_dream", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений (во время воспоминаний)


define kenji = Character( "Кендзи", color="#BBFF88" )
define aiko = Character( "Айко", color="#FF888B" )
define aiko_voice = Character( "Голос", color="#FF888B" )
define kasumi = Character( "Касуми", color="#88C0FF" )
define kasumis_aunt = Character( "Тётка Касуми", color="#B3B3B3" )
define blind_girl = Character( "Девушка", color="#88C0FF" )
define watanabe = Character( "Ватанабе", color="#009900" )
define zak = Character( "Заказчик", color="#FFC95C" )
define tv = Character( "Телевизор", color="#FFC95C" )
define trash_man_01 = Character( "Мусорщик", color="#009900" )
define trash_man_02 = Character( "Мусорщик", color="#009900" )
define trash_man_03 = Character( "Лысый", color="#009900" )
define someones_voice = Character( "Голос", color="#FF3CDA" )
define someones_cry = Character( "Крик", color="#FF3CDA" )
define kenji_phone = Character( "Телефон", color="#C5001D" )
define hooligan = Character( "Хулиган", color="#963CFF" )


label splashscreen:
    pause 1.0
    show Splash with Dissolve( my_dissolve_05 )
    pause 5.0
    hide Splash with Dissolve( my_dissolve_05 )
    pause 1.0
    return


label start:
            
    stop music fadeout 1
    
    
    #Пыль
    image dust = Dust( "images/other/dust.png" )
    
    
    #Рамки для мини-цг
    image border_01_right = "images/other/borders/01_Right/border.png"
    image border_01_right_mask = "images/other/borders/01_Right/mask.png"
    image border_01_left = "images/other/borders/01_Left/border.png"
    image border_01_left_mask = "images/other/borders/01_Left/mask.png"
    
    
    jump day_01
    return
