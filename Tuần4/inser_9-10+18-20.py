from typing import List, Tuple, Any

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

def bai9_binary_insertion(a: List[int]) -> Tuple[List[int], int, int]:
    b = a[:]
    n = len(b)
    so_sanh = 0
    shifts = 0
    for i in range(1, n):
        key = b[i]
        left, right = 0, i - 1
        while left <= right:
            so_sanh += 1
            mid = (left + right) // 2
            if b[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        j = i - 1
        while j >= left:
            b[j + 1] = b[j]
            shifts += 1
            j -= 1
        b[left] = key
    return b, so_sanh, shifts

def bai10_nghich_the_vs_shift(a: List[int]) -> Tuple[int, int]:
    n = len(a)
    nghich_the = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                nghich_the += 1
                
    b = a[:]
    shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            shifts += 1
            j -= 1
        b[j + 1] = key
    return nghich_the, shifts

def bai18_phan_tich_do_tim() -> str:
    return (
        "So sánh Dò từ phải sang trái vs trái sang phải:\n"
        "- Phải sang trái (Chuẩn): Nếu a[i] lớn hơn a[i-1], vòng lặp ngắt ngay (1 phép so sánh). Cực kỳ tối ưu cho mảng gần sắp xếp O(n).\n"
        "- Trái sang phải: Luôn phải duyệt từ đầu mảng để tìm vị trí, không tận dụng được tính chất mảng con đã sắp xếp, mất thời gian vô ích."
    )

def bai19_gnome_sort(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    pos = 0
    thao_tac = 0
    while pos < n:
        thao_tac += 1
        if pos == 0 or b[pos] >= b[pos - 1]:
            pos += 1
        else:
            b[pos], b[pos - 1] = b[pos - 1], b[pos]
            pos -= 1
    return b, thao_tac

def bai20_shell_sort(a: List[int]) -> Tuple[List[int], int]:
    b = a[:]
    n = len(b)
    gap = n // 2
    shifts = 0
    while gap > 0:
        for i in range(gap, n):
            key = b[i]
            j = i
            while j >= gap and b[j - gap] > key:
                b[j] = b[j - gap]
                shifts += 1
                j -= gap
            b[j] = key
        gap //= 2
    return b, shifts

Noidung = {
    '9': {
        'ten': 'BÀI 9: BINARY INSERTION SORT',
        'du_lieu': {'a': [5, 2, 4, 6, 1, 3]},
        'mong_doi': ([1, 2, 3, 4, 5, 6], 10, 9),
        'ham': lambda d: bai9_binary_insertion(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq[0]}\nSố so sánh: {kq[1]} (Đã giảm nhờ Binary Search)\nSố lần shift: {kq[2]}"
    },
    '10': {
        'ten': 'BÀI 10: SỐ SHIFT = SỐ NGHỊCH THẾ',
        'du_lieu': {'a': [2, 4, 1, 3]},
        'mong_doi': (3, 3),
        'ham': lambda d: bai10_nghich_the_vs_shift(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSố nghịch thế thực tế: {kq[0]}\nTổng số lần shift: {kq[1]}"
    },
    '18': {
        'ten': 'BÀI 18: CHÈN TỪ CUỐI HAY ĐẦU?',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai18_phan_tich_do_tim(),
        'format': lambda d, kq: kq
    },
    '19': {
        'ten': 'BÀI 19: GNOME SORT',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': ([1, 2, 3], 9),
        'ham': lambda d: bai19_gnome_sort(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq[0]}\nSố thao tác vòng lặp: {kq[1]}"
    },
    '20': {
        'ten': 'BÀI 20: SHELL SORT',
        'du_lieu': {'a': [8, 3, 5, 2, 9, 1, 4, 7]},
        'mong_doi': ([1, 2, 3, 4, 5, 7, 8, 9], 13),
        'ham': lambda d: bai20_shell_sort(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']} (Dãy gap: n/2)\nSau sắp xếp: {kq[0]}\nSố lần shift: {kq[1]} (Thấp hơn đáng kể so với Insertion thông thường)"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg.get('mong_doi') is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU INSERTION SORT: PHẦN 2 (BÀI 9, 10, 18-20) + UPDATE BÀI 6 ")
            print(" CHỌN KHÓA HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k:>14}. {v['ten']}")
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