import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq

def ve_do_thi(ma_tran, co_huong, ten_file, map_dinh=None):
    """Vẽ và lưu đồ thị ra file ảnh."""
    dt = nx.DiGraph() if co_huong else nx.Graph()
    so_dinh = len(ma_tran)
    
    for i in range(so_dinh):
        ten_node = map_dinh[i] if map_dinh else i
        dt.add_node(ten_node)
        for j in range(so_dinh):
            if ma_tran[i][j] > 0:
                ten_node_dich = map_dinh[j] if map_dinh else j
                dt.add_edge(ten_node, ten_node_dich, weight=ma_tran[i][j])
                
    plt.figure(figsize=(8, 6))
    vi_tri = nx.spring_layout(dt, seed=42)
    nx.draw(dt, vi_tri, with_labels=True, node_color="#ADD8E6", node_size=1200, font_weight="bold", edge_color="gray", arrows=co_huong)
    
    nhan_canh = nx.get_edge_attributes(dt, 'weight')
    nx.draw_networkx_edge_labels(dt, vi_tri, edge_labels=nhan_canh, font_color="red")
    
    plt.savefig(ten_file, bbox_inches="tight")
    plt.close()

def dijkstra_ma_tran(ma_tran, bat_dau):
    """Thuật toán Dijkstra tối ưu bằng Hàng đợi ưu tiên (Priority Queue / heapq)."""
    so_dinh = len(ma_tran)
    khoang_cach = {i: float('inf') for i in range(so_dinh)}
    truy_vet = {i: -1 for i in range(so_dinh)}
    khoang_cach[bat_dau] = 0
    hang_doi = [(0, bat_dau)]
    
    while hang_doi:
        kc_hien_tai, u = heapq.heappop(hang_doi)
        
        if kc_hien_tai > khoang_cach[u]:
            continue
            
        for v in range(so_dinh):
            trong_so = ma_tran[u][v]
            if trong_so > 0:
                kc_moi = kc_hien_tai + trong_so
                if kc_moi < khoang_cach[v]:
                    khoang_cach[v] = kc_moi
                    truy_vet[v] = u
                    heapq.heappush(hang_doi, (kc_moi, v))
                    
    return khoang_cach, truy_vet

def lay_duong_di(truy_vet, dich):
    """Truy vết lại đường đi từ mảng vet."""
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = truy_vet[hien_tai]
    return duong_di[::-1]

def xu_ly_bai_toan(tieu_de, ma_tran, co_huong, ten_anh, dinh_bat_dau=0, map_dinh=None):
    """Hàm Wrapper xử lý toàn bộ logic In ấn, Gọi hàm và Chấm điểm."""
    print(f"\n{'='*50}\n {tieu_de}\n{'='*50}")
    
    # 1. Vẽ đồ thị
    ve_do_thi(ma_tran, co_huong, ten_anh, map_dinh)
    print(f"[*] Đã xuất bản vẽ đồ thị: {ten_anh}")
    
    # 2. Nhận xét Input
    print("\n--- NHẬN XÉT INPUT ---")
    loai_dt = "Đồ thị có hướng" if co_huong else "Đồ thị vô hướng"
    print(f"- Loại đồ thị: {loai_dt} gồm {len(ma_tran)} đỉnh.")
    print("- Ma trận kề:")
    for dong in ma_tran:
        print("  " + str(dong))
        
    # 3. Chạy Dijkstra và Nhận xét Output
    ten_dinh_xuat_phat = map_dinh[dinh_bat_dau] if map_dinh else str(dinh_bat_dau)
    print(f"\n--- NHẬN XÉT OUTPUT (DIJKSTRA TỪ ĐỈNH {ten_dinh_xuat_phat}) ---")
    kc, vet = dijkstra_ma_tran(ma_tran, dinh_bat_dau)
    
    for i in range(len(ma_tran)):
        ten_dinh_dich = map_dinh[i] if map_dinh else str(i)
        
        if kc[i] == float('inf'):
            print(f"{ten_dinh_xuat_phat} đến đỉnh {ten_dinh_dich}: Không có đường đi")
        else:
            path = lay_duong_di(vet, i)
            # Ánh xạ tên đỉnh nếu có
            if map_dinh:
                chuoi_path = " -> ".join([map_dinh[p] for p in path])
            else:
                chuoi_path = " -> ".join(map(str, path))
            print(f"{ten_dinh_xuat_phat} đến đỉnh {ten_dinh_dich:<2} | Độ dài: {kc[i]:<2} | Chi tiết: {chuoi_path}")

if __name__ == "__main__":
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU: ĐỒ THỊ & DIJKSTRA ")
            print(" CHỌN BÀI (4-6) HOẶC 0 ĐỂ THOÁT")
            print("*"*50)
            print(" 4. THỰC HÀNH 04 (Đồ thị Vô Hướng)")
            print(" 5. THỰC HÀNH 05 (Đồ thị Có Hướng)")
            print(" 6. THỰC HÀNH 06 (Trích xuất từ Ảnh Hình 1)")
            
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
                
            elif chon == '4':
                ma_tran_th4 = [
                    [0, 3, 0, 1, 0, 0],
                    [3, 0, 5, 2, 0, 0],
                    [0, 5, 0, 0, 0, 2], # Đã fix: xóa số 4 ở vị trí index 4
                    [1, 2, 0, 0, 6, 0],
                    [0, 0, 0, 6, 0, 7], # Đã fix: xóa số 4 ở vị trí index 2
                    [0, 0, 2, 0, 7, 0]
                ]
                xu_ly_bai_toan("THỰC HÀNH 04", ma_tran_th4, co_huong=False, ten_anh="th4_vo_huong.png")
                
            elif chon == '5':
                ma_tran_th5 = [
                    [0, 3, 0, 0, 0, 0], # Đã fix: xóa số 4 ở vị trí index 3
                    [0, 0, 6, 2, 0, 0],
                    [0, 0, 0, 0, 4, 3],
                    [0, 0, 1, 0, 4, 0],
                    [0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0]
                ]
                xu_ly_bai_toan("THỰC HÀNH 05", ma_tran_th5, co_huong=True, ten_anh="th5_co_huong.png")
                
            elif chon == '6':
                # Map tên đỉnh thành chỉ số Index để chạy thuật toán: 
                # a:0, b:1, c:2, f:3, g:4, z:5
                dict_map = {0: 'a', 1: 'b', 2: 'c', 3: 'f', 4: 'g', 5: 'z'}
                
                # Trích xuất ma trận từ hình ảnh cung cấp (Hình 1)
                ma_tran_th6 = [
                    [0, 3, 0, 1, 0, 0],  # a (0) đi b(3), f(1)
                    [0, 0, 7, 0, 0, 0],  # b (1) đi c(7)
                    [0, 0, 0, 0, 0, 3],  # c (2) đi z(3)
                    [0, 0, 9, 0, 2, 0],  # f (3) đi c(9), g(2)
                    [0, 0, 3, 0, 0, 7],  # g (4) đi c(3), z(7)
                    [0, 0, 0, 0, 0, 0]   # z (5) không đi đâu
                ]
                xu_ly_bai_toan("THỰC HÀNH 06", ma_tran_th6, co_huong=True, 
                               ten_anh="th6_hinh1.png", dinh_bat_dau=0, map_dinh=dict_map)
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass