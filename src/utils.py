import csv
import random
from typing import List, Tuple

def read_points_from_csv(file_path):
    """
    从CSV文件中读取数据，输出一个点集列表
    
    Args:
        file_path (str): CSV文件路径
        
    Returns:
        list: 点集列表，每个元素为(x, y)元组
    """
    points = []
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:  # 确保行中有至少两个值
                x = float(row[0])
                y = float(row[1])
                points.append((x, y))
    
    return points

def add_noise_to_points(points: List[Tuple[float, float]], 
                       noise_range: Tuple[float, float] = (-0.5, 0.5)) -> List[Tuple[float, float]]:
    """
    为点集添加随机噪声
    
    Args:
        points: 原始点集列表，每个元素为(x, y)元组
        noise_range: 噪声范围，默认为(-0.5, 0.5)
        
    Returns:
        添加噪声后的点集列表
    """
    noisy_points = []
    min_noise, max_noise = noise_range
    
    for x, y in points:
        # 为x和y坐标分别添加随机噪声
        noise_x = random.uniform(min_noise, max_noise)
        noise_y = random.uniform(min_noise, max_noise)
        noisy_points.append((x + noise_x, y + noise_y))
    
    return noisy_points

if __name__ == '__main__':
    file_path = r'data/random_points.csv'  # 替换为实际的CSV文件路径
    points = read_points_from_csv(file_path)
    print(f"读取的点集: {points}")

    noisy_points = add_noise_to_points(points)
    formatted_points = [(f"{x:.2f}", f"{y:.2f}") for x, y in noisy_points]  # 格式化输出
    print(f"添加噪声后的点集: {formatted_points}")