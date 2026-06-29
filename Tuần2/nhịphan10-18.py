from typing import List
import math

def tim_mang_xoay(a: List[int], x: int) -> int:
    trai, phai = 0, len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return giua
        if a[trai] <= a[giua]:
            if a[trai] <= x < a[giua]:
                phai = giua - 1
            else:
                trai = giua + 1
        else:
            if a[giua] < x <= a[phai]:
                trai = giua + 1
            else:
                phai = giua - 1
    return -1

def nho_nhat_xoay(a: List[int]) -> int:
    trai, phai = 0, len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] > a[phai]:
            trai = giua + 1
        else:
            phai = giua
    return a[trai]

def tim_dinh(a: List[int]) -> int:
    trai, phai = 0, len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] < a[giua + 1]:
            trai = giua + 1
        else:
            phai = giua
    return trai

def don_le_mang_doi(a: List[int]) -> int:
    trai, phai = 0, len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        if giua % 2 == 1:
            giua -= 1
        if a[giua] == a[giua + 1]:
            trai = giua + 2
        else:
            phai = giua
    return a[trai]

def tim_ma_tran(M: List[List[int]], x: int) -> bool:
    if not M or not M[0]:
        return False
    hang, cot = len(M), len(M[0])
    trai, phai = 0, hang * cot - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        gt = M[giua // cot][giua % cot]
        if gt == x:
            return True
        elif gt < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return False

def k_gan_nhat(a: List[int], k: int, x: int) -> List[int]:
    trai, phai = 0, len(a) - k
    while trai < phai:
        giua = (trai + phai) // 2
        if x - a[giua] > a[giua + k] - x:
            trai = giua + 1
        else:
            phai = giua
    return a[trai:trai + k]

def koko_an_chuoi(dong: List[int], h: int) -> int:
    def co_the(toc_do):
        return sum(math.ceil(d / toc_do) for d in dong) <= h
    trai, phai = 1, max(dong)
    while trai < phai:
        giua = (trai + phai) // 2
        if co_the(giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

def suc_chua_tau(w: List[int], ngay: int) -> int:
    def co_the(suc):
        so_ngay, tai_hien_tai = 1, 0
        for kien in w:
            if tai_hien_tai + kien > suc:
                so_ngay += 1
                tai_hien_tai = 0
            tai_hien_tai += kien
        return so_ngay <= ngay
    trai, phai = max(w), sum(w)
    while trai < phai:
        giua = (trai + phai) // 2
        if co_the(giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

def k_thieu(a: List[int], k: int) -> int:
    trai, phai = 0, len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        thieu = a[giua] - (giua + 1)
        if thieu < k:
            trai = giua + 1
        else:
            phai = giua - 1
    return trai + k

Noidung = {
    '10': {
        'ten': 'BÀI 10: TÌM TRONG MẢNG XOAY',
        'du_lieu': {'a': [4, 5, 6, 7, 0, 1, 2], 'x': 0},
        'mong_doi': 4,
        'ham': lambda d: tim_mang_xoay(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng xoay: {d['a']}, x={d['x']}\n"
            f"=> {'Tìm thấy tại chỉ số ' + str(kq) if kq != -1 else 'Không tìm thấy'}"
        ),
    },
    '11': {
        'ten': 'BÀI 11: PHẦN TỬ NHỎ NHẤT TRONG MẢNG XOAY',
        'du_lieu': {'a': [3, 4, 5, 1, 2]},
        'mong_doi': 1,
        'ham': lambda d: nho_nhat_xoay(d['a']),
        'format': lambda d, kq: (
            f"Mảng xoay: {d['a']}\n=> Phần tử nhỏ nhất: {kq}"
        ),
    },
    '12': {
        'ten': 'BÀI 12: TÌM ĐỈNH (PEAK ELEMENT)',
        'du_lieu': {'a': [1, 2, 3, 1]},
        'mong_doi': 2,
        'ham': lambda d: tim_dinh(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n=> Chỉ số đỉnh: {kq} (giá trị: {d['a'][kq]})"
        ),
    },
    '13': {
        'ten': 'BÀI 13: PHẦN TỬ ĐƠN LẺ TRONG MẢNG ĐÔI',
        'du_lieu': {'a': [1, 1, 2, 3, 3, 4, 4]},
        'mong_doi': 2,
        'ham': lambda d: don_le_mang_doi(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n=> Phần tử đơn lẻ: {kq}"
        ),
    },
    '14': {
        'ten': 'BÀI 14: TÌM TRONG MA TRẬN 2D',
        'du_lieu': {'M': [[1, 3, 5], [7, 9, 11]], 'x': 9},
        'mong_doi': True,
        'ham': lambda d: tim_ma_tran(d['M'], d['x']),
        'format': lambda d, kq: (
            f"Ma trận: {d['M']}, x={d['x']}\n"
            f"=> {'Tìm thấy' if kq else 'Không tìm thấy'}"
        ),
    },
    '15': {
        'ten': 'BÀI 15: K PHẦN TỬ GẦN NHẤT',
        'du_lieu': {'a': [1, 2, 3, 4, 5], 'k': 4, 'x': 3},
        'mong_doi': [1, 2, 3, 4],
        'ham': lambda d: k_gan_nhat(d['a'], d['k'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, k={d['k']}, x={d['x']}\n"
            f"=> {d['k']} phần tử gần nhất: {kq}"
        ),
    },
    '16': {
        'ten': 'BÀI 16: KOKO ĂN CHUỐI',
        'du_lieu': {'dong': [3, 6, 7, 11], 'h': 8},
        'mong_doi': 4,
        'ham': lambda d: koko_an_chuoi(d['dong'], d['h']),
        'format': lambda d, kq: (
            f"Các đống: {d['dong']}, h={d['h']} giờ\n"
            f"=> Tốc độ ăn nhỏ nhất: {kq} quả/giờ"
        ),
    },
    '17': {
        'ten': 'BÀI 17: SỨC CHỨA TÀU HÀNG',
        'du_lieu': {'w': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'ngay': 5},
        'mong_doi': 15,
        'ham': lambda d: suc_chua_tau(d['w'], d['ngay']),
        'format': lambda d, kq: (
            f"Trọng lượng: {d['w']}, D={d['ngay']} ngày\n"
            f"=> Sức chứa tàu nhỏ nhất: {kq}"
        ),
    },
    '18': {
        'ten': 'BÀI 18: PHẦN TỬ THỨ K BỊ THIẾU',
        'du_lieu': {'a': [2, 3, 4, 7, 11], 'k': 5},
        'mong_doi': 9,
        'ham': lambda d: k_thieu(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, k={d['k']}\n"
            f"=> Số nguyên dương thứ {d['k']} bị thiếu: {kq}"
        ),
    },
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    print(f"Kết quả mong đợi: {cfg['mong_doi']}")

if __name__ == '__main__':
    while True:
        print("\n" + "*"*50)
        print(" CHỌN BÀI (10-18) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
