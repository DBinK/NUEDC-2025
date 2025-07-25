import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple
import random

def generate_random_points(n: int, x_range: Tuple[float, float] = (0, 10), 
                          y_range: Tuple[float, float] = (0, 10)) -> List[Tuple[float, float]]:
    """
    生成随机点集
    
    Args:
        n: 点的数量
        x_range: x坐标范围
        y_range: y坐标范围
        
    Returns:
        点坐标列表
    """
    points = []
    for _ in range(n):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        points.append((x, y))
    return points

def generate_grid_points(rows: int, cols: int, spacing: float = 1.0) -> List[Tuple[float, float]]:
    """
    生成网格状点集
    
    Args:
        rows: 行数
        cols: 列数
        spacing: 点间距
        
    Returns:
        点坐标列表
    """
    points = []
    for i in range(rows):
        for j in range(cols):
            points.append((j * spacing, i * spacing))
    return points

def generate_circular_points(n: int, radius: float = 5.0, center: Tuple[float, float] = (0, 0)) -> List[Tuple[float, float]]:
    """
    生成圆形排列的点集
    
    Args:
        n: 点的数量
        radius: 圆的半径
        center: 圆心坐标
        
    Returns:
        点坐标列表
    """
    points = []
    for i in range(n):
        angle = 2 * np.pi * i / n
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        points.append((x, y))
    return points

def generate_clustered_points(n: int, clusters: int = 3, cluster_radius: float = 1.0,
                             overall_range: Tuple[float, float] = (0, 10)) -> List[Tuple[float, float]]:
    """
    生成聚簇状点集
    
    Args:
        n: 点的总数
        clusters: 聚簇数量
        cluster_radius: 聚簇半径
        overall_range: 整体范围
        
    Returns:
        点坐标列表
    """
    points = []
    
    # 首先生成聚簇中心
    cluster_centers = generate_random_points(clusters, overall_range, overall_range)
    
    # 然后在每个聚簇中心周围生成点
    points_per_cluster = n // clusters
    for center in cluster_centers:
        for _ in range(points_per_cluster):
            angle = random.uniform(0, 2 * np.pi)
            distance = random.uniform(0, cluster_radius)
            x = center[0] + distance * np.cos(angle)
            y = center[1] + distance * np.sin(angle)
            points.append((x, y))
    
    # 如果点数不够，补充一些随机点
    while len(points) < n:
        points.append(generate_random_points(1, overall_range, overall_range)[0])
        
    return points[:n]

def plot_points(points: List[Tuple[float, float]], title: str = "Generated Points"):
    """
    绘制点集
    
    Args:
        points: 点坐标列表
        title: 图标题
    """
    if not points:
        return
        
    xs, ys = zip(*points)
    
    plt.figure(figsize=(10, 8))
    plt.scatter(xs, ys, c='red', s=50, zorder=2)
    
    # 标注点的序号
    for i, (x, y) in enumerate(points):
        plt.annotate(f'{i}', (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.show()

def save_points_to_csv(points: List[Tuple[float, float]], filename: str):
    """
    将点集保存到CSV文件
    
    Args:
        points: 点坐标列表
        filename: 文件名
    """
    with open(filename, 'w') as f:
        for point in points:
            f.write(f"{point[0]:.2f},{point[1]:.2f}\n")


def load_points_from_file(filename: str) -> List[Tuple[float, float]]:
    """
    从文件加载点集
    
    Args:
        filename: 文件名
        
    Returns:
        点坐标列表
    """
    points = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                x, y = map(float, line.strip().split(','))
                points.append((x, y))
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    return points

def main():
    print("点集生成器")
    print("=" * 30)
    
    # 生成不同类型的点集用于测试
    
    # 1. 随机点集
    print("1. 生成随机点集 (10个点)...")
    random_points = generate_random_points(50, (0, 100), (0, 100))
    print(f"生成了 {len(random_points)} 个随机点")
    plot_points(random_points, "随机点集")
    
    # 2. 网格点集
    print("\n2. 生成网格点集 (3x4网格)...")
    grid_points = generate_grid_points(10, 10, 2.0)
    print(f"生成了 {len(grid_points)} 个网格点")
    plot_points(grid_points, "网格点集")
    
    # 3. 圆形点集
    print("\n3. 生成圆形点集 (8个点)...")
    circular_points = generate_circular_points(80, 50.0, (0, 0))
    print(f"生成了 {len(circular_points)} 个圆形排列点")
    plot_points(circular_points, "圆形点集")
    
    # 4. 聚簇点集
    print("\n4. 生成聚簇点集 (15个点, 3个聚簇)...")
    clustered_points = generate_clustered_points(150, 6, 10.00, (0, 100))
    print(f"生成了 {len(clustered_points)} 个聚簇点")
    plot_points(clustered_points, "聚簇点集")

    # 保存点集
    # save_points_to_csv(random_points, "random_points.csv")
    save_points_to_csv(grid_points, "grid_points.csv")
    # save_points_to_csv(circular_points, "circular_points.csv")
    # save_points_to_csv(clustered_points, "clustered_points.csv")

    # 演示如何加载CSV文件
    # print("\n示例: 从CSV文件加载点集")
    # loaded_points = load_points_from_file("random_points.csv")
    # print(f"从random_points.txt加载了 {len(loaded_points)} 个点")
    # print("加载的点:", loaded_points)

if __name__ == "__main__":
    main()