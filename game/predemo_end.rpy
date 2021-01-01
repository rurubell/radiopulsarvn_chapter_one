label predemo_end:
    window hide
    
    play environment_sounds "sounds/environment/Suburb_Night.mp3" fadein 1
    scene Night_Street_01 with Dissolve( my_dissolve_05 )
    
    pause 2.0
    
    image End_Splash_Logo_JP = im.Scale( "images/other/pre_demo_logo_ru.png", 900, 506 )
    image End_Splash_Text = VBox(
        Text( "{b}{color=#FFE680}РадиоПульсар ПреДемо{/color}{/b}" ),
        #Text( "" ),
        Text( "{color=#FFE680}Сценарий:{/color} Дим Осторожно, Puankar, Крошка_Ру" ),
        Text( "{color=#FFE680}Редактура:{/color} lethargic" ),
        Text( "{color=#FFE680}Картинки, код:{/color} Крошка_Ру" ),
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
