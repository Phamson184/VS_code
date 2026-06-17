from typing import List, Tuple, Any

def bai1_chen_mot_phan_tu(a: List[int], x: int) -> List[int]:
    b = a[:]
    b.append(x)
    j = len(b) - 2
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
            so_sanh += 1
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

Noidung = {
    '1': {
        'ten': 'BÀI 1: CHÈN MỘT PHẦN TỬ VÀO MẢNG ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 3, 5, 7], 'x': 4},
        'mong_doi': [1, 3, 4, 5, 7],
        'ham': lambda d: bai1_chen_mot_phan_tu(d['a'], d['x']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}, x = {d['x']}\nSau khi chèn: {kq}"
    },
    '2': {
        'ten': 'BÀI 2: SẮP XẾP TĂNG DẦN CƠ BẢN',
        'du_lieu': {'a': [5, 2, 4, 6, 1, 3]},
        'mong_doi': [1, 2, 3, 4, 5, 6],
        'ham': lambda d: bai2_tang_dan(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nTăng dần: {kq}"
    },
    '3': {
        'ten': 'BÀI 3: SẮP XẾP GIẢM DẦN',
        'du_lieu': {'a': [5, 2, 4, 6, 1]},
        'mong_doi': [6, 5, 4, 2, 1],
        'ham': lambda d: bai3_giam_dan(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nGiảm dần: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: IN MẢNG SAU MỖI BƯỚC CHÈN',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [[1, 3, 2], [1, 2, 3]],
        'ham': lambda d: bai4_trang_thai_moi_vong(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nCác vòng: " + "\n          ".join(str(x) for x in kq)
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN DỊCH CHUYỂN (SHIFT)',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 3),
        'ham': lambda d: bai5_dem_shift(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq[0]}\nSố lần dịch chuyển (shift): {kq[1]}"
    },
    '6_best': {
        'ten': 'BÀI 6: CÓ KIỂM CHỨNG CÔNG THỨC',
        'du_lieu': {'a': [1, 2, 3]},
        'mong_doi': ([1, 2, 3], 2), 
        'ham': lambda d: bai6_dem_so_sanh(d['a']), 
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Số so sánh: {kq[1]}\n"
            f"Best case O(n-1) = {len(d['a']) - 1} | "
            f"Worst case O(n(n-1)/2) = {(len(d['a']) * (len(d['a']) - 1)) // 2}"
        )
    },
    '6_worst': {
        'ten': 'BÀI 6: CÓ KIỂM CHỨNG CÔNG THỨC',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 3),
        'ham': lambda d: bai6_dem_so_sanh(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Số so sánh: {kq[1]}\n"
            f"Best case O(n-1) = {len(d['a']) - 1} | "
            f"Worst case O(n(n-1)/2) = {(len(d['a']) * (len(d['a']) - 1)) // 2}"
        )
    },
    '7': {
        'ten': 'BÀI 7: SẮP XẾP MẢNG KÝ TỰ',
        'du_lieu': {'a': ['d', 'a', 'c', 'b']},
        'mong_doi': ['a', 'b', 'c', 'd'],
        'ham': lambda d: bai7_sap_xep_ky_tu(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '8': {
        'ten': 'BÀI 8: TRẠNG THÁI SAU K BƯỚC',
        'du_lieu': {'a': [4, 3, 2, 1], 'k': 1},
        'mong_doi': [3, 4, 2, 1],
        'ham': lambda d: bai8_trang_thai_k_buoc(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}, k = {d['k']}\nSau {d['k']} vòng chèn: {kq}\n(Lưu ý: Chỉ {d['k']+1} phần tử đầu được sắp xếp)"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if isinstance(cfg['mong_doi'], list) and len(cfg['mong_doi']) > 0 and isinstance(cfg['mong_doi'][0], list):
        print("Kết quả mong đợi: \n          " + "\n          ".join(str(x) for x in cfg['mong_doi']))
    else:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        
    if kq == cfg['mong_doi']:
        print("Trạng thái: THÀNH CÔNG")
    else:
        print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU INSERTION SORT: PHẦN 1 (BÀI 1 - 8) ")
            print(" CHỌN BÀI (1-8, 6_best, 6_worst) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k:>7}. {v['ten']}")
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