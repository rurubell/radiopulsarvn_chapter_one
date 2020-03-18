image Emo_What_01 = "./images/other/emo/what/01.png"
image Emo_What_02 = "./images/other/emo/what/02.png"
image Emo_What_03 = "./images/other/emo/what/03.png"

image Emo_What_Horizontal_Flipped_01 = im.Flip( "./images/other/emo/what/01.png", horizontal=True )
image Emo_What_Horizontal_Flipped_02 = im.Flip( "./images/other/emo/what/02.png", horizontal=True )
image Emo_What_Horizontal_Flipped_03 = im.Flip( "./images/other/emo/what/03.png", horizontal=True )

image Emo_What:
    "Emo_What_01"
    0.5
    "Emo_What_02"
    0.5
    "Emo_What_03"
    0.5
    repeat

image Emo_What_Horizontal_Flipped:
    "Emo_What_Horizontal_Flipped_01"
    0.5
    "Emo_What_Horizontal_Flipped_02"
    0.5
    "Emo_What_Horizontal_Flipped_03"
    0.5
    repeat
