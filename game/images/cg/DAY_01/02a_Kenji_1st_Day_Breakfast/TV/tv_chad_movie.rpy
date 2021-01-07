image TV_Chad_Movie_Other = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv_chad_movie.png"
image TV_Mask = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv_mask.png"
image TV = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/tv.png"

image TV_Chad_Movie_Other_Masked = AlphaMask( "TV_Chad_Movie_Other", "TV_Mask" )


image TV_Chad_Movie:
    contains:
        "empty_image"
    
    contains:
        "TV"
        xpos 100
        ypos 0
        
    contains:
        "TV_Chad_Movie_Other_Masked"
        xpos 100
        ypos 0
        
    contains:
        "TV_Interferences_Animation_Masked"
        xpos 100
