# PaddleOCR 本地安装版

## 环境

- 项目网站：https://github.com/PaddlePaddle/PaddleOCR/tree/main
- 安装包地址：https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
- 模型地址：https://github.com/PaddlePaddle/PaddleOCR/blob/d590a8d39a3f459a4009ce91a58f693f631848b3/docs/ppocr/model_list.md
- 参数列表：https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_ch/inference_args.md
- python3.8
- cuda 11.7
- cudnn 8.5
- paddlepaddle_gpu-2.4.2.post117-cp38-cp38-linux_x86_64.whl
- paddleocr=2.7

## 已知问题

根据案例发现什么总结什么，背后的成因不清楚

- python cuda cudnn 环境对结果的影响： cuda11.3 检出的结果少于 cuda 11.7
- server 模型偶现检测不出的问题，换用蒸馏后的小模型可以检出
- server 版本的模型环境配置不对的话，可能不报错但完全什么都检测不出来
