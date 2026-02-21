# Intro

## 1_intro_parallelism_concurrency

**1. Parallelismo vs. Concorrenza**
- **Concorrenza**: capacità di un sistema di gestire più azioni *in progress* (anche se non eseguite simultaneamente).
- **Parallelismo**: capacità di eseguire più azioni *contemporaneamente* (richiede più core/CPU).
- **Relazione**: il parallelismo è un sottoinsieme della concorrenza.  
  - Concorrenza → struttura del programma.  
  - Parallelismo → esecuzione effettiva in parallelo.

---
**2. Algoritmi Sequenziali vs. Paralleli**
- **Sequenziale**: esegue operazioni una dopo l’altra.
- **Parallelo**: esegue più operazioni contemporaneamente, sfruttando più core o unità funzionali.
- **Concorrente**: può essere eseguito sia in modo seriale che parallelo, ma è strutturato per eseguire passi indipendenti.

---
**3. Motivazioni per il Parallelismo**
- **Fine della “free lunch”** dell’aumento di clock delle CPU.
- Aggiungere core è più efficiente che aumentare la frequenza (problemi di calore, consumo energetico).
- Esempio: un CPU a 16 core con hyperthreading e vettori a 256 bit può offrire fino a 128 operazioni parallele.
- **Risparmio energetico**: GPU, nonostante l’alto consumo, grazie al parallelismo massiccio possono ridurre il consumo totale rispetto a CPU.

---
 **4. Tipi di Parallelismo**
1. **Bit-Level Parallelism**: operazioni su parole più grandi (es. 32 bit vs 8 bit).
2. **Instruction-Level Parallelism (ILP)**: pipeline, esecuzione out-of-order, esecuzione speculativa.
3. **Data Parallelism (SIMD)**: stessa operazione su molti dati (es. GPU).
4. **Task-Level Parallelism**: suddivisione per compiti (memoria condivisa o distribuita).
5. **Systolic Array**: architettura per accelerare operazioni come le moltiplicazioni matriciali (es. Google TPU).

---
**5. Modelli di Architettura**
- **RAM** (Random Access Machine): modello sequenziale.
- **PRAM** (Parallel RAM): modello parallelo astratto, ma poco realistico per la memoria condivisa.
- **CTA** (Candidate Type Architecture): distingue accessi locali (veloci) e non-locali (lenti, latenza λ).

---
**6. Metriche di Performance**
- **Service time**, **bandwidth**, **completion time**, **latency**.
- **Speedup**: $S_P = t_s / t_p$
  - Lineare: $S_P = P$
  - Superlineare: $S_P > P$ (possibile per effetti di cache).
- **Efficienza**: $E_P = S_P / P$
- **Legge di Amdahl**: limite di speedup dato dalla frazione sequenziale $f$.  
$$S_P \leq \frac{1}{f}$$
- **Legge di Gustafson**: se si aumenta la dimensione del problema con i processori, lo speedup può essere lineare anche con frazioni sequenziali.

---
**7. Scalabilità**
- **Strong scaling**: tempo di esecuzione per dimensione fissa del problema al variare dei processori.
- **Weak scaling**: dimensione del problema cresce con i processori, tempo fisso.
- La **scalabilità di memoria** è critica: se i dati non stanno nella memoria locale, il problema non è eseguibile.

---
**8. Sorgenti di Perdita di Performance**
- Overhead di comunicazione e sincronizzazione.
- **Dipendenze dei dati** (flow, anti, output, input).
- Contenzione per risorse condivise.
- Bilanciamento del carico (load imbalance).
- **Scarsa località (temporale/spaziale).**

---
 **9. Progettazione di Programmi Paralleli**
1. **Decomposizione**: identificare compiti indipendenti.
2. **Assegnazione**: distribuire compiti ai worker.
3. **Orchestrazione**: gestire comunicazione, sincronizzazione, dipendenze.
4. **Mapping**: assegnare worker all’hardware (OS, framework, compiler).

---
 **10. Esempio Pratico di Parallelizzazione**
- Elaborazione di un’immagine:  
  - Step 1: raddoppio luminosità pixel (parallelo).  
  - Step 2: calcolo media pixel (parzialmente parallelo con riduzione).  
- Lo speedup dipende dal bilanciamento e dalla riduzione dell’overhead.

---
**11. Considerazioni Finali**
- Non tutti i problemi sono parallelizzabili.
- Programmi paralleli mal progettati possono essere più lenti di quelli sequenziali.
- Strumenti di profilazione e analisi delle dipendenze sono essenziali.
- Focus su **hotspot** e **bottleneck** del programma.

---

## 2_parallelization

**1. Scomposizione del Lavoro**
- **Task decomposition (o decomposizione funzionale)**: si identifica l’insieme di compiti indipendenti che possono essere eseguiti in parallelo.  
  - Scheduling statico: i compiti sono assegnati all’inizio.  
  - Scheduling dinamico: i compiti vengono assegnati durante l’esecuzione per bilanciare il carico.  
- **Data decomposition**: si divide il dato in “chunk” indipendenti, assegnando ciascun chunk a un task parallelo.  
  - Problemi chiave: forma dei chunk, accesso ai dati, assegnazione ai thread.

---
**2. Criteri di Decomposizione**
- Deve esserci **almeno un task per thread** per evitare idle.  
- **Granularità**: ogni task deve avere lavoro sufficiente a giustificare l’overhead di gestione.  
- **Flessibilità**: numero e dimensione dei task devono adattarsi all’architettura.  
- **Semplicità**: codice deve rimanere leggibile e debuggabile.

---
**3. Distribuzione dei Dati per Array**
- **1D**:  
  - Blockwise: blocchi contigui di elementi.  
  - Cyclic: elementi assegnati in round-robin.  
  - Block-cyclic: combinazione dei due.  
- **2D**:  
  - Distribuzioni per righe/colonne o checkerboard (griglia di processori).  

---
 **4. Layout di Dati in Memoria**
- **AoS (Array of Structures)**: campi di una struttura sono contigui.  
  - Vantaggio: buona località se si accede a tutti i campi insieme.  
  - Svantaggio: allineamento cache e vettorizzazione difficoltosa.  
- **SoA (Structure of Arrays)**: ogni campo è in un array separato.  
  - Vantaggio: allineamento cache, facile vettorizzazione (SIMD).  
  - Svantaggio: località scarsa se si accede a più campi insieme.  
- **AoS0A (Array of Structures of Arrays)**: ibrido che “tile” i dati per bilanciare località e vettorizzazione.

---
 **5. Proprietà di Sicurezza e Liveness**
- **Safety**: “niente di male accade mai” (es. mutua esclusione).  
- **Liveness**: “qualcosa di buono accade prima o poi” (es. assenza di deadlock).  
- Altre proprietà: assenza di starvation, fault-tolerance.

---
 **6. Modelli di Programmazione Parallela**
- **Fork-Join**: un thread principale crea (fork) thread figli e attende il loro completamento (join).  
- **SPMD (Single Program, Multiple Data)**: stesso codice, dati diversi per ogni processore.  
- **Master-Worker**: un master assegna task dinamici a worker (load balancing automatico).  
- **Pipeline**: dati fluiscono attraverso stadi sequenziali di elaborazione.  
- **Producer-Consumer**: produttori generano dati, consumatori li elaborano (buffer condiviso).  
- **Task Pool**: coda di task da cui i thread pescano lavoro.

---
 **7. Pattern di Calcolo Parallelo**
- **Map**: applica una funzione a ogni elemento di una collezione (indipendente).  
- **Reduce**: combina elementi con un’operazione associativa (es. somma).  
- **Scan (prefix sum)**: calcola riduzioni parziali.  
- **Stencil**: ogni output dipende da un intorno di input (es. filtri di immagini).  
- **Recurrence**: dipendenze tra iterazioni (ipertesti di Lamport per parallelizzare).

---
**8. Scambio di Informazioni e Comunicazione**
- **Memoria condivisa**:  
  - Accesso a variabili globali, rischio di race condition.  
  - Necessità di lock e sezioni critiche.  
- **Memoria distribuita**:  
  - Comunicazione via messaggi (message passing).  
  - Operazioni: point-to-point, broadcast, scatter, gather, reduce, total exchange.

---
**9. Regole Pratiche per la Progettazione**
- Identificare **computazioni indipendenti** (evitare dipendenze da loop, variabili di induzione, riduzioni).  
- Parallelizzare al **livello più alto possibile** (granularità maggiore).  
- Progettare per **scalabilità** (preferire data decomposition).  
- Usare **librerie thread-safe**.  
- Bilanciare il carico (**load balancing**).  
- Non assumere **ordine di esecuzione** dei thread.  
- Usare **thread-local storage** per ridurre sincronizzazione.  
- **Cambiare algoritmo** se necessario per favorire parallelismo (es. moltiplicazione di matrici O(n³) vs. Strassen).

---
**10. Metodologie di Progettazione**
- **Top-down**: decomposizione gerarchica dal sistema generale ai componenti.  
- **Bottom-up**: composizione di componenti base fino al sistema completo.  
- Spesso si usa un **mix di entrambi**.

---
 **11. Considerazioni su Cache e Performance**
- **Cache misses**: compulsory, capacity, conflict.  
- **Località spaziale/temporale** fondamentale per prestazioni.  
- Layout dati (AoS/SoA) scelto in base ai pattern di accesso e all’architettura (CPU vs GPU).

---
## 3_shared memory

**1. Motivazioni per l’uso dei Thread**
- **Portabilità software**: stesso codice su macchine seriali e parallele.  
- **Nascondere la latenza**: un thread può lavorare mentre un altro è in attesa (I/O, memoria).  
- **Bilanciamento del carico**: scheduling dinamico su più core.  
- **Facilità di programmazione**: API disponibili in molti linguaggi.

---
**2. Processi vs Thread**
- **Processo**: programma in esecuzione con spazio di indirizzamento proprio, stack, heap, registri. 
- **Thread**: flusso di controllo all’interno di un processo; **condivide lo spazio di indirizzamento** con altri thread dello stesso processo.  
- **Thread leggeri**: creazione e context switch più veloci rispetto ai processi.  
- **Thread a livello utente vs kernel**: gestiti dalla libreria o dal sistema operativo.

---
**3. Stati di un Thread**
1. **Newly generated**: appena creato.  
2. **Executable**: pronto per esecuzione, in attesa di core.  
3. **Running**: in esecuzione su un core.  
4. **Waiting**: in attesa di evento esterno (I/O, sincronizzazione).  
5. **Finished**: terminato.

---
 **4. Dati nei Thread**
- **Condivisi**: variabili globali, heap.  
- **Privati**: stack locale per ogni thread (variabili locali).  
- La **memoria condivisa** permette scambio rapido di dati, ma richiede sincronizzazione.

---
 **5. Sincronizzazione e Race Condition**
- **Race condition**: risultato dipende dall’ordine di esecuzione dei thread.  
- **Sezione critica**: parte di codice che accede a dati condivisi e deve essere eseguita in mutua esclusione.  
- **Meccanismi di sincronizzazione**:
  - **Lock/Mutex**: variabile a due stati (locked/unlocked).  
  - **Semaphore**: contatore intero con operazioni `P()` (wait) e `V()` (signal).  
  - **Monitor**: costrutto di linguaggio che garantisce mutua esclusione sui metodi.  
- **Istruzioni atomiche** (es. `lock xchg`) necessarie per implementare lock.

---
**6. Altri Meccanismi di Controllo**
- **Barriera**: punto di sincronizzazione dove tutti i thread devono arrivare prima di proseguire.  
- **Variabile di condizione**: thread attende finché una condizione non è soddisfatta.  
- **Deadlock**: due o più thread si bloccano reciprocamente in attesa di risorse.  
  - Condizioni: mutua esclusione, hold and wait, no preemption, attesa circolare.  
- **Livelock**: thread cambiano stato ma non progrediscono (es. corridoio stretto).

---
 **7. Accesso alla Memoria e Coerenza della Cache**
- Più copie degli stessi dati possono risiedere in cache diverse.  
- **Meccanismo di coerenza della cache** (es. protocollo MESI) mantiene consistenti le copie.  
- **False sharing**: oggetti diversi ma sulla stessa linea di cache causano contenzione hardware.  
  - Effetto: serializzazione nascosta, cali di prestazioni.  
  - Soluzioni: allineamento, padding, riduzione scritture, variabili locali.

---
 **8. False Sharing e OOP**
- In C++/OOP, campi di oggetti vicini in memoria (es. array di strutture) possono causare false sharing.  
- Metodi non inlinati possono causare ==miss nella cache delle istruzioni== (L1i).  
- Strategie: separare i dati frequentemente scritti, usare `alignas`, padding.

---
 **9. Considerazioni Pratiche**
- **Numero di thread**: sufficienti per saturare i core, ma non troppi per evitare overhead.  
- **Sincronizzazione**: necessaria per correttezza, ma troppo sincronizzazione riduce il parallelismo.  
- **Atomicità**: richiesta a livello hardware per implementare lock.  
- **Progettazione**: evitare dipendenze non necessarie, usare thread-local storage, profilare per identificare false sharing.

---
**10. API e Standard**
- **POSIX Threads (Pthreads)**: standard per la programmazione multithread in C.  
- Altre API: Windows threads, Java threads, OpenMP, Intel TBB.  
- **Hyperthreading** (Intel): thread hardware che appaiono come core logici.

---
## 4_Modern_Cpus+vectorization

**1. CPU MODERNE – Trend attuali**
- **Single-thread** migliora poco (soprattutto con turbo boost).
- **Multi-core** è la norma: più transistor → più core, non più GHz.
- **SIMD** (Single Instruction, Multiple Data) sfrutta unità vettoriali per parallelismo a livello dati.
- **Architetture eterogenee**: big.LITTLE (Apple M1, ARM), core dedicati (NPU, GPU integrate).

---
**2. Memoria – Il vero collo di bottiglia**
- **Latenza RAM alta** → si usano cache L1/L2/L3 e prefetching.
- **Banda memoria limitata** → può saturarsi con molti core attivi.
- **NUMA** (Non-Uniform Memory Access): memoria locale vs. remota, latenze diverse.
- **Machine Balance** = FLOP / Banda → se >1, la CPU aspetta la memoria.

---
**3. Problemi di coerenza e sincronizzazione**
- **Cache coherence** → protocolli snooping o directory-based.
- **False sharing**: due thread toccano dati diversi ma sulla stessa cache line → invalidazioni inutili.
- **Memory reordering** (Out-of-Order Execution) → può far fallire algoritmi di sincronizzazione classici (es. Dekker).
- **Soluzioni**: memory barrier, lock, variabili atomiche.

---
 **4. VECTORIZATION – Come sfruttare SIMD**
 
- **SIMD**: stessa operazione su più dati contemporaneamente (es. 8 float sommati in un colpo solo).
- **Vantaggio**: stessa potenza per più operazioni, meno pressione sulla coda istruzioni.
- **MMX** → **SSE** → **AVX/AVX2** → **AVX-512**.
- Larghezze: 128 bit → 256 bit → 512 bit.
- **FMA** (Fused Multiply-Add) raddoppia le operazioni per ciclo.

---
 **5. Metodi per vettorizzare**
1. **Auto-vectorization** del compilatore (meno sforzo).
2. **Hint** con `#pragma omp simd`.
3. **Intrinsic** (`<immintrin.h>`) per controllo manuale.
4. **Librerie ottimizzate** (Intel MKL, BLAS).

- Flag del compilatore **obbligatorie**
```bash
-march=native -ftree-vectorize -fstrict-aliasing
```
- **Report**: `-fopt-info-vec-optimized` per vedere cosa è stato vettorizzato.

-  Problema **Pointer Aliasing**
	- Se due puntatori potrebbero sovrapporsi, il compilatore **non vettorizza**.
	- **Soluzione**: usare `restrict` (in C) o `__restrict` (in C++).

---
**6. Stile di codice vector-friendly**
- **SOA** (Structure of Arrays) invece di AOS.
- Dati **contigui e allineati** (es. a 64 byte).
- Loop semplici, senza chiamate a funzione dentro.
- Variabili locali dentro il loop, bounds noti a compile-time.


# OpenMP
## 5_shared_memory_openMP

**1. Introduzione a OpenMP**
- **Framework a thread impliciti**: gestisce automaticamente creazione, gestione e sincronizzazione dei thread.
- **Vantaggio**: semplifica la programmazione parallela, minimizzando la ristrutturazione del codice seriale.
- **OpenMP**: API per programmazione parallela a memoria condivisa in C/C++ e Fortran.
- Componenti: **direttive del compilatore**, funzioni di libreria, variabili d’ambiente.

---
**2. Modello a Thread di OpenMP**
- **Fork-join**: il thread principale (master) crea un team di thread per le regioni parallele, poi si sincronizza (join).
- **SPMD** (Single Program, Multiple Data): stesso codice, dati diversi.
- Il compilatore deve supportare OpenMP (es. GCC, Clang, ICC con flag `-fopenmp`).
- Simbolo `_OPENMP` definito se supportato.

---
 **3. Modelli di Coerenza della Memoria**
- **Coerenza sequenziale (SC)**: tutte le operazioni di memoria appaiono eseguite in un ordine totale globale.
- **Coerenza rilassata (weak ordering)**: garantisce l’ordine ==solo attorno ai punti di sincronizzazione.==
- **OpenMP usa un modello di memoria rilassato**: le scritture in memoria condivisa non sono visibili fino a un punto di sincronizzazione (`barrier` o `flush`).

---
 **4. Analisi delle Dipendenze e Condizioni di Bernstein**
- **Condizioni di Bernstein**: due processi possono essere eseguiti in parallelo se:
  1. $I_1 \cap O_2 = \emptyset$
  2. $I_2 \cap O_1 = \emptyset$
  3. $O_1 \cap O_2 = \emptyset$
- Dipendenze **RAW, WAR, WAW** impediscono la parallelizzazione.
- Nei cicli: bisogna verificare che le iterazioni siano indipendenti.

---
**5. Direttive OpenMP di Base**
- **`#pragma omp parallel`**: crea un team di thread che eseguono il blocco.
- **Clausole**:
  - `shared` / `private`: visibilità delle variabili.
  - `default(none)` / `default(shared)`.
- **`#pragma omp parallel for`**: parallelizza un ciclo `for`.
  - Scheduling: `static`, `dynamic`, `guided`.
  - Clausole: `schedule`, `collapse` (per cicli annidati).
- **`#pragma omp sections`**: divide lavoro in sezioni parallele.

---
**6. Sincronizzazione in OpenMP**
- **`#pragma omp critical`**: sezione critica (mutua esclusione).
- **`#pragma omp atomic`**: operazione atomica (es. incremento).
- **`#pragma omp barrier`**: punto di sincronizzazione globale.
- **`#pragma omp single`**: eseguito da un solo thread (primo che arriva).
- **`#pragma omp master` (o `masked`)**: eseguito solo dal thread master.

---
 **7. Riduzioni e Variabili Private**
- **`reduction(op:var)`**: crea copie private per ogni thread, poi combina i risultati.
- Operatori supportati: `+`, `*`, `-`, `&`, `|`, `^`, `&&`, `||`, `min`, `max`.
- **Variabili private**: ogni thread ha la sua copia (non inizializzata).
- **Variabili shared**: accesso condiviso (richiede **sincronizzazione**).

---
**8. Scheduling dei Cicli**
- **`schedule(static)`**: blocchi fissi assegnati a thread.
- **`schedule(dynamic)`**: blocchi assegnati dinamicamente a thread liberi.
- **`schedule(guided)`**: blocchi di dimensione decrescente.
- **`nowait`**: rimuove la barriera implicita alla fine del costrutto.

---
**9. Cicli Annidati e Collapse**
- **`collapse(n)`**: appiattisce `n` cicli annidati in un unico spazio di iterazioni, aumentando il lavoro per thread. => caso di cicli annidati
- Funziona solo con cicli **perfettamente annidati** (nessuna istruzione tra i cicli).

---
**10. Lock Espliciti**
- **`omp_lock_t`**: lock mutex standard.
- **`omp_nest_lock_t`**: lock annidabile (stesso thread può lockare più volte).
- Funzioni: `omp_init_lock`, `omp_set_lock`, `omp_unset_lock`, `omp_destroy_lock`.

---
**Esempio Hello World**
```c
#include <omp.h>
#include <stdio.h>
int main() {
    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        printf("Hello from thread %d\n", tid);
        if (tid == 0) {
            int n = omp_get_num_threads();
            printf("Total threads: %d\n", n);
        }
    }
}
```

## 6_OpenMP_direttive

**1. Variabili Condivise e Private**
- **`private(list)`**: ogni thread ottiene una copia privata della variabile (**non inizializzata**).
- **`shared(list)`**: tutti i thread accedono alla stessa variabile in memoria condivisa.
- **`default(none|shared)`**: forza la dichiarazione esplicita dello scope delle variabili.
  - `default(none)` è una buona pratica per evitare errori.
- **`firstprivate(list)`**: variabili private inizializzate con il valore del thread master.
- **`lastprivate(list)`**: l’ultimo thread (nell’ultima iterazione o sezione) copia il valore privato nella variabile condivisa.

---
 **2. Clausola `reduction`**
- Sintassi: `reduction(op:list)` con `op ∈ {+, -, *, &, |, ^, &&, ||}`.
- Per ogni variabile nella lista:
  - Viene creata una copia privata per ogni thread, inizializzata all’**elemento neutro** dell’operazione (es. 0 per `+`, 1 per `*`).
  - Alla fine della regione parallela, i valori privati vengono combinati con `op` e il risultato viene scritto nella variabile condivisa.
- **Vantaggio**: più efficiente di una sezione critica per operazioni associative.

---
**3. Regioni Parallele e Direttive di Lavoro**
- **`#pragma omp parallel`**: crea un team di thread, ma non distribuisce il lavoro.
- **`#pragma omp for`**: distribuisce le iterazioni di un ciclo parallelo.
  - Il ciclo deve essere **parallelizzabile** (iterazioni indipendenti, numero noto in anticipo).
  - L’indice del ciclo è **privato** per ogni thread.
- **`#pragma omp parallel for`**: versione compatta (parallelo + distribuzione).
- **`#pragma omp sections`**: assegna sezioni di codice diverse a thread diversi.
- **`#pragma omp single`**: eseguito da un solo thread (il primo che arriva).
- **`#pragma omp master` / `masked`**: eseguito solo dal thread master.

---
**4. Scheduling dei Cicli (`schedule`)**
- **`schedule(static[,chunk])`**: blocchi fissi assegnati in round-robin.
- **`schedule(dynamic[,chunk])`**: blocchi assegnati dinamicamente ai thread liberi.
- **`schedule(guided[,chunk])`**: blocchi di dimensione decrescente.
- **`schedule(auto)`**: decisione delegata al compilatore/runtime.
- **`schedule(runtime)`**: usa la variabile d’ambiente `OMP_SCHEDULE`.
- **`nowait`**: rimuove la barriera implicita alla fine del costrutto.

---
**5. Direttiva `task`**
- **`#pragma omp task`**: definisce un’unità di lavoro indipendente.
- Ideale per problemi **irregolari**: cicli non limitati, algoritmi ricorsivi, producer-consumer.
- **`#pragma omp taskwait`**: barriera per task (attende il completamento dei task figli).
- Esempio: attraversamento di liste concatenate in parallelo.
- Spesso usata con `single` per generare task da un solo thread.

---
**6. Modello di Memoria di OpenMP**
- OpenMP usa un modello di memoria **rilassato (weak consistency)**.
- Le scritture in memoria condivisa **non sono immediatamente visibili** a tutti i thread.
- La sincronizzazione avviene tramite **punti di flush** (espliciti o impliciti).
- **`#pragma omp flush[(list)]`**:
  - Forza la scrittura delle variabili dalla cache locale alla memoria condivisa.
  - Senza lista: flush di **tutte** le variabili visibili al thread.
  - Con lista: flush solo delle variabili specificate.
- **Flush implicito** avviene in:
  - Barriere (`barrier`, fine di `parallel`, `for`, `sections`, `single`).
  - Ingresso/uscita da `critical` e `atomic`.
  - Acquisizione/rilascio di lock.
- **NON** avviene in: ingresso a `for`, `sections`, `single`, `master`.

---
 **7. Sincronizzazione e Protezione dei Dati**
- **`#pragma omp atomic`**: operazione atomica su una singola variabile.
  - Supporta `read`, `write`, `update`, `capture`.
  - Meno overhead di `critical`.
- **`#pragma omp critical [(name)]`**: sezione critica con mutua esclusione.
  - Sezioni critiche con **nome diverso** possono essere eseguite in parallelo.
- **Lock espliciti** (`omp_lock_t`):
  - Più flessibili delle sezioni critiche anonime.
  - Utili per proteggere strutture dati complesse (es. code).
- **`#pragma omp threadprivate(list)`**:
  - Variabili globali replicate privatamente per ogni thread (persistono tra le regioni parallele).
  - `copyin(list)` inizializza le copie private con il valore del master.

---
**8. Avvertenze e Best Practice**
- **Non mescolare** `atomic` e `critical` sulla stessa variabile.
- **Evitare deadlock**:
  - Non annidare sezioni critiche **anonime**.
  - Acquisire lock/named critical in **ordine consistente**.
- **Ridurre al minimo le sezioni critiche**:
  - Usare `reduction` quando possibile.
  - Proteggere solo quando necessario (es. `flush` + doppio controllo per `max`).
- **`flush`** è potente ma **pericoloso**:
  - Difficile da usare correttamente, può introdurre bug sottili.
  - Flush multipli non ordinati possono causare race condition.
  - Meglio flushare insieme variabili correlate (es. `flag` e `data`).

---
**9. Esempio Pratico: Producer-Consumer con Code**
- **Problema**: thread che si scambiano messaggi tramite code.
- **Soluzione**:
  - Ogni thread ha una coda (`queue_s`) con lock dedicato.
  - `Enqueue` protetta da lock (o critical) perché modifica la coda di un altro thread.
  - `Dequeue` può essere ottimizzata: se la coda ha più di un elemento, non serve sincronizzazione (uso di `enqueued`/`dequeued` per stimare la dimensione).
  - Rilevazione terminazione: contatore `done_sending` aggiornato atomicamente.
  - Inizializzazione: barriera per assicurare che tutte le code siano allocate prima dell’uso.

---
**10. Riepilogo Direttive e Clausole**
- Clausole comuni: `private`, `shared`, `default`, `firstprivate`, `lastprivate`, `reduction`, `schedule`, `nowait`, `if`, `num_threads`.
- Direttive di lavoro: `for`, `sections`, `single`, `task`.
- Sincronizzazione: `critical`, `atomic`, `barrier`, `flush`, `taskwait`.
- Gestione lock: `omp_init_lock`, `omp_set_lock`, `omp_unset_lock`, `omp_destroy_lock`.
## 7_OpenMP_Perfomance

 **1. First Touch Policy (Slide 4-11)**
 
- **Problema**: Su sistemi NUMA, se un thread alloca **tutta la memoria**, tutti i dati finiscono su un solo nodo → accessi lenti per altri thread.
- **Soluzione**: Parallelizzare l'inizializzazione dei dati tramite `#pragma omp parallel for`.
- **Esempio**: Inizializzare array grandi in parallelo distribuisce la memoria vicino ai thread che la useranno.
- **Vantaggio**: Fino a 10× miglioramento delle prestazioni.

---
**2. Sistemi NUMA (Slide 5-8)**

- Architettura moderna: ogni CPU ha la sua memoria locale + accesso a memoria remota (più lenta).
- Usare `numactl -H` per vedere configurazione NUMA (nodi, CPU, distanze di latenza).
- Distanze tra nodi indicano latenze relative (es. 10=locale, 21=remota).

---
**3. Binding dei Thread**

- **OMP_PLACES**: Definisce dove possono eseguire i thread (`sockets`, `cores`, `threads`).
- **OMP_PROC_BIND**: Controlla il mapping:
  - `spread`: Thread distribuiti il più possibile
  - `close`: Thread vicini tra loro
  - `master/primary`: Tutti vicini al master
- **Scopo**: Migliorare località della memoria e ridurre latenza.

---
**4. Regole Pratiche (Slide 18)**

- Hyperthreading non aiuta in kernel memory-bound (ma non danneggia).
- Per kernel limitati da banda memoria su multi-socket: usare `OMP_PROC_BIND=spread`.
- First Touch è essenziale (fino a 10× speedup).

---
**5. Processo di Ottimizzazione in 4 Step**

1. **Base**: Implementazione semplice con loop-level OpenMP.
2. **Step 1**: Ridurre overhead thread → unire regioni parallele.
3. **Step 2**: Ridurre sincronizzazione → aggiungere `nowait`, partizionamento manuale.
4. **Step 3**: Privatizzare variabili → evitare race condition.
5. **Step 4**: Verificare correttezza → usare Intel Inspector per **race condition**.

---
**6. Esempio Pratico Stencil (Slide 24-42)**

- **Problema iniziale**: Due loop paralleli separati con overhead duplicato.
- **Ottimizzazione**:
  - Unica regione parallela
  - Calcolo manuale bounds (`jltb`, `jutb`) per ogni thread
  - Privatizzazione di tutte le variabili di loop
  - Aggiunta barriere esplicite dove necessario
- **Risultato**: Meno sincronizzazione, migliore località cache.

---
**7. Direttive SIMD**

- `#pragma omp simd`: Vettorizza loop interni.
- `#pragma omp for simd`: Combina parallelizzazione thread + vettorizzazione.
- **Esempio**: Applicare a kernel stencil 2D per miglioramento ulteriore.

---
**8. Kernel Separabili (Slide 45-53)**

- Alcuni stencil (es. Gaussiano) possono essere separati in kernel 1D.
- **Vantaggio**: Meno computazione, più località.
- **Memoria**: Usare variabili private per dati locali, condivise solo se necessario.
- **Sincronizzazione**: Barriere necessarie tra fasi di calcolo.

---
### **PARTE 2: THREAD SANITIZER (Slide 58-75)**

 **9. Rilevamento Data Race**
 
- **TSan**: Strumento LLVM per C/C++ che rileva accessi concorrenti non sincronizzati.
- **Funzionamento**: Traccia ogni accesso memoria, verifica sincronizzazione.
- **Performance Impact**: 2×-20× slowdown, 5×-10× memoria in più.
- **Uso**: Compilare con `-fsanitize=thread`, disabilitare ASLR.

---
 **10. Alternative**
 
- **Archer**: Versione per OpenMP.
- **Intel Inspector**: GUI per debug race condition e deadlock.
- **Altri sanitizer**: ASAN (memory errors), MSAN (uninitialized memory), UBSAN (undefined behavior).

---
### **PARTE 3: TIMING E PROFILING (Slide 76-111)**

 **11. Timing Corretto**
 
- **NO** `clock()`: Misura tempo CPU totale (non wall-clock).
- **SI** `omp_get_wtime()`, `gettimeofday()`, `std::chrono`: Misurano tempo reale.
- **clock_gettime()**: Precisione nanosecondi (POSIX).

---
**12. Profiling Tools**

- **Google Perftools**:
  - Leggero, sampling-based
  - Linkare con `-lprofiler`
  - Analisi con `pprof --text`
- **Valgrind/Callgrind**:
  - Più preciso, più lento
  - Profiling cache: `--simulate-cache=yes`
- **Intel VTune**:
  - Strumento avanzato per bottleneck
  - Parte di oneAPI (gratuito)

---
**13. Principali Bottleneck**

1. **I/O**: Fa attendere i thread, parallelismo non aiuta se non c'è lavoro durante attesa.
2. **Memoria**: Contesa in accessi NUMA, **false sharing**.
3. **Overhead Thread**: Creazione/distruzione thread costa; usare thread pool.

---
 **14. Consigli Generali**
 
- Ottimizza solo dopo aver misurato il bottleneck reale. => identificare questi punti prima di ottimizzare
- Mantieni il codice leggibile.
- Usa tool di profiling prima di ottimizzare.
- Considera trade-off complessità/guadagno.

# GPU_CUDA
