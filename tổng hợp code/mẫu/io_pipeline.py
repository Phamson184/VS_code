#xu li file
import os
def file():
    ds=[]
    if not os.path.exists("data_input.txt"):
        print("Lỗi: không tìm thấy file data_input.txt")
        return
    with open("data_input.txt","r") as f_in:
        for dong in f_in:
            data=dong.strip()
            if not data:
                continue
            try:
                ds.append(float(data))
            except ValueError:
                print(f"Cảnh báo: Đã bỏ qua dữ liệu không hợp lệ '{data}")
    if len(ds)>0:
        tb=sum(ds)/len(ds)
    else:
        tb=0
    with open("ket_qua.txt","r") as f_out:
        f_out.write(f"Trung bình cộng là: {tb}")
    print(f"Đã ghi kết quả {tb} vào file ket_qua.txt")
with open("data_input.txt","w") as f_tao:
    f_tao.write("10\n20.5\n\nLoi_TyPo\n30\n40\n50")
file()
#
import math
import os

# ================= 1. CÁC HÀM XỬ LÝ LÕI =================
def la_chinh_phuong(x):
    if x < 0: return False
    can = int(math.sqrt(x))
    return can * can == x

# ================= 2. I/O FILE =================
def doc_danh_sach_so(filepath):
    """Đọc file và trả về list số nguyên."""
    if not os.path.exists(filepath):
        print(f"Lỗi: Không tìm thấy file {filepath}")
        return []
        
    with open(filepath, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def ghi_ket_qua(filepath, noi_dung_list):
    """Ghi danh sách kết quả ra file trong 1 lần duy nhất."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(noi_dung_list) + '\n')
    print(f"Đã ghi toàn bộ kết quả vào {filepath}")

# ================= 3. HÀM ĐIỀU PHỐI (MAIN PIPELINE) =================
def main_process(input_file, output_file):
    # Bước 1: Đọc 1 lần duy nhất
    numbers = doc_danh_sach_so(input_file)
    if not numbers:
        return
        
    # Bước 2: Xử lý dữ liệu trong RAM
    so_duong = [x for x in numbers if x > 0]
    so_cp = [x for x in numbers if la_chinh_phuong(x)]
    
    ket_qua = []
    # Xử lý số dương
    if so_duong:
        ket_qua.append(f'Số dương nhỏ nhất: {min(so_duong)}')
        ket_qua.append(f'Số dương lớn nhất: {max(so_duong)}')
    else:
        ket_qua.append('Không có số dương trong file.')
        
    # Xử lý số chính phương
    if so_cp:
        ket_qua.append('Các số chính phương: ' + ', '.join(map(str, so_cp)))
    else:
        ket_qua.append('Không có số chính phương.')

    # Bước 3: Ghi ra file 1 lần duy nhất
    ghi_ket_qua(output_file, ket_qua)

# ================= CHẠY THỬ =================
if __name__ == '__main__':
    # Tạo data mẫu
    with open('data.txt', 'w') as f:
        f.write('\n'.join(map(str, [-3, 0, 7, -1, 4, 9, -5, 16, 25, 8])))
        
    # Chạy pipeline
    main_process('data.txt', 'output.txt')
#
import csv

def process_csv_template(input_csv, output_csv):
    """
    Template chuẩn để đọc dữ liệu từ CSV, lọc thông tin và ghi ra CSV mới.
    Ví dụ: Lọc các học sinh có điểm >= 8.0
    """
    du_lieu_da_loc = []
    
    # 1. ĐỌC DỮ LIỆU
    try:
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f) # Đọc thành dạng Dictionary
            for row in reader:
                # Xử lý ngay khi đọc từng dòng để tiết kiệm RAM
                if float(row['Diem']) >= 8.0:
                    du_lieu_da_loc.append(row)
    except FileNotFoundError:
        print("Không tìm thấy file input.")
        return

    # 2. GHI DỮ LIỆU
    if du_lieu_da_loc:
        with open(output_csv, 'w', encoding='utf-8', newline='') as f:
            # Lấy tên cột từ dòng đầu tiên
            fieldnames = du_lieu_da_loc[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(du_lieu_da_loc)
        print(f"Đã lưu {len(du_lieu_da_loc)} dòng vào {output_csv}")