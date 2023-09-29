import random
NestedTubes = []
TubeList= ["Tube 1","Tube 2","Tube 3","Tube 4","Tube 5","Tube 6","Tube 7","Tube 8","Tube 9","Tube 10","Tube 11","Tube 12",]
color_dict = {
    "Red": "Rd",
    "Blue": "Bl",
    "Green": "Gr",
    "Yellow": "Yl",
    "Purple": "Pu",
    "Orange": "Or",
    "Pink": "Pk",
    "Brown": "Br",
    "Cyan": "Cy",
    "Magenta": "Mg",
    "Gray": "Gy",
    "Black": "Bk"
}

def CreateTubes(Height,TubeNumber):
    x=0
    while x <= TubeNumber + 1:
        newTube = [TubeList[x]]
        for _ in range(Height):
            newTube.append("{}")
        NestedTubes.append(newTube)
        x+=1

def PickColors(Color_dict, TubeNumber):
    if TubeNumber <= 0:
        return []

    available_colors = list(Color_dict.values())
    
    if TubeNumber-2 > len(available_colors):
        print("Not enough unique colors available.")
        return []

    selected_colors = random.sample(available_colors, TubeNumber)

    return selected_colors

def FillTubes(Height, ColorList, NestedTubes):
    total_tubes = len(NestedTubes)

    if len(ColorList) < (total_tubes - 2):
        print(len(ColorList))
        print(total_tubes - 2)
        print("Not enough colors to fill the tubes.")
        return

    colors_to_assign = []
    for _ in range(Height):
        for color in ColorList:
            colors_to_assign.append(color)

    num_tubes = len(NestedTubes) - 2  # Exclude the last two tubes
    colors_per_tube = len(colors_to_assign) // num_tubes  # Calculate how many colors each tube should get
    random.shuffle(colors_to_assign)
    for i in range(num_tubes):
        tube = NestedTubes[i]
        for y in NestedTubes[i]:
            (NestedTubes[i]).clear()
    for i in range(num_tubes):
        tube = NestedTubes[i]
        tube.append (f"Tube {i + 1}")
        for _ in range(colors_per_tube):
         tube.append(colors_to_assign.pop(0))

    # Distribute any remaining colors
    for i in range(len(colors_to_assign)):
        tube = NestedTubes[i % num_tubes]
        tube.append(colors_to_assign.pop(0))
    
    for tube in NestedTubes:
        print(tube)




TubeNumber = 4
Height = 4
CreateTubes(Height,TubeNumber)

selected_colors = PickColors(color_dict, TubeNumber)
print("Selected Colors:", selected_colors)
FillTubes(Height, selected_colors, NestedTubes)