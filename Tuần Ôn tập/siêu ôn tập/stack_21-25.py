from typing import List, Dict, Any

# --- LOGIC THUẬT TOÁN ---

def bai21_ngoac_can_bang(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values(): stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]: return False
    return not stack

class MinStack:
    def __init__(self): self.s, self.ms = [], []
    def push(self, x):
        self.s.append(x)
        if not self.ms or x <= self.ms[-1]: self.ms.append(x)
    def pop(self):
        if self.s.pop() == self.ms[-1]: self.ms.pop()
    def getMin(self): return self.ms[-1]

def bai23_rpn(tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': stack.append(int(a / b))
        else: stack.append(int(t))
    return stack[0]

def bai24_next_greater(a: List[int]) -> List[int]:
    n = len(a)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[i] > a[stack[-1]]:
            res[stack.pop()] = a[i]
        stack.append(i)
    return res

def bai25_histogram(h: List[int]) -> int:
    h.append(0)
    stack = [-1]
    max_a = 0
    for i, height in enumerate(h):
        while stack[-1] != -1 and height < h[stack[-1]]:
            max_a = max(max_a, h[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    h.pop()
    return max_a

# --- MENU DATA-DRIVEN ---
Noidung = {
    '21': {'ten': 'CÂU 21: NGOẶC CÂN BẰNG', 'du_lieu': '([]{})', 'ham': bai21_ngoac_can_bang, 'format': lambda d, k: f"'{d}' cân bằng: {k}"},
    '22': {'ten': 'CÂU 22: MIN STACK O(1)', 'du_lieu': ['push 5', 'push 3', 'getMin', 'pop', 'getMin'], 'ham': lambda d: [MinStack()], 'format': "Thiết kế class hỗ trợ getMin() O(1) [cite: 379-381]."},
    '23': {'ten': 'CÂU 23: TÍNH RPN', 'du_lieu': ['3', '4', '+', '2', '*'], 'ham': bai23_rpn, 'format': lambda d, k: f"RPN: {d} = {k}"},
    '24': {'ten': 'CÂU 24: NEXT GREATER ELEMENT', 'du_lieu': [2, 1, 3], 'ham': bai24_next_greater, 'format': lambda d, k: f"{d} -> {k}"},
    '25': {'ten': 'CÂU 25: HISTOGRAM LỚN NHẤT', 'du_lieu': [2, 1, 5, 6, 2, 3], 'ham': bai25_histogram, 'format': lambda d, k: f"{d} -> Area: {k}"}
}

def chay_bai(k):
    cfg = Noidung[k]
    print(f"\n--- {cfg['ten']} ---")
    if k == '22': print(cfg['format'])
    else: print(cfg['format'](cfg['du_lieu'], cfg['ham'](cfg['du_lieu'])))
# ==========================================
# KHỐI ĐIỀU KHIỂN & MENU TƯƠNG TÁC
# ==========================================
def chay_bai_tu_dong(key_bai: str, tap_du_lieu: dict):
    if key_bai not in tap_du_lieu:
        return
    cfg = tap_du_lieu[key_bai]
    print(f"\n{'='*75}")
    print(f" {cfg['ten']}")
    print(f"{'='*75}")

    try:
        # Xử lý chạy hàm (có hoặc không có dữ liệu)
        if 'du_lieu' in cfg and cfg['du_lieu'] is not None:
            kq = cfg['ham'](cfg['du_lieu'])
            d = cfg['du_lieu']
        else:
            kq = cfg['ham']()
            d = None

        # Xử lý in kết quả theo format cấu hình
        fmt = cfg.get('format')
        if callable(fmt):
            try:
                print(fmt(d, kq))
            except TypeError:
                print(fmt(kq))
        elif isinstance(fmt, str):
            print(fmt)
        else:
            print(f"Kết quả: {kq}")

    except Exception as e:
        print(f"[!] Lỗi thực thi: {e}")

if __name__ == '__main__':
    try:
        # Tự động nhận diện tên biến cấu hình của file hiện tại (Noidung hoặc NoidungQ)
        dict_noidung = None
        if 'Noidung' in globals(): 
            dict_noidung = globals()['Noidung']
        elif 'NoidungQ' in globals(): 
            dict_noidung = globals()['NoidungQ']
        
        if not dict_noidung:
            print("Lỗi: Không tìm thấy từ điển cấu hình Noidung hoặc NoidungQ.")
            exit()

        danh_sach_keys = sorted(dict_noidung.keys(), key=lambda x: int(x))
        
        while True:
            print("\n" + "*"*75)
            print(f" MENU ĐIỀU KHIỂN (CÁC CÂU: {danh_sach_keys[0]} -> {danh_sach_keys[-1]})")
            print(" NHẬP MÃ CÂU HOẶC '0' ĐỂ THOÁT | 'all' ĐỂ CHẠY TOÀN BỘ")
            print("*"*75)
            for k in danh_sach_keys:
                print(f" {k:>3}. {dict_noidung[k]['ten']}")
            
            chon = input("\nLựa chọn của bạn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in danh_sach_keys: 
                    chay_bai_tu_dong(k, dict_noidung)
            elif chon in dict_noidung:
                chay_bai_tu_dong(chon, dict_noidung)
            else:
                print("\n[!] Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
        print("\nĐã thoát chương trình.")