image Electronics_For_Dummies_Book = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/book.png"

image Electronics_For_Dummies_Angel_01a = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_01a.png"
image Electronics_For_Dummies_Angel_01b = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_01b.png"

image Electronics_For_Dummies_Angel_02a = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_02a.png"
image Electronics_For_Dummies_Angel_02b = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_02b.png"

image Electronics_For_Dummies_Angel_03a = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_03a.png"
image Electronics_For_Dummies_Angel_03b = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_03b.png"

image Electronics_For_Dummies_Angel_04a = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_04a.png"
image Electronics_For_Dummies_Angel_04b = "images/cg/DAY_01/10a_Makoto's_Books/Electronics_For_Dummies/Angel_04b.png"


image Electronics_For_Dummies_Angel_01_Animated_Wings:
    "Electronics_For_Dummies_Angel_01a"
    0.2
    "Electronics_For_Dummies_Angel_01b"
    0.2
    repeat
    

image Electronics_For_Dummies_Angel_02_Animated_Wings:
    "Electronics_For_Dummies_Angel_02a"
    0.2
    "Electronics_For_Dummies_Angel_02b"
    0.2
    repeat


image Electronics_For_Dummies_Angel_03_Animated_Wings:
    "Electronics_For_Dummies_Angel_03a"
    0.2
    "Electronics_For_Dummies_Angel_03b"
    0.2
    repeat

image Electronics_For_Dummies_Angel_04_Animated_Wings:
    "Electronics_For_Dummies_Angel_04a"
    0.2
    "Electronics_For_Dummies_Angel_04b"
    0.2
    repeat


image Electronics_For_Dummies_Angels:
    contains:
        "Electronics_For_Dummies_Angel_01_Animated_Wings"
        ease 2.0 ypos 50
        ease 2.0 ypos 0
        repeat

    contains:
        xpos 300
        ypos 450
        "Electronics_For_Dummies_Angel_02_Animated_Wings"
        ease 1.8 ypos 500
        ease 1.8 ypos 450
        repeat

    contains:
        xpos 1100
        "Electronics_For_Dummies_Angel_03_Animated_Wings"
        ease 2.2 ypos 50
        ease 2.2 ypos 0
        repeat

    contains:
        xpos 1400
        ypos 400
        "Electronics_For_Dummies_Angel_04_Animated_Wings"
        ease 1.7 ypos 450
        ease 1.7 ypos 400
        repeat


image Electronics_For_Dummies:
    contains:
        "Electronics_For_Dummies_Book"
    
    contains:
        "Electronics_For_Dummies_Angels"
    

