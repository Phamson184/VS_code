import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq

def ve_do_thi(ma_tran, nhan_dinh, ten_file):
    dt = nx.DiGraph()
    so_dinh = len(ma_tran)
    
    for i in range(so_dinh):
        dt.add_node(i, label=nhan_dinh[i])
        for j in range(so_dinh):
            if ma_tran[i][j] > 0:
                dt.add_edge(i, j, weight=ma_tran[i][j])
                
    plt.figure(figsize=(8, 6))
    vi_tri = nx.spring_layout(dt, seed=42)
    
    nhan_hien_thi = {i: nhan_dinh[i] for i in range(so_dinh)}
    nx.draw(dt, vi_tri, labels=nhan_hien_thi, with_labels=True, node_color="#98FB98", node_size=1200, font_weight="bold", edge_color="gray", arrows=True)
    
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

def lay_duong_di(truy_vet, dich, nhan_dinh):
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(nhan_dinh[hien_tai])
        hien_tai = truy_vet[hien_tai]
    return duong_di[::-1]

def xu_ly_bai_toan(tieu_de, ma_tran, nhan_dinh, bat_dau_idx, dich_idx, ten_anh):
    print(f"========== {tieu_de} ==========")
    ve_do_thi(ma_tran, nhan_dinh, ten_anh)
    
    print("--- YÊU CẦU A: VIẾT MA TRẬN KỀ ---")
    dinh_chuoi = "   ".join(nhan_dinh)
    print(f"      {dinh_chuoi}")
    for i, dong in enumerate(ma_tran):
        dong_chuoi = "  ".join(f"{x:>2}" for x in dong)
        print(f"  {nhan_dinh[i]} [{dong_chuoi}]")
        
    print(f"\n--- YÊU CẦU B: TÌM ĐƯỜNG ĐI ({nhan_dinh[bat_dau_idx]} -> {nhan_dinh[dich_idx]}) ---")
    kc, vet = dijkstra_ma_tran(ma_tran, bat_dau_idx)
    
    if kc[dich_idx] == float('inf'):
        print(f"Không có đường đi từ {nhan_dinh[bat_dau_idx]} đến {nhan_dinh[dich_idx]}")
    else:
        path = lay_duong_di(vet, dich_idx, nhan_dinh)
        chuoi_path = " -> ".join(path)
        print(f"Đường đi ngắn nhất: {chuoi_path}")
        print(f"Tổng trọng số: {kc[dich_idx]}")
    print("\n")

if __name__ == "__main__":
    nhan_th3 = ['a', 'b', 'c', 'f', 'g', 'z']
    ma_tran_th3 = [
        [0, 3, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 2, 0],
        [0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0]
    ]
    xu_ly_bai_toan("THỰC HÀNH 03", ma_tran_th3, nhan_th3, 0, 5, "th3_graph.png")

    nhan_th4_h1 = ['0', '1', '2', '3', '4', '5', '6', '7']
    ma_tran_th4_h1 = [
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    xu_ly_bai_toan("THỰC HÀNH 04 - HÌNH 1 (Không trọng số, gán = 1)", ma_tran_th4_h1, nhan_th4_h1, 0, 7, "th4_hinh1.png")

    nhan_th4_h2 = ['a', 'b', 'c', 'd', 'e', 'z']
    ma_tran_th4_h2 = [
        [0, 2, 0, 5, 0, 0],
        [0, 0, 7, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 6, 0],
        [0, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 0]
    ]
    xu_ly_bai_toan("THỰC HÀNH 04 - HÌNH 2", ma_tran_th4_h2, nhan_th4_h2, 0, 5, "th4_hinh2.png")