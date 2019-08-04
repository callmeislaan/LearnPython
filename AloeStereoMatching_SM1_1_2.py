import numpy as np
from PIL import Image

def stereo_matching_aloe_sm1_1_2(left_img, right_img, disparity_range):
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    width = 427
    height = 370
    scale = 255 / disparity_range   

    depth = np.zeros((height, width), np.uint8)

    for y in range(height):
        for x in range(width):
            cost_min = (int(left[y, x]) - int(right[y, x]))**2
            disparity = 0
            for j in range(1, disparity_range):
                cost = (int(left[y, x]) - int(right[y, x - j]))**2
                if cost < cost_min:
                    cost_min = cost
                    disparity = j
            depth[y, x] = disparity * scale
    
    Image.fromarray(depth).save('Images/AloeStereoMatching_SM1_1_2.png')

if __name__ == '__main__':
    disparity_range = 64
    stereo_matching_aloe_sm1_1_2('Images/Aloe_left_1.png', 'Images/Aloe_right_1.png', disparity_range)
