import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """
    计算两点之间的欧几里得距离
    """
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_path(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """
    使用最近邻算法生成路径
    """
    if not points:
        return []
    
    # 复制点列表，避免修改原始数据
    unvisited = points[:]
    path = [unvisited.pop(0)]  # 从第一个点开始
    
    while unvisited:
        current_point = path[-1]
        # 找到距离当前点最近的未访问点
        nearest_point = min(unvisited, key=lambda point: distance(current_point, point))
        unvisited.remove(nearest_point)
        path.append(nearest_point)
    
    return path

def plot_path(points: List[Tuple[float, float]], path: List[Tuple[float, float]]):
    """
    绘制点和路径
    """
    xs, ys = zip(*points)
    
    plt.figure(figsize=(10, 8))
    plt.scatter(xs, ys, c='red', s=100, zorder=2)
    
    # 标注点的序号
    # for i, (x, y) in enumerate(points):
    #     plt.annotate(f'{i}({x},{y})', (x, y), xytext=(5, 5), textcoords='offset points')
    
    # 如果提供了路径，则绘制路径
    if path:
        path_xs, path_ys = zip(*path)
        plt.plot(path_xs, path_ys, 'b-', linewidth=1, zorder=1)
        # 标注路径方向
        for i in range(len(path) - 1):
            plt.annotate('', xy=path[i+1], xytext=path[i],
                        arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    
    plt.title('Point Path Planning')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    pass