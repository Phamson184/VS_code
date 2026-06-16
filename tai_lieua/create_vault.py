import os

VAULT = r"G:\Workspace\Personal-Project\So-Tay-Ca-Nhan"

files = {}

# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
files["Dashboard.md"] = """\
# 🏠 Dashboard — Sổ Tay Cá Nhân

> Mở file này mỗi ngày. Mọi thứ khác tra từ đây.

---

## Hôm nay tập gì?
→ [[Lich-Tap|📅 Xem lịch tập 5 ngày]]

---

## Tra cứu nhanh
| Nhóm | Link |
|------|------|
| Bài sửa tư thế (làm mỗi ngày) | [[Sua-Tu-The]] |
| Vai & Ngực | [[Vai-Nguc]] |
| Lưng & Core | [[Lung-Core]] |
| Chân | [[Chan]] |
| Tay & Forearm | [[Tay-Forearm]] |

---

## Võ thuật
| | Link |
|-|------|
| Học môn gì, thứ tự | [[Lo-Trinh-Vo]] |
| Sifu vs thực tế | [[Sifu-Thuc-Te]] |
| Tìm video đúng cách | [[Tim-Video]] |

---

## Tra từ lạ
- [[Glossary-The-Hinh|Thuật ngữ thể hình]]
- [[Glossary-Vo-Thuat|Thuật ngữ võ thuật]]
"""

# ─────────────────────────────────────────────
# LỊCH TẬP
# ─────────────────────────────────────────────
files["Lich-Tap.md"] = """\
# 📅 Lịch Tập — 5 Ngày/Tuần

Mỗi buổi: **25–35 phút**
Cấu trúc: Sửa tư thế (10p) → Bài chính (20p) → Giãn nhanh (5p)

---

## Thứ 2 — Tư Thế + Vai/Ngực
- [[Sua-Tu-The]] — 10 phút
- [[Vai-Nguc#Push-up Chuẩn|Push-up Chuẩn]]
- [[Vai-Nguc#Pike Push-up|Pike Push-up]]
- [[Lung-Core#Dead Bug|Dead Bug]]

## Thứ 3 — Lưng + Core
- [[Sua-Tu-The]] — 10 phút
- [[Lung-Core#Inverted Row|Inverted Row]]
- [[Sua-Tu-The#Scapular Push-up|Scapular Push-up]]
- [[Lung-Core#Dead Bug|Dead Bug]]

## Thứ 4 — Chân + Cẳng Tay
- [[Sua-Tu-The#Hip Flexor Stretch|Hip Flexor Stretch]]
- [[Chan#Bodyweight Squat|Bodyweight Squat]]
- [[Chan#Bulgarian Split Squat|Bulgarian Split Squat]]
- [[Tay-Forearm#Wrist Flex/Extend|Wrist Flex/Extend]]
- [[Tay-Forearm#Towel Curl|Towel Curl]]

## Thứ 5 — Vai + Cổ
- [[Sua-Tu-The#Wall Angels|Wall Angels]]
- [[Vai-Nguc#Pike Push-up|Pike Push-up]]
- [[Vai-Nguc#Neck Isometric|Neck Isometric]]
- [[Sua-Tu-The#Scapular Push-up|Scapular Push-up]]

## Thứ 6 — Toàn Thân Nhẹ
- Tất cả bài [[Sua-Tu-The]]
- 2–3 bài tự chọn từ tuần
- [[Lung-Core#Dead Hang|Dead Hang]] — kết thúc buổi

---

← [[Dashboard|🏠 Dashboard]]
"""

# ─────────────────────────────────────────────
# BÀI TẬP — SỬA TƯ THẾ
# ─────────────────────────────────────────────
files["Bai-Tap/Sua-Tu-The.md"] = """\
# 🔧 Sửa Tư Thế — Làm Mỗi Ngày (10 phút)

> Đây là phần quan trọng nhất. Làm trước mọi bài tập khác.

---

## Posterior Pelvic Tilt Drill
**10 lần × 10 giây giữ**

Nằm ngửa, gập gối.
Siết bụng → kéo lưng dưới ép sát sàn hoàn toàn.
Tưởng tượng đang dán lưng xuống.

→ Chữa ưỡn lưng

---

## Wall Angels
**2 hiệp × 10–15 reps**

Đứng sát tường: lưng + mông + đầu + khuỷu đều chạm tường.
Dang tay lên (chữ Y) → hạ xuống (chữ W). Chậm.
Khó hơn tưởng — đừng để vai rời tường.

→ Mở vai, sửa gù

---

## Hip Flexor Stretch
**30–45 giây/bên × 2–3 lần**

Quỳ 1 gối, chân kia gập 90 độ trước.
Đẩy hông về trước → cảm nhận căng ở bẹn/đùi trên chân phía sau.
Giữ lưng thẳng, không ngả người.

→ Giải phóng hip flexor — thủ phạm chính của ưỡn bụng

---

## Scapular Push-up
**3 hiệp × 12–15 reps**

Tư thế hít đất, giữ tay thẳng — không gập khuỷu.
Chỉ dùng bả vai: kéo hai bả vai lại gần nhau → đẩy ra xa.
Chuyển động nhỏ nhưng rất quan trọng.

→ Kiểm soát scapula

---

← [[Dashboard|🏠 Dashboard]] · [[Lich-Tap|📅 Lịch tập]]
"""

# ─────────────────────────────────────────────
# BÀI TẬP — VAI & NGỰC
# ─────────────────────────────────────────────
files["Bai-Tap/Vai-Nguc.md"] = """\
# 💪 Vai & Ngực

---

## Push-up Chuẩn
**4 hiệp × 8–15 reps**

Khuỷu tay 30–45 độ so với thân (không dang ngang).
Siết bụng, không võng lưng.
Kiểm soát chiều xuống — đừng thả người đột ngột.

→ Ngực + vai trước + core

---

## Pike Push-up
**3–4 hiệp × 6–10 reps**

Từ tư thế hít đất, đẩy mông lên cao (hình chữ V ngược).
Đầu cúi xuống nhìn về phía chân.
Thực hiện hít đất trong tư thế này — trọng lượng dồn lên vai.

→ Vai giữa + vai sau — quan trọng nhất cho chiều rộng khung

---

## Neck Isometric
**2 hiệp × 12–15 reps/hướng**

Đặt lòng bàn tay lên trán / thái dương / gáy.
Tạo lực cản bằng tay — đầu cố đẩy vào tay nhưng không di chuyển.
Giữ 3–5 giây mỗi lần. Làm cả 4 hướng.

→ Cổ dày = khí chất tăng rõ, cân bằng tỉ lệ với đầu

---

← [[Dashboard|🏠 Dashboard]] · [[Lich-Tap|📅 Lịch tập]]
"""

# ─────────────────────────────────────────────
# BÀI TẬP — LƯNG & CORE
# ─────────────────────────────────────────────
files["Bai-Tap/Lung-Core.md"] = """\
# 🔙 Lưng & Core

---

## Inverted Row
**4 hiệp × 8–12 reps**

Bài kéo (pulling) — bắt buộc để cân bằng với push-up.

**3 cách làm tại nhà:**
- Chui dưới bàn vững: nằm ngửa, tay bám mép bàn, kéo ngực lên
- Door row: buộc khăn vào tay nắm cửa, ngả người ra sau rồi kéo
- Xà ngang công viên: tốt nhất nếu có

Cách làm đúng: siết vai về phía sau và xuống trước khi kéo.
Không để vai nhún lên tai. Ngực chạm điểm tựa = 1 rep.

→ Lưng xô (lats) — tạo chữ V, giúp vai không đổ

---

## Dead Bug
**3 hiệp × 8–10 reps/bên**

Nằm ngửa, tay thẳng lên trời, gối gập 90 độ.
Từ từ duỗi tay phải + chân trái xuống song song sàn.
Giữ lưng không rời sàn. Đổi bên. Thở đều, không nín thở.

→ Core chống ưỡn — nền tảng cho mọi bài khác

---

## Dead Hang
**20–40 giây × 3 hiệp — làm cuối buổi**

Treo người thẳng lên xà, không co người.
Buông lỏng hoàn toàn. Thở sâu và đều.

→ Giải nén cột sống + kéo giãn toàn thân

---

← [[Dashboard|🏠 Dashboard]] · [[Lich-Tap|📅 Lịch tập]]
"""

# ─────────────────────────────────────────────
# BÀI TẬP — CHÂN
# ─────────────────────────────────────────────
files["Bai-Tap/Chan.md"] = """\
# 🦵 Chân

---

## Bodyweight Squat
**4 hiệp × 15–20 reps**

Chân rộng bằng vai.
Ngồi xuống chậm (3–4 giây) → giữ đáy 2 giây → đứng lên.
Gối không vượt qua mũi chân quá nhiều. Nhìn thẳng, lưng thẳng.

→ Đùi và mông — tạo cảm giác cân đối thân trên-dưới

---

## Bulgarian Split Squat
**3 hiệp × 8–10 reps/bên**

Đặt một chân lên ghế/giường phía sau.
Chân trước gập 90 độ.
Ngồi xuống thẳng đứng — không để gối trước đổ vào trong.

→ Áp lực đơn chân — hiệu quả hơn squat đều cho mông và đùi

---

← [[Dashboard|🏠 Dashboard]] · [[Lich-Tap|📅 Lịch tập]]
"""

# ─────────────────────────────────────────────
# BÀI TẬP — TAY & FOREARM
# ─────────────────────────────────────────────
files["Bai-Tap/Tay-Forearm.md"] = """\
# ✋ Tay & Forearm

> Đừng lạm biceps. Forearm quan trọng hơn cho visual hàng ngày.

---

## Towel Curl
**3 hiệp × chậm đến mỏi**

Cuộn khăn thành ống dài, cầm hai đầu.
Dùng sức tay bóp chặt và kéo căng ngược chiều nhau.
Giữ 3–5 giây rồi thả từ từ.

→ Cẳng tay dày — trông khỏe kể cả mặc áo tay ngắn đơn giản

---

## Wrist Flex/Extend
**3 hiệp × 15–20 reps**

Cầm chai nước hoặc vật nặng nhẹ.
Đặt cẳng tay lên đùi — chỉ dùng cổ tay uốn lên rồi xuống.
Làm cả hai chiều. Chuyển động chậm.

→ Forearm rõ nét — nhóm cơ bị bỏ qua nhiều nhất

---

← [[Dashboard|🏠 Dashboard]] · [[Lich-Tap|📅 Lịch tập]]
"""

# ─────────────────────────────────────────────
# VÕ THUẬT — LỘ TRÌNH
# ─────────────────────────────────────────────
files["Vo-Thuat/Lo-Trinh-Vo.md"] = """\
# 🥋 Lộ Trình Học Võ

Mục tiêu: bảo vệ người khác — không phải thi đấu.

---

## Thứ tự ưu tiên

### 1 — Bắt Buộc: Judo hoặc BJJ
Grappling là nền tảng.
Biết quật, giữ, kiểm soát mà không cần đánh.
Thực tế nhất trong đụng độ đời thường.
> Nếu chỉ chọn 1 môn duy nhất → **Judo** hoặc **BJJ**

### 2 — Rất Nên: Muay Thai
Có clinch (ôm đứng), gối, chỏ.
Bổ sung hoàn hảo cho grappling.
Có spar thật từ sớm.

### 3 — Thêm Vào: Boxing
Guard, di chuyển, phản xạ, chịu đòn.
Nền tảng striking tốt nhất để bắt đầu.

### Tìm Hiểu Thêm: Pak Mei / Southern Kung Fu
Cho tư thế, trọng tâm, nguyên lý phát lực ngắn.
Học qua video + tự tập — không cần lớp học.
→ [[Sifu-Thuc-Te|Xem thêm về Sifu và Pak Mei]]

---

## Về Karate
- Có spar thật + dạy ứng dụng → ổn
- Chỉ học kata múa → bỏ qua

---

← [[Dashboard|🏠 Dashboard]]
"""

# ─────────────────────────────────────────────
# VÕ THUẬT — SIFU VS THỰC TẾ
# ─────────────────────────────────────────────
files["Vo-Thuat/Sifu-Thuc-Te.md"] = """\
# 🎮 Sifu vs Thực Tế

Sifu dựa trên **Pak Mei Kung Fu** (Bạch Mi Quyền) — võ phái Nam Trung Hoa.
Nhiều nguyên lý trong game có nền tảng thực tế.

---

## Có thể học áp dụng ✓
- Tư thế thấp, trọng tâm ổn định
- Phát lực ngắn từ eo (không dùng biên độ lớn)
- Áp sát và kiểm soát khoảng cách
- Đòn chỏ/gối ở cự ly gần (0–1m)
- Tận dụng môi trường (tường, cản vật)
- Phá trụ đối phương trước khi đánh

## Không thực tế ngoài game ✗
- Combo 15 đòn liên tiếp không sơ hở
- Hất người vào tường bằng 1 tay
- Đứng dậy ngay sau khi ngã nặng
- Đánh 8 người cùng lúc

---

## Các nhóm kỹ thuật cốt lõi

### Phá Trụ (Structure Breaking)
Làm mất thăng bằng đối phương trước — đánh sau.
- Palm strike: an toàn hơn nắm đấm, lực tốt
- Elbow (chỏ): cực mạnh ở cự ly dưới 1m
- Short punch: phát lực từ eo, không cần rút tay

### Quét Chân
Sweep/low kick vào cổ chân hoặc bắp chân.
Hiệu quả nhất khi kết hợp đẩy tay ngược chiều đồng thời.

### Đòn Ngắn Cự Ly 0–1m
Vùng quan trọng nhất trong đụng độ thực tế.
Boxing yếu ở đây — Pak Mei và Muay Thai clinch mạnh nhất.

---

> Học Sifu để hiểu tư thế, trọng tâm, áp sát.
> Cách thể hiện trong game là nghệ thuật, không phải tài liệu huấn luyện.

← [[Dashboard|🏠 Dashboard]] · [[Lo-Trinh-Vo|Lộ trình học võ]]
"""

# ─────────────────────────────────────────────
# VÕ THUẬT — TÌM VIDEO
# ─────────────────────────────────────────────
files["Vo-Thuat/Tim-Video.md"] = """\
# 🔍 Tìm Video Đúng Cách

---

## Video tốt có ít nhất 2/4 dấu hiệu
- Giải thích rõ mục tiêu bài tập
- Làm chậm lại kỹ thuật
- Chỉ ra lỗi sai thường gặp
- Có đối tác kháng nhẹ (drilling)

## Video rác — bỏ qua ngay
- Chỉ có nhạc nền, không giải thích
- Cắt cảnh liên tục
- Tiêu đề kiểu "Self-defense in 7 days" / "One hit KO"
- Không có spar / drilling / kháng lực

---

## Nhóm 1 — Tư Thế & Khí Chất (Pak Mei)
Từ khóa:
- `Pak Mei Kung Fu fundamentals`
- `Southern Chinese martial arts body mechanics`
- `Short power martial arts`

Chỉ học 4 thứ từ nhóm này:
1. Cách đứng (stance) — giữ 2–5 phút
2. Trọng tâm thấp — cảm giác điều khiển từ eo
3. Xoay eo — phát lực ngắn
4. Giữ tay che trung tuyến

**Đừng học:** combo nhanh, đánh điểm hiểm, kỹ thuật "kết liễu"

---

## Nhóm 2 — Guard & Phòng Thủ
Từ khóa:
- `Boxing defense fundamentals`
- `Boxing guard drill beginner`
- `Muay Thai clinch basic drill`

Học: che đầu, di chuyển chân, giữ thăng bằng khi bị đẩy, shadowboxing chậm

---

## Nhóm 3 — Grappling Solo
Từ khóa:
- `Judo basics solo drill`
- `BJJ fundamental movement solo`
- `Wrestling stance and motion drill`

Học theo thứ tự:
1. **Breakfall (Ukemi)** — ngã an toàn, học trước tiên
2. **Shrimping / Hip escape** — di chuyển khi nằm dưới
3. **Technical stand-up** — đứng dậy an toàn
4. **Stance & motion drill** — đứng vững, di chuyển không mất trụ

---

← [[Dashboard|🏠 Dashboard]] · [[Lo-Trinh-Vo|Lộ trình học võ]]
"""

# ─────────────────────────────────────────────
# GLOSSARY — THỂ HÌNH
# ─────────────────────────────────────────────
files["Glossary/Glossary-The-Hinh.md"] = """\
# 📖 Thuật Ngữ Thể Hình

---

| Thuật ngữ | Giải thích |
|-----------|------------|
| **Hip Flexor** | Cơ gập hông — nối xương chậu với đùi, mặt trước háng. Ngồi nhiều → căng → gây ưỡn lưng |
| **Hamstring** | Cơ phía sau đùi. Căng → ảnh hưởng tư thế và dễ chấn thương lưng |
| **Scapula** | Xương bả vai — hình tam giác ở lưng trên. Cần kiểm soát tốt để vai không đổ |
| **Anterior Pelvic Tilt** | Ưỡn lưng dưới — hông đổ ra trước, lưng cong quá mức. Phổ biến khi ngồi nhiều |
| **Posterior Pelvic Tilt** | Ngược lại — kéo lưng dưới thẳng bằng cách siết bụng, kéo hông vào trong |
| **Rounded Shoulders** | Vai đổ về trước, ngực hẹp. Do cơ ngực căng + cơ lưng trên yếu |
| **Deltoids (Delts)** | Cơ vai — 3 đầu: trước, giữa, sau. Vai giữa và sau quan trọng nhất cho chiều rộng |
| **Lats** | Cơ lưng xô (Latissimus Dorsi) — cơ lớn nhất lưng, tạo hình chữ V |
| **Trapezius (Trap)** | Cơ thang — từ cổ xuống vai và lưng giữa. Trap trên to = cổ dày |
| **Rhomboids** | Cơ giữa hai bả vai — kéo scapula lại. Yếu = vai đổ ra trước |
| **Core** | Không chỉ cơ bụng — toàn bộ cơ thân mình (bụng, lưng, hông) |
| **Time Under Tension** | Tổng thời gian cơ chịu lực trong 1 hiệp. Chậm = TUT cao = cơ phát triển tốt hơn |
| **Progressive Overload** | Tăng dần độ khó (thêm reps, thêm hiệp, bớt nghỉ). Nguyên tắc tăng trưởng cơ |
| **Mind-Muscle Connection** | Tập trung ý thức vào cơ đang tập — không nghĩ lung tung khi tập |

---

← [[Dashboard|🏠 Dashboard]]
"""

# ─────────────────────────────────────────────
# GLOSSARY — VÕ THUẬT
# ─────────────────────────────────────────────
files["Glossary/Glossary-Vo-Thuat.md"] = """\
# 📖 Thuật Ngữ Võ Thuật

---

| Thuật ngữ | Giải thích |
|-----------|------------|
| **Grappling** | Khóa, quật, giữ, kiểm soát — không dùng đòn đánh mạnh. Judo, BJJ, Wrestling |
| **Striking** | Kỹ thuật đánh — đấm, đá, chỏ, gối. Boxing, Muay Thai, Karate |
| **Guard** | Tư thế phòng thủ tay — che mặt và đầu. Nắm đấm hai bên mặt, khuỷu che sườn |
| **Clinch** | Ôm đứng ở cự ly rất gần. Muay Thai clinch cho phép dùng gối và chỏ |
| **Sweep** | Quét chân — làm mất thăng bằng đối phương |
| **Shrimping** | Di chuyển bằng hông khi nằm dưới — cơ bản nhất của BJJ |
| **Hip Escape** | Tạo khoảng hở giữa bạn và đối phương khi bị ghì. Tương tự shrimping |
| **Technical Stand-up** | Đứng dậy an toàn khi đối phương gần — không để lộ lưng |
| **Breakfall (Ukemi)** | Kỹ thuật ngã an toàn từ Judo. Học trước mọi thứ khác |
| **Kata** | Bài quyền — chuỗi kỹ thuật tập một mình, không có đối tác kháng |
| **Sparring** | Tập đối kháng thật với đối tác, có kiểm soát. Cần thiết để kỹ thuật hoạt động thực tế |
| **Drilling** | Lặp 1 kỹ thuật nhiều lần với đối tác — hình thành kỹ năng cơ bản |
| **Pak Mei (Bạch Mi)** | Võ phái Nam Trung Hoa — đòn ngắn, lực từ eo, áp sát. Nền tảng trong Sifu |
| **Structure Breaking** | Phá trụ — làm mất tư thế và thăng bằng đối phương trước khi đánh |
| **Palm Strike** | Đánh bằng lòng bàn tay — ít rủi ro chấn thương hơn nắm đấm |

---

← [[Dashboard|🏠 Dashboard]]
"""

# ─────────────────────────────────────────────
# TẠO FILES
# ─────────────────────────────────────────────
print(f"Đang tạo vault tại: {VAULT}\n")

for relative_path, content in files.items():
    full_path = os.path.join(VAULT, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {relative_path}")

print(f"\nXong! Mở Obsidian → Open folder as vault → chọn thư mục:")
print(f"  {VAULT}")
