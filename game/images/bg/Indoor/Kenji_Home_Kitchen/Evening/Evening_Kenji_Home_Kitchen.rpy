image Evening_Kenji_Home_Kitchen_Other = "images/bg/Indoor/Kenji_Home_Kitchen/Evening/Other.jpg"
image Evening_Kenji_Home_Kitchen_Mask = "images/bg/Indoor/Kenji_Home_Kitchen/Evening/Mask.png"
image Evening_Kenji_Home_Kitchen_Other_Dust = AlphaMask( "dust", "Evening_Kenji_Home_Kitchen_Mask" )

image Evening_Kenji_Home_Kitchen:
    contains:
        "Evening_Kenji_Home_Kitchen_Other"
    contains:
        "Evening_Kenji_Home_Kitchen_Other_Dust"
