import os
import csv

INPUT_DIR = 'input_texts'
OUTPUT_FILENAMES = 'game_filenames.tsv'
OUTPUT_TEXTS = 'game_texts.tsv'

os.makedirs(INPUT_DIR, exist_ok=True)

def import_texts_to_tsv():
    files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
    files.sort()  # Đảm bảo thứ tự nhất quán
    with open(OUTPUT_FILENAMES, 'w', encoding='utf-8', newline='') as fnfile, \
         open(OUTPUT_TEXTS, 'w', encoding='utf-8', newline='') as txtfile:
        fn_writer = csv.writer(fnfile, delimiter='\t')
        txt_writer = csv.writer(txtfile, delimiter='\t')
        fn_writer.writerow(['index', 'filename'])
        txt_writer.writerow(['index', 'text'])
        for idx, filename in enumerate(files, 1):
            with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8') as f:
                text = f.read().replace('\r\n', '\n').replace('\r', '\n')
                fn_writer.writerow([idx, filename])
                txt_writer.writerow([idx, text])
    print(f'Đã import {len(files)} file vào {OUTPUT_FILENAMES} và {OUTPUT_TEXTS}')

if __name__ == '__main__':
    import_texts_to_tsv()
