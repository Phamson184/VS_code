from typing import List, Dict, Any, Optional

# ==========================================
# MODULE B2 & B3: LINKED LIST - THUẬT TOÁN NÂNG CAO (BÀI 7, 8, 10, 12, 13, 15)
# ==========================================

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_ll(arr: List[int]) -> Node:
    dummy = Node(0)
    curr = dummy
    for val in arr:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

def ll_to_list(head: Node, limit=20) -> List[int]:
    res = []
    curr = head
    count = 0
    while curr and count < limit: # Giới hạn chống lặp vô hạn nếu có chu trình
        res.append(curr.val)
        curr = curr.next
        count += 1
    return res

def create_cycle_ll(arr: List[int], cycle_idx: int) -> Node:
    """Hỗ trợ tạo Linked List có chu trình để test Bài 8 và Bài 12."""
    if not arr: return None
    head = list_to_ll(arr)
    if cycle_idx == -1: return head
    
    cycle_node = None
    tail = head
    idx = 0
    while tail.next:
        if idx == cycle_idx:
            cycle_node = tail
        tail = tail.next
        idx += 1
    if idx == cycle_idx:
        cycle_node = tail
        
    tail.next = cycle_node # Khép vòng
    return head

# --- Bài 7: Tìm nút giữa (Slow & Fast Pointers) ---
def bai_7_tim_nut_giua(du_lieu: Dict[str, Any]) -> int:
    head = list_to_ll(du_lieu['arr'])
    slow = fast = head
    
    # Rùa đi 1 bước, Thỏ đi 2 bước. Thỏ tới đích thì Rùa ở giữa.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val if slow else -1

# --- Bài 8: Phát hiện chu trình (Floyd's Cycle-Finding) ---
def bai_8_phat_hien_chu_trinh(du_lieu: Dict[str, Any]) -> bool:
    head = create_cycle_ll(du_lieu['arr'], du_lieu['cycle_idx'])
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # Rùa và Thỏ gặp nhau -> Có vòng lặp
            return True
            
    return False

# --- Bài 10: Xóa nút thứ k từ cuối ---
def bai_10_xoa_k_tu_cuoi(du_lieu: Dict[str, Any]) -> List[int]:
    head = list_to_ll(du_lieu['arr'])
    k = du_lieu['k']
    
    dummy = Node(0, head)
    slow = fast = dummy
    
    # Cho fast đi trước k bước
    for _ in range(k):
        fast = fast.next
        
    # Di chuyển cả 2 cùng lúc cho đến khi fast chạm đáy
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    # Lúc này slow đang đứng ngay trước nút cần xóa
    slow.next = slow.next.next
    
    return ll_to_list(dummy.next)

# --- Bài 12: Tìm điểm bắt đầu chu trình ---
def bai_12_diem_bat_dau_chu_trinh(du_lieu: Dict[str, Any]) -> int:
    head = create_cycle_ll(du_lieu['arr'], du_lieu['cycle_idx'])
    slow = fast = head
    has_cycle = False
    
    # Giai đoạn 1: Tìm điểm gặp nhau
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return -1
        
    # Giai đoạn 2: Tìm điểm bắt đầu
    # Trả slow về đầu, cho 2 con trỏ đi cùng tốc độ 1 bước, gặp nhau ở đâu đó chính là đầu chu trình.
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow.val

# --- Bài 13: Sắp xếp danh sách liên kết (Merge Sort O(n log n)) ---
def bai_13_merge_sort_ll(du_lieu: Dict[str, Any]) -> List[int]:
    def merge(l1: Node, l2: Node) -> Node:
        dummy = Node(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    def merge_sort(head: Node) -> Node:
        if not head or not head.next:
            return head
            
        # Tìm điểm giữa để cắt đứt Linked List làm 2 nửa
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None # Cắt đứt
        
        # Đệ quy sắp xếp 2 nửa
        left = merge_sort(head)
        right = merge_sort(mid)
        
        # Trộn lại
        return merge(left, right)

    head = list_to_ll(du_lieu['arr'])
    sorted_head = merge_sort(head)
    return ll_to_list(sorted_head)

# --- Bài 15: LRU Cache (Least Recently Used) ---
class DNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Hash map: key -> DNode
        # Dummy head và tail để tránh kiểm tra None phức tạp
        self.head = DNode()
        self.tail = DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DNode):
        """Rút node ra khỏi Doubly Linked List."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: DNode):
        """Thêm node vào ngay sau Dummy Head (Đánh dấu vừa được sử dụng)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Kéo lên đầu (Đánh dấu Mới Dùng)
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Xóa phần tử ít sử dụng nhất (Nút đứng ngay trước Dummy Tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
                
            new_node = DNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

def bai_15_lru_cache(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    lru = LRUCache(du_lieu['capacity'])
    log = []
    
    for lenh in du_lieu['lenh']:
        parts = lenh.split()
        if parts[0] == 'put':
            lru.put(int(parts[1]), int(parts[2]))
        elif parts[0] == 'get':
            log.append(lru.get(int(parts[1])))
            
    # Trích xuất trạng thái cache hiện tại (từ Head -> Tail)
    trang_thai = []
    curr = lru.head.next
    while curr != lru.tail:
        trang_thai.append(f"[{curr.key}:{curr.val}]")
        curr = curr.next
        
    return {'log_get': log, 'trang_thai_tu_moi_nhat': trang_thai}


# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '7': {
        'ten': 'BÀI 7: TÌM NÚT GIỮA (SLOW/FAST POINTERS)',
        'du_lieu': {'arr': [1, 2, 3, 4, 5]},
        'mong_doi': 3,
        'ham': lambda d: bai_7_tim_nut_giua(d),
        'format': lambda d, kq: (
            f"List gốc: {' -> '.join(map(str, d['arr']))}\n"
            f"=> Nút ở giữa có giá trị là: {kq}\n"
            f"[*] Bằng cách cho thỏ đi 2 bước, rùa đi 1 bước, khi thỏ chạm đáy thì rùa ở ngay giữa. Đạt O(n) chỉ trong 1 lần duyệt."
        )
    },
    '8': {
        'ten': 'BÀI 8: PHÁT HIỆN CHU TRÌNH (FLOYD)',
        'du_lieu': {'arr': [3, 2, 0, -4], 'cycle_idx': 1}, # Đuôi -4 trỏ ngược về 2
        'mong_doi': True,
        'ham': lambda d: bai_8_phat_hien_chu_trinh(d),
        'format': lambda d, kq: (
            f"List mô phỏng: {d['arr']} | Đuôi trỏ về Index: {d['cycle_idx']}\n"
            f"=> Có chu trình (vòng lặp)? {'Có (True)' if kq else 'Không (False)'}\n"
            f"[*] Nếu rùa và thỏ chạy trong một vòng lặp, chắc chắn thỏ sẽ chạy vòng quanh và bắt kịp rùa từ phía sau."
        )
    },
    '10': {
        'ten': 'BÀI 10: XÓA NÚT THỨ K TỪ CUỐI LÊN',
        'du_lieu': {'arr': [1, 2, 3, 4, 5], 'k': 2},
        'mong_doi': [1, 2, 3, 5], # Xóa số 4
        'ham': lambda d: bai_10_xoa_k_tu_cuoi(d),
        'format': lambda d, kq: (
            f"List gốc: {' -> '.join(map(str, d['arr']))}\n"
            f"Xóa vị trí thứ k = {d['k']} tính từ cuối\n"
            f"=> Kết quả: {' -> '.join(map(str, kq))}\n"
            f"[*] Giữ 2 con trỏ cách nhau chính xác k bước. Khi con trỏ trước chạm đáy, con trỏ sau đang đứng ở vị trí cần xóa."
        )
    },
    '12': {
        'ten': 'BÀI 12: TÌM ĐIỂM BẮT ĐẦU CHU TRÌNH',
        'du_lieu': {'arr': [3, 2, 0, -4], 'cycle_idx': 1}, # Điểm bắt đầu chu trình là nút có giá trị 2
        'mong_doi': 2,
        'ham': lambda d: bai_12_diem_bat_dau_chu_trinh(d),
        'format': lambda d, kq: (
            f"List mô phỏng: {d['arr']} | Đuôi khép vòng tại Index {d['cycle_idx']}\n"
            f"=> Giá trị của nút bắt đầu chu trình: {kq}\n"
            f"[*] Toán học cực hay: Sau khi Rùa và Thỏ gặp nhau, trả Rùa về vạch xuất phát. Cả 2 cùng đi vận tốc x1, chúng sẽ gặp nhau tại đúng cửa ngõ chu trình."
        )
    },
    '13': {
        'ten': 'BÀI 13: SẮP XẾP DANH SÁCH (MERGE SORT O(n log n))',
        'du_lieu': {'arr': [4, 2, 1, 3]},
        'mong_doi': [1, 2, 3, 4],
        'ham': lambda d: bai_13_merge_sort_ll(d),
        'format': lambda d, kq: (
            f"List lộn xộn: {' -> '.join(map(str, d['arr']))}\n"
            f"=> Đã sắp xếp : {' -> '.join(map(str, kq))}\n"
            f"[*] Đạt được O(n log n) bằng cách liên tục chặt đôi mảng (dùng kỹ thuật tìm nút giữa) và ghép đan xen chúng lại."
        )
    },
    '15': {
        'ten': 'BÀI 15: LRU CACHE (TRÙM CUỐI SYSTEM DESIGN)',
        'du_lieu': {
            'capacity': 2,
            'lenh': ['put 1 1', 'put 2 2', 'get 1', 'put 3 3', 'get 2', 'put 4 4', 'get 1', 'get 3', 'get 4']
        },
        'mong_doi': {'log_get': [1, -1, -1, 3, 4], 'trang_thai_tu_moi_nhat': ['[4:4]', '[3:3]']},
        'ham': lambda d: bai_15_lru_cache(d),
        'format': lambda d, kq: (
            f"Khởi tạo LRU Cache dung lượng: {d['capacity']}\n"
            f"Lệnh chạy: {d['lenh']}\n\n"
            f"- Lịch sử lệnh Get (Nếu bị đẩy ra sẽ trả về -1): {kq['log_get']}\n"
            f"- Trạng thái Cache hiện tại (Từ Mới Dùng -> Cũ Nhất): {' -> '.join(kq['trang_thai_tu_moi_nhat'])}\n"
            f"[*] Hash Map đảm bảo việc tìm kiếm tốn O(1). Doubly Linked List đảm bảo việc xóa/kéo phần tử lên đỉnh tốn O(1)."
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
            print(" MENU: PHIÊN 4 (LINKED LIST - BÀI 7, 8, 10, 12, 13, 15)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            
            danh_sach_keys = ['7', '8', '10', '12', '13', '15']
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