
image = [
    [  0,  50, 100, 150, 200],
    [ 10,  60, 110, 160, 210],
    [ 20,  70, 255, 170, 220],
    [ 30,  80, 130, 180, 230],
    [ 40,  90, 140, 190, 240],
]

def print_image(img , title):
    print(title)
    for row in img:
        for pixel in row:
            print(f"{pixel:4}", end = "")
        print()
    print()


def invert(img):
    new_img = []
    for row in img:
        new_row = []
        for pixel in row:
            new_row.append(255 - pixel)
        new_img.append(new_row)
    return(new_img)

def brightness(img , amount):
    new_img = []
    for row in img:
        new_row =[]
        for pixel in row:
            value = pixel + amount
            value = max(0 , min(255 , value))
            new_row.append(value)
        new_img.append(new_row)
    return(new_img)

def threshold(img , cutoff):
    new_img = []
    for row in img:
        new_row = []
        for pixel in row:
            if pixel >= cutoff:
                value = 255
            else:
                value = 0
            new_row.append(value)
        new_img.append(new_row)
    return(new_img)

print_image(image , "Original")
print_image(invert(image) , "Inverted Image")
print_image(brightness(image , 72) , "Adjusted Brightness Image +72")
print_image(threshold(image , 128) , "Adjusted Threshold Image (Cutoff = 128)")


                