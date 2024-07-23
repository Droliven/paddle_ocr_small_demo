# -*- coding: utf-8 -*-

# @FileName:     test.py
# @AuthorName:   Sanqi Lu (Lingwei Dang)
# @Institution:  SCUT, Guangzhou, China
# @EmailAddress: lenvondang@163.com
# @CreateTime:   2024/7/23 下午1:20


from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(
    det_model_dir="/home/addstorage/codes/paddle_ocr/assets/whl/det/ch_PP-OCRv4_det_server_infer",
    cls_model_dir="/home/addstorage/codes/paddle_ocr/assets/whl/cls/ch_ppocr_mobile_v2.0_cls_infer",
    rec_model_dir="/home/addstorage/codes/paddle_ocr/assets/whl/rec/ch_PP-OCRv4_rec_server_infer",
    use_gpu=True,
    use_angle_cls=True,
    det_db_thresh=0.3,
    det_db_box_thresh=0.6,
    lang="ch"
)  # need to run only once to download and load model into memory
img_path = './test.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='/home/addstorage/codes/paddle_ocr/assets/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')