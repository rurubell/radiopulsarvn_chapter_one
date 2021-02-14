image First_Trash_Place_Room_Base = "images/bg/Indoor/First_Trash_Place_Room/First_Trash_Place_Room.png"
image First_Trash_Place_Room_Dust_Mask = "images/bg/Indoor/First_Trash_Place_Room/First_Trash_Place_Room_Dust_Mask.png"

image First_Trash_Place_Room_Dust = Dust( "images/other/dust.png", 500 )
image First_Trash_Place_Room_Dust_Masked = AlphaMask( "First_Trash_Place_Room_Dust", "First_Trash_Place_Room_Dust_Mask" )

image DAY_First_Trash_Place_Room:
    contains:
        "First_Trash_Place_Room_Base"
    
    contains:
        "First_Trash_Place_Room_Dust_Masked"
