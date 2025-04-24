from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def evaluate_answer(student_answer, model_answer):
    embeddings = model.encode([student_answer, model_answer])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    return similarity
