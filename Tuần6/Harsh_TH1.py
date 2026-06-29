from typing import List, Dict, Any

def thuc_hanh_01(du_lieu: Dict[str, Any]) -> List[int]:
    """Sử dụng phương pháp chia để tính giá trị băm."""
    m = du_lieu['m']
    keys = du_lieu['keys']
    # Hàm băm hash_key(key, m)
    return [key % m for key in keys]

def thuc_hanh_02(du_lieu: Dict[str, Any]) -> List[List[str]]:
    """Tạo bảng băm và xử lý xung đột bằng Chaining (Danh sách liên kết/Mảng phụ)."""
    m = du_lieu['m']
    hash_table = [[] for _ in range(m)]
    
    def hashing(keyvalue: int) -> int:
        return keyvalue % m
        
    def insert(ht: List[List[str]], keyvalue: int, value: str):
        hash_key = hashing(keyvalue)
        ht[hash_key].append(value)
        
    for k, v in du_lieu['items']:
        insert(hash_table, k, v)
        
    return hash_table

class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key: str) -> int:
        # Sử dụng hàm hash built-in của Python để băm chuỗi
        return hash(key) % self.capacity

    def insert(self, key: str, value: int):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key: str) -> int:
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key: str):
        index = self._hash(key)
        previous = None
        current = self.table[index]
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def __contains__(self, key: str) -> bool:
        try:
            self.search(key)
            return True
        except KeyError:
            return False

def thuc_hanh_03(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ht = HashTable(du_lieu['capacity'])
    
    # Bước 1: Nạp dữ liệu giai đoạn 1
    for k, v in du_lieu['inserts_giai_doan_1']:
        ht.insert(k, v)
    
    kq = {}
    kq['has_data_science'] = "data science" in ht
    kq['has_IT'] = "IT" in ht
    kq['search_IoT'] = ht.search("IoT") if "IoT" in ht else None
    
    # Bước 2: Nạp tiếp dữ liệu giai đoạn 2 (giữ tính data-driven thuần túy)
    for k, v in du_lieu['inserts_giai_doan_2']:
        ht.insert(k, v)
    kq['search_machine_learning'] = ht.search("machine learning")
    
    # Bước 3: Xóa phần tử theo chỉ định cấu hình
    ht.remove(du_lieu['xoa_khoa'])
    kq['len_sau_xoa'] = len(ht)
    
    return kq

Noidung = {
    '1': {
        'ten': 'THỰC HÀNH 01: BẢNG BĂM (PHƯƠNG PHÁP CHIA)',
        'du_lieu': {'m': 7, 'keys': [15, 2, 3, 9, 11, 7]},
        'mong_doi': [1, 2, 3, 2, 4, 0],
        'ham': lambda d: thuc_hanh_01(d),
        'format': lambda d, kq: (
            f"Kích thước m = {d['m']}\n"
            f"Các khóa đầu vào: {d['keys']}\n"
            f"Giá trị băm (Hash values): {kq}\n"
            f"\n[*] NHẬN XÉT (Kỹ thuật Dò tuyến tính):\n"
            f"    - Ở khóa '9', giá trị băm thu được là 2, trùng khớp và xảy ra xung đột với vị trí của khóa '2'.\n"
            f"    - Ở khóa '7', giá trị băm bằng 0. Đây là một điểm xung đột tiềm năng nếu trong tương lai hệ thống \n"
            f"      nạp thêm phần tử cũng ánh xạ về index 0.\n"
            f"    - Khi áp dụng Dò tuyến tính (Linear Probing), thuật toán xử lý bằng cách duyệt tuần tiến qua các \n"
            f"      ô liền kề tiếp theo (vị trí 3, 4, 5...) cho đến khi định vị được slot trống đầu tiên để chèn."
        )
    },
    '2': {
        'ten': 'THỰC HÀNH 02: BẢNG BĂM (PHƯƠNG PHÁP CHAINING)',
        'du_lieu': {
            'm': 10, 
            'items': [(10, 'MachineLearning'), (45, 'DataScience'), (20, 'DataAnalytics'), 
                      (9, 'BigData'), (21, 'DataStructure '), (41, 'IoT'), (35, 'Probability')]
        },
        'mong_doi': [['MachineLearning', 'DataAnalytics'], ['DataStructure ', 'IoT'], [], [], [], ['DataScience', 'Probability'], [], [], [], ['BigData']],
        'ham': lambda d: thuc_hanh_02(d),
        'format': lambda d, kq: (
            f"Bảng băm (m={d['m']}) sau khi phân tách và chèn:\n" + 
            "\n".join([f"Index {i}: {(' --> '.join(row) if row else '(Trống)')}" for i, row in enumerate(kq)]) +
            f"\n\n[*] NHẬN XÉT:\n"
            f"    - Quan sát danh sách trực quan, tại các vị trí Index 0, Index 1, và Index 5 xuất hiện đụng độ.\n"
            f"    - Giải thuật giải quyết triệt để xung đột bằng phương pháp nối dây Chaining thông qua mảng phụ.\n"
            f"    - Toàn bộ các giá trị đụng độ cùng slot được nối liên tục vào cấu trúc mảng tại chính index đó."
        )
    },
    '3': {
        'ten': 'THỰC HÀNH 03: HASH TABLE OOP (MÔ PHỎNG SẠCH)',
        'du_lieu': {
            'capacity': 7,
            'inserts_giai_doan_1': [("data science", 15), ("IoT", 11), ("machine learning", 27), 
                                    ("deep learning", 8), ("computer science", 32)],
            'inserts_giai_doan_2': [("big data", 18)],
            'xoa_khoa': "IoT"
        },
        'mong_doi': {
            'has_data_science': True,
            'has_IT': False,
            'search_IoT': 11,
            'search_machine_learning': 27,
            'len_sau_xoa': 5
        },
        'ham': lambda d: thuc_hanh_03(d),
        'format': lambda d, kq: (
            f"Kiểm tra sự tồn tại ('data science' in ht): {kq['has_data_science']}\n"
            f"Kiểm tra sự tồn tại ('IT' in ht): {kq['has_IT']}\n"
            f"Gọi hàm ht.search('IoT'): {kq['search_IoT']}\n"
            f"Gọi hàm ht.search('machine learning'): {kq['search_machine_learning']}\n"
            f"Tổng kích thước thực tế (len) sau khi chèn thêm 'big data' và xóa 'IoT': {kq['len_sau_xoa']}"
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*60}\n {cfg['ten']}\n{'='*60}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    print(f"\nKết quả mong đợi:\n{cfg['mong_doi']}")
    if kq == cfg['mong_doi']:
        print("\nTrạng thái: THÀNH CÔNG")
    else:
        print("\nTrạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*60)
            print(" MENU: HASH TABLE (BẢNG BĂM) - ĐÃ ĐƯỢC TỐI ƯU")
            print(" CHỌN BÀI (1-3) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*60)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        pass