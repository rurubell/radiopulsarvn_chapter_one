image Crazy_Phone = "images/cg/DAY_02/05a_Train_station/Crazy_Phone/Kenji_Mobile_Phone.png"


#Выезд телефона из под пола
image Crazy_Phone_01:
    contains:
        "empty_image"
    
    contains:
        "Crazy_Phone"
        xpos 783
        ypos 1080
        
        
        ease 0.5 ypos 100


#Телефон крутится вокруг своей оси
image Crazy_Phone_02:
    contains:
        "empty_image"
    
    contains:
        "Crazy_Phone"
        xpos 783
        ypos 100
        xcenter 0.5
        ycenter 0.5
        
        block:
            #xpos 563
            linear 0.5 rotate 360
            linear 0 rotate 0
            repeat


#Телефон крутится вокруг своей оси и ездит из угла в угол
image Crazy_Phone_03:
    contains:
        "empty_image"
    
    contains:
        "Crazy_Phone"
        xpos 783
        ypos 100
        xcenter 0.5
        ycenter 0.5
        
        block:
            parallel:
                linear 0.5 rotate 360
                linear 0 rotate 0
                repeat
            
            parallel:
                linear 0.5 xpos 783
                linear 0.5 xpos 1800
                linear 1.0 xpos 50
                repeat


#Телефон скукоживается
image Crazy_Phone_04:
    contains:
        "empty_image"
    
    contains:
        "Crazy_Phone"
        xpos 783
        ypos 100
        xcenter 0.5
        ycenter 0.5
        
        block:
            parallel:
                linear 0.5 rotate 10
                linear 1.0 rotate -20
                linear 0.5 rotate 0
                repeat
                
            parallel:
                ease 1.0 xzoom 3.0
                ease 1.0 xzoom 1.0
                repeat
            
            parallel:
                ease 1.0 yzoom 0.5
                ease 1.0 yzoom 1.0
                repeat

#Телефон дергается
image Crazy_Phone_05:
    contains:
        "empty_image"
    
    contains:
        "Crazy_Phone"
        xpos 783
        ypos 1
        xcenter 0.5
        ycenter 0.5
    
    block:
        xpos 983
        linear 0.1 xpos 983+80
        linear 0.1 xpos 983-80
        repeat
