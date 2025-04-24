import os
from scripts.preprocess import preprocess_image, segment_answers
from scripts.hwr import recognize_handwriting
from scripts.scorer import evaluate_answer
from scripts.utils import ensure_dir_exists, get_file_name, list_sorted_images
from scripts.text_cleaning import preprocess_ocr_output

# -------- Configuration --------
raw_img_path = "data/raw/sample_sheet.jpeg"      # Path to a scanned answer sheet
processed_dir = "data/processed"                # Folder for segmented answer images
model_answer = "Newton's first law states that an object remains at rest or in uniform motion unless acted upon by an external force."

# -------- Setup --------
ensure_dir_exists(processed_dir)
base_name = get_file_name(raw_img_path)

# -------- Step 1: Preprocess and Segment Answers --------
print("🔄 Preprocessing and segmenting...")
img = preprocess_image(raw_img_path)
segment_answers(img, processed_dir, base_name)

# -------- Step 2: OCR and Evaluation --------
print("\n🧠 Evaluating segmented answers...\n")
for img_file in list_sorted_images(processed_dir, prefix=base_name):
    img_path = os.path.join(processed_dir, img_file)
    student_text = recognize_handwriting(img_path)
    student_text = preprocess_ocr_output(student_text)  # 🔥 Clean & correct text
    score = evaluate_answer(student_text, model_answer)

    print(f"[{img_file}] | Score: {score:.2f}")
    print(f"Student Text: {student_text}\n")
