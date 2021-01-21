#Ватанабе 01
image Watanabe_01_Normal_Say = im.Scale( "images/sprites/Watanabe/Watanabe_01/Watanabe_01_Normal_Say.png", 622, 1080 )
image Watanabe_01_Normal_Silent = im.Scale( "images/sprites/Watanabe/Watanabe_01/Watanabe_01_Normal_Silent.png", 622, 1080 )
image Watanabe_01_Sad_Say = im.Scale( "images/sprites/Watanabe/Watanabe_01/Watanabe_01_Sad_Say.png", 622, 1080 )
image Watanabe_01_Sad_Silent = im.Scale( "images/sprites/Watanabe/Watanabe_01/Watanabe_01_Sad_Silent.png", 622, 1080 )

layeredimage Watanabe_01:
    group emotion:
        attribute Normal_Say:
            "Watanabe_01_Normal_Say"
        attribute Normal_Silent:
            "Watanabe_01_Normal_Silent"
        attribute Sad_Say:
            "Watanabe_01_Sad_Say"
        attribute Sad_Silent:
            "Watanabe_01_Sad_Silent"


#Ватанабе 02
image Watanabe_02_Normal_Say = im.Scale( "images/sprites/Watanabe/Watanabe_02/Watanabe_02_Normal_Say.png", 622, 1080 )
image Watanabe_02_Normal_Silent = im.Scale( "images/sprites/Watanabe/Watanabe_02/Watanabe_02_Normal_Silent.png", 622, 1080 )

layeredimage Watanabe_02:
    group emotion:
        attribute Normal_Say:
            "Watanabe_02_Normal_Say"
        attribute Normal_Silent:
            "Watanabe_02_Normal_Silent"
