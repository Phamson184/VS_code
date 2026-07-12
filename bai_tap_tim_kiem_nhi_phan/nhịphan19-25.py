from typing import List

def bo_vao_chuong(vi_tri: List[int], bo: int) -> int:
    vi_tri = sorted(vi_tri)
    def co_the(kc_min):
        dem, cuoi = 1, vi_tri[0]
        for v in vi_tri[1:]:
            if v - cuoi >= kc_min:
                dem += 1
                cuoi = v
        return dem >= bo
    trai, phai = 1, vi_tri[-1] - vi_tri[0]
    while trai < phai:
        giua = (trai + phai + 1) // 2
        if co_the(giua):
            trai = giua
        else:
            phai = giua - 1
    return trai

def chia_sach(trang: List[int], hoc_sinh: int) -> int:
    def co_the(trang_max):
        dem, hien_tai = 1, 0
        for t in trang:
            if hien_tai + t > trang_max:
                dem += 1
                hien_tai = 0
            hien_tai += t
        return dem <= hoc_sinh
    trai, phai = max(trang), sum(trang)
    while trai < phai:
        giua = (trai + phai) // 2
        if co_the(giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

def chia_mang_tong_lon_nhat(a: List[int], k: int) -> int:
    def co_the(tong_max):
        dem, hien_tai = 1, 0
        for v in a:
            if hien_tai + v > tong_max:
                dem += 1
                hien_tai = 0
            hien_tai += v
        return dem <= k
    trai, phai = max(a), sum(a)
    while trai < phai:
        giua = (trai + phai) // 2
        if co_the(giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

def median_hai_mang(a: List[int], b: List[int]) -> float:
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    trai, phai = 0, m
    while trai <= phai:
        i = (trai + phai) // 2
        j = (m + n + 1) // 2 - i
        trai_a = float('-inf') if i == 0 else a[i - 1]
        phai_a = float('inf') if i == m else a[i]
        trai_b = float('-inf') if j == 0 else b[j - 1]
        phai_b = float('inf') if j == n else b[j]
        if trai_a <= phai_b and trai_b <= phai_a:
            if (m + n) % 2 == 0:
                return (max(trai_a, trai_b) + min(phai_a, phai_b)) / 2
            return float(max(trai_a, trai_b))
        elif trai_a > phai_b:
            phai = i - 1
        else:
            trai = i + 1
    return 0.0

def k_nho_ma_tran(M: List[List[int]], k: int) -> int:
    n = len(M)
    def dem_nho_hon(gt):
        dem, hang = 0, n - 1
        for cot in range(n):
            while hang >= 0 and M[hang][cot] > gt:
                hang -= 1
            dem += hang + 1
        return dem
    trai, phai = M[0][0], M[n-1][n-1]
    while trai < phai:
        giua = (trai + phai) // 2
        if dem_nho_hon(giua) < k:
            trai = giua + 1
        else:
            phai = giua
    return trai

def tram_xang(vi_tri: List[int], k: int) -> float:
    n = len(vi_tri)
    khoang = [vi_tri[i+1] - vi_tri[i] for i in range(n-1)]
    def co_the(kc_max):
        them = sum(int(kc / kc_max - 1e-9) for kc in khoang)
        return them <= k
    trai, phai = 0.0, max(khoang)
    for _ in range(100):
        giua = (trai + phai) / 2
        if co_the(giua):
            phai = giua
        else:
            trai = giua
    return phai

def luc_tu_nam_cham(vi_tri: List[int], m: int) -> int:
    vi_tri = sorted(vi_tri)
    def co_the(luc_min):
        dem, cuoi = 1, vi_tri[0]
        for v in vi_tri[1:]:
            if v - cuoi >= luc_min:
                dem += 1
                cuoi = v
        return dem >= m
    trai, phai = 1, vi_tri[-1] - vi_tri[0]
    while trai < phai:
        giua = (trai + phai + 1) // 2
        if co_the(giua):
            trai = giua
        else:
            phai = giua - 1
    return trai

Noidung = {
    '19': {
        'ten': 'BÀI 19: CHIA BÒ VÀO CHUỒNG (AGGRESSIVE COWS)',
        'du_lieu': {'vi_tri': [1, 2, 4, 8, 9], 'bo': 3},
        'mong_doi': 3,
        'ham': lambda d: bo_vao_chuong(d['vi_tri'], d['bo']),
        'format': lambda d, kq: (
            f"Vị trí chuồng: {d['vi_tri']}, số bò: {d['bo']}\n"
            f"=> Khoảng cách nhỏ nhất lớn nhất: {kq}"
        ),
    },
    '20': {
        'ten': 'BÀI 20: CHIA SÁCH CHO HỌC SINH',
        'du_lieu': {'trang': [12, 34, 67, 90], 'hoc_sinh': 2},
        'mong_doi': 113,
        'ham': lambda d: chia_sach(d['trang'], d['hoc_sinh']),
        'format': lambda d, kq: (
            f"Số trang: {d['trang']}, học sinh: {d['hoc_sinh']}\n"
            f"=> Số trang tối đa nhỏ nhất: {kq}"
        ),
    },
    '21': {
        'ten': 'BÀI 21: CHIA MẢNG TỔNG LỚN NHẤT NHỎ NHẤT',
        'du_lieu': {'a': [7, 2, 5, 10, 8], 'k': 2},
        'mong_doi': 18,
        'ham': lambda d: chia_mang_tong_lon_nhat(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, k={d['k']} đoạn\n"
            f"=> Tổng lớn nhất nhỏ nhất: {kq}"
        ),
    },
    '22': {
        'ten': 'BÀI 22: MEDIAN CỦA HAI MẢNG ĐÃ SẮP XẾP',
        'du_lieu': {'a': [1, 2], 'b': [3, 4]},
        'mong_doi': 2.5,
        'ham': lambda d: median_hai_mang(d['a'], d['b']),
        'format': lambda d, kq: (
            f"a={d['a']}, b={d['b']}\n"
            f"=> Trung vị: {kq}"
        ),
    },
    '23': {
        'ten': 'BÀI 23: PHẦN TỬ NHỎ THỨ K TRONG MA TRẬN',
        'du_lieu': {
            'M': [[1, 5, 9], [10, 11, 13], [12, 13, 15]],
            'k': 8
        },
        'mong_doi': 13,
        'ham': lambda d: k_nho_ma_tran(d['M'], d['k']),
        'format': lambda d, kq: (
            f"Ma trận: {d['M']}, k={d['k']}\n"
            f"=> Phần tử nhỏ thứ {d['k']}: {kq}"
        ),
    },
    '24': {
        'ten': 'BÀI 24: GIẢM THIỂU KHOẢNG CÁCH LỚN NHẤT GIỮA TRẠM XĂNG',
        'du_lieu': {
            'vi_tri': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'k': 9
        },
        'mong_doi': 0.5,
        'ham': lambda d: tram_xang(d['vi_tri'], d['k']),
        'format': lambda d, kq: (
            f"Trạm: {d['vi_tri']}, thêm k={d['k']} trạm\n"
            f"=> Khoảng cách lớn nhất nhỏ nhất: {kq:.6f}"
        ),
    },
    '25': {
        'ten': 'BÀI 25: LỰC TỪ GIỮA CÁC NAM CHÂM',
        'du_lieu': {'vi_tri': [1, 2, 3, 4, 7], 'm': 3},
        'mong_doi': 3,
        'ham': lambda d: luc_tu_nam_cham(d['vi_tri'], d['m']),
        'format': lambda d, kq: (
            f"Vị trí giỏ: {d['vi_tri']}, số nam châm: {d['m']}\n"
            f"=> Lực từ nhỏ nhất lớn nhất: {kq}"
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
