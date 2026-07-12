from typing import List, Tuple, Any, Dict
import random

# ==========================================
# MODULE 1 - NHÓM 2: SẮP XẾP & PHÂN TÍCH (CÂU 7 - 14)
# ==========================================

def bai7_bubble_sort_swap(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                swaps += 1
    return b, swaps

def bai8_bubble_sort_toi_uu(a: List[int]) -> int:
    b = a[:]
    n = len(b)
    passes = 0
    for i in range(n - 1):
        passes += 1
        swapped = False
        for j in range(n - 1 - i):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                swapped = True
        if not swapped: break
    return passes

def bai9_insertion_sort_shift(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j+1] = b[j]
            shifts += 1
            j -= 1
        b[j+1] = key
    return b, shifts

def bai10_binary_insertion_sort(a: List[int]) -> Tuple[List[int], int, int]:
    b = a[:]
    n = len(b)
    comps, shifts = 0, 0
    for i in range(1, n):
        key = b[i]
        l, r = 0, i - 1
        while l <= r:
            comps += 1
            mid = (l + r) // 2
            if b[mid] < key: l = mid + 1
            else: r = mid - 1
        # Chèn
        pos = l
        for j in range(i - 1, pos - 1, -1):
            b[j+1] = b[j]
            shifts += 1
        b[pos] = key
    return b, comps, shifts

def bai11_selection_sort_compare(a: List[int]) -> int:
    b = a[:]
    n = len(b)
    comps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if b[j] < b[min_idx]: min_idx = j
        b[i], b[min_idx] = b[min_idx], b[i]
    return comps

def bai13_merge_sort_inversions(a: List[int]) -> int:
    def merge_count(arr, temp, l, r):
        if l >= r: return 0
        mid = (l + r) // 2
        count = merge_count(arr, temp, l, mid) + merge_count(arr, temp, mid + 1, r)
        # Trộn
        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if arr[i] <= arr[j]: temp[k] = arr[i]; i += 1
            else: temp[k] = arr[j]; j += 1; count += (mid - i + 1)
            k += 1
        while i <= mid: temp[k] = arr[i]; i += 1; k += 1
        while j <= r: temp[k] = arr[j]; j += 1; k += 1
        arr[l:r+1] = temp[l:r+1]
        return count
    return merge_count(a[:], [0]*len(a), 0, len(a)-1)

def bai14_shell_sort(a: List[int], gaps: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    shifts = 0
    for gap in gaps:
        for i in range(gap, n):
            temp = b[i]
            j = i
            while j >= gap and b[j-gap] > temp:
                b[j] = b[j-gap]
                shifts += 1
                j -= gap
            b[j] = temp
    return b, shifts

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '7': {'ten': 'CÂU 7: BUBBLE SORT & SWAP (NGHỊCH THẾ)', 'du_lieu': {'a': [2, 3, 1]}, 'mong_doi': ([1, 2, 3], 2), 'ham': lambda d: bai7_bubble_sort_swap(d['a']), 'format': lambda d, kq: f"Mảng {d['a']} -> {kq[0]}. Số swap: {kq[1]}"},
    '8': {'ten': 'CÂU 8: BUBBLE SORT TỐI ƯU (EARLY-EXIT)', 'du_lieu': {'a': [1, 2, 3, 4]}, 'mong_doi': 1, 'ham': lambda d: bai8_bubble_sort_toi_uu(d['a']), 'format': lambda d, kq: f"Mảng {d['a']} -> Dừng sau {kq} lượt duyệt."},
    '9': {'ten': 'CÂU 9: INSERTION SORT & SHIFT', 'du_lieu': {'a': [3, 2, 1]}, 'mong_doi': ([1, 2, 3], 3), 'ham': lambda d: bai9_insertion_sort_shift(d['a']), 'format': lambda d, kq: f"Mảng {d['a']} -> {kq[0]}. Số shift: {kq[1]}"},
    '10': {'ten': 'CÂU 10: BINARY INSERTION SORT', 'du_lieu': {'a': [3, 2, 1]}, 'mong_doi': ([1, 2, 3], 3, 3), 'ham': lambda d: bai10_binary_insertion_sort(d['a']), 'format': lambda d, kq: f"Mảng {d['a']} -> So sánh: {kq[1]}, Shift: {kq[2]}"},
    '11': {'ten': 'CÂU 11: SELECTION SORT (LUÔN O(n^2))', 'du_lieu': {'a': [1, 2, 3, 4, 5]}, 'mong_doi': 10, 'ham': lambda d: bai11_selection_sort_compare(d['a']), 'format': lambda d, kq: f"Mảng size {len(d['a'])} -> Phép so sánh: {kq} (Công thức: {len(d['a'])*(len(d['a'])-1)//2})"},
    '13': {'ten': 'CÂU 13: ĐẾM NGHỊCH THẾ O(n log n)', 'du_lieu': {'a': [2, 4, 1, 3]}, 'mong_doi': 3, 'ham': lambda d: bai13_merge_sort_inversions(d['a']), 'format': lambda d, kq: f"Mảng {d['a']} -> Số nghịch thế: {kq}"},
    '14': {'ten': 'CÂU 14: SHELL SORT', 'du_lieu': {'a': [8, 7, 6, 5, 4, 3, 2, 1], 'gaps': [4, 2, 1]}, 'mong_doi': ([1, 2, 3, 4, 5, 6, 7, 8], 12), 'ham': lambda d: bai14_shell_sort(d['a'], d['gaps']), 'format': lambda d, kq: f"Mảng {d['a']} -> {kq[0]}. Số shift: {kq[1]}"}
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    if kq == cfg['mong_doi'] or (isinstance(kq, tuple) and kq[0] == cfg['mong_doi'][0]):
        print("\nTrạng thái: THÀNH CÔNG")
    else: print(f"\nTrạng thái: THẤT BẠI (Mong đợi: {cfg['mong_doi']})")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*70 + "\n MENU: PHIÊN 1 - NHÓM 2 (CÂU 7-14) \n" + "*"*70)
            for k, v in sorted(Noidung.items(), key=lambda item: int(item[0])): print(f" {k:>2}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            if chon == '0': break
            elif chon in Noidung: chay_bai(Noidung[chon])
            else: print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt: pass