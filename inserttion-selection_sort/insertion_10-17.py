from typing import List, Tuple, Any, Dict

def bai10_shift_va_nghich_the(a: List[int]) -> Dict[str, int]:
    n = len(a)
    # 1. Đếm số nghịch thế (Inversions) bằng O(n^2) cho mảng nhỏ
    nghich_the = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                nghich_the += 1
                
    # 2. Đếm số lần shift khi chạy Insertion Sort
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
        
    return {
        'nghich_the': nghich_the,
        'shifts': shifts
    }

def bai11_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(1, n):
        key = b[i]
        j = i - 1
        # So sánh theo trị tuyệt đối
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
        # So sánh theo độ dài chuỗi
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
        # So sánh chỉ theo phần tử đầu tiên (khóa)
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
            # Ưu tiên 1: Điểm giảm dần
            if b[j][1] < key[1]:
                b[j + 1] = b[j]
                j -= 1
            # Ưu tiên 2: Bằng điểm thì Tên tăng dần (Alphabet)
            elif b[j][1] == key[1] and b[j][0] > key[0]:
                b[j + 1] = b[j]
                j -= 1
            else:
                break
        b[j + 1] = key
    return b

# --- Hỗ trợ cho Bài 15 ---
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
        # Tìm vị trí chèn trong danh sách liên kết đã sắp xếp
        while curr and curr.val <= new_node.val:
            prev = curr
            curr = curr.next
        # Nối node mới vào giữa prev và curr
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
        b.append(x) # Nạp phần tử mới vào cuối
        j = len(b) - 2
        # Đưa phần tử mới vào đúng vị trí để mảng luôn duy trì tính sắp xếp
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

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '10': {
        'ten': 'BÀI 10: SỐ SHIFT = SỐ NGHỊCH THẾ',
        'du_lieu': {'a': [2, 4, 1, 3]},
        'mong_doi': {'nghich_the': 3, 'shifts': 3},
        'ham': lambda d: bai10_shift_va_nghich_the(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Tổng số nghịch thế đếm được: {kq['nghich_the']}\n"
            f"Tổng số lần shift của thuật toán: {kq['shifts']}\n"
            f"[*] Bằng chứng: Mỗi phép shift của Insertion Sort chính xác là triệt tiêu đi một nghịch thế."
        )
    },
    '11': {
        'ten': 'BÀI 11: SẮP XẾP THEO TRỊ TUYỆT ĐỐI (ỔN ĐỊNH)',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: bai11_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\n=> Sau sắp xếp theo |x|: {kq}\n[*] Số -2 vẫn đứng trước số 2 (Tính ổn định)."
    },
    '12': {
        'ten': 'BÀI 12: SẮP XẾP CHUỖI THEO ĐỘ DÀI',
        'du_lieu': {'a': ['abc', 'a', 'ab']},
        'mong_doi': ['a', 'ab', 'abc'],
        'ham': lambda d: bai12_chuoi_theo_do_dai(d['a']),
        'format': lambda d, kq: f"Mảng chuỗi gốc: {d['a']}\n=> Sau sắp xếp theo len(): {kq}"
    },
    '13': {
        'ten': 'BÀI 13: TÍNH ỔN ĐỊNH (STABILITY)',
        'du_lieu': {'a': [(2, 'a'), (1, 'b'), (2, 'c')]},
        'mong_doi': [(1, 'b'), (2, 'a'), (2, 'c')],
        'ham': lambda d: bai13_tinh_on_dinh(d['a']),
        'format': lambda d, kq: (
            f"Mảng Tuple (Khóa, Nhãn): {d['a']}\n"
            f"=> Sau sắp xếp theo Khóa: {kq}\n"
            f"[*] Tuple (2, 'a') vẫn đứng trước (2, 'c') như ban đầu."
        )
    },
    '14': {
        'ten': 'BÀI 14: SẮP XẾP ĐỐI TƯỢNG (ĐA KHÓA)',
        'du_lieu': {'a': [('An', 8), ('Ba', 9), ('Cu', 8)]},
        'mong_doi': [('Ba', 9), ('An', 8), ('Cu', 8)],
        'ham': lambda d: bai14_da_khoa(d['a']),
        'format': lambda d, kq: (
            f"Danh sách HS (Tên, Điểm): {d['a']}\n"
            f"=> Sắp xếp theo [Điểm giảm dần -> Tên tăng dần]:\n   {kq}"
        )
    },
    '15': {
        'ten': 'BÀI 15: INSERTION SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai15_linked_list(d['a']),
        'format': lambda d, kq: f"Luồng dữ liệu gốc nạp vào Linked List: {d['a']}\n=> Trích xuất mảng sau khi sắp xếp trên List: {kq}"
    },
    '16': {
        'ten': 'BÀI 16: SẮP XẾP TRỰC TUYẾN (ONLINE SORT)',
        'du_lieu': {'stream': [5, 2, 8, 1]},
        'mong_doi': [[5], [2, 5], [2, 5, 8], [1, 2, 5, 8]],
        'ham': lambda d: bai16_online_sort(d['stream']),
        'format': lambda d, kq: (
            f"Luồng vào lần lượt: {d['stream']}\n"
            f"Trạng thái duy trì tính sắp xếp:\n" + 
            "\n".join(f"  Nhận {d['stream'][idx]:>2} -> {v}" for idx, v in enumerate(kq))
        )
    },
    '17': {
        'ten': 'BÀI 17: MẢNG GẦN NHƯ ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 2, 4, 3, 5]},
        'mong_doi': ([1, 2, 3, 4, 5], 1),
        'ham': lambda d: bai17_mang_gan_sap_xep(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc (Chỉ 1 cặp nghịch thế): {d['a']}\n"
            f"=> Số lần shift thực tế: {kq[1]}\n"
            f"[*] Thuật toán chạm ngưỡng độ phức tạp O(n) thay vì O(n^2)."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
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
            print(" MENU INSERTION SORT: PHIÊN 2 (BÀI 10 -> BÀI 17) ")
            print(" CHỌN BÀI (10-17) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*70)
            # Ép kiểu int để sort đúng từ 10 đến 17
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
