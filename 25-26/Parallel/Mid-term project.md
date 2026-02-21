
---

# 🧠 ANN Retrieval - Roadmap Progetto

**Corso**: Parallel Programming for Machine Learning  
**Progetto**: Approssimato Nearest Neighbor (ANN) Retrieval  
**Tecnologie**: C/C++, OpenMP, SIMD (AVX/SSE), LSH (opzionale)  
**Repository**: [Inserisci URL GitHub/GitLab]

---
## 📊 Indice

1. [Panoramica](#panoramica)
2. [Fase 1: Fondamenti e Progettazione](#fase-1-fondamenti-e-progettazione)
3. [Fase 2: Implementazione Sequenziale](#fase-2-implementazione-sequenziale)
4. [Fase 3: Parallelizzazione Base (OpenMP)](#fase-3-parallelizzazione-base-openmp)
5. [Fase 4: Ottimizzazione Avanzata & LSH](#fase-4-ottimizzazione-avanzata--lsh)
6. [Fase 5: Sperimentazione e Report](#fase-5-sperimentazione-e-report)
7. [Fase 6: Presentazione](#fase-6-presentazione)
8. [Checklist Finale](#checklist-finale)
9. [Risorse Utili](#risorse-utili)

---
## 🎯 Panoramica

**Problema**: Dato un insieme di vettori in spazio ad alta dimensionalità (≥128) e una query, trovare i **k vicini più prossimi** secondo una metrica di distanza.

**Obiettivi**:
- Implementazione sequenziale (baseline)
- Parallelizzazione con OpenMP (query-level, calcolo distanze)
- Ottimizzazione SIMD (vettorizzazione)
- [Opzionale] Implementazione LSH per ricerca approssimata
- Analisi performance: speedup, efficienza, scalabilità

**Requisiti tecnici** (dal PDF):
- Linguaggio: C/C++
- OpenMP + tecniche di vettorizzazione
- Test con k = 1, 10, 100
- Dataset: vettori ≥128 dimensioni
- Metriche: Euclidea, Coseno, Manhattan

[↑ Torna all'indice](#-indice)

---

## 📁 Struttura Repository

```
ann-retrieval/
├── README.md
├── Makefile
├── CMakeLists.txt (opzionale)
├── data/
│   ├── README.md         # Fonti dataset e preprocessing
│   └── sift/             # Dataset SIFT (scaricare localmente)
├── src/
│   ├── main.cpp
│   ├── ann_sequential.cpp/.h
│   ├── ann_parallel.cpp/.h
│   ├── ann_simd.cpp/.h   # Versione vettorizzata
│   ├── lsh.cpp/.h        # Opzionale
│   ├── distances.cpp/.h  # Metriche di distanza
│   └── io/
│       ├── fvecs_reader.cpp/.h
│       └── dataset_loader.cpp/.h
├── benchmarks/
│   ├── scripts/          # Script per test automatizzati
│   ├── results/          # CSV con tempi di esecuzione
│   └── plots/            # Grafici generati
├── report/
│   ├── figures/          # Immagini per report
│   └── report.md/pdf
└── presentation/
    └── slides.pptx/pdf
```

[↑ Torna all'indice](#-indice)

---

## 🗓️ Fase 1: Fondamenti e Progettazione  
**Settimana 1** · Obiettivo: Capire l'algoritmo e progettare l'architettura

### 📚 Studio
- [x] Leggi [k-NN tutorial (scikit-learn)](https://scikit-learn.org/stable/modules/neighbors.html)
- [ ] Approfondisci:
  - [Distanza Euclidea](https://en.wikipedia.org/wiki/Euclidean_distance)
  - [Similarità coseno](https://en.wikipedia.org/wiki/Cosine_similarity)
  - [Distanza Manhattan](https://en.wikipedia.org/wiki/Taxicab_geometry)
- [ ] Opzionale - Studia [Locality-Sensitive Hashing (LSH)](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)

### 💾 Dataset
- [x] Scarica dataset di test da [http://corpus-texmex.irisa.fr/](http://corpus-texmex.irisa.fr/)
  - Consiglio: **SIFT** (`sift_base.fvecs`, `sift_query.fvecs`)
- [x] Trova/scrivi un reader per file `.fvecs` (formato binario)
- [ ] Prepara piccolo dataset sintetico per testing (2D/3D, 100 punti)

### 🏗️ Progettazione
- [ ] Definisci strutture dati:
  - `struct Vector { int dim; float* data; }` (AoS)
  - `struct Dataset { int n_vectors; int dim; float* data_flat; }` (SoA)
- [ ] Progetta interfaccia funzioni:
  - `float euclidean(const float* a, const float* b, int dim)`
  - `vector<int> knn_sequential(const Dataset& db, const Vector& query, int k)`
- [ ] Crea repository Git
- [ ] Scrivi README.md con obiettivi progetto

### ✅ Deliverable Fase 1
- Repository inizializzata
- Dataset identificati e scaricati
- Schema architetturale

[↑ Torna all'indice](#-indice)

---

## 🐢 Fase 2: Implementazione Sequenziale  
**Settimana 2** · Obiettivo: Baseline corretta e funzionante

### 🔧 Implementazione
- [ ] Implementa lettore `.fvecs` (esistono snippet online)
- [ ] Implementa funzioni di distanza:
  - [ ] Euclidea (con e senza radice quadrata)
  - [ ] Coseno
  - [ ] Manhattan
- [ ] Implementa **brute-force kNN**:
  - Per ogni query → calcola distanza con **tutti** i punti del DB
  - Seleziona k minimi (con heap o array ordinato)
- [ ] Ottimizzazione base: evita sqrt per confronto distanze

### ✅ Testing & Validazione
- [ ] Crea test su **dataset piccolo 2D** (es. 10 punti, 2 dimensioni)
- [ ] Calcola manualmente i kNN e verifica output
- [ ] Test su SIFT con N=1000 per verificare tempi

### 📊 Profilazione Base
- [ ] Misura tempo sequenziale su varie dimensioni:
  - N = 1.000, 10.000, 100.000
  - D = 128 (SIFT)
- [ ] Documenta: tempo medio su 5 esecuzioni

### ✅ Deliverable Fase 2
- Codice sequenziale completo e testato
- Primi dati di performance (tempi sequenziali)
- Commit: "Sequential brute-force kNN implemented"

[↑ Torna all'indice](#-indice)

---

## ⚡ Fase 3: Parallelizzazione Base (OpenMP)  
**Settimana 3** · Obiettivo: Primo speedup significativo

### 🧵 Strategia 1: Parallelismo sulle query
- [ ] Individua loop sulle query (`for each query { ... }`)
- [ ] Applica `#pragma omp parallel for`
- [ ] Gestisci variabili `private`/`shared`
- [ ] Test su 2, 4, 8, 16 thread

### 📈 Sperimentazione Scheduling
- [ ] Testa `schedule(static)`
- [ ] Testa `schedule(dynamic, chunk)`
- [ ] Testa `schedule(guided)`
- [ ] Trova chunk size ottimale

### 🔍 Validazione
- [ ] **Sempre**: Confronta risultati con versione sequenziale
- [ ] Verifica che gli stessi vicini siano restituiti

### 📊 Benchmark
- [ ] Misura speedup su dataset SIFT:
  - Query singola vs batch di query
  - N = 10k, 50k, 100k
- [ ] Crea primo grafico: speedup vs thread count

### ✅ Deliverable Fase 3
- Versione parallela funzionante
- Dati di speedup baseline
- Commit: "OpenMP parallelization on queries"

[↑ Torna all'indice](#-indice)

---

## 🚀 Fase 4: Ottimizzazione Avanzata & LSH  
**Settimana 4** · Obiettivo: Massimizzare performance

### 📐 Ottimizzazione 1: Vettorizzazione (SIMD)
**Obiettivo**: Velocizzare il calcolo della distanza Euclidea

- [ ] Studia le **intrinsics AVX/SSE**:
  - `_mm256_load_ps`, `_mm256_sub_ps`, `_mm256_mul_ps`, `_mm256_add_ps`, `_mm256_hadd_ps`
- [ ] Implementa `euclidean_simd(const float* a, const float* b, int dim)`
- [ ] Allinea memoria a 32/64 byte (`aligned_alloc`)
- [ ] Confronta performance vs versione scalare

**Risorse**: 
- [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/)
- Esempi di dot product vettorizzato

### 🧠 Ottimizzazione 2: SoA vs AoS
- [ ] Riorganizza dataset in **Struct of Arrays (SoA)**
  - Invece di `vector<Vector>` → `float* all_data` (dim × n_vectors)
- [ ] Misura impatto su cache e SIMD
- [ ] Documenta differenza di performance

### 🎯 Ottimizzazione 3: Blocchi/Tiling (Opzionale)
- [ ] Partiziona dataset in blocchi per migliorare località cache
- [ ] Processa blocchi in parallelo

### 🧩 [Opzionale] Implementazione LSH
**Obiettivo**: Ricerca approssimata molto più veloce (trade-off recall)

- [ ] Implementa **proiezioni casuali** per hashing
- [ ] Costruisci LSH index (più tabelle hash)
- [ ] Funzione di query: cerca nei bucket corrispondenti
- [ ] Misura **recall@k** vs brute-force
- [ ] Confronta speedup con perdita di precisione

**Approccio minimo**: 
- Usa proiezioni casuali per ridurre dimensionalità
- 2-3 tabelle hash
- Ricerca solo nei bucket della query

### ✅ Deliverable Fase 4
- Distanza vettorizzata (SIMD) funzionante
- Confronto AoS vs SoA
- [Opzionale] Prototipo LSH
- Commit: "SIMD optimizations" / "LSH experimental"

[↑ Torna all'indice](#-indice)

---

## 📝 Fase 5: Sperimentazione e Report  
**Settimana 5** · Obiettivo: Dati solidi e report completo

### 🧪 Piano Sperimentale (dal PDF)

| Parametro | Valori da testare |
|-----------|-------------------|
| Numero thread | 1, 2, 4, 8, 16, 32 |
| Dimensione dataset | 10k, 50k, 100k, 500k |
| k | 1, 10, 100 |
| Scheduling | static, dynamic, guided |
| Metriche | Euclidea, Coseno, Manhattan |
| Ottimizzazioni | Baseline, SIMD, SoA |

### 📊 Raccolta Dati
- [ ] Automatizza benchmark con script Python/bash
- [ ] Salva risultati in CSV con formato:
  ```
  version,dataset_size,k,threads,schedule,chunk,time_ms,speedup
  ```
- [ ] Esegui **minimo 5 run** per configurazione → media, std dev
- [ ] Escludi I/O dalla misurazione

### 📈 Analisi
- [ ] **Speedup curve**: speedup vs thread count (per vari N)
- [ ] **Efficienza**: speedup / thread count
- [ ] **Scalabilità forte**: dimensione fissa, thread variabili
- [ ] **Confronto scheduling**: static vs dynamic vs guided
- [ ] **Bottleneck analysis**: memory-bound? CPU-bound?
- [ ] **SIMD speedup**: scalare vs vettorizzato
- [ ] **Opzionale**: recall vs speedup per LSH

### 📄 Stesura Report
Segui **pagine 42-43** del PDF. Struttura:

1. **Abstract** (1/2 pagina)
2. **Introduzione** (1 pagina)
3. **Descrizione Algoritmo** (2 pagine)
4. **Implementazione Parallela** (3-4 pagine)
5. **Setup Sperimentale** (1-2 pagine)
6. **Risultati e Analisi** (4-5 pagine) ← **Cuore del report**
7. **Discussione** (1-2 pagine)
8. **Conclusioni** (1 pagina)
9. **Riferimenti**

**Regole d'oro**:
- Ogni grafico: titolo, etichette assi, legenda, caption
- Confronta sempre con aspettative teoriche (Amdahl/Gustafson)
- Spiega i bottleneck osservati

### ✅ Deliverable Fase 5
- Report tecnico completo (PDF)
- Dati grezzi in repository
- Commit: "Final report v1.0"

[↑ Torna all'indice](#-indice)

---

## 🎤 Fase 6: Presentazione  
**Settimana 6** · Obiettivo: Comunicare efficacemente

### 📽️ Struttura Slide (10-12 minuti)

1. **Problema** (1-2 slide)
   - Cos'è ANN k-NN? A cosa serve? (ML, retrieval, recommendation)
   - Perché è computazionalmente costoso? (maledizione dimensionalità, grandi volumi)

2. **Approccio** (2-3 slide)
   - Algoritmo sequenziale brute-force
   - Strategie di parallelizzazione
   - Ottimizzazioni (SIMD, SoA, LSH)

3. **Risultati** (3-4 slide) ← **Focus**
   - Speedup curve (thread vs speedup)
   - Confronto scheduling
   - Impatto SIMD/SoA
   - [Opzionale] Trade-off LSH

4. **Conclusioni** (1-2 slide)
   - Miglior configurazione trovata
   - Limiti e lavoro futuro
   - Lezioni apprese

### ⚠️ Consigli
- **Non mettere codice** nelle slide (a meno di snippet brevissimi)
- **Grafici grandi e leggibili**
- Prepara slide extra per le domande
- Esercitati con timer

### ✅ Deliverable Fase 6
- Presentazione PPT/PDF
- (Opzionale) Screenshot/demo se applicabile

[↑ Torna all'indice](#-indice)

---

## ✅ Checklist Finale Consegna

### 📦 Repository
- [ ] README con istruzioni compilazione/esecuzione
- [ ] Makefile o CMakeLists.txt
- [ ] Commenti significativi nel codice
- [ ] Commit frequenti e descrittivi
- [ ] Tag milestone (es. `v1.0-sequential`, `v1.1-openmp`)

### 📄 Report
- [ ] Copertina con nomi e matricole
- [ ] Abstract
- [ ] Introduzione
- [ ] Descrizione algoritmo
- [ ] Dettagli implementazione parallela
- [ ] Setup sperimentale completo
- [ ] Almeno 4-5 grafici di performance
- [ ] Discussione dei risultati
- [ ] Conclusioni
- [ ] Bibliografia

### 🎥 Presentazione
- [ ] Durata 10-12 minuti
- [ ] Struttura chiara
- [ ] Grafici leggibili
- [ ] Pronti per domande

[↑ Torna all'indice](#-indice)

---

## 📚 Risorse Utili

### Documentazione Ufficiale
- [OpenMP Specifications](https://www.openmp.org/specifications/)
- [OpenMP Tutorial (LLNL)](https://computing.llnl.gov/tutorials/openMP/)
- [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/)

### Dataset
- [TexMex Corpus](http://corpus-texmex.irisa.fr/) - **Dataset standard per ANN**
- [SIFT1M / GIST1M](http://corpus-texmex.irisa.fr/)

### Letture Consigliate
- [k-NN tutorial (scikit-learn)](https://scikit-learn.org/stable/modules/neighbors.html)
- [Locality-Sensitive Hashing (Wikipedia)](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
- [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law)
- [Gustafson's Law](https://en.wikipedia.org/wiki/Gustafson%27s_law)

### Codice di Riferimento
- [fvecs reading utility](https://github.com/arbabenko/spann/blob/master/utils/fvecs.h) (esempio)
- [SIMD Euclidean distance](https://stackoverflow.com/questions/59444896/avx2-computing-vector-dot-product)

[↑ Torna all'indice](#-indice)

---
