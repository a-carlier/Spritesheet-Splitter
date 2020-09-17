import sys
from pathlib import Path
from PIL import Image


def split(args):
    # Errors Checks
    if len(args) < 3:
        return "You must provide a PNG file and at least the split sprites width"

    extension = args[1][-4:]

    if extension != ".png" and extension != ".PNG":
        return "File extension must be PNG"

    name = args[1].split('/')[-1][0:-4]

    try:
        f = open(args[1])
        f.close()
    except IOError:
        return "Spritesheet " + args[1] + " doesn't exist"

    if not args[2].isdigit():
        return "Width must be an Integer above Zero"
    if int(args[2]) < 1:
        return "Width must be an Integer above Zero"

    spritesheet = Image.open(args[1])
    max_width, max_height = spritesheet.size

    tile_width = int(args[2])

    # If user doesn't precise height, we will split our spritesheet by squares
    if len(sys.argv) < 4:
        tile_height = tile_width
    else:
        if not args[3].isdigit():
            return "Height must be an Integer above Zero"
        if int(args[3]) < 1:
            return "Height must be an Integer above Zero"
        tile_height = args[3]

    # Crop and save each frame in a /split folder
    Path("./split").mkdir(parents=True, exist_ok=True)

    for y in range(0, max_height // tile_height):
        for x in range(0, max_width // tile_width):
            spritesheet\
                .crop((x * tile_width, y * tile_height, (x+1) * tile_width, (y+1) * tile_height))\
                .save('./split/' + name + str((max_width // tile_width) * y + x) + extension)

    return "Spritesheet successfully split"

if __name__ == '__main__':
    print(split(sys.argv))