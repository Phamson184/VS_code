from typing import List, Dict, Any, Optional

# ==========================================
# CẤU TRÚC LÕI & HÀM HỖ TRỢ (HELPER)
# ==========================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_ll(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head: Optional[ListNode], limit: int = 20) -> List[int]:
    res = []
    count = 0
    while head and count < limit: # Chống lặp vô hạn nếu có chu trình
        res.append(head.val)
        head = head.next
        count += 1
    return res

# ==========================================
# PHẦN B: LINKED LIST (CÂU 36 - 41)
# ==========================================

# --- Câu 36: Đảo ngược danh sách (Iterative) ---
def bai36_reverse_list(du_lieu: Dict[str, Any]) -> List[int]:
    head = to_ll(du_lieu['arr'])
    prev, curr = None, head
    # Dùng 3 con trỏ để đảo ngược mũi tên [cite: 224, 225]
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return to_list(prev)

# --- Câu 37: Tìm nút giữa ---
def bai37_middle_node(du_lieu: Dict[str, Any]) -> int:
    head = to_ll(du_lieu['arr'])
    slow = fast = head
    # Kỹ thuật rùa (đi 1 bước) và thỏ (đi 2 bước) [cite: 228, 229]
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val if slow else -1

# --- Câu 38: Phát hiện & Tìm đầu chu trình ---
def bai38_cycle_start(du_lieu: Dict[str, Any]) -> int:
    arr = du_lieu['arr']
    pos = du_lieu['pos']
    
    # 1. Khởi tạo mảng có chu trình (mô phỏng)
    head = to_ll(arr)
    if pos == -1: return -1
    
    curr = head
    cycle_node = tail = None
    idx = 0
    while curr:
        if idx == pos: cycle_node = curr
        tail = curr
        curr = curr.next
        idx += 1
    tail.next = cycle_node # Nối đuôi về điểm pos để khép vòng
    
    # 2. Thuật toán Floyd [cite: 231, 232]
    slow = fast = head
    has_cycle = False
    
    # Giai đoạn 1: Phát hiện chu trình
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle: return -1
    
    # Giai đoạn 2: Tìm nút bắt đầu chu trình
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.val

# --- Câu 39: Xóa nút thứ k từ cuối ---
def bai39_remove_kth_from_end(du_lieu: Dict[str, Any]) -> List[int]:
    head = to_ll(du_lieu['arr'])
    k = du_lieu['k']
    
    dummy = ListNode(0, head)
    slow = fast = dummy
    
    # Cho fast đi trước k bước [cite: 234, 235]
    for _ in range(k):
        fast = fast.next
        
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    # Xóa nút
    slow.next = slow.next.next
    return to_list(dummy.next)

# --- Câu 40: Sắp xếp Linked List (Merge Sort O(n log n)) ---
def bai40_sort_list(du_lieu: Dict[str, Any]) -> List[int]:
    def get_mid(node):
        s, f = node, node.next
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
        
    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def merge_sort(node):
        if not node or not node.next: return node
        mid = get_mid(node)
        right = mid.next
        mid.next = None # Tách đôi danh sách [cite: 237, 238]
        return merge(merge_sort(node), merge_sort(right)) # Trộn đệ quy [cite: 237, 238]

    head = to_ll(du_lieu['arr'])
    return to_list(merge_sort(head))

# --- Câu 41: LRU Cache ---
class DoubleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # Thiết kế LRU Cache kết hợp Doubly Linked List + Bảng băm [cite: 241, 242]
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node) # Đẩy phần tử vừa truy cập lên đầu (Mới nhất) [cite: 242, 243]
            return node.val
        return -1
        
    def put(self, key: int, val: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DoubleNode(key, val)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

def bai41_lru_cache(du_lieu: Dict[str, Any]) -> List[Any]:
    lru = LRUCache(du_lieu['cap'])
    res = []
    for op, val in zip(du_lieu['ops'], du_lieu['vals']):
        if op == "put":
            lru.put(val[0], val[1])
            res.append(None)
        elif op == "get":
            res.append(lru.get(val[0]))
    return res


# ==========================================
# CẤU HÌNH MENU DATA-DRIVEN
# ==========================================
Noidung = {
    '36': {
        'ten': 'CÂU 36: ĐẢO NGƯỢC DANH SÁCH LIÊN KẾT',
        'du_lieu': {'arr': [1, 2, 3]},
        'ham': bai36_reverse_list,
        'format': lambda d, kq: f"Gốc: {d['arr']} -> Đảo ngược: {kq} [cite: 226, 227]"
    },
    '37': {
        'ten': 'CÂU 37: TÌM NÚT GIỮA (RÙA & THỎ)',
        'du_lieu': {'arr': [1, 2, 3, 4, 5]},
        'ham': bai37_middle_node,
        'format': lambda d, kq: f"Danh sách: {d['arr']} -> Nút giữa: {kq} [cite: 229, 230]"
    },
    '38': {
        'ten': 'CÂU 38: PHÁT HIỆN VÀ TÌM ĐẦU CHU TRÌNH',
        'du_lieu': {'arr': [3, 2, 0, -4], 'pos': 1},
        'ham': bai38_cycle_start,
        'format': lambda d, kq: f"Tạo chu trình nối đuôi vào vị trí Index={d['pos']} -> Nút bắt đầu vòng lặp: {kq} [cite: 231, 232, 233]"
    },
    '39': {
        'ten': 'CÂU 39: XÓA NÚT THỨ K TỪ CUỐI',
        'du_lieu': {'arr': [1, 2, 3, 4, 5], 'k': 2},
        'ham': bai39_remove_kth_from_end,
        'format': lambda d, kq: f"Gốc: {d['arr']}, Xóa vị trí k={d['k']} từ cuối -> Kết quả: {kq} [cite: 235, 236]"
    },
    '40': {
        'ten': 'CÂU 40: SẮP XẾP LINKED LIST (MERGE SORT)',
        'du_lieu': {'arr': [3, 1, 2]},
        'ham': bai40_sort_list,
        'format': lambda d, kq: f"Gốc lộn xộn: {d['arr']} -> Sắp xếp O(n log n): {kq} [cite: 238, 239, 240]"
    },
    '41': {
        'ten': 'CÂU 41: LRU CACHE (DOUBLY LL + HASH MAP)',
        'du_lieu': {'cap': 2, 'ops': ["put", "put", "get", "put", "get"], 'vals': [[1,1], [2,2], [1], [3,3], [2]]},
        'ham': bai41_lru_cache,
        'format': lambda d, kq: f"Khởi tạo sức chứa: {d['cap']}\nLệnh: {d['ops']} với tham số {d['vals']}\nKết quả trả về: {kq} [cite: 242, 243]"
    }
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

        danh_sach_keys = sorted(dict_noidung.keys(), key=lambda x: int(x))

        while True:
            print("\n" + "*"*75)
            print(f" MENU CHÍNH (CÁC CÂU: {danh_sach_keys[0]} -> {danh_sach_keys[-1]})")
            print(" NHẬP MÃ CÂU HOẶC '0' ĐỂ THOÁT | 'all' ĐỂ CHẠY TOÀN BỘ")
            print("*"*75)
            
            for k in danh_sach_keys:
                print(f" {k:>3}. {dict_noidung[k]['ten']}")
                
            chon = input("\nLựa chọn của bạn: ").strip()
            
            if chon == '0':
                print("Chương trình kết thúc.")
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