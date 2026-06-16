import re

def tinh_tb_ascii(s):
    return sum(ord(c) for c in s)/len(s) if s else 0

def nhap_list_chuoi():
    while True:
        try:
            N = int(input("Nhập số lượng chuỗi N (0<N<=50): "))
            if 0 < N <= 50: break
            print("N không hợp lệ. Nhập lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Nhập số nguyên.")
    a = []
    for i in range(N):
        while True:
            st = input(f"Nhập chuỗi thứ {i+1} (≤30 ký tự): ").strip()
            if len(st) <= 30: 
                a.append(st)
                break
            print("Chuỗi quá dài. Nhập lại.")
    return a

def phan_tich_co_ban(a):
    min_len, max_len = min(len(s) for s in a), max(len(s) for s in a)
    tb_len = sum(len(s) for s in a)/len(a)
    print(f"\nMin/Max độ dài: {min_len}/{max_len}, TB: {tb_len:.2f}")
    print("Chuỗi đối xứng:", [s for s in a if s==s[::-1]])
    email_re = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    print("Email chuẩn:", [s for s in a if re.match(email_re, s)])
    print("Chứa số:", [s for s in a if any(c.isdigit() for c in s)])
    print("Chứa in hoa:", [s for s in a if any(c.isupper() for c in s)])
    print("Độ dài giữa Min/Max:", [s for s in a if min_len < len(s) < max_len])
    return min_len, max_len

def phan_tich_tim_kiem(a):
    st = input("Nhập chuỗi st để tìm cùng kích thước: ").strip()
    print(f"Cùng kích thước {len(st)}:", [s for s in a if len(s)==len(st)])
    try:
        do_dai = int(input("Nhập độ dài xác định: "))
        print(f"Độ dài {do_dai}:", [s for s in a if len(s)==do_dai])
    except ValueError:
        print("Độ dài không hợp lệ.")

    c = input("Nhập ký tự c để tìm: ").strip()
    print(f"Chứa ký tự '{c}': {[s for s in a if c in s]}")

    try:
        M_count = int(input("Nhập số lượng chuỗi M để đếm tần suất: "))
        if 0 < M_count < len(a):
            M = [input(f"Chuỗi M thứ {i+1}: ").strip() for i in range(M_count)]
            print("Tần suất M:", {s:a.count(s) for s in M})
    except ValueError:
        print("Dữ liệu M không hợp lệ.")

def phan_tich_in_an(a):
    print("Min/Max ASCII:", min(a), "/", max(a))
    print("Sắp xếp ASCII tăng:", sorted(a))
    print("Sắp xếp ASCII giảm:", sorted(a, reverse=True))
    print("Số từ mỗi chuỗi:", [len(s.split()) for s in a])
    print("Nối chuỗi:", ' '.join(a))
    print("Chuỗi chứa chuỗi đầu tiên:", [s for s in a if a[0] in s])
    print("Trung bình ASCII từng chuỗi:", [f"{tinh_tb_ascii(s):.2f}" for s in a])

def thao_tac_thay_doi(a):
    # chèn '|' vào chuỗi cuối
    a[-1] = a[-1][:5] + '|' + a[-1][5:] if len(a[-1])>=5 else a[-1]+'|'
    print("Chuỗi cuối sau chèn '|':", a[-1])
    if len(a)>=2:
        print(f"Chuỗi áp chót có số từ:", len(a[-2].split()))
        a[1] = a[1].upper()
        print("Chuỗi thứ 2 thành HOA:", a[1])
    chuoi_cuoi = a[-1]
    print("Cắt trắng cuối:", chuoi_cuoi.rstrip())
    print("Cắt trắng đầu:", chuoi_cuoi.lstrip())
    print("Chuẩn hóa khoảng trắng:", ' '.join(chuoi_cuoi.split()))

if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH XỬ LÝ LIST CHUỖI ===")
    lst = nhap_list_chuoi()
    phan_tich_co_ban(lst)
    phan_tich_tim_kiem(lst)
    phan_tich_in_an(lst)
    thao_tac_thay_doi(lst)
