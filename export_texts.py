import os
import csv

INPUT_FILENAMES = 'game_filenames.tsv'
INPUT_TEXTS = 'game_texts.tsv'
OUTPUT_DIR = 'output_texts'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def export_tsv_to_texts():
    filenames = {}
    texts = {}
    # Đọc file tên
    with open(INPUT_FILENAMES, 'r', encoding='utf-8') as fnfile:
        reader = csv.DictReader(fnfile, delimiter='\t')
        for row in reader:
            idx = row['index']
            filenames[idx] = row['filename']
    # Đọc file text
    with open(INPUT_TEXTS, 'r', encoding='utf-8') as txtfile:
        reader = csv.DictReader(txtfile, delimiter='\t')
        for row in reader:
            idx = row['index']
            texts[idx] = row['text']
    # Ghép và xuất file
    for idx in filenames:
        filename = filenames[idx]
        text = texts.get(idx, '')
        with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
            f.write(text)
    print(f'Đã export {len(filenames)} file text vào thư mục {OUTPUT_DIR}')

if __name__ == '__main__':
    export_tsv_to_texts()
