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

def box_blur(img):
    """Blur with a 3x3 box kernel. Border pixels are left unchanged."""
    height = len(img)
    width = len(img[0])
    new_img = []
    for row in img:
        new_img.append(row[:])    
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            total = 0
            for dr in range(-1, 2):       
                for dc in range(-1, 2):    
                    total += img[r + dr][c + dc]
            new_img[r][c] = total // 9     
    return new_img

print_image(image, "Original")
print_image(box_blur(image), "After Blur")