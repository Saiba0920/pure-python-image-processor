color_image = [
    [(255, 0, 0),   (0, 255, 0),     (0, 0, 255)],
    [(255, 255, 0), (0, 255, 255),   (255, 0, 255)],
    [(0, 0, 0),     (128, 128, 128), (255, 255, 255)],
]

def print_image(img, title):
    print(title)
    for row in img:
        for pixel in row:
            print(f"{pixel:4}", end="")
        print()
    print()

def print_color_image(img, title):
    print(title)
    for row in img:
        for (r, g, b) in row:
            print(f"({r:3},{g:3},{b:3})", end=" ")
        print()
    print()


def invert_color(img):
    new_img = []
    for row in img:
        new_row = []
        for (r, g, b) in row:
            new_row.append((255 - r, 255 - g, 255 - b))
        new_img.append(new_row)
    return new_img


def to_grayscale(img):
    new_img = []
    for row in img:
        new_row = []
        for (r, g, b) in row:
            gray = (r * 299 + g * 587 + b * 114) // 1000
            new_row.append(gray)
        new_img.append(new_row)
    return new_img

print_color_image(color_image, "Color original:")
print_color_image(invert_color(color_image), "Color inverted:")
print_image(to_grayscale(color_image), "Converted to grayscale:")
