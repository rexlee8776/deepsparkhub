# Copyright (c) 2022, Shanghai Iluvatar CoreX Semiconductor Co., Ltd.
import mmcv
from os import path as osp
from PIL import Image


def generate_meta_info_div2k():
    """Generate meta info for DIV2K dataset.
    """

    gt_folder = 'data/DIV2K/DIV2K_train_HR'
    meta_info_txt = 'data/DIV2K/meta_info_DIV2K800sub_GT.txt'

    img_list = sorted(list(mmcv.scandir(gt_folder)))

    with open(meta_info_txt, 'w') as f:
        for idx, img_path in enumerate(img_list):
            img = Image.open(osp.join(gt_folder, img_path))  # lazy load
            width, height = img.size
            mode = img.mode
            if mode == 'RGB':
                n_channel = 3
            elif mode == 'L':
                n_channel = 1
            else:
                raise ValueError(f'Unsupported mode {mode}.')

            info = f'{img_path} ({height},{width},{n_channel})'
            print(idx + 1, info)
            f.write(f'{info}\n')


if __name__ == '__main__':
    generate_meta_info_div2k()
