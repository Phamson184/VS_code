from typing import List, Dict, Any, Tuple

# ==========================================
# MODULE A1: ARRAY LIST CƠ BẢN (BÀI 1 ĐẾN BÀI 7)
# ==========================================

class CustomArrayList:
    """Mô phỏng cấu trúc danh sách mảng động (Dynamic Array) từ mảng tĩnh."""
    def __init__(self, initial_capacity: int = 2):
        self.capacity = initial_capacity
        self.size_ = 0
        # Mảng nội bộ (Internal array) cấp phát sẵn bộ nhớ tĩnh
        self.array = [None] * self.capacity
        self.log_resize = [] # Theo dõi lịch sử nhân đôi mảng cho Bài 6

    def size(self) -> int:
        return self.size_

    def get(self, index: int) -> Any:
        if index < 0 or index >= self.size_:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index: int, val: Any):
        if index < 0 or index >= self.size_:
            raise IndexError("Index out of bounds")
        self.array[index] = val

    def _resize(self, new_capacity: int):
        """Mở rộng dung lượng mảng khi bị đầy (Bài 6)."""
        self.log_resize.append(f"Resized: {self.capacity} -> {new_capacity}")
        new_array = [None] * new_capacity
        # Copy O(n)
        for i in range(self.size_):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, val: Any):
        """Thêm vào cuối (Bài 2)."""
        if self.size_ == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size_] = val
        self.size_ += 1

    def pop_back(self) -> Any:
        """Xóa ở cuối (Bài 2)."""
        if self.size_ == 0:
            raise IndexError("Pop from empty list")
        val = self.array[self.size_ - 1]
        self.array[self.size_ - 1] = None # Hủy tham chiếu
        self.size_ -= 1
        return val

    def insert(self, index: int, val: Any):
        """Chèn tại vị trí bất kỳ (Bài 3)."""
        if index < 0 or index > self.size_:
            raise IndexError("Index out of bounds")
        if self.size_ == self.capacity:
            self._resize(self.capacity * 2)
            
        # Shift các phần tử sang phải O(n)
        for i in range(self.size_, index, -1):
            self.array[i] = self.array[i - 1]
            
        self.array[index] = val
        self.size_ += 1

    def remove_at(self, index: int) -> Any:
        """Xóa tại vị trí bất kỳ (Bài 3)."""
        if index < 0 or index >= self.size_:
            raise IndexError("Index out of bounds")
        val = self.array[index]
        
        # Shift các phần tử sang trái O(n)
        for i in range(index, self.size_ - 1):
            self.array[i] = self.array[i + 1]
            
        self.array[self.size_ - 1] = None
        self.size_ -= 1
        return val

    def index_of(self, val: Any) -> int:
        """Tìm kiếm tuyến tính (Bài 4)."""
        for i in range(self.size_):
            if self.array[i] == val:
                return i
        return -1

    def to_list(self) -> List[Any]:
        """Hàm hỗ trợ in ấn (Trích xuất các phần tử thực sự có dữ liệu)."""
        return self.array[:self.size_]


# --- CÁC HÀM XỬ LÝ (WRAPPER) CHO TỪNG BÀI TẬP ---

def bai_1_cai_dat_co_ban(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    arr = CustomArrayList(initial_capacity=5)
    for v in du_lieu['adds']:
        arr.append(v)
    return {
        'list': arr.to_list(),
        'get_idx_1': arr.get(du_lieu['get_idx'])
    }

def bai_2_them_xoa_cuoi(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    arr = CustomArrayList()
    for v in du_lieu['initial']:
        arr.append(v)
    val_popped = arr.pop_back()
    return {
        'val_popped': val_popped,
        'list_sau_pop': arr.to_list()
    }

def bai_3_chen_xoa_bat_ky(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    arr = CustomArrayList()
    for v in du_lieu['initial']:
        arr.append(v)
    # Chèn
    arr.insert(du_lieu['insert_idx'], du_lieu['insert_val'])
    list_sau_chen = arr.to_list()
    # Xóa
    val_removed = arr.remove_at(du_lieu['remove_idx'])
    
    return {
        'list_sau_chen': list_sau_chen,
        'val_removed': val_removed,
        'list_sau_xoa': arr.to_list()
    }

def bai_4_tim_kiem_tuyen_tinh(du_lieu: Dict[str, Any]) -> int:
    arr = CustomArrayList()
    for v in du_lieu['arr']:
        arr.append(v)
    return arr.index_of(du_lieu['target'])

def bai_5_duyet_va_dem(du_lieu: Dict[str, Any]) -> int:
    arr = CustomArrayList()
    for v in du_lieu['arr']:
        arr.append(v)
        
    dem_chan = 0
    # Mô phỏng duyệt mảng
    for i in range(arr.size()):
        if arr.get(i) % 2 == 0:
            dem_chan += 1
    return dem_chan

def bai_6_tu_dong_mo_rong(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    # Khởi tạo mảng có sức chứa ban đầu rất nhỏ (capacity = 2)
    arr = CustomArrayList(initial_capacity=2)
    
    # Nạp 5 phần tử để ép mảng phải resize 2 lần (2 -> 4 -> 8)
    for v in du_lieu['adds']:
        arr.append(v)
        
    return {
        'final_capacity': arr.capacity,
        'final_size': arr.size(),
        'log_resize': arr.log_resize
    }

def bai_7_phan_tich_amortized() -> str:
    return (
        "PHÂN TÍCH CHI PHÍ KHẤU HAO (AMORTIZED ANALYSIS) CỦA APPEND:\n"
        "- Đa số các lần gọi append(): Mảng vẫn còn chỗ trống, việc gán giá trị tốn O(1).\n"
        "- Khi mảng đầy (size == capacity): Cần cấp phát mảng mới (gấp đôi mảng cũ) và sao chép n phần tử. Lúc này tốn O(n).\n"
        "- Tuy nhiên, nhờ việc nhân đôi (x2) dung lượng, sau mỗi lần tốn O(n), ta có thêm n ô trống. "
        "Nghĩa là n lần append tiếp theo sẽ tốn đúng O(1).\n"
        "- Trung bình lại: (Chi phí O(n) + n lần O(1)) / n thao tác = O(1).\n"
        "=> Kết luận: Thao tác thêm vào cuối mảng động cực kỳ hiệu quả, chi phí trung bình luôn là O(1)."
    )

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '1': {
        'ten': 'BÀI 1: CÀI ĐẶT ARRAY LIST CƠ BẢN',
        'du_lieu': {'adds': [1, 2, 3], 'get_idx': 1},
        'mong_doi': {'list': [1, 2, 3], 'get_idx_1': 2},
        'ham': lambda d: bai_1_cai_dat_co_ban(d),
        'format': lambda d, kq: f"Lệnh: add {d['adds']}, gọi get({d['get_idx']})\n=> Giá trị trả về: {kq['get_idx_1']}"
    },
    '2': {
        'ten': 'BÀI 2: THÊM / XÓA Ở CUỐI MẢNG',
        'du_lieu': {'initial': [1, 2, 3]},
        'mong_doi': {'val_popped': 3, 'list_sau_pop': [1, 2]},
        'ham': lambda d: bai_2_them_xoa_cuoi(d),
        'format': lambda d, kq: f"Mảng gốc: {d['initial']}\n=> Gọi popBack() lấy ra: {kq['val_popped']}\n=> Mảng còn lại: {kq['list_sau_pop']}"
    },
    '3': {
        'ten': 'BÀI 3: CHÈN / XÓA Ở VỊ TRÍ BẤT KỲ (O(n))',
        'du_lieu': {'initial': [1, 2, 4], 'insert_idx': 2, 'insert_val': 3, 'remove_idx': 0},
        'mong_doi': {'list_sau_chen': [1, 2, 3, 4], 'val_removed': 1, 'list_sau_xoa': [2, 3, 4]},
        'ham': lambda d: bai_3_chen_xoa_bat_ky(d),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['initial']}\n"
            f"- Chèn {d['insert_val']} tại index {d['insert_idx']} -> {kq['list_sau_chen']}\n"
            f"- Xóa tại index {d['remove_idx']} (lấy ra số {kq['val_removed']}) -> {kq['list_sau_xoa']}\n"
            f"[*] Việc chèn/xóa ở giữa mảng đòi hỏi phải dịch chuyển (shift) các phần tử nên tốn O(n)."
        )
    },
    '4': {
        'ten': 'BÀI 4: TÌM KIẾM TUYẾN TÍNH (INDEX_OF)',
        'du_lieu': {'arr': [5, 3, 7, 9], 'target': 7},
        'mong_doi': 2,
        'ham': lambda d: bai_4_tim_kiem_tuyen_tinh(d),
        'format': lambda d, kq: f"Mảng: {d['arr']} | Tìm giá trị: {d['target']}\n=> Vị trí index đầu tiên: {kq}"
    },
    '5': {
        'ten': 'BÀI 5: DUYỆT VÀ ĐẾM PHẦN TỬ THỎA ĐIỀU KIỆN',
        'du_lieu': {'arr': [1, 2, 3, 4]},
        'mong_doi': 2,
        'ham': lambda d: bai_5_duyet_va_dem(d),
        'format': lambda d, kq: f"Mảng duyệt: {d['arr']}\n=> Đếm số phần tử chẵn: {kq}"
    },
    '6': {
        'ten': 'BÀI 6: TỰ ĐỘNG MỞ RỘNG DUNG LƯỢNG (RESIZING)',
        'du_lieu': {'adds': [10, 20, 30, 40, 50]},
        'mong_doi': {'final_capacity': 8, 'final_size': 5, 'log_resize': ['Resized: 2 -> 4', 'Resized: 4 -> 8']},
        'ham': lambda d: bai_6_tu_dong_mo_rong(d),
        'format': lambda d, kq: (
            f"Mảng tĩnh ban đầu có Capacity = 2. Nạp liên tục 5 phần tử: {d['adds']}\n"
            f"- Nhật ký hệ thống tự động mở rộng:\n  " + "\n  ".join(kq['log_resize']) + "\n"
            f"- Kích thước thực tế (Size): {kq['final_size']}\n"
            f"- Sức chứa hiện tại của mảng (Capacity): {kq['final_capacity']}"
        )
    },
    '7': {
        'ten': 'BÀI 7: PHÂN TÍCH AMORTIZED CỦA APPEND',
        'du_lieu': {},
        'mong_doi': 'In lý thuyết',
        'ham': lambda d: bai_7_phan_tich_amortized(),
        'format': lambda d, kq: kq
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] != 'In lý thuyết':
        print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 1 (ARRAY LIST - BÀI 1 -> BÀI 7)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            # Sắp xếp key menu
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