image Day_Kenji_Home_Kitchen_Other = "images/bg/Indoor/Kenji_Home_Kitchen//Day/Day_Kenji_Home_Kitchen_Other.png"
image Day_Kenji_Home_Kitchen_Mask = "images/bg/Indoor/Kenji_Home_Kitchen//Day/Day_Kenji_Home_Kitchen_Mask.png"
image Day_Kenji_Home_Kitchen_Other_Dust = AlphaMask( "dust", "Day_Kenji_Home_Kitchen_Mask" )

image Day_Kenji_Home_Kitchen:
    contains:
        "Day_Kenji_Home_Kitchen_Other"
    contains:
        "Day_Kenji_Home_Kitchen_Other_Dust"
