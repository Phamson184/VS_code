from typing import List, Dict, Any
from collections import deque
import heapq

# ==========================================
# MODULE B2 & B3: HÀNG ĐỢI (QUEUE) - BÀI 8 ĐẾN BÀI 15
# ==========================================

# --- Bài 8: Hàng đợi hai đầu (Deque) ---
def bai_8_deque(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    dq = deque()
    log = []
    for lenh in du_lieu['lenh']:
        parts = lenh.split()
        cmd = parts[0]
        if cmd == 'pushFront': dq.appendleft(int(parts[1]))
        elif cmd == 'pushBack': dq.append(int(parts[1]))
        elif cmd == 'popFront': log.append(dq.popleft())
        elif cmd == 'popBack': log.append(dq.pop())
        
    return {'log_pop': log, 'deque_cuoi': list(dq)}

# --- Bài 9: BFS dùng hàng đợi ---
def bai_9_bfs(du_lieu: Dict[str, Any]) -> List[str]:
    graph = du_lieu['do_thi']
    start = du_lieu['dinh_bat_dau']
    q = deque([start])
    visited = {start}
    thu_tu_duyet = []
    
    while q:
        u = q.popleft()
        thu_tu_duyet.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
                
    return thu_tu_duyet

# --- Bài 10: Hàng đợi ưu tiên cơ bản (Dùng Heap) ---
def bai_10_priority_queue(du_lieu: Dict[str, Any]) -> List[int]:
    pq = []
    log_pop = []
    for lenh in du_lieu['lenh']:
        parts = lenh.split()
        if parts[0] == 'push':
            heapq.heappush(pq, int(parts[1])) # Min-Heap
        elif parts[0] == 'pop':
            log_pop.append(heapq.heappop(pq))
            
    return log_pop

# --- Bài 11: Giá trị lớn nhất trong cửa sổ trượt (Monotonic Deque) ---
def bai_11_sliding_window_max(du_lieu: Dict[str, Any]) -> List[int]:
    a = du_lieu['mang']
    k = du_lieu['k']
    dq = deque() # Lưu CHỈ SỐ, duy trì giá trị tương ứng giảm dần
    res = []
    
    for i in range(len(a)):
        # 1. Loại bỏ các chỉ số đã trượt khỏi cửa sổ kích thước k
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. Loại bỏ các phần tử nhỏ hơn phần tử hiện tại (vì chúng không thể làm Max được nữa)
        while dq and a[dq[-1]] < a[i]:
            dq.pop()
            
        # 3. Thêm chỉ số hiện tại
        dq.append(i)
        
        # 4. Khi cửa sổ đã đủ kích thước k, ghi nhận kết quả ở đầu Deque
        if i >= k - 1:
            res.append(a[dq[0]])
            
    return res

# --- Bài 12: Bài toán Josephus ---
def bai_12_josephus(du_lieu: Dict[str, Any]) -> int:
    n = du_lieu['n']
    k = du_lieu['k']
    q = deque(range(1, n + 1))
    
    while len(q) > 1:
        # Chuyển k-1 người ra sau hàng
        for _ in range(k - 1):
            q.append(q.popleft())
        # Loại người thứ k
        q.popleft()
        
    return q[0] # Người sống sót

# --- Bài 13: Phân tích Amortized O(1) ---
def bai_13_amortized_analysis() -> str:
    return (
        "PHÂN TÍCH KẾ TOÁN (ACCOUNTING METHOD):\n"
        "- Khi cài đặt Queue bằng 2 Stack (in_stack và out_stack).\n"
        "- Lệnh push (enqueue): Nạp vào in_stack tốn O(1).\n"
        "- Lệnh pop (dequeue): Nếu out_stack rỗng, ta trút toàn bộ in_stack sang out_stack.\n"
        "- Trông có vẻ tốn O(n), nhưng thực tế MỖI PHẦN TỬ chỉ bị di chuyển sang out_stack ĐÚNG 1 LẦN trong suốt vòng đời của nó.\n"
        "- Suy ra, tổng chi phí cho n phần tử là O(n). Chi phí trung bình (Amortized) cho mỗi thao tác là O(n) / n = O(1)."
    )

# --- Bài 14: Đếm Hit trong cửa sổ thời gian T ---
def bai_14_hit_counter(du_lieu: Dict[str, Any]) -> List[int]:
    q = deque()
    T = du_lieu['T'] # Cửa sổ thời gian (giây)
    log_hits = []
    
    for timestamp in du_lieu['su_kien']:
        # 1. Nhận sự kiện mới
        q.append(timestamp)
        # 2. Loại bỏ các sự kiện đã quá hạn (> T giây so với hiện tại)
        while q and q[0] <= timestamp - T:
            q.popleft()
        # 3. Ghi nhận số lượng Hit còn lại trong cửa sổ
        log_hits.append(len(q))
        
    return log_hits

# --- Bài 15: Lập lịch xoay vòng (Round-Robin) ---
def bai_15_round_robin(du_lieu: Dict[str, Any]) -> Dict[str, int]:
    # Mỗi tiến trình: [Tên_Tiến_Trình, Thời_Gian_Cần_Chạy (Burst Time)]
    q = deque(du_lieu['tien_trinh'])
    quantum = du_lieu['quantum']
    thoi_gian_hien_tai = 0
    thoi_diem_hoan_thanh = {}
    
    while q:
        ten, burst = q.popleft()
        if burst > quantum:
            thoi_gian_hien_tai += quantum
            q.append([ten, burst - quantum]) # Chưa xong, đẩy lại vào cuối hàng đợi
        else:
            thoi_gian_hien_tai += burst
            thoi_diem_hoan_thanh[ten] = thoi_gian_hien_tai # Đã xong, ghi nhận
            
    return thoi_diem_hoan_thanh


# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '8': {
        'ten': 'BÀI 8: HÀNG ĐỢI HAI ĐẦU (DEQUE)',
        'du_lieu': {'lenh': ['pushFront 1', 'pushBack 2', 'pushFront 3', 'popBack', 'popFront']},
        'mong_doi': {'log_pop': [2, 3], 'deque_cuoi': [1]},
        'ham': lambda d: bai_8_deque(d),
        'format': lambda d, kq: (
            f"Các lệnh: {d['lenh']}\n"
            f"- Đã lấy ra: {kq['log_pop']}\n"
            f"- Deque còn lại: {kq['deque_cuoi']}"
        )
    },
    '9': {
        'ten': 'BÀI 9: DUYỆT ĐỒ THỊ BẰNG QUEUE (BFS)',
        'du_lieu': {
            'do_thi': {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []},
            'dinh_bat_dau': 'A'
        },
        'mong_doi': ['A', 'B', 'C', 'D', 'E', 'F'],
        'ham': lambda d: bai_9_bfs(d),
        'format': lambda d, kq: (
            f"Đồ thị: {d['do_thi']}\n"
            f"=> Trình tự duyệt theo chiều rộng (BFS): {kq}\n"
            f"[*] Queue giúp duyệt lan tỏa theo từng tầng (Level) một cách tự nhiên."
        )
    },
    '10': {
        'ten': 'BÀI 10: HÀNG ĐỢI ƯU TIÊN (PRIORITY QUEUE)',
        'du_lieu': {'lenh': ['push 5', 'push 1', 'push 3', 'pop', 'pop', 'push 2', 'pop']},
        'mong_doi': [1, 3, 2],
        'ham': lambda d: bai_10_priority_queue(d),
        'format': lambda d, kq: (
            f"Lệnh nạp/rút: {d['lenh']}\n"
            f"=> Kết quả lấy ra: {kq}\n"
            f"[*] Khác với FIFO, Priority Queue luôn trả về phần tử có độ ưu tiên cao nhất (nhỏ nhất) mỗi khi pop."
        )
    },
    '11': {
        'ten': 'BÀI 11: MAX TRONG CỬA SỔ TRƯỢT (O(n))',
        'du_lieu': {'mang': [1, 3, -1, -3, 5, 3], 'k': 3},
        'mong_doi': [3, 3, 5, 5],
        'ham': lambda d: bai_11_sliding_window_max(d),
        'format': lambda d, kq: (
            f"Mảng: {d['mang']} | Kích thước cửa sổ k = {d['k']}\n"
            f"=> Giá trị lớn nhất mỗi cửa sổ: {kq}\n"
            f"[*] Bằng Deque đơn điệu giảm, ta loại bỏ ngay các số nhỏ vô dụng, duy trì độ phức tạp O(n)."
        )
    },
    '12': {
        'ten': 'BÀI 12: BÀI TOÁN JOSEPHUS',
        'du_lieu': {'n': 5, 'k': 2},
        'mong_doi': 3,
        'ham': lambda d: bai_12_josephus(d),
        'format': lambda d, kq: (
            f"Có {d['n']} người, đếm tới {d['k']} thì loại.\n"
            f"=> Người sống sót cuối cùng là số: {kq}"
        )
    },
    '13': {
        'ten': 'BÀI 13: PHÂN TÍCH AMORTIZED O(1)',
        'du_lieu': {},
        'mong_doi': 'In lý thuyết',
        'ham': lambda d: bai_13_amortized_analysis(),
        'format': lambda d, kq: kq
    },
    '14': {
        'ten': 'BÀI 14: HỆ THỐNG ĐẾM HIT TRONG T GIÂY',
        'du_lieu': {
            'T': 300, # Giâ
            'su_kien': [10, 50, 200, 310, 400, 600, 610, 620]
        },
        'mong_doi': [1, 2, 3, 3, 3, 3, 3, 4],
        'ham': lambda d: bai_14_hit_counter(d),
        'format': lambda d, kq: (
            f"Cửa sổ thời gian T = {d['T']} giây.\n"
            f"Luồng sự kiện (Timestamps): {d['su_kien']}\n"
            f"=> Số Hit hợp lệ tại từng thời điểm: {kq}\n"
            f"[*] Queue tự động vứt bỏ các timestamp quá hạn ở phía trước (Front)."
        )
    },
    '15': {
        'ten': 'BÀI 15: LẬP LỊCH CPU ROUND-ROBIN',
        'du_lieu': {
            'quantum': 2,
            'tien_trinh': [['P1', 3], ['P2', 1], ['P3', 4]] # [Tên, Burst_Time]
        },
        'mong_doi': {'P2': 3, 'P1': 6, 'P3': 8},
        'ham': lambda d: bai_15_round_robin(d),
        'format': lambda d, kq: (
            f"Danh sách tiến trình: {d['tien_trinh']} | Lượng thời gian Quantum = {d['quantum']}\n"
            f"=> Thời điểm hoàn thành của từng tiến trình:\n" +
            "\n".join([f"   - {ten}: {thoi_gian}" for ten, thoi_gian in kq.items()]) +
            f"\n[*] Tiến trình chưa xong bị đẩy về cuối hàng đợi, đảm bảo công bằng cho mọi tiến trình."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] != 'In lý thuyết':
        print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 4 (QUEUE - BÀI 8 -> BÀI 15)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            # Ép kiểu int để sort đúng từ 8 đến 15
            for k, v in sorted(Noidung.items(), key=lambda item: int(item[0])):
                print(f" {k:>2}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in sorted(Noidung.keys(), key=int):
                    chay_bai(Noidung[k])
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
        pass