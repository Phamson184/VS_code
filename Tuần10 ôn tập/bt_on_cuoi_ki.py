import heapq
from collections import deque
from typing import List, Dict, Any, Tuple

# ==========================================
# MÃ NGUỒN: GIẢI ĐỀ ÔN TẬP CUỐI KÌ (7 CÂU)
# ==========================================

# --- Câu 1: Chia mảng (Binary Search trên đáp án) ---
def q1_truck_capacity(du_lieu: Dict[str, Any]) -> Tuple[int, List[List[int]]]:
    W = du_lieu['W']
    K = du_lieu['K']
    
    l, r = max(W), sum(W)
    ans = r
    
    # Binary Search tìm tải trọng
    while l <= r:
        mid = (l + r) // 2
        count, curr = 1, 0
        for w in W:
            if curr + w > mid:
                count += 1
                curr = w
            else:
                curr += w
                
        if count <= K:
            ans = mid
            r = mid - 1 # Thử tìm mức tải trọng nhỏ hơn
        else:
            l = mid + 1 # Tải trọng quá nhỏ, cần tăng lên
            
    # Phân bổ các kiện hàng vào xe theo tải trọng tìm được
    breakdown = []
    curr_truck = []
    curr = 0
    for w in W:
        if curr + w > ans:
            breakdown.append(curr_truck)
            curr_truck = [w]
            curr = w
        else:
            curr_truck.append(w)
            curr += w
    if curr_truck:
        breakdown.append(curr_truck)
        
    return ans, breakdown

# --- Câu 2: Insertion Sort & Số nghịch thế ---
def q2_insertion_sort(du_lieu: Dict[str, Any]) -> Tuple[List[int], int]:
    A = du_lieu['A'][:]
    shifts = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            shifts += 1
            j -= 1
        A[j+1] = key
    return A, shifts

# --- Câu 3: Dijkstra vs Bellman-Ford (Cạnh âm) ---
def q3_dijkstra_negative(du_lieu: Dict[str, Any]) -> Tuple[int, int]:
    graph = du_lieu['graph']
    edges = du_lieu['edges']
    # A = 0, B = 1, C = 2
    
    # 1. Thuật toán Dijkstra (Sẽ bị sai)
    dist_d = {0: 0, 1: float('inf'), 2: float('inf')}
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_d[u]: continue
        for v, w in graph.get(u, []):
            if dist_d[u] + w < dist_d[v]:
                dist_d[v] = dist_d[u] + w
                heapq.heappush(pq, (dist_d[v], v))
                
    # 2. Thuật toán Bellman-Ford (Đúng)
    dist_bf = {0: 0, 1: float('inf'), 2: float('inf')}
    for _ in range(2): # Duyệt V-1 lần (3 đỉnh -> duyệt 2 lần)
        for u, v, w in edges:
            if dist_bf[u] + w < dist_bf[v]:
                dist_bf[v] = dist_bf[u] + w
                
    # Trả về kết quả đi từ A(0) đến B(1) của 2 thuật toán
    return dist_d[1], dist_bf[1]

# --- Câu 4: Ngăn xếp đơn điệu (Daily Temperatures) ---
def q4_daily_temps(du_lieu: Dict[str, Any]) -> List[int]:
    T = du_lieu['T']
    res = [0] * len(T)
    stack = [] # Lưu trữ các CHỈ SỐ của mảng nhiệt độ
    
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx
        stack.append(i)
        
    return res

# --- Câu 5: Hàng đợi hai đầu (Sliding Window Minimum) ---
def q5_sliding_window_min(du_lieu: Dict[str, Any]) -> List[int]:
    A = du_lieu['A']
    k = du_lieu['k']
    dq = deque()
    res = []
    
    for i in range(len(A)):
        # 1. Loại bỏ các chỉ số đã trượt khỏi cửa sổ
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. ĐỂ TÌM MIN: Loại bỏ các phần tử LỚN HƠN A[i] ở đuôi Deque
        while dq and A[dq[-1]] > A[i]:
            dq.pop()
            
        # 3. Thêm chỉ số hiện tại
        dq.append(i)
        
        # 4. Ghi nhận kết quả khi cửa sổ đủ kích thước
        if i >= k - 1:
            res.append(A[dq[0]])
            
    return res

# --- Câu 6: Danh sách liên kết (Toán học Floyd) ---
def q6_floyd_math() -> str:
    return (
        "NGUYÊN LÝ GIAI ĐOẠN 2 - THUẬT TOÁN FLOYD:\n"
        "- Gọi L là khoảng cách từ Head đến đầu chu trình, K là điểm Rùa và Thỏ gặp nhau, C là chu vi.\n"
        "- Khi gặp nhau, Rùa đi được: L + K\n"
        "- Thỏ đi được: L + K + n*C (n là số vòng)\n"
        "- Vì Thỏ nhanh gấp đôi Rùa nên: 2(L + K) = L + K + n*C\n"
        "=> L + K = n*C => L = n*C - K\n"
        "=> L = (n-1)*C + (C - K)\n"
        "*Kết luận:* Quãng đường từ Head đến đầu chu trình (L) đúng bằng đoạn đường từ điểm gặp nhau \n"
        "đi nốt phần còn lại của chu trình (C-K). Do đó, nếu Rùa từ Head, Thỏ từ điểm gặp nhau đi cùng \n"
        "1 vận tốc, chúng sẽ khợp nhau ngay tại đầu chu trình."
    )

# --- Câu 7: Hash Map & Mảng cộng dồn (Subarray Sum) ---
def q7_subarray_sum(du_lieu: Dict[str, Any]) -> int:
    A = du_lieu['A']
    S = du_lieu['S']
    
    prefix_map = {0: 1} # Khởi tạo Map[0] = 1 để đếm mảng con xuất phát từ index 0
    curr_sum = 0
    count = 0
    
    for num in A:
        curr_sum += num
        # Kiểm tra xem có phần tiền tố nào thỏa mãn: Prefix[j] - Prefix[i-1] = S không
        if curr_sum - S in prefix_map:
            count += prefix_map[curr_sum - S]
            
        # Cập nhật tần suất của tiền tố hiện tại vào Map
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        
    return count

# ==========================================
# CẤU HÌNH MENU DATA-DRIVEN
# ==========================================
Noidung = {
    '1': {
        'ten': 'CÂU 1: CHIA MẢNG (TÌM KIẾM NHỊ PHÂN TRÊN ĐÁP ÁN)',
        'du_lieu': {'W': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'K': 5},
        'ham': q1_truck_capacity,
        'format': lambda d, kq: f"Danh sách hàng: {d['W']}\n=> Tải trọng tối thiểu: {kq[0]}\nCách phân xe: {kq[1]}"
    },
    '2': {
        'ten': 'CÂU 2: THUẬT TOÁN SẮP XẾP (INSERTION SORT & SHIFTS)',
        'du_lieu': {'A': [5, 2, 4, 6, 1, 3]},
        'ham': q2_insertion_sort,
        'format': lambda d, kq: f"Mảng gốc: {d['A']}\n=> Đã sắp xếp: {kq[0]}\n=> Tổng số lần dịch chuyển (Bằng số nghịch thế): {kq[1]}"
    },
    '3': {
        'ten': 'CÂU 3: DIJKSTRA VS BELLMAN-FORD (CẠNH ÂM)',
        'du_lieu': {
            'graph': {0: [(1, 2), (2, 5)], 2: [(1, -10)]},
            'edges': [(0, 1, 2), (0, 2, 5), (2, 1, -10)]
        },
        'ham': q3_dijkstra_negative,
        'format': lambda d, kq: f"Tính khoảng cách từ A(0) đến B(1):\n- Thuật toán Dijkstra trả về sai: {kq[0]} (Do bị 'chốt' sớm)\n- Thuật toán Bellman-Ford trả về đúng: {kq[1]}"
    },
    '4': {
        'ten': 'CÂU 4: NGĂN XẾP ĐƠN ĐIỆU (DAILY TEMPERATURES)',
        'du_lieu': {'T': [73, 74, 75, 71, 69, 72, 76, 73]},
        'ham': q4_daily_temps,
        'format': lambda d, kq: f"Nhiệt độ các ngày: {d['T']}\n=> Mảng số ngày phải chờ (Dùng Stack): {kq}"
    },
    '5': {
        'ten': 'CÂU 5: HÀNG ĐỢI HAI ĐẦU (SLIDING WINDOW MINIMUM)',
        'du_lieu': {'A': [4, 2, 12, 11, -5, 8, 1, 5, 6], 'k': 3},
        'ham': q5_sliding_window_min,
        'format': lambda d, kq: f"Mảng gốc: {d['A']} (Cửa sổ K={d['k']})\n=> Giá trị NHỎ NHẤT mỗi cửa sổ (Dùng Deque): {kq}"
    },
    '6': {
        'ten': 'CÂU 6: LÝ THUYẾT LINKED LIST (FLOYD CYCLE)',
        'du_lieu': None,
        'ham': q6_floyd_math,
        'format': lambda kq: kq
    },
    '7': {
        'ten': 'CÂU 7: BẢNG BĂM & MẢNG CỘNG DỒN (SUBARRAY SUM)',
        'du_lieu': {'A': [3, 4, 7, 2, -3, 1, 4, 2], 'S': 7},
        'ham': q7_subarray_sum,
        'format': lambda d, kq: f"Mảng gốc: {d['A']}\n=> Số lượng mảng con có tổng bằng {d['S']} (Tối ưu O(N)): {kq}"
    }
}

# ==========================================
# KHỐI ĐIỀU KHIỂN & MENU TƯƠNG TÁC
# ==========================================
def chay_bai_tu_dong(key_bai: str, tap_du_lieu_noidung: dict):
    if key_bai not in tap_du_lieu_noidung:
        print(f"\n[!] Lỗi: Không tìm thấy bài tập có mã '{key_bai}'.")
        return

    cfg = tap_du_lieu_noidung[key_bai]
    print(f"\n{'='*75}")
    print(f" {cfg['ten']}")
    print(f"{'='*75}")

    try:
        if 'du_lieu' in cfg and cfg['du_lieu'] is not None:
             ket_qua_thuc_te = cfg['ham'](cfg['du_lieu'])
             if callable(cfg.get('format')):
                 print(cfg['format'](cfg['du_lieu'], ket_qua_thuc_te))
             else:
                 print(f"Kết quả: {ket_qua_thuc_te}")
        else:
             ket_qua_thuc_te = cfg['ham']()
             if callable(cfg.get('format')):
                 try:
                     print(cfg['format'](None, ket_qua_thuc_te))
                 except TypeError:
                     print(cfg['format'](ket_qua_thuc_te))
             else:
                 print(f"{ket_qua_thuc_te}")
    except Exception as e:
        print(f"[!] Quá trình chạy bị lỗi: {str(e)}")
        return

if __name__ == '__main__':
    try:
        dict_noidung = locals().get('Noidung')
        if not dict_noidung:
             print("Lỗi: Không tìm thấy từ điển cấu hình bài tập (Noidung).")
             exit()

        danh_sach_keys = sorted(dict_noidung.keys(), key=lambda x: int(x))

        while True:
            print("\n" + "*"*75)
            print(f" MENU CHÍNH - ĐỀ ÔN TẬP CUỐI KÌ (CÁC CÂU: {danh_sach_keys[0]} -> {danh_sach_keys[-1]})")
            print(" NHẬP MÃ CÂU HOẶC '0' ĐỂ THOÁT | 'all' ĐỂ CHẠY TOÀN BỘ")
            print("*"*75)
            
            for k in danh_sach_keys:
                print(f" {k:>3}. {dict_noidung[k]['ten']}")
                
            chon = input("\nLựa chọn của bạn: ").strip()
            
            if chon == '0':
                print("Chương trình kết thúc. Chúc bạn thi tốt!")
                break
            elif chon.lower() == 'all':
                for k in danh_sach_keys:
                    chay_bai_tu_dong(k, dict_noidung)
            elif chon in dict_noidung:
                chay_bai_tu_dong(chon, dict_noidung)
            else:
                print("\n[!] Lựa chọn không hợp lệ, vui lòng nhập chính xác mã câu!")
    except KeyboardInterrupt:
        print("\nChương trình bị ngắt bởi người dùng.")