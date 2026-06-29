<<<<<<< HEAD
from typing import List, Tuple, Any
import random
import heapq

def bai18_so_sanh_swap(a: List[int]) -> Tuple[int, int]:
    b1 = a[:]
    n = len(b1)
    sel_swaps = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b1[j] < b1[vt_min]:
                vt_min = j
        if vt_min != i:
            b1[i], b1[vt_min] = b1[vt_min], b1[i]
            sel_swaps += 1
            
    b2 = a[:]
    bub_swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
                bub_swaps += 1
                
    return sel_swaps, bub_swaps

def bai19_phan_tich_double() -> str:
    return (
        "Phân tích Double Selection Sort:\n"
        "- Số vòng lặp: Giảm một nửa (n//2).\n"
        "- Số phép so sánh: Mỗi vòng tìm cả min và max mất 2*(n-2i-1). Tổng số so sánh vẫn là O(n^2).\n"
        "- Trường hợp biên: Khi max đang nằm ở vị trí i (vị trí đầu đoạn), thao tác đổi min về i sẽ vô tình đẩy max sang vị trí của min. Phải cập nhật lại vt_max = vt_min trước khi đổi max về cuối."
    )

def bai20_lien_he_heap() -> str:
    return (
        "Liên hệ với Heap Sort:\n"
        "- Selection Sort tốn O(n) để quét tìm min/max ở mỗi vòng.\n"
        "- Heap Sort chính là bản nâng cấp: Dùng cấu trúc Max-Heap/Min-Heap để lấy phần tử lớn nhất/nhỏ nhất chỉ trong O(log n).\n"
        "- Nhờ vậy, Heap Sort kéo độ phức tạp tổng thể xuống O(n log n)."
    )

def bai21_chung_minh_so_sanh() -> str:
    return (
        "Chứng minh số phép so sánh luôn cố định:\n"
        "- Vòng lặp ngoài chạy từ i = 0 đến n-2.\n"
        "- Vòng lặp trong luôn duyệt từ j = i+1 đến n-1, thực hiện chính xác (n - i - 1) phép so sánh.\n"
        "- Tổng số so sánh S = (n-1) + (n-2) + ... + 1 = n*(n-1)/2.\n"
        "- Quá trình này không chứa bất kỳ điều kiện ngắt sớm nào, nên luôn cố định bất kể mảng đầu vào."
    )

def bai22_stable_inplace(a: List[int]) -> Tuple[int, int]:
    b = a[:]
    n = len(b)
    shifts = 0
    swaps_equivalent = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            val = b[vt_min]
            curr = vt_min
            while curr > i:
                b[curr] = b[curr - 1]
                curr -= 1
                shifts += 1
            b[i] = val
            swaps_equivalent += 1
    return swaps_equivalent, shifts

def bai23_phan_tich_cases(n: int) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    def dem(arr):
        b = arr[:]
        l = len(b)
        ss = 0
        sw = 0
        for i in range(l - 1):
            vt_min = i
            for j in range(i + 1, l):
                ss += 1
                if b[j] < b[vt_min]:
                    vt_min = j
            if vt_min != i:
                b[i], b[vt_min] = b[vt_min], b[i]
                sw += 1
        return ss, sw
        
    best = list(range(n))
    worst = list(range(n, 0, -1))
    random.seed(42)
    avg = list(range(n))
    random.shuffle(avg)
    
    return dem(best), dem(avg), dem(worst)

def bai24_partial_vs_heap(a: List[int], k: int) -> Tuple[List[int], List[int]]:
    b1 = a[:]
    n = len(b1)
    for i in range(min(k, n)):
        vt_min = i
        for j in range(i + 1, n):
            if b1[j] < b1[vt_min]:
                vt_min = j
        b1[i], b1[vt_min] = b1[vt_min], b1[i]
    partial_res = b1[:k]
    
    b2 = a[:]
    heapq.heapify(b2)
    heap_res = [heapq.heappop(b2) for _ in range(k)]
    
    return partial_res, heap_res

def bai25_loop_invariant() -> str:
    return (
        "Chứng minh tính đúng đắn (Loop Invariant):\n"
        "- Bất biến: Trước vòng lặp thứ i, đoạn a[0..i-1] đã được sắp xếp và chứa i phần tử nhỏ nhất của mảng gốc.\n"
        "- Khởi tạo: i = 0, đoạn a[0..-1] rỗng, tính chất hiển nhiên đúng.\n"
        "- Duy trì: Tại vòng i, ta tìm min trong đoạn a[i..n-1] và đặt vào a[i]. Do a[0..i-1] đã chứa các phần tử nhỏ hơn, a[0..i] lúc này chứa i+1 phần tử nhỏ nhất.\n"
        "- Kết thúc (Tính dừng): Vòng lặp chạy hữu hạn và dừng ở i = n-1. Lúc này a[0..n-2] chứa n-1 phần tử nhỏ nhất. Phần tử a[n-1] còn lại chắc chắn là lớn nhất. Thuật toán đúng và kết thúc hoàn toàn."
    )

Noidung = {
    '18': {
        'ten': 'BÀI 18: SO SÁNH SỐ SWAP VỚI BUBBLE SORT',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': (2, 10),
        'ham': lambda d: bai18_so_sanh_swap(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSelection Sort (swap): {kq[0]} (<= n-1)\nBubble Sort (swap): {kq[1]} (Số nghịch thế)"
    },
    '19': {
        'ten': 'BÀI 19: PHÂN TÍCH DOUBLE-ENDED SELECTION',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai19_phan_tich_double(),
        'format': lambda d, kq: kq
    },
    '20': {
        'ten': 'BÀI 20: LIÊN HỆ VỚI HEAP SORT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai20_lien_he_heap(),
        'format': lambda d, kq: kq
    },
    '21': {
        'ten': 'BÀI 21: CHỨNG MINH SỐ SO SÁNH CỐ ĐỊNH',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai21_chung_minh_so_sanh(),
        'format': lambda d, kq: kq
    },
    '22': {
        'ten': 'BÀI 22: SELECTION SORT ỔN ĐỊNH IN-PLACE (ĐÁNH ĐỔI)',
        'du_lieu': {'a': [5, 2, 4, 6, 1, 3]},
        'mong_doi': None,
        'ham': lambda d: bai22_stable_inplace(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nNếu dùng Swap thông thường: ~{kq[0]} thao tác ghi.\nDùng Shift để giữ Stable: {kq[1]} thao tác ghi -> Chi phí dịch chuyển rất lớn."
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH BEST / AVERAGE / WORST CASE',
        'du_lieu': {'n': 10},
        'mong_doi': None,
        'ham': lambda d: bai23_phan_tich_cases(d['n']),
        'format': lambda d, kq: f"Kích thước n = {d['n']}\nBest Case (Đã sắp xếp)  : So sánh = {kq[0][0]}, Swap = {kq[0][1]}\nAverage Case (Ngẫu nhiên): So sánh = {kq[1][0]}, Swap = {kq[1][1]}\nWorst Case (Ngược chiều) : So sánh = {kq[2][0]}, Swap = {kq[2][1]}\n-> So sánh luôn là O(n^2), chỉ có Swap thay đổi."
    },
    '24': {
        'ten': 'BÀI 24: TÌM K NHỎ NHẤT (PARTIAL SELECTION VS HEAP)',
        'du_lieu': {'a': [7, 2, 5, 1, 9, 3, 6], 'k': 3},
        'mong_doi': ([1, 2, 3], [1, 2, 3]),
        'ham': lambda d: bai24_partial_vs_heap(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}, k = {d['k']}\nPartial Selection O(n·k): {kq[0]}\nHeap Sort O(n+k log n): {kq[1]}"
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
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU SELECTION SORT: PHẦN 4 (BÀI 18 - 25) ")
            print(" CHỌN BÀI (18-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
import random
import heapq

def bai18_so_sanh_swap(a: List[int]) -> Tuple[int, int]:
    b1 = a[:]
    n = len(b1)
    sel_swaps = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b1[j] < b1[vt_min]:
                vt_min = j
        if vt_min != i:
            b1[i], b1[vt_min] = b1[vt_min], b1[i]
            sel_swaps += 1
            
    b2 = a[:]
    bub_swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
                bub_swaps += 1
                
    return sel_swaps, bub_swaps

def bai19_phan_tich_double() -> str:
    return (
        "Phân tích Double Selection Sort:\n"
        "- Số vòng lặp: Giảm một nửa (n//2).\n"
        "- Số phép so sánh: Mỗi vòng tìm cả min và max mất 2*(n-2i-1). Tổng số so sánh vẫn là O(n^2).\n"
        "- Trường hợp biên: Khi max đang nằm ở vị trí i (vị trí đầu đoạn), thao tác đổi min về i sẽ vô tình đẩy max sang vị trí của min. Phải cập nhật lại vt_max = vt_min trước khi đổi max về cuối."
    )

def bai20_lien_he_heap() -> str:
    return (
        "Liên hệ với Heap Sort:\n"
        "- Selection Sort tốn O(n) để quét tìm min/max ở mỗi vòng.\n"
        "- Heap Sort chính là bản nâng cấp: Dùng cấu trúc Max-Heap/Min-Heap để lấy phần tử lớn nhất/nhỏ nhất chỉ trong O(log n).\n"
        "- Nhờ vậy, Heap Sort kéo độ phức tạp tổng thể xuống O(n log n)."
    )

def bai21_chung_minh_so_sanh() -> str:
    return (
        "Chứng minh số phép so sánh luôn cố định:\n"
        "- Vòng lặp ngoài chạy từ i = 0 đến n-2.\n"
        "- Vòng lặp trong luôn duyệt từ j = i+1 đến n-1, thực hiện chính xác (n - i - 1) phép so sánh.\n"
        "- Tổng số so sánh S = (n-1) + (n-2) + ... + 1 = n*(n-1)/2.\n"
        "- Quá trình này không chứa bất kỳ điều kiện ngắt sớm nào, nên luôn cố định bất kể mảng đầu vào."
    )

def bai22_stable_inplace(a: List[int]) -> Tuple[int, int]:
    b = a[:]
    n = len(b)
    shifts = 0
    swaps_equivalent = 0
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        if vt_min != i:
            val = b[vt_min]
            curr = vt_min
            while curr > i:
                b[curr] = b[curr - 1]
                curr -= 1
                shifts += 1
            b[i] = val
            swaps_equivalent += 1
    return swaps_equivalent, shifts

def bai23_phan_tich_cases(n: int) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    def dem(arr):
        b = arr[:]
        l = len(b)
        ss = 0
        sw = 0
        for i in range(l - 1):
            vt_min = i
            for j in range(i + 1, l):
                ss += 1
                if b[j] < b[vt_min]:
                    vt_min = j
            if vt_min != i:
                b[i], b[vt_min] = b[vt_min], b[i]
                sw += 1
        return ss, sw
        
    best = list(range(n))
    worst = list(range(n, 0, -1))
    random.seed(42)
    avg = list(range(n))
    random.shuffle(avg)
    
    return dem(best), dem(avg), dem(worst)

def bai24_partial_vs_heap(a: List[int], k: int) -> Tuple[List[int], List[int]]:
    b1 = a[:]
    n = len(b1)
    for i in range(min(k, n)):
        vt_min = i
        for j in range(i + 1, n):
            if b1[j] < b1[vt_min]:
                vt_min = j
        b1[i], b1[vt_min] = b1[vt_min], b1[i]
    partial_res = b1[:k]
    
    b2 = a[:]
    heapq.heapify(b2)
    heap_res = [heapq.heappop(b2) for _ in range(k)]
    
    return partial_res, heap_res

def bai25_loop_invariant() -> str:
    return (
        "Chứng minh tính đúng đắn (Loop Invariant):\n"
        "- Bất biến: Trước vòng lặp thứ i, đoạn a[0..i-1] đã được sắp xếp và chứa i phần tử nhỏ nhất của mảng gốc.\n"
        "- Khởi tạo: i = 0, đoạn a[0..-1] rỗng, tính chất hiển nhiên đúng.\n"
        "- Duy trì: Tại vòng i, ta tìm min trong đoạn a[i..n-1] và đặt vào a[i]. Do a[0..i-1] đã chứa các phần tử nhỏ hơn, a[0..i] lúc này chứa i+1 phần tử nhỏ nhất.\n"
        "- Kết thúc (Tính dừng): Vòng lặp chạy hữu hạn và dừng ở i = n-1. Lúc này a[0..n-2] chứa n-1 phần tử nhỏ nhất. Phần tử a[n-1] còn lại chắc chắn là lớn nhất. Thuật toán đúng và kết thúc hoàn toàn."
    )

Noidung = {
    '18': {
        'ten': 'BÀI 18: SO SÁNH SỐ SWAP VỚI BUBBLE SORT',
        'du_lieu': {'a': [5, 4, 3, 2, 1]},
        'mong_doi': (2, 10),
        'ham': lambda d: bai18_so_sanh_swap(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSelection Sort (swap): {kq[0]} (<= n-1)\nBubble Sort (swap): {kq[1]} (Số nghịch thế)"
    },
    '19': {
        'ten': 'BÀI 19: PHÂN TÍCH DOUBLE-ENDED SELECTION',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai19_phan_tich_double(),
        'format': lambda d, kq: kq
    },
    '20': {
        'ten': 'BÀI 20: LIÊN HỆ VỚI HEAP SORT',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai20_lien_he_heap(),
        'format': lambda d, kq: kq
    },
    '21': {
        'ten': 'BÀI 21: CHỨNG MINH SỐ SO SÁNH CỐ ĐỊNH',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: bai21_chung_minh_so_sanh(),
        'format': lambda d, kq: kq
    },
    '22': {
        'ten': 'BÀI 22: SELECTION SORT ỔN ĐỊNH IN-PLACE (ĐÁNH ĐỔI)',
        'du_lieu': {'a': [5, 2, 4, 6, 1, 3]},
        'mong_doi': None,
        'ham': lambda d: bai22_stable_inplace(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nNếu dùng Swap thông thường: ~{kq[0]} thao tác ghi.\nDùng Shift để giữ Stable: {kq[1]} thao tác ghi -> Chi phí dịch chuyển rất lớn."
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH BEST / AVERAGE / WORST CASE',
        'du_lieu': {'n': 10},
        'mong_doi': None,
        'ham': lambda d: bai23_phan_tich_cases(d['n']),
        'format': lambda d, kq: f"Kích thước n = {d['n']}\nBest Case (Đã sắp xếp)  : So sánh = {kq[0][0]}, Swap = {kq[0][1]}\nAverage Case (Ngẫu nhiên): So sánh = {kq[1][0]}, Swap = {kq[1][1]}\nWorst Case (Ngược chiều) : So sánh = {kq[2][0]}, Swap = {kq[2][1]}\n-> So sánh luôn là O(n^2), chỉ có Swap thay đổi."
    },
    '24': {
        'ten': 'BÀI 24: TÌM K NHỎ NHẤT (PARTIAL SELECTION VS HEAP)',
        'du_lieu': {'a': [7, 2, 5, 1, 9, 3, 6], 'k': 3},
        'mong_doi': ([1, 2, 3], [1, 2, 3]),
        'ham': lambda d: bai24_partial_vs_heap(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}, k = {d['k']}\nPartial Selection O(n·k): {kq[0]}\nHeap Sort O(n+k log n): {kq[1]}"
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
    
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU SELECTION SORT: PHẦN 4 (BÀI 18 - 25) ")
            print(" CHỌN BÀI (18-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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