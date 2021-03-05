init python:
    renpy.music.register_channel( "environment_sounds", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений
    renpy.music.register_channel( "environment_sounds_dream", "sfx", loop=True, stop_on_mute=True, tight=True ) #Канал для звуков улиц/помещений (во время воспоминаний)


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
