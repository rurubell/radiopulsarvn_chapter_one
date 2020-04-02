image Jet_Red = "images/bg/Outdoor/Jets/Night/red.png"
image Jet_Blue = "images/bg/Outdoor/Jets/Night/blue.png"
image Jet_Empty = "images/bg/Outdoor/Jets/Night/empty.png"

image Jet_Blink_Animation:
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Red"
    0.1
    "Jet_Empty"
    0.5
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.1
    "Jet_Blue"
    0.1
    "Jet_Empty"
    0.5
    repeat

image Night_Jets_Right_To_Left:
    contains:
        "empty_image"
    
    contains:
        "Jet_Blink_Animation"
        xpos 2000
        ypos 100
        linear 50.0 xpos -10
        repeat
