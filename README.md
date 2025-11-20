# 📊 Projeto de Clusterização de Documentos com K-Means e TF-IDF

Este projeto de Datamining visa aplicar técnicas de Processamento de Linguagem Natural (NLP) e aprendizado não supervisionado para **agrupar artigos de notícias** com base em seu conteúdo. O objetivo é testar a eficácia do **algoritmo K-Means** na identificação de temas centrais (clusters) usando o peso das palavras dado pelo **TF-IDF**.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Scikit-learn:** Para as implementações de TfidfVectorizer e KMeans.
* **NLTK (Natural Language Toolkit):** Para manipulação de *stopwords* em Português.
* **Pathlib:** Para manipulação segura de caminhos de arquivos.

## 🚀 Como Configurar e Executar

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd datamining_kenji
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate  # No Windows (PowerShell)
    # source .venv/bin/activate  # No Linux/Mac
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Estrutura de Dados:**
    * Certifique-se de que a pasta de dados original (`C50train`) esteja posicionada em `data/raw/`.

5.  **Execução do Experimento:**
    ```bash
    python main.py
    ```
    Os resultados (lista dos top termos por cluster) serão salvos na pasta `results/`.

    ## 📈 Resultados Chave

Os testes foram executados com $K=5$ e $K=10$.

* **$K=5$**: Os clusters formados tendem a ser mais genéricos, separando claramente notícias de (1) Esportes, (2) Política e (3) Economia.
* **$K=10$**: Observou-se uma granularidade maior, com clusters especializados, como "Política Externa" e "Resultados de Futebol".

O **Coeficiente de Silhueta Médio** foi utilizado para avaliar a consistência da clusterização, uma vez que não tínhamos rótulos verdadeiros (ground truth).

* **K=5:** $S_{score} \approx 0.18$
* **K=10:** $S_{score} \approx 0.15$

Embora ambos os valores sejam modestos (o que é comum em dados de texto complexos), a configuração com **$K=5$ apresentou uma separação ligeiramente mais clara e robusta** ($0.18 > 0.15$), indicando que os 5 temas centrais foram mais distintivos que os 10.

## Análise Qualitativa dos Termos (Interpretabilidade)

A inspeção manual dos **Top 10 Termos** em cada cluster confirmou a coesão temática:

* **Cluster 1 (K=5):** Termos como *'governo', 'presidente', 'reforma'* (claramente **Política**).
* **Cluster 4 (K=5):** Termos como *'petróleo', 'dólar', 'juros'* (claramente **Economia/Mercado**).

Apesar de $K=10$ ter uma Inércia menor, ele resultou em alguns clusters menos interpretáveis, reforçando a decisão de que **$K=5$ é o melhor ponto de parada** para uma análise coerente e útil.
