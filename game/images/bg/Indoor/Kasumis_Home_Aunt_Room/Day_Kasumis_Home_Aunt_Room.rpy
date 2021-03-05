image Day_Kasumis_Home_Aunt_Room_Base = "images/bg/Indoor/Kasumis_Home_Aunt_Room/Base.png"
image Day_Kasumis_Home_Aunt_Room_Dust_Mask = "images/bg/Indoor/Kasumis_Home_Aunt_Room/Dust_Mask.png"
image Day_Kasumis_Home_Aunt_Room_Dust = Dust( "images/other/dust.png", 300 )
image Day_Kasumis_Home_Aunt_Room_Dust_Masked = AlphaMask( "Day_Kasumis_Home_Aunt_Room_Dust", "Day_Kasumis_Home_Aunt_Room_Dust_Mask" )


image Day_Kasumis_Home_Aunt_Room:
    contains:
        "Day_Kasumis_Home_Aunt_Room_Base"
    
    contains:
        "Day_Kasumis_Home_Aunt_Room_Dust_Masked"
    
    contains:
        xpos 1342
        ypos 246
        alpha 0.5
        "Day_Kasumis_Home_Aunt_Room_TV"


image Kasumis_Home_Aunt_Room_TV_Noice_Frame_01 = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/01.png"
image Kasumis_Home_Aunt_Room_TV_Noice_Frame_02 = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/02.png"
image Kasumis_Home_Aunt_Room_TV_Noice_Frame_03 = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/03.png"
image Kasumis_Home_Aunt_Room_TV_Noice_Frame_04 = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/04.png"
image Kasumis_Home_Aunt_Room_TV_Noice_Frame_05 = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/05.png"

image Kasumis_Home_Aunt_Room_TV_Biverbuck = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/Biverbuck.png"
image Kasumis_Home_Aunt_Room_TV_Queen = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/Queen.png"
image Kasumis_Home_Aunt_Room_TV_RickRoll = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/Rickroll.png"
image Kasumis_Home_Aunt_Room_TV_Eye = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/Eye.png"
image Kasumis_Home_Aunt_Room_TV_BlackMonument = "images/bg/Indoor/Kasumis_Home_Aunt_Room/tv_frames/Black_Monument.png"


image Day_Kasumis_Home_Aunt_Room_TV:
    contains:
        "Day_Kasumis_Home_Aunt_Room_TV_White_Noice"
    
    contains:
        "Kasumis_Home_Aunt_Room_TV_Biverbuck"
        alpha 0.0
        
        choice 0.1:
            alpha 0.5
            pause 0.1
        
        choice 0.9:
            alpha 0.0
            pause 1.5
        
        repeat

    contains:
        "Kasumis_Home_Aunt_Room_TV_Queen"
        alpha 0.0
        
        choice 0.1:
            alpha 0.5
            pause 0.1
        
        choice 0.9:
            alpha 0.0
            pause 1.5
        
        repeat

    contains:
        "Kasumis_Home_Aunt_Room_TV_RickRoll"
        alpha 0.0
        
        choice 0.1:
            alpha 0.5
            pause 0.1
        
        choice 0.9:
            alpha 0.0
            pause 1.5
        
        repeat

    contains:
        "Kasumis_Home_Aunt_Room_TV_Eye"
        alpha 0.0
        
        choice 0.1:
            alpha 0.5
            pause 0.1
        
        choice 0.9:
            alpha 0.0
            pause 1.5
        
        repeat

    contains:
        "Kasumis_Home_Aunt_Room_TV_BlackMonument"
        alpha 0.0
        
        choice 0.1:
            alpha 0.5
            pause 0.1
        
        choice 0.9:
            alpha 0.0
            pause 1.5
        
        repeat


image Day_Kasumis_Home_Aunt_Room_TV_White_Noice:
    "Kasumis_Home_Aunt_Room_TV_Noice_Frame_01"
    0.1
    "Kasumis_Home_Aunt_Room_TV_Noice_Frame_02"
    0.1
    "Kasumis_Home_Aunt_Room_TV_Noice_Frame_03"
    0.1
    "Kasumis_Home_Aunt_Room_TV_Noice_Frame_04"
    0.1
    "Kasumis_Home_Aunt_Room_TV_Noice_Frame_05"
    0.1
    repeat
