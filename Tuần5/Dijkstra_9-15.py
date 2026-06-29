import heapq
from typing import Dict, List, Tuple, Any

def tao_g1() -> Dict[int, List[Tuple[int, int]]]:
    return {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }

def tao_luoi() -> List[List[int]]:
    return [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

def bai9_dijkstra_heap(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, float]:
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > kc[u]:
            continue
            
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                heapq.heappush(pq, (kc[v], v))
                
    return kc

def bai10_chon_cai_dat() -> str:
    return (
        "Phân tích chọn cấu trúc dữ liệu:\n"
        "- Đồ thị thưa (E ≈ V): Dùng Priority Queue (Min-Heap). Độ phức tạp O((V+E)log V) ≈ O(V log V), nhanh hơn nhiều so với O(V^2).\n"
        "- Đồ thị dày (E ≈ V^2): Dùng mảng chốt (Bản O(V^2) cơ bản). Vì nếu dùng Heap, việc cập nhật key/push nhiều lần sẽ đẩy độ phức tạp lên O(E log V) ≈ O(V^2 log V), chậm hơn mảng cơ bản."
    )

def bai11_nhieu_nguon(g: Dict[int, List[Tuple[int, int]]], ds_nguon: List[int]) -> Dict[int, float]:
    g_moi = {k: v[:] for k, v in g.items()}
    g_moi[-1] = [(u, 0) for u in ds_nguon]
    
    kc = bai9_dijkstra_heap(g_moi, -1)
    del kc[-1]
    
    return kc

def bai12_qua_dinh_bat_buoc(g: Dict[int, List[Tuple[int, int]]], s: int, k: int, t: int) -> float:
    kc_tu_s = bai9_dijkstra_heap(g, s)
    kc_tu_k = bai9_dijkstra_heap(g, k)
    return kc_tu_s[k] + kc_tu_k[t]

def bai13_dem_duong_di(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, int]:
    kc = {i: float('inf') for i in g}
    dem = {i: 0 for i in g}
    kc[s] = 0
    dem[s] = 1
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > kc[u]:
            continue
            
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                dem[v] = dem[u]
                heapq.heappush(pq, (kc[v], v))
            elif kc[u] + w == kc[v]:
                dem[v] += dem[u]
                
    return dem

def bai14_duong_ngan_nhi(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> float:
    kc1 = {i: float('inf') for i in g}
    kc2 = {i: float('inf') for i in g}
    kc1[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > kc2[u]:
            continue
            
        for v, w in g[u]:
            d_moi = d + w
            if d_moi < kc1[v]:
                kc2[v] = kc1[v]
                kc1[v] = d_moi
                heapq.heappush(pq, (d_moi, v))
            elif kc1[v] < d_moi < kc2[v]:
                kc2[v] = d_moi
                heapq.heappush(pq, (d_moi, v))
                
    return kc2[t]

def bai15_dijkstra_luoi(luoi: List[List[int]]) -> float:
    h = len(luoi)
    c = len(luoi[0])
    kc = {(i, j): float('inf') for i in range(h) for j in range(c)}
    kc[(0, 0)] = luoi[0][0]
    pq = [(luoi[0][0], 0, 0)]
    huong = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        d, ux, uy = heapq.heappop(pq)
        
        if (ux, uy) == (h - 1, c - 1):
            return d
            
        if d > kc[(ux, uy)]:
            continue
            
        for dx, dy in huong:
            vx, vy = ux + dx, uy + dy
            if 0 <= vx < h and 0 <= vy < c:
                w = luoi[vx][vy]
                if kc[(ux, uy)] + w < kc[(vx, vy)]:
                    kc[(vx, vy)] = kc[(ux, uy)] + w
                    heapq.heappush(pq, (kc[(vx, vy)], vx, vy))
                    
    return float('inf')

Noidung = {
    '9': {
        'ten': 'BÀI 9: DIJKSTRA VỚI MIN-HEAP (PRIORITY QUEUE)',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': {0: 0, 1: 3, 2: 1, 3: 4, 4: 7, 5: 9},
        'ham': lambda d: bai9_dijkstra_heap(d['g'], d['s']),
        'format': lambda d, kq: f"dist[]: {kq}"
    },
    '10': {
        'ten': 'BÀI 10: CHỌN CÀI ĐẶT THEO MẬT ĐỘ ĐỒ THỊ',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai10_chon_cai_dat(),
        'format': lambda d, kq: kq
    },
    '11': {
        'ten': 'BÀI 11: ĐA NGUỒN (MULTI-SOURCE)',
        'du_lieu': {'g': tao_g1(), 'ds': [0, 3]},
        'mong_doi': {0: 0, 1: 3, 2: 1, 3: 0, 4: 3, 5: 6},
        'ham': lambda d: bai11_nhieu_nguon(d['g'], d['ds']),
        'format': lambda d, kq: f"Nguồn s={d['ds']}\nKhoảng cách tới nguồn gần nhất: {kq}"
    },
    '12': {
        'ten': 'BÀI 12: ĐI QUA ĐỈNH BẮT BUỘC (0 -> 5 qua 2)',
        'du_lieu': {'g': tao_g1(), 's': 0, 'k': 2, 't': 5},
        'mong_doi': 12,
        'ham': lambda d: bai12_qua_dinh_bat_buoc(d['g'], d['s'], d['k'], d['t']),
        'format': lambda d, kq: f"Đường đi s={d['s']} tới t={d['t']} qua k={d['k']}: {kq}"
    },
    '13': {
        'ten': 'BÀI 13: ĐẾM SỐ ĐƯỜNG ĐI NGẮN NHẤT',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1},
        'ham': lambda d: bai13_dem_duong_di(d['g'], d['s']),
        'format': lambda d, kq: f"Số lượng đường đi tối ưu tới các đỉnh: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: ĐƯỜNG ĐI NGẮN NHÌ (0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': 8,
        'ham': lambda d: bai14_duong_ngan_nhi(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Đường đi ngắn thứ hai từ s={d['s']} tới t={d['t']}: {kq}"
    },
    '15': {
        'ten': 'BÀI 15: DIJKSTRA TRÊN LƯỚI (GRID 3x3)',
        'du_lieu': {'luoi': tao_luoi()},
        'mong_doi': 7,
        'ham': lambda d: bai15_dijkstra_luoi(d['luoi']),
        'format': lambda d, kq: f"Lưới:\n{d['luoi'][0]}\n{d['luoi'][1]}\n{d['luoi'][2]}\nChi phí nhỏ nhất tới đích: {kq}"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU DIJKSTRA: PHIÊN 2 (BÀI 9 - 15) ")
            print(" CHỌN BÀI (9-15) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k:>6}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
        pass