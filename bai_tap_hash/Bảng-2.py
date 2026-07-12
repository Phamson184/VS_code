from typing import List, Dict, Any, Tuple
import hashlib
import bisect

# --- Bài 8: Băm kép (Double Hashing) ---
class DoubleHashingTable:
    def __init__(self, capacity: int = 7):
        self.capacity = capacity
        self.table: List[Any] = [None] * capacity
        self.size = 0
        self.R = 5 # Số nguyên tố nhỏ hơn capacity dùng cho h2

    def h1(self, key: int) -> int:
        return key % self.capacity

    def h2(self, key: int) -> int:
        return self.R - (key % self.R)

    def put(self, key: int, value: str):
        if self.size >= self.capacity:
            raise Exception("Bảng đầy")
        
        idx = self.h1(key)
        step = self.h2(key)
        
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + step) % self.capacity
            
        self.table[idx] = (key, value)
        self.size += 1

def bai_8_double_hashing(du_lieu: Dict[str, Any]) -> List[Any]:
    ht = DoubleHashingTable(capacity=7)
    for k, v in du_lieu['puts']:
        ht.put(k, v)
    return ht.table

# --- Bài 9: Two Sum dùng Hash ---
def bai_9_two_sum(du_lieu: Dict[str, Any]) -> Tuple[int, int]:
    arr = du_lieu['arr']
    target = du_lieu['target']
    hash_map = {} # Lưu {giá_trị : chỉ_số}
    
    for i, num in enumerate(arr):
        phan_bu = target - num
        if phan_bu in hash_map:
            return (hash_map[phan_bu], i)
        hash_map[num] = i
    return (-1, -1)

# --- Bài 10: Phần tử không lặp đầu tiên ---
def bai_10_first_unique(du_lieu: Dict[str, Any]) -> str:
    s = du_lieu['s']
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    for char in s:
        if freq[char] == 1:
            return char
    return ""

# --- Bài 11: Cài đặt HashSet cơ bản ---
class SimpleHashSet:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def add(self, key: Any):
        if not self.contains(key):
            self.table[self._hash(key)].append(key)

    def contains(self, key: Any) -> bool:
        return key in self.table[self._hash(key)]

    def remove(self, key: Any):
        if self.contains(key):
            self.table[self._hash(key)].remove(key)

def bai_11_hash_set(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    hset = SimpleHashSet()
    for item in du_lieu['adds']:
        hset.add(item)
    
    kq = {
        'contains_2': hset.contains(2),
        'contains_5': hset.contains(5)
    }
    hset.remove(2)
    kq['contains_2_after_remove'] = hset.contains(2)
    return kq

# --- Bài 12: Tổng đoạn con bằng K ---
def bai_12_subarray_sum(du_lieu: Dict[str, Any]) -> int:
    arr = du_lieu['arr']
    k = du_lieu['k']
    count = 0
    prefix_sum = 0
    # Lưu tần suất của các prefix_sum. Khởi tạo {0: 1} để tính các đoạn bắt đầu từ index 0
    sum_map = {0: 1} 
    
    for num in arr:
        prefix_sum += num
        # Nếu (prefix_sum - k) đã tồn tại, tức là có mảng con kết thúc tại đây có tổng = k
        if (prefix_sum - k) in sum_map:
            count += sum_map[prefix_sum - k]
            
        sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1
        
    return count

# --- Bài 13: Dãy liên tiếp dài nhất ---
def bai_13_longest_consecutive(du_lieu: Dict[str, Any]) -> int:
    nums = du_lieu['arr']
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Chỉ bắt đầu đếm nếu num là số bắt đầu của một dãy (không có num - 1)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak

# --- Bài 14: Xóa lười (Tombstone) trong Open Addressing ---
class LazyDeletionHashTable:
    TOMBSTONE = "<DELETED>"
    
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: str):
        idx = self._hash(key)
        # Tìm chỗ trống hoặc bia mộ để chèn
        while self.table[idx] is not None and self.table[idx] != self.TOMBSTONE:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.capacity
        self.table[idx] = (key, value)

    def remove(self, key: int):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx] != self.TOMBSTONE and self.table[idx][0] == key:
                self.table[idx] = self.TOMBSTONE # Cắm bia mộ
                return
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break

    def get(self, key: int) -> str:
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx] != self.TOMBSTONE and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break
        return "Not Found"

def bai_14_lazy_deletion(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ht = LazyDeletionHashTable(capacity=5)
    for k, v in du_lieu['puts']:
        ht.put(k, v)
    
    ht.remove(du_lieu['remove_key'])
    ht.put(du_lieu['put_after_remove'][0], du_lieu['put_after_remove'][1])
    
    return {'table_state': ht.table}

# --- Bài 15: Băm nhất quán (Consistent Hashing) ---
class ConsistentHashing:
    def __init__(self, virtual_nodes: int = 3):
        self.virtual_nodes = virtual_nodes
        self.ring = [] # Lưu các hash values
        self.server_map = {} # Map hash_value -> server_name

    def _hash(self, key: str) -> int:
        # Dùng MD5 để ánh xạ key thành 1 số nguyên lớn trên vòng băm
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_server(self, server_name: str):
        for i in range(self.virtual_nodes):
            v_node_key = f"{server_name}_v{i}"
            h = self._hash(v_node_key)
            bisect.insort(self.ring, h)
            self.server_map[h] = server_name

    def get_server(self, key: str) -> str:
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self.ring, h)
        # Nếu vượt quá vòng, quay lại nút đầu tiên
        if idx == len(self.ring):
            idx = 0
        return self.server_map[self.ring[idx]]

def bai_15_consistent_hashing(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ch = ConsistentHashing(virtual_nodes=3)
    for server in du_lieu['initial_servers']:
        ch.add_server(server)
        
    # Ánh xạ các data_keys vào server ban đầu
    mapping_truoc = {}
    for key in du_lieu['data_keys']:
        mapping_truoc[key] = ch.get_server(key)
        
    # Thêm 1 server mới
    ch.add_server(du_lieu['new_server'])
    
    # Kiểm tra xem có bao nhiêu khóa phải di chuyển
    mapping_sau = {}
    keys_migrated = 0
    for key in du_lieu['data_keys']:
        mapping_sau[key] = ch.get_server(key)
        if mapping_sau[key] != mapping_truoc[key]:
            keys_migrated += 1
            
    return {
        'total_keys': len(du_lieu['data_keys']),
        'keys_migrated': keys_migrated,
        'servers_after': du_lieu['initial_servers'] + [du_lieu['new_server']]
    }
Noidung = {
    '8': {
        'ten': 'BÀI 8: QUADRATIC PROBING / DOUBLE HASHING',
        'du_lieu': {'puts': [(10, 'A'), (17, 'B'), (24, 'C')]},
        'mong_doi': [None, None, None, (10, 'A'), (24, 'C'), None, (17, 'B')],
        'ham': lambda d: bai_8_double_hashing(d),
        'format': lambda d, kq: (
            f"Thông số: Capacity = 7, h1 = k % 7, h2 = 5 - (k % 5)\n"
            f"Chèn lần lượt: {d['puts']}\n"
            f"Trạng thái Bảng:\n" + "\n".join([f"  Index {i}: {val}" for i, val in enumerate(kq)]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - K(10) -> h1=3. Chèn vào Index 3.\n"
            f"    - K(17) -> h1=3 (Đụng độ!). Tính h2(17) = 5 - 2 = 3. Bước nhảy = 3.\n"
            f"      Thử Index (3+3)%7 = 6. Chèn vào Index 6.\n"
            f"    - K(24) -> h1=3 (Đụng độ!). Tính h2(24) = 5 - 4 = 1. Bước nhảy = 1.\n"
            f"      Thử Index (3+1)%7 = 4. Chèn vào Index 4.\n"
            f"    - Băm kép giúp giảm thiểu Clustering (gom cụm) cực kỳ hiệu quả."
        )
    },
    '9': {
        'ten': 'BÀI 9: TWO SUM (O(n) dùng Hash Map)',
        'du_lieu': {'arr': [2, 7, 11, 15], 'target': 9},
        'mong_doi': (0, 1),
        'ham': lambda d: bai_9_two_sum(d),
        'format': lambda d, kq: f"Mảng: {d['arr']} | Target = {d['target']}\n=> Cặp index thỏa mãn: {kq}"
    },
    '10': {
        'ten': 'BÀI 10: PHẦN TỬ KHÔNG LẶP ĐẦU TIÊN',
        'du_lieu': {'s': 'leetcode'},
        'mong_doi': 'l',
        'ham': lambda d: bai_10_first_unique(d),
        'format': lambda d, kq: f"Chuỗi gốc: '{d['s']}'\n=> Ký tự không lặp đầu tiên: '{kq}'"
    },
    '11': {
        'ten': 'BÀI 11: CÀI ĐẶT HASH SET',
        'du_lieu': {'adds': [1, 1, 2, 3]},
        'mong_doi': {'contains_2': True, 'contains_5': False, 'contains_2_after_remove': False},
        'ham': lambda d: bai_11_hash_set(d),
        'format': lambda d, kq: (
            f"Lệnh chèn: add(1), add(1), add(2), add(3)\n"
            f"- Kiểm tra contains(2): {kq['contains_2']}\n"
            f"- Kiểm tra contains(5): {kq['contains_5']}\n"
            f"- Kiểm tra contains(2) sau khi remove(2): {kq['contains_2_after_remove']}"
        )
    },
    '12': {
        'ten': 'BÀI 12: TỔNG ĐOẠN CON BẰNG K (Prefix Sum + Hash)',
        'du_lieu': {'arr': [1, 1, 1], 'k': 2},
        'mong_doi': 2,
        'ham': lambda d: bai_12_subarray_sum(d),
        'format': lambda d, kq: (
            f"Mảng: {d['arr']} | k = {d['k']}\n"
            f"=> Số lượng đoạn con liên tiếp có tổng = {d['k']} là: {kq}\n"
            f"[*] Phương pháp Prefix Sum kết hợp Hash giúp giảm từ O(n^2) xuống O(n)."
        )
    },
    '13': {
        'ten': 'BÀI 13: DÃY LIÊN TIẾP DÀI NHẤT (O(n))',
        'du_lieu': {'arr': [100, 4, 200, 1, 3, 2]},
        'mong_doi': 4,
        'ham': lambda d: bai_13_longest_consecutive(d),
        'format': lambda d, kq: f"Mảng: {d['arr']}\n=> Độ dài dãy liên tiếp dài nhất (1, 2, 3, 4): {kq}"
    },
    '14': {
        'ten': 'BÀI 14: XÓA LƯỜI (TOMBSTONE) TRONG OPEN ADDRESSING',
        'du_lieu': {
            'puts': [(10, 'A'), (15, 'B'), (20, 'C')], # Giả sử băm k % 5 (đều vào index 0)
            'remove_key': 15,
            'put_after_remove': (25, 'D')
        },
        'mong_doi': {'table_state': [(10, 'A'), (25, 'D'), (20, 'C'), None, None]},
        'ham': lambda d: bai_14_lazy_deletion(d),
        'format': lambda d, kq: (
            f"Chèn 10, 15, 20. Xóa 15. Sau đó chèn 25.\n"
            f"Trạng thái bảng cuối cùng:\n{kq['table_state']}\n"
            f"\n[*] NHẬN XÉT:\n"
            f"    - Khi xóa 15, ta không xóa hẳn (tránh đứt chuỗi dò) mà cắm cờ <DELETED>.\n"
            f"    - Khi chèn 25, thuật toán thấy slot <DELETED> liền ghi đè (tái sử dụng)."
        )
    },
    '15': {
        'ten': 'BÀI 15: BĂM NHẤT QUÁN (CONSISTENT HASHING)',
        'du_lieu': {
            'initial_servers': ['Server_A', 'Server_B', 'Server_C'],
            'new_server': 'Server_D',
            'data_keys': [f"User_ID_{i}" for i in range(100)] # 100 khóa mô phỏng
        },
        'mong_doi': 'Kiểm tra mô phỏng, không so strict match',
        'ham': lambda d: bai_15_consistent_hashing(d),
        'format': lambda d, kq: (
            f"Cụm ban đầu có {len(d['initial_servers'])} máy chủ. Phân bổ {kq['total_keys']} khóa.\n"
            f"Tiến hành thêm {d['new_server']} vào cụm...\n"
            f"Tổng số máy chủ hiện tại: {len(kq['servers_after'])}\n"
            f"Số lượng khóa (keys) phải di chuyển sang server khác: {kq['keys_migrated']}/{kq['total_keys']}\n"
            f"\n[*] NHẬN XÉT:\n"
            f"    - Thay vì phải di chuyển gần như toàn bộ khóa nếu dùng h = key % n_servers,\n"
            f"      vòng băm nhất quán chỉ làm dịch chuyển khoảng ~1/N số khóa (khoảng 25% trong trường hợp này)\n"
            f"      khi quy mô máy chủ thay đổi. Đây là xương sống của các DB phân tán."
        )
    }
}

def chay_bai(cfg, check_strict=True):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if check_strict and cfg['mong_doi'] != 'Kiểm tra mô phỏng, không so strict match':
        print(f"\nKết quả mong đợi:\n{cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("\nTrạng thái: THÀNH CÔNG")
        else:
            print("\nTrạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*70)
            print(" MENU: PHIÊN 2 (PHẦN A: BÀI 8 -> BÀI 15)")
            print(" CHỌN BÀI (8-15) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*70)
            # Ép kiểu int cho key để sort đúng thứ tự 8 -> 15
            for k, v in sorted(Noidung.items(), key=lambda item: int(item[0])):
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in sorted(Noidung.keys(), key=int):
                    cfg = Noidung[k]
                    chay_bai(cfg, check_strict=(k != '15'))
            elif chon in Noidung:
                chay_bai(Noidung[chon], check_strict=(chon != '15'))
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass
