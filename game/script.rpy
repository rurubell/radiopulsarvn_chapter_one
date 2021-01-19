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
    image white_image = "images/other/colored/white.png"
    image black_image = "images/other/colored/black.png"
    image black_image_alpha_50pc:
        contains:
            "black_image"
            alpha 0.5
            
    stop music fadeout 1
    
    scene Trash_Place_In_Kenji_Mind_Animated
    
    "...."
    
    scene black_image
    
    "..."
    
    scene Day_Cats_Paw_Shrine_Torii_Static_BG
    
    "111"
    
    show Cats_Paw_Shrine_Stairs_With_Border_01 with dissolve
    "..."
    
    #Пыль
    image dust = Dust( "images/other/dust.png" )
    #Рамка для флешбеков
    image Dream_Frame = "images/cg/Misc/Dream_Frame/Dream_Frame.png"
    #пустая картинка
    image empty_image = "images/other/empty.png"
    
    
    #Рамки для мини-цг
    image border_01_right = "images/other/borders/01_Right/border.png"
    image border_01_right_mask = "images/other/borders/01_Right/mask.png"
    image border_01_left = "images/other/borders/01_Left/border.png"
    image border_01_left_mask = "images/other/borders/01_Left/mask.png"
    
    
    jump day_01
    return
