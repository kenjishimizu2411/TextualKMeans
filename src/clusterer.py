import os
import sys
from pathlib import Path # Melhor que 'os' para caminhos de arquivo
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
# from sklearn.utils.extmath import density # Não usada, foi removida

class TextClusterer:
    """
    Encapsula toda a lógica de carregamento, vetorização TF-IDF e 
    clusterização K-Means de documentos de texto.
    """
    
    def __init__(self, data_path: Path):
        # Garante que o caminho é um objeto Path
        self.data_path = data_path 
        self.documentos = []
        self.termos = None
        
        # 0. Preparar Stop Words
        # Checagem feita uma única vez na inicialização da classe
        try:
            stopwords.words('portuguese')
        except LookupError:
            print("Baixando pacote 'stopwords' da NLTK (download único)...")
            nltk.download('stopwords')
            
        self.lista_stopwords_pt = stopwords.words('portuguese')

    def load_documents(self):
        """1. Carrega todos os documentos de todas as subpastas."""
        
        if not self.data_path.exists():
            print(f"ERRO: Pasta '{self.data_path}' não encontrada.")
            sys.exit(1)

        print(f"Iniciando carga de documentos em '{self.data_path}'")
        
        # O método glob é muito mais limpo para iterar em arquivos
        # O padrão '**/*.txt' busca recursivamente todos os .txt
        for doc_path in self.data_path.glob('**/*.txt'):
            # Path.read_text tenta abrir o arquivo
            try:
                # Tenta ler com utf-8 (padrão)
                conteudo = doc_path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                # Tenta com latin-1
                conteudo = doc_path.read_text(encoding='latin-1')
            except Exception as e:
                # Captura outros erros de I/O
                print(f"AVISO: Não foi possível ler {doc_path}. Erro: {e}")
                continue # Pula para o próximo arquivo
                
            self.documentos.append(conteudo)

        print(f"Total de {len(self.documentos)} documentos carregados.")

        if not self.documentos:
            print("ERRO: Nenhum documento foi carregado. Verifique as subpastas.")
            sys.exit(1)
            
        return self.documentos

    def vectorize_data(self, max_df=0.6, min_df=2):
        """2. Transforma os documentos carregados em vetores TF-IDF."""
        
        print("Convertendo textos para vetores TF-IDF...")
        
        vectorizer = TfidfVectorizer(
            stop_words=self.lista_stopwords_pt, 
            max_df=max_df, 
            min_df=min_df
        )

        X = vectorizer.fit_transform(self.documentos)
        self.termos = vectorizer.get_feature_names_out()
        
        print(f"Matriz TF-IDF criada com {X.shape[1]} features.\n")
        return X

    def run_kmeans(self, X, k_teste: int, output_dir: Path):
        """3. Roda o algoritmo K-Means e salva os resultados."""
        
        print(f"=========================================")
        print(f"  EXECUTANDO TESTE COM K={k_teste}        ")
        print(f"=========================================")

        # K-means não pode ter mais clusters (k) do que documentos (n_samples)
        if X.shape[0] < k_teste:
            print(f"AVISO: Pulando k={k_teste} (muito alto).")
            return
        
        # Uso de kwargs (argumentos chave-valor) para configurar o modelo, mais limpo
        kmeans_params = {
            'n_clusters': k_teste,
            'max_iter': 300,
            'n_init': 10,
            'random_state': 42
        }
        
        kmeans = KMeans(**kmeans_params)
        kmeans.fit(X) 
        print("Clusterização concluída.")

        # --- Salvar os Resultados ---
        centroides = kmeans.cluster_centers_
        termos_ordenados = centroides.argsort()[:, ::-1]
        
        # Garante que a pasta 'results' exista
        output_dir.mkdir(exist_ok=True) 
        nome_arquivo = output_dir / f"saida_clusters_k{k_teste}.txt"
        
        print(f"Salvando resultados em '{nome_arquivo}'...")
        
        # O bloco de escrita agora usa Path.write_text, mais conciso
        conteudo_saida = [f"### RESULTADOS DO TESTE COM K={k_teste} ###\n\n"]
        
        for i in range(k_teste):
            conteudo_saida.append(f"--- Cluster {i} ---\n")
            conteudo_saida.append("Top 10 termos: ")
            
            termos_cluster = [
                self.termos[indice] 
                for indice in termos_ordenados[i, :10]
            ]
            
            conteudo_saida.append(" ".join(termos_cluster) + "\n\n")

        nome_arquivo.write_text("".join(conteudo_saida), encoding="utf-8")
        print(f"Resultados salvos em '{nome_arquivo}'\n")