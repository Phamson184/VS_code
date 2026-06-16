from pypdf import PdfWriter
import os

def merge_all_pdfs(output_filename):
    # Khởi tạo PdfWriter thay vì PdfMerger
    merger = PdfWriter()
    
    # Lấy danh sách toàn bộ file PDF trong cùng thư mục (bỏ qua file kết quả nếu đã có)
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf') and f != output_filename]
    
    # Sắp xếp thứ tự file 
    pdf_files.sort()
    
    if not pdf_files:
        print("Không tìm thấy file PDF nào trong thư mục.")
        return

    print(f"Đang gộp các file: {pdf_files}")
    
    # Đọc và gộp từng file
    for pdf in pdf_files:
        merger.append(pdf)
        
    # Xuất ra file cuối cùng
    merger.write(output_filename)
    merger.close()
    print(f"Đã gộp thành công! File lưu tại: {output_filename}")

# Chạy hàm để tạo ra file gộp cuối cùng
merge_all_pdfs("tai_lieu_hoan_chinh.pdf")
