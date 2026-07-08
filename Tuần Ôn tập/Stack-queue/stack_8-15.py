from typing import List, Dict, Any
from collections import deque

# ==========================================
# MODULE A2 & A3: NGĂN XẾP (STACK) - BÀI 8 ĐẾN BÀI 15
# ==========================================

# --- Bài 8: Tính biểu thức hậu tố (RPN) ---
def bai_8_tinh_hau_to(du_lieu: Dict[str, Any]) -> int:
    tokens = du_lieu['bieu_thuc'].split()
    stack = []
    
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b)) # Chia lấy phần nguyên trong Python
            
    return stack[0]

# --- Bài 9: Chuyển trung tố sang hậu tố (Shunting-yard) ---
def bai_9_trung_to_sang_hau_to(du_lieu: Dict[str, Any]) -> str:
    bieu_thuc = du_lieu['bieu_thuc']
    do_uu_tien = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    
    for char in bieu_thuc:
        if char.isalnum():  # Toán hạng (chữ cái/số)
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() # Bỏ dấu '('
        else: # Toán tử
            while stack and stack[-1] != '(' and do_uu_tien.get(char, 0) <= do_uu_tien.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
            
    while stack:
        output.append(stack.pop())
        
    return "".join(output)

# --- Bài 10: Cài đặt ngăn xếp bằng 2 hàng đợi ---
class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int):
        self.q1.append(x) # Chi phí O(1)

    def pop(self) -> int:
        if not self.q1:
            return -1
        # Chuyển n-1 phần tử sang q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Phần tử cuối cùng chính là đỉnh Stack
        res = self.q1.popleft()
        # Hoán đổi q1 và q2
        self.q1, self.q2 = self.q2, self.q1
        return res # Chi phí O(n)

def bai_10_stack_bang_2_queue(du_lieu: Dict[str, Any]) -> List[int]:
    sq = StackUsingQueues()
    ket_qua = []
    for lenh in du_lieu['lenh']:
        if lenh.startswith('push'):
            sq.push(int(lenh.split()[1]))
        elif lenh == 'pop':
            ket_qua.append(sq.pop())
    return ket_qua

# --- Bài 11: Phần tử lớn hơn kế tiếp (Monotonic Stack) ---
def bai_11_next_greater_element(du_lieu: Dict[str, Any]) -> List[int]:
    a = du_lieu['mang']
    n = len(a)
    ket_qua = [-1] * n
    stack = [] # Lưu CHỈ SỐ (index) của các phần tử đang chờ tìm giá trị lớn hơn
    
    for i in range(n):
        # Nếu phần tử hiện tại lớn hơn phần tử ở đỉnh stack -> đã tìm thấy Next Greater
        while stack and a[i] > a[stack[-1]]:
            idx = stack.pop()
            ket_qua[idx] = a[i]
        stack.append(i)
        
    return ket_qua

# --- Bài 12: Hình chữ nhật lớn nhất trong Histogram ---
def bai_12_largest_rectangle(du_lieu: Dict[str, Any]) -> int:
    h = du_lieu['chieu_cao']
    h.append(0) # Thêm cột 0 vào cuối để ép stack pop hết ra ở vòng lặp cuối
    stack = [-1] # Lưu chỉ số, -1 làm biên trái ảo
    max_area = 0
    
    for i in range(len(h)):
        # Đảm bảo stack đơn điệu tăng. Nếu gặp cột thấp hơn, tính diện tích cho các cột cao trước đó.
        while stack[-1] != -1 and h[i] < h[stack[-1]]:
            chieu_cao = h[stack.pop()]
            chieu_rong = i - stack[-1] - 1
            max_area = max(max_area, chieu_cao * chieu_rong)
        stack.append(i)
        
    h.pop() # Xóa cột 0 để trả lại mảng ban đầu
    return max_area

# --- Bài 13: DFS dùng ngăn xếp (Khử đệ quy) ---
def bai_13_dfs_iterative(du_lieu: Dict[str, Any]) -> List[str]:
    graph = du_lieu['do_thi']
    start = du_lieu['dinh_bat_dau']
    visited = set()
    stack = [start]
    ket_qua = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            ket_qua.append(node)
            # Push hàng xóm vào stack. (Đảo ngược để duyệt đúng thứ tự từ trái sang phải như đệ quy)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return ket_qua

# --- Bài 14: Bài toán nhịp giá cổ phiếu (Stock Span) ---
def bai_14_stock_span(du_lieu: Dict[str, Any]) -> List[int]:
    prices = du_lieu['gia']
    n = len(prices)
    span = [1] * n
    stack = [] # Stack lưu chỉ số, luôn duy trì đơn điệu giảm dần
    
    for i in range(n):
        # Loại bỏ các ngày trước đó có giá <= giá hôm nay
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()
            
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]
            
        stack.append(i)
        
    return span

# --- Bài 15: Sắp xếp một ngăn xếp ---
def bai_15_sort_stack(du_lieu: Dict[str, Any]) -> List[int]:
    stack_goc = du_lieu['stack'][:]
    stack_phu = [] # Stack này sẽ chứa các phần tử được sắp xếp tăng dần từ đáy lên đỉnh
    
    while stack_goc:
        tam = stack_goc.pop()
        # Đẩy trả lại các phần tử lớn hơn 'tam' từ stack phụ về stack gốc
        while stack_phu and stack_phu[-1] > tam:
            stack_goc.append(stack_phu.pop())
        stack_phu.append(tam)
        
    return stack_phu

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '8': {
        'ten': 'BÀI 8: TÍNH BIỂU THỨC HẬU TỐ (RPN)',
        'du_lieu': {'bieu_thuc': '3 4 + 2 * 1 +'},
        'mong_doi': 15,
        'ham': lambda d: bai_8_tinh_hau_to(d),
        'format': lambda d, kq: f"Biểu thức RPN: '{d['bieu_thuc']}'\n=> Kết quả tính toán: {kq}"
    },
    '9': {
        'ten': 'BÀI 9: CHUYỂN TRUNG TỐ SANG HẬU TỐ (SHUNTING-YARD)',
        'du_lieu': {'bieu_thuc': 'a+b*c'},
        'mong_doi': 'abc*+',
        'ham': lambda d: bai_9_trung_to_sang_hau_to(d),
        'format': lambda d, kq: f"Trung tố: '{d['bieu_thuc']}'\n=> Hậu tố: '{kq}'\n[*] Toán tử '*' được ưu tiên in ra trước '+'."
    },
    '10': {
        'ten': 'BÀI 10: CÀI ĐẶT NGĂN XẾP BẰNG 2 HÀNG ĐỢI (QUEUES)',
        'du_lieu': {'lenh': ['push 1', 'push 2', 'push 3', 'pop', 'push 4', 'pop', 'pop']},
        'mong_doi': [3, 4, 2],
        'ham': lambda d: bai_10_stack_bang_2_queue(d),
        'format': lambda d, kq: (
            f"Chuỗi lệnh: {d['lenh']}\n"
            f"Kết quả khi lấy ra (Pop): {kq}\n"
            f"[*] Push tốn O(1). Tuy nhiên Pop tốn O(n) do phải đổ dữ liệu qua lại giữa 2 Queue."
        )
    },
    '11': {
        'ten': 'BÀI 11: PHẦN TỬ LỚN HƠN KẾ TIẾP (NEXT GREATER ELEMENT)',
        'du_lieu': {'mang': [2, 1, 3]},
        'mong_doi': [3, 3, -1],
        'ham': lambda d: bai_11_next_greater_element(d),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['mang']}\n"
            f"=> Mảng Next Greater: {kq}\n"
            f"[*] Sử dụng Monotonic Stack, độ phức tạp được tối ưu tuyệt đối ở mức O(n)."
        )
    },
    '12': {
        'ten': 'BÀI 12: HÌNH CHỮ NHẬT LỚN NHẤT TRONG HISTOGRAM',
        'du_lieu': {'chieu_cao': [2, 1, 5, 6, 2, 3]},
        'mong_doi': 10,
        'ham': lambda d: bai_12_largest_rectangle(d),
        'format': lambda d, kq: (
            f"Biểu đồ chiều cao: {d['chieu_cao']}\n"
            f"=> Diện tích hình chữ nhật lớn nhất: {kq}\n"
            f"[*] Diện tích này được tạo bởi 2 cột [5, 6] (Chiều cao min = 5, chiều rộng = 2)."
        )
    },
    '13': {
        'ten': 'BÀI 13: DFS DÙNG NGĂN XẾP (KHỬ ĐỆ QUY)',
        'du_lieu': {
            'do_thi': {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []},
            'dinh_bat_dau': 'A'
        },
        'mong_doi': ['A', 'B', 'D', 'E', 'C', 'F'],
        'ham': lambda d: bai_13_dfs_iterative(d),
        'format': lambda d, kq: f"Đồ thị: {d['do_thi']}\nTrình tự duyệt DFS: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: BÀI TOÁN NHỊP GIÁ CỔ PHIẾU (STOCK SPAN)',
        'du_lieu': {'gia': [100, 80, 60, 70, 60, 75, 85]},
        'mong_doi': [1, 1, 1, 2, 1, 4, 6],
        'ham': lambda d: bai_14_stock_span(d),
        'format': lambda d, kq: (
            f"Chuỗi giá cổ phiếu: {d['gia']}\n"
            f"=> Số ngày 'nhịp giá' (Span): {kq}\n"
            f"[*] Tại ngày cuối cùng (giá 85), nó lớn hơn toàn bộ 5 ngày liên tiếp trước đó nên Span = 6."
        )
    },
    '15': {
        'ten': 'BÀI 15: SẮP XẾP MỘT NGĂN XẾP (CHỈ DÙNG 1 STACK PHỤ)',
        'du_lieu': {'stack': [3, 1, 4, 2]},
        'mong_doi': [1, 2, 3, 4], # Đỉnh là 4
        'ham': lambda d: bai_15_sort_stack(d),
        'format': lambda d, kq: (
            f"Stack lộn xộn ban đầu (Đáy -> Đỉnh): {d['stack']}\n"
            f"=> Stack sau khi sắp xếp (Đáy -> Đỉnh): {kq}\n"
            f"[*] Phần tử lớn nhất đã được đẩy lên đỉnh Stack."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
    if kq == cfg['mong_doi']:
        print("Trạng thái: THÀNH CÔNG")
    else:
        print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 2 (STACK - BÀI 8 -> BÀI 15)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            # Ép kiểu int để sort đúng theo thứ tự từ 8 đến 15
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