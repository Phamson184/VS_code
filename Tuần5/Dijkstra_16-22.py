<<<<<<< HEAD
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

def tao_g_xac_suat() -> Dict[int, List[Tuple[int, float]]]:
    return {
        0: [(1, 0.8), (2, 0.5)],
        1: [(3, 0.5)],
        2: [(3, 0.9)],
        3: []
    }

def tao_g_nhien_lieu() -> Dict[int, List[Tuple[int, int, int]]]:
    # value: (đỉnh_đích, thời_gian, hao_nhiên_liệu)
    return {
        0: [(1, 2, 5), (2, 5, 2)],
        1: [(3, 4, 3)],
        2: [(3, 1, 6)],
        3: []
    }

def bai16_trong_so_dinh(g_canh: Dict[int, List[int]], cp_dinh: Dict[int, int], s: int) -> Dict[int, int]:
    kc = {i: float('inf') for i in g_canh}
    kc[s] = cp_dinh[s]
    pq = [(cp_dinh[s], s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > kc[u]: continue
            
        for v in g_canh[u]:
            if kc[u] + cp_dinh[v] < kc[v]:
                kc[v] = kc[u] + cp_dinh[v]
                heapq.heappush(pq, (kc[v], v))
    return kc

def bai17_bottleneck(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> float:
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == t: return d
        if d > kc[u]: continue
            
        for v, w in g[u]:
            max_canh = max(d, w)
            if max_canh < kc[v]:
                kc[v] = max_canh
                heapq.heappush(pq, (kc[v], v))
    return float('inf')

def bai18_giai_thich_am() -> str:
    return (
        "Khi có cạnh trọng số âm (VD: 2 -> 1 giá -4):\n"
        "- Dijkstra dùng mảng chốt (visited) sẽ bị sai, vì nó mặc định đỉnh lấy ra khỏi PQ đã là tối ưu.\n"
        "- Đỉnh 1 có thể đã được chốt với khoảng cách 5 (từ 0 -> 1).\n"
        "- Sau đó duyệt qua đỉnh 2, cập nhật lại đỉnh 1 qua cạnh âm thành 2 - 4 = -2, phá vỡ tính bất biến.\n"
        "- Thuật toán thay thế: Bellman-Ford."
    )

def bai19_xac_suat(g: Dict[int, List[Tuple[int, float]]], s: int, t: int) -> float:
    xs = {i: 0.0 for i in g}
    xs[s] = 1.0
    pq = [(-1.0, s)] 
    
    while pq:
        p, u = heapq.heappop(pq)
        p = -p 
        if u == t: return p
        if p < xs[u]: continue
            
        for v, w in g[u]:
            if xs[u] * w > xs[v]:
                xs[v] = xs[u] * w
                heapq.heappush(pq, (-xs[v], v))
    return 0.0

def bai20_k_duong_di(g: Dict[int, List[Tuple[int, int]]], s: int, t: int, k: int) -> List[float]:
    pq = [(0, s)]
    dem = {i: 0 for i in g}
    kq = []
    
    while pq:
        d, u = heapq.heappop(pq)
        dem[u] += 1
        
        if u == t:
            kq.append(d)
            if len(kq) == k: break
            
        if dem[u] <= k:
            for v, w in g[u]:
                heapq.heappush(pq, (d + w, v))
                
    return kq

def bai21_trang_thai(g: Dict[int, List[Tuple[int, int, int]]], s: int, t: int, max_xang: int) -> int:
    pq = [(0, s, max_xang)]
    kc = {} 
    
    while pq:
        d, u, xang = heapq.heappop(pq)
        if u == t: return d
        
        if (u, xang) in kc and kc[(u, xang)] <= d:
            continue
        kc[(u, xang)] = d
        
        for v, tg, hao_xang in g[u]:
            xang_con = xang - hao_xang
            if xang_con >= 0:
                heapq.heappush(pq, (d + tg, v, xang_con))
    return -1

def bai22_gioi_han_canh(g: Dict[int, List[Tuple[int, int]]], s: int, t: int, max_canh: int) -> float:
    pq = [(0, s, 0)]
    kc = {} 
    min_d = float('inf')
    
    while pq:
        d, u, canh = heapq.heappop(pq)
        if canh > max_canh: continue
        
        if u == t: 
            min_d = min(min_d, d)
            continue
        
        if (u, canh) in kc and kc[(u, canh)] <= d:
            continue
        kc[(u, canh)] = d
        
        for v, w in g[u]:
            heapq.heappush(pq, (d + w, v, canh + 1))
            
    return min_d if min_d != float('inf') else -1

Noidung = {
    '16': {
        'ten': 'BÀI 16: TRỌNG SỐ TRÊN ĐỈNH',
        'du_lieu': {
            'g': {0: [1, 2], 1: [3], 2: [3], 3: []}, 
            'cp': {0: 1, 1: 5, 2: 2, 3: 1}, 
            's': 0
        },
        'mong_doi': {0: 1, 1: 6, 2: 3, 3: 4},
        'ham': lambda d: bai16_trong_so_dinh(d['g'], d['cp'], d['s']),
        'format': lambda d, kq: f"Chi phí tới các đỉnh: {kq}"
    },
    '17': {
        'ten': 'BÀI 17: ĐƯỜNG ĐI BOTTLENECK (0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': 3,
        'ham': lambda d: bai17_bottleneck(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Cạnh lớn nhất nhỏ nhất trên đường đi: {kq}"
    },
    '18': {
        'ten': 'BÀI 18: LÝ DO KHÔNG DÙNG CẠNH ÂM',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai18_giai_thich_am(),
        'format': lambda d, kq: kq
    },
    '19': {
        'ten': 'BÀI 19: ĐƯỜNG ĐI XÁC SUẤT LỚN NHẤT (0 -> 3)',
        'du_lieu': {'g': tao_g_xac_suat(), 's': 0, 't': 3},
        'mong_doi': 0.45,
        'ham': lambda d: bai19_xac_suat(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Xác suất cao nhất: {kq}"
    },
    '20': {
        'ten': 'BÀI 20: K ĐƯỜNG ĐI NGẮN NHẤT (K=3, 0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4, 'k': 3},
        'mong_doi': [7, 8, 9],
        'ham': lambda d: bai20_k_duong_di(d['g'], d['s'], d['t'], d['k']),
        'format': lambda d, kq: f"Chiều dài 3 đường đi tốt nhất: {kq}"
    },
    '21': {
        'ten': 'BÀI 21: TRẠNG THÁI MỞ RỘNG (GIỚI HẠN NHIÊN LIỆU)',
        'du_lieu': {'g': tao_g_nhien_lieu(), 's': 0, 't': 3, 'max_xang': 7},
        'mong_doi': 6,
        'ham': lambda d: bai21_trang_thai(d['g'], d['s'], d['t'], d['max_xang']),
        'format': lambda d, kq: f"Thời gian ngắn nhất tới đích với nhiên liệu <= {d['max_xang']}: {kq}"
    },
    '22': {
        'ten': 'BÀI 22: GIỚI HẠN SỐ CẠNH TRUNG CHUYỂN (TỐI ĐA 2 CẠNH, 0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4, 'max': 2},
        'mong_doi': 9,
        'ham': lambda d: bai22_gioi_han_canh(d['g'], d['s'], d['t'], d['max']),
        'format': lambda d, kq: f"Chi phí rẻ nhất dùng <= {d['max']} cạnh: {kq}"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if isinstance(kq, float) and isinstance(cfg['mong_doi'], float):
            is_match = abs(kq - cfg['mong_doi']) < 1e-9
        else:
            is_match = kq == cfg['mong_doi']
            
        if is_match:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU DIJKSTRA: PHIÊN 3 (BÀI 16 - 22) ")
            print(" CHỌN BÀI (16-22) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
=======
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

def tao_g_xac_suat() -> Dict[int, List[Tuple[int, float]]]:
    return {
        0: [(1, 0.8), (2, 0.5)],
        1: [(3, 0.5)],
        2: [(3, 0.9)],
        3: []
    }

def tao_g_nhien_lieu() -> Dict[int, List[Tuple[int, int, int]]]:
    # value: (đỉnh_đích, thời_gian, hao_nhiên_liệu)
    return {
        0: [(1, 2, 5), (2, 5, 2)],
        1: [(3, 4, 3)],
        2: [(3, 1, 6)],
        3: []
    }

def bai16_trong_so_dinh(g_canh: Dict[int, List[int]], cp_dinh: Dict[int, int], s: int) -> Dict[int, int]:
    kc = {i: float('inf') for i in g_canh}
    kc[s] = cp_dinh[s]
    pq = [(cp_dinh[s], s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > kc[u]: continue
            
        for v in g_canh[u]:
            if kc[u] + cp_dinh[v] < kc[v]:
                kc[v] = kc[u] + cp_dinh[v]
                heapq.heappush(pq, (kc[v], v))
    return kc

def bai17_bottleneck(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> float:
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == t: return d
        if d > kc[u]: continue
            
        for v, w in g[u]:
            max_canh = max(d, w)
            if max_canh < kc[v]:
                kc[v] = max_canh
                heapq.heappush(pq, (kc[v], v))
    return float('inf')

def bai18_giai_thich_am() -> str:
    return (
        "Khi có cạnh trọng số âm (VD: 2 -> 1 giá -4):\n"
        "- Dijkstra dùng mảng chốt (visited) sẽ bị sai, vì nó mặc định đỉnh lấy ra khỏi PQ đã là tối ưu.\n"
        "- Đỉnh 1 có thể đã được chốt với khoảng cách 5 (từ 0 -> 1).\n"
        "- Sau đó duyệt qua đỉnh 2, cập nhật lại đỉnh 1 qua cạnh âm thành 2 - 4 = -2, phá vỡ tính bất biến.\n"
        "- Thuật toán thay thế: Bellman-Ford."
    )

def bai19_xac_suat(g: Dict[int, List[Tuple[int, float]]], s: int, t: int) -> float:
    xs = {i: 0.0 for i in g}
    xs[s] = 1.0
    pq = [(-1.0, s)] 
    
    while pq:
        p, u = heapq.heappop(pq)
        p = -p 
        if u == t: return p
        if p < xs[u]: continue
            
        for v, w in g[u]:
            if xs[u] * w > xs[v]:
                xs[v] = xs[u] * w
                heapq.heappush(pq, (-xs[v], v))
    return 0.0

def bai20_k_duong_di(g: Dict[int, List[Tuple[int, int]]], s: int, t: int, k: int) -> List[float]:
    pq = [(0, s)]
    dem = {i: 0 for i in g}
    kq = []
    
    while pq:
        d, u = heapq.heappop(pq)
        dem[u] += 1
        
        if u == t:
            kq.append(d)
            if len(kq) == k: break
            
        if dem[u] <= k:
            for v, w in g[u]:
                heapq.heappush(pq, (d + w, v))
                
    return kq

def bai21_trang_thai(g: Dict[int, List[Tuple[int, int, int]]], s: int, t: int, max_xang: int) -> int:
    pq = [(0, s, max_xang)]
    kc = {} 
    
    while pq:
        d, u, xang = heapq.heappop(pq)
        if u == t: return d
        
        if (u, xang) in kc and kc[(u, xang)] <= d:
            continue
        kc[(u, xang)] = d
        
        for v, tg, hao_xang in g[u]:
            xang_con = xang - hao_xang
            if xang_con >= 0:
                heapq.heappush(pq, (d + tg, v, xang_con))
    return -1

def bai22_gioi_han_canh(g: Dict[int, List[Tuple[int, int]]], s: int, t: int, max_canh: int) -> float:
    pq = [(0, s, 0)]
    kc = {} 
    min_d = float('inf')
    
    while pq:
        d, u, canh = heapq.heappop(pq)
        if canh > max_canh: continue
        
        if u == t: 
            min_d = min(min_d, d)
            continue
        
        if (u, canh) in kc and kc[(u, canh)] <= d:
            continue
        kc[(u, canh)] = d
        
        for v, w in g[u]:
            heapq.heappush(pq, (d + w, v, canh + 1))
            
    return min_d if min_d != float('inf') else -1

Noidung = {
    '16': {
        'ten': 'BÀI 16: TRỌNG SỐ TRÊN ĐỈNH',
        'du_lieu': {
            'g': {0: [1, 2], 1: [3], 2: [3], 3: []}, 
            'cp': {0: 1, 1: 5, 2: 2, 3: 1}, 
            's': 0
        },
        'mong_doi': {0: 1, 1: 6, 2: 3, 3: 4},
        'ham': lambda d: bai16_trong_so_dinh(d['g'], d['cp'], d['s']),
        'format': lambda d, kq: f"Chi phí tới các đỉnh: {kq}"
    },
    '17': {
        'ten': 'BÀI 17: ĐƯỜNG ĐI BOTTLENECK (0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': 3,
        'ham': lambda d: bai17_bottleneck(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Cạnh lớn nhất nhỏ nhất trên đường đi: {kq}"
    },
    '18': {
        'ten': 'BÀI 18: LÝ DO KHÔNG DÙNG CẠNH ÂM',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai18_giai_thich_am(),
        'format': lambda d, kq: kq
    },
    '19': {
        'ten': 'BÀI 19: ĐƯỜNG ĐI XÁC SUẤT LỚN NHẤT (0 -> 3)',
        'du_lieu': {'g': tao_g_xac_suat(), 's': 0, 't': 3},
        'mong_doi': 0.45,
        'ham': lambda d: bai19_xac_suat(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Xác suất cao nhất: {kq}"
    },
    '20': {
        'ten': 'BÀI 20: K ĐƯỜNG ĐI NGẮN NHẤT (K=3, 0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4, 'k': 3},
        'mong_doi': [7, 8, 9],
        'ham': lambda d: bai20_k_duong_di(d['g'], d['s'], d['t'], d['k']),
        'format': lambda d, kq: f"Chiều dài 3 đường đi tốt nhất: {kq}"
    },
    '21': {
        'ten': 'BÀI 21: TRẠNG THÁI MỞ RỘNG (GIỚI HẠN NHIÊN LIỆU)',
        'du_lieu': {'g': tao_g_nhien_lieu(), 's': 0, 't': 3, 'max_xang': 7},
        'mong_doi': 6,
        'ham': lambda d: bai21_trang_thai(d['g'], d['s'], d['t'], d['max_xang']),
        'format': lambda d, kq: f"Thời gian ngắn nhất tới đích với nhiên liệu <= {d['max_xang']}: {kq}"
    },
    '22': {
        'ten': 'BÀI 22: GIỚI HẠN SỐ CẠNH TRUNG CHUYỂN (TỐI ĐA 2 CẠNH, 0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4, 'max': 2},
        'mong_doi': 9,
        'ham': lambda d: bai22_gioi_han_canh(d['g'], d['s'], d['t'], d['max']),
        'format': lambda d, kq: f"Chi phí rẻ nhất dùng <= {d['max']} cạnh: {kq}"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if isinstance(kq, float) and isinstance(cfg['mong_doi'], float):
            is_match = abs(kq - cfg['mong_doi']) < 1e-9
        else:
            is_match = kq == cfg['mong_doi']
            
        if is_match:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU DIJKSTRA: PHIÊN 3 (BÀI 16 - 22) ")
            print(" CHỌN BÀI (16-22) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
        pass