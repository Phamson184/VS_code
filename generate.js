const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber, PageBreak, HeadingLevel,
  TableOfContents, Bookmark, NumberFormat
} = require('docx');
const fs = require('fs');

// ─── Palette ─────────────────────────────────────────────────────
const BLUE_DARK   = "1F4E79";
const BLUE_MID    = "2E75B6";
const BLUE_LIGHT  = "D6E4F0";
const BLUE_HEADER = "BDD7EE";
const GRAY_TEXT   = "404040";
const GREEN_DARK  = "1E5631";
const GREEN_LIGHT = "D9EAD3";
const ORANGE_DARK = "7B3F00";
const ORANGE_LIGHT= "FCE5CD";
const WHITE       = "FFFFFF";

// ─── Borders ─────────────────────────────────────────────────────
const thinBorder  = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
const thickBorder = { style: BorderStyle.SINGLE, size: 6, color: BLUE_MID, space: 1 };
const allBorders  = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };

// ─── Helpers ─────────────────────────────────────────────────────
function emptyLine(before=60, after=60) {
  return new Paragraph({ spacing:{before,after}, children:[new TextRun("")] });
}
function divider() {
  return new Paragraph({
    spacing:{before:120,after:120},
    border:{ bottom: thickBorder },
    children:[new TextRun("")]
  });
}
function para(text, opts={}) {
  return new Paragraph({
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { before: opts.before??100, after: opts.after??100, line:340, lineRule:"auto" },
    indent: opts.indent ? {firstLine:720} : undefined,
    children:[new TextRun({
      text, bold:opts.bold||false, italic:opts.italic||false,
      size: opts.size||24, font:"Times New Roman",
      color: opts.color||GRAY_TEXT
    })]
  });
}
function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    pageBreakBefore: true,
    alignment: AlignmentType.CENTER,
    spacing:{before:300,after:200},
    children:[new Bookmark({
      id: text.replace(/[^a-zA-Z0-9]/g,"_").slice(0,40),
      children:[new TextRun({
        text, bold:true, size:30,
        font:"Times New Roman", color:BLUE_DARK
      })]
    })]
  });
}
function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing:{before:240,after:120},
    children:[new TextRun({ text, bold:true, size:26, font:"Times New Roman", color:BLUE_MID })]
  });
}
function heading3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing:{before:180,after:80},
    children:[new TextRun({ text, bold:true, size:24, font:"Times New Roman", color:GRAY_TEXT })]
  });
}

// ─── Table cell builder ──────────────────────────────────────────
function tc(text, width, opts={}) {
  return new TableCell({
    columnSpan: opts.span||1,
    rowSpan: opts.rowSpan||1,
    borders: allBorders,
    shading:{ fill: opts.fill||WHITE, type:ShadingType.CLEAR },
    margins:{ top:80, bottom:80, left:120, right:120 },
    width:{ size:width, type:WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    children:[new Paragraph({
      alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing:{before:40,after:40,line:320,lineRule:"auto"},
      children:[new TextRun({
        text:String(text), bold:opts.bold||false, italic:opts.italic||false,
        size:opts.size||22, font:"Times New Roman",
        color: opts.color||GRAY_TEXT
      })]
    })]
  });
}

// ─── Cover ───────────────────────────────────────────────────────
function coverSection() {
  const noBorder = { style:BorderStyle.NONE };
  const noBorders = { top:noBorder, bottom:noBorder, left:noBorder, right:noBorder };
  const infoRow = (label, value) => new TableRow({ children:[
    new TableCell({ borders:noBorders, width:{size:3000,type:WidthType.DXA},
      children:[new Paragraph({ alignment:AlignmentType.RIGHT,
        children:[new TextRun({text:label, bold:true, size:24, font:"Times New Roman", color:BLUE_DARK})] })] }),
    new TableCell({ borders:noBorders, width:{size:5500,type:WidthType.DXA},
      children:[new Paragraph({
        children:[new TextRun({text:value, size:24, font:"Times New Roman", color:GRAY_TEXT})] })] }),
  ]});
  return [
    emptyLine(0,200),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:80},
      children:[new TextRun({ text:"TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN", bold:true, size:26, font:"Times New Roman", color:BLUE_DARK })] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:360},
      children:[new TextRun({ text:"KHOA HỆ THỐNG THÔNG TIN", bold:true, size:24, font:"Times New Roman", color:BLUE_MID })] }),
    divider(), emptyLine(120,120),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:160,after:80},
      children:[new TextRun({ text:"ĐỒ ÁN MÔN HỌC", bold:true, size:36, font:"Times New Roman", color:BLUE_DARK })] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:80},
      children:[new TextRun({ text:"PHÂN TÍCH VÀ THIẾT KẾ CƠ SỞ DỮ LIỆU", bold:true, size:26, font:"Times New Roman", color:BLUE_DARK })] }),
    emptyLine(160,80),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:40},
      children:[new TextRun({ text:"Đề tài:", size:26, font:"Times New Roman", color:GRAY_TEXT })] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:40,after:360},
      children:[new TextRun({ text:"QUẢN LÝ NHÀ THUỐC BÁN LẺ", bold:true, size:36, font:"Times New Roman", color:BLUE_MID })] }),
    emptyLine(80,80), divider(), emptyLine(120,80),
    new Table({
      width:{size:8500,type:WidthType.DXA}, columnWidths:[3000,5500],
      borders:{ top:{style:BorderStyle.NONE}, bottom:{style:BorderStyle.NONE},
                left:{style:BorderStyle.NONE}, right:{style:BorderStyle.NONE},
                insideH:{style:BorderStyle.NONE}, insideV:{style:BorderStyle.NONE} },
      rows:[
        infoRow("Lớp học phần:  ", "253_71ITIS30103_02"),
        infoRow("Nhóm:  ", "Team 13"),
        infoRow("Giảng viên hướng dẫn:  ", "Hà Đông Hưng"),
        infoRow("Phiên bản:  ", "0.2 — Tháng 6 năm 2026"),
      ]
    }),
    emptyLine(200,200), emptyLine(200,200),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:160,after:0},
      children:[new TextRun({ text:"TP. HỒ CHÍ MINH, NĂM 2026", bold:true, size:24, font:"Times New Roman", color:BLUE_DARK })] }),
    new Paragraph({ children:[new PageBreak()] }),
  ];
}

// ─── History tables ───────────────────────────────────────────────
const HC = [800,3200,1200,4000]; // history col widths, sum=9200
function histHead() {
  const labels = ["STT","Nội dung","Phiên bản","Thành viên thực hiện"];
  return new TableRow({ tableHeader:true, children: labels.map((l,i)=>
    new TableCell({ borders:allBorders, shading:{fill:BLUE_DARK,type:ShadingType.CLEAR},
      margins:{top:100,bottom:100,left:120,right:120}, width:{size:HC[i],type:WidthType.DXA}, verticalAlign:VerticalAlign.CENTER,
      children:[new Paragraph({ alignment:AlignmentType.CENTER,
        children:[new TextRun({text:l,bold:true,color:WHITE,font:"Times New Roman",size:22})] })] })
  )});
}
function histRow(stt,nd,pv,tv,shade) {
  const fill = shade ? BLUE_LIGHT : WHITE;
  const vals = [String(stt),nd,pv,tv];
  return new TableRow({ children: vals.map((v,i)=>
    new TableCell({ borders:allBorders, shading:{fill,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120}, width:{size:HC[i],type:WidthType.DXA}, verticalAlign:VerticalAlign.CENTER,
      children:[new Paragraph({ alignment: i===0?AlignmentType.CENTER:AlignmentType.LEFT,
        children:[new TextRun({text:v,font:"Times New Roman",size:22,color:GRAY_TEXT})] })] })
  )});
}

// ─── Constraint card (box per constraint) ────────────────────────
// We'll build a styled table per constraint group

// Group header
function groupHeader(num, title, fill, textColor) {
  return new Paragraph({
    spacing:{before:240,after:80},
    shading:{fill,type:ShadingType.CLEAR},
    border:{ left:{ style:BorderStyle.SINGLE, size:18, color:textColor } },
    indent:{ left:180 },
    children:[
      new TextRun({ text:`${num}  `, bold:true, size:26, font:"Times New Roman", color:textColor }),
      new TextRun({ text:title, bold:true, size:26, font:"Times New Roman", color:textColor }),
    ]
  });
}

// Constraint block: numbered badge + title + Mô tả + Kỹ thuật
function constraintBlock(num, title, desc, tech, shaded) {
  const fill = shaded ? BLUE_LIGHT : WHITE;
  const TW = 9200;
  const COL_NUM = 700;
  const COL_BODY = TW - COL_NUM;
  return new Table({
    width:{size:TW,type:WidthType.DXA},
    columnWidths:[COL_NUM, COL_BODY],
    margins:{top:60,bottom:60},
    rows:[
      new TableRow({ children:[
        // Badge cell (rowspan 3)
        new TableCell({
          rowSpan: 3,
          borders: allBorders,
          shading:{fill:BLUE_DARK,type:ShadingType.CLEAR},
          margins:{top:100,bottom:100,left:60,right:60},
          width:{size:COL_NUM,type:WidthType.DXA},
          verticalAlign:VerticalAlign.CENTER,
          children:[new Paragraph({ alignment:AlignmentType.CENTER,
            children:[new TextRun({ text:String(num), bold:true, size:28, font:"Times New Roman", color:WHITE })] })]
        }),
        // Title cell
        new TableCell({
          borders:allBorders,
          shading:{fill:BLUE_MID,type:ShadingType.CLEAR},
          margins:{top:80,bottom:80,left:160,right:120},
          width:{size:COL_BODY,type:WidthType.DXA},
          children:[new Paragraph({
            spacing:{before:40,after:40},
            children:[new TextRun({ text:title, bold:true, size:22, font:"Times New Roman", color:WHITE })] })]
        }),
      ]}),
      new TableRow({ children:[
        new TableCell({
          borders:allBorders,
          shading:{fill,type:ShadingType.CLEAR},
          margins:{top:80,bottom:80,left:160,right:120},
          width:{size:COL_BODY,type:WidthType.DXA},
          children:[
            new Paragraph({ spacing:{before:40,after:20}, children:[
              new TextRun({ text:"Mô tả:  ", bold:true, size:20, font:"Times New Roman", color:BLUE_MID }),
              new TextRun({ text:desc, size:20, font:"Times New Roman", color:GRAY_TEXT }),
            ]}),
          ]
        }),
      ]}),
      new TableRow({ children:[
        new TableCell({
          borders:allBorders,
          shading:{fill: shaded ? "#EAF4FB" : "#F4F9FE", type:ShadingType.CLEAR},
          margins:{top:80,bottom:80,left:160,right:120},
          width:{size:COL_BODY,type:WidthType.DXA},
          children:[
            new Paragraph({ spacing:{before:40,after:20}, children:[
              new TextRun({ text:"Kỹ thuật:  ", bold:true, size:20, font:"Times New Roman", color:GREEN_DARK }),
              new TextRun({ text:tech, size:20, font:"Times New Roman", color:GRAY_TEXT }),
            ]}),
          ]
        }),
      ]}),
    ]
  });
}

function spacer() { return emptyLine(80,80); }

// ─── Doc ─────────────────────────────────────────────────────────
const doc = new Document({
  numbering:{
    config:[
      { reference:"numbers", levels:[{ level:0, format:LevelFormat.DECIMAL, text:"%1.",
          alignment:AlignmentType.LEFT,
          style:{ paragraph:{ indent:{left:720,hanging:360}, spacing:{before:80,after:80} } } }] },
      { reference:"bullets", levels:[{ level:0, format:LevelFormat.BULLET, text:"\u2022",
          alignment:AlignmentType.LEFT,
          style:{ paragraph:{ indent:{left:720,hanging:360}, spacing:{before:60,after:60} } } }] },
    ]
  },
  styles:{
    default:{ document:{ run:{ font:"Times New Roman", size:24, color:GRAY_TEXT } } },
    paragraphStyles:[
      { id:"Heading1", name:"Heading 1", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{ size:30, bold:true, font:"Times New Roman", color:BLUE_DARK },
        paragraph:{ spacing:{before:300,after:200}, outlineLevel:0 } },
      { id:"Heading2", name:"Heading 2", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{ size:26, bold:true, font:"Times New Roman", color:BLUE_MID },
        paragraph:{ spacing:{before:240,after:120}, outlineLevel:1 } },
      { id:"Heading3", name:"Heading 3", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{ size:24, bold:true, font:"Times New Roman", color:GRAY_TEXT },
        paragraph:{ spacing:{before:180,after:80}, outlineLevel:2 } },
    ]
  },
  sections:[
    // ── Cover (no header/footer) ──────────────────────────────────
    {
      properties:{ page:{
        size:{width:11906,height:16838},
        margin:{top:1440,right:1080,bottom:1440,left:1800}
      }},
      children: coverSection()
    },
    // ── Main body ─────────────────────────────────────────────────
    {
      properties:{
        page:{ size:{width:11906,height:16838}, margin:{top:1440,right:1080,bottom:1440,left:1800} },
        pageNumberStart:1, pageNumberFormatType:NumberFormat.DECIMAL,
      },
      headers:{ default: new Header({ children:[
        new Paragraph({
          border:{ bottom:thickBorder }, spacing:{before:0,after:120},
          tabStops:[{type:"right",position:9026}],
          children:[
            new TextRun({text:"ĐỒ ÁN: QUẢN LÝ NHÀ THUỐC BÁN LẺ", bold:true, size:20, font:"Times New Roman", color:BLUE_DARK}),
            new TextRun({text:"\tLớp 253_71ITIS30103_02  ·  Team 13", size:18, font:"Times New Roman", color:"888888"}),
          ]
        })
      ]})},
      footers:{ default: new Footer({ children:[
        new Paragraph({
          border:{ top:thickBorder }, spacing:{before:120,after:0},
          alignment:AlignmentType.CENTER,
          children:[
            new TextRun({text:"Trang ", size:18, font:"Times New Roman", color:"888888"}),
            new TextRun({children:[PageNumber.CURRENT], size:18, font:"Times New Roman", color:BLUE_MID, bold:true}),
            new TextRun({text:" / ", size:18, font:"Times New Roman", color:"888888"}),
            new TextRun({children:[PageNumber.TOTAL_PAGES], size:18, font:"Times New Roman", color:"888888"}),
          ]
        })
      ]})},
      children:[

        // ── LỊCH SỬ THAY ĐỔI ─────────────────────────────────────
        heading1("LỊCH SỬ THAY ĐỔI"),
        emptyLine(),
        new Table({
          width:{size:9200,type:WidthType.DXA}, columnWidths:HC,
          rows:[
            histHead(),
            histRow(1,"Mô tả dự án (Project Description)","0.1","Võ Thành Long, Phạm Trường Sơn",false),
            histRow(2,"Sơ đồ ERD","0.1","Võ Thành Long, Phạm Trường Sơn",true),
            histRow(3,"Ràng buộc nghiệp vụ (Business Constraint)","0.1","Võ Thành Long, Phạm Trường Sơn",false),
            histRow(4,"Lược đồ cơ sở dữ liệu (Database Schema)","0.2","Võ Thành Long, Phạm Trường Sơn",true),
            histRow(5,"Sơ đồ dữ liệu logic (Logic Data Diagram)","0.2","Võ Thành Long, Phạm Trường Sơn",false),
            histRow(6,"Sơ đồ dữ liệu vật lý (Physical Data Diagram)","0.2","Võ Thành Long, Phạm Trường Sơn",true),
            histRow(7,"Lập trình SQL (SQL Programming)","0.2","Võ Thành Long, Phạm Trường Sơn",false),
          ]
        }),
        emptyLine(),
        heading2("Mức độ đóng góp thành viên"),
        emptyLine(),
        new Table({
          width:{size:9200,type:WidthType.DXA}, columnWidths:HC,
          rows:[
            new TableRow({ tableHeader:true, children:["STT","Thành viên","Phiên bản","Mức đóng góp"].map((l,i)=>
              new TableCell({ borders:allBorders, shading:{fill:BLUE_MID,type:ShadingType.CLEAR},
                margins:{top:100,bottom:100,left:120,right:120}, width:{size:HC[i],type:WidthType.DXA}, verticalAlign:VerticalAlign.CENTER,
                children:[new Paragraph({ alignment:AlignmentType.CENTER,
                  children:[new TextRun({text:l,bold:true,color:WHITE,font:"Times New Roman",size:22})] })] })
            )}),
            histRow(1,"Võ Thành Long","0.2","100%",false),
            histRow(2,"Phạm Trường Sơn","0.2","100%",true),
          ]
        }),
        emptyLine(),

        // ── MỤC LỤC ──────────────────────────────────────────────
        new Paragraph({ children:[new PageBreak()] }),
        new Paragraph({
          heading:HeadingLevel.HEADING_1,
          alignment:AlignmentType.CENTER,
          spacing:{before:300,after:200},
          children:[new TextRun({text:"MỤC LỤC",bold:true,size:30,font:"Times New Roman",color:BLUE_DARK})]
        }),
        new TableOfContents("Mục lục",{hyperlink:true, headingStyleRange:"1-3"}),
        new Paragraph({children:[new PageBreak()]}),

        // ════════════════════════════════════════════════
        // CHƯƠNG 1
        // ════════════════════════════════════════════════
        heading1("CHƯƠNG 1: MÔ TẢ DỰ ÁN"),
        divider(), emptyLine(),
        para("Hệ thống Quản lý Nhà thuốc bán lẻ là một nền tảng phần mềm toàn diện, được thiết kế chuyên biệt nhằm số hóa và tối ưu hóa toàn bộ vòng đời hoạt động của một cơ sở kinh doanh dược phẩm đạt tiêu chuẩn Thực hành tốt nhà thuốc (GPP – Good Pharmacy Practice). Hệ thống đóng vai trò như một lõi trung tâm xử lý nghiệp vụ, bao phủ bốn nhóm quy trình cốt lõi: quản lý danh mục, quản lý kho hàng, bán hàng và kê đơn, nhân sự và quan hệ khách hàng.", {indent:true}),
        emptyLine(),

        heading2("1.1  Quản lý Danh mục và Dữ liệu Nền tảng"),
        para("Hệ thống cung cấp không gian dữ liệu có cấu trúc để phân loại chi tiết hàng hóa thành các nhóm theo quy định pháp lý: thuốc kê đơn, thuốc không kê đơn (OTC), thực phẩm chức năng, thiết bị y tế và mỹ phẩm. Cơ sở dữ liệu duy trì cấu trúc phân cấp từ nhóm dược lý, hoạt chất, quy cách đóng gói đến hồ sơ pháp lý của nhà cung cấp, đảm bảo khả năng truy xuất nguồn gốc minh bạch theo quy định.",{indent:true}),
        para("Theo Quyết định số 540/QĐ-QLD của Cục Quản lý Dược, mã thuốc khi liên thông dữ liệu bắt buộc phải được tổ hợp theo cấu trúc: \"Số đăng ký thuốc – Quy cách đóng gói nhỏ nhất\". Yêu cầu này bắt buộc hệ thống phải lưu trữ các trường thông tin dưới dạng thuộc tính riêng biệt, có cấu trúc (structured attributes), loại bỏ hoàn toàn việc sử dụng trường văn bản tự do (free-text) dễ gây sai lệch trong quá trình đồng bộ với cơ quan quản lý nhà nước.",{indent:true}),
        emptyLine(),

        heading2("1.2  Quản trị Kho hàng, Lô thuốc và Hạn sử dụng"),
        para("Điểm khác biệt cốt lõi trong thiết kế cơ sở dữ liệu nhà thuốc so với bán lẻ thông thường là khái niệm vòng đời sản phẩm theo lô (Batch-level Lifecycle). Mỗi lần nhập kho, hệ thống bắt buộc phân mảnh dữ liệu tồn kho theo từng lô hàng riêng biệt với mã số sản xuất và hạn sử dụng (Expiry Date) tương ứng — ví dụ: \"Panadol: Lô X (HSD 01/2026) — 200 hộp; Lô Y (HSD 12/2026) — 300 hộp\".",{indent:true}),
        para("Cấu trúc dữ liệu phân rã theo lô là nền tảng để hệ thống thực thi thuật toán xuất kho FEFO (First Expired – First Out). Khi thực hiện bán hàng, Database Engine gọi một Stored Procedure tuần tự xác định lô hàng ưu tiên theo hạn sử dụng gần nhất và khấu trừ tồn kho theo thứ tự đó. Toàn bộ quá trình xử lý giao dịch phải tuân thủ tính chất ACID để ngăn chặn hiện tượng tồn kho âm (Negative Inventory) và khóa chết (Deadlock) trong môi trường đồng thời.",{indent:true}),
        emptyLine(),

        heading2("1.3  Giao dịch Bán hàng, Liên thông Điện tử và Quản lý Đơn thuốc"),
        para("Đối với thuốc thông thường (OTC), quy trình bán hàng được thực hiện qua quét mã vạch và tạo hóa đơn điện tử. Đối với thuốc kê đơn, hệ thống bắt buộc kích hoạt một luồng kiểm soát (workflow) tuân thủ Quyết định 4041/QĐ-BYT: khi phát hiện mặt hàng có cờ \"Thuốc kê đơn\", dược sĩ phải liên kết giao dịch với mã đơn thuốc quốc gia và nhập đầy đủ thông tin bác sĩ kê đơn (họ tên, nơi công tác) cùng chẩn đoán bệnh lý — các thông tin này được lưu thành các thực thể quan hệ gắn với hóa đơn.",{indent:true}),
        para("Sau khi giao dịch được COMMIT thành công vào cơ sở dữ liệu, một dịch vụ nền (background job hoặc message queue) tự động trích xuất, định dạng dữ liệu thành cấu trúc JSON/XML chuẩn và truyền tải qua API lên Cơ sở dữ liệu Dược Quốc gia (do Viettel vận hành). Trạng thái truyền tải được ghi nhận trong cơ sở dữ liệu để thực hiện cơ chế gửi lại (retry), đảm bảo tuân thủ yêu cầu báo cáo thời gian thực sau mỗi giao dịch.",{indent:true}),
        emptyLine(),

        heading2("1.4  Quản trị Nhân sự và Quan hệ Khách hàng (HR & CRM)"),
        para("Hồ sơ nhân sự được số hóa đầy đủ, bao gồm trình độ chuyên môn, chức danh và số Chứng chỉ hành nghề dược. Hệ thống sử dụng dữ liệu này để xây dựng cơ chế Phân quyền dựa trên vai trò (Role-Based Access Control – RBAC): chỉ tài khoản có chứng chỉ hành nghề dược sĩ đại học hợp lệ mới được phê duyệt hóa đơn chứa thuốc độc, thuốc hướng thần hoặc thuốc kê đơn phức tạp. Toàn bộ thao tác Thêm, Sửa, Xóa được ghi nhận vào bảng Audit Log phục vụ công tác thanh tra và đánh giá định kỳ GPP.",{indent:true}),
        para("Phân hệ CRM mở rộng hồ sơ khách hàng vượt ra ngoài thông tin liên hệ cơ bản, bao gồm lịch sử dị ứng thuốc và danh sách bệnh lý nền. Hệ thống tích hợp module chương trình khách hàng thân thiết (Loyalty Program), tự động tính điểm tích lũy theo giá trị hóa đơn và sinh mã giảm giá, nhằm nâng cao tỷ lệ tái mua hàng và trải nghiệm dịch vụ.",{indent:true}),
        emptyLine(),

        // ════════════════════════════════════════════════
        // CHƯƠNG 2
        // ════════════════════════════════════════════════
        heading1("CHƯƠNG 2: SƠ ĐỒ THỰC THỂ – LIÊN KẾT (ERD)"),
        divider(), emptyLine(),
        para("Để chuyển hóa các yêu cầu nghiệp vụ thành kiến trúc kỹ thuật, bước tiếp theo là xây dựng Sơ đồ Thực thể – Liên kết (Entity-Relationship Diagram – ERD). Quá trình thiết kế tuân thủ các quy tắc Chuẩn hóa dữ liệu (Database Normalization), đưa toàn bộ kiến trúc về Dạng chuẩn 3 (3NF – Third Normal Form) nhằm loại bỏ các dị thường dữ liệu (Data Anomalies).",{indent:true}),
        para("Cấu trúc cơ sở dữ liệu được thiết kế gồm 12 thực thể (Entities) cốt lõi. Các thực thể trung gian (Associative Entities) như CHI_TIET_HOA_DON và CHI_TIET_PHIEU_NHAP đóng vai trò phân giải các mối quan hệ Nhiều–Nhiều (N:N), đồng thời lưu trữ các thuộc tính phát sinh tại thời điểm giao dịch.",{indent:true}),
        emptyLine(),
        new Paragraph({
          alignment:AlignmentType.CENTER, spacing:{before:200,after:200},
          border:{ top:thinBorder, bottom:thinBorder, left:thinBorder, right:thinBorder },
          shading:{fill:BLUE_LIGHT,type:ShadingType.CLEAR},
          children:[new TextRun({ text:"[ DÁN HÌNH ẢNH SƠ ĐỒ ERD VÀO ĐÂY ]",
            bold:true, size:26, font:"Times New Roman", color:BLUE_MID, italics:true })]
        }),
        new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:80,after:120},
          children:[new TextRun({ text:"Hình 2.1 – Sơ đồ Thực thể – Liên kết (ERD) của Hệ thống Quản lý Nhà thuốc bán lẻ",
            italic:true, size:22, font:"Times New Roman", color:"666666" })] }),
        emptyLine(),

        // ════════════════════════════════════════════════
        // CHƯƠNG 3
        // ════════════════════════════════════════════════
        heading1("CHƯƠNG 3: RÀNG BUỘC NGHIỆP VỤ (BUSINESS CONSTRAINT)"),
        divider(), emptyLine(),

        para("Mô hình dữ liệu tĩnh (ERD) chỉ là bộ khung xương của hệ thống. Để biến nó thành một phần mềm quản trị thông minh, có khả năng tự động hóa và phòng ngừa rủi ro, các ràng buộc nghiệp vụ (Business Rules) phải được cấy sâu vào bên trong nhân của Hệ quản trị cơ sở dữ liệu (DBMS). Khi được khai báo ở tầng Database dưới dạng Constraint, Trigger hoặc Stored Procedure, các quy tắc này trở thành chốt chặn cuối cùng (Last line of defense) — ngay cả khi tầng giao diện người dùng bị lỗi hoặc bị vượt qua, cơ sở dữ liệu vẫn bảo vệ tính toàn vẹn của nghiệp vụ nhà thuốc GPP.",{indent:true}),
        para("Dưới đây là hệ thống gồm 15 ràng buộc nghiệp vụ được thiết kế chặt chẽ, chia thành ba nhóm cốt lõi.",{indent:true}),
        emptyLine(),

        // ── Nhóm 1 ───────────────────────────────────────────────
        groupHeader("Nhóm 1:", "Ràng buộc về Dữ liệu và Kho (Data & Inventory Rules)", BLUE_LIGHT, BLUE_DARK),
        para("Nhóm ràng buộc này đóng vai trò quyết định trong việc bảo vệ tính toàn vẹn của số liệu hàng hóa, ngăn chặn triệt để tình trạng thất thoát tài sản và hạn chế việc phân phối thuốc kém chất lượng ra cộng đồng.",{indent:true}),
        spacer(),

        constraintBlock(1,
          "Ràng buộc Hạn sử dụng khi Nhập kho tối thiểu (Minimum Expiry Constraint)",
          "Theo tiêu chuẩn GPP do Bộ Y tế ban hành, tất cả dược phẩm nhập kho từ nhà cung cấp bắt buộc phải có thời hạn sử dụng còn lại ít nhất 06 tháng tính từ thời điểm nhập liệu. Quy định nhằm đảm bảo an toàn lưu thông và duy trì chất lượng tồn kho.",
          "Thực thi qua BEFORE INSERT TRIGGER trên bảng LO_THUOC hoặc CHI_TIET_PHIEU_NHAP. Trigger so sánh GETDATE() và cột HanSuDung bằng hàm DATEDIFF(month). Nếu khoảng cách < 6 tháng, hệ thống ném Exception và ROLLBACK toàn bộ phiên giao dịch nhập kho.",
          false),
        spacer(),

        constraintBlock(2,
          "Thuật toán Trừ tồn kho tự động theo nguyên tắc FEFO (First Expired – First Out)",
          "Nhà thuốc không được tự chọn lô hàng xuất ngẫu nhiên. Hệ thống phải tự động ưu tiên phân bổ số lượng bán cho những lô thuốc có hạn sử dụng gần nhất (nhưng chưa quá hạn), tối ưu vòng quay hàng tồn kho, tránh tồn đọng thuốc quá date.",
          "Cơ chế FEFO bắt buộc dùng STORED PROCEDURE cho giao dịch bán hàng. Thủ tục dùng CURSOR hoặc WINDOW FUNCTION duyệt bảng LO_THUOC theo điều kiện ORDER BY HanSuDung ASC, lặp và trừ lùi SoLuongTon qua từng lô liên tiếp đến khi đáp ứng đủ số lượng yêu cầu.",
          true),
        spacer(),

        constraintBlock(3,
          "Ràng buộc Cấm Số lượng Tồn kho Âm (Negative Inventory Prohibition)",
          "Đặc thù bán lẻ dược phẩm không cho phép bán nợ hàng hóa vật lý. Số lượng xuất bán tuyệt đối không được vượt quá số lượng đang thực tế tồn kho.",
          "Khai báo CONSTRAINT CK_TonKho CHECK (SoLuongTon >= 0) trên cột SoLuongTon của bảng LO_THUOC. Bất kỳ lệnh UPDATE nào dẫn đến giá trị < 0 sẽ bị Database Engine chặn lập tức (Transaction aborted).",
          false),
        spacer(),

        constraintBlock(4,
          "Ràng buộc Tính hợp lý của Ngày tháng Lô thuốc (Date Validity Constraint)",
          "Hạn sử dụng của một lô thuốc hiển nhiên phải luôn lớn hơn ngày sản xuất. Sai sót nhập liệu (lộn năm) có thể khiến thuốc bị hệ thống hiểu nhầm là đã hết hạn ngay từ khi mới nhập, gây ách tắc luồng bán hàng.",
          "Ràng buộc CHECK đơn giản nhưng cực kỳ hiệu quả: CONSTRAINT CK_DateValidity CHECK (NgaySanXuat < HanSuDung) áp đặt trên bảng LO_THUOC.",
          true),
        spacer(),

        constraintBlock(5,
          "Cảnh báo và Phong tỏa Tự động Thuốc Cận Date / Quá Date (Auto-Lock Expired Batches)",
          "Thuốc đã quá hạn sử dụng bắt buộc phải bị thu hồi và tiêu hủy theo quy định kiểm soát đặc biệt, tuyệt đối không được lưu hành. Cơ sở dữ liệu tự động từ chối cung cấp mã lô này cho các giao dịch bán hàng.",
          "Tích hợp logic vào STORED PROCEDURE xuất bán hoặc BEFORE INSERT TRIGGER trên CHI_TIET_HOA_DON: nếu HanSuDung < GETDATE(), giao dịch bị hủy kèm mã lỗi \"ERR_EXPIRED_BATCH\". Một SQL Agent Job chạy ngầm mỗi đêm quét LO_THUOC để báo cáo danh sách hàng cận date (dưới 3 tháng) gửi dược sĩ quản lý.",
          false),
        spacer(), emptyLine(),

        // ── Nhóm 2 ───────────────────────────────────────────────
        groupHeader("Nhóm 2:", "Ràng buộc về Giao dịch Bán hàng (Sales Transaction Rules)", GREEN_LIGHT, GREEN_DARK),
        para("Nhóm ràng buộc thứ hai kiểm soát luồng di chuyển của dòng tiền và chứng từ. Quy trình giao dịch ngành dược liên quan trực tiếp đến sinh mạng con người và chịu giám sát trực tuyến của Cục Quản lý Dược, do đó các quy tắc này là bắt buộc để duy trì giấy phép hoạt động.",{indent:true}),
        spacer(),

        constraintBlock(6,
          "Ràng buộc Bắt buộc Kèm Đơn thuốc đối với Thuốc Kê Đơn (Rx Dispensing Compliance)",
          "Theo Quyết định 4041/QĐ-BYT, nhà thuốc chỉ được phép xuất hóa đơn bán thuốc kê đơn khi người mua cung cấp đơn thuốc hợp lệ từ bác sĩ, nhằm thắt chặt tình trạng lạm dụng kháng sinh và kháng thuốc trong cộng đồng.",
          "Triển khai AFTER INSERT TRIGGER trên CHI_TIET_HOA_DON. Trigger JOIN sang bảng THUOC qua LO_THUOC để kiểm tra cờ LoaiThuoc. Nếu tồn tại dòng có LoaiThuoc = 1 (Kê đơn) và MaDonThuoc trong HOA_DON IS NULL, trigger lập tức RAISERROR và ROLLBACK toàn bộ hóa đơn.",
          true),
        spacer(),

        constraintBlock(7,
          "Ràng buộc Chuẩn hóa Dữ liệu Liên thông Quốc gia (National Schema Conformity)",
          "Theo Quyết định số 540/QĐ-QLD, dữ liệu đẩy lên cổng thông tin quốc gia phải hoàn toàn chính xác về định dạng. Mã thuốc phải theo công thức: Số đăng ký thuốc được Cục Quản lý Dược cấp + Quy cách đóng gói nhỏ nhất.",
          "Áp dụng CHECK CONSTRAINT NOT NULL và quy tắc định dạng trên hai cột SoDangKy và QuyCach của bảng THUOC. Một Computed Column (MaThuocQuocGia AS SoDangKy + '-' + QuyCach) tự động sinh mã liên thông, đảm bảo không có ký tự bất hợp lệ lọt vào gói JSON/XML khi gọi API gửi lên máy chủ Viettel.",
          false),
        spacer(),

        constraintBlock(8,
          "Ràng buộc Đóng băng Hóa đơn và Chống Sửa đổi Ngầm (Immutable Financial Records)",
          "Một khi hóa đơn đã hoàn tất thanh toán và giao thuốc, dữ liệu chi tiết (số lượng, mặt hàng, đơn giá, mã bác sĩ) không được phép sửa đổi ngầm để đảm bảo tính minh bạch tài chính và toàn vẹn hồ sơ y tế liên thông.",
          "Cấp quyền GRANT/REVOKE để hạn chế quyền UPDATE trên bảng HOA_DON (khi TrangThaiLT = 1) và CHI_TIET_HOA_DON đối với toàn bộ người dùng thông thường. Mọi chỉnh sửa nghiệp vụ phải thực hiện qua quy trình Hủy hóa đơn (IsDeleted = 1) và lập hóa đơn bù trừ mới.",
          true),
        spacer(),

        constraintBlock(9,
          "Ràng buộc Tính Điểm và Giới hạn Quy đổi Điểm Khách hàng (Loyalty Point Limit)",
          "Khi khách hàng yêu cầu trừ điểm để giảm giá, số điểm quy đổi tuyệt đối không được vượt quá số điểm thực tế khách đang sở hữu, nhằm bảo đảm ngân sách chương trình tích điểm của nhà thuốc.",
          "Khai báo CHECK CONSTRAINT (DiemTichLuy >= 0) trên bảng KHACH_HANG. Nếu hóa đơn yêu cầu trừ 500 điểm nhưng tài khoản chỉ còn 300 điểm, lệnh UPDATE SET DiemTichLuy = DiemTichLuy - 500 sẽ vi phạm ràng buộc và bị từ chối ngay lập tức.",
          false),
        spacer(),

        constraintBlock(10,
          "Ràng buộc Toàn vẹn Tổng tiền Hóa đơn (Mathematical Header-Detail Match)",
          "Không thể tồn tại hóa đơn hợp lệ có TongTien = 100.000 nhưng tổng giá trị các dòng chi tiết ThanhTien chỉ bằng 90.000. Sự bất đồng bộ này có thể xảy ra trong môi trường xử lý đồng thời (Concurrency).",
          "Thiết kế AFTER INSERT, UPDATE, DELETE TRIGGER gắn trên CHI_TIET_HOA_DON. Mỗi khi có thay đổi ở chi tiết giỏ hàng, trigger tự động tính SUM(ThanhTien) và cập nhật ngược lên cột TongTien của bảng HOA_DON, đảm bảo luôn khớp toán học.",
          true),
        spacer(), emptyLine(),

        // ── Nhóm 3 ───────────────────────────────────────────────
        groupHeader("Nhóm 3:", "Ràng buộc về Nhân sự & Quản trị (HR & Management Rules)", ORANGE_LIGHT, ORANGE_DARK),
        para("Những ràng buộc quản trị này minh bạch hóa trách nhiệm cá nhân (Audit Trail) và bảo đảm nhà thuốc luôn trong trạng thái sẵn sàng cho các đợt thanh tra duy trì tiêu chuẩn GPP từ Sở Y tế.",{indent:true}),
        spacer(),

        constraintBlock(11,
          "Ràng buộc Kiểm soát Phân quyền Kê đơn theo Chứng chỉ Dược sĩ (Qualified Dispensing Control)",
          "Việc tư vấn và bán thuốc kê đơn phải do Dược sĩ đại học đảm nhận. Một dược sĩ trung cấp hoặc nhân viên thu ngân không được quyền dùng tài khoản của mình để phê duyệt hóa đơn thuốc kê đơn.",
          "Áp dụng kiểm tra khóa ngoại chéo (Cross-table Validation). Khi hóa đơn chứa thuốc kê đơn được tạo, hệ thống đọc MaNhanVien, truy vấn sang bảng NHAN_VIEN và kiểm tra ChucVu và ChungChi. Nếu ChungChi IS NULL hoặc chức vụ không đủ thẩm quyền, giao dịch bị từ chối bằng Authorization Error.",
          false),
        spacer(),

        constraintBlock(12,
          "Ràng buộc Tính Độc nhất của Chứng chỉ Hành nghề (License Uniqueness Identifier)",
          "Theo pháp luật y tế, một cá nhân chỉ được cấp một chứng chỉ hành nghề duy nhất và không được sử dụng song song cho nhiều cơ sở. Cho thuê bằng dược sĩ hoặc tái sử dụng chứng chỉ của người khác là hành vi gian lận nghiêm trọng.",
          "Áp dụng UNIQUE CONSTRAINT trên cột ChungChi của bảng NHAN_VIEN. Database tự động từ chối bất kỳ lệnh INSERT nào mang số chứng chỉ đã tồn tại ở bản ghi nhân sự khác.",
          true),
        spacer(),

        constraintBlock(13,
          "Ràng buộc Toàn vẹn Chuỗi cung ứng và Hồ sơ Nhà cung cấp (Supplier Validation)",
          "Quy trình GPP yêu cầu nhà thuốc chỉ được phép nhập hàng từ nhà sản xuất, phân phối, bán buôn hợp pháp, có hóa đơn chứng từ và Giấy chứng nhận đủ điều kiện kinh doanh dược.",
          "Khóa ngoại MaNCC trên bảng PHIEU_NHAP phải tồn tại trong NHA_CUNG_CAP (FOREIGN KEY, NOT NULL). Mở rộng ràng buộc yêu cầu thuộc tính GiayPhepKD của nhà cung cấp phải có giá trị (NOT NULL) tại thời điểm tạo phiếu nhập. Nếu đối tác chưa hoàn thiện hồ sơ, hệ thống khóa không cho nhập hàng.",
          false),
        spacer(),

        constraintBlock(14,
          "Ràng buộc Bảo tồn Dữ liệu Lịch sử Đơn thuốc Điện tử (Data Retention & No Cascade Delete)",
          "Khi bác sĩ nghỉ hưu hoặc phòng khám đóng cửa, hồ sơ có thể bị ẩn nhưng toàn bộ đơn thuốc đã kê trong quá khứ phải được bảo tồn vĩnh viễn trong CSDL để phục vụ tra cứu y tế, đối soát dịch tễ và thanh tra liên thông.",
          "Trong kiến trúc khóa ngoại, mối quan hệ từ DON_THUOC về BAC_SI tuyệt đối không được cài đặt ON DELETE CASCADE. Bắt buộc dùng ON DELETE RESTRICT (hoặc NO ACTION). Nếu quản trị viên cố xóa bác sĩ đang có lịch sử kê đơn, DBMS chặn đứng thao tác để bảo vệ dữ liệu y khoa lịch sử.",
          true),
        spacer(),

        constraintBlock(15,
          "Ràng buộc Bảo mật Mật khẩu và An toàn Thông tin (Password Hashing & Network Security)",
          "Do hệ thống kết nối mạng diện rộng qua API để truyền dữ liệu lên Cục Quản lý Dược và lưu trữ thông tin bệnh lý nhạy cảm của khách hàng, bắt buộc phải áp dụng tiêu chuẩn an toàn thông tin ở tầng cơ sở dữ liệu.",
          "Mật khẩu dược sĩ tuyệt đối không được lưu dạng Plain-text. Cột PasswordHash trong bảng NHAN_VIEN được gán VARCHAR(256). Trong Stored Procedure khởi tạo tài khoản, hàm băm mật mã học (SHA-256 kết hợp Salting) bắt buộc được gọi trước khi ghi xuống disk. Ngay cả DBA truy cập trực tiếp cũng không thể dịch ngược mật khẩu.",
          false),
        spacer(), emptyLine(),

        // Tổng kết
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing:{before:200,after:200},
          shading:{fill:BLUE_LIGHT,type:ShadingType.CLEAR},
          children:[
            new TextRun({text:"Tổng cộng: 15 ràng buộc nghiệp vụ  |  ", bold:true, size:24, font:"Times New Roman", color:BLUE_DARK}),
            new TextRun({text:"Nhóm 1: 5  ·  Nhóm 2: 5  ·  Nhóm 3: 5", size:22, font:"Times New Roman", color:BLUE_MID}),
          ]
        }),
        emptyLine(),
      ]
    }
  ]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("QuanLyNhaThuoc_v2.docx", buf);
  console.log("Done! File QuanLyNhaThuoc_v2.docx đã được tạo thành công trong thư mục của bạn.");
});