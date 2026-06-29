<<<<<<< HEAD
from typing import List, Tuple, Any
import random

def bai11_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and abs(b[j]) > abs(key):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai12_chuoi_theo_do_dai(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and len(b[j]) > len(key):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai13_tinh_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j][0] > key[0]:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai14_da_khoa(a: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0:
            if b[j][1] < key[1]:
                b[j + 1] = b[j]
                j -= 1
            elif b[j][1] == key[1] and b[j][0] > key[0]:
                b[j + 1] = b[j]
                j -= 1
            else:
                break
        b[j + 1] = key
    return b

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bai15_linked_list(a: List[int]) -> List[int]:
    if not a: return []
    dummy = Node(0)
    for val in a:
        new_node = Node(val)
        prev = dummy
        curr = dummy.next
        while curr and curr.val <= new_node.val:
            prev = curr
            curr = curr.next
        new_node.next = curr
        prev.next = new_node
        
    res = []
    curr = dummy.next
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def bai16_online_sort(stream: List[int]) -> List[List[int]]:
    b = []
    trang_thai = []
    for x in stream:
        b.append(x)
        j = len(b) - 2
        while j >= 0 and b[j] > x:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = x
        trang_thai.append(b[:])
    return trang_thai

def bai17_mang_gan_sap_xep(a: List[int]) -> Tuple[List[int], int]:
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

def bai21_dem_shift_merge_sort(a: List[int]) -> int:
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
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
    n = len(b)
    temp = [0] * n
    return merge_sort_and_count(b, temp, 0, n - 1)

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

def bai23_phan_tich_cases(n: int) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
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
    return count_ops(best), count_ops(avg), count_ops(worst)

def bai24_so_sanh_3_thuat_toan(a: List[int]) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
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

    return ins(a), bub(a), sel(a)

def bai25_loop_invariant() -> str:
    return (
        "Bất biến vòng lặp (Loop Invariant) của Insertion Sort:\n"
        "- Bất biến: Trước khi bắt đầu vòng lặp ngoài lần thứ i, mảng con a[0..i-1] luôn chứa các phần tử ban đầu của đoạn này nhưng đã được sắp xếp tăng dần.\n"
        "- Khởi tạo (i=1): Mảng con a[0..0] chỉ có 1 phần tử nên luôn coi là đã được sắp xếp. Đúng.\n"
        "- Duy trì: Tại vòng lặp i, phần tử a[i] được chèn vào vị trí đúng trong mảng con a[0..i-1]. Kết thúc vòng lặp, đoạn a[0..i] chứa các phần tử ban đầu nhưng đã sắp xếp.\n"
        "- Kết thúc: Khi vòng lặp chạy đến i=n, đoạn a[0..n-1] đã sắp xếp. Đây chính là toàn bộ mảng. Suy ra thuật toán đúng đắn."
    )

Noidung = {
    '11': {
        'ten': 'BÀI 11: SẮP XẾP THEO TRỊ TUYỆT ĐỐI (ỔN ĐỊNH)',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: bai11_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '12': {
        'ten': 'BÀI 12: SẮP XẾP CHUỖI THEO ĐỘ DÀI',
        'du_lieu': {'a': ['abc', 'a', 'ab']},
        'mong_doi': ['a', 'ab', 'abc'],
        'ham': lambda d: bai12_chuoi_theo_do_dai(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '13': {
        'ten': 'BÀI 13: TÍNH ỔN ĐỊNH (STABILITY)',
        'du_lieu': {'a': [(2, 'a'), (1, 'b'), (2, 'c')]},
        'mong_doi': [(1, 'b'), (2, 'a'), (2, 'c')],
        'ham': lambda d: bai13_tinh_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: SẮP XẾP ĐỐI TƯỢNG (ĐA KHÓA)',
        'du_lieu': {'a': [('An', 8), ('Ba', 9), ('Cu', 8)]},
        'mong_doi': [('Ba', 9), ('An', 8), ('Cu', 8)],
        'ham': lambda d: bai14_da_khoa(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '15': {
        'ten': 'BÀI 15: INSERTION SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai15_linked_list(d['a']),
        'format': lambda d, kq: f"Luồng dữ liệu gốc: {d['a']}\nDanh sách kết quả: {kq}"
    },
    '16': {
        'ten': 'BÀI 16: SẮP XẾP TRỰC TUYẾN (ONLINE SORT)',
        'du_lieu': {'stream': [5, 2, 8, 1]},
        'mong_doi': [[5], [2, 5], [2, 5, 8], [1, 2, 5, 8]],
        'ham': lambda d: bai16_online_sort(d['stream']),
        'format': lambda d, kq: f"Luồng vào: {d['stream']}\nTrạng thái mảng: " + "\n                 ".join(str(x) for x in kq)
    },
    '17': {
        'ten': 'BÀI 17: MẢNG GẦN NHƯ ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 2, 4, 3, 5]},
        'mong_doi': ([1, 2, 3, 4, 5], 1),
        'ham': lambda d: bai17_mang_gan_sap_xep(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSố shift: {kq[1]} -> Chi phí gần O(n)"
    },
    '21': {
        'ten': 'BÀI 21: ĐẾM SHIFT CHO MẢNG LỚN O(n log n)',
        'du_lieu': {'a': [2, 4, 1, 3]},
        'mong_doi': 3,
        'ham': lambda d: bai21_dem_shift_merge_sort(d['a']),
        'format': lambda d, kq: f"Mảng gốc giả lập: {d['a']}\nThuật toán sử dụng: Merge Sort Counting\nTổng số shift/nghịch thế: {kq}"
    },
    '22': {
        'ten': 'BÀI 22: MẢNG ĐỘ LỆCH <= K',
        'du_lieu': {'a': [2, 1, 4, 3, 6, 5], 'k': 1},
        'mong_doi': ([1, 2, 3, 4, 5, 6], 3),
        'ham': lambda d: bai22_do_lech_k(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Kích thước n={len(d['a'])}, lệch tối đa k={d['k']}\n"
            f"Số shift thực tế: {kq[1]}\n"
            f"Kết luận: {kq[1]} <= n*k = {len(d['a'])*d['k']} -> Chứng minh O(n·k) thành công"
        )
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH BEST / AVERAGE / WORST',
        'du_lieu': {'n': 5},
        'mong_doi': None,
        'ham': lambda d: bai23_phan_tich_cases(d['n']),
        'format': lambda d, kq: (
            f"Kích thước giả lập n = {d['n']}\n"
            f"Best Case  : So sánh = {kq[0][0]}, Shift = {kq[0][1]}\n"
            f"Average    : So sánh = {kq[1][0]}, Shift = {kq[1][1]}\n"
            f"Worst Case : So sánh = {kq[2][0]}, Shift = {kq[2][1]}"
        )
    },
    '24': {
        'ten': 'BÀI 24: SO SÁNH 3 THUẬT TOÁN O(n^2)',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': None,
        'ham': lambda d: bai24_so_sanh_3_thuat_toan(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Insertion: So sánh={kq[0][0]}, Shift={kq[0][1]}\n"
            f"Bubble   : So sánh={kq[1][0]}, Swap={kq[1][1]}\n"
            f"Selection: So sánh={kq[2][0]}, Swap={kq[2][1]}"
        )
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai25_loop_invariant(),
        'format': lambda d, kq: kq
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
            print(" MENU INSERTION SORT: PHẦN 3 & 4 (BÀI 11 - 25) ")
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
=======
from typing import List, Tuple, Any
import random

def bai11_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and abs(b[j]) > abs(key):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai12_chuoi_theo_do_dai(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and len(b[j]) > len(key):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai13_tinh_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j][0] > key[0]:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b

def bai14_da_khoa(a: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0:
            if b[j][1] < key[1]:
                b[j + 1] = b[j]
                j -= 1
            elif b[j][1] == key[1] and b[j][0] > key[0]:
                b[j + 1] = b[j]
                j -= 1
            else:
                break
        b[j + 1] = key
    return b

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bai15_linked_list(a: List[int]) -> List[int]:
    if not a: return []
    dummy = Node(0)
    for val in a:
        new_node = Node(val)
        prev = dummy
        curr = dummy.next
        while curr and curr.val <= new_node.val:
            prev = curr
            curr = curr.next
        new_node.next = curr
        prev.next = new_node
        
    res = []
    curr = dummy.next
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def bai16_online_sort(stream: List[int]) -> List[List[int]]:
    b = []
    trang_thai = []
    for x in stream:
        b.append(x)
        j = len(b) - 2
        while j >= 0 and b[j] > x:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = x
        trang_thai.append(b[:])
    return trang_thai

def bai17_mang_gan_sap_xep(a: List[int]) -> Tuple[List[int], int]:
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

def bai21_dem_shift_merge_sort(a: List[int]) -> int:
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
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
    n = len(b)
    temp = [0] * n
    return merge_sort_and_count(b, temp, 0, n - 1)

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

def bai23_phan_tich_cases(n: int) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
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
    return count_ops(best), count_ops(avg), count_ops(worst)

def bai24_so_sanh_3_thuat_toan(a: List[int]) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
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

    return ins(a), bub(a), sel(a)

def bai25_loop_invariant() -> str:
    return (
        "Bất biến vòng lặp (Loop Invariant) của Insertion Sort:\n"
        "- Bất biến: Trước khi bắt đầu vòng lặp ngoài lần thứ i, mảng con a[0..i-1] luôn chứa các phần tử ban đầu của đoạn này nhưng đã được sắp xếp tăng dần.\n"
        "- Khởi tạo (i=1): Mảng con a[0..0] chỉ có 1 phần tử nên luôn coi là đã được sắp xếp. Đúng.\n"
        "- Duy trì: Tại vòng lặp i, phần tử a[i] được chèn vào vị trí đúng trong mảng con a[0..i-1]. Kết thúc vòng lặp, đoạn a[0..i] chứa các phần tử ban đầu nhưng đã sắp xếp.\n"
        "- Kết thúc: Khi vòng lặp chạy đến i=n, đoạn a[0..n-1] đã sắp xếp. Đây chính là toàn bộ mảng. Suy ra thuật toán đúng đắn."
    )

Noidung = {
    '11': {
        'ten': 'BÀI 11: SẮP XẾP THEO TRỊ TUYỆT ĐỐI (ỔN ĐỊNH)',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: bai11_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '12': {
        'ten': 'BÀI 12: SẮP XẾP CHUỖI THEO ĐỘ DÀI',
        'du_lieu': {'a': ['abc', 'a', 'ab']},
        'mong_doi': ['a', 'ab', 'abc'],
        'ham': lambda d: bai12_chuoi_theo_do_dai(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '13': {
        'ten': 'BÀI 13: TÍNH ỔN ĐỊNH (STABILITY)',
        'du_lieu': {'a': [(2, 'a'), (1, 'b'), (2, 'c')]},
        'mong_doi': [(1, 'b'), (2, 'a'), (2, 'c')],
        'ham': lambda d: bai13_tinh_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: SẮP XẾP ĐỐI TƯỢNG (ĐA KHÓA)',
        'du_lieu': {'a': [('An', 8), ('Ba', 9), ('Cu', 8)]},
        'mong_doi': [('Ba', 9), ('An', 8), ('Cu', 8)],
        'ham': lambda d: bai14_da_khoa(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '15': {
        'ten': 'BÀI 15: INSERTION SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai15_linked_list(d['a']),
        'format': lambda d, kq: f"Luồng dữ liệu gốc: {d['a']}\nDanh sách kết quả: {kq}"
    },
    '16': {
        'ten': 'BÀI 16: SẮP XẾP TRỰC TUYẾN (ONLINE SORT)',
        'du_lieu': {'stream': [5, 2, 8, 1]},
        'mong_doi': [[5], [2, 5], [2, 5, 8], [1, 2, 5, 8]],
        'ham': lambda d: bai16_online_sort(d['stream']),
        'format': lambda d, kq: f"Luồng vào: {d['stream']}\nTrạng thái mảng: " + "\n                 ".join(str(x) for x in kq)
    },
    '17': {
        'ten': 'BÀI 17: MẢNG GẦN NHƯ ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 2, 4, 3, 5]},
        'mong_doi': ([1, 2, 3, 4, 5], 1),
        'ham': lambda d: bai17_mang_gan_sap_xep(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSố shift: {kq[1]} -> Chi phí gần O(n)"
    },
    '21': {
        'ten': 'BÀI 21: ĐẾM SHIFT CHO MẢNG LỚN O(n log n)',
        'du_lieu': {'a': [2, 4, 1, 3]},
        'mong_doi': 3,
        'ham': lambda d: bai21_dem_shift_merge_sort(d['a']),
        'format': lambda d, kq: f"Mảng gốc giả lập: {d['a']}\nThuật toán sử dụng: Merge Sort Counting\nTổng số shift/nghịch thế: {kq}"
    },
    '22': {
        'ten': 'BÀI 22: MẢNG ĐỘ LỆCH <= K',
        'du_lieu': {'a': [2, 1, 4, 3, 6, 5], 'k': 1},
        'mong_doi': ([1, 2, 3, 4, 5, 6], 3),
        'ham': lambda d: bai22_do_lech_k(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Kích thước n={len(d['a'])}, lệch tối đa k={d['k']}\n"
            f"Số shift thực tế: {kq[1]}\n"
            f"Kết luận: {kq[1]} <= n*k = {len(d['a'])*d['k']} -> Chứng minh O(n·k) thành công"
        )
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH BEST / AVERAGE / WORST',
        'du_lieu': {'n': 5},
        'mong_doi': None,
        'ham': lambda d: bai23_phan_tich_cases(d['n']),
        'format': lambda d, kq: (
            f"Kích thước giả lập n = {d['n']}\n"
            f"Best Case  : So sánh = {kq[0][0]}, Shift = {kq[0][1]}\n"
            f"Average    : So sánh = {kq[1][0]}, Shift = {kq[1][1]}\n"
            f"Worst Case : So sánh = {kq[2][0]}, Shift = {kq[2][1]}"
        )
    },
    '24': {
        'ten': 'BÀI 24: SO SÁNH 3 THUẬT TOÁN O(n^2)',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': None,
        'ham': lambda d: bai24_so_sanh_3_thuat_toan(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Insertion: So sánh={kq[0][0]}, Shift={kq[0][1]}\n"
            f"Bubble   : So sánh={kq[1][0]}, Swap={kq[1][1]}\n"
            f"Selection: So sánh={kq[2][0]}, Swap={kq[2][1]}"
        )
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai25_loop_invariant(),
        'format': lambda d, kq: kq
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
            print(" MENU INSERTION SORT: PHẦN 3 & 4 (BÀI 11 - 25) ")
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
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
        pass