import open3d as o3d

# 读取PLY文件
pcd = o3d.io.read_point_cloud("./log/tensorf_0615_VM/tensorf_0615_VM.ply")

o3d.visualization.draw_geometries([pcd])