image Dad_In_Room_Other = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/Dad_In_Room.png"

image Dad_In_Room_Lamps_01 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/lamps_01.png"
image Dad_In_Room_Lamps_02 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/lamps_02.png"
image Dad_In_Room_Lamps_03 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/lamps_03.png"
image Dad_In_Room_Lamps_04 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/lamps_04.png"
image Dad_In_Room_Lamps_05 = "images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Dad_In_Room/lamps_05.png"


image Dad_In_Room:
    contains:
        "Dad_In_Room_Other"
    
    contains:
        "Dad_In_Room_Lamps_Animated"


image Dad_In_Room_Lamps_Animated:
    contains:
        "Dad_In_Room_Lamps_01"
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.3 alpha 0.2
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.2 alpha 1.0
        repeat

    contains:
        "Dad_In_Room_Lamps_02"
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.3 alpha 0.2
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.2 alpha 1.0
        repeat

    contains:
        "Dad_In_Room_Lamps_03"
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.3 alpha 0.2
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.2 alpha 1.0
        repeat

    contains:
        "Dad_In_Room_Lamps_04"
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.3 alpha 0.2
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.2 alpha 1.0
        repeat

    contains:
        "Dad_In_Room_Lamps_05"
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.3 alpha 0.2
        pause renpy.random.uniform( 0.1, 0.5 )
        linear 0.2 alpha 1.0
        repeat
