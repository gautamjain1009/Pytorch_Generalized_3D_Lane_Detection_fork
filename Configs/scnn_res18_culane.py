
#TODO: Optimize this config
"""
Dataloader params
"""

#TODO: Mya be the mean and std values are not correct for the dataset
img_norm = dict(
    mean=[0.485, 0.456, 0.406] ,
    std=[0.229, 0.224, 0.225]
)

img_height = 360
img_width = 480
cut_height = 240
ori_img_h = 590
ori_img_w = 1640

#for vis
sample_y = range(710,150, -10)
thr = 0.6

# train_augmentation = [
#     dict(type='RandomRotation', degree=(-2, 2)) ,
#     dict(type='RandomHorizontalFlip'),
#     dict(type='Resize', size=(img_width, img_height)),
#     dict(type='Normalize', img_norm=img_norm),
#     dict(type='ToTensor'),
# ] 

# val_augmentation = [
#     dict(type='Resize', size=(img_width, img_height)),
#     dict(type='Normalize', img_norm=img_norm),
#     dict(type='ToTensor')
# ] 

# dataset_path = '/home/ims-robotics/Documents/gautam/dataset/culane'

# dataset = dict(
#     train=dict(
#         type='CULaneLoader',
#         data_root=dataset_path,
#         split='train',
#         transform = train_augmentation
#     ),
#     val=dict(
#         type='CULaneLoader',
#         data_root=dataset_path,
#         split='val',
#         transform = val_augmentation
#     ),
#     test=dict(
#         type='CULaneLoader',
#         data_root=dataset_path,
#         split='val',
#         transform = val_augmentation
#     )
# )

"""
training params
"""
workers = 12
num_classes = 1 + 1
# num_classes = 6 + 1
# ignore_label = 255


"""
model params
"""
featuremap_out_channel = 128
featuremap_out_stride = 8
backbone = dict(
    type='ResNetWrapper',
    resnet_variant='resnet18',
    pretrained=True,
    replace_stride_with_dilation=[False, True, False],
    out_conv=True,
    in_channels=[64, 128, 256, -1],
    featuremap_out_channel = 128)

aggregator = dict(type= "SCNN")

heads = dict(type = 'PlainDecoder')

###logging params
date_it = "_9_August_"
train_run_name = "SCNN_Res18_culane_b16" + date_it
val_frequency = 2500
train_log_frequency = 200

#Hyperparams
epochs = 100
batch_size = 16
l2_lambda = 1e-4
log_frequency_steps = 200
lr = 0.001 
lrs_cd = 0
lrs_factor = 0.75
lrs_min = 1e-6
lrs_patience = 3
lrs_thresh = 1e-4
prefetch_factor = 2
bg_weight = 0.4 #used in the loss function to reduce the importance of one class in tusimple

train_type = "binary"

pretrained_2dmodel_path = "/home/ims-robotics/Documents/gautam/Pytorch_Generalized_3D_Lane_Detection_fork/pretrained/r18_nodrop_scnn_binary_2dLane_imgnet_meanstd_b167_August_0.01457406859844923_23.pth"