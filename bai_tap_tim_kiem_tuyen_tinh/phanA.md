### Bài 1: Trình bày ý tưởng
* **Ý tưởng:** Tìm kiếm tuyến tính duyệt lần lượt từng phần tử của dãy, so sánh với giá trị cần tìm x đến khi tìm thấy hay duyệt hết dãy.
* **Input:** Một mảng (danh sách) chứa các phần tử và một giá trị $x$ cần tìm.
* **Output:** Vị trí (chỉ số) của phần tử nếu tìm thấy, hoặc thông báo/trả về `-1` nếu không có.
* **Điều kiện dừng:** Khi tìm thấy giá trị $x$ hoặc duyệt hết toàn bộ dãy mà không tìm thấy.

### Bài 2: Mô phỏng từng bước
Cho mảng `A = [7, 3, 9, 12, 5, 8, 1]` và `x = 5`.

| Chỉ số i | Giá trị A[i] | Kết quả so sánh (A[i] == x) | Kết luận |
| :---: | :---: | :---: | :--- |
| 0 | 7 | Sai | Tiếp tục |
| 1 | 3 | Sai | Tiếp tục |
| 2 | 9 | Sai | Tiếp tục |
| 3 | 12 | Sai | Tiếp tục |
| **4** | **5** | **Đúng** | **Dừng** |

 **Kết quả:** Hàm trả về giá trị `4` (vị trí của phần tử 5).

### Bài 3: Đếm số phép so sánh
Với mảng `A` ở Bài 2:
* (a) Tìm `x = 7`: Cần **1** phép so sánh.
* (b) Tìm `x = 1`: Cần **7** phép so sánh.
* (c) Tìm `x = 100`: Cần **7** phép so sánh vì duyệt hết mảng.
* **Nhận xét:** Phần tử cần tìm càng nằm về cuối mảng thì càng cần nhiều phép so sánh và để duyệt hết phần tử trong mảng thì cần bấy nhiêu phép so sánh trong mảng mà nếu phần tử không tồn tại thì số phép so sánh cũng bằng số lượng phần tử trong mảng.

### Bài 4: Phân tích độ phức tạp
Một mảng có $n$ phần tử:
* **Trường hợp tốt nhất:** 1 phép so sánh.
* **Trường hợp xấu nhất:** $n$ phép so sánh.
* **Trường hợp trung bình:** $n/2$ phép so sánh.
* **Độ phức tạp thời gian (Big O):** $O(n)$.

### Bài 5: Điều kiện áp dụng và so sánh
* Tìm kiếm tuyến tính không cần mảng đã sắp xếp vì tính chất duyệt tuần tự thì có sắp xếp cũng không tạo ra sự khác biệt. Thế nên tìm kiếm tuyến tính phù hợp để xử lí dữ liệu hỗn loạn và với dữ liệu tương đối nhỏ thì độ chênh lệch hiệu năng so với các thuật toán khác là ít mà dễ triển khai.
*  So với nhị phân về điều kiện thì nhị phân bắt buộc dữ liệu đã sắp xếp vì khi có thứ tự thì mới xác định được nên tìm tiếp ở nửa nào, khoanh vùng nhanh hơn trên mảng lớn. 
  * Về độ phức tạp: Tuyến tình là O(n)- dữ liệu tăng bao nhiêu thì bước tăng theo. Nhị phân là O(log n)- mỗi bước loại bỏ một nửa dữ liệu còn lại nên dù mảng lớn thì số bước vẫn tăng rất chậm, dẫn đến ở quy mô lớn nhị phân nhẹ hơn tuyến tính.