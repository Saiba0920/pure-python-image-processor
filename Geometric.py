image = [
    [  0,  50, 100, 150, 200],
    [ 10,  60, 110, 160, 210],
    [ 20,  70, 255, 170, 220],
    [ 30,  80, 130, 180, 230],
    [ 40,  90, 140, 190, 240],
]


def print_image(img,title):
    print(title)
    for row in img:
        for pixel in row:
            print(f"{pixel:4}", end = "")
        print()



def flip_horizontal(img):
    height = len(img)
    width = len(img[0])
    new_img = []
    for r in range(height):
        new_row = []
        for c in range(width - 1, -1, -1):   
            new_row.append(img[r][c])
        new_img.append(new_row)
    return new_img


def rotate_90_clockwise(img):
    height = len(img)
    width = len(img[0])
    new_img = []
    for c in range(width):                    
        new_row = []
        for r in range(height - 1, -1, -1):   
            new_row.append(img[r][c])
        new_img.append(new_row)
    return new_img


def crop(img, top, left, crop_height, crop_width):
    new_img = []
    for r in range(top, top + crop_height):
        new_row = []
        for c in range(left, left + crop_width):
            new_row.append(img[r][c])
        new_img.append(new_row)
    return new_img


print_image(image, "Original")
print_image(flip_horizontal(image), "After Horizontal Flip")
print_image(rotate_90_clockwise(image), "After Rotating 90 degrees Clockwise")
print_image(crop(image, 1, 1, 3, 3), "After Cropping (Top = 1, Left = 1, 3x3)")