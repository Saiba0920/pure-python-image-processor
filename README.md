# Pure Python Image Processor

By Saiba Manikandan

This is my Week 1 assignment for the CEAM Computer Vision team. I built a small image processor using only core Python. An image is just a grid of numbers, so every operation here is done by looping over that grid by hand.

## How to run

Each step is in its own file. You can run any of them like this:

```
python3 pixel_ops.py
```

(Replace the file name with the step you want to run.)

## Files

| File | What is inside |
|---|---|
| `2D_grayscale_image.py` | The 5x5 image and the function that prints it |
| `Pixel-wise.py` | invert, brightness, threshold |
| `Geometric.py` | flip, rotate, crop |
| `Neighbourhood.py` | 3x3 box blur |
| `RGB.py` | color image functions (bonus) |

## How I stored the image

A grayscale image is a list of rows, and each row is a list of numbers from 0 (black) to 255 (white). I used a 5x5 image so I can check every answer by eye.

```python
image = [
    [  0,  50, 100, 150, 200],
    [ 10,  60, 110, 160, 210],
    [ 20,  70, 255, 170, 220],
    [ 30,  80, 130, 180, 230],
    [ 40,  90, 140, 190, 240],
]
```

`image[r][c]` means row r, column c. Counting starts from 0, and row 0 is the top row.

## Important rule

Every function takes an image and gives back a **new** image. It never changes the original. I printed the original again at the end of each file to prove this.

The printed output of the original image is:

```
   0  50 100 150 200
  10  60 110 160 210
  20  70 255 170 220
  30  80 130 180 230
  40  90 140 190 240
```

---

## 1. Pixel-wise operations (`Pixel-wise.py`)

In these, the new value of a pixel depends only on that same pixel.

### `invert(img)`
Replaces every pixel with `255 - pixel`, so black becomes white and white becomes black.

```
 255 205 155 105  55
 245 195 145  95  45
 235 185   0  85  35
 225 175 125  75  25
 215 165 115  65  15
```

Output: the bright center pixel (255) became 0, and the 0 in the top-left became 255.

### `adjust_brightness(img, amount)`
Adds `amount` to every pixel. If the answer goes above 255 I make it 255, and if it goes below 0 I make it 0. I did this using `max(0, min(255, value))`.

Brightness +60:
```
  60 110 160 210 255
  70 120 170 220 255
  80 130 255 230 255
  90 140 190 240 255
 100 150 200 250 255
```

Output: the pixels that would have gone over 255 (like 200 + 60) stopped at 255.

Brightness -80:
```
   0   0  20  70 120
   0   0  30  80 130
   0   0 175  90 140
   0   0  50 100 150
   0  10  60 110 160
```

Output: the pixels that would have gone below 0 stopped at 0.

### `threshold(img, cutoff)`
Pixels that are greater than or equal to the cutoff become 255 (white). All the others become 0 (black). I used a cutoff of 128.

```
   0   0   0 255 255
   0   0   0 255 255
   0   0 255 255 255
   0   0 255 255 255
   0   0 255 255 255
```

Output: the image is now only black and white. The left side was dark so it became 0, and the right side was bright so it became 255.

---

## 2. Geometric operations (`Geometric.py`)

In these, the pixels move to a new place but their values stay the same.

### `flip_horizontal(img)`
Mirrors the image left to right. Each row is read from the last column to the first.

```
 200 150 100  50   0
 210 160 110  60  10
 220 170 255  70  20
 230 180 130  80  30
 240 190 140  90  40
```

Output: every row is reversed. The center 255 stays in the middle.

### `rotate_90_clockwise(img)`
Rotates the image 90 degrees clockwise. Each old column, read from bottom to top, becomes a new row.

```
  40  30  20  10   0
  90  80  70  60  50
 140 130 255 110 100
 190 180 170 160 150
 240 230 220 210 200
```

Output: the first new row is `40 30 20 10 0`, which is the old first column read from the bottom to the top.

A 5x5 image does not show that the size changes, so I also tried a 3x4 image (3 rows, 4 columns). After rotating it became 4x3:

```
   1   2   3   4            9   5   1
   5   6   7   8     ->    10   6   2
   9  10  11  12           11   7   3
                           12   8   4
```

### `crop(img, top, left, crop_height, crop_width)`
Keeps only a rectangle of the image. `top` and `left` tell where the rectangle starts (its top-left corner), and `crop_height` and `crop_width` tell how many rows and columns to keep. If the rectangle goes outside the image, the function gives an error message instead of crashing.

Crop with top=1, left=1, size 3x3:
```
  60 110 160
  70 255 170
  80 130 180
```

Output: it starts at the pixel 60 (row 1, column 1) and keeps a 3x3 block.

---

## 3. Neighborhood operation (`Neighbourhood.py`)

### `box_blur(img)`
This blurs the image. Each pixel is replaced by the average of the 3x3 square around it (the pixel itself plus its 8 neighbors). All 9 values count equally. The 3x3 square is called the kernel.

```
   0  50 100 150 200
  10  75 125 175 210
  20  85 135 185 220
  30  95 145 195 230
  40  90 140 190 240
```

Output: only the inside 3x3 block changed. The outside border is the same as the original.

I checked the center pixel by hand. Its neighbors are 60, 110, 160, 70, 255, 170, 80, 130, 180. The sum is 1215, and 1215 // 9 = 135. So the bright 255 went down to 135, which is what a blur should do.

### How I handled the borders

The pixels on the edge do not have 9 neighbors (for example, the top row has no row above it). 

The simplest way to overcome this issue is to skip the edges entirely, and I can check it by eye. It also does not make up any fake values. 
The downside is that the outer ring of pixels does not get blurred. In a 5x5 image this is easy to notice, but in a big image the border is very small compared to the whole picture.

---

## 4. Bonus: color images (`RGB.py`)

A color pixel is three numbers `(r, g, b)`, one each for red, green and blue, from 0 to 255. I stored each pixel as a tuple.

```python
color_image = [
    [(255, 0, 0),   (0, 255, 0),     (0, 0, 255)],
    [(255, 255, 0), (0, 255, 255),   (255, 0, 255)],
    [(0, 0, 0),     (128, 128, 128), (255, 255, 255)],
]
```

### `invert_color(img)`
Inverts each of the three values: `(255 - r, 255 - g, 255 - b)`.

```
(  0,255,255) (255,  0,255) (255,255,  0)
(  0,  0,255) (255,  0,  0) (  0,255,  0)
(255,255,255) (127,127,127) (  0,  0,  0)
```

Output: red `(255, 0, 0)` became cyan `(0, 255, 255)`, and white became black.

### `to_grayscale(img)`
Changes a color image into a grayscale image. I used the weights 0.299 for red, 0.587 for green and 0.114 for blue, because our eyes see green as brighter than red or blue. To avoid decimals I multiplied by 1000 and used `//`.

```
  76 149  29
 225 178 105
   0 128 255
```

Output: pure green (149) is brighter than pure red (76), and pure red is brighter than pure blue (29).


---

## Things that are not perfect

- The blur leaves a 1 pixel border unblurred.
- The blur is only for grayscale images.

## What I learned

- An image is only a grid (or a 2D list) of numbers, and every operation is just a loop over that grid.
- There are different types of operations that can be done on an image using purely Python, like pixel-wise, geometric and neighbourhood.
- A colored image contains of three values of three colours (Red, Green and Blue or RGB), unlike a grayscale image, which consists of one pixel value from 0 to 255.
- Rotating changes the height and width of the image, which I only noticed after trying a non-square image.
