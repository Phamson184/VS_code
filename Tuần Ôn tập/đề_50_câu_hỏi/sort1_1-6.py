from typing import List, Dict, Any, Tuple
import math

# ==========================================
# MODULE 1: TÌM KIẾM NHỊ PHÂN & SẮP XẾP CƠ BẢN (CÂU 1 - 14)
# ==========================================

# --- CÁC HÀM LOGIC THUẬT TOÁN ---

def bai1_tim_kiem_nhi_phan(arr: List[int], x: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x: return mid
        elif arr[mid] < x: left = mid + 1
        else: right = mid - 1
    return -1

def bai2_first_last_pos(arr: List[int], x: int) -> Tuple[int, int]:
    def find_bound(is_first):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                res = mid
                if is_first: right = mid - 1
                else: left = mid + 1
            elif arr[mid] < x: left = mid + 1
            else: right = mid - 1
        return res
    return (find_bound(True), find_bound(False))

def bai3_lower_upper_bound(arr: List[int], x: int) -> Tuple[int, int]:
    # Lower: nhỏ nhất >= x
    lb, rb = 0, len(arr) - 1
    lower, upper = len(arr), len(arr)
    
    # Lower bound
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= x: lower = mid; r = mid - 1
        else: l = mid + 1
            
    # Upper bound
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x: upper = mid; r = mid - 1
        else: l = mid + 1
    return lower, upper

def bai4_tim_trong_mang_xoay(arr: List[int], x: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x: return mid
        if arr[l] <= arr[mid]: # Nửa trái sắp xếp
            if arr[l] <= x < arr[mid]: r = mid - 1
            else: l = mid + 1
        else: # Nửa phải sắp xếp
            if arr[mid] < x <= arr[r]: l = mid + 1
            else: r = mid - 1
    return -1

def bai5_koko_an_chuoi(piles: List[int], h: int) -> int:
    def can_eat(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h
    l, r = 1, max(piles)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if can_eat(mid): ans = mid; r = mid - 1
        else: l = mid + 1
    return ans

def bai6_chia_mang(a: List[int], k: int) -> int:
    def check(max_sum):
        count, curr = 1, 0
        for x in a:
            if curr + x > max_sum: count += 1; curr = x
            else: curr += x
        return count <= k
    l, r = max(a), sum(a)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if check(mid): ans = mid; r = mid - 1
        else: l = mid + 1
    return ans

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '1': {
        'ten': 'CÂU 1: TÌM KIẾM NHỊ PHÂN CƠ BẢN',
        'du_lieu': {'a': [1, 3, 5, 7, 9], 'x': 7},
        'mong_doi': 3,
        'ham': lambda d: bai1_tim_kiem_nhi_phan(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng {d['a']}, Tìm {d['x']} => Vị trí: {kq}"
    },
    '2': {
        'ten': 'CÂU 2: TÌM VỊ TRÍ ĐẦU/CUỐI (DỮ LIỆU TRÙNG)',
        'du_lieu': {'a': [1, 2, 2, 2, 3], 'x': 2},
        'mong_doi': (1, 3), # (đầu, cuối)
        'ham': lambda d: bai2_first_last_pos(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng {d['a']}, Số {d['x']} xuất hiện từ {kq[0]} đến {kq[1]}, số lần: {kq[1]-kq[0]+1}"
    },
    '3': {
        'ten': 'CÂU 3: LOWER/UPPER BOUND',
        'du_lieu': {'a': [1, 3, 5, 7], 'x': 4},
        'mong_doi': (2, 2), # Index 2 (giá trị 5) cho cả hai vì 5 >= 4 và 5 > 4
        'ham': lambda d: bai3_lower_upper_bound(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng {d['a']}, X={d['x']} => LowerBound: {kq[0]}, UpperBound: {kq[1]}"
    },
    '4': {
        'ten': 'CÂU 4: TÌM TRONG MẢNG XOAY',
        'du_lieu': {'a': [4, 5, 6, 7, 0, 1, 2], 'x': 0},
        'mong_doi': 4,
        'ham': lambda d: bai4_tim_trong_mang_xoay(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng xoay {d['a']}, Tìm {d['x']} => Vị trí: {kq}"
    },
    '5': {
        'ten': 'CÂU 5: KOKO ĂN CHUỐI (BS TRÊN ĐÁP ÁN)',
        'du_lieu': {'piles': [3, 6, 7, 11], 'h': 8},
        'mong_doi': 4,
        'ham': lambda d: bai5_koko_an_chuoi(d['piles'], d['h']),
        'format': lambda d, kq: f"Đống {d['piles']}, Giới hạn {d['h']} giờ => Tốc độ ăn tối thiểu: {kq}"
    },
    '6': {
        'ten': 'CÂU 6: CHIA MẢNG TỔNG LỚN NHẤT NHỎ NHẤT',
        'du_lieu': {'a': [7, 2, 5, 10, 8], 'k': 2},
        'mong_doi': 18,
        'ham': lambda d: bai6_chia_mang(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng {d['a']}, Chia {d['k']} đoạn => Tổng lớn nhất của đoạn nhỏ nhất: {kq}"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    if kq == cfg['mong_doi']: print("\nTrạng thái: THÀNH CÔNG")
    else: print(f"\nTrạng thái: THẤT BẠI (Mong đợi: {cfg['mong_doi']})")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*70)
            print(" MENU: PHIÊN 1 (TÌM KIẾM NHỊ PHÂN - CÂU 1-6) ")
            print(" CHỌN CÂU (1-6) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass