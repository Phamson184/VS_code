<<<<<<< HEAD
import heapq
from typing import Dict, List, Tuple, Any

def bai23_chien_luoc_truy_van() -> str:
    return (
        "Chiến lược xử lý Q truy vấn (s, t):\n"
        "- Nếu Q nhỏ: Chạy Dijkstra trực tiếp cho mỗi truy vấn. Thời gian: O(Q * (V + E) log V).\n"
        "- Nếu Q lớn và đồ thị thưa: Tiền xử lý bằng cách chạy Dijkstra từ tất cả V đỉnh (All-Pairs Shortest Path), lưu kết quả vào ma trận V x V. Thời gian tiền xử lý: O(V * (V + E) log V). Thời gian truy vấn: O(1).\n"
        "- Nếu Q lớn và đồ thị dày: Cân nhắc dùng thuật toán Floyd-Warshall O(V^3) để tiền xử lý."
    )

def bai24_astar_vs_dijkstra() -> Tuple[int, int]:
    # Tạo một lưới 5x5 có vật cản (chi phí cao = 10) để thấy rõ sự khác biệt
    luoi = [
        [1, 1, 1, 10, 1],
        [1, 10, 1, 10, 1],
        [1, 10, 1, 1, 1],
        [1, 10, 10, 10, 1],
        [1, 1, 1, 1, 1]
    ]
    h, c = 5, 5
    s, t = (0, 0), (4, 4)
    huong = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Tính min_cost để đảm bảo heuristic là admissible
    min_cost = min(luoi[i][j] for i in range(h) for j in range(c))
    
    # --- Chạy Dijkstra ---
    kc_d = {(i, j): float('inf') for i in range(h) for j in range(c)}
    kc_d[s] = luoi[s[0]][s[1]]
    pq_d = [(kc_d[s], s)]
    duyet_d = 0
    
    while pq_d:
        d, u = heapq.heappop(pq_d)
        
        # Kiểm tra stale trước khi đếm
        if d > kc_d[u]: 
            continue
            
        duyet_d += 1
        if u == t: 
            break
        
        for dx, dy in huong:
            vx, vy = u[0] + dx, u[1] + dy
            if 0 <= vx < h and 0 <= vy < c:
                w = luoi[vx][vy]
                if kc_d[u] + w < kc_d[(vx, vy)]:
                    kc_d[(vx, vy)] = kc_d[u] + w
                    heapq.heappush(pq_d, (kc_d[(vx, vy)], (vx, vy)))
                    
    # --- Chạy A* (Heuristic: Manhattan distance * min_cost) ---
    def manhattan(p1, p2):
        return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) * min_cost
        
    kc_a = {(i, j): float('inf') for i in range(h) for j in range(c)}
    kc_a[s] = luoi[s[0]][s[1]]
    pq_a = [(kc_a[s] + manhattan(s, t), kc_a[s], s)]
    duyet_a = 0
    
    while pq_a:
        f, g_val, u = heapq.heappop(pq_a)
        
        # Kiểm tra stale trước khi đếm
        if g_val > kc_a[u]: 
            continue
            
        duyet_a += 1
        if u == t: 
            break
        
        for dx, dy in huong:
            vx, vy = u[0] + dx, u[1] + dy
            if 0 <= vx < h and 0 <= vy < c:
                w = luoi[vx][vy]
                if kc_a[u] + w < kc_a[(vx, vy)]:
                    kc_a[(vx, vy)] = kc_a[u] + w
                    f_moi = kc_a[(vx, vy)] + manhattan((vx, vy), t)
                    heapq.heappush(pq_a, (f_moi, kc_a[(vx, vy)], (vx, vy)))
                    
    return duyet_d, duyet_a

def bai25_chung_minh() -> str:
    return (
        "Chứng minh tính đúng đắn (Bất biến tham lam):\n"
        "- Bất biến: Khi một đỉnh u được lấy ra khỏi hàng đợi ưu tiên (chốt), khoảng cách d(s, u) của nó đã là ngắn nhất và tối ưu.\n"
        "- Phản chứng: Giả sử tồn tại một đường đi thực sự ngắn hơn tới u, đi qua một đỉnh y chưa được chốt (y nằm trong hàng đợi).\n"
        "- Theo tính chất khoảng cách: d(s, y) <= d(s, y) + w(y, ..., u). Vì w >= 0 (trọng số không âm), ta có d(s, y) <= d(s, u).\n"
        "- Nếu điều kiện trên đúng, thuật toán tham lam của PQ đáng lẽ phải chọn (pop) y trước u. Việc thuật toán chọn u trước chứng tỏ d(s, u) <= d(s, y).\n"
        "- Giao của hai bất đẳng thức cho thấy d(s, u) = d(s, y), nghĩa là đường đi giả định qua y không thể ngắn hơn đường hiện tại của u.\n"
        "- Vai trò trọng số: Chứng minh trên lập tức đổ vỡ nếu có w < 0, vì khi đó d(s, y) + w(y, ..., u) có thể nhỏ hơn d(s, y)."
    )

Noidung = {
    '23': {
        'ten': 'BÀI 23: NHIỀU TRUY VẤN ĐƯỜNG ĐI NGẮN NHẤT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai23_chien_luoc_truy_van(),
        'format': lambda d, kq: kq
    },
    '24': {
        'ten': 'BÀI 24: SO SÁNH HIỆU NĂNG DIJKSTRA VS A* TRÊN LƯỚI',
        'du_lieu': {},
        'mong_doi': None, # Chỉ xuất thông tin so sánh, không fix cứng kết quả
        'ham': lambda d: bai24_astar_vs_dijkstra(),
        'format': lambda d, kq: f"Số đỉnh Dijkstra phải duyệt: {kq[0]}\nSố đỉnh A* phải duyệt: {kq[1]}\n-> A* duyệt ít đỉnh hơn nhờ hàm Heuristic định hướng về phía đích."
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN CỦA DIJKSTRA',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai25_chung_minh(),
        'format': lambda d, kq: kq
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        # Áp dụng logic kiểm tra bao gồm cả khoảng sai số (1e-9) cho float
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
            print(" MENU DIJKSTRA: PHIÊN 4 (BÀI 23 - 25) ")
            print(" CHỌN BÀI (23-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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

def bai23_chien_luoc_truy_van() -> str:
    return (
        "Chiến lược xử lý Q truy vấn (s, t):\n"
        "- Nếu Q nhỏ: Chạy Dijkstra trực tiếp cho mỗi truy vấn. Thời gian: O(Q * (V + E) log V).\n"
        "- Nếu Q lớn và đồ thị thưa: Tiền xử lý bằng cách chạy Dijkstra từ tất cả V đỉnh (All-Pairs Shortest Path), lưu kết quả vào ma trận V x V. Thời gian tiền xử lý: O(V * (V + E) log V). Thời gian truy vấn: O(1).\n"
        "- Nếu Q lớn và đồ thị dày: Cân nhắc dùng thuật toán Floyd-Warshall O(V^3) để tiền xử lý."
    )

def bai24_astar_vs_dijkstra() -> Tuple[int, int]:
    # Tạo một lưới 5x5 có vật cản (chi phí cao = 10) để thấy rõ sự khác biệt
    luoi = [
        [1, 1, 1, 10, 1],
        [1, 10, 1, 10, 1],
        [1, 10, 1, 1, 1],
        [1, 10, 10, 10, 1],
        [1, 1, 1, 1, 1]
    ]
    h, c = 5, 5
    s, t = (0, 0), (4, 4)
    huong = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Tính min_cost để đảm bảo heuristic là admissible
    min_cost = min(luoi[i][j] for i in range(h) for j in range(c))
    
    # --- Chạy Dijkstra ---
    kc_d = {(i, j): float('inf') for i in range(h) for j in range(c)}
    kc_d[s] = luoi[s[0]][s[1]]
    pq_d = [(kc_d[s], s)]
    duyet_d = 0
    
    while pq_d:
        d, u = heapq.heappop(pq_d)
        
        # Kiểm tra stale trước khi đếm
        if d > kc_d[u]: 
            continue
            
        duyet_d += 1
        if u == t: 
            break
        
        for dx, dy in huong:
            vx, vy = u[0] + dx, u[1] + dy
            if 0 <= vx < h and 0 <= vy < c:
                w = luoi[vx][vy]
                if kc_d[u] + w < kc_d[(vx, vy)]:
                    kc_d[(vx, vy)] = kc_d[u] + w
                    heapq.heappush(pq_d, (kc_d[(vx, vy)], (vx, vy)))
                    
    # --- Chạy A* (Heuristic: Manhattan distance * min_cost) ---
    def manhattan(p1, p2):
        return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) * min_cost
        
    kc_a = {(i, j): float('inf') for i in range(h) for j in range(c)}
    kc_a[s] = luoi[s[0]][s[1]]
    pq_a = [(kc_a[s] + manhattan(s, t), kc_a[s], s)]
    duyet_a = 0
    
    while pq_a:
        f, g_val, u = heapq.heappop(pq_a)
        
        # Kiểm tra stale trước khi đếm
        if g_val > kc_a[u]: 
            continue
            
        duyet_a += 1
        if u == t: 
            break
        
        for dx, dy in huong:
            vx, vy = u[0] + dx, u[1] + dy
            if 0 <= vx < h and 0 <= vy < c:
                w = luoi[vx][vy]
                if kc_a[u] + w < kc_a[(vx, vy)]:
                    kc_a[(vx, vy)] = kc_a[u] + w
                    f_moi = kc_a[(vx, vy)] + manhattan((vx, vy), t)
                    heapq.heappush(pq_a, (f_moi, kc_a[(vx, vy)], (vx, vy)))
                    
    return duyet_d, duyet_a

def bai25_chung_minh() -> str:
    return (
        "Chứng minh tính đúng đắn (Bất biến tham lam):\n"
        "- Bất biến: Khi một đỉnh u được lấy ra khỏi hàng đợi ưu tiên (chốt), khoảng cách d(s, u) của nó đã là ngắn nhất và tối ưu.\n"
        "- Phản chứng: Giả sử tồn tại một đường đi thực sự ngắn hơn tới u, đi qua một đỉnh y chưa được chốt (y nằm trong hàng đợi).\n"
        "- Theo tính chất khoảng cách: d(s, y) <= d(s, y) + w(y, ..., u). Vì w >= 0 (trọng số không âm), ta có d(s, y) <= d(s, u).\n"
        "- Nếu điều kiện trên đúng, thuật toán tham lam của PQ đáng lẽ phải chọn (pop) y trước u. Việc thuật toán chọn u trước chứng tỏ d(s, u) <= d(s, y).\n"
        "- Giao của hai bất đẳng thức cho thấy d(s, u) = d(s, y), nghĩa là đường đi giả định qua y không thể ngắn hơn đường hiện tại của u.\n"
        "- Vai trò trọng số: Chứng minh trên lập tức đổ vỡ nếu có w < 0, vì khi đó d(s, y) + w(y, ..., u) có thể nhỏ hơn d(s, y)."
    )

Noidung = {
    '23': {
        'ten': 'BÀI 23: NHIỀU TRUY VẤN ĐƯỜNG ĐI NGẮN NHẤT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai23_chien_luoc_truy_van(),
        'format': lambda d, kq: kq
    },
    '24': {
        'ten': 'BÀI 24: SO SÁNH HIỆU NĂNG DIJKSTRA VS A* TRÊN LƯỚI',
        'du_lieu': {},
        'mong_doi': None, # Chỉ xuất thông tin so sánh, không fix cứng kết quả
        'ham': lambda d: bai24_astar_vs_dijkstra(),
        'format': lambda d, kq: f"Số đỉnh Dijkstra phải duyệt: {kq[0]}\nSố đỉnh A* phải duyệt: {kq[1]}\n-> A* duyệt ít đỉnh hơn nhờ hàm Heuristic định hướng về phía đích."
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN CỦA DIJKSTRA',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai25_chung_minh(),
        'format': lambda d, kq: kq
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        # Áp dụng logic kiểm tra bao gồm cả khoảng sai số (1e-9) cho float
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
            print(" MENU DIJKSTRA: PHIÊN 4 (BÀI 23 - 25) ")
            print(" CHỌN BÀI (23-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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