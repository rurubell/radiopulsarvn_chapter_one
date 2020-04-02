image Kasumi_Lifting_Up_RadioSet_Other = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Other.png"

image Kasumi_Lifting_Up_RadioSet_Dummy_Lines_01 = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Dummy_Lines_01.png"
image Kasumi_Lifting_Up_RadioSet_Dummy_Lines_02 = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Dummy_Lines_02.png"
image Kasumi_Lifting_Up_RadioSet_Dummy_Lines_03 = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Dummy_Lines_03.png"

image Kasumi_Lifting_Up_RadioSet_Drops = "images/cg/DAY_01/04a_Trash_Place_Meeting/Kasumi_Lifting_Up_RadioSet/Drops.png"


image Kasumi_Lifting_Up_RadioSet:
    contains:
        "Kasumi_Lifting_Up_RadioSet_Other"
    
    contains:
        "Kasumi_Lifting_Up_RadioSet_Dummy_Lines_01"
        0.2
        "Kasumi_Lifting_Up_RadioSet_Dummy_Lines_02"
        0.2
        "Kasumi_Lifting_Up_RadioSet_Dummy_Lines_03"
        0.2
        repeat
    
    contains:
        "Kasumi_Lifting_Up_RadioSet_Drops"
        alpha 0.0
        ypos -10
        linear 0.8 alpha 1.0 ypos 5
        pause 3.0
        linear 0.2 alpha 0.0
        pause 1.0
        repeat
        
    contains:
        "Emo_What"
        xpos 800
        ypos 70
