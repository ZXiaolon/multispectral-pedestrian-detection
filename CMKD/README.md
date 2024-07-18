# Cross Modality Knowledge Distillation for Robust Pedestrian detection in low light and adverse weather condition

The goal of this project is to use knowledge distillation techniques to improve the performance of the object detectors (for Pedestrian) in adverse weather and low light conditions.

This implementation is based on [Faster R-CNN](https://proceedings.neurips.cc/paper/2015/file/14bfa6bb14875e45bba028a21ed38046-Paper.pdf) with ResNet50-FPN backone in Pytorch using [Seeing Through Fog](https://www.cs.princeton.edu/~fheide/AdverseWeatherFusion/) dataset. 

Trained and tested with python: 3.9.7, Ubuntu:18.04.5 LTS, Cuda: 11.2, Pytorch:1.11, GPU: Geforce RTX 3090

## Usage
- Install [PyTorch](https://pytorch.org/).
- Download the data from [here](https://drive.google.com/file/d/1uz2vP5Bl_pmXPNCXk7ftttjvwtncCfGn/view?usp=sharing) and extract the ZIP file in `data/` folder.
- Download the [trained teacher network](https://drive.google.com/file/d/1FShIWdq_U213vWoCUk5EMh_nMfysmx4c/view?usp=sharing) or train it by running this comment. The teacher network is trained using both RGB images and 3 Gated slices in the dataset.
```
python train_teacher.py
``` 
- train Cross Modality Knowledge Distillation (CMKD) method based on Mean Squred Error (MSE) of backnone features by running this comment:
```
python train_cmkd_mse.py
```
- train Cross Modality Knowledge Distillation (CMKD) method based adversarial training of backnone features by running this comment:
```
python train_cmkd_adv.py
```
- The trained network can be tested using valand test sets by changing the name of tested weights file in `test.py` line 109 and running this comment:
```
python test.py
```
- The baseline network can be trained by running this comment. Baseline is trained using only RGB images without CMKD. 
```
python train_baseline.py
```
- Visual detection examples can be seen by running this comment:
```
visual_detect.py
```

## Results & Pretrained Weights
|Model|COCO mAP val set| COCO mAP test set| Trained model|
|---|---|---|---|
Teacher|25.8|27.5|[download](https://drive.google.com/file/d/1FShIWdq_U213vWoCUk5EMh_nMfysmx4c/view?usp=sharing)
|Baseline|22.5|24.2|[download](https://drive.google.com/file/d/1zT8UMh0ihzDLPP6Fy_E2G_7cAnUcluqr/view?usp=sharing)
|CMKD-MSE|23.6|25.4|[download](https://drive.google.com/file/d/16iMhJynAi39kJac0m0NUxXlxnOphwu4G/view?usp=sharing)
|CMKD-Adv|24.2|26.0|[download](https://drive.google.com/file/d/1m37Yb4bUKzZfilG4Xaeu0AjcR0hAzy8s/view?usp=sharing)

## Citation
```
@inproceedings{cmkd,
  title={Cross Modality Knowledge Distillation for Robust Pedestrian Detection in Low Light and Adverse Weather Conditions},
  author={Hnewa, Mazin and Rahimpour, Alireza and Miller, Justin and Upadhyay, Devesh and Radha, Hayder},
  booktitle={ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={1--5},
  year={2023},
  organization={IEEE}
}
```
