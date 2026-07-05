from typing import List, Dict, Any, Tuple
from collections import Counter

# --- Bài 1: Hàm băm modulo cho số nguyên ---
def bai_1_modulo(du_lieu: Dict[str, Any]) -> List[int]:
    m = du_lieu['m']
    return [k % m for k in du_lieu['keys']]

# --- Bài 2: Hàm băm chuỗi (Tổng mã ASCII) ---
def bai_2_ascii_hash(du_lieu: Dict[str, Any]) -> Dict[str, int]:
    m = du_lieu['m']
    kq = {}
    for s in du_lieu['strings']:
        # Tính tổng mã ASCII của từng ký tự
        tong = sum(ord(c) for c in s)
        kq[s] = tong % m
    return kq

# --- Bài 3: Hàm băm đa thức (Polynomial Hash) ---
def bai_3_polynomial_hash(du_lieu: Dict[str, Any]) -> Dict[str, int]:
    p = du_lieu['p'] # Base (thường là 31, 37)
    m = du_lieu['m'] # Số nguyên tố lớn
    kq = {}
    for s in du_lieu['strings']:
        hash_val = 0
        p_pow = 1
        # Tính hash: (s[0]*p^0 + s[1]*p^1 + ... + s[n-1]*p^(n-1)) % m
        for char in s:
            hash_val = (hash_val + (ord(char) - ord('a') + 1) * p_pow) % m
            p_pow = (p_pow * p) % m
        kq[s] = hash_val
    return kq

# --- Bài 4: Đếm va chạm của một hàm băm ---
def bai_4_dem_va_cham(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    m = du_lieu['m']
    buckets = {}
    so_va_cham = 0
    
    for s in du_lieu['keys']:
        h = sum(ord(c) for c in s) % m
        if h in buckets:
            buckets[h].append(s)
            so_va_cham += 1
        else:
            buckets[h] = [s]
            
    return {
        'buckets': buckets,
        'so_va_cham': so_va_cham
    }

# --- Bài 5: Vì sao chọn m là số nguyên tố ---
def bai_5_so_nguyen_to(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    keys = du_lieu['keys']
    m_hop_so = du_lieu['m_hop_so']     # VD: 16 (2^4)
    m_nguyen_to = du_lieu['m_nguyen_to'] # VD: 17
    
    dist_hop_so = Counter([k % m_hop_so for k in keys])
    dist_nguyen_to = Counter([k % m_nguyen_to for k in keys])
    
    return {
        'dist_hop_so': dict(dist_hop_so),
        'dist_nguyen_to': dict(dist_nguyen_to)
    }

# --- Bài 6: Rolling Hash & Rabin-Karp ---
def bai_6_rabin_karp(du_lieu: Dict[str, Any]) -> List[int]:
    text = du_lieu['text']
    pattern = du_lieu['pattern']
    n, m = len(text), len(pattern)
    if m == 0 or n < m: return []
    
    p = 31
    mod = 10**9 + 9
    
    # Precompute p_pow
    p_pow = [1] * max(n, m)
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % mod
        
    # Tính hash cho pattern
    h_p = 0
    for i in range(m):
        h_p = (h_p + (ord(pattern[i]) - ord('a') + 1) * p_pow[i]) % mod
        
    # Tính prefix hash cho text
    h_t = [0] * (n + 1)
    for i in range(n):
        h_t[i+1] = (h_t[i] + (ord(text[i]) - ord('a') + 1) * p_pow[i]) % mod
        
    matches = []
    # Duyệt cửa sổ trượt (Rolling Hash)
    for i in range(n - m + 1):
        # Hash của đoạn text[i : i+m]
        cur_h = (h_t[i+m] + mod - h_t[i]) % mod
        # So sánh hash (nhân p_pow để bù bậc)
        if cur_h == (h_p * p_pow[i]) % mod:
            matches.append(i)
            
    return matches

# --- Bài 7: Hàm băm cho Tuple/Cặp ---
def bai_7_tuple_hash(du_lieu: Dict[str, Any]) -> Dict[Tuple[int, int], int]:
    # Sử dụng nguyên lý boost::hash_combine
    # seed ^= hash_val + 0x9e3779b9 + (seed << 6) + (seed >> 2)
    def hash_combine(a: int, b: int) -> int:
        seed = hash(a)
        seed ^= hash(b) + 0x9e3779b9 + (seed << 6) + (seed >> 2)
        return seed

    kq = {}
    for tup in du_lieu['tuples']:
        kq[tup] = hash_combine(tup[0], tup[1])
    return kq

Noidung = {
    '1': {
        'ten': 'BÀI 1: HÀM BĂM MODULO CHO SỐ NGUYÊN',
        'du_lieu': {'keys': [37, 45, 12, 10, 89], 'm': 10},
        'mong_doi': [7, 5, 2, 0, 9],
        'ham': lambda d: bai_1_modulo(d),
        'format': lambda d, kq: f"Khóa đầu vào: {d['keys']} (m={d['m']})\nDanh sách chỉ số bucket: {kq}"
    },
    '2': {
        'ten': 'BÀI 2: HÀM BĂM CHUỖI (TỔNG MÃ KÝ TỰ)',
        'du_lieu': {'strings': ['abc', 'cba', 'bca', 'xyz'], 'm': 100},
        'mong_doi': {'abc': 94, 'cba': 94, 'bca': 94, 'xyz': 63},
        'ham': lambda d: bai_2_ascii_hash(d),
        'format': lambda d, kq: (
            f"Kết quả băm:\n" + "\n".join([f"  '{k}' -> {v}" for k, v in kq.items()]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - Các chuỗi 'abc', 'cba', 'bca' đều cho cùng một giá trị băm.\n"
            f"    - Nhược điểm chí mạng: Tổng ASCII không quan tâm đến THỨ TỰ ký tự.\n"
            f"    - Dễ gây ra va chạm lớn với các chuỗi đảo chữ (Anagrams)."
        )
    },
    '3': {
        'ten': 'BÀI 3: HÀM BĂM ĐA THỨC (POLYNOMIAL HASH)',
        'du_lieu': {'strings': ['abc', 'cba'], 'p': 31, 'm': 10**9 + 9},
        'mong_doi': 'So khớp thủ công, giá trị sẽ khác nhau',
        'ham': lambda d: bai_3_polynomial_hash(d),
        'format': lambda d, kq: (
            f"Kết quả băm đa thức (p={d['p']}, m={d['m']}):\n" + 
            "\n".join([f"  '{k}' -> {v}" for k, v in kq.items()]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - Bằng cách nhân mã ASCII với p^i (trọng số theo vị trí i),\n"
            f"      'abc' và 'cba' đã cho ra mã băm hoàn toàn khác biệt.\n"
            f"    - p=31 là số nguyên tố phổ biến dùng cho bộ ký tự chữ cái.\n"
            f"    - m là số nguyên tố lớn để tránh tràn số và giảm đụng độ."
        )
    },
    '4': {
        'ten': 'BÀI 4: ĐẾM VA CHẠM CỦA HÀM BĂM',
        'du_lieu': {'keys': ['cat', 'tac', 'act', 'dog', 'god'], 'm': 10},
        'mong_doi': {'so_va_cham': 3},
        'ham': lambda d: bai_4_dem_va_cham(d),
        'format': lambda d, kq: (
            f"Sử dụng hàm tổng ASCII (như bài 2) trên tập từ: {d['keys']}\n"
            f"Phân bố Bucket:\n" + "\n".join([f"  Index {k}: {v}" for k, v in kq['buckets'].items()]) +
            f"\nTổng số lần va chạm: {kq['so_va_cham']}"
        )
    },
    '5': {
        'ten': 'BÀI 5: THỰC NGHIỆM VÌ SAO m LÀ SỐ NGUYÊN TỐ',
        'du_lieu': {
            'keys': [16, 32, 48, 64, 80, 96, 112, 128], # Các bội số của 16
            'm_hop_so': 16,
            'm_nguyen_to': 17
        },
        'mong_doi': 'So sánh mô phỏng',
        'ham': lambda d: bai_5_so_nguyen_to(d),
        'format': lambda d, kq: (
            f"Khóa đầu vào (Đều là bội số của 16): {d['keys']}\n\n"
            f"[1] Phân bố khi m = 16 (Hợp số / Lũy thừa của 2):\n  {kq['dist_hop_so']}\n"
            f"[2] Phân bố khi m = 17 (Số nguyên tố):\n  {kq['dist_nguyen_to']}\n\n"
            f"[*] NHẬN XÉT:\n"
            f"    - Nếu m=16, TOÀN BỘ dữ liệu dồn về index 0. Bảng băm suy biến thành mảng 1 chiều $O(n)$.\n"
            f"    - Nếu m=17, dữ liệu được rải đều đặn qua các index khác nhau.\n"
            f"    - Chọn m là số nguyên tố giúp phá vỡ tính tuần hoàn nếu dữ liệu đầu vào có quy luật (như bội số chung)."
        )
    },
    '6': {
        'ten': 'BÀI 6: ROLLING HASH & RABIN-KARP',
        'du_lieu': {'text': 'zabcdabc', 'pattern': 'abc'},
        'mong_doi': [1, 5],
        'ham': lambda d: bai_6_rabin_karp(d),
        'format': lambda d, kq: (
            f"Văn bản: '{d['text']}'\n"
            f"Chuỗi mẫu cần tìm: '{d['pattern']}'\n"
            f"Kết quả các vị trí xuất hiện (Index): {kq}\n"
            f"[*] Phương pháp Rolling Hash cho phép tính hash cửa sổ tiếp theo trong $O(1)$ thay vì $O(m)$."
        )
    },
    '7': {
        'ten': 'BÀI 7: HÀM BĂM CHO CẶP (TUPLE)',
        'du_lieu': {'tuples': [(1, 2), (2, 1), (10, 10)]},
        'mong_doi': 'So sánh tuple hash',
        'ham': lambda d: bai_7_tuple_hash(d),
        'format': lambda d, kq: (
            f"Mã băm kết hợp (Sử dụng nguyên lý boost::hash_combine):\n" +
            "\n".join([f"  Tuple {k} -> {v}" for k, v in kq.items()]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - Hàm hash_combine dùng phép dịch bit (<<, >>) và XOR mạng nhện.\n"
            f"    - Việc này đảm bảo Tuple (1, 2) và (2, 1) cho ra mã băm khác biệt, khắc phục lỗi đối xứng."
        )
    }
}

def chay_bai(cfg, check_strict=True):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    # Bỏ strict check cho bài 3, 5, 7 vì giá trị băm hash() nội bộ / ngẫu nhiên
    is_strict = check_strict and isinstance(cfg['mong_doi'], (list, dict))
    
    if is_strict:
        print(f"\nKết quả mong đợi:\n{cfg['mong_doi']}")
        # Xử lý bài 4 so sánh nested dict 1 key đặc biệt
        if 'so_va_cham' in cfg['mong_doi']:
            if kq['so_va_cham'] == cfg['mong_doi']['so_va_cham']:
                print("\nTrạng thái: THÀNH CÔNG")
            else:
                print("\nTrạng thái: THẤT BẠI")
        elif kq == cfg['mong_doi']:
            print("\nTrạng thái: THÀNH CÔNG")
        else:
            print("\nTrạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 3 (PHẦN B: BÀI 1 -> BÀI 7)")
            print(" CHỌN BÀI (1-7) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            for k, v in sorted(Noidung.items()):
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in sorted(Noidung.keys()):
                    chay_bai(Noidung[k])
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass
