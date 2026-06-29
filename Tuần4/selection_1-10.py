<<<<<<< HEAD
from typing import List, Tuple, Any

def bai1_min_ve_dau(a: List[int]) -> List[int]:
    b = a[:]
    if not b: 
        return b
    vt_min = 0
    for i in range(1, len(b)):
        if b[i] < b[vt_min]:
            vt_min = i
    b[0], b[vt_min] = b[vt_min], b[0]
    return b

def bai2_tang_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai3_giam_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_max = i
        for j in range(i + 1, n):
            if b[j] > b[vt_max]:
                vt_max = j
        b[i], b[vt_max] = b[vt_max], b[i]
    return b

def bai4_trang_thai_moi_vong(a: List[int]) -> List[List[int]]:
    b = a[:]
    n = len(b)
    trang_thai = []
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
        trang_thai.append(b[:])
    return trang_thai

def bai5_dem_swap(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_lan_swap = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            so_lan_swap += 1
    return b, so_lan_swap

def bai6_dem_so_sanh(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_sanh = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            so_sanh += 1
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b, so_sanh

def bai7_sap_xep_ky_tu(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai8_tim_min_trong_doan(a: List[int], start_i: int) -> int:
    vt_min = start_i
    for j in range(start_i + 1, len(a)):
        if a[j] < a[vt_min]:
            vt_min = j
    return vt_min

def bai9_double_selection(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n // 2):
        vt_min = i
        vt_max = i
        for j in range(i + 1, n - i):
            if b[j] < b[vt_min]:
                vt_min = j
            if b[j] > b[vt_max]:
                vt_max = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            if vt_max == i:
                vt_max = vt_min
        if vt_max != n - 1 - i:
            b[n - 1 - i], b[vt_max] = b[vt_max], b[n - 1 - i]
    return b

def bai10_dem_swap_chinh_xac(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_lan_swap = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            so_lan_swap += 1
    return b, so_lan_swap


Noidung = {
    '1': {
        'ten': 'BÀI 1: TÌM MIN ĐƯA VỀ ĐẦU',
        'du_lieu': {'a': [4, 2, 7, 1, 3]},
        'mong_doi': [1, 2, 7, 4, 3],
        'ham': lambda d: bai1_min_ve_dau(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau 1 bước: {kq}"
    },
    '2': {
        'ten': 'BÀI 2: SẮP XẾP TĂNG DẦN',
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
        'ten': 'BÀI 4: IN TRẠNG THÁI SAU MỖI VÒNG',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [[1, 3, 2], [1, 2, 3]],
        'ham': lambda d: bai4_trang_thai_moi_vong(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nCác vòng: " + "\n          ".join(str(x) for x in kq)
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN HOÁN ĐỔI (SWAP)',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 1),
        'ham': lambda d: bai5_dem_swap(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sắp xếp: {kq[0]}\n"
            f"Số swap thực tế: {kq[1]}\n"
            f"Tối đa cho phép (n-1): {len(d['a']) - 1}"
        )
    },
    '6': {
        'ten': 'BÀI 6: ĐẾM SỐ LẦN SO SÁNH',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': ([1, 2, 3, 4, 5], 10),
        'ham': lambda d: bai6_dem_so_sanh(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sắp xếp: {kq[0]}\n"
            f"Số so sánh thực tế: {kq[1]}\n"
            f"Công thức n(n-1)/2 = {(len(d['a'])*(len(d['a'])-1))//2}\n"
            f"Kiểm chứng: {'KHỚP' if kq[1] == (len(d['a'])*(len(d['a'])-1))//2 else 'SAI'}"
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
        'ten': 'BÀI 8: TÌM CHỈ SỐ MIN TRONG ĐOẠN [i, n)',
        'du_lieu': {'a': [9, 3, 7, 1, 5], 'i': 1},
        'mong_doi': 3,
        'ham': lambda d: bai8_tim_min_trong_doan(d['a'], d['i']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nĐoạn bắt đầu từ i={d['i']}\nChỉ số của Min: {kq}"
    },
    '9': {
        'ten': 'BÀI 9: DOUBLE SELECTION SORT',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [1, 2, 4, 5, 8],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp (Double): {kq}"
    },
    '9_edge': {
        'ten': 'BÀI 9 (TEST EDGE CASE): MAX Ở VỊ TRÍ ĐẦU',
        'du_lieu': {'a': [8, 4, 2, 1]},
        'mong_doi': [1, 2, 4, 8],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']} (max đang ở vị trí 0)\nSau sắp xếp (Double): {kq}"
    },
    '9_same': {
        'ten': 'BÀI 9 (TEST EDGE CASE): MẢNG TRÙNG LẶP',
        'du_lieu': {'a': [3, 3, 3]},
        'mong_doi': [3, 3, 3],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp (Double): {kq}"
    },
    '10': {
        'ten': 'BÀI 10: ĐẾM CHÍNH XÁC SỐ SWAP',
        'du_lieu': {'a': [1, 2, 3]},
        'mong_doi': ([1, 2, 3], 0),
        'ham': lambda d: bai10_dem_swap_chinh_xac(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq[0]}\nSố swap thực tế: {kq[1]}"
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
            print(" MENU SELECTION SORT: PHẦN 1 (BÀI 1 - 10) ")
            print(" CHỌN BÀI (1-10, 9_edge, 9_same) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
from typing import List, Tuple, Any

def bai1_min_ve_dau(a: List[int]) -> List[int]:
    b = a[:]
    if not b: 
        return b
    vt_min = 0
    for i in range(1, len(b)):
        if b[i] < b[vt_min]:
            vt_min = i
    b[0], b[vt_min] = b[vt_min], b[0]
    return b

def bai2_tang_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai3_giam_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_max = i
        for j in range(i + 1, n):
            if b[j] > b[vt_max]:
                vt_max = j
        b[i], b[vt_max] = b[vt_max], b[i]
    return b

def bai4_trang_thai_moi_vong(a: List[int]) -> List[List[int]]:
    b = a[:]
    n = len(b)
    trang_thai = []
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
        trang_thai.append(b[:])
    return trang_thai

def bai5_dem_swap(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_lan_swap = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            so_lan_swap += 1
    return b, so_lan_swap

def bai6_dem_so_sanh(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_sanh = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            so_sanh += 1
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b, so_sanh

def bai7_sap_xep_ky_tu(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai8_tim_min_trong_doan(a: List[int], start_i: int) -> int:
    vt_min = start_i
    for j in range(start_i + 1, len(a)):
        if a[j] < a[vt_min]:
            vt_min = j
    return vt_min

def bai9_double_selection(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n // 2):
        vt_min = i
        vt_max = i
        for j in range(i + 1, n - i):
            if b[j] < b[vt_min]:
                vt_min = j
            if b[j] > b[vt_max]:
                vt_max = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            if vt_max == i:
                vt_max = vt_min
        if vt_max != n - 1 - i:
            b[n - 1 - i], b[vt_max] = b[vt_max], b[n - 1 - i]
    return b

def bai10_dem_swap_chinh_xac(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    so_lan_swap = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            b[i], b[vt_min] = b[vt_min], b[i]
            so_lan_swap += 1
    return b, so_lan_swap


Noidung = {
    '1': {
        'ten': 'BÀI 1: TÌM MIN ĐƯA VỀ ĐẦU',
        'du_lieu': {'a': [4, 2, 7, 1, 3]},
        'mong_doi': [1, 2, 7, 4, 3],
        'ham': lambda d: bai1_min_ve_dau(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau 1 bước: {kq}"
    },
    '2': {
        'ten': 'BÀI 2: SẮP XẾP TĂNG DẦN',
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
        'ten': 'BÀI 4: IN TRẠNG THÁI SAU MỖI VÒNG',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [[1, 3, 2], [1, 2, 3]],
        'ham': lambda d: bai4_trang_thai_moi_vong(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nCác vòng: " + "\n          ".join(str(x) for x in kq)
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN HOÁN ĐỔI (SWAP)',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 1),
        'ham': lambda d: bai5_dem_swap(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sắp xếp: {kq[0]}\n"
            f"Số swap thực tế: {kq[1]}\n"
            f"Tối đa cho phép (n-1): {len(d['a']) - 1}"
        )
    },
    '6': {
        'ten': 'BÀI 6: ĐẾM SỐ LẦN SO SÁNH',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': ([1, 2, 3, 4, 5], 10),
        'ham': lambda d: bai6_dem_so_sanh(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sắp xếp: {kq[0]}\n"
            f"Số so sánh thực tế: {kq[1]}\n"
            f"Công thức n(n-1)/2 = {(len(d['a'])*(len(d['a'])-1))//2}\n"
            f"Kiểm chứng: {'KHỚP' if kq[1] == (len(d['a'])*(len(d['a'])-1))//2 else 'SAI'}"
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
        'ten': 'BÀI 8: TÌM CHỈ SỐ MIN TRONG ĐOẠN [i, n)',
        'du_lieu': {'a': [9, 3, 7, 1, 5], 'i': 1},
        'mong_doi': 3,
        'ham': lambda d: bai8_tim_min_trong_doan(d['a'], d['i']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nĐoạn bắt đầu từ i={d['i']}\nChỉ số của Min: {kq}"
    },
    '9': {
        'ten': 'BÀI 9: DOUBLE SELECTION SORT',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [1, 2, 4, 5, 8],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp (Double): {kq}"
    },
    '9_edge': {
        'ten': 'BÀI 9 (TEST EDGE CASE): MAX Ở VỊ TRÍ ĐẦU',
        'du_lieu': {'a': [8, 4, 2, 1]},
        'mong_doi': [1, 2, 4, 8],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']} (max đang ở vị trí 0)\nSau sắp xếp (Double): {kq}"
    },
    '9_same': {
        'ten': 'BÀI 9 (TEST EDGE CASE): MẢNG TRÙNG LẶP',
        'du_lieu': {'a': [3, 3, 3]},
        'mong_doi': [3, 3, 3],
        'ham': lambda d: bai9_double_selection(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp (Double): {kq}"
    },
    '10': {
        'ten': 'BÀI 10: ĐẾM CHÍNH XÁC SỐ SWAP',
        'du_lieu': {'a': [1, 2, 3]},
        'mong_doi': ([1, 2, 3], 0),
        'ham': lambda d: bai10_dem_swap_chinh_xac(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq[0]}\nSố swap thực tế: {kq[1]}"
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
            print(" MENU SELECTION SORT: PHẦN 1 (BÀI 1 - 10) ")
            print(" CHỌN BÀI (1-10, 9_edge, 9_same) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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