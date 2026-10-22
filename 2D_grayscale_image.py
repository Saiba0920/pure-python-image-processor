image = [
    [  0,  50, 100, 150, 200],
    [ 10,  60, 110, 160, 210],
    [ 20,  70, 255, 170, 220],
    [ 30,  80, 130, 180, 230],
    [ 40,  90, 140, 190, 240],
]


def print_image(img):
    for row in img:
        for pixel in row:
            print(f"{pixel:4}", end = "")
        print()


print_image(image)