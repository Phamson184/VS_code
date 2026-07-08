from typing import List, Dict, Any

# ==========================================
# PHẦN A: ARRAY LIST (CÂU 31 - 35)
# ==========================================

# --- Câu 31: Mở rộng & Amortized O(1) ---
def bai31_amortized_analysis() -> str:
    # Trả về chuỗi lý thuyết theo yêu cầu của đề bài [cite: 409-411]
    return (
        "CƠ CHẾ MỞ RỘNG (RESIZING) VÀ CHI PHÍ AMORTIZED O(1):\n"
        "- Khi mảng đầy, ta cấp phát mảng mới có kích thước gấp đôi (2x) và chép n phần tử cũ sang. Thao tác này tốn O(n)[cite: 410].\n"
        "- Tuy nhiên, nhờ gấp đôi dung lượng, ta sẽ có n ô trống mới. Nghĩa là n lần append tiếp theo sẽ tốn đúng O(1)[cite: 411].\n"
        "- Trung bình (Amortized): Tổng chi phí = O(n) (lúc mở rộng) + n * O(1) (lúc chèn) = O(2n).\n"
        "- Chi phí cho mỗi thao tác = O(2n) / n = O(1).\n"
        "-> Append trên Array List cực kỳ hiệu quả[cite: 410]."
    )

# --- Câu 32: removeIf tại chỗ (In-place O(n)) ---
def bai32_remove_if(du_lieu: Dict[str, Any]) -> List[int]:
    a = du_lieu['a'][:]
    # Kỹ thuật 2 con trỏ: Write (ghi) và Read (đọc) [cite: 412-413]
    w = 0
    for r in range(len(a)):
        # Điều kiện: Xóa chẵn -> Giữ lại lẻ [cite: 414]
        if a[r] % 2 != 0: 
            a[w] = a[r]
            w += 1
    # Cắt mảng để loại bỏ phần dư thừa
    return a[:w]

# --- Câu 33: Xoay mảng k vị trí ---
def bai33_rotate_k(du_lieu: Dict[str, Any]) -> List[int]:
    a = du_lieu['a'][:]
    k = du_lieu['k']
    n = len(a)
    if n == 0: return a
    k %= n
    
    # Tuyệt chiêu đảo 3 lần (O(n) thời gian, O(1) bộ nhớ) [cite: 415-416]
    def reverse(lst, i, j):
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
            
    reverse(a, 0, n - 1)      # 1. Đảo toàn bộ
    reverse(a, 0, k - 1)      # 2. Đảo k phần tử đầu
    reverse(a, k, n - 1)      # 3. Đảo phần còn lại
    
    return a

# --- Câu 34: Loại bỏ trùng lặp giữ thứ tự ---
def bai34_remove_duplicates(du_lieu: Dict[str, Any]) -> List[int]:
    a = du_lieu['a']
    seen = set() # Sử dụng Hash Set để đạt O(n) [cite: 418-419]
    res = []
    
    for x in a:
        if x not in seen:
            seen.add(x)
            res.append(x)
            
    return res

# --- Câu 35: Merge Intervals ---
def bai35_merge_intervals(du_lieu: Dict[str, Any]) -> List[List[int]]:
    intervals = du_lieu['intervals']
    if not intervals: return []
    
    # B1: Sắp xếp theo điểm bắt đầu [cite: 421-422]
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    # B2: Quét một lượt để gộp [cite: 422]
    for curr in intervals[1:]:
        last = merged[-1]
        if curr[0] <= last[1]: # Có giao nhau
            last[1] = max(last[1], curr[1])
        else:
            merged.append(curr)
            
    return merged


# ==========================================
# CẤU HÌNH MENU DATA-DRIVEN
# ==========================================
Noidung = {
    '31': {
        'ten': 'CÂU 31: MỞ RỘNG MẢNG & AMORTIZED O(1)',
        'ham': bai31_amortized_analysis,
        'format': lambda kq: kq
    },
    '32': {
        'ten': 'CÂU 32: REMOVE-IF TẠI CHỖ (XÓA CHẴN)',
        'du_lieu': {'a': [1, 2, 3, 4]},
        'ham': bai32_remove_if,
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau khi xóa chẵn: {kq} [cite: 412-414]"
    },
    '33': {
        'ten': 'CÂU 33: XOAY MẢNG K VỊ TRÍ',
        'du_lieu': {'a': [1, 2, 3, 4, 5], 'k': 2},
        'ham': bai33_rotate_k,
        'format': lambda d, kq: f"Mảng gốc: {d['a']} | k = {d['k']}\nSau khi xoay: {kq} [cite: 415-417]"
    },
    '34': {
        'ten': 'CÂU 34: LOẠI BỎ TRÙNG LẶP (GIỮ THỨ TỰ)',
        'du_lieu': {'a': [3, 1, 3, 2, 1]},
        'ham': bai34_remove_duplicates,
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau khi lọc (Dùng Set): {kq} [cite: 418-420]"
    },
    '35': {
        'ten': 'CÂU 35: MERGE INTERVALS (TRỘN KHOẢNG)',
        'du_lieu': {'intervals': [[1, 3], [2, 6], [8, 10]]},
        'ham': bai35_merge_intervals,
        'format': lambda d, kq: f"Các khoảng gốc: {d['intervals']}\nĐã trộn: {kq} [cite: 421-423]"
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

        danh_sach_keys = sorted(dict_noidung.keys(), key=lambda x: int(x) if x.isdigit() else x)

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