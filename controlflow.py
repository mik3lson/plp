#while loopss 
colors = ["black", "purple","green", "white", "yellow", "pink"]
color_i_want = "white"

count = 0
lenght = len(colors)

while count< lenght:
    print(colors[count])
    
    if colors[count]== color_i_want:
        print("they have the color i want", color_i_want)

    count+=1
 
