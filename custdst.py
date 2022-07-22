import os
import shutil

from tqdm import tqdm


# 抽取特定类型的标注文件
def labels_extract(src_dir,dst_dir,label):
    files = list(os.listdir(src_dir))
    files_len = len(files)
    extract_num = 0

    process_bar = tqdm(total=files_len)
    process_bar.set_description('Processing:')

    for file in files:
        custom_label = []
        extract_txt = False
        process_bar.update(1)

        with open(os.path.join(src_dir, file), 'r') as f:
            strs = [x.split() for x in f.read().strip().splitlines()]
            for single_line in strs:
                if single_line[0] == label:
                    custom_label.append(single_line)
                    extract_num += 1
                    extrct_txt = True
            f.close()
        if extract_txt == True:
            with open(os.path.join(dst_dir, file), 'w') as fp:
                for line in custom_label:
                    newline = " ".join(line) + "\n"
                    fp.writelines(newline)
                fp.close()

    print(f'\n Extrcated number of target:{extract_num}')

# 抽取特定类型的图片文件
def images_path_txt(txt_dir, img_src_dir, img_dst_dir, img_path_file):
    files = list(os.listdir(txt_dir))
    process_bar = tqdm(total=len(files))
    if not os.path.exists(img_dst_dir):
        os.makedirs(img_dst_dir)
    with open(img_path_file, 'w') as f:
        for file in files:
            process_bar.update(1)
            line = img_dst_dir + "/" + file.replace("txt", "jpg") + '\n'
            img_path = os.path.join(img_src_dir, file.replace("txt", "jpg"))
            shutil.copy(img_path, img_dst_dir)
            f.writelines(line)
        f.close()


if __name__ == '__main__':
    # txt_dir = r"D:\DATA\od\coco\labels\train2017"
    # dstdir = r"D:\od\datasets\person\labels\train2017"
    # label = "0"
    # labels_extract(txt_dir, dstdir, label)
    #
    # txt_dir = r"D:\DATA\od\coco\labels\val2017"
    # dstdir = r"D:\od\datasets\person\labels\val2017"
    # label = "0"
    # labels_extract(txt_dir, dstdir, label)

    txt_dir = r"D:/od/datasets/person/labels/train2017"
    img_src_dir = r"D:\DATA\od\coco\images\train2017"
    img_dst_dir = r"D:/od/datasets/person/images/train2017/"
    img_path_file=r"D:/od/datasets/person/train2017.txt"
    images_path_txt(txt_dir, img_src_dir,img_dst_dir, img_path_file)

    txt_dir = r"D:/od/datasets/person/labels/val2017"
    img_src_dir = r"D:\DATA\od\coco\images\val2017"
    img_dst_dir = r"D:/od/datasets/person/images/val2017/"
    img_path_file=r"D:/od/datasets/person/val2017.txt"
    images_path_txt(txt_dir, img_src_dir, img_dst_dir, img_path_file)

