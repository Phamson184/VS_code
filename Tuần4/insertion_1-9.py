from typing import List, Tuple, Any, Dict

def bai1_chen_mot_phan_tu(a: List[int], x: int) -> List[int]:
    b = a[:]
    b.append(x)
    j = len(b) - 2
    # Tìm vị trí từ phải sang trái và dịch chuyển
    while j >= 0 and b[j] > x:
        b[j + 1] = b[j]
        j -= 1
    b[j + 1] = x
    return b

def bai2_tang_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai3_giam_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        # Thay đổi dấu so sánh để sắp xếp giảm dần
        while j >= 0 and b[j] < key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai4_trang_thai_moi_vong(a: List[int]) -> List[List[int]]:
    b = a[:]
    n = len(b)
    trang_thai = []
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
        # Lưu lại bản sao của mảng sau mỗi vòng lặp ngoài
        trang_thai.append(b[:])
    return trang_thai

def bai5_dem_shift(a: List[int]) -> Tuple[List[int], int]:
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

def bai6_dem_so_sanh(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_sanh = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0:
            so_sanh += 1 # Đếm cả những lần so sánh thất bại (break)
            if b[j] > key:
                b[j + 1] = b[j]
                j -= 1
            else:
                break
        b[j + 1] = key
    return b, so_sanh

def bai7_sap_xep_ky_tu(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai8_trang_thai_k_buoc(a: List[int], k: int) -> List[int]:
    b = a[:]
    n = len(b)
    so_vong = min(k, n - 1)
    for i in range(1, so_vong + 1):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai9_binary_insertion_sort(a: List[int]) -> Dict[str, Any]:
    # Thuật toán gốc để so sánh
    _, standard_comps = bai6_dem_so_sanh(a)
    _, standard_shifts = bai5_dem_shift(a)
    
    b = a[:]
    n = len(b)
    binary_comps = 0
    binary_shifts = 0
    
    for i in range(1, n):
        key = b[i]
        # Tìm kiếm nhị phân thủ công để đếm số phép so sánh
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            binary_comps += 1
            if b[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        # left chính là vị trí cần chèn
        pos = left
        # Thực hiện dịch chuyển mảng (số lần shift)
        j = i - 1
        while j >= pos:
            b[j + 1] = b[j]
            binary_shifts += 1
            j -= 1
        b[pos] = key
        
    return {
        'sorted_arr': b,
        'standard_comps': standard_comps,
        'standard_shifts': standard_shifts,
        'binary_comps': binary_comps,
        'binary_shifts': binary_shifts
    }


# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '1': {
        'ten': 'BÀI 1: CHÈN MỘT PHẦN TỬ VÀO MẢNG ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 3, 5, 7], 'x': 4},
        'mong_doi': [1, 3, 4, 5, 7],
        'ham': lambda d: bai1_chen_mot_phan_tu(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}, Chèn x = {d['x']}\n=> Kết quả: {kq}"
    },
    '2': {
        'ten': 'BÀI 2: SẮP XẾP TĂNG DẦN CƠ BẢN',
        'du_lieu': {'a': [5, 2, 4, 6, 1, 3]},
        'mong_doi': [1, 2, 3, 4, 5, 6],
        'ham': lambda d: bai2_tang_dan(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\n=> Tăng dần: {kq}"
    },
    '3': {
        'ten': 'BÀI 3: SẮP XẾP GIẢM DẦN',
        'du_lieu': {'a': [5, 2, 4, 6, 1]},
        'mong_doi': [6, 5, 4, 2, 1],
        'ham': lambda d: bai3_giam_dan(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\n=> Giảm dần: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: IN MẢNG SAU MỖI BƯỚC CHÈN (VÒNG LẶP NGOÀI)',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [[1, 3, 2], [1, 2, 3]],
        'ham': lambda d: bai4_trang_thai_moi_vong(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Trạng thái mảng (từng vòng lặp):\n" + 
            "\n".join(f"  Vòng {idx + 1}: {v}" for idx, v in enumerate(kq))
        )
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN DỊCH CHUYỂN (SHIFT)',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 3),
        'ham': lambda d: bai5_dem_shift(d['a']),
        'format': lambda d, kq: f"Mảng: {d['a']} -> Đã sắp: {kq[0]}\n=> Tổng số lần dịch chuyển: {kq[1]} lần"
    },
    '6': {
        'ten': 'BÀI 6: ĐẾM SỐ LẦN SO SÁNH (BEST & WORST CASE)',
        'du_lieu': {'best': [1, 2, 3], 'worst': [3, 2, 1]},
        'mong_doi': 'So khớp thủ công',
        'ham': lambda d: (bai6_dem_so_sanh(d['best']), bai6_dem_so_sanh(d['worst'])), 
        'format': lambda d, kq: (
            f"[Best Case] Mảng {d['best']} -> Số so sánh thực tế: {kq[0][1]} "
            f"(Lý thuyết O(n-1) = {len(d['best']) - 1})\n"
            f"[Worst Case] Mảng {d['worst']} -> Số so sánh thực tế: {kq[1][1]} "
            f"(Lý thuyết O(n(n-1)/2) = {(len(d['worst']) * (len(d['worst']) - 1)) // 2})"
        )
    },
    '7': {
        'ten': 'BÀI 7: SẮP XẾP MẢNG KÝ TỰ (CHARACTER ARRAY)',
        'du_lieu': {'a': ['d', 'a', 'c', 'b']},
        'mong_doi': ['a', 'b', 'c', 'd'],
        'ham': lambda d: bai7_sap_xep_ky_tu(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\n=> Sau sắp xếp: {kq}"
    },
    '8': {
        'ten': 'BÀI 8: TRẠNG THÁI MẢNG SAU K BƯỚC',
        'du_lieu': {'a': [4, 3, 2, 1], 'k': 1},
        'mong_doi': [3, 4, 2, 1],
        'ham': lambda d: bai8_trang_thai_k_buoc(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}, Thực hiện k = {d['k']} vòng chèn\n"
            f"=> Trạng thái mảng hiện tại: {kq}\n"
            f"[*] Nhận xét: Chỉ {d['k']+1} phần tử đầu mảng (3, 4) được đảm bảo có thứ tự."
        )
    },
    '9': {
        'ten': 'BÀI 9: BINARY INSERTION SORT (SO SÁNH TỐI ƯU)',
        'du_lieu': {'a': [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]},
        'mong_doi': 'So sánh hiệu năng',
        'ham': lambda d: bai9_binary_insertion_sort(d['a']),
        'format': lambda d, kq: (
            f"Đầu vào: Mảng ngẫu nhiên cỡ {len(d['a'])}\n"
            f"1. Insertion Sort cơ bản:\n"
            f"   - Số phép so sánh: {kq['standard_comps']}\n"
            f"   - Số lần dịch chuyển: {kq['standard_shifts']}\n"
            f"2. Binary Insertion Sort (Cải tiến):\n"
            f"   - Số phép so sánh: {kq['binary_comps']} (Giảm đáng kể nhờ O(n log n))\n"
            f"   - Số lần dịch chuyển: {kq['binary_shifts']} (Không thay đổi)\n"
            f"[*] Kết luận: BS chỉ giảm số phép so sánh, mảng vẫn phải Shift từng phần tử."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    # Bỏ strict check cho bài 6 và bài 9 vì đang so khớp logic/hiệu năng
    if cfg['mong_doi'] not in ['So khớp thủ công', 'So sánh hiệu năng']:
        if isinstance(cfg['mong_doi'], list) and len(cfg['mong_doi']) > 0 and isinstance(cfg['mong_doi'][0], list):
            print("\nKết quả mong đợi:\n  " + "\n  ".join(f"Vòng {idx + 1}: {v}" for idx, v in enumerate(cfg['mong_doi'])))
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
            print(" MENU INSERTION SORT: PHIÊN 1 (BÀI 1 -> BÀI 9) ")
            print(" CHỌN BÀI (1-9) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*70)
            # Ép kiểu int để sort đúng từ 1 đến 9
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
