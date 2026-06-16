import networkx as nx
import matplotlib.pyplot as plt

def auto_draw_graph(edges, filename="dothi_lab.png"):
    """
    Hàm vẽ đồ thị đa năng. 
    Nhận vào danh sách các cạnh (edges) và tự động xuất ra file ảnh.
    """
    # Khởi tạo đồ thị
    G = nx.Graph()
    G.add_edges_from(edges)
    
    # Thiết lập kích thước khung hình
    plt.figure(figsize=(6, 4))
    
    # Sử dụng Kamada-Kawai layout: Tối ưu khoảng cách giữa các node, ít bị cắt dây
    pos = nx.kamada_kawai_layout(G)
    
    # Vẽ đồ thị với các tùy chỉnh giao diện "sạch"
    nx.draw(
        G, pos,
        with_labels=True,
        node_color='#ADD8E6',   # Màu xanh dương nhạt dịu mắt
        node_size=800,          # Kích thước node vừa vặn
        font_size=12,
        font_weight='bold',
        edge_color='gray',
        width=2.0               # Độ dày của cạnh
    )
    
    # Lưu ra file ảnh
    plt.savefig(filename, format="PNG", bbox_inches='tight')
    plt.close() # Đóng plot để giải phóng bộ nhớ
    print(f"✅ Đã tự động vẽ đồ thị và lưu thành file: {filename}")

# --- CÁCH SỬ DỤNG TRONG MỌI BÀI ---
if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), 
        (1, 4), (1, 3), 
        (2, 4), 
        (3, 4), (3, 5), 
        (4, 5)
    ]
    auto_draw_graph(edges, "hinh_bai_1.png")