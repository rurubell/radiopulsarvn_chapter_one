image Night_RadioPulsar_HomeRoom_Other = "images/bg/Indoor/RadioPulsar_HomeRoom/Night/other.png"


#Анимации мониторов
image Night_RadioPulsar_HomeRoom_Monitor_01_Animation:
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_01/01.png"
    1.0
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_01/02.png"
    1.0
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_01/03.png"
    1.0
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_01/04.png"
    1.0
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_01/05.png"
    1.0
    repeat


image Night_RadioPulsar_HomeRoom_Monitor_02_Animation:
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_02/01.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_02/02.png"
    0.2
    repeat


image Night_RadioPulsar_HomeRoom_Monitor_03_Animation:
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/01.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/02.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/03.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/04.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/05.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/06.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/07.png"
    0.7
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/08.png"
    0.7
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/09.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/10.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/11.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/12.png"
    0.1
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/13.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/14.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/15.png"
    0.2
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/16.png"
    0.05
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/17.png"
    0.05
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/screen_03/18.png"
    0.05
    repeat


image Night_RadioPulsar_HomeRoom_Clock:
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/clock_01.png"
    1.0
    "images/bg/Indoor/RadioPulsar_HomeRoom/Night/clock_02.png"
    1.0
    repeat


image Night_RadioPulsar_HomeRoom_Light_SFX:
    contains:
        "images/bg/Indoor/RadioPulsar_HomeRoom/Night/sfx.png"
        linear 0.1 alpha 1.0
        linear 0.1 alpha 0.95 
        repeat
        

image Night_RadioPulsar_HomeRoom_Static_Leds_SFX:
    contains:
        "images/bg/Indoor/RadioPulsar_HomeRoom/Night/static_leds_sfx.png"
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.5
        repeat


image Night_RadioPulsar_HomeRoom:
    contains:
        "Night_RadioPulsar_HomeRoom_Other"
    
    contains:
        xpos 1153
        ypos 449
        "Night_RadioPulsar_HomeRoom_Monitor_01_Animation"
    
    contains:
        xpos 179
        ypos 465
        "Night_RadioPulsar_HomeRoom_Monitor_02_Animation"

    contains:
        xpos 295
        ypos 465
        "Night_RadioPulsar_HomeRoom_Monitor_03_Animation"
    
    contains:
        "Night_RadioPulsar_HomeRoom_Light_SFX"
    
    contains:
        "Night_RadioPulsar_HomeRoom_Static_Leds_SFX"
    
    contains:
        xpos 1635
        ypos 913
        "Night_RadioPulsar_HomeRoom_HDD_LED"
        
    contains:
        xpos 301
        ypos 947
        "Night_RadioPulsar_HomeRoom_HDD_LED"
    
    contains:
        xpos 0
        ypos 288
        "Night_RadioPulsar_HomeRoom_Clock"

