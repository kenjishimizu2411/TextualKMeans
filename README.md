# 📊 Clusterização de Documentos com K-Means e TF-IDF

> Projeto de Data Mining aplicando NLP e Machine Learning não-supervisionado para identificar padrões temáticos em notícias.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)

## 🧠 Sobre o Projeto

Este projeto explora a eficácia do algoritmo **K-Means** na identificação automática de temas em um corpus de notícias (Dataset C50), sem qualquer rotulagem prévia.

Para transformar texto em dados numéricos processáveis, utilizei a técnica **TF-IDF (Term Frequency-Inverse Document Frequency)**, que pondera a importância das palavras, penalizando termos genéricos (como artigos e preposições) e valorizando termos que carregam o significado do tópico.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Scikit-learn:** Implementação dos algoritmos de vetorização e clusterização.
* **NLTK (Natural Language Toolkit):** Tratamento de stopwords em Português/Inglês.
* **Pathlib:** Manipulação robusta de caminhos de sistema de arquivos.

---

## 🚀 Como Configurar e Executar

### 1. Clone o Repositório
```bash
git clone https://github.com/kenjishimizu2411/TextualKMeans.git
cd TextualKMeans
```

### 2. Ambiente Virtual
Recomendamos o uso de um ambiente virtual para isolar as dependências.
```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instalação
```bash
pip install -r requirements.txt
```

### 4. Setup dos Dados (⚠️ Importante)
Como boas práticas de versionamento, o dataset bruto não está incluído no repositório.
1. Baixe o **Dataset C50**.
2. Crie a pasta `data/raw/` na raiz do projeto.
3. Extraia a pasta `C50train` para dentro dela.
   * Caminho esperado: `TextualKMeans/data/raw/C50train/...`

### 5. Execução
```bash
python main.py
```
> Os resultados (arquivos .txt com os clusters) serão gerados na pasta `results/`.

---

## 📈 Análise de Resultados

Os experimentos compararam a performance do algoritmo dividindo os dados em **5** e **10** grupos. Utilizamos o **Coeficiente de Silhueta (Silhouette Score)** para medir a coesão dos clusters (quanto mais próximo de 1, melhor).

| Configuração (K) | Silhouette Score (S) | Observação Qualitativa |
| :---: | :---: | :--- |
| **K=5** | **~0.18** | Separação clara de macro-temas (Esporte, Política, Economia). |
| **K=10** | ~0.15 | Maior granularidade, mas com sobreposição de temas e menor coesão. |

### 💡 Conclusão Técnica
Embora ambos os scores sejam modestos (comum em dados textuais de alta dimensionalidade), a configuração **K=5 apresentou maior robustez ($0.18 > 0.15$)**.

A inspeção manual dos **Top 10 Termos** (Centróides) validou a decisão:
* **Cluster Política:** *'government', 'president', 'reform'*
* **Cluster Mercado:** *'oil', 'dollar', 'rate', 'market'*

Apesar de K=10 ter tecnicamente menor inércia (erro quadrático), ele gerou clusters fragmentados e difíceis de interpretar, confirmando que para este dataset, **5 clusters** representam melhor a distribuição real dos tópicos.