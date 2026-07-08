from typing import List, Dict, Any, Tuple

# ==========================================
# MODULE A2 & A3: ARRAY LIST (BÀI 8 ĐẾN BÀI 15)
# ==========================================

# --- Bài 8: Xóa các phần tử thỏa điều kiện (In-place O(n)) ---
def bai_8_xoa_theo_dieu_kien(du_lieu: Dict[str, Any]) -> List[int]:
    arr = du_lieu['arr'][:]
    # Kỹ thuật hai con trỏ (Đọc và Ghi)
    write_idx = 0
    for read_idx in range(len(arr)):
        # Nếu KHÔNG thỏa mãn điều kiện xóa (VD: xóa số chẵn -> giữ số lẻ)
        if arr[read_idx] % 2 != 0: 
            arr[write_idx] = arr[read_idx]
            write_idx += 1
            
    # Cắt bỏ phần dư thừa phía sau
    return arr[:write_idx]

# --- Bài 9: Đảo ngược tại chỗ (In-place O(n) thời gian, O(1) bộ nhớ) ---
def bai_9_dao_nguoc_tai_cho(du_lieu: Dict[str, Any]) -> List[int]:
    arr = du_lieu['arr'][:]
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr

# --- Bài 10: Trộn hai danh sách đã sắp xếp ---
def bai_10_tron_2_list(du_lieu: Dict[str, Any]) -> List[int]:
    arr1 = du_lieu['arr1']
    arr2 = du_lieu['arr2']
    p1, p2 = 0, 0
    merged = []
    
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1
            
    # Đưa phần còn dư vào mảng (nếu có)
    merged.extend(arr1[p1:])
    merged.extend(arr2[p2:])
    return merged

# --- Bài 11: Xoay mảng k vị trí (Tuyệt chiêu đảo 3 lần) ---
def bai_11_xoay_mang_k_vi_tri(du_lieu: Dict[str, Any]) -> List[int]:
    arr = du_lieu['arr'][:]
    k = du_lieu['k']
    n = len(arr)
    if n == 0: return arr
    k = k % n # Đảm bảo k không vượt quá n
    
    def reverse(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
            
    # 1. Đảo ngược toàn bộ mảng
    reverse(arr, 0, n - 1)
    # 2. Đảo ngược k phần tử đầu
    reverse(arr, 0, k - 1)
    # 3. Đảo ngược phần còn lại
    reverse(arr, k, n - 1)
    
    return arr

# --- Bài 12: Loại bỏ trùng lặp giữ nguyên thứ tự (Dùng Hash Set O(n)) ---
def bai_12_loai_bo_trung_lap(du_lieu: Dict[str, Any]) -> List[int]:
    arr = du_lieu['arr']
    seen = set()
    result = []
    
    for val in arr:
        if val not in seen:
            seen.add(val)
            result.append(val)
            
    return result

# --- Bài 13: Trộn các khoảng (Merge Intervals) ---
def bai_13_merge_intervals(du_lieu: Dict[str, Any]) -> List[List[int]]:
    intervals = [iv[:] for iv in du_lieu['intervals']]
    intervals = du_lieu['intervals']
    if not intervals: return []
    
    # B1: Sắp xếp theo điểm bắt đầu
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for curr in intervals[1:]:
        last_merged = merged[-1]
        # B2: Giao nhau -> Cập nhật điểm kết thúc của khoảng trước đó
        if curr[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], curr[1])
        else:
            merged.append(curr)
            
    return merged

# --- Bài 14: Mảng động 2 chiều ---
class DynamicMatrix:
    def __init__(self):
        self.matrix = []

    def add_row(self, row: List[Any]):
        self.matrix.append(row[:])  # Copy tránh mutation

    def add_col(self, col_data: List[Any]):
        # Cần số lượng phần tử bằng với số hàng hiện tại
        for i in range(len(self.matrix)):
            val = col_data[i] if i < len(col_data) else 0
            self.matrix[i].append(val)

    def get(self, r: int, c: int) -> Any:
        return self.matrix[r][c]

    def set(self, r: int, c: int, val: Any):
        self.matrix[r][c] = val

def bai_14_mang_dong_2_chieu(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    mat = DynamicMatrix()
    for row in du_lieu['rows']:
        mat.add_row(row)
        
    mat.add_col(du_lieu['new_col'])
    mat.set(0, 0, 99)
    
    return {
        'gia_tri_0_0': mat.get(0, 0),
        'ma_tran_hien_tai': mat.matrix
    }

# --- Bài 15: Iterator và Fail-fast ---
class FailFastList:
    def __init__(self, items: List[int]):
        self.data = items
        self.mod_count = 0 # Bộ đếm số lần cấu trúc bị thay đổi

    def add(self, val: int):
        self.data.append(val)
        self.mod_count += 1

    def remove(self) -> int:
        self.mod_count += 1
        return self.data.pop()

    def get_iterator(self):
        # Trả về một generator (Iterator) ghi nhớ mod_count lúc khởi tạo
        expected_mod_count = self.mod_count
        for item in self.data:
            if self.mod_count != expected_mod_count:
                raise RuntimeError("ConcurrentModificationException: Danh sách bị thay đổi trong lúc đang duyệt!")
            yield item

def bai_15_fail_fast(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ff_list = FailFastList([1, 2, 3])
    log = []
    loi = []
    
    try:
        iterator = ff_list.get_iterator()
        log.append(next(iterator)) # Lấy phần tử đầu tiên (1)
        
        # Cố tình thay đổi cấu trúc mảng trong lúc duyệt
        ff_list.add(4) 
        
        log.append(next(iterator)) # Cố gắng lấy phần tử tiếp theo sẽ văng lỗi ngay
    except Exception as e:
        loi.append(str(e))
        
    return {'log_duyet': log, 'loi': loi}

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '8': {
        'ten': 'BÀI 8: XÓA PHẦN TỬ IN-PLACE (HAI CON TRỎ)',
        'du_lieu': {'arr': [1, 2, 3, 4, 5, 6]},
        'mong_doi': [1, 3, 5],
        'ham': lambda d: bai_8_xoa_theo_dieu_kien(d),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['arr']}\n"
            f"=> Mảng sau khi xóa số chẵn: {kq}\n"
            f"[*] Không cấp phát mảng phụ, tận dụng con trỏ ghi đè lên ngay chính mảng gốc."
        )
    },
    '9': {
        'ten': 'BÀI 9: ĐẢO NGƯỢC TẠI CHỖ',
        'du_lieu': {'arr': [1, 2, 3, 4]},
        'mong_doi': [4, 3, 2, 1],
        'ham': lambda d: bai_9_dao_nguoc_tai_cho(d),
        'format': lambda d, kq: f"Mảng gốc: {d['arr']}\n=> Đảo ngược (Swap 2 đầu): {kq}"
    },
    '10': {
        'ten': 'BÀI 10: TRỘN HAI DANH SÁCH ĐÃ SẮP XẾP',
        'du_lieu': {'arr1': [1, 3, 5], 'arr2': [2, 4]},
        'mong_doi': [1, 2, 3, 4, 5],
        'ham': lambda d: bai_10_tron_2_list(d),
        'format': lambda d, kq: f"L1: {d['arr1']} | L2: {d['arr2']}\n=> Trộn: {kq}"
    },
    '11': {
        'ten': 'BÀI 11: XOAY MẢNG K VỊ TRÍ (RIGHT SHIFT)',
        'du_lieu': {'arr': [1, 2, 3, 4, 5], 'k': 2},
        'mong_doi': [4, 5, 1, 2, 3],
        'ham': lambda d: bai_11_xoay_mang_k_vi_tri(d),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['arr']} | Xoay phải k = {d['k']}\n"
            f"=> Kết quả: {kq}\n"
            f"[*] Kỹ thuật Reverse 3 lần: Toàn bộ -> K phần tử đầu -> Phần còn lại. O(n) thời gian, O(1) không gian."
        )
    },
    '12': {
        'ten': 'BÀI 12: LOẠI BỎ TRÙNG LẶP (GIỮ THỨ TỰ)',
        'du_lieu': {'arr': [3, 1, 3, 2, 1]},
        'mong_doi': [3, 1, 2],
        'ham': lambda d: bai_12_loai_bo_trung_lap(d),
        'format': lambda d, kq: f"Mảng gốc: {d['arr']}\n=> Lọc trùng (Dùng Hash Set): {kq}"
    },
    '13': {
        'ten': 'BÀI 13: TRỘN CÁC KHOẢNG (MERGE INTERVALS)',
        'du_lieu': {'intervals': [[1, 3], [2, 6], [8, 10], [15, 18]]},
        'mong_doi': [[1, 6], [8, 10], [15, 18]],
        'ham': lambda d: bai_13_merge_intervals(d),
        'format': lambda d, kq: (
            f"Các khoảng ban đầu: {d['intervals']}\n"
            f"=> Giao nhau được gộp lại: {kq}"
        )
    },
    '14': {
        'ten': 'BÀI 14: MẢNG ĐỘNG 2 CHIỀU (DYNAMIC MATRIX)',
        'du_lieu': {
            'rows': [[1, 2], [3, 4]],
            'new_col': [5, 6]
        },
        'mong_doi': 'So khớp cấu trúc',
        'ham': lambda d: bai_14_mang_dong_2_chieu(d),
        'format': lambda d, kq: (
            f"Ma trận ban đầu: {d['rows']}\n"
            f"- Thêm cột mới: {d['new_col']}\n"
            f"- Set lại giá trị tại (0,0) = 99\n"
            f"=> Ma trận hiện tại:\n  " + "\n  ".join(str(r) for r in kq['ma_tran_hien_tai'])
        )
    },
    '15': {
        'ten': 'BÀI 15: CƠ CHẾ FAIL-FAST TRONG ITERATOR',
        'du_lieu': {},
        'mong_doi': 'Kiểm tra ngoại lệ',
        'ham': lambda d: bai_15_fail_fast(d),
        'format': lambda d, kq: (
            f"Khởi tạo mảng: [1, 2, 3]. Tạo Iterator.\n"
            f"1. Lấy phần tử đầu tiên thành công: {kq['log_duyet']}\n"
            f"2. Người dùng ngầm add(4) vào mảng.\n"
            f"3. Cố lấy phần tử tiếp theo từ Iterator ban đầu...\n"
            f"=> LỖI: {kq['loi'][0]}\n"
            f"[*] Bằng cách so sánh modCount, Iterator bảo vệ an toàn dữ liệu, chống lại việc mảng bị sửa lén."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] not in ['So khớp cấu trúc', 'Kiểm tra ngoại lệ']:
        print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 2 (ARRAY LIST - BÀI 8 -> BÀI 15)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
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