image Meteor_01 = "./images/bg/Outdoor/Meteors/Meteor_01.png"
image Meteor_02 = "./images/bg/Outdoor/Meteors/Meteor_02.png"
image Meteor_03 = "./images/bg/Outdoor/Meteors/Meteor_03.png"

image Meteors:
    contains:
        choice:
            "Meteor_01"
            alpha 0.0
            linear 0.1 alpha 1.0
            linear 0.0 alpha 0.0
            pause renpy.random.randint( 40, 120 )
        
        choice:
            "Meteor_02"
            alpha 0.0
            linear 0.1 alpha 1.0
            linear 0.0 alpha 0.0
            pause renpy.random.randint( 40, 120 )

        choice:
            "Meteor_03"
            alpha 0.0
            linear 0.1 alpha 1.0
            linear 0.0 alpha 0.0
            pause renpy.random.randint( 40, 120 )
        repeat
