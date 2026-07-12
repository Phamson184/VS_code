from typing import List, Tuple, Any, Dict
import random

# ==========================================
# MODULE 3: INSERTION SORT - BIẾN THỂ & PHÂN TÍCH (BÀI 18 -> 25)
# ==========================================

def bai18_so_sanh_chieu_do(a: List[int]) -> Dict[str, Any]:
    n = len(a)
    # 1. Dò từ Phải sang Trái (Chuẩn)
    b_right = a[:]
    comp_right = 0
    for i in range(1, n):
        key = b_right[i]
        j = i - 1
        while j >= 0:
            comp_right += 1
            if b_right[j] > key:
                b_right[j + 1] = b_right[j]
                j -= 1
            else:
                break
        b_right[j + 1] = key
        
    # 2. Dò từ Trái sang Phải
    b_left = a[:]
    comp_left = 0
    for i in range(1, n):
        key = b_left[i]
        pos = i
        # Tìm vị trí từ trái sang phải
        for j in range(i):
            comp_left += 1
            if b_left[j] > key:
                pos = j
                break
        # Dịch chuyển mảng
        j = i - 1
        while j >= pos:
            b_left[j + 1] = b_left[j]
            j -= 1
        b_left[pos] = key
        
    return {
        'comp_right': comp_right,
        'comp_left': comp_left
    }

def bai19_gnome_sort(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    pos = 0
    ops = 0 # Đếm số thao tác lùi/tiến
    
    while pos < n:
        ops += 1
        if pos == 0 or b[pos] >= b[pos - 1]:
            pos += 1
        else:
            # Swap và lùi lại
            b[pos], b[pos - 1] = b[pos - 1], b[pos]
            pos -= 1
            
    return b, ops

def bai20_shell_sort(a: List[int], gaps: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    shifts = 0
    
    for gap in gaps:
        for i in range(gap, n):
            temp = b[i]
            j = i
            while j >= gap and b[j - gap] > temp:
                b[j] = b[j - gap]
                shifts += 1
                j -= gap
            b[j] = temp
            
    return b, shifts

def bai21_dem_shift_merge_sort(a: List[int]) -> int:
    def merge_and_count(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        return inv_count

    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)
        return inv_count

    b = a[:]
    temp = [0] * len(b)
    return merge_sort_and_count(b, temp, 0, len(b) - 1)

def bai22_do_lech_k(a: List[int], k: int) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            shifts += 1
            j -= 1
        b[j + 1] = key
    return b, shifts

def bai23_phan_tich_cases(n: int) -> Dict[str, Tuple[int, int]]:
    def count_ops(arr):
        b = arr[:]
        l = len(b)
        ss = 0
        sw = 0
        for i in range(1, l):
            key = b[i]
            j = i - 1
            while j >= 0:
                ss += 1
                if b[j] > key:
                    b[j + 1] = b[j]
                    sw += 1
                    j -= 1
                else:
                    break
            b[j + 1] = key
        return ss, sw
        
    best = list(range(n))
    worst = list(range(n, 0, -1))
    avg = list(range(n))
    random.seed(42)
    random.shuffle(avg)
    
    return {
        'best': count_ops(best),
        'avg': count_ops(avg),
        'worst': count_ops(worst)
    }

def bai24_so_sanh_3_thuat_toan(a: List[int]) -> Dict[str, Tuple[int, int]]:
    def ins(arr):
        b = arr[:]
        ss, sh = 0, 0
        for i in range(1, len(b)):
            key = b[i]
            j = i - 1
            while j >= 0:
                ss += 1
                if b[j] > key:
                    b[j + 1] = b[j]
                    sh += 1
                    j -= 1
                else:
                    break
            b[j + 1] = key
        return ss, sh
    
    def bub(arr):
        b = arr[:]
        ss, sw = 0, 0
        n = len(b)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                ss += 1
                if b[j] > b[j + 1]:
                    b[j], b[j + 1] = b[j + 1], b[j]
                    sw += 1
        return ss, sw
    
    def sel(arr):
        b = arr[:]
        ss, sw = 0, 0
        n = len(b)
        for i in range(n - 1):
            vt_min = i
            for j in range(i + 1, n):
                ss += 1
                if b[j] < b[vt_min]:
                    vt_min = j
            if vt_min != i:
                b[i], b[vt_min] = b[vt_min], b[i]
                sw += 1
        return ss, sw

    return {'insertion': ins(a), 'bubble': bub(a), 'selection': sel(a)}

def bai25_loop_invariant() -> str:
    return (
        "Bất biến vòng lặp (Loop Invariant) của Insertion Sort:\n"
        "- Bất biến: Trước khi bắt đầu vòng lặp ngoài lần thứ i, mảng con a[0..i-1] luôn chứa các phần tử ban đầu của đoạn này nhưng đã được sắp xếp tăng dần.\n"
        "- Khởi tạo (i=1): Mảng con a[0..0] chỉ có 1 phần tử nên luôn coi là đã được sắp xếp. Đúng.\n"
        "- Duy trì: Tại vòng lặp i, phần tử a[i] được chèn vào vị trí đúng trong mảng con a[0..i-1]. Kết thúc vòng lặp, đoạn a[0..i] chứa các phần tử ban đầu nhưng đã sắp xếp.\n"
        "- Kết thúc: Khi vòng lặp chạy đến i=n, đoạn a[0..n-1] đã sắp xếp. Đây chính là toàn bộ mảng. Suy ra thuật toán đúng đắn."
    )

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '18': {
        'ten': 'BÀI 18: CHÈN TỪ CUỐI HAY ĐẦU?',
        'du_lieu': {'a': [1, 2, 4, 3, 5]},
        'mong_doi': 'So sánh hiệu năng',
        'ham': lambda d: bai18_so_sanh_chieu_do(d['a']),
        'format': lambda d, kq: (
            f"Mảng gần sắp xếp: {d['a']}\n"
            f"- Số phép so sánh khi dò từ Phải sang Trái (Chuẩn): {kq['comp_right']}\n"
            f"- Số phép so sánh khi dò từ Trái sang Phải: {kq['comp_left']}\n"
            f"[*] Kết luận: Dò từ phải sang cực kỳ hiệu quả với mảng gần sắp xếp vì nó gặp phần tử nhỏ hơn và DỪNG NGAY LẬP TỨC."
        )
    },
    '19': {
        'ten': 'BÀI 19: GNOME SORT (BIẾN THỂ CỦA INSERTION)',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 6),
        'ham': lambda d: bai19_gnome_sort(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"=> Sau sắp xếp (Gnome Sort): {kq[0]}\n"
            f"Số thao tác tiến/lùi con trỏ: {kq[1]}\n"
            f"[*] Gnome sort chỉ dùng 1 vòng lặp while duy nhất thay vì lồng nhau."
        )
    },
    '20': {
        'ten': 'BÀI 20: SHELL SORT (TỔNG QUÁT HÓA INSERTION)',
        'du_lieu': {'a': [8, 7, 6, 5, 4, 3, 2, 1], 'gaps': [4, 2, 1]},
        'mong_doi': ([1, 2, 3, 4, 5, 6, 7, 8], 12),
        'ham': lambda d: bai20_shell_sort(d['a'], d['gaps']),
        'format': lambda d, kq: (
            f"Mảng gốc kích thước 8: {d['a']}\n"
            f"Dãy Gap sử dụng: {d['gaps']}\n"
            f"=> Kết quả: {kq[0]}\n"
            f"Số phép Shift: {kq[1]} (So với ~28 shift nếu dùng Insertion chuẩn)"
        )
    },
    '21': {
        'ten': 'BÀI 21: ĐẾM SHIFT CHO MẢNG LỚN BẰNG O(n log n)',
        'du_lieu': {'a': [2, 4, 1, 3]},
        'mong_doi': 3,
        'ham': lambda d: bai21_dem_shift_merge_sort(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc mô phỏng: {d['a']}\n"
            f"Thuật toán: Merge Sort Counting Inversions\n"
            f"=> Tổng số nghịch thế (bằng tổng shift): {kq}"
        )
    },
    '22': {
        'ten': 'BÀI 22: MẢNG ĐỘ LỆCH TỐI ĐA <= k',
        'du_lieu': {'a': [2, 1, 4, 3, 6, 5], 'k': 1},
        'mong_doi': ([1, 2, 3, 4, 5, 6], 3),
        'ham': lambda d: bai22_do_lech_k(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']} (Mỗi phần tử cách vị trí đúng <= {d['k']})\n"
            f"=> Số shift thực tế: {kq[1]}\n"
            f"[*] Vì mỗi phần tử lùi tối đa k bước, độ phức tạp bị chặn ở ngưỡng O(n * k)."
        )
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH BEST / AVERAGE / WORST CASE',
        'du_lieu': {'n': 5},
        'mong_doi': 'In thống kê',
        'ham': lambda d: bai23_phan_tich_cases(d['n']),
        'format': lambda d, kq: (
            f"Kích thước giả lập N = {d['n']}\n"
            f"- Best Case (Đã sắp xếp)  : So sánh = {kq['best'][0]}, Shift = {kq['best'][1]}\n"
            f"- Average Case (Ngẫu nhiên): So sánh = {kq['avg'][0]}, Shift = {kq['avg'][1]}\n"
            f"- Worst Case (Ngược hoàn toàn): So sánh = {kq['worst'][0]}, Shift = {kq['worst'][1]}\n"
            f"[*] Khớp với lý thuyết: Best O(n), Average & Worst O(n^2)."
        )
    },
    '24': {
        'ten': 'BÀI 24: SO SÁNH 3 THUẬT TOÁN O(n^2)',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': 'In thống kê',
        'ham': lambda d: bai24_so_sanh_3_thuat_toan(d['a']),
        'format': lambda d, kq: (
            f"Dữ liệu tồi tệ nhất (Worst Case): {d['a']}\n"
            f"- Insertion Sort: So sánh = {kq['insertion'][0]}, Shift/Swap = {kq['insertion'][1]}\n"
            f"- Bubble Sort   : So sánh = {kq['bubble'][0]}, Swap = {kq['bubble'][1]}\n"
            f"- Selection Sort: So sánh = {kq['selection'][0]}, Swap = {kq['selection'][1]}\n"
            f"[*] Tùy đặc tính dữ liệu (Đã sắp xếp 1 phần, Chi phí swap đắt...) để chọn thuật toán phù hợp."
        )
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN (LOOP INVARIANT)',
        'du_lieu': {},
        'mong_doi': 'In lý thuyết',
        'ham': lambda d: bai25_loop_invariant(),
        'format': lambda d, kq: kq
    }
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] not in ['So sánh hiệu năng', 'In thống kê', 'In lý thuyết']:
        if isinstance(cfg['mong_doi'], list) and len(cfg['mong_doi']) > 0 and isinstance(cfg['mong_doi'][0], list):
            print("\nKết quả mong đợi:\n  " + "\n  ".join(f"Trạng thái {idx + 1}: {v}" for idx, v in enumerate(cfg['mong_doi'])))
        else:
            print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
            
        if kq == cfg['mong_doi']:
            print("\nTrạng thái: THÀNH CÔNG")
        else:
            print("\nTrạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*70)
            print(" MENU INSERTION SORT: PHIÊN 3 (BÀI 18 -> 25) ")
            print(" CHỌN BÀI (18-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*70)
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
