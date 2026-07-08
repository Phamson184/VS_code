from typing import List, Dict, Any, Tuple

class FixedStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.capacity

    def push(self, item: Any):
        # Bài 4: Báo lỗi Overflow khi đầy
        if self.is_full():
            raise OverflowError("Overflow: Ngăn xếp đã đầy!")
        self.stack.append(item)

    def pop(self) -> Any:
        # Bài 4: Báo lỗi Underflow khi rỗng
        if self.is_empty():
            raise IndexError("Underflow: Ngăn xếp đang rỗng!")
        return self.stack.pop()

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError("Underflow: Ngăn xếp đang rỗng!")
        return self.stack[-1]

def bai_1_va_4_stack_co_ban(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    st = FixedStack(capacity=du_lieu['capacity'])
    ket_qua_pop = []
    loi_xay_ra = []
    
    for lenh in du_lieu['lenh']:
        try:
            if lenh.startswith('push'):
                val = int(lenh.split()[1])
                st.push(val)
            elif lenh == 'pop':
                ket_qua_pop.append(st.pop())
        except Exception as e:
            loi_xay_ra.append(str(e))
            
    return {
        'trang_thai_cuoi': st.stack,
        'da_pop': ket_qua_pop,
        'loi_thu_duoc': loi_xay_ra
    }

# --- Bài 2: Đảo ngược chuỗi ---
def bai_2_dao_nguoc_chuoi(du_lieu: Dict[str, Any]) -> str:
    s = du_lieu['chuoi']
    stack = list(s) # Đưa toàn bộ ký tự vào stack (Push)
    chuoi_dao = ""
    while stack:
        chuoi_dao += stack.pop() # Lấy ra theo thứ tự ngược lại
    return chuoi_dao

# --- Bài 3: Mô phỏng dãy thao tác ---
def bai_3_mo_phong(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    stack = []
    log_pop = []
    for thao_tac in du_lieu['thao_tac']:
        if thao_tac.startswith("push"):
            stack.append(int(thao_tac.split()[1]))
        elif thao_tac == "pop":
            if stack:
                log_pop.append(stack.pop())
    return {
        'log_pop': log_pop,
        'stack_cuoi': stack
    }

# --- Bài 5: Duyệt và đếm phần tử (Không làm mất Stack gốc) ---
def bai_5_duyet_khong_mat_du_lieu(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    # Khởi tạo stack gốc
    stack_goc = du_lieu['stack_ban_dau'][:]
    stack_phu = []
    
    # 1. Duyệt từ đỉnh xuống đáy (LIFO) và đưa sang stack phụ
    duyet_lifo = []
    dem = 0
    while stack_goc:
        phan_tu = stack_goc.pop()
        duyet_lifo.append(phan_tu)
        stack_phu.append(phan_tu)
        dem += 1
        
    # 2. Khôi phục lại stack gốc từ đáy lên đỉnh
    while stack_phu:
        stack_goc.append(stack_phu.pop())
        
    return {
        'so_luong': dem,
        'thu_tu_in': duyet_lifo,
        'trang_thai_goc_sau_cung': stack_goc
    }

# --- Bài 6: Dấu ngoặc cân bằng ---
def bai_6_ngoac_can_bang(du_lieu: Dict[str, Any]) -> bool:
    chuoi = du_lieu['chuoi']
    stack = []
    cap_ngoac = {')': '(', ']': '[', '}': '{'}
    
    for char in chuoi:
        if char in cap_ngoac.values():
            stack.append(char)
        elif char in cap_ngoac.keys():
            if not stack or stack.pop() != cap_ngoac[char]:
                return False
    return len(stack) == 0

# --- Bài 7: Min Stack O(1) ---
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] # Stack phụ chỉ lưu các giá trị Minimum

    def push(self, val: int):
        self.stack.append(val)
        # Nếu min_stack rỗng hoặc giá trị mới <= giá trị Min hiện tại
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            # Nếu giá trị bị lấy ra chính là giá trị Min hiện tại
            if val == self.min_stack[-1]:
                self.min_stack.pop()
                
    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1

def bai_7_min_stack(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    ms = MinStack()
    log = []
    for lenh in du_lieu['lenh']:
        if lenh.startswith('push'):
            ms.push(int(lenh.split()[1]))
        elif lenh == 'pop':
            ms.pop()
        elif lenh == 'getMin':
            log.append(ms.get_min())
    return {'log_getMin': log, 'stack_cuoi': ms.stack}

Noidung = {
    '1': {
        'ten': 'BÀI 1 & BÀI 4: CÀI ĐẶT NGĂN XẾP & BẮT LỖI OVERFLOW/UNDERFLOW',
        'du_lieu': {'capacity': 3, 'lenh': ['push 10', 'push 20', 'push 30', 'push 40', 'pop', 'pop', 'pop', 'pop']},
        'mong_doi': 'Kiểm tra lỗi hiển thị',
        'ham': lambda d: bai_1_va_4_stack_co_ban(d),
        'format': lambda d, kq: (
            f"Sức chứa mảng tĩnh: {d['capacity']}\n"
            f"Chuỗi lệnh chạy: {d['lenh']}\n\n"
            f"- Đã lấy ra (Pop): {kq['da_pop']}\n"
            f"- Trạng thái cuối: {kq['trang_thai_cuoi']}\n"
            f"- Lỗi bắt được:\n" + "\n".join(f"  [!] {loi}" for loi in kq['loi_thu_duoc']) + "\n"
            f"\n[*] NHẬN XÉT: Lệnh 'push 40' gây Overflow vì mảng chỉ chứa 3 phần tử. \n"
            f"    Lệnh 'pop' cuối cùng gây Underflow vì Stack đã rỗng."
        )
    },
    '2': {
        'ten': 'BÀI 2: ĐẢO NGƯỢC CHUỖI',
        'du_lieu': {'chuoi': 'Hello World'},
        'mong_doi': 'dlroW olleH',
        'ham': lambda d: bai_2_dao_nguoc_chuoi(d),
        'format': lambda d, kq: f"Chuỗi gốc: '{d['chuoi']}'\n=> Sau khi qua Stack: '{kq}'"
    },
    '3': {
        'ten': 'BÀI 3: MÔ PHỎNG DÃY THAO TÁC',
        'du_lieu': {'thao_tac': ['push 5', 'push 7', 'pop', 'push 9', 'pop']},
        'mong_doi': {'log_pop': [7, 9], 'stack_cuoi': [5]},
        'ham': lambda d: bai_3_mo_phong(d),
        'format': lambda d, kq: (
            f"Các lệnh: {d['thao_tac']}\n"
            f"- Nhật ký in khi Pop: {kq['log_pop']}\n"
            f"- Stack còn lại cuối cùng: {kq['stack_cuoi']}"
        )
    },
    '5': {
        'ten': 'BÀI 5: DUYỆT VÀ ĐẾM KHÔNG LÀM MẤT DỮ LIỆU',
        'du_lieu': {'stack_ban_dau': [1, 2, 3, 4, 5]},
        'mong_doi': {'so_luong': 5, 'thu_tu_in': [5, 4, 3, 2, 1], 'trang_thai_goc_sau_cung': [1, 2, 3, 4, 5]},
        'ham': lambda d: bai_5_duyet_khong_mat_du_lieu(d),
        'format': lambda d, kq: (
            f"Stack ban đầu (Đáy -> Đỉnh): {d['stack_ban_dau']}\n"
            f"- Số lượng đếm được: {kq['so_luong']}\n"
            f"- Thứ tự duyệt (Đỉnh -> Đáy): {kq['thu_tu_in']}\n"
            f"- Trạng thái Stack gốc sau khi duyệt: {kq['trang_thai_goc_sau_cung']}\n"
            f"[*] Bằng cách dùng 1 Stack phụ tạm thời chứa dữ liệu bị đẩy ra, ta dễ dàng khôi phục lại Stack gốc."
        )
    },
    '6': {
        'ten': 'BÀI 6: KIỂM TRA DẤU NGOẶC CÂN BẰNG',
        'du_lieu': {'chuoi': '([]{})'},
        'mong_doi': True,
        'ham': lambda d: bai_6_ngoac_can_bang(d),
        'format': lambda d, kq: (
            f"Chuỗi kiểm tra: '{d['chuoi']}'\n"
            f"=> Kết quả: {'Hợp lệ (True)' if kq else 'Không hợp lệ (False)'}\n"
            f"[*] Khi gặp ngoặc mở thì Push. Khi gặp ngoặc đóng thì Pop và đối chiếu sự trùng khớp."
        )
    },
    '7': {
        'ten': 'BÀI 7: MIN STACK (GET_MIN VỚI ĐỘ PHỨC TẠP O(1))',
        'du_lieu': {'lenh': ['push 5', 'push 3', 'getMin', 'push 7', 'getMin', 'pop', 'pop', 'getMin']},
        'mong_doi': {'log_getMin': [3, 3, 5], 'stack_cuoi': [5]},
        'ham': lambda d: bai_7_min_stack(d),
        'format': lambda d, kq: (
            f"Kịch bản thao tác: {d['lenh']}\n"
            f"- Lịch sử trả về khi gọi getMin(): {kq['log_getMin']}\n"
            f"- Stack thực tế cuối cùng: {kq['stack_cuoi']}\n"
            f"[*] Bí quyết O(1) là duy trì song song một Min_Stack chỉ lưu lại giá trị Kỷ lục nhỏ nhất mỗi khi nó xuất hiện."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] != 'Kiểm tra lỗi hiển thị':
        print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 1 (STACK - BÀI 1 -> BÀI 7)")
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
