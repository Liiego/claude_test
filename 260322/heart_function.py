"""
心形函数绘制程序
使用参数方程绘制二维和三维心形曲线
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def heart_2d(t, size=1):
    """
    二维心形函数参数方程
    
    参数:
        t: 参数 (0 到 2π)
        size: 心形大小缩放因子
    
    返回:
        x, y: 心形曲线的坐标
    """
    x = size * 16 * np.sin(t) ** 3
    y = size * (13 * np.cos(t) - 5 * np.cos(2*t) - 
                2 * np.cos(3*t) - np.cos(4*t))
    return x, y


def heart_3d(u, v, size=1):
    """
    三维心形函数参数方程
    
    参数:
        u: 参数 (0 到 π)
        v: 参数 (0 到 2π)
        size: 心形大小缩放因子
    
    返回:
        x, y, z: 三维心形表面的坐标
    """
    x = size * 16 * np.sin(u) ** 3 * np.sin(v)
    y = size * (13 * np.cos(u) - 5 * np.cos(2*u) - 
                2 * np.cos(3*u) - np.cos(4*u)) * np.sin(v)
    z = size * 8 * np.cos(u)
    return x, y, z


def plot_heart_2d(size=1, color='red', title='2D 心形曲线'):
    """
    绘制二维心形曲线
    
    参数:
        size: 心形大小
        color: 曲线颜色
        title: 图表标题
    """
    # 生成参数值
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # 计算坐标
    x, y = heart_2d(t, size)
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(x, y, color=color, linewidth=2)
    ax.fill(x, y, alpha=0.3, color=color)
    
    # 设置图形属性
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    plt.tight_layout()
    plt.show()
    
    return x, y


def plot_heart_3d(size=1, color='red', title='3D 心形表面'):
    """
    绘制三维心形表面
    
    参数:
        size: 心形大小
        color: 表面颜色
        title: 图表标题
    """
    # 生成参数值
    u = np.linspace(0, np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)
    
    # 计算坐标
    x, y, z = heart_3d(u, v, size)
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制表面
    surface = ax.plot_surface(x, y, z, cmap='Reds', 
                             alpha=0.8, linewidth=0, 
                             antialiased=True)
    
    # 设置图形属性
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # 添加颜色条
    fig.colorbar(surface, shrink=0.5, aspect=10)
    
    plt.tight_layout()
    plt.show()
    
    return x, y, z


def animate_heart_2d(frames=50, size=1, save_gif=False):
    """
    创建动态心形动画（呼吸效果）
    
    参数:
        frames: 动画帧数
        size: 基础大小
        save_gif: 是否保存为 GIF
    """
    from matplotlib.animation import FuncAnimation
    
    fig, ax = plt.subplots(figsize=(8, 8))
    t = np.linspace(0, 2 * np.pi, 1000)
    line, = ax.plot([], [], color='red', linewidth=2)
    
    def init():
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_aspect('equal')
        ax.set_title('动态心形', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        return line,
    
    def update(frame):
        # 呼吸效果：大小周期性变化
        scale = size * (1 + 0.1 * np.sin(frame * 0.2))
        x, y = heart_2d(t, scale)
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, update, frames=frames, 
                        init_func=init, blit=True, interval=50)
    
    if save_gif:
        anim.save('heart_animation.gif', writer='pillow', fps=30)
        print("动画已保存为 heart_animation.gif")
    
    plt.show()


def main():
    """主函数：展示各种心形图案"""
    print("=" * 50)
    print("心形函数绘制程序")
    print("=" * 50)
    print("\n可选功能:")
    print("1. 绘制 2D 心形曲线")
    print("2. 绘制 3D 心形表面")
    print("3. 创建动态心形动画")
    print("4. 绘制多个不同大小的心形")
    print("=" * 50)
    
    choice = input("请选择功能 (1-4): ")
    
    if choice == '1':
        size = float(input("输入心形大小 (默认 1): ") or "1")
        plot_heart_2d(size=size)
    elif choice == '2':
        size = float(input("输入心形大小 (默认 1): ") or "1")
        plot_heart_3d(size=size)
    elif choice == '3':
        frames = int(input("输入动画帧数 (默认 50): ") or "50")
        size = float(input("输入心形大小 (默认 1): ") or "1")
        save = input("是否保存为 GIF? (y/n): ").lower() == 'y'
        animate_heart_2d(frames=frames, size=size, save_gif=save)
    elif choice == '4':
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = ['red', 'pink', 'darkred', 'lightcoral']
        sizes = [1, 0.8, 0.6, 0.4]
        
        t = np.linspace(0, 2 * np.pi, 1000)
        for size, color in zip(sizes, colors):
            x, y = heart_2d(t, size)
            ax.plot(x, y, color=color, linewidth=2, alpha=0.7)
            ax.fill(x, y, alpha=0.2, color=color)
        
        ax.set_aspect('equal')
        ax.set_title('多层心形', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    else:
        print("无效选择，使用默认选项：绘制 2D 心形")
        plot_heart_2d()


if __name__ == "__main__":
    main()
