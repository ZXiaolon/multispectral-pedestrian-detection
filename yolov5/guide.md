# YOLOv5
## 目录结构
# LLVIP
# ├── images
#     └── train
#     └── val
# └── labels
#     └── train
#     └── val

path: C:\Workplace\DL\dataset\Lowlight\LLVIP2  # dataset root dir
train: images/train
val: images/val
test:  # test images (optional)


## 训练
测试脚本
```shell
python train.py --weights yolov5s.pt --cfg yolov5s.yaml --data ./data/LLVIP.yaml --batch-size 8 --epochs 1 --img 640 --nosave --single-cls --name epochs_200
```

训练脚本
```shell
nohup python train.py --weights yolov5s.pt --cfg yolov5s.yaml --data ./data/LLVIP.yaml --batch-size 16 --epochs 200 --img 640 --nosave --single-cls --name yolo_train_epochs_200 > record.log 2>&1 &
```
nohup后台挂载

## 验证

测试脚本
```shell
python detect.py --weights ./runs/train/xxx/best.pt --img 640 --conf-thres 0.5 --iou-thres 0.5 --save-txt --save-conf --classes 0 --name val_epoch200 --source /root/autodl-temp/dataset/LVIP/images/val 
```
