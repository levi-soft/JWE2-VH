# JWE2-VH
Jurassic World Evolution 2 Việt Hóa

## Sử dụng

1. Đặt các file text game vào thư mục `input_texts/`.
2. Chạy `import_texts.py` để tạo file `game_texts.tsv`.
3. Dịch file `game_texts.tsv` (giữ nguyên cấu trúc cột).
4. Đặt file TSV đã dịch vào thư mục dự án, chạy `export_texts.py` để tách lại các file text nhỏ vào thư mục `output_texts/`.

## Yêu cầu
- Python 3.7 trở lên

## Chạy lệnh
```cmd
py import_texts.py
py export_texts.py
```

## Lưu ý
- Nếu text game có ký tự đặc biệt (tab, xuống dòng, dấu \\...), ứng dụng vẫn giữ nguyên khi import/export.
- Nếu dịch file bằng Excel, nên lưu lại đúng định dạng TSV (UTF-8, tab-separated) để tránh lỗi ký tự.
- Không thay đổi cột 'filename' và số thứ tự trong các file TSV.
- Nếu cần phân biệt giữa xuống dòng thật và ký tự kỹ thuật \n trong game, hãy liên hệ để được hướng dẫn nâng cao.
