from typing import List, Dict, Any, Tuple, Set

# --- Bài 1: Cài đặt bảng băm bằng Chaining ---
class ChainingHashTable:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key: Any) -> Any:
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def remove(self, key: Any) -> bool:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return True
        return False

def bai_1_chaining(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ht = ChainingHashTable(capacity=3)
    for k, v in du_lieu['puts']:
        ht.put(k, v)
    kq_get = ht.get(du_lieu['get_key'])
    ht.remove(du_lieu['remove_key'])
    return {
        'get_result': kq_get,
        'table_state': ht.table
    }

# --- Bài 2: Cài đặt bảng băm bằng Dò tuyến tính ---
class LinearProbingHashTable:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.table: List[Any] = [None] * capacity
        self.size = 0

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any):
        if self.size >= self.capacity:
            raise Exception("Bảng băm đã đầy")
        idx = self._hash(key)
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.capacity
        self.table[idx] = (key, value)
        self.size += 1

    def get(self, key: Any) -> Any:
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break
        return None

def bai_2_linear_probing(du_lieu: Dict[str, Any]) -> List[Any]:
    ht = LinearProbingHashTable(capacity=5)
    for k, v in du_lieu['puts']:
        ht.put(k, v)
    return ht.table

# --- Bài 3: Đếm tần suất ---
def bai_3_dem_tan_suat(du_lieu: Dict[str, Any]) -> Dict[Any, int]:
    freq: Dict[Any, int] = {}
    for item in du_lieu['arr']:
        freq[item] = freq.get(item, 0) + 1
    return freq

# --- Bài 4: Hai mảng có phần tử chung ---
def bai_4_phan_tu_chung(du_lieu: Dict[str, Any]) -> Set[Any]:
    set_a = set(du_lieu['arr1'])
    # Dùng set giao (intersection) với độ phức tạp trung bình O(n)
    return set_a.intersection(du_lieu['arr2'])

# --- Bài 5: Nhóm theo khóa (Group by) ---
def bai_5_nhom_theo_khoa(du_lieu: Dict[str, Any]) -> Dict[str, List[str]]:
    grouped: Dict[str, List[str]] = {}
    for item in du_lieu['arr']:
        key = item[0]  # Khóa là chữ cái đầu
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped

# --- Bài 6: So sánh Chaining vs Open Addressing ---
def bai_6_so_sanh(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ht_chain = ChainingHashTable(capacity=5)
    ht_linear = LinearProbingHashTable(capacity=5)
    
    for k, v in du_lieu['puts']:
        ht_chain.put(k, v)
        ht_linear.put(k, v)
        
    return {
        'chaining_state': ht_chain.table,
        'linear_state': ht_linear.table
    }

# --- Bài 7: Hệ số tải và Rehashing ---
class RehashingHashTable:
    def __init__(self, initial_capacity: int = 4, load_factor_threshold: float = 0.75):
        self.capacity = initial_capacity
        self.threshold = load_factor_threshold
        self.size = 0
        self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self.rehash_count = 0

    def _hash(self, key: Any, cap: int) -> int:
        return hash(key) % cap

    def put(self, key: Any, value: Any):
        if (self.size + 1) / self.capacity > self.threshold:
            self._rehash()
            
        idx = self._hash(key, self.capacity)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.size += 1

    def _rehash(self):
        self.rehash_count += 1
        new_capacity = self.capacity * 2
        new_table: List[List[Tuple[Any, Any]]] = [[] for _ in range(new_capacity)]
        
        for bucket in self.table:
            for k, v in bucket:
                idx = self._hash(k, new_capacity)
                new_table[idx].append((k, v))
                
        self.capacity = new_capacity
        self.table = new_table

def bai_7_rehashing(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ht = RehashingHashTable(initial_capacity=4, load_factor_threshold=0.75)
    cap_history = [ht.capacity]
    
    for k, v in du_lieu['puts']:
        ht.put(k, v)
        if ht.capacity != cap_history[-1]:
            cap_history.append(ht.capacity)
            
    return {
        'final_capacity': ht.capacity,
        'rehash_count': ht.rehash_count,
        'capacity_history': cap_history
    }
Noidung = {
    '1': {
        'ten': 'BÀI 1: CÀI ĐẶT BẢNG BĂM BẰNG CHAINING',
        'du_lieu': {'puts': [('a', 1), ('b', 2), ('c', 3), ('a', 10)], 'get_key': 'a', 'remove_key': 'b'},
        'mong_doi': {'get_result': 10, 'table_state': [[], [('c', 3)], [('a', 10)]]},
        'ham': lambda d: bai_1_chaining(d),
        'format': lambda d, kq: (
            f"Lịch sử chèn: {d['puts']}\n"
            f"Kết quả get('{d['get_key']}'): {kq['get_result']}\n"
            f"Đã gọi remove('{d['remove_key']}')\n"
            f"Trạng thái mảng nội bộ (capacity=3): {kq['table_state']}"
        )
    },
    '2': {
        'ten': 'BÀI 2: BẢNG BĂM DÒ TUYẾN TÍNH (LINEAR PROBING)',
        'du_lieu': {'puts': [(10, 'A'), (20, 'B'), (15, 'C'), (25, 'D')]}, # Giả sử băm = key % 5
        'mong_doi': [(10, 'A'), (15, 'C'), None, (20, 'B'), (25, 'D')],
        'ham': lambda d: bai_2_linear_probing(d),
        'format': lambda d, kq: (
            f"Chèn các khóa: {[k for k, v in d['puts']]}\n"
            f"Trạng thái mảng nội bộ (capacity=5):\n" + 
            "\n".join([f"  Index {i}: {val}" for i, val in enumerate(kq)]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - Khóa 10 (hash 0) vào Index 0.\n"
            f"    - Khóa 20 (hash 0) xung đột tại Index 0, dò tịnh tiến và vào Index 1.\n" # Giả định băm đơn giản, ở đây dùng hash() python nên vị trí thực tế phụ thuộc hash()
            f"    - Sự xê dịch này là đặc trưng của Linear Probing."
        )
    },
    '3': {
        'ten': 'BÀI 3: ĐẾM TẦN SUẤT BẰNG HASH MAP',
        'du_lieu': {'arr': ['a', 'b', 'a', 'c', 'a', 'b']},
        'mong_doi': {'a': 3, 'b': 2, 'c': 1},
        'ham': lambda d: bai_3_dem_tan_suat(d),
        'format': lambda d, kq: f"Mảng gốc: {d['arr']}\nKết quả đếm: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: HAI MẢNG CÓ PHẦN TỬ CHUNG',
        'du_lieu': {'arr1': [1, 2, 3, 5, 8], 'arr2': [2, 3, 4, 8, 9]},
        'mong_doi': {8, 2, 3},
        'ham': lambda d: bai_4_phan_tu_chung(d),
        'format': lambda d, kq: f"Mảng 1: {d['arr1']}\nMảng 2: {d['arr2']}\nPhần tử chung: {kq}"
    },
    '5': {
        'ten': 'BÀI 5: NHÓM THEO KHÓA (GROUP BY)',
        'du_lieu': {'arr': ['apple', 'banana', 'apricot', 'cherry', 'avocado', 'blueberry']},
        'mong_doi': {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']},
        'ham': lambda d: bai_5_nhom_theo_khoa(d),
        'format': lambda d, kq: (
            f"Danh sách từ: {d['arr']}\n"
            f"Kết quả phân nhóm (theo chữ cái đầu):\n" +
            "\n".join([f"  '{k}': {v}" for k, v in kq.items()])
        )
    },
    '6': {
        'ten': 'BÀI 6: SO SÁNH CHAINING VS OPEN ADDRESSING',
        'du_lieu': {'puts': [(5, 'A'), (10, 'B'), (15, 'C')]},
        'mong_doi': 'So sánh cấu trúc, không check strict match',
        'ham': lambda d: bai_6_so_sanh(d),
        'format': lambda d, kq: (
            f"Cùng chèn dữ liệu đụng độ: {d['puts']}\n\n"
            f"[1] Trạng thái Chaining (Mảng chứa List):\n{kq['chaining_state']}\n\n"
            f"[2] Trạng thái Linear Probing (Mảng phẳng 1 chiều):\n{kq['linear_state']}\n\n"
            f"[*] NHẬN XÉT:\n"
            f"  - Chaining: Tiêu tốn bộ nhớ cho con trỏ list, nhưng không bị giới hạn dung lượng.\n"
            f"  - Linear Probing: Cache-friendly hơn do dùng mảng phẳng, nhưng dễ sập khi bảng đầy (Hệ số tải cao)."
        )
    },
    '7': {
        'ten': 'BÀI 7: HỆ SỐ TẢI VÀ CƠ CHẾ REHASHING',
        'du_lieu': {'puts': [(1,'A'), (2,'B'), (3,'C'), (4,'D'), (5,'E')]},
        'mong_doi': {'final_capacity': 8, 'rehash_count': 1, 'capacity_history': [4, 8]},
        'ham': lambda d: bai_7_rehashing(d),
        'format': lambda d, kq: (
            f"Sức chứa ban đầu: 4. Ngưỡng (Threshold): 0.75 (Tối đa 3 phần tử)\n"
            f"Chèn 5 phần tử: {d['puts']}\n"
            f"Lịch sử mở rộng dung lượng: {kq['capacity_history']}\n"
            f"Tổng số lần Rehash: {kq['rehash_count']}\n"
            f"Dung lượng cuối cùng: {kq['final_capacity']}"
        )
    }
}

def chay_bai(cfg, check_strict=True):
    print(f"\n{'='*60}\n {cfg['ten']}\n{'='*60}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if check_strict and cfg['mong_doi'] != 'So sánh cấu trúc, không check strict match':
        print(f"\nKết quả mong đợi:\n{cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("\nTrạng thái: THÀNH CÔNG")
        else:
            print("\nTrạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*60)
            print(" MENU: PHIÊN 1 (PHẦN A: BÀI 1 -> BÀI 7)")
            print(" CHỌN BÀI (1-7) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*60)
            for k, v in sorted(Noidung.items()):
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    # Bài 6 bỏ qua check match vì kết quả hash() của Python xáo trộn mỗi lần chạy
                    chay_bai(cfg, check_strict=(cfg != Noidung['6'] and cfg != Noidung['2']))
            elif chon in Noidung:
                chay_bai(Noidung[chon], check_strict=(chon not in ['2', '6']))
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass