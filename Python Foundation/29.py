color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for i in color_list_1:
    if i not in color_list_2:
        print(i,end="  ")