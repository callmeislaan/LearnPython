import numpy as np
from PIL import Image

def stereo_matching(left_img, right_img, disparity_range):
    # doc anh trai va anh phai, roi chuyen anh sang grayscale
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    # cho truoc chieu rong va chieu dai cua anh
    height = 288
    width = 384

    # tao disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = 255 / disparity_range
    for y in range(height):
        for x in range(width):
            # tim j tai do cost co gia tri min
            disparirty = 0
            cost_min = (int(left[y, x]) - int(right[y, x]))**2
            for j in range(1, disparity_range):
                cost = 255**2 if x - j < 0 else (int(left[y, x]) - int(right[y, x - j]))**2
                if cost < cost_min:
                    cost_min = cost
                    disparirty = j
            # da tim ra j de cost min
            # gan j do vao disaprity map
            # nhan cho scale de nhin thay ro rang (khong can scale cung duoc)
            depth[y, x] = disparirty * scale
    # chuyen du lieu tu ndarray sang kieu Image va luu xuong file
    Image.fromarray(depth).save('Images/tsukuba_disparity_map.png')    
if __name__ == '__main__':
    disparirty_range = 16 # cho cap anh tsukuba
    stereo_matching('Images/tsukuba_left.png', 'Images/tsukuba_right.png', disparirty_range)
