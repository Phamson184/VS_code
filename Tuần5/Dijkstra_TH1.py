<<<<<<< HEAD
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq

def ve_do_thi(ma_tran, co_huong, ten_file):
    dt = nx.DiGraph() if co_huong else nx.Graph()
    so_dinh = len(ma_tran)
    
    for i in range(so_dinh):
        dt.add_node(i)
        for j in range(so_dinh):
            if ma_tran[i][j] > 0:
                dt.add_edge(i, j, weight=ma_tran[i][j])
                
    plt.figure(figsize=(8, 6))
    vi_tri = nx.spring_layout(dt, seed=42)
    nx.draw(dt, vi_tri, with_labels=True, node_color="#ADD8E6", node_size=1200, font_weight="bold", edge_color="gray", arrows=co_huong)
    
    nhan_canh = nx.get_edge_attributes(dt, 'weight')
    nx.draw_networkx_edge_labels(dt, vi_tri, edge_labels=nhan_canh, font_color="red")
    
    plt.savefig(ten_file, bbox_inches="tight")
    plt.close()

def dijkstra_ma_tran(ma_tran, bat_dau):
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
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = truy_vet[hien_tai]
    return duong_di[::-1]

def xu_ly_bai_toan(tieu_de, ma_tran, co_huong, ten_anh):
    print(f"========== {tieu_de} ==========")
    ve_do_thi(ma_tran, co_huong, ten_anh)
    print(f"[*] Đã xuất bản vẽ đồ thị: {ten_anh}")
    
    print("\n--- NHẬN XÉT INPUT ---")
    loai_dt = "Đồ thị có hướng" if co_huong else "Đồ thị vô hướng"
    print(f"- Loại đồ thị: {loai_dt} gồm {len(ma_tran)} đỉnh.")
    print("- Ma trận kề:")
    for dong in ma_tran:
        print("  " + str(dong))
        
    print("\n--- NHẬN XÉT OUTPUT (DIJKSTRA TỪ ĐỈNH 0) ---")
    kc, vet = dijkstra_ma_tran(ma_tran, 0)
    for i in range(len(ma_tran)):
        if kc[i] == float('inf'):
            print(f"0 đến đỉnh {i}: Không có đường đi")
        else:
            path = lay_duong_di(vet, i)
            chuoi_path = " -> ".join(map(str, path))
            print(f"0 đến đỉnh {i} | Độ dài: {kc[i]:<2} | Chi tiết đường đi: {chuoi_path}")
    print("\n")

if __name__ == "__main__":
    ma_tran_th1 = [
        [0, 3, 0, 1, 0, 0],
        [3, 0, 5, 2, 0, 0],
        [0, 5, 0, 0, 4, 2],
        [1, 2, 0, 0, 6, 0],
        [0, 0, 4, 6, 0, 7],
        [0, 0, 2, 0, 7, 0]
    ]
    xu_ly_bai_toan("THỰC HÀNH 01", ma_tran_th1, co_huong=False, ten_anh="th1_vo_huong.png")

    ma_tran_th2 = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 6, 2, 0, 0],
        [0, 0, 0, 0, 4, 3],
        [0, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0]
    ]
=======
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq

def ve_do_thi(ma_tran, co_huong, ten_file):
    dt = nx.DiGraph() if co_huong else nx.Graph()
    so_dinh = len(ma_tran)
    
    for i in range(so_dinh):
        dt.add_node(i)
        for j in range(so_dinh):
            if ma_tran[i][j] > 0:
                dt.add_edge(i, j, weight=ma_tran[i][j])
                
    plt.figure(figsize=(8, 6))
    vi_tri = nx.spring_layout(dt, seed=42)
    nx.draw(dt, vi_tri, with_labels=True, node_color="#ADD8E6", node_size=1200, font_weight="bold", edge_color="gray", arrows=co_huong)
    
    nhan_canh = nx.get_edge_attributes(dt, 'weight')
    nx.draw_networkx_edge_labels(dt, vi_tri, edge_labels=nhan_canh, font_color="red")
    
    plt.savefig(ten_file, bbox_inches="tight")
    plt.close()

def dijkstra_ma_tran(ma_tran, bat_dau):
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
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = truy_vet[hien_tai]
    return duong_di[::-1]

def xu_ly_bai_toan(tieu_de, ma_tran, co_huong, ten_anh):
    print(f"========== {tieu_de} ==========")
    ve_do_thi(ma_tran, co_huong, ten_anh)
    print(f"[*] Đã xuất bản vẽ đồ thị: {ten_anh}")
    
    print("\n--- NHẬN XÉT INPUT ---")
    loai_dt = "Đồ thị có hướng" if co_huong else "Đồ thị vô hướng"
    print(f"- Loại đồ thị: {loai_dt} gồm {len(ma_tran)} đỉnh.")
    print("- Ma trận kề:")
    for dong in ma_tran:
        print("  " + str(dong))
        
    print("\n--- NHẬN XÉT OUTPUT (DIJKSTRA TỪ ĐỈNH 0) ---")
    kc, vet = dijkstra_ma_tran(ma_tran, 0)
    for i in range(len(ma_tran)):
        if kc[i] == float('inf'):
            print(f"0 đến đỉnh {i}: Không có đường đi")
        else:
            path = lay_duong_di(vet, i)
            chuoi_path = " -> ".join(map(str, path))
            print(f"0 đến đỉnh {i} | Độ dài: {kc[i]:<2} | Chi tiết đường đi: {chuoi_path}")
    print("\n")

if __name__ == "__main__":
    ma_tran_th1 = [
        [0, 3, 0, 1, 0, 0],
        [3, 0, 5, 2, 0, 0],
        [0, 5, 0, 0, 4, 2],
        [1, 2, 0, 0, 6, 0],
        [0, 0, 4, 6, 0, 7],
        [0, 0, 2, 0, 7, 0]
    ]
    xu_ly_bai_toan("THỰC HÀNH 01", ma_tran_th1, co_huong=False, ten_anh="th1_vo_huong.png")

    ma_tran_th2 = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 6, 2, 0, 0],
        [0, 0, 0, 0, 4, 3],
        [0, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0]
    ]
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
    xu_ly_bai_toan("THỰC HÀNH 02", ma_tran_th2, co_huong=True, ten_anh="th2_co_huong.png")