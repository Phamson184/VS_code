from typing import List, Dict, Any, Set
import math
import random

# --- Bài 8: So sánh chất lượng phân bố (Chi-square) ---
def bai_8_chi_square(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    keys = du_lieu['keys']
    m = du_lieu['m']
    n = len(keys)
    
    # Đếm phân bố
    buckets = {i: 0 for i in range(m)}
    for k in keys:
        buckets[k % m] += 1
        
    # Kỳ vọng mỗi bucket
    expected = n / m
    
    # Tính Chi-square: sum((O - E)^2 / E)
    chi_square = sum((buckets[i] - expected)**2 / expected for i in range(m))
    
    return {
        'buckets': buckets,
        'chi_square': round(chi_square, 2)
    }

# --- Bài 9: Băm phổ quát (Universal Hashing) ---
def bai_9_universal_hashing(du_lieu: Dict[str, Any]) -> List[int]:
    keys = du_lieu['keys']
    p = du_lieu['p'] # Số nguyên tố lớn hơn mọi khóa
    m = du_lieu['m']
    
    # Sinh ngẫu nhiên a (1 -> p-1) và b (0 -> p-1)
    # Để test có kết quả cố định, bài này dùng giá trị cứng từ du_lieu
    a = du_lieu['a']
    b = du_lieu['b']
    
    # h(k) = ((a*k + b) % p) % m
    return [((a * k + b) % p) % m for k in keys]

# --- Bài 10: Phương pháp nhân (Multiplication Method) ---
def bai_10_multiplication(du_lieu: Dict[str, Any]) -> List[int]:
    keys = du_lieu['keys']
    m = du_lieu['m']
    A = du_lieu['A'] # Thường là (sqrt(5)-1)/2
    
    # h(k) = floor(m * (k * A mod 1))
    kq = []
    for k in keys:
        phan_thap_phan = (k * A) % 1
        kq.append(math.floor(m * phan_thap_phan))
    return kq

# --- Bài 11: Hàm băm độc lập thứ tự ---
def bai_11_order_independent(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    set1 = du_lieu['set1']
    set2 = du_lieu['set2']
    
    # Dùng phép cộng (hoặc XOR) các giá trị băm để không phụ thuộc thứ tự
    hash1 = sum(hash(x) for x in set1)
    hash2 = sum(hash(x) for x in set2)
    
    return {
        'hash1': hash1,
        'hash2': hash2,
        'is_equal': hash1 == hash2
    }

# --- Bài 12: Tấn công Hash Flooding ---
def bai_12_hash_flooding(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    m = du_lieu['m']
    normal_keys = du_lieu['normal_keys']
    malicious_keys = du_lieu['malicious_keys'] # Kẻ tấn công chọn toàn bội số của m
    
    def simulate(keys):
        buckets = {}
        max_collisions = 0
        for k in keys:
            h = k % m
            buckets[h] = buckets.get(h, 0) + 1
            max_collisions = max(max_collisions, buckets[h])
        return max_collisions
        
    return {
        'normal_max_collisions': simulate(normal_keys),
        'malicious_max_collisions': simulate(malicious_keys)
    }

# --- Bài 13: Rolling Hash 2 Chiều (Minh họa đơn giản) ---
def bai_13_2d_hash(du_lieu: Dict[str, Any]) -> int:
    # Để giữ code ngắn gọn mô phỏng, ta băm từng dòng rồi gộp lại
    matrix = du_lieu['matrix']
    
    def hash_row(row: List[int]) -> int:
        p = 31
        m = 10**9 + 9
        h = 0
        for val in row:
            h = (h * p + val) % m
        return h
        
    total_hash = 0
    p_col = 37
    m = 10**9 + 9
    for row in matrix:
        total_hash = (total_hash * p_col + hash_row(row)) % m
        
    return total_hash

# --- Bài 14: Bloom Filter ---
class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [False] * size
        
    def _hashes(self, item: str) -> List[int]:
        # Dùng seed khác nhau để giả lập nhiều hàm băm
        return [hash(item + str(i)) % self.size for i in range(self.num_hashes)]
        
    def add(self, item: str):
        for h in self._hashes(item):
            self.bit_array[h] = True
            
    def check(self, item: str) -> bool:
        for h in self._hashes(item):
            if not self.bit_array[h]:
                return False # Chắc chắn không có
        return True # Có thể có (Dương tính giả)

def bai_14_bloom_filter(du_lieu: Dict[str, Any]) -> Dict[str, bool]:
    bf = BloomFilter(size=du_lieu['m'], num_hashes=du_lieu['k'])
    for item in du_lieu['adds']:
        bf.add(item)
        
    kq = {}
    for item in du_lieu['checks']:
        kq[item] = bf.check(item)
    return kq

# --- Bài 15: MinHash (Ước lượng Jaccard) ---
def bai_15_minhash(du_lieu: Dict[str, Any]) -> Dict[str, float]:
    set_a = set(du_lieu['set_a'])
    set_b = set(du_lieu['set_b'])
    num_hashes = du_lieu['num_hashes']
    
    # Jaccard thực tế
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    true_jaccard = intersection / union if union != 0 else 1.0
    
    # MinHash giả lập
    # Tạo danh sách các cặp (a, b) cho hàm băm vạn năng: h(x) = (ax + b) % p
    p = 104729
    hash_funcs = [(random.randint(1, p-1), random.randint(0, p-1)) for _ in range(num_hashes)]
    
    def get_minhash(s: Set[int], a: int, b: int) -> int:
        return min(((a * x + b) % p) for x in s)
        
    matches = 0
    for a, b in hash_funcs:
        min_a = get_minhash(set_a, a, b)
        min_b = get_minhash(set_b, a, b)
        if min_a == min_b:
            matches += 1
            
    est_jaccard = matches / num_hashes
    
    return {
        'true_jaccard': round(true_jaccard, 3),
        'est_jaccard': round(est_jaccard, 3)
    }

Noidung = {
    '8': {
        'ten': 'BÀI 8: SO SÁNH CHẤT LƯỢNG PHÂN BỐ (CHI-SQUARE)',
        'du_lieu': {'keys': [12, 44, 13, 88, 23, 94, 11, 39, 20, 16], 'm': 5},
        'mong_doi': 'So sánh chỉ số',
        'ham': lambda d: bai_8_chi_square(d),
        'format': lambda d, kq: (
            f"Số lượng khóa n = {len(d['keys'])}, số bucket m = {d['m']} (Kỳ vọng: {len(d['keys'])/d['m']} khóa/bucket)\n"
            f"Phân bố thực tế: {kq['buckets']}\n"
            f"Chỉ số Chi-square: {kq['chi_square']}\n"
            f"[*] Chi-square càng nhỏ, phân bố càng đều (Hàm băm càng tốt)."
        )
    },
    '9': {
        'ten': 'BÀI 9: BĂM PHỔ QUÁT (UNIVERSAL HASHING)',
        'du_lieu': {'keys': [10, 22, 31, 4, 15], 'p': 97, 'm': 10, 'a': 3, 'b': 4},
        'mong_doi': [4, 0, 0, 6, 9], # ((3*10+4)%97)%10 = 34 % 10 = 4...
        'ham': lambda d: bai_9_universal_hashing(d),
        'format': lambda d, kq: (
            f"Công thức: h(k) = ((a*k + b) % p) % m\n"
            f"Tham số: a={d['a']}, b={d['b']}, p={d['p']}, m={d['m']}\n"
            f"Khóa đầu vào: {d['keys']}\nKết quả băm: {kq}\n"
            f"[*] Bằng cách random a và b lúc khởi tạo, ta chặn đứng kẻ tấn công đoán trước quy luật."
        )
    },
    '10': {
        'ten': 'BÀI 10: PHƯƠNG PHÁP NHÂN (MULTIPLICATION METHOD)',
        'du_lieu': {'keys': [12345, 67890], 'm': 1000, 'A': 0.618033},
        'mong_doi': [617, 397],
        'ham': lambda d: bai_10_multiplication(d),
        'format': lambda d, kq: f"Khóa: {d['keys']} | m={d['m']} | A≈{d['A']}\nIndex thu được: {kq}"
    },
    '11': {
        'ten': 'BÀI 11: HÀM BĂM ĐỘC LẬP THỨ TỰ',
        'du_lieu': {'set1': [1, 2, 3], 'set2': [3, 1, 2]},
        'mong_doi': {'is_equal': True},
        'ham': lambda d: bai_11_order_independent(d),
        'format': lambda d, kq: (
            f"Tập 1: {d['set1']} -> Hash: {kq['hash1']}\n"
            f"Tập 2: {d['set2']} -> Hash: {kq['hash2']}\n"
            f"Bằng nhau? {kq['is_equal']}"
        )
    },
    '12': {
        'ten': 'BÀI 12: TẤN CÔNG HASH FLOODING',
        'du_lieu': {
            'm': 10,
            'normal_keys': [12, 34, 56, 78, 90, 21, 43],
            'malicious_keys': [10, 20, 30, 40, 50, 60, 70] # Toàn bội số của 10
        },
        'mong_doi': 'So sánh số va chạm max',
        'ham': lambda d: bai_12_hash_flooding(d),
        'format': lambda d, kq: (
            f"Giả lập với hàm băm tĩnh h(k) = k % 10:\n"
            f"- Mảng bình thường: Max đụng độ tại 1 bucket = {kq['normal_max_collisions']}\n"
            f"- Mảng độc hại (Attacker craft): Max đụng độ = {kq['malicious_max_collisions']}\n"
            f"[*] Bảng băm suy biến thành mảng 1 chiều (Linked List) $O(n)$, gây tấn công từ chối dịch vụ (DoS)."
        )
    },
    '13': {
        'ten': 'BÀI 13: ROLLING HASH 2 CHIỀU',
        'du_lieu': {'matrix': [[1, 2], [3, 4]]},
        'mong_doi': 'Không check strict',
        'ham': lambda d: bai_13_2d_hash(d),
        'format': lambda d, kq: f"Ma trận:\n {d['matrix'][0]}\n {d['matrix'][1]}\nTổng mã băm 2D: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: CÀI ĐẶT BLOOM FILTER',
        'du_lieu': {
            'm': 20, 'k': 3,
            'adds': ['apple', 'banana', 'cherry'],
            'checks': ['apple', 'orange']
        },
        'mong_doi': {'apple': True, 'orange': False},
        'ham': lambda d: bai_14_bloom_filter(d),
        'format': lambda d, kq: (
            f"Đã nạp: {d['adds']}\n"
            f"Kiểm tra 'apple': {kq['apple']} (Chắc chắn đúng)\n"
            f"Kiểm tra 'orange': {kq['orange']} (Có thể bị Dương tính giả nếu xui, nhưng không bao giờ mâu thuẫn báo False nếu đã nạp)"
        )
    },
    '15': {
        'ten': 'BÀI 15: MINHASH (ƯỚC LƯỢNG TƯƠNG ĐỒNG JACCARD)',
        'du_lieu': {
            'set_a': [1, 2, 3, 4, 5, 6, 7, 8],
            'set_b': [5, 6, 7, 8, 9, 10, 11, 12],
            'num_hashes': 100
        },
        'mong_doi': 'So sánh tỉ lệ',
        'ham': lambda d: bai_15_minhash(d),
        'format': lambda d, kq: (
            f"Số lượng hàm băm (Num Hashes) giả lập: {d['num_hashes']}\n"
            f"Jaccard thực tế (Tính toán tốn kém trên dữ liệu khổng lồ): {kq['true_jaccard']}\n"
            f"Jaccard ước lượng (MinHash cực nhanh): {kq['est_jaccard']}\n"
            f"[*] Tăng số lượng hàm băm sẽ làm cho mức độ ước lượng càng tiệm cận chính xác."
        )
    }
}

def chay_bai(cfg, check_strict=True):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    is_strict = check_strict and isinstance(cfg['mong_doi'], (list, dict))
    
    if is_strict:
        print(f"\nKết quả mong đợi:\n{cfg['mong_doi']}")
        # Lọc key riêng cho bài 11
        if 'is_equal' in cfg['mong_doi']:
            if kq['is_equal'] == cfg['mong_doi']['is_equal']:
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
            print(" MENU: PHIÊN 4 (PHẦN B: BÀI 8 -> BÀI 15)")
            print(" CHỌN BÀI (8-15) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            # Ép kiểu int để sort đúng từ 8 đến 15
            for k, v in sorted(Noidung.items(), key=lambda item: int(item[0])):
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in sorted(Noidung.keys(), key=int):
                    chay_bai(Noidung[k])
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass