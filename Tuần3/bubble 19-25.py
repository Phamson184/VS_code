from typing import List, Tuple
import random

def luot_toi_thieu(a: List[int]) -> Tuple[int, int]:
    b, so_luot = a[:], 0
    n = len(b)
    for i in range(n - 1):
        da_swap = False
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                da_swap = True
        if not da_swap:
            break
        so_luot += 1
    return so_luot, b

def dem_nghich_the_nhanh(a: List[int]) -> int:
    if len(a) <= 1:
        return 0
    giua = len(a) // 2
    trai, phai = a[:giua], a[giua:]
    dem = dem_nghich_the_nhanh(trai) + dem_nghich_the_nhanh(phai)
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            i += 1
        else:
            dem += len(trai) - i
            j += 1
    return dem

def do_hieu_nang(a: List[int]) -> dict:
    def chay(b):
        arr, so_ss, so_swap = b[:], 0, 0
        n = len(arr)
        for i in range(n - 1):
            da_swap = False
            for j in range(n - 1 - i):
                so_ss += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    so_swap += 1
                    da_swap = True
            if not da_swap:
                break
        return so_ss, so_swap

    ngau_nhien = a[:]
    da_sort = sorted(a)
    nguoc = sorted(a, reverse=True)
    n = len(a)

    ss_nn, sw_nn = chay(ngau_nhien)
    ss_ds, sw_ds = chay(da_sort)
    ss_ng, sw_ng = chay(nguoc)

    return {
        'n': n,
        'ngau_nhien': (ss_nn, sw_nn),
        'da_sort': (ss_ds, sw_ds),
        'nguoc': (ss_ng, sw_ng),
        'ly_thuyet_tot': n - 1,
        'ly_thuyet_xau': n * (n - 1) // 2,
    }

def khoi_phuc_luot(dau: List[int], sau: List[int]) -> int:
    kiem_tra = dau[:]
    n = len(kiem_tra)
    so_luot = 0
    while kiem_tra != sau:
        da_swap = False
        for j in range(n - 1 - so_luot):
            if kiem_tra[j] > kiem_tra[j + 1]:
                kiem_tra[j], kiem_tra[j + 1] = kiem_tra[j + 1], kiem_tra[j]
                da_swap = True
        so_luot += 1
        if not da_swap:
            break
    return so_luot

def gan_sort_ok(a: List[int], k: int) -> Tuple[int, bool]:
    b, so_luot = a[:], 0
    n = len(b)
    for i in range(n - 1):
        da_swap = False
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                da_swap = True
        so_luot += 1
        if not da_swap:
            break
    chung_minh = so_luot <= n * k
    return so_luot, chung_minh

BAT_BIEN = """
BẤT BIẾN VÒNG LẶP CỦA BUBBLE SORT
====================================
Phát biểu:
  Sau lượt thứ i (i = 1, 2, ..., n-1):
  - i phần tử lớn nhất đã nằm đúng vị trí ở cuối mảng
    tức là a[n-i], a[n-i+1], ..., a[n-1] đã được sắp xếp đúng
    và đây là i phần tử lớn nhất của toàn mảng.

Chứng minh bằng quy nạp:
  [Cơ sở] i = 1:
    Trong lượt 1, duyệt j từ 0 đến n-2:
    Mỗi khi a[j] > a[j+1] thì hoán đổi.
    Phần tử lớn nhất sẽ được "nổi bọt" dần về cuối.
    => Sau lượt 1: a[n-1] = max(a) → đúng chỗ.

  [Quy nạp] Giả sử đúng với lượt i:
    a[n-i..n-1] chứa i phần tử lớn nhất, đúng vị trí.
    Lượt i+1 duyệt j từ 0 đến n-i-2 (bỏ qua phần đã đúng).
    Phần tử lớn nhất trong a[0..n-i-1] sẽ nổi về a[n-i-1].
    => Sau lượt i+1: a[n-i-1..n-1] đúng → bất biến giữ.

Kết luận:
  - Thuật toán dừng: sau tối đa n-1 lượt, toàn mảng đúng vị trí.
  - Tính đúng đắn: bất biến đảm bảo sau n-1 lượt mảng đã sắp xếp.
  - Early-exit: nếu 1 lượt không có swap → mảng đã đúng → dừng sớm.
"""

du_lieu_chung = [5, 3, 8, 1, 9, 2, 7, 4]

Noidung = {
    '19': {
        'ten': 'BÀI 19: SỐ LƯỢT TỐI THIỂU (MẢNG GẦN SẮP XẾP)',
        'du_lieu': {'a': [1, 2, 3, 5, 4]},
        'mong_doi': 1,
        'ham': lambda d: luot_toi_thieu(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"Sau sort: {kq[1]}\n"
            f"=> Số lượt cần: {kq[0]}\n"
            f"   (phần tử 4 phải đi ngược 1 bước → 1 lượt)"
        ),
    },
    '20': {
        'ten': 'BÀI 20: ĐẾM NGHỊCH THẾ O(n log n) - MERGE SORT',
        'du_lieu': {'a': [5, 3, 8, 1, 9, 2, 7, 4]},
        'mong_doi': None,
        'ham': lambda d: dem_nghich_the_nhanh(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']} (n={len(d['a'])})\n"
            f"=> Số nghịch thế (= số swap bubble sort): {kq}\n"
            f"   Đếm bằng merge sort O(n log n), không mô phỏng O(n²)"
        ),
    },
    '21': {
        'ten': 'BÀI 21: SẮP XẾP ỔN ĐỊNH THEO CẶP (KEY, VALUE)',
        'du_lieu': {'a': [(3, 'x'), (1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')]},
        'mong_doi': [(1, 'a'), (1, 'c'), (2, 'b'), (2, 'd'), (3, 'x')],
        'ham': lambda d: (
            lambda b: (
                [b.__setitem__(slice(None), sorted(b, key=lambda t: t[0])), None][1],
                b
            )
        )([t for t in d['a']]),
        'ham': lambda d: __import__('functools').reduce(
            lambda acc, _: acc,
            [],
            (lambda b: [
                [b.__setitem__(j, b[j+1]) or b.__setitem__(j+1, b[j]) for j in range(len(b)-1) if b[j][0] > b[j+1][0]],
                b
            ][-1])([t for t in d['a']])
        ),
        'ham': lambda d: _on_dinh_cap(d['a']),
        'format': lambda d, kq: (
            f"Gốc:       {d['a']}\n"
            f"Bubble:    {kq}\n"
            f"=> (1,'a') trước (1,'c'): {kq.index((1,'a')) < kq.index((1,'c'))} → ổn định"
        ),
    },
    '22': {
        'ten': 'BÀI 22: MẢNG GẦN SẮP XẾP VỚI ĐỘ LỆCH ≤ K',
        'du_lieu': {'a': [1, 3, 2, 4, 6, 5, 7, 8], 'k': 1},
        'mong_doi': None,
        'ham': lambda d: gan_sort_ok(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']} (n={len(d['a'])}, k={d['k']})\n"
            f"=> Số lượt thực tế: {kq[0]}\n"
            f"   n*k = {len(d['a'])*d['k']} | Thỏa O(n·k): {kq[1]}"
        ),
    },
    '23': {
        'ten': 'BÀI 23: PHÂN TÍCH & SO SÁNH HIỆU NĂNG',
        'du_lieu': {'a': du_lieu_chung},
        'mong_doi': None,
        'ham': lambda d: do_hieu_nang(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc (n={kq['n']}): {d['a']}\n\n"
            f"{'Loại dữ liệu':<20} {'So sánh':>10} {'Swap':>8}\n"
            f"{'-'*40}\n"
            f"{'Ngẫu nhiên':<20} {kq['ngau_nhien'][0]:>10} {kq['ngau_nhien'][1]:>8}\n"
            f"{'Đã sắp xếp':<20} {kq['da_sort'][0]:>10} {kq['da_sort'][1]:>8}\n"
            f"{'Sắp xếp ngược':<20} {kq['nguoc'][0]:>10} {kq['nguoc'][1]:>8}\n"
            f"{'-'*40}\n"
            f"Lý thuyết tốt nhất  O(n)  : {kq['ly_thuyet_tot']} so sánh\n"
            f"Lý thuyết xấu nhất  O(n²) : {kq['ly_thuyet_xau']} so sánh"
        ),
    },
    '24': {
        'ten': 'BÀI 24: KHÔI PHỤC SỐ LƯỢT TỪ HAI TRẠNG THÁI',
        'du_lieu': {'dau': [4, 3, 2, 1], 'sau': [3, 2, 1, 4]},
        'mong_doi': 1,
        'ham': lambda d: khoi_phuc_luot(d['dau'], d['sau']),
        'format': lambda d, kq: (
            f"Trạng thái đầu: {d['dau']}\n"
            f"Trạng thái sau: {d['sau']}\n"
            f"=> Đã thực hiện ít nhất {kq} lượt"
        ),
    },
    '25': {
        'ten': 'BÀI 25: CHỨNG MINH TÍNH ĐÚNG ĐẮN (LOOP INVARIANT)',
        'du_lieu': {},
        'mong_doi': None,
        'ham': lambda d: BAT_BIEN,
        'format': lambda d, kq: kq,
    },
}

def _on_dinh_cap(a):
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j][0] > b[j + 1][0]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

Noidung['21']['ham'] = lambda d: _on_dinh_cap(d['a'])

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    if cfg['mong_doi'] is not None:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")

if __name__ == '__main__':
    while True:
        print("\n" + "*"*50)
        print(" CHỌN BÀI (19-25) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
        print("*"*50)
        for k, v in Noidung.items():
            print(f" {k}. {v['ten']}")
        chon = input("\nLựa chọn: ").strip()
        if chon == '0':
            print("Đã thoát.")
            break
        elif chon == 'all':
            for cfg in Noidung.values():
                chay_bai(cfg)
        elif chon in Noidung:
            chay_bai(Noidung[chon])
        else:
            print("Không hợp lệ, thử lại!")
