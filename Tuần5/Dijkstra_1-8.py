<<<<<<< HEAD
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

def tao_g2() -> Dict[int, List[Tuple[int, int]]]:
    g = {i: [] for i in range(5)}
    canh = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 6), (3, 4, 4)]
    for u, v, w in canh:
        g[u].append((v, w))
        g[v].append((u, w))
    return g

def bai1_bieu_dien(g: Dict[int, List[Tuple[int, int]]]) -> str:
    kq = []
    for u, ds in g.items():
        kq.append(f"adj[{u}] = {ds}")
    return "\n".join(kq)

def bai2_tinh_tay() -> str:
    return (
        "Thứ tự chốt: 0, 2, 1, 3, 4, 5\n"
        "dist[] sau mỗi bước:\n"
        "B0 (chốt 0): [0, 4, 1, inf, inf, inf]\n"
        "B1 (chốt 2): [0, 3, 1, 6, 9, inf]\n"
        "B2 (chốt 1): [0, 3, 1, 4, 9, inf]\n"
        "B3 (chốt 3): [0, 3, 1, 4, 7, 10]\n"
        "B4 (chốt 4): [0, 3, 1, 4, 7, 9]\n"
        "B5 (chốt 5): [0, 3, 1, 4, 7, 9]"
    )

def dijkstra_v2(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, float]:
    n = len(g)
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    chot = {i: False for i in g}

    for _ in range(n):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc

def bai3_dijkstra_co_ban(g: Dict[int, List[Tuple[int, int]]], s: int) -> List[float]:
    kc = dijkstra_v2(g, s)
    return [kc[i] for i in range(len(g))]

def bai4_in_khoang_cach(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, int]:
    kc = dijkstra_v2(g, s)
    return {k: (v if v != float('inf') else -1) for k, v in kc.items()}

def bai5_vo_huong(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[str, float]:
    kc = dijkstra_v2(g, s)
    chuoi_ten = ['A', 'B', 'C', 'D', 'E']
    return {chuoi_ten[k]: v for k, v in kc.items()}

def bai6_dung_som(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> float:
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    chot = {i: False for i in g}
    
    for _ in range(len(g)):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1 or u == t:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc[t]

def bai7_truy_vet(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> List[int]:
    kc = {i: float('inf') for i in g}
    truoc = {i: -1 for i in g}
    kc[s] = 0
    chot = {i: False for i in g}
    
    for _ in range(len(g)):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1 or u == t:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                truoc[v] = u
                
    duong_di = []
    hien_tai = t
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = truoc[hien_tai]
    
    return duong_di[::-1] if duong_di and duong_di[-1] == s else []

def bai8_ban_kinh(g: Dict[int, List[Tuple[int, int]]], s: int, d: float) -> int:
    kc = dijkstra_v2(g, s)
    dem = sum(1 for v in kc.values() if v <= d)
    return dem

Noidung = {
    '1': {
        'ten': 'BÀI 1: BIỂU DIỄN ĐỒ THỊ',
        'du_lieu': {'g': tao_g1()},
        'mong_doi': None,
        'ham': lambda d: bai1_bieu_dien(d['g']),
        'format': lambda d, kq: f"Danh sách kề G1:\n{kq}"
    },
    '2': {
        'ten': 'BÀI 2: TÍNH TAY ĐƯỜNG ĐI NGẮN NHẤT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai2_tinh_tay(),
        'format': lambda d, kq: kq
    },
    '3': {
        'ten': 'BÀI 3: DIJKSTRA CƠ BẢN TỪ NGUỒN (G1, s=0)',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': [0, 3, 1, 4, 7, 9],
        'ham': lambda d: bai3_dijkstra_co_ban(d['g'], d['s']),
        'format': lambda d, kq: f"dist[]: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: IN KHOẢNG CÁCH TỚI MỌI ĐỈNH (HOẶC -1)',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': {0: 0, 1: 3, 2: 1, 3: 4, 4: 7, 5: 9},
        'ham': lambda d: bai4_in_khoang_cach(d['g'], d['s']),
        'format': lambda d, kq: f"Kết quả: {kq}"
    },
    '5': {
        'ten': 'BÀI 5: ĐỒ THỊ VÔ HƯỚNG CÓ TRỌNG SỐ (G2, NGUỒN A)',
        'du_lieu': {'g': tao_g2(), 's': 0},
        'mong_doi': {'A': 0, 'B': 4, 'C': 3, 'D': 6, 'E': 10},
        'ham': lambda d: bai5_vo_huong(d['g'], d['s']),
        'format': lambda d, kq: f"Khoảng cách từ A: {kq}"
    },
    '6': {
        'ten': 'BÀI 6: ĐƯỜNG ĐI NGẮN NHẤT GIỮA 2 ĐỈNH (0 -> 4, DỪNG SỚM)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': 7,
        'ham': lambda d: bai6_dung_som(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Khoảng cách s={d['s']} tới t={d['t']}: {kq}"
    },
    '7': {
        'ten': 'BÀI 7: TRUY VẾT ĐƯỜNG ĐI (0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': [0, 2, 1, 3, 4],
        'ham': lambda d: bai7_truy_vet(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Đường đi: {' -> '.join(map(str, kq))}"
    },
    '7_unreachable': {
        'ten': 'BÀI 7 (TEST LỖI): TRUY VẾT KHI KHÔNG THỂ TỚI ĐÍCH (5 -> 0)',
        'du_lieu': {'g': tao_g1(), 's': 5, 't': 0},
        'mong_doi': [],
        'ham': lambda d: bai7_truy_vet(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Đường đi: {'Không có đường đi' if not kq else ' -> '.join(map(str, kq))}"
    },
    '8': {
        'ten': 'BÀI 8: SỐ ĐỈNH TRONG BÁN KÍNH D',
        'du_lieu': {'g': tao_g1(), 's': 0, 'd': 3},
        'mong_doi': 3,
        'ham': lambda d: bai8_ban_kinh(d['g'], d['s'], d['d']),
        'format': lambda d, kq: f"D = {d['d']}, Số đỉnh = {kq} (Đỉnh 0, 1, 2)"
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
            print(" MENU DIJKSTRA: PHIÊN 1 (BÀI 1 - 8) ")
            print(" CHỌN BÀI (1-8) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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

def tao_g2() -> Dict[int, List[Tuple[int, int]]]:
    g = {i: [] for i in range(5)}
    canh = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 6), (3, 4, 4)]
    for u, v, w in canh:
        g[u].append((v, w))
        g[v].append((u, w))
    return g

def bai1_bieu_dien(g: Dict[int, List[Tuple[int, int]]]) -> str:
    kq = []
    for u, ds in g.items():
        kq.append(f"adj[{u}] = {ds}")
    return "\n".join(kq)

def bai2_tinh_tay() -> str:
    return (
        "Thứ tự chốt: 0, 2, 1, 3, 4, 5\n"
        "dist[] sau mỗi bước:\n"
        "B0 (chốt 0): [0, 4, 1, inf, inf, inf]\n"
        "B1 (chốt 2): [0, 3, 1, 6, 9, inf]\n"
        "B2 (chốt 1): [0, 3, 1, 4, 9, inf]\n"
        "B3 (chốt 3): [0, 3, 1, 4, 7, 10]\n"
        "B4 (chốt 4): [0, 3, 1, 4, 7, 9]\n"
        "B5 (chốt 5): [0, 3, 1, 4, 7, 9]"
    )

def dijkstra_v2(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, float]:
    n = len(g)
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    chot = {i: False for i in g}

    for _ in range(n):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc

def bai3_dijkstra_co_ban(g: Dict[int, List[Tuple[int, int]]], s: int) -> List[float]:
    kc = dijkstra_v2(g, s)
    return [kc[i] for i in range(len(g))]

def bai4_in_khoang_cach(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[int, int]:
    kc = dijkstra_v2(g, s)
    return {k: (v if v != float('inf') else -1) for k, v in kc.items()}

def bai5_vo_huong(g: Dict[int, List[Tuple[int, int]]], s: int) -> Dict[str, float]:
    kc = dijkstra_v2(g, s)
    chuoi_ten = ['A', 'B', 'C', 'D', 'E']
    return {chuoi_ten[k]: v for k, v in kc.items()}

def bai6_dung_som(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> float:
    kc = {i: float('inf') for i in g}
    kc[s] = 0
    chot = {i: False for i in g}
    
    for _ in range(len(g)):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1 or u == t:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc[t]

def bai7_truy_vet(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> List[int]:
    kc = {i: float('inf') for i in g}
    truoc = {i: -1 for i in g}
    kc[s] = 0
    chot = {i: False for i in g}
    
    for _ in range(len(g)):
        u = -1
        min_kc = float('inf')
        for i in g:
            if not chot[i] and kc[i] < min_kc:
                min_kc = kc[i]
                u = i
        
        if u == -1 or u == t:
            break
        chot[u] = True
        
        for v, w in g[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                truoc[v] = u
                
    duong_di = []
    hien_tai = t
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = truoc[hien_tai]
    
    return duong_di[::-1] if duong_di and duong_di[-1] == s else []

def bai8_ban_kinh(g: Dict[int, List[Tuple[int, int]]], s: int, d: float) -> int:
    kc = dijkstra_v2(g, s)
    dem = sum(1 for v in kc.values() if v <= d)
    return dem

Noidung = {
    '1': {
        'ten': 'BÀI 1: BIỂU DIỄN ĐỒ THỊ',
        'du_lieu': {'g': tao_g1()},
        'mong_doi': None,
        'ham': lambda d: bai1_bieu_dien(d['g']),
        'format': lambda d, kq: f"Danh sách kề G1:\n{kq}"
    },
    '2': {
        'ten': 'BÀI 2: TÍNH TAY ĐƯỜNG ĐI NGẮN NHẤT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai2_tinh_tay(),
        'format': lambda d, kq: kq
    },
    '3': {
        'ten': 'BÀI 3: DIJKSTRA CƠ BẢN TỪ NGUỒN (G1, s=0)',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': [0, 3, 1, 4, 7, 9],
        'ham': lambda d: bai3_dijkstra_co_ban(d['g'], d['s']),
        'format': lambda d, kq: f"dist[]: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: IN KHOẢNG CÁCH TỚI MỌI ĐỈNH (HOẶC -1)',
        'du_lieu': {'g': tao_g1(), 's': 0},
        'mong_doi': {0: 0, 1: 3, 2: 1, 3: 4, 4: 7, 5: 9},
        'ham': lambda d: bai4_in_khoang_cach(d['g'], d['s']),
        'format': lambda d, kq: f"Kết quả: {kq}"
    },
    '5': {
        'ten': 'BÀI 5: ĐỒ THỊ VÔ HƯỚNG CÓ TRỌNG SỐ (G2, NGUỒN A)',
        'du_lieu': {'g': tao_g2(), 's': 0},
        'mong_doi': {'A': 0, 'B': 4, 'C': 3, 'D': 6, 'E': 10},
        'ham': lambda d: bai5_vo_huong(d['g'], d['s']),
        'format': lambda d, kq: f"Khoảng cách từ A: {kq}"
    },
    '6': {
        'ten': 'BÀI 6: ĐƯỜNG ĐI NGẮN NHẤT GIỮA 2 ĐỈNH (0 -> 4, DỪNG SỚM)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': 7,
        'ham': lambda d: bai6_dung_som(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Khoảng cách s={d['s']} tới t={d['t']}: {kq}"
    },
    '7': {
        'ten': 'BÀI 7: TRUY VẾT ĐƯỜNG ĐI (0 -> 4)',
        'du_lieu': {'g': tao_g1(), 's': 0, 't': 4},
        'mong_doi': [0, 2, 1, 3, 4],
        'ham': lambda d: bai7_truy_vet(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Đường đi: {' -> '.join(map(str, kq))}"
    },
    '7_unreachable': {
        'ten': 'BÀI 7 (TEST LỖI): TRUY VẾT KHI KHÔNG THỂ TỚI ĐÍCH (5 -> 0)',
        'du_lieu': {'g': tao_g1(), 's': 5, 't': 0},
        'mong_doi': [],
        'ham': lambda d: bai7_truy_vet(d['g'], d['s'], d['t']),
        'format': lambda d, kq: f"Đường đi: {'Không có đường đi' if not kq else ' -> '.join(map(str, kq))}"
    },
    '8': {
        'ten': 'BÀI 8: SỐ ĐỈNH TRONG BÁN KÍNH D',
        'du_lieu': {'g': tao_g1(), 's': 0, 'd': 3},
        'mong_doi': 3,
        'ham': lambda d: bai8_ban_kinh(d['g'], d['s'], d['d']),
        'format': lambda d, kq: f"D = {d['d']}, Số đỉnh = {kq} (Đỉnh 0, 1, 2)"
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
            print(" MENU DIJKSTRA: PHIÊN 1 (BÀI 1 - 8) ")
            print(" CHỌN BÀI (1-8) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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