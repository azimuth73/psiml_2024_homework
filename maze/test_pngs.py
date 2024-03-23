from PIL import Image
import numpy as np
import os


def list_files(directory):
    file_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_list.append(filename)
    return file_list


def test() -> None:
    base_path = './public/set/'
    image_paths = list_files(base_path)

    rgb_pixel_count = 0
    rgba_pixel_count = 0

    for i, path in enumerate(image_paths):
        image_paths[i] = os.path.join(base_path, path)
        maze_image_file = Image.open(image_paths[i])
        maze_image = np.array(maze_image_file)

        print(f'{path}_shape = {maze_image.shape}')

        image_has_rgba_pixel = False
        image_has_rgb_pixel = False

        # Iterate through each pixel
        for row in maze_image:
            for pixel in row:
                if len(pixel) == 4:  # RGBA image
                    image_has_rgba_pixel = True
                    rgba_pixel_count += 1
                    red, green, blue, alpha = pixel
                    # print(f'red = {red}\ngreen = {green}\nblue = {blue}\nalpha = {alpha}\n')
                    if (red != 0 and red != 255) or (green != 0 and green != 255) or (blue != 0 and blue != 255) or (alpha != 255):
                        raise Exception
                elif len(pixel) == 3:  # RGB image without alpha channel
                    image_has_rgb_pixel = True
                    rgb_pixel_count += 1
                    red, green, blue = pixel
                    # print(f'red = {red}\ngreen = {green}\nblue = {blue}\nalpha = N/A (no alpha channel)\n')
                    if (red != 0 and red != 255) or (green != 0 and green != 255) or (blue != 0 and blue != 255):
                        raise Exception
                else:
                    print("Unexpected pixel format.")
                    raise Exception
        if image_has_rgb_pixel and image_has_rgba_pixel:
            raise Exception

    print(f'rgb_pixel_count = {rgb_pixel_count}')
    print(f'rgba_pixel_count = {rgba_pixel_count}')


if __name__ == '__main__':
    test()
