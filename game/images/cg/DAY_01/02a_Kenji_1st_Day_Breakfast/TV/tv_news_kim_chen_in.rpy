image TV_News_Kim_Chen_In_Other = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv_news_kim_chen_in.png"
image TV_Mask = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv_mask.png"
image TV = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv.png"

image TV_News_Kim_Chen_In_Other_Masked = AlphaMask( "TV_News_Kim_Chen_In_Other", "TV_Mask" )


image TV_News_Kim_Chen_In:
    contains:
        "empty_image"
    
    contains:
        "TV"
        xpos 100
        ypos 0
        
    contains:
        "TV_News_Kim_Chen_In_Other_Masked"
        xpos 100
        ypos 0
        
    contains:
        "TV_Interferences_Animation_Masked"
        xpos 100
