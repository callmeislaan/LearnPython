import numpy as np
from PIL import Image
import time

def stereo_matching_ssd(left_img, right_img, dernel_size, disparity_range):
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)
    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    width = 384
    height = 288

    # tao depth map
    depth = np.zeros((height, width), np.uint8)

    dernel_haft = int((dernel_size - 1) / 2)
    scale = 255 / disparity_range
    
    for y in range(dernel_haft, height - dernel_haft):
        for x in range(dernel_haft, width - dernel_haft):

            disparity = 0
            cost_min = 65534

            for j in range(disparity_range):
                step = 0
                ssd_step = 0
                for v in range(-dernel_haft, dernel_haft):
                    for u in range(-dernel_haft, dernel_haft):
                        step = (int(left[y+v, x+u]) - int(right[y+u, (x+u) - j]))**2
                        ssd_step += step
                if ssd_step < cost_min:
                    cost_min = ssd_step
                    disparity = j

            depth[y, x] = disparity * scale
    Image.fromarray(depth).save('Images/tsukuba_disparity_map_ssd.png')

if __name__ == '__main__':
    disparity_range = 16
    dernel_size = 5
    start = time.time()
    stereo_matching_ssd('Images/tsukuba_left.png', 'Images/tsukuba_right.png', dernel_size, disparity_range)
    print('time: ', (time.time() - start) * 1000)