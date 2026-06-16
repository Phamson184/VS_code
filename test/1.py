import heapq
from collections import deque

TAP_DINH = ['A', 'B', 'C', 'D', 'E', 'F']

MA_TRAN_KE = [
    [0, 2, 3, 0, 0, 0], 
    [2, 0, 0, 5, 2, 0], 
    [3, 0, 0, 0, 5, 0], 
    [0, 5, 0, 0, 1, 2], 
    [0, 2, 5, 1, 0, 4], 
    [0, 0, 0, 2, 4, 0]  
]

def lay_dinh_ke(dinh_idx):
    ke = {}
    for i, trong_so in enumerate(MA_TRAN_KE[dinh_idx]):
        if trong_so > 0:
            ke[i] = trong_so
    return ke

def bfs_ma_tran(bat_dau, dich):
    hang_doi = deque([(bat_dau, [bat_dau], 0)])
    da_tham = {bat_dau}
    
    while hang_doi:
        hien_tai, duong_di, tong_trong_so = hang_doi.popleft()
        
        if hien_tai == dich:
            return duong_di, tong_trong_so
            
        cac_dinh_ke = lay_dinh_ke(hien_tai)
        for dinh_ke, trong_so in cac_dinh_ke.items():
            if dinh_ke not in da_tham:
                da_tham.add(dinh_ke)
                hang_doi.append((dinh_ke, duong_di + [dinh_ke], tong_trong_so + trong_so))
                
    return None, 0

def dfs_ma_tran(hien_tai, dich, da_tham, duong_di, tong_trong_so):
    da_tham.add(hien_tai)
    duong_di.append(hien_tai)
    
    if hien_tai == dich:
        return duong_di, tong_trong_so
        
    cac_dinh_ke = lay_dinh_ke(hien_tai)
    for dinh_ke, trong_so in cac_dinh_ke.items():
        if dinh_ke not in da_tham:
            kq_duong, kq_trong_so = dfs_ma_tran(dinh_ke, dich, da_tham, duong_di, tong_trong_so + trong_so)
            if kq_duong:
                return kq_duong, kq_trong_so
                
    duong_di.pop()
    return None, 0

def tham_lam_ma_tran(bat_dau, dich):
    da_tham = {bat_dau}
    duong_di = [bat_dau]
    tong_trong_so = 0
    hien_tai = bat_dau
    
    while hien_tai != dich:
        chua_tham = {d: ts for d, ts in lay_dinh_ke(hien_tai).items() if d not in da_tham}
        
        if not chua_tham:
            return None, 0
            
        tiep_theo = min(chua_tham, key=chua_tham.get)
        tong_trong_so += chua_tham[tiep_theo]
        
        da_tham.add(tiep_theo)
        duong_di.append(tiep_theo)
        hien_tai = tiep_theo
        
    return duong_di, tong_trong_so

def dijkstra_ma_tran_co_vet(bat_dau, tap_dinh, ma_tran):
    n = len(tap_dinh)
    khoang_cach = {i: float('inf') for i in range(n)}
    truy_vet = {i: -1 for i in range(n)}
    khoang_cach[bat_dau] = 0
    hang_doi = [(0, bat_dau)]
    
    while hang_doi:
        kc, u = heapq.heappop(hang_doi)
        if kc > khoang_cach[u]: 
            continue
            
        for v, trong_so in enumerate(ma_tran[u]):
            if trong_so > 0:
                kc_moi = kc + trong_so
                if kc_moi < khoang_cach[v]:
                    khoang_cach[v] = kc_moi
                    truy_vet[v] = u
                    heapq.heappush(hang_doi, (kc_moi, v))
                    
    return khoang_cach, truy_vet

def lay_duong_di(truy_vet, bat_dau, dich, tap_dinh):
    if truy_vet[dich] == -1 and bat_dau != dich:
        return []
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(tap_dinh[hien_tai])
        hien_tai = truy_vet[hien_tai]
    return duong_di[::-1]

if __name__ == "__main__":
    idx_A = TAP_DINH.index('A')
    idx_F = TAP_DINH.index('F')
    idx_D = TAP_DINH.index('D')
    
    print("A) THUẬT TOÁN BFS (A -> F)")
    kq_bfs, ts_bfs = bfs_ma_tran(idx_A, idx_F)
    chuoi_bfs = " -> ".join([TAP_DINH[i] for i in kq_bfs])
    print(f"Đường đi: {chuoi_bfs}")
    print(f"Tổng trọng số: {ts_bfs}\n")
    
    print("B) THUẬT TOÁN DFS (A -> F)")
    kq_dfs, ts_dfs = dfs_ma_tran(idx_A, idx_F, set(), [], 0)
    chuoi_dfs = " -> ".join([TAP_DINH[i] for i in kq_dfs])
    print(f"Đường đi: {chuoi_dfs}")
    print(f"Tổng trọng số: {ts_dfs}\n")
    
    print("C) THUẬT TOÁN THAM LAM (A -> F)")
    kq_tl, ts_tl = tham_lam_ma_tran(idx_A, idx_F)
    chuoi_tl = " -> ".join([TAP_DINH[i] for i in kq_tl])
    print(f"Đường đi: {chuoi_tl}")
    print(f"Tổng trọng số: {ts_tl}\n")
    
    print("D) THUẬT TOÁN DIJKSTRA (TỪ ĐỈNH D)")
    kq_dijkstra, truy_vet_dijkstra = dijkstra_ma_tran_co_vet(idx_D, TAP_DINH, MA_TRAN_KE)
    
    for i in range(len(TAP_DINH)):
        if kq_dijkstra[i] != float('inf'):
            path = lay_duong_di(truy_vet_dijkstra, idx_D, i, TAP_DINH)
            chuoi_path = " -> ".join(path)
            print(f"Khoảng cách D -> {TAP_DINH[i]}: {kq_dijkstra[i]:<3} | Đường đi: {chuoi_path}")