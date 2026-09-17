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

## 8_gpu_introduction.pdf

---
### 🧠 1. FILOSOFIA CPU vs GPU

- **CPU**: progettata per la **bassa latenza**. Ottimizzata per codice sequenziale, ha grosse cache, branch prediction, out-of-order execution. Esegue bene poche cose complesse e con controlli logici intricati (control-intensive).
- **GPU**: progettata per l'**alto throughput**. Ha migliaia di core semplici, cache piccole, quasi nessuna logica di controllo. È ottimizzata per calcoli ripetitivi su grandi moli di dati (data-parallel).
- **Conseguenza**: La CPU esegue la parte sequenziale e di controllo, la GPU esegue la parte pesante e parallela (modello eterogeneo).

---
### ⚙️ 2. ARCHITETTURA HARDWARE DELLA GPU

- La GPU è composta da **Streaming Multiprocessors (SM)**.
- Ogni SM contiene **CUDA Core** (i "semplici operai" che fanno i calcoli) e una **Shared Memory** (memoria condivisa veloce).
- L'unità di esecuzione minima è il **warp**: 32 thread che eseguono la stessa identica istruzione in contemporanea (lockstep). 
- **SIMT (Single Instruction Multiple Thread)**: i thread hanno un proprio program counter e registri, quindi possono seguire percorsi diversi (anche se con divergenza causano cali di performance).

---
### 🚀 3. IL PROBLEMA DELLA BANDWIDTH (MOLTO IMPORTANTE!)

- La memoria globale (VRAM) è il **collo di bottiglia** principale. La banda è enorme (GB/s), ma la potenza di calcolo cresce più velocemente. 
- Esempio pratico: su una GTX 1080 Ti ogni CUDA core ha a disposizione solo **0.09 byte/cycle**. Significa che per ogni 11 istruzioni, il core può leggere solo 1 byte dalla VRAM!
- **Morale:** Se il codice continua a leggere/scrivere dalla VRAM, i core restano in attesa (memory-bound). 
- **Soluzione:** Bisogna **riutilizzare i dati** (località di riferimento) usando le cache e soprattutto la **shared memory**, per ridurre il traffico verso la VRAM (compute-bound).

---
### 🧮 4. TENSOR CORES

- Unità di calcolo **specializzate** per la moltiplicazione di matrici (fondamentali per il Deep Learning).
- Eseguono `D = A*B + C` (Fused Multiply-Add) in **1 singolo ciclo di clock** (contro le centinaia di operazioni dei normali core).
- Lavorano con precisione mista (FP16, BF16, INT8, INT4) per massimizzare le performance.
- Sono il motivo per cui le GPU NVIDIA dominano il settore dell'Intelligenza Artificiale.

---
### 🧩 5. IL MODELLO DI PROGRAMMAZIONE (LA GERARCHIA)

*(La parte più importante per scrivere il codice!)*

- **Grid (griglia)**: l'insieme di **tutti** i thread lanciati da un kernel.
- **Block (blocco)**: sottogruppo di thread che cooperano. Possono sincronizzarsi (`__syncthreads()`) e condividere dati tramite **Shared Memory** (veloce!).
- **Thread**: singola unità di esecuzione (il "lavoratore").
- **Regola di Ferro**: Thread di blocchi **diversi** NON possono cooperare (nessuna sincronizzazione, nessuna shared memory condivisa).

---
### 🧮 6. INDICIZZAZIONE E DECOMPOSIZIONE DEI DATI

- Per trovare l'indice globale del dato da processare quando si usano più blocchi:
  `int idx = blockIdx.x * blockDim.x + threadIdx.x;`
- **Attenzione al Padding**: se il numero di dati non è multiplo del numero di thread, si aggiungono elementi fittizi. Nel kernel si usa `if (idx < N) return;` per escluderli.
- La dimensione del blocco (`blockDim.x`) deve essere **multiplo di 32** (warp size) per non sprecare risorse.

---
### 🏃 6. OCCUPANCY

- **Occupancy**: è il rapporto tra i warp attivi su uno SM e il massimo numero di warp supportati (es. 64 warp per SM su GPU moderne).
- Serve ad avere abbastanza warp in coda in modo che, quando un warp aspetta i dati dalla VRAM, lo scheduler possa passare subito a un altro warp (nascondendo la latenza).
- **Attenzione**: Alta Occupancy non è sempre sinonimo di alte prestazioni! Una Occupancy più bassa (ma con risorse come registri e shared memory maggiori per singolo thread) può talvolta dare performance migliori.

---
### 🔌 8. TRASFERIMENTO DATI (HOST ↔ DEVICE)

- CPU e GPU hanno memorie separate. Per lavorare, i dati devono viaggiare attraverso il bus **PCI Express (PCIe)**.
- Il PCIe è un **"tubo" molto stretto** (es. 16 GB/s su Gen3) rispetto alla velocità interna della GPU (centinaia di GB/s).
- **Conseguenza**: il trasferimento dei dati è un costo enorme. La strategia è trasferire pochi dati e riusarli il più possibile sulla GPU.
- Per collegare più GPU (o GPU-CPU) più velocemente, NVIDIA usa il bus **NVLink** (fino a 1.8 TB/s).

---
### ⏳ 9. ASINCRONIA

- Il lancio di un kernel è **asincrono**: la CPU lancia il comando sulla GPU e **continua subito** a eseguire il suo codice senza aspettare che la GPU finisca.
- Per sincronizzarsi e aspettare la fine dei calcoli sulla GPU, si usa `cudaDeviceSynchronize()`.
- Si possono usare gli **stream (CUDA)** per sovrapporre il trasferimento dei dati con i calcoli, ottimizzando ulteriormente le performance.

---
### ⚠️ 10. SINCRONIZZAZIONE

- La GPU offre solo meccanismi base di coordinamento: **barriere** (solo all'interno di uno stesso blocco) e **operazioni atomiche** (per aggiornamenti sicuri in memoria globale).
- Non esistono i classici mutex della programmazione CPU.


## 9_cuda_intro

---
### 🚀 1. INTRODUZIONE A CUDA

- **CUDA** (Compute Unified Device Architecture) è la piattaforma di NVIDIA per la programmazione GPU generica (GPGPU).
- La GPU è vista come un **co-processore** della CPU (host), con la sua propria memoria (VRAM / global memory) e in grado di eseguire migliaia di thread in parallelo.
- Un programma CUDA è **eterogeneo**: il codice host gira sulla CPU, il codice device (kernel) gira sulla GPU.

---
### ⚙️ 2. COMPILAZIONE (nvcc)

- **nvcc** è il compilatore CUDA. Separa il codice host (compilato con gcc/clang) dal codice device.
- **PTX** (Parallel Thread Execution): è un assembly virtuale intermedio, indipendente dall'architettura specifica.
- **JIT (Just-In-Time) Compilation**: il driver CUDA compila il PTX in binario nativo al momento dell'esecuzione, rendendo i programmi compatibili con GPU future.
- **Fat Binary**: l'eseguibile contiene sia PTX che binario precompilato per architetture note. Se non trova il binario, usa il JIT.
- **JIT Caching**: il driver salva in cache il binario generato per evitare di ricolpilarlo a ogni esecuzione.

---
### 🔑 3. QUALIFICATORI (SPECIALI PAROLETTE MAGICHE)

| Qualificatore | Eseguito su | Chiamabile da                    |
| ------------- | ----------- | -------------------------------- |
| `__global__`  | GPU         | CPU (kernel)                     |
| `__device__`  | GPU         | GPU                              |
| `__host__`    | CPU         | CPU (default se non specificato) |

- `__global__` deve ritornare `void`.
- Si può usare `__host__ __device__` per generare due versioni della stessa funzione (una per CPU, una per GPU).

---
### 🧠 4. LA GERARCHIA DEI THREAD (FONDAMENTALE!)

- **Grid**: insieme di **tutti** i thread lanciati da un kernel.
- **Block**: sottogruppo di thread che cooperano. Possono sincronizzarsi (`__syncthreads()`) e condividere dati tramite **shared memory**.
- **Thread**: singola unità di esecuzione.
- **Regola d'oro**: thread di blocchi **diversi** NON possono cooperare.

---
### 🧮 5. INDICI E COORDINATE

- **`threadIdx`** e **`blockIdx`** sono vettori a 3 componenti (`x`, `y`, `z`).
- Per calcolare l'indice **globale** (1D):
  ```cpp
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  ```
- Per 2D:
  ```cpp
  int col = blockIdx.x * blockDim.x + threadIdx.x;
  int row = blockIdx.y * blockDim.y + threadIdx.y;
  int idx = row * width + col;
  ```
- **Convenzione cruciale**: `threadIdx.x` si usa per l'ultima dimensione (colonne) per garantire **accesso coalescente** (thread adiacenti leggono celle di memoria contigue).

---
### 🧠 6. LA STRUTTURA DI UN PROGRAMMA CUDA (I 5 PASSI)

1. **Alloca memoria sulla GPU** → `cudaMalloc()`
2. **Copia i dati dalla CPU alla GPU** → `cudaMemcpy(..., cudaMemcpyHostToDevice)`
3. **Lancia il kernel** → `kernel<<<grid, block>>>(args)`
4. **Copia i risultati dalla GPU alla CPU** → `cudaMemcpy(..., cudaMemcpyDeviceToHost)`
5. **Libera la memoria sulla GPU** → `cudaFree()`

---
### 🗂️ 7. MEMORIE DELLA GPU (GERARCHIA)

| Memoria | Chi ci scrive? | Velocità | Visibilità |
|---------|---------------|----------|------------|
| **Registers** | Ogni thread | ⚡⚡⚡ Veloce | Privata (per thread) |
| **Local memory** | Ogni thread | 🐢 Lenta | Privata (per thread) |
| **Shared memory** | Programmatore (esplicita) | ⚡⚡⚡ Veloce | Condivisa (tra thread dello stesso blocco) |
| **Global memory** | Programmatore | 🐢🐢 Lenta | Condivisa (tutti i thread del grid) |
| **Constant memory** | Programmatore | ⚡⚡ Veloce (se tutti leggono lo stesso dato) | Condivisa (tutti i thread del grid) |

---
### 🧰 8. API DI GESTIONE MEMORIA

- **`cudaMalloc((void**)&ptr, size)`** → alloca sulla GPU.
- **`cudaMemcpy(dst, src, size, kind)`** → copia dati. **È sincrona!**
- **`cudaFree(ptr)`** → libera memoria.
- **`cudaGetErrorString(err)`** → trasforma un errore in messaggio leggibile.
- **Buona pratica**: usare macro come `CUDA_CHECK_RETURN` per gestire gli errori.

---
### ⏳ 9. ASINCRONIA

- Il lancio del kernel è **asincrono**: la CPU non aspetta che la GPU finisca.
- Per sincronizzarsi: `cudaDeviceSynchronize()` (blocca la CPU fino al completamento di tutti i kernel).
- `cudaMemcpy` è **sincrono** (blocca la CPU fino a fine copia).

---
### 🧪 10. ESEMPI PRATICI

#### Somma Vettoriale (1D)

```cpp
__global__ void sum(float *A, float *B, float *C) {
    int i = threadIdx.x;
    C[i] = A[i] + B[i];
}
// Lancio: sum<<<1, N>>>(A, B, C);
```

#### Moltiplicazione Matrici (2D)

```cpp
__global__ void matMul(float *M, float *N, float *P, int w) {
    int tx = threadIdx.x;   // colonna
    int ty = threadIdx.y;   // riga
    float sum = 0.0f;
    for (int k = 0; k < w; k++) {
        sum += M[ty * w + k] * N[k * w + tx];
    }
    P[ty * w + tx] = sum;
}
// Lancio: dim3 block(16,16); dim3 grid(w/16, w/16); matMul<<<grid, block>>>(M, N, P, w);
```

---
### 🧩 11. LIMITI E INDICIZZAZIONE CON PIÙ BLOCCHI

- Il numero massimo di thread per blocco è **1024** (tipicamente).
- Se il problema è più grande, si usano **più blocchi** e l'indice globale diventa:
  ```cpp
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  ```
- Se `N` non è multiplo di `blockDim.x`, si usa il **padding** e un controllo:
  ```cpp
  if (idx < N) { ... }
  ```

---
### 📊 12. OCCUPANCY (SLIDE 57-65)

- **Occupancy**: rapporto tra warp attivi su uno SM e il massimo supportato.
- **Formula**: `Occupancy = Warp attivi / Warp massimi`.
- Strumenti: **Occupancy Calculator** (deprecato) → ora **NVIDIA Nsight Compute**.
- Per sapere quanti registri usa il kernel: compilare con `nvcc -Xptxas="-v"`.
- L'occupancy è limitata da:
  - **Registri per thread**
  - **Shared memory per blocco**
  - **Numero di warp**
- **Attenzione**: alta occupancy non sempre = alte prestazioni! A volte ridurre l'occupancy (usando più risorse per thread) può migliorare le performance.

---

## 10_cuda_2

---
### 🧵 1. ESECUZIONE E SCHEDULAZIONE (WARP E SM)

- **Warp**: unità di esecuzione minima (32 thread). Tutti i thread in un warp eseguono la stessa istruzione in **lockstep**.
- **Block**: assegnato a uno Streaming Multiprocessor (SM). Uno SM può ospitare **più blocchi** contemporaneamente (es. fino a 8, dipende dalle risorse).
- **Thread**: ogni thread viene eseguito su un CUDA core.
- **Scheduling**: a ogni clock, lo scheduler dello SM sceglie un warp **pronto** (cioè che non aspetta dati dalla memoria o che non ha dipendenze da istruzioni precedenti) e lo esegue.
- **Scalabilità trasparente**: i blocchi possono essere eseguiti in qualsiasi ordine e su qualsiasi SM. Il codice scala automaticamente su GPU con più o meno SM.

---
### 🧩 2. INDICIZZAZIONE (ARRAY E MATRICI)

- **Indice globale 1D**:
  ```cpp
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  ```
- **Indice 2D (riga/colonna)**:
  ```cpp
  int row = blockIdx.y * blockDim.y + threadIdx.y;
  int col = blockIdx.x * blockDim.x + threadIdx.x;
  int idx = row * width + col;
  ```
- **Indice 3D (volume)**:
  ```cpp
  int plane = blockIdx.z * blockDim.z + threadIdx.z;
  int idx = plane * height * width + row * width + col;
  ```
- **Regola d'oro**: la dimensione `x` è quella che cambia più velocemente (serve per l'accesso coalescente alla memoria).

---
### ⚙️ 3. DIMENSIONI MASSIME

- **Grid (blocchi)**: max 65.535 in ogni dimensione (`x`, `y`, `z`). Praticamente illimitato.
- **Block (thread)**: max **1024 thread totali** per blocco (distribuibili in 3D, es. 32×32×1 = 1024, ma 32×32×2 = 2048 non è permesso).

---

### 🧵 4. THREAD E WARP (PARTIZIONAMENTO)

- I thread in un blocco vengono divisi in warp da 32.
- **Ordine di assegnazione**: prima si riempiono i thread `x`, poi `y`, poi `z`. Quindi:
  - Warp 0 = thread 0–31
  - Warp 1 = thread 32–63
  - ecc.
- Se il numero di thread non è multiplo di 32, l'ultimo warp ha thread **inattivi** (non è efficiente).
- **Buona pratica**: usare blocchi con dimensione **multipla di 32** (es. 128, 256, 512, 1024).

---
### ⚠️ 5. DIVERGENZA (WARP DIVERGENCE)

- **Problema**: se in uno stesso warp i thread prendono percorsi diversi (es. `if/else`), il warp esegue **prima un ramo** (disattivando gli altri thread) e **poi l'altro ramo**.
- **Conseguenza**: i due rami vengono eseguiti in **seriale**, non in parallelo. Questo riduce le performance.
- **Esempio**: 32 thread in un warp, metà fanno `then`, metà `else` → il warp esegue `then` (con 16 thread attivi) e poi `else` (con gli altri 16). Si perde il 50% della capacità.
- **Casi estremi**: uno `switch` con 32 case diversi è un disastro (32 esecuzioni seriali → performance crollano del 97%).
- **Predicazione**: per brevi rami, il compilatore usa istruzioni predicate (NOP per i thread che non devono eseguire) invece di fare branching, evitando la divergenza.

---
### 🛑 6. SINCRONIZZAZIONE E DEADLOCK

- **`__syncthreads()`**: barriera a livello di blocco. Tutti i thread del blocco devono raggiungerla prima che qualcuno prosegua.
- **Regola d'oro**: `__syncthreads()` **deve** essere raggiunta da **tutti** i thread attivi del blocco. Se anche un solo thread non la raggiunge (perché in un ramo `else` diverso), si può verificare un **deadlock** (il blocco si blocca per sempre).
- **Attenzione alle GPU Volta+** (compute capability 7.x+): la sincronizzazione è più rigorosa. Sulle GPU pre-Volta, bastava che almeno un thread per warp raggiungesse la barriera. Ora **tutti** i thread del blocco devono raggiungerla, altrimenti deadlock certo.

---
### 🧠 7. ESEMPI PRATICI (KERNEL 2D E 3D)

- **Elaborazione immagine (2D)**:
  - Si usa un grid 2D di blocchi 2D.
  - Ogni thread calcola la riga (`row`) e colonna (`col`) del pixel da elaborare.
  - Si controlla che il thread non esca dai bordi dell'immagine (`if (row < h && col < w)`).
  - Esempi: conversione RGB→Grigio, blur (filtro di sfocatura).
- **RGB → Grayscale**:
  - L'immagine RGB ha 3 canali per pixel. L'offset per l'array RGB è `rgbOffset = grayOffset * CHANNELS`.
- **Blur (sfocatura)**:
  - Ogni thread legge un intorno di pixel (es. 3×3) per calcolare la media.
  - Accessi alla global memory molto intensivi. Problema di bandwidth! (serve shared memory).

---
### 🗂️ 8. GERARCHIA DELLE MEMORIE (RIEPILOGO)

| Memoria | Qualificatore | Scope | Velocità | Visibilità |
|---------|---------------|-------|----------|------------|
| **Registri** | (nessuno, variabili locali) | Thread | ⚡⚡⚡ (1 ciclo) | Privata |
| **Local memory** | (array automatici) | Thread | 🐢 (in global memory) | Privata |
| **Shared memory** | `__shared__` | Block | ⚡⚡⚡ (on-chip) | Condivisa (blocco) |
| **Global memory** | `__device__` | Grid | 🐢🐢 (DRAM) | Condivisa (tutti) |
| **Constant memory** | `__constant__` | Grid | ⚡⚡ (cache dedicata) | Condivisa (tutti, sola lettura) |

---
### 🧰 9. QUALIFICATORI PER VARIABILI

- **`__shared__ int shVar;`**: variabile in shared memory (visibile a tutto il blocco, veloce).
- **`__device__ int gVar;`**: variabile in global memory (visibile a tutti, lenta).
- **`__constant__ int cVar;`**: variabile in constant memory (sola lettura, cache dedicata).
- **`extern __shared__ int dynSh[];`**: shared memory dinamica (dimensione decisa al lancio del kernel).

---
### 💡 10. SHARED MEMORY (DETTAGLI)

- È **programmabile** (a differenza della cache L1 della CPU). Il programmatore decide cosa metterci.
- È **on-chip**: velocissima (bassa latenza) e ad alta bandwidth.
- Usata per:
  - Comunicazione tra thread dello stesso blocco.
  - Riuso dei dati (riduce accessi alla global memory).
- **Sincronizzazione obbligatoria**: per evitare race condition, si usa `__syncthreads()` prima e dopo l'accesso.

---
### 🌐 11. CONSTANT MEMORY

- **Sola lettura** per i thread.
- **Cache dedicata** per SM.
- **Performance ottimale** quando **tutti i thread di un warp leggono lo stesso indirizzo**.
- Esempio: coefficienti, parametri fissi, lookup table.
- Si inizializza dalla CPU con `cudaMemcpyToSymbol()`.

---
### 📦 12. PINNED (PAGE-LOCKED) MEMORY

- La memoria della CPU viene **bloccata** (non può essere swappata su disco).
- Permette al controller DMA di trasferire dati tra host e device **più velocemente** (senza intervento della CPU).
- Si alloca con `cudaMallocHost()` invece di `malloc()`.
- **Pro**: trasferimenti più veloci.
- **Contro**: allocazione/deallocazione più costosa. Se se ne usa troppa, il sistema operativo ha meno memoria disponibile per lo swapping.

---
### ☁️ 13. UNIFIED MEMORY

- Disponibile da CUDA 6.0 e Kepler.
- **Astrazione**: un unico spazio di indirizzamento (virtuale) condiviso tra CPU e GPU.
- **Vantaggio**: codice più semplice (non serve `cudaMemcpy` esplicito). Si usa `cudaMallocManaged()`.
- **Svantaggio**: più lento della gestione manuale ottimizzata.
- **Su Pascal+**: supporto hardware al page fault e migrazione automatica delle pagine tra CPU e GPU. La memoria viene allocata fisicamente solo al primo accesso.
- **Consiglio**: per performance massime, usare ancora la gestione manuale.

---
### 📏 14. LINEA GUIDA PER I BLOCCHI

- **Dimensione multipla di 32** (warp size).
- **Almeno 128 o 256 thread per blocco** (per avere abbastanza warp da nascondere la latenza).
- **Numero di blocchi molto maggiore del numero di SM** (per esporre abbastanza parallelismo).
- **Esempio (Fermi SM)**: 8×8 = 64 thread → solo 512 thread per SM (male). 16×16 = 256 thread → fino a 6 blocchi = 1536 thread (pieno). 32×32 = 1024 thread → solo 1 blocco = 1024 thread (2/3 della capacità).

---
### 📊 15. ESEMPIO DI BANDWIDTH (PERCHÉ SERVE SHARED MEMORY)

- Nel kernel `blurKernel`, ogni thread legge un intorno di pixel dalla global memory.
- Per ogni operazione in virgola mobile, si fanno accessi alla global memory (4 byte).
- GPU con 1500 GFLOPS e 200 GB/s di banda: per raggiungere i 1500 GFLOPS servirebbero 6000 GB/s di banda! La banda reale limita il tutto a 50 GFLOPS (solo il 3.3% del picco).
- **Morale**: bisogna ridurre gli accessi alla global memory, usando **shared memory** per riusare i dati.

## 11_cuda_3

---
### 🧠 1. IL PROBLEMA DELLA MOLTIPLICAZIONE DI MATRICI (NAIVE)

- **Ogni thread** calcola un singolo elemento della matrice risultato `P` come prodotto scalare di una riga di `M` e una colonna di `N`.
- **Problema**: Ogni thread, per calcolare il suo elemento, deve caricare dalla global memory **tutta** la sua riga di `M` e tutta la sua colonna di `N`. 
- **Conseguenza**: Gli elementi di `M` e `N` vengono ricaricati dalla global memory **decine/centinaia di volte**, causando un traffico di memoria enorme e colli di bottiglia (si sfrutta solo il ~3% della potenza di calcolo!).

---
### 🧩 2. LA SOLUZIONE: IL TILING (PIASTRELLAMENTO)

- **Idea**: Sfruttare il fatto che più thread nello stesso blocco accedono agli **stessi elementi** di `M` e `N` (es. due thread nella stessa riga leggono gli stessi elementi di `M`).
- **Obiettivo**: Caricare ogni elemento di `M` e `N` dalla global memory **una sola volta** e riutilizzarlo per tutti i thread del blocco che ne hanno bisogno.
- **Come**: Si usa la **shared memory** (on-chip, veloce) come cache programmabile.

---
### 🧱 3. CONCETTI CHIAVE DEL TILING

- **Tile (piastrella)**: Un sottoinsieme della matrice che può essere contenuto nella shared memory. Dimensione tipica: `TILE_WIDTH × TILE_WIDTH` (es. 16×16 o 32×32).
- **Fasi (Phases)**: Il calcolo del prodotto scalare viene suddiviso in più fasi. In ogni fase, il blocco carica un tile di `M` e uno di `N` nella shared memory, li usa per calcolare un contributo parziale del prodotto scalare, poi passa al tile successivo.
- **Numero di fasi** = `k / TILE_WIDTH` (per matrici rettangolari `j×k` * `k×l`). => width della matrice

---
### 🔄 4. IL FLUSSO DEL TILING (PASSI DEL KERNEL)

Per ogni fase (`ph`), il blocco esegue:
1. **Caricamento collaborativo**: Ogni thread carica un elemento di `M` (dalla riga `Row`, colonna `ph*TILE_WIDTH + tx`) e uno di `N` (dalla riga `ph*TILE_WIDTH + ty`, colonna `Col`) nella shared memory.
2. **Sincronizzazione**: `__syncthreads()` per assicurarsi che **tutti** i thread abbiano finito di caricare il tile.
3. **Calcolo**: Ogni thread usa i dati nella shared memory (`Mds[ty][i] * Nds[i][tx]`) per accumulare il contributo parziale del tile corrente.
4. **Sincronizzazione**: `__syncthreads()` per assicurarsi che **tutti** i thread abbiano finito di usare i dati del tile prima di sovrascriverli con il tile successivo.

---
### 📈 5. VANTAGGI DEL TILING (NUMERI)

- **Riduzione del traffico**: Invece di caricare ogni elemento `k` volte dalla global memory, lo si carica **una sola volta** per blocco.
- **Rapporto operazioni/load**:
  - Con `TILE_WIDTH = 16`: per ogni caricamento dalla global memory, si fanno **16 operazioni** floating-point.
  - Con `TILE_WIDTH = 32`: ==per ogni caricamento==, si fanno **32 operazioni** floating-point.
- **Morale**: Più grande è il tile, più alto è il riuso dei dati e migliori sono le performance (fino a quando la shared memory e l'occupancy lo permettono).

---
### ⚠️ 6. LIMITAZIONI E TRADE-OFF DEL TILING

- **Shared memory limitata**: Se il tile è troppo grande, non ci sta nella shared memory.
- **Occupancy**: Tile grandi riducono il numero di blocchi che possono risiedere contemporaneamente su uno SM, riducendo l'occupancy e la capacità di nascondere la latenza.
- **Esempio su Fermi (16KB shared memory)**:
  - `TILE_WIDTH = 16` (2KB per blocco) → fino a **8 blocchi** per SM → alta occupancy.
  - `TILE_WIDTH = 32` (8KB per blocco) → solo **1-2 blocchi** per SM → bassa occupancy.

---
### 🧩 7. INDICIZZAZIONE E ACCESSO ALLA MEMORIA

- **Shared memory**: si dichiara con `__shared__ float Mds[TILE_WIDTH][TILE_WIDTH]`. La sintassi `[][]` è zucchero sintattico: il compilatore la traduce in un array 1D lineare.
- **Global memory**: si accede SEMPRE con indicizzazione lineare: `M[Row * k + ph * TILE_WIDTH + tx]` (per M) e `N[(ph * TILE_WIDTH + ty) * l + Col]` (per N).
- **Perché?** Perché la global memory è allocata con `cudaMalloc()` come array 1D; l'indicizzazione lineare è l'unico modo per accedervi in modo efficiente e coalescente.

---
### 🛡️ 8. GESTIONE DEI BORDI (BOUNDARY CHECKS)

- **Problema**: Se la dimensione della matrice non è multipla di `TILE_WIDTH`, gli ultimi tile "sforano" la matrice.
- **Soluzione**: Prima di caricare un elemento in shared memory, si controlla se l'indice è valido. Se non lo è, si carica **0**.
- **Condizioni di validità** (per matrici rettangolari `j×k` * `k×l`):
  - **Caricamento M**: `Row < j && ph * TILE_WIDTH + tx < k`
  - **Caricamento N**: `ph * TILE_WIDTH + ty < k && Col < l`
  - **Scrittura P**: `Row < j && Col < l`
- **Perché mettere 0?** Perché `0 * x = 0`, quindi il contributo del tile "fuori bordo" non altera il risultato finale.

---
### 📐 9. GENERALIZZAZIONE A MATRICI RETTANGOLARI

- Si sostituisce l'unico parametro `Width` con tre parametri:
  - `j` = numero di righe di M (e di P)
  - `k` = numero di colonne di M (e righe di N)
  - `l` = numero di colonne di N (e di P)
- Tutti gli indici e i controlli vanno adattati di conseguenza (es. `Row * k + ...` per M, `Row * l + Col` per P).

---
### 💡 10. LINEE GUIDA PER IL TILING

- **Scegli TILE_WIDTH** in base alla GPU e alla dimensione del problema:
  - `16` → buon compromesso tra riuso dei dati e occupancy.
  - `32` → massimo riuso, ma attenzione alla shared memory e al limite di 1024 thread per blocco.
- **Usa `ceil()` per il numero di blocchi**: `dim3 dimGrid(ceil(l / TILE_WIDTH), ceil(j / TILE_WIDTH))`.
- **Usa sempre i controlli sui bordi** per rendere il codice robusto e portabile.
- **Profilare** per trovare la configurazione ottimale (Nsight Compute, nvprof).

---
### ✅ Esempio: Codice Completo e Corretto per Tiled Matrix Multiplication (Caso di matrici Rettangolari)

```cpp
// Kernel per moltiplicazione di matrici rettangolari con TILING
// M: j x k
// N: k x l
// P: j x l
__global__ void MatrixMulKernel(float* M, float* N, float* P, int j, int k, int l) {
    // Shared memory per i tiles
    __shared__ float Mds[TILE_WIDTH][TILE_WIDTH];
    __shared__ float Nds[TILE_WIDTH][TILE_WIDTH];

    int bx = blockIdx.x;
    int by = blockIdx.y;
    int tx = threadIdx.x;
    int ty = threadIdx.y;

    // Coordinate globali del thread
    int Row = by * TILE_WIDTH + ty;   // Riga di P (e di M)
    int Col = bx * TILE_WIDTH + tx;   // Colonna di P (e di N)

    float Pvalue = 0.0f;

    // Numero di fasi (tiles) necessarie per coprire la dimensione k
    int phases = (k + TILE_WIDTH - 1) / TILE_WIDTH;  // ceil(k / TILE_WIDTH)

    // Loop sulle fasi
    for (int ph = 0; ph < phases; ++ph) {
        // 1. CARICAMENTO DEL TILE DI M
        // Ogni thread carica un elemento di M nella shared memory
        // Condizione: la riga Row deve esistere (Row < j) e la colonna ph*TILE_WIDTH+tx deve esistere (colonna < k)
        if (Row < j && ph * TILE_WIDTH + tx < k) {
            Mds[ty][tx] = M[Row * k + ph * TILE_WIDTH + tx];
        } else {
            Mds[ty][tx] = 0.0f;  // Fuori dai bordi: metto 0
        }

        // 2. CARICAMENTO DEL TILE DI N
        // Ogni thread carica un elemento di N nella shared memory
        // Condizione: la riga ph*TILE_WIDTH+ty deve esistere (riga < k) e la colonna Col deve esistere (Col < l)
        if (ph * TILE_WIDTH + ty < k && Col < l) {
            Nds[ty][tx] = N[(ph * TILE_WIDTH + ty) * l + Col];
        } else {
            Nds[ty][tx] = 0.0f;  // Fuori dai bordi: metto 0
        }

        __syncthreads();  // BARRIERA: assicura che tutti i thread abbiano caricato i dati

        // 3. CALCOLO DEL PRODOTTO SCALARE PARZIALE
        // Ogni thread usa i dati in shared memory per calcolare il contributo di questo tile
        for (int i = 0; i < TILE_WIDTH; ++i) {
            Pvalue += Mds[ty][i] * Nds[i][tx];
        }

        __syncthreads();  // BARRIERA: assicura che tutti i thread abbiano finito di usare i dati
    }

    // 4. SCRITTURA DEL RISULTATO FINALE
    // Solo se il thread calcola un elemento valido di P (Row < j e Col < l)
    if (Row < j && Col < l) {
        P[Row * l + Col] = Pvalue;
    }
}
```

---
#### 📌 Come si lancia il kernel

```cpp
// Esempio: M 128x64, N 64x32 → P 128x32
int j = 128;   // righe di M e di P
int k = 64;    // colonne di M e righe di N
int l = 32;    // colonne di N e di P

// Dimensione del blocco (TILE_WIDTH)
// Deve essere scelto in base alla GPU e al problema
#define TILE_WIDTH 16  // 16x16 = 256 thread per blocco

// Dimensione del grid (numero di blocchi)
dim3 dimBlock(TILE_WIDTH, TILE_WIDTH);                 // 16x16 thread
dim3 dimGrid(ceil(l / (float)TILE_WIDTH), ceil(j / (float)TILE_WIDTH));  // colonne di P / TILE_WIDTH, righe di P / TILE_WIDTH

// Allocazione e copia dei dati (non mostrato per brevità)
// cudaMalloc, cudaMemcpy, ecc.

// Lancio del kernel
MatrixMulKernel<<<dimGrid, dimBlock>>>(d_M, d_N, d_P, j, k, l);

// Sincronizzazione e copia dei risultati
cudaDeviceSynchronize();
cudaMemcpy(h_P, d_P, j * l * sizeof(float), cudaMemcpyDeviceToHost);
```

---

## 12_cuda_4

---
### 🧠 1. MEMORY BANDWIDTH E DRAM BURSTING

- **Global memory (VRAM)** è il collo di bottiglia principale delle performance. Un accesso alla DRAM richiede **10-100 ns**, mentre un ciclo di clock della GPU è ~0.5-1 ns → **1 accesso = 10-100 cicli di clock**!
- **DRAM bursting**: quando si accede a una locazione di memoria, la DRAM legge **un blocco di locazioni consecutive** (es. 128 byte). Questo perché leggere più locazioni consecutive è quasi veloce come leggerne una sola.
- Se gli accessi non sono a locazioni consecutive, alcuni byte trasferiti vengono **scartati** → bandwidth sprecata.

---
### 🔗 2. ACCESSO COALESCENTE (FONDAMENTALE!)

- **Coalescing**: se i 32 thread di un warp accedono a **indirizzi consecutivi** (es. N, N+1, N+2, ...), l'hardware combina tutti questi accessi in **una singola richiesta** alla DRAM.
- **Vantaggio**: 1 richiesta invece di 32 → **bandwidth saturata**.
- **Regola per accesso coalescente**: l'indice dell'array deve essere della forma:
  ```cpp
  A[qualcosa_di_costante + threadIdx.x]
  ```
  - ✅ `A[col * Width + threadIdx.x]` → coalescente
  - ❌ `A[threadIdx.y * Width + threadIdx.x]` → non coalescente (salta di Width)

- **Accesso perfettamente coalescente**: tutti i thread del warp accedono a locazioni **nella stessa sezione di burst** → 1 DRAM request, 100% bandwidth.
- **Accesso non coalescente**: gli accessi sono sparsi su più sezioni di burst → multiple DRAM request, bandwidth ridotta.

---
### 📊 3. ACCESSI NELLA MOLTIPLICAZIONE DI MATRICI (NAIVE)

Nel kernel naive:
```cpp
for (int i = 0; i < Width; ++i) {
    Pvalue += A[Row * Width + i] * B[i * Width + Col];
}
```

| Matrice | Accesso | Coalescente? | Perché? |
|---------|---------|--------------|---------|
| **A (prima)** | `A[Row * Width + i]` | ❌ **No** (broadcast) | `i` è costante per tutti i thread del warp → tutti leggono lo stesso elemento |
| **B (seconda)** | `B[i * Width + Col]` | ✅ **Sì** | `Col` varia con `threadIdx.x` → accessi consecutivi |

---
### 🔄 4. CORNER TURNING (CON SHARED MEMORY)

- **Problema**: alcuni algoritmi richiedono di iterare lungo le **colonne** (accesso non coalescente).
- **Soluzione**: usare la **shared memory** per "girare l'angolo" (corner turning).
- **Corner turning**: caricare i dati nella shared memory in un orientamento (es. per righe) e accedervi in un altro orientamento (es. per colonne).
- **Vantaggio**: una volta che i dati sono nella shared memory (veloce), il pattern di accesso non è più un problema → si può accedere per righe o per colonne senza penalità.

---
### 🧩 5. TILING E COALESCING (VANTAGGI DEL TILING)

Il **tiling** (visto nel file precedente) ha **due vantaggi**:
1. **Riduzione dei caricamenti**: i dati vengono caricati una sola volta e riutilizzati (riduce il traffico verso la global memory).
2. **Accessi coalescenti**: **entrambi** gli accessi (M e N) sono coalescenti!

**Nel kernel tiled:**
- **M (prima matrice)**: `M[Row * Width + ph * TILE_WIDTH + tx]` → `tx` varia → **coalescente**.
- **N (seconda matrice)**: `N[(ph * TILE_WIDTH + ty) * Width + Col]` → `Col` varia con `tx` → **coalescente**.

---
### 🧮 6. STRIDED MEMORY ACCESS

- **Strided access**: quando i thread accedono a locazioni con un **passo (stride)** maggiore di 1.
- **Esempio**: `xid = (blockIdx.x * blockDim.x + threadIdx.x) * STRIDE`
  - Thread 0 → indirizzo 0
  - Thread 1 → indirizzo `STRIDE`
  - Thread 2 → indirizzo `2*STRIDE`
  - Se `STRIDE > 1`, gli accessi **non sono coalescenti**!
- **Conseguenza**: performance pessime (no coalescing, no L2 caching efficiente).

---
### 🏗️ 7. AoS vs SoA (STRUTTURE DATI)

- **AoS (Array of Structures)**:
  ```cpp
  struct point { float x, y, z; };
  struct point d_points[n];
  ```
  - Accesso a `x`, `y`, `z` → **stridato** (distanza 3) → **non coalescente**.

- **SoA (Structure of Arrays)**:
  ```cpp
  struct point { float x[n], y[n], z[n]; };
  struct point d_points;
  ```
  - Accesso a `x`, `y`, `z` → **coalescente** (distanza 1).

- **Morale**: preferire **SoA** rispetto ad **AoS** per avere accesso coalescente.

---
### 🏦 8. MEMORY PARALLELISM (BANKS E CHANNELS)

- La DRAM moderna usa **parallelismo** a più livelli:
  - **Bursting**: legge più locazioni consecutive.
  - **Banks**: più banchi di memoria possono essere accessati in parallelo.
  - **Channels**: più canali di memoria (controller) possono operare in parallelo.
- **Per saturare la bandwidth**: servono **abbastanza thread** che facciano accessi simultanei.
- **Interleaving**: distribuisce i dati sui diversi banchi e canali per massimizzare il parallelismo.

---
### ⚠️ 9. DIVERGENZA (WARP DIVERGENCE)

- **Dentro un warp**: SIMD (stessa istruzione, stessi dati diversi).
- **Fuori da un warp**: SIMT (i thread possono divergere, ma con costi).
- **Divergenza**: se i thread di un warp prendono percorsi diversi (if/else), il warp esegue i percorsi in **sequenza** → perdita di performance.
- **Ideale**: evitare codice condizionale basato su `threadIdx` (che causa divergenza).
- **Esempio di divergenza**:
  ```cpp
  if (threadIdx.x % 2) { ... } else { ... }  // ❌ metà warp diverge
  ```
- **Esempio senza divergenza**:
  ```cpp
  if (blockIdx.x % 2) { ... } else { ... }  // ✅ tutto il warp esegue lo stesso ramo
  ```
- **Strategia per casi reali**: se alcuni elementi richiedono elaborazione costosa, prima costruisci due liste (semplici/costosi) e poi processale separatamente.

---
### 🌊 10. CUDA STREAMS E OVERLAPPING

- **Stream**: sequenza di operazioni (kernel, memcpy) eseguite sulla GPU **in ordine**.
- **Operazioni in stream diversi**: possono essere eseguite **in parallelo** (se non ci sono dipendenze).
- **Default stream (stream 0)**: usato se non si specifica uno stream.
- **Da CUDA 7**: ogni thread host ha il suo **per-thread default stream** (attivare con `nvcc --default-stream per-thread`).

---
### 📦 11. ASYNC MEMORY COPY

- **Async memory copy** richiede **pinned memory** (memoria host bloccata, non swappabile):
  ```cpp
  cudaMallocHost(&host_ptr, size);          // pinned memory
  cudaMemcpyAsync(dev_ptr, host_ptr, size, H2D, stream);
  ```
- **Vantaggio**: la copia può essere eseguita **in parallelo** con i kernel (overlap).

---
### 🔄 12. OVERLAPPING (SOVRAPPOSIZIONE)

- **Obiettivo**: trasferire dati CPU→GPU mentre la GPU calcola → nascondere la latenza del trasferimento.
- **Limite**: c'è un solo bus PCIe, quindi non si possono avere due trasferimenti in parallelo sulla stessa GPU.
- **Strategia**: dividere i dati in **chunk**:
  - Chunk 0: trasferimento → kernel → risultato
  - Chunk 1: trasferimento → kernel → risultato
  - Sovrapporre il trasferimento del chunk `i+1` con il calcolo del chunk `i`.
- **Da compute capability 3.5** (Kepler): GPU con **code hardware multiple** → semplificano l'esecuzione di più kernel in parallelo.

---

## 13_cuda_5

---
### 🔐 1. ATOMIC OPERATIONS

- **Definizione**: Operazioni di lettura-modifica-scrittura eseguite come un'unica istruzione hardware su una locazione di memoria (garantiscono che nessun altro thread interferisca fino al completamento).
- **Serializzazione**: Tutti i thread che accedono alla stessa locazione eseguono le operazioni in **seriale** → collo di bottiglia se molti thread competono.
- **Disponibilità**: Operano su parole da 32/64 bit in **global o shared memory**. Utilizzabili **solo in funzioni device**.
- **Funzioni principali**: `atomicAdd()`, `atomicSub()`, `atomicInc()`, `atomicDec()`, `atomicMin()`, `atomicMax()`, `atomicExch()`, `atomicCAS()`, `atomicAnd()`, `atomicOr()`, `atomicXor()`.
- **`atomicCAS` (Compare-And-Swap)**: La più potente. Legge `old` da `address`, se `old == compare` scrive `val`, altrimenti lascia invariato. Restituisce `old`.
- **Implementazione di altre atomiche**: Qualsiasi operazione atomica può essere implementata con `atomicCAS` (es. `atomicAdd` per `double` su GPU pre-Volta).
- **Performance**: Con latenza di 200 cicli → solo ~2.5M atomics/s (vs GFlops della GPU). Le GPU moderne permettono atomiche in **L2 cache** per ridurre la latenza.

---
### 🚫 2. CRITICAL SECTION E DEADLOCK

- **Lock con atomiche**: Si usa `atomicCAS` per implementare uno spin-lock.
- **Deadlock nei warp**: Se tutti i thread di un warp cercano di acquisire lo stesso lock, il warp si blocca (perché è in lockstep). **Soluzione**: usare un loop `while(blocked)` dove ogni thread che non prende il lock continua a iterare.
- **Memory Fence**: `__threadfence()` forza la visibilità di tutte le scritture precedenti a tutti i thread (evita letture di valori stale).
- **Consiglio**: Evitare mutex tra thread dello stesso warp; se necessario, delegare a un singolo thread e usare `__syncthreads()`.

---
### 🧩 3. PRIVATIZZAZIONE

- **Idea**: Replicare strutture dati contese in **copie private** (es. in shared memory) per ridurre la contenzione e la latenza.
- **Vantaggio**: Gli aggiornamenti sulle copie private sono molto più veloci (shared memory).
- **Svantaggio**: Le copie private devono essere **riunite (merge)** nella struttura originale alla fine → costo da bilanciare con il guadagno.
- **Esempio (istogramma)**:
  - Ogni blocco ha una copia privata dei bins in shared memory.
  - Ogni thread aggiorna il suo bin con `atomicAdd` sulla copia privata (contesa ridotta).
  - Alla fine, ogni blocco fa il merge dei suoi bins nella global memory con `atomicAdd`.

---
### 🧮 4. ACCESSO ALLA MEMORIA PER ISTOGRAMMA

- **Sectioned partitioning (cattivo)**: Ogni thread processa una sezione contigua → thread adiacenti accedono a locazioni non adiacenti → **non coalescente**.
- **Interleaved partitioning (buono)**: Tutti i thread processano elementi intervallati (`i += stride`) → thread adiacenti accedono a locazioni consecutive → **coalescente**.
- **Stride pattern**: `int stride = blockDim.x * gridDim.x; while (i < size) { ... i += stride; }`

---
### 🧵 5. CONVOLUTION (STENCIL)

- **Definizione**: Ogni output è una somma pesata di un intorno di input (maschera).
- **Boundary (ghost cells)**: Elementi fuori dai bordi → zero padding (o altre politiche).
- **Kernel naive**: Ogni output usa `Mask_Width` accessi alla global memory → **memory-bound**.
- **Ottimizzazioni**:
  - **Shared memory (tiling)**: Caricare l'input tile una volta e riutilizzarlo.
  - **Constant memory per la maschera**: La maschera è piccola e non cambia → `__constant__` con `cudaMemcpyToSymbol`.

---
### 🧩 6. TILING PER CONVOLUTION (1D)

- **Output tile**: `O_TILE_WIDTH` elementi calcolati da un blocco.
- **Input tile**: `O_TILE_WIDTH + Mask_Width - 1` elementi necessari (perché ogni output usa `Mask_Width` input e c'è overlap).
- **Due design**:
  - **Block size = output tile**: Tutti i thread calcolano output, ma alcuni caricano più input.
  - **Block size = input tile**: Ogni thread carica un input, ma alcuni non calcolano output.
- **Regola**: `BLOCK_WIDTH = O_TILE_WIDTH + Mask_Width - 1`.
- **Riuso dei dati**: Elementi centrali dell'input tile riusati fino a `Mask_Width` volte.

---
### 📊 7. VALUTAZIONE DEL TILING (RIDUZIONE BANDWIDTH)

- **1D convolution**:
  - Accessi senza tiling: `O_TILE_WIDTH × Mask_Width`
  - Accessi con tiling: `O_TILE_WIDTH + Mask_Width - 1`
  - **Fattore di riduzione**: `(O_TILE_WIDTH × Mask_Width) / (O_TILE_WIDTH + Mask_Width - 1)`
  - Esempi: `O_TILE_WIDTH=128, Mask_Width=5` → **4.9×**; `Mask_Width=9` → **8.5×**
- **2D convolution**:
  - Input tile: `(O_TILE_WIDTH + Mask_Width - 1)²`
  - Accessi senza tiling: `O_TILE_WIDTH² × Mask_Width²`
  - **Fattore di riduzione**: `O_TILE_WIDTH² × Mask_Width² / (O_TILE_WIDTH + Mask_Width - 1)²`
  - Esempi: `O_TILE_WIDTH=64, Mask_Width=5` → **22×**; `Mask_Width=9` → **64×**
- **Morale**: Tile più grandi danno maggior riduzione, ma richiedono più shared memory.

---
### 📦 8. PATTERN: MAP, GATHER, SCATTER

- **Map**: Applica una funzione `f` a ogni elemento di un input → output 1:1. Esempio: somma vettoriale.
- **Gather**: Legge da **più input** (con accesso sequenziale o random) e scrive un output coalescente.
- **Scatter**: Legge da un singolo input e scrive su **uno o più output**. Può usare `atomicAdd` se ci sono collisioni in scrittura.

---
### 🌳 9. REDUCTION

- **Definizione**: Operazione associativa che riduce `N` elementi a 1 (es. somma, max, min).
- **Algoritmo ad albero**: Ogni passo riduce i dati della metà → `log2(N)` passi.
- **Sfida in CUDA**: Nessuna sincronizzazione globale → bisogna dividere in fasi (kernel separati).
- **Kernel naive (con divergenza)**:
  ```cpp
  for (stride = 1; stride <= blockDim.x; stride *= 2) {
      if (t % stride == 0) partialSum[2*t] += partialSum[2*t+stride];
  }
  ```
  **Problema**: `if (t % stride == 0)` causa **alta divergenza** (metà thread inattivi dopo il primo passo).
- **Kernel migliorato (thread consecutivi)**:
  ```cpp
  for (stride = blockDim.x; stride > 0; stride /= 2) {
      if (t < stride) partialSum[t] += partialSum[t + stride];
  }
  ```
  **Vantaggi**: Thread attivi consecutivi; nessuna divergenza per `stride >= 32` (warp pieni).
- **Ulteriori ottimizzazioni**: Loop unrolling, addizione iniziale durante il caricamento.

---
### 📈 10. SCAN (PREFIX SUM)

- **Definizione**: Calcola tutte le riduzioni parziali di un array. Esempio: `[1,2,3,4]` → `[1,3,6,10]`
- **Serial scan**: `O(N)` operazioni (efficiente).
- **Parallel scan naive**: `O(N * log2(N))` → **non work-efficient**.
- **Algoritmo a due fasi (balanced tree)**:
  1. **Reduction phase (bottom-up)**: Costruisce somme parziali sui nodi interni.
  2. **Reverse phase (top-down)**: Propaga i valori per calcolare i prefix.
- **Kernel naive (non work-efficient)**:
  ```cpp
  for (stride = 1; stride < blockDim.x; stride *= 2) {
      if (threadIdx.x >= stride) XY[threadIdx.x] += XY[threadIdx.x - stride];
  }
  ```
  **Problema**: Troppe operazioni duplicate (`n * log2(n)`).
- **Usi dello scan**: Assegnazione lavoro, radix sort, stream compaction, valutazione polinomi, ecc.

---

## 14_cuda_6 + CNN

---
### 📦 1. 2D CONVOLUTION CON 2-BATCH LOADING (FILE 14)

- **Definizione**: Tecnica per caricare in shared memory più elementi di quanti siano i thread nel blocco (input tile più grande del blocco).
- **Perché serve**: L'input tile per la convolution 2D è `(TILE_WIDTH + Mask_Width - 1)²`. Questo è tipicamente più grande del numero di thread (`TILE_WIDTH²`).
- **Due batch**:
  - **Primo batch**: Ogni thread carica un elemento (da 0 a `TILE_WIDTH² - 1`).
  - **Secondo batch**: Solo un sottoinsieme di thread carica gli elementi rimanenti (offset di `TILE_WIDTH²`).
- **Parametri**:
  ```cpp
  #define TILE_WIDTH 16
  #define Mask_width 5
  #define w (TILE_WIDTH + Mask_width - 1)  // = 20
  ```
- **Calcolo delle coordinate**:
  ```cpp
  dest = threadIdx.y * TILE_WIDTH + threadIdx.x;
  destY = dest / w;
  destX = dest % w;
  srcY = blockIdx.y * TILE_WIDTH + destY - Mask_radius;
  srcX = blockIdx.x * TILE_WIDTH + destX - Mask_radius;
  ```
- **Ghost cells**: Elementi di input "presi in prestito" dai tile vicini (o zero padding se ai bordi dell'immagine).
- **Numero di thread nel secondo batch**: Non tutti i 256 thread partecipano. Solo quelli con `destY < w` (145 su 256 nell'esempio).
- **Constant memory per la maschera**: La maschera è `const __restrict__` per essere cacheata in constant memory (broadcast a tutti i thread del warp).
- **Pitch**: Allineamento delle righe ai confini di DRAM burst per migliorare l'accesso coalescente. Si usa `cudaMallocPitch()`.

---
### 🧠 2. CNN E PARALLELIZZAZIONE (FILE 15)

#### 2.1 Architettura e Forward Path
- **CNN**: Composte da layer convolutivi, pooling e fully connected.
- **Input**: `X[N, C, H, W]` (mini-batch, canali, altezza, larghezza).
- **Output**: `Y[N, M, Ho, Wo]` (mini-batch, filtri output, altezza output, larghezza output).
- **Filtri**: `W[M, C, K, K]` (output channels, input channels, kernel size).
- **Forward path**: `Y = W * X` (convoluzione 3D per ogni filtro di output).
- **Pooling**: Riduce dimensione spaziale (max o average pooling). Numero di feature maps invariato.

#### 2.2 Backward Path (Training)
- **Backpropagation**: Si calcola il gradiente della loss rispetto ai pesi (`dE/dW`) e lo si propaga verso l'input (`dE/dX`).
- **dE/dX**: Convoluzione del gradiente `dE/dY` con i pesi trasposti (`W^T`).
- **dE/dW**: Gradiente dei pesi per aggiornarli durante la discesa del gradiente.

---
### 🏗️ 3. PARALLELIZZAZIONE CUDA PER CNN

#### 3.1 Mapping Grid-Block-Thread
- **Ogni thread** calcola **un pixel** di **una feature map** di output.
- **Ogni blocco** calcola un tile `TILE_WIDTH × TILE_WIDTH` di una feature map.
- **Grid 3D**:
  - `blockIdx.x` → **N** (campione nel mini-batch)
  - `blockIdx.y` → **M** (feature map di output)
  - `blockIdx.z` → **posizione del tile** nella feature map (comprime `H` e `W`)

#### 3.2 Calcolo delle coordinate

```cpp
W_grid = W_out / TILE_WIDTH;   // tile orizzontali per mappa
H_grid = H_out / TILE_WIDTH;   // tile verticali per mappa
Z = H_grid * W_grid;           // tile totali per mappa

dim3 gridDim(N, M, Z);
dim3 blockDim(TILE_WIDTH, TILE_WIDTH, 1);

// Coordinate output:
n = blockIdx.x;
m = blockIdx.y;
h = (blockIdx.z / W_grid) * TILE_WIDTH + threadIdx.y;
w = (blockIdx.z % W_grid) * TILE_WIDTH + threadIdx.x;
```

#### 3.3 Tiling con Shared Memory

- **Input tile** in shared memory: `X_shared[(TILE_WIDTH + K - 1)²]`
- **Filtri** in shared memory: `W_shared[K × K]`
- **Allocazione dinamica**: `shmem_size = (TILE_WIDTH + K - 1)² + K²`
- **Caricamento**:
  1. Ogni thread carica un elemento del filtro in `W_shared` (se dentro `K`).
  2. Ogni thread carica un elemento dell'input tile in `X_shared`.
  3. `__syncthreads()` per sincronizzare.
  4. Calcolo della convoluzione (loop su `K × K`).
  5. `__syncthreads()` per sincronizzare prima del prossimo canale.

---
### ⚙️ 4. OTTIMIZZAZIONI AVANZATE

#### 4.1 im2col + GEMM

- **Convolution → Matrix Multiplication**: Si "unrolla" l'input in colonne (im2col) e i filtri in righe.
- **Espansione della memoria**: im2col richiede `K × K` volte più memoria (duplicazione dei pixel).
- **Vantaggio**: La moltiplicazione di matrici (GEMM) è altamente ottimizzata su GPU (cuBLAS).
- **CuDNN**: Libreria NVIDIA che implementa questa trasformazione in modo efficiente, con caricamento lazy e tiling.
#### 4.2 Stride (passo)

- **Definizione**: Quanti pixel il filtro si sposta tra un calcolo e l'altro.
- **Vertical stride (`u`)**: Passo in altezza.
- **Horizontal stride (`v`)**: Passo in larghezza.
- **Formula output**:
  ```
  H_out = floor((H - K + 2*pad_h) / u) + 1
  W_out = floor((W - K + 2*pad_w) / v) + 1
  ```
- **Stride > 1** → output più piccolo, meno calcoli, campo recettivo più ampio.

#### 4.3 Padding (ghost cells)

- **Zero padding**: Aggiunge zeri ai bordi per mantenere la dimensione dell'output.
- **Valid convolution**: Nessun padding → output più piccolo.
- **Same convolution**: Padding tale che output = input (stride = 1).

---

## 16_Cuda_7_librerie

---
### 📚 1. INTRODUZIONE (PERCHÉ USARE LE LIBRERIE)

- Le librerie **incapsulano la complessità** di scrivere codice ottimizzato per algoritmi comuni, fornendo interfacce standard e di alto livello.
- Offrono **prestazioni elevate** perché le implementazioni sono curate direttamente da NVIDIA.
- Esempi di librerie NVIDIA: **Thrust**, **cuBLAS**, **cuDNN**, **cuFFT**, **cuRAND**, **NVIDIA libc++**.

---
### 🧰 2. THRUST (ALGORITMI STL-LIKE)

- **Thrust** è una libreria template inclusa nel toolkit CUDA, ispirata alla STL del C++.
- Basta includere gli header (`#include <thrust/...>`) per usarla.
- Fornisce algoritmi comuni: `reduce`, `sort`, `scan`, `transform`, `search`, ecc.
- Supporta un **backend OpenMP** per l'esecuzione su CPU multicore.
- Permette un **uso trasparente della GPU**: il programmatore non gestisce manualmente il lancio dei kernel.

### 2.1 Contenitori (host_vector e device_vector)
- `thrust::host_vector<T>` → vettore in memoria **host** (CPU).
- `thrust::device_vector<T>` → vettore in memoria **device** (GPU).
- Entrambi hanno un'interfaccia simile a `std::vector` (`begin()`, `end()`, `push_back()`, `operator[]`, ecc.).

#### 2.2 Iteratori e Raw Pointer
- Gli iteratori Thrust possono essere convertiti in **raw pointer** per interfacciarsi con kernel CUDA:
  ```cpp
  int* d_ptr = thrust::raw_pointer_cast(d_vec.begin());
  ```
- Anche i raw pointer allocati con `cudaMalloc` possono essere "wrappati" in iteratori Thrust:
  ```cpp
  thrust::device_ptr<int> d_vec = thrust::device_pointer_cast(d_ptr);
  ```

#### 2.3 Esempi di Utilizzo
- **Ordinamento**: `thrust::sort(d_vec.begin(), d_vec.end());`
- **Riduzione** (somma): `int x = thrust::reduce(d_vec.begin(), d_vec.end(), 0, thrust::plus<int>());`

---
### 🧮 3. CUBLAS (ALGEBRA LINEARE)

- **cuBLAS** è l'implementazione GPU-accelerata delle **Basic Linear Algebra Subprograms (BLAS)**.
- Si include con `#include <cublas.h>` (o `cublas_v2.h`) e si linka con `-lcublas`.
- **Attenzione al layout dei dati**: cuBLAS usa il **column-major storage** e **1-based indexing** (eredità Fortran).
- Per C/C++ (0-based) si usa la macro:
  ```cpp
  #define IDX2C(i, j, ld) ((j) * (ld) + (i))
  ```
  dove `ld` (leading dimension) è il numero di righe della matrice.

#### 3.1 Esempio: SAXPY (A*X + Y)
- `cublasInit()` → inizializza il contesto.
- `cublasSetVector()` → copia dati host → device.
- `cublasSaxpy(N, alpha, d_x, 1, d_y, 1)` → esegue `y = alpha * x + y` sulla GPU.
- `cublasGetVector()` → copia dati device → host.
- `cublasShutdown()` → termina il contesto.

---
### ⚡ 4. FAST MATH (OTTIMIZZAZIONI MATEMATICHE)

- Opzione del compilatore **`-use_fast_math`**: forza l'uso di funzioni matematiche **intrinseche** (più veloci, ma meno precise) per operazioni come divisioni, `log`, `exp`, `sin`, `cos`, `tan`.
- Funziona **solo per il codice device** (GPU).
- Opera in **singola precisione**: può essere meno preciso rispetto al doppio.

---
### 🖥️ 5. C++ E NVIDIA LIBC++ (STANDARD LIBRARY PER DEVICE)
#### 5.1 Supporto C++ nelle GPU
- Da CUDA 7.0: supporto a **C++11** (`auto`, lambda, `nullptr`, move semantics, ecc.).
- Da CUDA 9.0: supporto quasi completo a **C++14**.
- **Mancanza**: le funzionalità di concorrenza C++11 (`std::thread`, ecc.) **non sono supportate** in device code.

#### 5.2 NVIDIA libc++ (libcu++)
- **Obiettivo**: fornire un'implementazione eterogenea della C++ Standard Library che funzioni **sia su CPU che su GPU**.
- Si include con `#include <cuda/std/...>` e si usa il namespace `cuda::std`.
- Attualmente supporta un **sottoinsieme** della libreria standard (sincronizzazione, time, utilities).
#### 5.3 Namespace
| Namespace | Utilizzo |
|-----------|----------|
| `std::` | Solo per codice **host** (CPU) |
| `cuda::std::` | **Host e device**, conforme allo standard C++ |
| `cuda::` | **Host e device**, estensioni NVIDIA |
| `cuda::device` | **Solo device**, estensioni NVIDIA |
#### 5.4 Esempio di Atomic con Scope
```cpp
#include <cuda/atomic>
cuda::atomic<int, cuda::thread_scope_block> x;
```
Permette di specificare lo **scope** delle operazioni atomiche (es. `thread_scope_block`, `thread_scope_device`).

---
