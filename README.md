# 📊 Document Clustering with K-Means & TF-IDF

> An unsupervised Machine Learning project applying NLP techniques to identify thematic patterns in news articles.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)

## 🧠 About the Project

This project investigates the efficacy of the **K-Means algorithm** in automatically identifying topics within a news corpus (C50 Dataset) without any prior labeling (unsupervised learning).

To transform unstructured text into processable numerical data, I implemented **TF-IDF (Term Frequency-Inverse Document Frequency)**. This technique weighs the importance of words, penalizing generic terms (like articles and prepositions) while boosting terms that carry significant semantic value for the topic.

## 🛠️ Tech Stack

* **Python 3.x**
* **Scikit-learn:** Core implementation for vectorization (TF-IDF) and clustering algorithms.
* **NLTK (Natural Language Toolkit):** Used for stopword removal and text preprocessing.
* **Pathlib:** Robust file system path manipulation (OS-agnostic).

---

## 🚀 Setup & Execution

### 1. Clone the Repository
```bash
git clone [https://github.com/kenjishimizu2411/TextualKMeans.git](https://github.com/kenjishimizu2411/TextualKMeans.git)
cd TextualKMeans
```

### 2. Virtual Environment
It is highly recommended to use a virtual environment to isolate dependencies.
```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Installation
```bash
pip install -r requirements.txt
```

### 4. Data Setup (⚠️ Important)
Following data versioning best practices, the raw dataset is not included in the repository.
1. Download the **C50 Dataset**.
2. Create a folder named `data/raw/` in the project root.
3. Extract the `C50train` folder inside it.
   * Expected path: `TextualKMeans/data/raw/C50train/...`

### 5. Running the Project
```bash
python main.py
```
> The results (cluster output files) will be generated in the `results/` directory.

---

## 📈 Results Analysis

The experiments compared the algorithm's performance by splitting the data into **5** and **10** groups (K). We used the **Silhouette Score** to measure cluster cohesion (values closer to 1 indicate better separation).

| Configuration (K) | Silhouette Score (S) | Qualitative Observation |
| :---: | :---: | :--- |
| **K=5** | **~0.18** | Clear separation of macro-topics (Sports, Politics, Economy). |
| **K=10** | ~0.15 | Higher granularity, but resulted in topic overlap and lower cohesion. |

### 💡 Technical Conclusion
Although both scores are modest—which is typical for **high-dimensional text data**—the **K=5 configuration proved more robust ($0.18 > 0.15$)**.

A manual inspection of the **Top 10 Terms** (Centroids) validated this decision:
* **Politics Cluster:** *'government', 'president', 'reform'*
* **Market Cluster:** *'oil', 'dollar', 'rate', 'market'*

While K=10 technically yielded lower **inertia** (sum of squared errors), it generated fragmented clusters that were harder to interpret. This confirms that for this specific dataset, **5 clusters** better represent the natural distribution of the topics.

---

<p align="center">
Developed by <strong>Kenji Shimizu</strong>
</p>
