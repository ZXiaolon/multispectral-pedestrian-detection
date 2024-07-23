# YOLOv5
## 目录结构
# LLVIP
# ├── images
#     └── train
#     └── val
# └── labels
#     └── train
#     └── val


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: C:\Workplace\DL\dataset\Lowlight\LLVIP2  # dataset root dir
train: images/train
val: images/val
test:  # test images (optional)


## 训练
测试脚本
```shell
python train.py --weights yolov5s.pt --cfg yolov5s.yaml --data ./data/LLVIP.yaml --bach-size 8 --epochs 1 --img 640 --nosave --single-cls --name epochs_200
```

训练脚本
```shell
python train.py --weights yolov5s.pt --cfg yolov5s.yaml --data ./data/LLVIP.yaml --batch-size 8 --epochs 200 --img 640 --nosave --single-cls --name epochs_200
```

## 验证

测试脚本
```shell
python detect.py --weights ./runs/train/xxx/best.pt --img 640 --conf-thres 0.5 --iou-thres 0.5 --save-txt --save-conf --classes 0 --name val_epoch200 --source /root/autodl-temp/dataset/LVIP/images/val 
```
