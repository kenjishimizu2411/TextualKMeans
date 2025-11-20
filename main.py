# main.py

import sys
from pathlib import Path
# Importa a classe do novo módulo que criamos
from src.clusterer import TextClusterer 

# --- Configs do Experimento (Agora centralizadas no início) ---
VALORES_K = [5, 10] 
# Uso de Path para caminhos relativos ao projeto, removendo caminhos absolutos (C50/C50train)
PATH_DADOS = Path(sys.path[0]) / 'data' / 'raw' / 'C50train' 
PATH_SAIDA = Path(sys.path[0]) / 'results' 


if __name__ == "__main__":
    print("-" * 30)
    print("Iniciando Experimento de Clusterização de Texto")
    
    # Inicializa o objeto com o caminho dos dados (também prepara stop words)
    clusterer = TextClusterer(data_path=PATH_DADOS)
    
    try:
        # 1. Carrega os documentos
        clusterer.load_documents()
        
        # 2. Vetorização (TF-IDF)
        X_tfidf = clusterer.vectorize_data()
        
        # 3. Rodar os Experimentos (K=5 e K=10)
        for k_teste in VALORES_K:
            clusterer.run_kmeans(X_tfidf, k_teste=k_teste, output_dir=PATH_SAIDA)

    except Exception as e:
        print(f"\nERRO FATAL NO EXPERIMENTO: {e}")
        sys.exit(1)

    print("-" * 30)
    print("Experimento finalizado com sucesso.")