from typing import List, Dict, Any
from collections import deque

# ==========================================
# MODULE B1: HÀNG ĐỢI (QUEUE) - BÀI 1 ĐẾN BÀI 7
# ==========================================

# --- Bài 1, 4, 5: Cài đặt Hàng đợi cơ bản, Tìm Front/Rear & Bắt lỗi ---
class FixedQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        return len(self.queue) == self.capacity

    def enqueue(self, item: Any):
        if self.is_full():
            raise OverflowError("Overflow: Hàng đợi đã đầy!")
        self.queue.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Underflow: Hàng đợi đang rỗng!")
        return self.queue.pop(0) # Pop ở đầu (O(n) đối với list thường, nhưng phù hợp để mô phỏng)

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("Hàng đợi rỗng, không có Front!")
        return self.queue[0]

    def rear(self) -> Any:
        if self.is_empty():
            raise IndexError("Hàng đợi rỗng, không có Rear!")
        return self.queue[-1]

def bai_1_4_5_queue_co_ban(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    q = FixedQueue(capacity=du_lieu['capacity'])
    log_dequeue = []
    loi = []
    
    for lenh in du_lieu['lenh']:
        try:
            if lenh.startswith('enq'):
                q.enqueue(int(lenh.split()[1]))
            elif lenh == 'deq':
                log_dequeue.append(q.dequeue())
        except Exception as e:
            loi.append(str(e))
            
    trang_thai = {
        'front': q.front() if not q.is_empty() else None,
        'rear': q.rear() if not q.is_empty() else None,
        'queue_cuoi': q.queue,
        'da_deq': log_dequeue,
        'loi_bat_duoc': loi
    }
    return trang_thai

# --- Bài 2: Hàng đợi vòng (Circular Queue) ---
class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = -1
        self.size = 0

    def enqueue(self, item: Any) -> bool:
        if self.size == self.capacity:
            return False # Đầy
        self.tail = (self.tail + 1) % self.capacity # Xoay vòng bằng Modulo
        self.queue[self.tail] = item
        self.size += 1
        return True

    def dequeue(self) -> Any:
        if self.size == 0:
            return None # Rỗng
        item = self.queue[self.head]
        self.queue[self.head] = None # Clear dữ liệu cũ
        self.head = (self.head + 1) % self.capacity # Xoay vòng
        self.size -= 1
        return item

def bai_2_circular_queue(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    cq = CircularQueue(capacity=du_lieu['capacity'])
    
    # 1. Nạp đầy
    for val in du_lieu['nap_lan_1']:
        cq.enqueue(val)
    trang_thai_1 = cq.queue[:]
    
    # 2. Rút bớt
    for _ in range(du_lieu['rut_bot']):
        cq.dequeue()
        
    # 3. Nạp tiếp (Sẽ xoay vòng đè lên ô trống ở đầu mảng)
    for val in du_lieu['nap_lan_2']:
        cq.enqueue(val)
    trang_thai_2 = cq.queue[:]
    
    return {
        'sau_khi_nap_day': trang_thai_1,
        'sau_khi_xoay_vong': trang_thai_2,
        'head_hien_tai': cq.head,
        'tail_hien_tai': cq.tail
    }

# --- Bài 3: Mô phỏng dãy thao tác ---
def bai_3_mo_phong_queue(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    q = deque()
    log_deq = []
    for thao_tac in du_lieu['thao_tac']:
        if thao_tac.startswith("enq"):
            q.append(int(thao_tac.split()[1]))
        elif thao_tac == "deq":
            if q:
                log_deq.append(q.popleft())
    return {
        'log_deq': log_deq,
        'queue_cuoi': list(q)
    }

# --- Bài 6: Cài đặt Hàng đợi bằng 2 Ngăn xếp (Stacks) ---
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int):
        self.in_stack.append(x) # Chi phí O(1)

    def dequeue(self) -> int:
        if not self.out_stack:
            # Đổ toàn bộ dữ liệu từ in_stack sang out_stack để đảo ngược thứ tự
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue rỗng!")
        return self.out_stack.pop() # Chi phí Amortized O(1)

def bai_6_queue_bang_2_stack(du_lieu: Dict[str, Any]) -> List[int]:
    qs = QueueUsingStacks()
    ket_qua = []
    for lenh in du_lieu['lenh']:
        if lenh.startswith('enq'):
            qs.enqueue(int(lenh.split()[1]))
        elif lenh == 'deq':
            ket_qua.append(qs.dequeue())
    return ket_qua

# --- Bài 7: Đảo ngược Hàng đợi ---
def bai_7_dao_nguoc_queue(du_lieu: Dict[str, Any]) -> List[int]:
    q = deque(du_lieu['queue_goc'])
    stack = []
    
    # B1: Dequeue toàn bộ vào Stack
    while q:
        stack.append(q.popleft())
        
    # B2: Pop từ Stack và Enqueue lại vào Queue
    while stack:
        q.append(stack.pop())
        
    return list(q)

# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '1': {
        'ten': 'BÀI 1, 4, 5: CÀI ĐẶT QUEUE, TÌM FRONT/REAR & BẮT LỖI',
        'du_lieu': {'capacity': 3, 'lenh': ['enq 10', 'enq 20', 'enq 30', 'enq 40', 'deq', 'deq', 'deq', 'deq']},
        'mong_doi': 'Kiểm tra mô phỏng',
        'ham': lambda d: bai_1_4_5_queue_co_ban(d),
        'format': lambda d, kq: (
            f"Sức chứa: {d['capacity']}. Chuỗi lệnh: {d['lenh']}\n\n"
            f"- Nhật ký Dequeue: {kq['da_deq']}\n"
            f"- Front hiện tại: {kq['front']} | Rear hiện tại: {kq['rear']}\n"
            f"- Lỗi bắt được:\n" + "\n".join(f"  [!] {loi}" for loi in kq['loi_bat_duoc']) + "\n"
            f"[*] NHẬN XÉT: Lệnh 'enq 40' bị chặn vì Queue đầy (Overflow). "
            f"Lệnh 'deq' cuối bị chặn vì Queue rỗng (Underflow)."
        )
    },
    '2': {
        'ten': 'BÀI 2: HÀNG ĐỢI VÒNG (CIRCULAR QUEUE)',
        'du_lieu': {
            'capacity': 4,
            'nap_lan_1': [1, 2, 3, 4],
            'rut_bot': 2,
            'nap_lan_2': [5, 6]
        },
        'mong_doi': 'Kiểm tra mảng nội bộ',
        'ham': lambda d: bai_2_circular_queue(d),
        'format': lambda d, kq: (
            f"Dung lượng mảng tĩnh: {d['capacity']}\n"
            f"1. Nạp đầy 4 phần tử: {kq['sau_khi_nap_day']}\n"
            f"2. Rút 2 phần tử, sau đó nạp thêm 2 phần tử ({d['nap_lan_2']}).\n"
            f"3. Trạng thái mảng nội bộ hiện tại: {kq['sau_khi_xoay_vong']}\n"
            f"   - Vị trí Head: {kq['head_hien_tai']}\n"
            f"   - Vị trí Tail: {kq['tail_hien_tai']}\n"
            f"[*] NHẬN XÉT: Nhờ công thức (tail + 1) % capacity, các số [5, 6] đã tự động xoay vòng "
            f"quay lại điền vào 2 ô trống đầu mảng (Index 0 và 1) mà không cần phải shift mảng."
        )
    },
    '3': {
        'ten': 'BÀI 3: MÔ PHỎNG DÃY THAO TÁC (FIFO)',
        'du_lieu': {'thao_tac': ['enq 5', 'enq 7', 'deq', 'enq 9', 'deq']},
        'mong_doi': {'log_deq': [5, 7], 'queue_cuoi': [9]},
        'ham': lambda d: bai_3_mo_phong_queue(d),
        'format': lambda d, kq: (
            f"Các lệnh: {d['thao_tac']}\n"
            f"- Nhật ký in khi Dequeue: {kq['log_deq']}\n"
            f"- Queue còn lại: {kq['queue_cuoi']}\n"
            f"[*] Khác với Stack, số 5 vào trước nên sẽ được pop ra trước tiên."
        )
    },
    '6': {
        'ten': 'BÀI 6: CÀI ĐẶT HÀNG ĐỢI BẰNG 2 NGĂN XẾP',
        'du_lieu': {'lenh': ['enq 1', 'enq 2', 'enq 3', 'deq', 'enq 4', 'deq', 'deq']},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai_6_queue_bang_2_stack(d),
        'format': lambda d, kq: (
            f"Chuỗi lệnh: {d['lenh']}\n"
            f"Kết quả Dequeue: {kq}\n"
            f"[*] Khi Dequeue, nếu out_stack rỗng, ta trút toàn bộ in_stack sang out_stack. "
            f"Điều này đảo ngược mảng (LIFO -> FIFO)."
        )
    },
    '7': {
        'ten': 'BÀI 7: ĐẢO NGƯỢC HÀNG ĐỢI',
        'du_lieu': {'queue_goc': [1, 2, 3, 4, 5]},
        'mong_doi': [5, 4, 3, 2, 1],
        'ham': lambda d: bai_7_dao_nguoc_queue(d),
        'format': lambda d, kq: (
            f"Queue gốc: {d['queue_goc']}\n"
            f"=> Queue đảo ngược: {kq}\n"
            f"[*] Phương pháp cực kỳ đơn giản: Xả toàn bộ Queue vào 1 Stack (trung gian), sau đó xả từ Stack về lại Queue."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] not in ['Kiểm tra mô phỏng', 'Kiểm tra mảng nội bộ']:
        print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
        if kq == cfg['mong_doi']:
            print("Trạng thái: THÀNH CÔNG")
        else:
            print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 3 (QUEUE - BÀI 1 -> BÀI 7)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            # Sắp xếp key để in menu đúng thứ tự
            danh_sach_keys = ['1', '2', '3', '6', '7']
            for k in danh_sach_keys:
                print(f" {k:>2}. {Noidung[k]['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for k in danh_sach_keys:
                    chay_bai(Noidung[k])
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
        pass