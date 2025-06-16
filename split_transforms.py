import json
import os
import shutil

# 读取原始 transforms.json 文件
with open('data/images/transforms.json', 'r') as f:
    transforms = json.load(f)

# 分割帧，例如 90% 用于训练，10% 用于测试
frames = transforms['frames']
n_frames = len(frames)
n_train = int(n_frames * 0.9)  # 90% 作为训练数据

# 创建训练集 JSON
train_transforms = transforms.copy()
train_transforms['frames'] = frames[:n_train]
with open('data/images/transforms_train.json', 'w') as f:
    json.dump(train_transforms, f, indent=4)

# 创建测试集 JSON
test_transforms = transforms.copy()
test_transforms['frames'] = frames[n_train:]
with open('data/images/transforms_test.json', 'w') as f:
    json.dump(test_transforms, f, indent=4)

print(f"已将数据分割为 {n_train} 张训练图像和 {n_frames - n_train} 张测试图像")
