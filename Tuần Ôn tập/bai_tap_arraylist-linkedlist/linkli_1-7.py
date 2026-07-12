from typing import List, Dict, Any, Tuple

# ==========================================
# MODULE B1 & B3: LINKED LIST CƠ BẢN & ỨNG DỤNG
# ==========================================

# --- Lớp Node cơ bản và Hàm hỗ trợ ---
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_ll(arr: List[int]) -> Node:
    """Hàm hỗ trợ: Chuyển mảng Python thành Linked List."""
    dummy = Node(0)
    curr = dummy
    for val in arr:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

def ll_to_list(head: Node) -> List[int]:
    """Hàm hỗ trợ: Chuyển Linked List thành mảng Python để dễ in ấn."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# --- Bài 1: Cài đặt danh sách liên kết đơn (pushFront, pushBack) ---
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, val: int):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

def bai_1_cai_dat(du_lieu: Dict[str, Any]) -> List[int]:
    ll = SinglyLinkedList()
    for lenh in du_lieu['lenh']:
        cmd, val = lenh.split()
        if cmd == 'pushFront':
            ll.push_front(int(val))
        elif cmd == 'pushBack':
            ll.push_back(int(val))
    return ll_to_list(ll.head)

# --- Bài 2: Tính độ dài / duyệt ---
def bai_2_duyet_do_dai(du_lieu: Dict[str, Any]) -> Dict[str, Any]:
    head = list_to_ll(du_lieu['arr'])
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return {'chieu_dai': length, 'danh_sach': du_lieu['arr']}

# --- Bài 3: Tìm kiếm một giá trị ---
def bai_3_tim_kiem(du_lieu: Dict[str, Any]) -> int:
    head = list_to_ll(du_lieu['arr'])
    target = du_lieu['target']
    idx = 0
    curr = head
    while curr:
        if curr.val == target:
            return idx
        curr = curr.next
        idx += 1
    return -1

# --- Bài 4: Chèn sau vị trí k ---
def bai_4_chen_sau_k(du_lieu: Dict[str, Any]) -> List[int]:
    head = list_to_ll(du_lieu['arr'])
    k = du_lieu['k']
    val = du_lieu['val']
    
    curr = head
    idx = 0
    while curr and idx < k:
        curr = curr.next
        idx += 1
        
    if curr:
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        
    return ll_to_list(head)

# --- Bài 5: Xóa nút theo giá trị ---
def bai_5_xoa_theo_gia_tri(du_lieu: Dict[str, Any]) -> List[int]:
    head = list_to_ll(du_lieu['arr'])
    target = du_lieu['target']
    
    # Xử lý xóa nút đầu tiên (Edge case)
    if head and head.val == target:
        return ll_to_list(head.next)
        
    curr = head
    while curr and curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next # Cắt bỏ nút target
            break
        curr = curr.next
        
    return ll_to_list(head)

# --- Bài 6: Đảo ngược danh sách (Lặp & Đệ quy) ---
def bai_6_dao_nguoc(du_lieu: Dict[str, Any]) -> Dict[str, List[int]]:
    # 1. Cách Lặp (Iterative) - Dùng 3 con trỏ
    def reverse_iterative(head: Node) -> Node:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next # Lưu lại nút tiếp theo
            curr.next = prev      # Quay ngược mũi tên
            prev = curr           # Dịch prev lên
            curr = next_temp      # Dịch curr lên
        return prev
        
    # 2. Cách Đệ quy (Recursive)
    def reverse_recursive(head: Node) -> Node:
        if not head or not head.next:
            return head
        new_head = reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    head1 = list_to_ll(du_lieu['arr'])
    head2 = list_to_ll(du_lieu['arr'])
    
    return {
        'iterative': ll_to_list(reverse_iterative(head1)),
        'recursive': ll_to_list(reverse_recursive(head2))
    }

# --- Bài 9: Trộn hai danh sách đã sắp xếp ---
def bai_9_tron_2_danh_sach(du_lieu: Dict[str, Any]) -> List[int]:
    l1 = list_to_ll(du_lieu['arr1'])
    l2 = list_to_ll(du_lieu['arr2'])
    
    dummy = Node(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 if l1 else l2
    return ll_to_list(dummy.next)

# --- Bài 11: Danh sách liên kết đôi (Doubly Linked List) ---
class DoubleNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, val: int):
        new_node = DoubleNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, val: int):
        new_node = DoubleNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def traverse_backward(self) -> List[int]:
        res = []
        curr = self.tail
        while curr:
            res.append(curr.val)
            curr = curr.prev
        return res

def bai_11_doubly_linked_list(du_lieu: Dict[str, Any]) -> Dict[str, List[int]]:
    dll = DoublyLinkedList()
    for lenh in du_lieu['lenh']:
        cmd, val = lenh.split()
        if cmd == 'pushFront': dll.push_front(int(val))
        elif cmd == 'pushBack': dll.push_back(int(val))
        
    return {
        'xuoi': dll.traverse_forward(),
        'nguoc': dll.traverse_backward()
    }

# --- Bài 14: Cộng hai số biểu diễn bằng Linked List ---
def bai_14_cong_hai_so(du_lieu: Dict[str, Any]) -> List[int]:
    l1 = list_to_ll(du_lieu['num1'])
    l2 = list_to_ll(du_lieu['num2'])
    
    dummy = Node(0)
    curr = dummy
    carry = 0 # Biến nhớ
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)
        
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return ll_to_list(dummy.next)


# ==========================================
# CẤU HÌNH DATA-DRIVEN MENU
# ==========================================
Noidung = {
    '1': {
        'ten': 'BÀI 1: CÀI ĐẶT SINGLY LINKED LIST',
        'du_lieu': {'lenh': ['pushFront 2', 'pushBack 5', 'pushFront 1']},
        'mong_doi': [1, 2, 5],
        'ham': lambda d: bai_1_cai_dat(d),
        'format': lambda d, kq: f"Chuỗi lệnh: {d['lenh']}\n=> Danh sách kết quả: " + " -> ".join(map(str, kq)) + " -> null"
    },
    '2': {
        'ten': 'BÀI 2: TÍNH ĐỘ DÀI & DUYỆT',
        'du_lieu': {'arr': [10, 20, 30]},
        'mong_doi': 3,
        'ham': lambda d: bai_2_duyet_do_dai(d),
        'format': lambda d, kq: f"Linked List: {' -> '.join(map(str, kq['danh_sach']))} -> null\n=> Chiều dài: {kq['chieu_dai']} nút"
    },
    '3': {
        'ten': 'BÀI 3: TÌM KIẾM MỘT GIÁ TRỊ',
        'du_lieu': {'arr': [5, 10, 15, 20], 'target': 15},
        'mong_doi': 2,
        'ham': lambda d: bai_3_tim_kiem(d),
        'format': lambda d, kq: f"List: {' -> '.join(map(str, d['arr']))}\nTìm số {d['target']} => Nằm ở Index: {kq}"
    },
    '4': {
        'ten': 'BÀI 4: CHÈN SAU VỊ TRÍ K',
        'du_lieu': {'arr': [1, 3], 'k': 0, 'val': 2},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai_4_chen_sau_k(d),
        'format': lambda d, kq: (
            f"List ban đầu: {' -> '.join(map(str, d['arr']))}\n"
            f"Chèn số {d['val']} vào sau index {d['k']}\n"
            f"=> Kết quả: {' -> '.join(map(str, kq))}"
        )
    },
    '5': {
        'ten': 'BÀI 5: XÓA NÚT THEO GIÁ TRỊ',
        'du_lieu': {'arr': [1, 2, 3, 2], 'target': 2},
        'mong_doi': [1, 3, 2],
        'ham': lambda d: bai_5_xoa_theo_gia_tri(d),
        'format': lambda d, kq: f"List: {' -> '.join(map(str, d['arr']))}\nXóa số {d['target']} đầu tiên => {' -> '.join(map(str, kq))}"
    },
    '6': {
        'ten': 'BÀI 6: ĐẢO NGƯỢC DANH SÁCH (ITERATIVE & RECURSIVE)',
        'du_lieu': {'arr': [1, 2, 3, 4]},
        'mong_doi': 'So sánh 2 cách',
        'ham': lambda d: bai_6_dao_nguoc(d),
        'format': lambda d, kq: (
            f"List gốc: {' -> '.join(map(str, d['arr']))}\n"
            f"- Đảo ngược bằng Vòng lặp (3 con trỏ) : {' -> '.join(map(str, kq['iterative']))}\n"
            f"- Đảo ngược bằng Đệ quy (Recursive)  : {' -> '.join(map(str, kq['recursive']))}\n"
            f"[*] Đảo ngược Linked List là bài toán kinh điển. Cách lặp tốn O(1) bộ nhớ, cách đệ quy tốn O(n) call stack."
        )
    },
    '9': {
        'ten': 'BÀI 9: TRỘN HAI DANH SÁCH ĐÃ SẮP XẾP',
        'du_lieu': {'arr1': [1, 3, 5], 'arr2': [2, 4]},
        'mong_doi': [1, 2, 3, 4, 5],
        'ham': lambda d: bai_9_tron_2_danh_sach(d),
        'format': lambda d, kq: (
            f"L1: {' -> '.join(map(str, d['arr1']))}\n"
            f"L2: {' -> '.join(map(str, d['arr2']))}\n"
            f"=> Đã trộn: {' -> '.join(map(str, kq))}\n"
            f"[*] Không tạo node mới, chỉ đan xen lại các dây con trỏ (mũi tên)."
        )
    },
    '11': {
        'ten': 'BÀI 11: DANH SÁCH LIÊN KẾT ĐÔI (DOUBLY LINKED LIST)',
        'du_lieu': {'lenh': ['pushFront 2', 'pushFront 1', 'pushBack 3']},
        'mong_doi': {'xuoi': [1, 2, 3], 'nguoc': [3, 2, 1]},
        'ham': lambda d: bai_11_doubly_linked_list(d),
        'format': lambda d, kq: (
            f"Lệnh: {d['lenh']}\n"
            f"- Duyệt xuôi (head -> tail): {' <-> '.join(map(str, kq['xuoi']))}\n"
            f"- Duyệt ngược (tail -> head): {' <-> '.join(map(str, kq['nguoc']))}\n"
            f"[*] Nút bây giờ có 2 con trỏ `prev` và `next` giúp duyệt hai chiều dễ dàng."
        )
    },
    '14': {
        'ten': 'BÀI 14: CỘNG HAI SỐ BIỂU DIỄN BẰNG LINKED LIST',
        'du_lieu': {'num1': [2, 4, 3], 'num2': [5, 6, 4]}, # 342 + 465 = 807
        'mong_doi': [7, 0, 8],
        'ham': lambda d: bai_14_cong_hai_so(d),
        'format': lambda d, kq: (
            f"Số thứ 1 (lưu ngược): {' -> '.join(map(str, d['num1']))} (Tức là 342)\n"
            f"Số thứ 2 (lưu ngược): {' -> '.join(map(str, d['num2']))} (Tức là 465)\n"
            f"=> Tổng (lưu ngược): {' -> '.join(map(str, kq))} (Tức là 807)\n"
            f"[*] Thuật toán này giúp cộng các con số siêu lớn tràn kiểu dữ liệu int thông thường."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*75}\n {cfg['ten']}\n{'='*75}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if cfg['mong_doi'] != 'So sánh 2 cách':
        # Custom logic for index 2 to match format
        if isinstance(cfg['mong_doi'], int) and 'chieu_dai' in kq if isinstance(kq, dict) else False:
            print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
            if kq['chieu_dai'] == cfg['mong_doi']:
                print("Trạng thái: THÀNH CÔNG")
            else:
                print("Trạng thái: THẤT BẠI")
        else:
            print(f"\nKết quả mong đợi: {cfg['mong_doi']}")
            if kq == cfg['mong_doi']:
                print("Trạng thái: THÀNH CÔNG")
            else:
                print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*75)
            print(" MENU: PHIÊN 3 (LINKED LIST - BÀI 1->6, 9, 11, 14)")
            print(" CHỌN BÀI HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*75)
            
            danh_sach_keys = ['1', '2', '3', '4', '5', '6', '9', '11', '14']
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