from collections import deque

# --- LOGIC THUẬT TOÁN ---

class CircularQueue: # Câu 26
    def __init__(self, k): self.q, self.k, self.h, self.t, self.sz = [0]*k, k, 0, -1, 0
    def enq(self, v): 
        if self.sz == self.k: return False
        self.t = (self.t + 1) % self.k; self.q[self.t] = v; self.sz += 1; return True
    def deq(self):
        if self.sz == 0: return None
        v = self.q[self.h]; self.h = (self.h + 1) % self.k; self.sz -= 1; return v

def bai29_sliding_window_max(a: List[int], k: int) -> List[int]: # Câu 29
    dq = deque()
    res = []
    for i in range(len(a)):
        if dq and dq[0] < i - k + 1: dq.popleft()
        while dq and a[dq[-1]] < a[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: res.append(a[dq[0]])
    return res

# --- MENU DATA-DRIVEN ---
NoidungQ = {
    '26': {'ten': 'CÂU 26: HÀNG ĐỢI VÒNG', 'ham': lambda: "Sử dụng mod n [cite: 392-394]"},
    '27': {'ten': 'CÂU 27: QUEUE BẰNG 2 STACK', 'ham': lambda: "Phân tích amortized O(1) [cite: 395-397]"},
    '28': {'ten': 'CÂU 28: BFS', 'ham': lambda: "Dùng hàng đợi duyệt tầng [cite: 398-400]"},
    '29': {'ten': 'CÂU 29: SLIDING WINDOW MAX', 'du_lieu': ([1,3,-1,-3,5,3], 3), 'ham': lambda d: bai29_sliding_window_max(*d), 'format': lambda d, k: f"{d[0]}, k={d[1]} -> {k}"},
    '30': {'ten': 'CÂU 30: ROUND-ROBIN', 'ham': lambda: "Mô phỏng tiến trình quantum [cite: 404-407]"}
}
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