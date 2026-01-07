import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 使用OpenCV读取图像
image = cv2.imread('ultralytics/assets/bus.jpg')

# 如果图像是彩色的，可以转换成灰度图像以便简化处理
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 傅里叶变换并移至中心
f_transform = np.fft.fft2(gray_image)
f_transform_shifted = np.fft.fftshift(f_transform)  # 移动零频率分量到中心
magnitude_spectrum = np.abs(f_transform_shifted)  # 计算幅度谱

# 获取频谱图尺寸
height, width = magnitude_spectrum.shape

# 创建x,y坐标数组
x = np.arange(0, width)
y = np.arange(0, height)
x, y = np.meshgrid(x, y)

# 标准化幅度谱到[0, 1]范围以便于显示
z = magnitude_spectrum / np.max(magnitude_spectrum)

# 创建图形
fig = plt.figure(figsize=(20, 10))

# 空间域3D曲面
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax1.set_title('3D Surface Plot of Image Pixel Intensities (Spatial Domain)')
fig.colorbar(surf, shrink=0.5, aspect=10)

# 频域3D曲面
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf_freq = ax2.plot_surface(x, y, np.log(z + 1), cmap='magma', edgecolor='none')  # 对数变换以增强视觉效果
ax2.set_title('3D Surface Plot of Frequency Domain Representation')
fig.colorbar(surf_freq, shrink=0.5, aspect=10)

plt.tight_layout()
plt.show()