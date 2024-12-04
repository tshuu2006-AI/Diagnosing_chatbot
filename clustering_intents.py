import json
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
from transformers import pipeline
from collections import Counter

# Tải dữ liệu chưa gán nhãn
def load_unlabeled_data(file_path):
    with open(file_path, "r") as f:
        sentences = [line.strip().replace("â€™","'") for line in f.readlines()]
    return sentences

# Phân cụm câu
def dbscan_clustering(sentences, eps=0.2,min_samples = 1):
  # Bước 1: Tạo vector ngữ nghĩa cho các câu
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Mô hình Sentence-BERT
    embeddings = model.encode(sentences)  # Chuyển các câu thành vector

    # Bước 2: Áp dụng thuật toán DBSCAN
    clustering_model = DBSCAN(eps=eps, min_samples=min_samples, metric='cosine')
    cluster_labels = clustering_model.fit_predict(embeddings)
    # Bước 3: Gom nhóm các câu theo cụm
    clusters = {}
    responses = {}
    for sentence, label in zip(sentences, cluster_labels):
        clusters.setdefault(f"Intent_{label}", []).append(sentence)
        responses[f"Response_{label}"] = "..."
    return clusters,responses


sentences = load_unlabeled_data("New_questions.txt")
clusters, responses = dbscan_clustering(sentences)


with open("Unlableled_intents.json","w") as file1:
    json.dump(clusters,file1,indent=1)


with open("responses.json", "w") as file2:
    json.dump(responses,file2,indent=1)

