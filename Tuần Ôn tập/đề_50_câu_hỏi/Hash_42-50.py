from typing import List, Dict, Any, Tuple
import random

# ==========================================
# PHẦN 8: BẢNG BĂM (CÂU 42 - 46)
# ==========================================

# --- Câu 42: Chaining & Open Addressing ---
class ChainingHashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def put(self, key: int, val: Any):
        idx = hash(key) % self.size
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, val)
                return
        self.table[idx].append((key, val))
        
    def get(self, key: int) -> Any:
        idx = hash(key) % self.size
        for k, v in self.table[idx]:
            if k == key: return v
        return None

def bai42_hash_collisions(du_lieu: Dict[str, Any]) -> str:
    ht = ChainingHashTable()
    for k, v in du_lieu['puts']: ht.put(k, v)
    return f"Lấy key {du_lieu['get_key']} -> Giá trị: {ht.get(du_lieu['get_key'])}"

# --- Câu 43: Hệ số tải & Rehashing ---
class RehashingHashTable:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity
        self.log = []
        
    def put(self, key: int):
        if self.size / self.capacity >= 0.75:
            self._rehash()
        idx = hash(key) % self.capacity
        while self.table[idx] is not None:
            idx = (idx + 1) % self.capacity
        self.table[idx] = key
        self.size += 1
        
    def _rehash(self):
        old_table = self.table
        self.capacity *= 2
        self.log.append(f"Rehashed -> Mảng mới size: {self.capacity}")
        self.table = [None] * self.capacity
        self.size = 0
        for key in old_table:
            if key is not None: self.put(key)

def bai43_rehashing(du_lieu: Dict[str, Any]) -> List[str]:
    ht = RehashingHashTable(initial_capacity=4)
    for k in du_lieu['keys']: ht.put(k)
    return ht.log

# --- Câu 44: Two Sum dùng Hash ---
def bai44_two_sum(du_lieu: Dict[str, Any]) -> Tuple[int, int]:
    a, target = du_lieu['a'], du_lieu['target']
    seen = {}
    for i, num in enumerate(a):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return (-1, -1)

# --- Câu 45: Tổng đoạn con bằng k ---
def bai45_subarray_sum(du_lieu: Dict[str, Any]) -> int:
    a, k = du_lieu['a'], du_lieu['k']
    prefix_sums = {0: 1}
    curr_sum, count = 0, 0
    
    for num in a:
        curr_sum += num
        if (curr_sum - k) in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
    return count

# --- Câu 46: Dãy liên tiếp dài nhất ---
def bai46_longest_consecutive(du_lieu: Dict[str, Any]) -> int:
    nums = set(du_lieu['a'])
    max_len = 0
    
    for x in nums:
        if x - 1 not in nums:
            curr_num = x
            curr_len = 1
            while curr_num + 1 in nums:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
            
    return max_len

# ==========================================
# PHẦN 9: HÀM BĂM (CÂU 47 - 50)
# ==========================================

# --- Câu 47: Polynomial Rolling Hash ---
def bai47_poly_hash(du_lieu: Dict[str, Any]) -> int:
    s = du_lieu['s']
    p, m = 31, 10**9 + 9
    hash_val = 0
    p_pow = 1
    for char in s:
        hash_val = (hash_val + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_val

# --- Câu 48: Rabin-Karp ---
def bai48_rabin_karp(du_lieu: Dict[str, Any]) -> int:
    text, pattern = du_lieu['text'], du_lieu['pattern']
    n, m = len(text), len(pattern)
    if m == 0 or n < m: return -1
    
    p, mod = 31, 10**9 + 9
    p_pow = [1] * max(n, m)
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % mod
        
    h_pattern = 0
    for i in range(m):
        h_pattern = (h_pattern + (ord(pattern[i]) - ord('a') + 1) * p_pow[i]) % mod
        
    h_text = [0] * (n + 1)
    for i in range(n):
        h_text[i+1] = (h_text[i] + (ord(text[i]) - ord('a') + 1) * p_pow[i]) % mod
        
    for i in range(n - m + 1):
        curr_hash = (h_text[i+m] + mod - h_text[i]) % mod
        if curr_hash == (h_pattern * p_pow[i]) % mod:
            return i
    return -1

# --- Câu 49: Universal Hashing ---
def bai49_universal_hash(du_lieu: Dict[str, Any]) -> List[int]:
    keys = du_lieu['keys']
    m = du_lieu['m']
    p = 10**9 + 7
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    return [((a * k + b) % p) % m for k in keys]

# --- Câu 50: Bloom Filter ---
class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size
        
    def _hash(self, item: str, seed: int) -> int:
        return hash(item + str(seed)) % self.size
        
    def add(self, item: str):
        for i in range(self.hash_count):
            self.bit_array[self._hash(item, i)] = True
            
    def check(self, item: str) -> bool:
        for i in range(self.hash_count):
            if not self.bit_array[self._hash(item, i)]:
                return False
        return True

def bai50_bloom_filter(du_lieu: Dict[str, Any]) -> Dict[str, bool]:
    bf = BloomFilter()
    for item in du_lieu['adds']: bf.add(item)
    res = {}
    for item in du_lieu['checks']: res[item] = bf.check(item)
    return res

# ==========================================
# CẤU HÌNH MENU DATA-DRIVEN
# ==========================================
Noidung = {
    '42': {'ten': 'CÂU 42: CHAINING & OPEN ADDRESSING', 'du_lieu': {'puts': [(1, 'A'), (8, 'B')], 'get_key': 8}, 'ham': bai42_hash_collisions, 'format': lambda d, kq: f"Thao tác: Nạp {d['puts']} | {kq} [cite: 245-247]"},
    '43': {'ten': 'CÂU 43: HỆ SỐ TẢI & REHASHING', 'du_lieu': {'keys': [1, 2, 3, 4, 5]}, 'ham': bai43_rehashing, 'format': lambda d, kq: f"Nạp {d['keys']} vào mảng ban đầu size 4 -> Logs kích hoạt: {kq} [cite: 248-250]"},
    '44': {'ten': 'CÂU 44: TWO SUM (DÙNG HASH MAP O(n))', 'du_lieu': {'a': [2, 7, 11, 15], 'target': 9}, 'ham': bai44_two_sum, 'format': lambda d, kq: f"Mảng {d['a']}, Tìm tổng={d['target']} -> Cặp chỉ số tìm được: {kq} [cite: 251-253]"},
    '45': {'ten': 'CÂU 45: TỔNG ĐOẠN CON BẰNG K', 'du_lieu': {'a': [1, 1, 1], 'k': 2}, 'ham': bai45_subarray_sum, 'format': lambda d, kq: f"Mảng {d['a']}, k={d['k']} -> Số lượng đoạn con thỏa mãn: {kq} [cite: 254-256]"},
    '46': {'ten': 'CÂU 46: DÃY LIÊN TIẾP DÀI NHẤT', 'du_lieu': {'a': [100, 4, 200, 1, 3, 2]}, 'ham': bai46_longest_consecutive, 'format': lambda d, kq: f"Mảng {d['a']} -> Độ dài dãy liên tiếp lớn nhất: {kq} [cite: 257-259]"},
    '47': {'ten': 'CÂU 47: POLYNOMIAL ROLLING HASH', 'du_lieu': {'s': 'abc'}, 'ham': bai47_poly_hash, 'format': lambda d, kq: f"Chuỗi '{d['s']}' -> Mã băm đa thức thu được: {kq} [cite: 261-263]"},
    '48': {'ten': 'CÂU 48: THUẬT TOÁN RABIN-KARP', 'du_lieu': {'text': 'zabcd', 'pattern': 'abc'}, 'ham': bai48_rabin_karp, 'format': lambda d, kq: f"Tìm pattern '{d['pattern']}' trong '{d['text']}' -> Xuất hiện tại vị trí (index): {kq} [cite: 265-267]"},
    '49': {'ten': 'CÂU 49: UNIVERSAL HASHING', 'du_lieu': {'keys': [10, 20, 30], 'm': 7}, 'ham': bai49_universal_hash, 'format': lambda d, kq: f"Keys: {d['keys']}, Bảng size: {d['m']} -> Băm với a, b ngẫu nhiên: {kq} [cite: 268-271]"},
    '50': {'ten': 'CÂU 50: CẤU TRÚC XÁC SUẤT BLOOM FILTER', 'du_lieu': {'adds': ['apple', 'banana'], 'checks': ['apple', 'orange']}, 'ham': bai50_bloom_filter, 'format': lambda d, kq: f"Nạp dữ liệu: {d['adds']}.\nKiểm tra {d['checks']} -> Kết quả: {kq}\n(Lưu ý: False = Chắc chắn không có, True = Có thể có) [cite: 272-275]"}
}

# ==========================================
# KHỐI ĐIỀU KHIỂN & MENU TƯƠNG TÁC
# ==========================================
def chay_bai_tu_dong(key_bai: str, tap_du_lieu_noidung: dict):
    if key_bai not in tap_du_lieu_noidung:
        print(f"\n[!] Lỗi: Không tìm thấy bài tập có mã '{key_bai}'.")
        return

    cfg = tap_du_lieu_noidung[key_bai]
    print(f"\n{'='*75}")
    print(f" {cfg['ten']}")
    print(f"{'='*75}")

    try:
        if 'du_lieu' in cfg and cfg['du_lieu'] is not None:
             ket_qua_thuc_te = cfg['ham'](cfg['du_lieu'])
             if callable(cfg.get('format')):
                 print(cfg['format'](cfg['du_lieu'], ket_qua_thuc_te))
             else:
                 print(f"Kết quả: {ket_qua_thuc_te}")
        else:
             ket_qua_thuc_te = cfg['ham']()
             if callable(cfg.get('format')):
                 try:
                     print(cfg['format'](None, ket_qua_thuc_te))
                 except TypeError:
                     print(cfg['format'](ket_qua_thuc_te))
             else:
                 print(f"{ket_qua_thuc_te}")
    except Exception as e:
        print(f"[!] Quá trình chạy bị lỗi: {str(e)}")
        return

if __name__ == '__main__':
    try:
        dict_noidung = locals().get('Noidung')
        if not dict_noidung:
             print("Lỗi: Không tìm thấy từ điển cấu hình bài tập (Noidung).")
             exit()

        danh_sach_keys = sorted(dict_noidung.keys(), key=lambda x: int(x) if x.isdigit() else x)

        while True:
            print("\n" + "*"*75)
            print(f" MENU CHÍNH (CÁC CÂU: {danh_sach_keys[0]} -> {danh_sach_keys[-1]})")
            print(" NHẬP MÃ CÂU HOẶC '0' ĐỂ THOÁT | 'all' ĐỂ CHẠY TOÀN BỘ")
            print("*"*75)
            
            for k in danh_sach_keys:
                print(f" {k:>3}. {dict_noidung[k]['ten']}")
                
            chon = input("\nLựa chọn của bạn: ").strip()
            
            if chon == '0':
                print("Chương trình kết thúc. Chúc mừng bạn đã đi hết 50 câu!")
                break
            elif chon.lower() == 'all':
                for k in danh_sach_keys:
                    chay_bai_tu_dong(k, dict_noidung)
            elif chon in dict_noidung:
                chay_bai_tu_dong(chon, dict_noidung)
            else:
                print("\n[!] Lựa chọn không hợp lệ, vui lòng nhập chính xác mã câu!")
    except KeyboardInterrupt:
        print("\nChương trình bị ngắt bởi người dùng.")