import numpy as np
import matplotlib.pyplot as plt
import imageio

# تعداد فریم‌های انیمیشن
num_frames = 30
frames = []

for i in range(num_frames):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + (i / 5.0))

    # رسم نمودار
    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue', linewidth=2)
    ax.set_ylim(-1.5, 1.5)

    # ذخیره به عنوان تصویر
    filename = f"frame_{i}.png"
    plt.savefig(filename)
    frames.append(imageio.imread(filename))
    plt.close(fig)

# ذخیره همه فریم‌ها به صورت GIF
imageio.mimsave("animation.gif", frames, duration=0.1)
print("✅ انیمیشن با موفقیت ساخته شد!")
