# 📊 Agrupamento de Documentos com K-Means & TF-IDF

> Projeto de Machine Learning não supervisionado aplicando técnicas de NLP para identificar padrões temáticos em notícias.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)

## 🧠 Sobre o Projeto

Este projeto investiga a eficácia do algoritmo **K-Means** na identificação automática de tópicos dentro de um corpus de notícias (Dataset C50) sem qualquer rotulagem prévia (aprendizado não supervisionado).

Para transformar texto não estruturado em dados numéricos processáveis, implementei o **TF-IDF (Term Frequency-Inverse Document Frequency)**. Essa técnica pondera a importância das palavras, penalizando termos genéricos (como artigos e preposições) enquanto impulsiona termos que carregam valor semântico significativo para o tópico.

## 🛠️ Tech Stack

* **Python 3.x**
* **Scikit-learn:** Implementação central para vetorização (TF-IDF) e algoritmos de clusterização.
* **NLTK (Natural Language Toolkit):** Utilizado para remoção de stopwords e pré-processamento de texto.
* **Pathlib:** Manipulação robusta de caminhos do sistema de arquivos (agnóstico ao S.O.).

---

## 🚀 Instalação & Execução

### 1. Clone o Repositório
```bash
git clone [https://github.com/kenjishimizu2411/TextualKMeans.git](https://github.com/kenjishimizu2411/TextualKMeans.git)
cd TextualKMeans
```

### 2. Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências.
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

### 4. Configuração dos Dados (⚠️ Importante)
Seguindo as boas práticas de versionamento de dados, o dataset bruto não está incluído no repositório.
1. Baixe o **Dataset C50**.
2. Crie uma pasta chamada `data/raw/` na raiz do projeto.
3. Extraia a pasta `C50train` dentro dela.
   * Caminho esperado: `TextualKMeans/data/raw/C50train/...`

### 5. Executando o Projeto
```bash
python main.py
```
> Os resultados (arquivos de saída dos clusters) serão gerados no diretório `results/`.

---

## 📈 Análise dos Resultados

Os experimentos compararam a performance do algoritmo dividindo os dados em **5** e **10** grupos (K). Utilizamos o **Silhouette Score** para medir a coesão dos clusters (valores mais próximos de 1 indicam melhor separação).

| Configuração (K) | Silhouette Score (S) | Observação Qualitativa |
| :---: | :---: | :--- |
| **K=5** | **~0.18** | Separação clara de macro-tópicos (Esportes, Política, Economia). |
| **K=10** | ~0.15 | Maior granularidade, mas resultou em sobreposição de tópicos e menor coesão. |

### 💡 Conclusão Técnica
Embora ambas as pontuações sejam modestas — o que é típico para **dados textuais de alta dimensão** — a configuração **K=5 provou-se mais robusta ($0.18 > 0.15$)**.

Uma inspeção manual dos **Top 10 Termos** (Centroides) validou essa decisão:
* **Cluster de Política:** *'government', 'president', 'reform'*
* **Cluster de Mercado:** *'oil', 'dollar', 'rate', 'market'*

Enquanto K=10 tecnicamente gerou uma **inércia** menor (soma dos erros quadrados), ele criou clusters fragmentados e mais difíceis de interpretar. Isso confirma que, para este dataset específico, **5 clusters** representam melhor a distribuição natural dos tópicos.

---

<p align="center">
Desenvolvido por <strong>Kenji Shimizu</strong>
</p>
