# Introduzione al corso - Ingegneria del Software per Sistemi Embedded

**Ingegneria del Software per Sistemi Embedded**  
**Introduzione al corso**

Laura Carnevali  
Laboratorio di Tecnologie Software  
Dipartimento di Ingegneria dell’Informazione  
Università di Firenze

[http://stlab.dinfo.unifi.it/carnevali](http://stlab.dinfo.unifi.it/carnevali)  
[laura.carnevali@unifi.it](mailto:laura.carnevali@unifi.it)

---

**Struttura del corso**

1. Crediti
2. Contenuti del corso
3. Organizzazione del corso

---

## Crediti

- Gran parte del materiale presentato in queste slide è tratto da:
    
    - Le slide del corso “Real-Time Systems” tenuto dal Prof. Giorgio Buttazzo:  
        [http://retis.sssup.it/~giorgio/rts-MECS.html](http://retis.sssup.it/~giorgio/rts-MECS.html)
    - Le slide del corso “Real-Time Systems” tenuto dal Prof. Tullio Vardanega:  
        [https://www.math.unipd.it/~tullio/RTS/2019](https://www.math.unipd.it/~tullio/RTS/2019)
- Queste slide sono autorizzate solo per uso personale.
    
- Qualsiasi altro uso, redistribuzione o vendita a scopo di lucro delle slide (in qualsiasi forma) richiede il consenso dei titolari del copyright.
    

---

## Contenuti del corso

**Il corso tratta** di:

- Progettazione, implementazione e testing del **software embedded**
	- Cos’è un sistema embedded?
	- Dove viene utilizzato il software embedded?
	- Quali sono le sfide nella progettazione software?
	- Quali sono le linee guida per la programmazione e l’implementazione del software?
	- Quali sono le strategie per il testing del software?

---

**Sistemi Embedded**

- Un **sistema embedded** è un sistema di elaborazione dedicato progettato per funzioni specifiche all'interno di un sistema più grande, spesso con vincoli di elaborazione in tempo reale.
	- Possono essere **autonomi, in rete, mobili o real-time**.
	- Sono dotati di **microcontrollori, microprocessori o chip progettati su misura**.
	- Possono includere **interfacce utente, anche complesse e grafiche**.

**Sistemi embedded vs sistemi generici**

- **Sistemi embedded**: progettati per uno scopo specifico o per pochi scopi.
- **Sistemi generici**: progettati per molteplici utilizzi.

**Sistemi embedded vs sistemi cyber-fisici**

- **Sistemi embedded**: essenzialmente **chiusi**.
- **Sistemi cyber-fisici**: essenzialmente **aperti**.

![[Pasted image 20250306184601.png]]

---

**Sistemi embedded in tempo reale**

- Un **sistema in tempo reale** è un sistema informatico soggetto a **vincoli temporali**.
	- **I tempi di risposta e l’interferenza tra i task devono essere limitati in tutti gli scenari**.
	- Il **tempo** non è un attributo intrinseco, ma dipende strettamente dall’ambiente.

- Il **rispetto dei vincoli temporali deve essere dimostrato**.

- La correttezza dipende sia dal **risultato logico** (correttezza funzionale) sia dal **tempo in cui il risultato è prodotto** (correttezza non funzionale).
	- **Una risposta tardiva, anche se logicamente corretta, può essere dannosa quanto una risposta errata**.

- Un sistema in tempo reale è tipicamente **incorporato** in un sistema più grande per:
    - **Controllarne le funzioni**
    - **Gestire le risorse disponibili**
    - **Semplificare l’interazione con l’utente**

![[Pasted image 20250306184843.png]]

---

**Un po’ di storia sui sistemi embedded (1/3)**

- **Primi anni ‘60**: **Apollo Guidance Computer** (MIT Instrumentation Lab)
    - **Primo sistema embedded in tempo reale** usato per guida, navigazione e controllo delle missioni Apollo.
    - Uno dei **primi computer con circuiti integrati**.
    - Uso di **simulatori software e hardware per la verifica e la validazione**.
![[Pasted image 20250306185021.png]]

---

**Un po’ di storia sui sistemi embedded (2/3)**

- **Metà anni ‘60**: sistemi di guida missilistica (Autonetics, ora Boeing)
    - **D-17B**: primo sistema embedded prodotto su larga scala.
    - **NS-17**: primo sistema embedded con un uso massiccio di circuiti integrati.
- **Fine anni ‘60**: **microprocessore per il controllo dell'iniezione elettronica di carburante** (Bosch)
    - Primo sistema embedded nel settore **automobilistico**.

![[Pasted image 20250306185117.png]]

---

**Un po’ di storia sui sistemi embedded (3/3)**

- **Fine anni ‘60 - inizio anni ‘70**: **Calo del costo dei circuiti integrati**, maggiore diffusione.
    - **TMS1000** (Texas Instruments): primo microcontrollore commerciale.
    - **Intel 4004**: primo microprocessore commerciale.

- **Anni ‘80 e ‘90**:
    - **VxWorks**: primo sistema operativo embedded real-time (WindRiver).
    - **Windows Embedded CE**: sistema operativo embedded real-time (Microsoft).
    - **Embedded Linux**: sistemi operativi embedded basati su Linux.
    - **RTLinux**: sistema operativo real-time basato su Linux.

![[Pasted image 20250306185229.png]]

---

**Evoluzione dei sistemi embedded (1/3)**

- **Numero di transistor nei circuiti integrati (1971-2018)**. 

![[Pasted image 20250306185258.png]]

---

 **Evoluzione dei sistemi embedded (2/3)**

- **Numero di dispositivi connessi (1992-2020)**.

![[Pasted image 20250306185621.png]]

---

 **Evoluzione dei sistemi embedded (3/3)**

- **Ricavi globali del mercato dei sistemi embedded (2015-2021)**. ![[Pasted image 20250306185753.png]]

---

**I sistemi embedded sono ovunque**

- **Oggi il 98% dei processori nel mondo è utilizzato nei sistemi embedded**.  Applicazioni in:
    - **Avionica**
    - **Automotive**
    - **Militare e aerospaziale**
    - **Robotica**
    - **Automazione industriale**
    - **Sanità**
    - **Elettronica di consumo**
    - **Telecomunicazioni**
    - **Multimedia**
    - **Sistemi di trasporto intelligenti**
    - ... e molti altri settori.

![[Pasted image 20250306190210.png]]

---

**Aumento della complessità nei sistemi embedded**

- **Numero medio di Unità di Controllo Elettronico (ECU) in un'auto**.
    - Un'auto di lusso moderna può avere fino a **100 ECU**.
![[Pasted image 20250306190232.png]]

---

**Dove viene utilizzato il software embedded?**

- Il **software embedded controlla quasi tutto in un'auto**.
![[Pasted image 20250306190248.png]]

---

**Complessità del software embedded (1/2)**

- **Numero medio di linee di codice (LOC) in un'auto**.

![[Pasted image 20250306190458.png]]

---

 **Complessità del software embedded (2/2)**

- **Confronto della complessità del software**:
    - Le auto sono tra i **sistemi più intensivi dal punto di vista software**.
![[Pasted image 20250306190805.png]]

---

**Cosa rende speciali i sistemi embedded?**

- **Caratteristiche**
	- **Elevata eterogeneità** dei componenti e delle attività di elaborazione.
	- **Alta variabilità** in dimensioni e ambito di applicazione.
	- **Risorse limitate** (spazio, peso, tempo, memoria, energia, ...).
	- **Elevata concorrenza e condivisione delle risorse** (alta interferenza tra i task).
	- **Interazione con l’ambiente**: reattività a eventi esterni e gestione temporale.
	- **Variabilità elevata** nella richiesta di risorse e nel carico di lavoro.

- **Requisiti**
	- **Affidabilità garantita** (sicurezza, disponibilità, manutenzione, ...).
	- **Continuità operativa** senza supervisione umana costante.
	- **Efficienza nella gestione delle risorse**.
	- **Rispetto dei vincoli temporali** e isolamento per limitare le interferenze tra i task.
	- **Alta prevedibilità** nel rispondere a eventi ambientali e temporali.
	- **Adattabilità (robustezza)** per gestire situazioni di sovraccarico.
![[Pasted image 20250306190917.png]]
---

**Fonti di non determinismo nei sistemi embedded (1/2)**

- **Multitasking** (chiamate di sistema per la programmazione concorrente)
    - Può introdurre **ritardi imprevedibili** nell'esecuzione dei task.

- **Scheduling basato sulle priorità**
    - Supporta la gestione avanzata dei task, ma può richiedere **riassegnazione delle priorità** in caso di nuovi task in arrivo.

- **Gestione delle interruzioni esterne**
    - Elevata priorità delle interruzioni rispetto ai task può migliorare la reattività del sistema, ma può anche causare **ritardi imprevedibili**.

- **Accesso diretto alla memoria (DMA)**
    - Il trasferimento dati indipendente dalla CPU può bloccare il processore, causando ritardi non prevedibili.(fenomeno del cycle stealing dove la CPU rimane ferma un numero di cicli indefinito se la DMA eseguo un trasferimento dati)
    - **Metodo time-slice**: riduce l'efficienza ma garantisce una maggiore prevedibilità.

---

**Fonti di non determinismo nei sistemi embedded (2/2)**

- **Cache**
    - Accelera l’esecuzione del processore ma è influenzata dal numero di **preemption**, che distruggono la **località dei dati**.

- **Chiamate di sistema**
    - Devono essere **preemptabili** e avere **tempo di esecuzione limitato**.

- **Meccanismi di comunicazione e sincronizzazione tra task**
    - Se mal gestiti, possono introdurre effetti indesiderati come:
        - **Inversione di priorità**.
        - **Blocchi e deadlock**.

- **Gestione della memoria**
    - L’**allocazione statica** migliora la prevedibilità ma riduce la flessibilità.

- **Kernel leggero e cambio di contesto veloce**
    - Riduce il **tempo medio di risposta**, ma **non garantisce il rispetto dei vincoli temporali**.

- Scarso supporto per le specifiche di vincoli temporali sui tasks.

---

 **Soddisfare i requisiti: miti da sfatare**

- **La programmazione real-time non è empirica**.
    - Le tecniche empiriche possono rendere il comportamento del software **imprevedibile**.

- **La programmazione real-time non è a basso livello**.
    - La programmazione a basso livello è **complicata** e il codice è **difficile da mantenere**.
    - L'uso di linguaggi di alto livello semplifica la **verifica dei requisiti**.

- **Minimizzare il ==tempo medio di risposta== non è sufficiente**.
	- **Aumentare la potenza della CPU non è una soluzione garantita** per i sistemi real-time.
	- **Il real-time computing non è ==sinonimo di velocità di elaborazione**.==

- **Il testing è essenziale, ma non è sufficiente**:
    - Il comportamento del software dipende dai dati di input → il testing fornisce solo una **verifica parziale**.

- **La simulazione hardware/software è utile, ma non basta**.

![[Pasted image 20250306191745.png]]

---

**Soddisfare i requisiti: prevedibilità**

- **La ==prevedibilità== a livello di sistema è essenziale**.
    - Ho necessità di **predire il comportamento dei task e rispettare i vincoli temporali**.

- **Come raggiungere prevedibilità e soddisfare i requisiti?**
    - Servono **nuove soluzioni** per la progettazione e il testing del software.
    - Sono necessari **test di schedulabilità e fattibilità efficienti**.
    - È essenziale **stimare il tempo di esecuzione nel peggior caso (WCET)**.
    - Anche **l’hardware deve essere progettato per migliorare la prevedibilità** (fuori dall'ambito di questo corso).
    - 
![[Pasted image 20250306192253.png]]
---

**Soddisfare i requisiti: la stima del WCET non è facile (1/3)**

- **Stima analitica**:
    - **Limitare il numero di iterazioni dei cicli**.
    - **Calcolare il percorso più lungo**.
    - **Stimare i cache miss massimi**.
    - **Determinare il tempo di esecuzione delle istruzioni più critiche**.

---

**Soddisfare i requisiti: la stima del WCET non è facile (2/3)**

- **Stima basata su misurazioni**:
    - **Eseguire il task più volte con input diversi**.
    - **Raccogliere statistiche sui tempi di esecuzione**.

![[Pasted image 20250306192441.png]]

---

**Soddisfare i requisiti: la stima del WCET non è facile (3/3)**

- **Combinazione di analisi e misurazioni**:
    - **BOET (Best Observed Execution Time)**.
    - **AOET (Average Observed Execution Time)**.
    - **WOET (Worst Observed Execution Time)**.
    - **WCET (Worst Case Execution Time)**.

![[Pasted image 20250306192543.png]]

---

**Soddisfare i requisiti: prevedibilità vs efficienza**

- **Criticità del software embedded (basata sugli effetti di un mancato rispetto della scadenza)**:
    - **Soft**: il mancato rispetto della scadenza riduce le prestazioni.
    - **Firm**: il mancato rispetto della scadenza invalida il task.
    - **Hard**: il mancato rispetto della scadenza può avere effetti **catastrofici**.

![[Pasted image 20250306192729.png]]

---

**Obiettivi del corso**

- Studiare le **metodologie software** che migliorano la **prevedibilità** nei sistemi embedded.
	- Imparare a **modellare applicazioni critiche dal punto di vista temporale** e **analizzarne le proprietà temporali**.
	- Progettare, programmare e testare **applicazioni software con vincoli temporali**.

![[Pasted image 20250306193027.png]]

---

**Panoramica del programma**

- **Parte 1: Sistemi embedded e in tempo reale**
	- **Algoritmi di scheduling per sistemi embedded real-time**:
	    - Concetti di base
	    - Scheduling dei task periodici
	    - Scheduling ciclico esecutivo
	    - Scheduling Rate Monotonic
	    - Scheduling Deadline Monotonic
	    - Scheduling Earliest Deadline First (EDF)

	- **Protocolli di accesso alle risorse nei sistemi embedded real-time**:
	    - Protocollo di ereditarietà delle priorità (Priority Inheritance Protocol)
	    - Protocollo del soffitto delle priorità (Priority Ceiling Protocol)
	    - Test avanzati di schedulabilità

	- **Sistemi operativi real-time e standard**:
	    - RT-POSIX, OSEK/VDX, ARINC-APEX
	    - Il sistema operativo real-time VxWorks
	    - Sviluppo di applicazioni real-time su **Raspberry Pi**

 - **Parte 2: Argomenti avanzati su scheduling e testing**
	- **Analisi avanzata della schedulabilità**:
	    - Reti di Petri (Petri Nets)
	    - Reti di Petri Temporizzate (Time Petri Nets)
	    - Reti di Petri Temporizzate Preemptive (Preemptive Time Petri Nets)
	    - Uso delle reti di Petri nel ciclo di vita del software secondo il **V-Model (MIL-STD-498)**
	    - **Automi temporizzati (Timed Automata)**
	
	- **Testing del software**:
	    - Metodologie di testing
	    - Testing basato sul flusso di controllo e sul flusso di dati
	    - Testing basato sugli automi a stati finiti (Finite State Testing)
	    - Testing real-time

- **Parte 3: Ingegneria dei sistemi**
	- **Elementi di ingegneria dei sistemi basata su modelli (MBSE - Model-Based Systems Engineering)** **SysML (Systems Modeling Language)**

---

## Organizzazione del corso

 **Lezioni**

- **Pagina Moodle del corso**:  
    [https://e-l.unifi.it/course/view.php?id=42580](https://e-l.unifi.it/course/view.php?id=42580)  
    **Password:** SWEES
- **Registrarsi alla pagina del corso per ricevere annunci e aggiornamenti**.
- **Periodo**: Primo semestre (dal **16/09/2024 al 13/12/2024**).
- **Orario delle lezioni**:
    - **Martedì 16:00-18:00**, aula 49, Santa Marta.
    - **Mercoledì 15:00-17:00**, aula 33, Santa Marta.
- **Il calendario delle lezioni sarà confermato settimana per settimana**:
    - **Lezione 1 (17/09/2024)** – Introduzione al corso.
    - **Lezione 2 (18/09/2024)** – Algoritmi di scheduling.
    - **…**
- **Sessioni di laboratorio** con **Dr. Imad Zaza** (da annunciare durante il corso).
- **Disponibilità per incontri con gli studenti**:
    - Domande e richieste di chiarimenti possono essere inviate via email.
    - È possibile fissare incontri in orario di ricevimento o in altri orari su richiesta.

---

**Esame**

- **Valutazione delle competenze teoriche e pratiche** acquisite nel corso.
    
- **Esame di "Software Engineering for Embedded Systems" (6 CFU)**:
    - **Colloquio orale** sui contenuti del corso.
    - **Sviluppo individuale di un assignment (facoltativo)**.

- **Esame di "Software Engineering for Embedded Systems Laboratory" (3 CFU)**:
    
    - Discussione di un assignment relativo agli argomenti del corso.
    - L'**assignment può essere svolto individualmente o in gruppi (2-3 studenti)**.
    - **Il tema è concordato con il docente** (gli studenti possono proporre argomenti).
    - **Date d'esame** disponibili sulla pagina del corso.
    - **Iscrizione all'esame**: [http://sol.unifi.it/prenot/prenot](http://sol.unifi.it/prenot/prenot)

---

**Esame orale con self-assignment (6 CFU)**

- **Lo sviluppo di un self-assignment è facoltativo**.

- Gli studenti che scelgono di svilupparlo devono:
    - **Definire autonomamente il tema**.
    - **Inviare un breve report una settimana prima dell'esame**.
- **Esempi di self-assignment**:
	- **Implementazione di task real-time** con scheduling a priorità fissa preemptiva su **VxWorks**.
	- **Uso di ORIS 1.0 o Uppaal** per verificare i requisiti di un sistema concorrente temporizzato.
	- **Sviluppo di diagrammi SysML** per modellare un sistema embedded.

---

**Project Work (3 CFU)**

- Formare un gruppo di **1-3 studenti** e **concordare il tema via email** prima di iniziare.

- **Presentazione dei risultati durante l’esame**.
	- Ogni studente deve avere un **contributo chiaramente identificabile**.

- **Esempi di assignment**:
	- **Verifica dei requisiti di un task-set real-time** gestito da scheduling a priorità fissa preemptiva.
	- **Sviluppo e testing di un task-set real-time** su **VxWorks**.
	- **Analisi del log temporale** di eventi di un modello PTPN.
	- **Fault injection** e testing di sistemi real-time.

---

**Esempi di progetti passati**: **Real-Time Programming su Linux-RTAI**

- Implementazione e testing di **task-set real-time**:
    - Task periodici e sporadici con risorse in mutua esclusione.
    - **Testing rispetto a un modello formale basato su reti di Petri temporizzate**.

- **RTAI (Real-Time Application Interface for Linux)**.
    - Set di task Real-time sono implementati come moduli Kernel eseguiti su un *Intel NUC NUC10i3FNHN.

![[Pasted image 20250307082401.png]]

---
**Un assignment su generazione e prioritizzazione dei test case**

- Generazione automatica di **test case per sistemi cyber-fisici**
	- Simulazione di **sistemi cyber-physical complessi**.
	- **Uso di algoritmi genetici per la generazione di test reattivi**.

![[Pasted image 20250307082543.png]]

---

**Un assignment su scheduling di grafi di task**

- **Scheduling di task nel settore tessile**:
    - Un grafo di task rappresenta le fasi di lavoro di un "bill of materials" con scadenza.
    - Ogni fase di lavoro è eseguita tramite un sottocontratto su una macchina specifica
    - Ogni istanza della macchina di un certo tipo ha la sua velocità di esecuzione.

- Un algoritmo di scheduling **sequenziale senza prelazione**
	- L'algoritmo schedula un task graph alla volta
	- Si evitano prelazioni del task per costi pratici
	- **Schedulazione con Earliest Deadline First (EDF)** e spinti al massimo senza violare le precedenze 

![[Pasted image 20250307083055.png]]

---
**Altri esempi di temi di assignment**

- **Analisi della schedulabilità** in sistemi real-time. (sistemi di scheduling a gerarchie)

![[Pasted image 20250307083209.png]]

- **Testing di sistemi real-time**.

- **Analisi delle prestazioni nei sistemi ferroviari**.

![[Pasted image 20250307083253.png]]

- **Manutenzione predittiva in sistemi distribuiti**. 
	- **Allocazione delle risorse nei sistemi edge-cloud**.

![[Pasted image 20250307083400.png]]

---

# Concetti di base

## Task (1/2)

- Un task è una sequenza di istruzioni che, in assenza di altre attività, viene eseguita continuamente dal processore fino al completamento.
- Esempio: un singolo task in esecuzione che non subisce preemption.

	 ![[Pasted image 20240923171258.png]]

- Un processo è un programma in esecuzione, composto da task concorrenti (anche detti thread) che condividono uno spazio di memoria comune.
---
## Task (2/2) 

- Caratteristiche del task:
    - **Tempo di attivazione ($a_i$)**: tempo in cui un task diventa pronto per l'esecuzione.
    - **Tempo di inizio ($s_i$)**: tempo in cui un task inizia la sua esecuzione.
    - **Tempo di completamento ($f_i$)**: tempo in cui un task termina la sua esecuzione.
    - **Tempo di calcolo ($C_i$)**: tempo di esecuzione del task senza interruzioni.
    - **Tempo di Completamento** ($K_{i}$): $K_{i} = f_{i} - s_{i}$, nell'esempio coincide con il tempo di calcolo
    - **Tempo di risposta ($R_i$)**: $R_i = f_i - a_i$.
    -
![[Pasted image 20240923171417.png]]
---

## Stati del task

- Un task è **attivo** se può potenzialmente essere eseguito sul processore.
	- Un task attivo è **pronto** se è in attesa del processore.
	- Un task attivo è in **stato running** se è in esecuzione.
- Un task è **bloccato** se è in attesa di utilizzare una risorsa.

![[Pasted image 20240923171513.png]]

---

## Dispatching

- I task pronti sono mantenuti in una coda detta **_ready queue_**, gestita da una politica di **scheduling**.
- Un'operazione di **_dispatching_** assegna il processore al primo task nella coda.
- Se ci sono diversi tipi di task, potrebbero esserci più code pronte.
-![[Pasted image 20240923171944.png]]

---

## Preemption

- Meccanismo del kernel che sospende l'esecuzione del task in esecuzione (che ritorna nella coda dei pronti) a favore di un task più importante.
- Migliora la concorrenza tra i task :)
- Riduce il tempo di risposta dei task ad alta priorità, ma introduce overhead di runtime, sul tempo di esecuzione dei task :(
- Per assicurare task critici può essere disabilitato (temporaneamente o permanentemente)
---

## Schedulazione

- Una schedulazione è un'assegnazione dei task al processore, che determina la sequenza di esecuzione dei task considerati.
- Formalmente, una schedulazione per un insieme di task $\Gamma = {\tau_1, \tau_2, ..., \tau_n}$ è una funzione $\sigma: R+ \to N$, tale che $∀ t ∈ R+ ∃ t1 , t2 ∈ R+$, tale che $t ∈ [t1 , t2)$ e σ(t) = σ(t′ ) ∀ t′ ∈ $[t1 , t2]$  :
	• σ(t) = 0 se il processore è in idle al tempo t
	• σ(t) = k ∈ {1, 2, . . . , n} se il processore esegue il task $τ_k$ al tempo t
- Ogni intervallo $[ti , ti+1 )$, è chiamato _time slice_ $∀ i ∈ N+$
- Ad ogni istante $t_i$, il processore compie un **_context switch_**
	
![[Pasted image 20240923172113.png]]

---

### Schedulazione preemptive

Un'immagine mostra una schedulazione preemptive.
![[Pasted image 20240923172211.png]]

---
### Sistema concorrente

- Più task possono essere attivi simultaneamente (pronti o in esecuzione).
- Uno e solo un task è in esecuzione in un determinato momento.
![[Pasted image 20240923172346.png]]
---

## Task in tempo reale

- Un task in tempo reale è caratterizzato da un vincolo temporale sul tempo di risposta, detto **deadline** (assoluta/relativa).
- **Deadline assoluta ($d_i$)**: tempo entro il quale un task deve completare l'esecuzione.
- **Deadline relativa ($D_i$)**: $D_i = d_i - a_i$.
-![[Pasted image 20240923172414.png]]
- Un task sarà quindi detto **feasible** se completa la sua esecuzione prima della sua deadline assoluta 
	- dunque $f_i ≤ d_i$ oppure $R_i ≤ D_i$
---
### Laxity

- **Laxity $X_i$**: massimo ritardo che un task può subire dopo la sua attivazione, pur completando entro la sua deadline.
- Misurato al tempo di attivazione: $X_i = D_i - C_i$.
- Anche detto "slack time".
-![[Pasted image 20240923172446.png]]
- La **Residual laxity** $Yi$ di un task, è invece la laxity misurata al completamento del task
	- Ovvero uguale alla deadline assoluta meno il finishing time

---
### Lateness e Tardiness

- **Lateness $L_i$**: ritardo del task rispetto alla sua deadline.
	- è negativa se il task finisce prima della sua deadline
-![[Pasted image 20240923172528.png]]
- **Tardiness $E_i$**: tempo in cui un task rimane attivo oltre la sua deadline.
	- Definito come: $E_i = max${$0,L_i$}, 
	- Detto anche _exceeding time_

---

## Task e Job

- Un task che viene eseguito più volte su dati diversi genera una sequenza di attività identiche chiamate **job** o istanze di task.
![[Pasted image 20240923172617.png]]
---

### Modalità di attivazione di un task

- **Modalità di attivazione a tempo**: il task è automaticamente attivato dal sistema operativo in momenti predefiniti.
- **Modalità di attivazione evento**: il task è attivato al verificarsi di un evento, da un interrupt o da un altro task tramite una chiamata di sistema esplicita.
	- Modalità di attivazione dei task **aperiodici**

---

### Task periodico 

- Un **task periodico** $\tau_i$ consiste in una sequenza infinita di job $\tau_{i1}, \tau_{i2}, \dots, \tau_{ik}$, regolarmente attivati con un tasso costante, ossia con periodo $T_i$. 
-  Se $T_i = D_i$, allora l'attività è detta **task periodica pura**.
- Il **fattore di utilizzazione del task** è $U_i := \frac{C_i}{T_i}$.![[Pasted image 20240923172729.png]]
---
#### Task periodico(2/3)

- Parametri di un'attività periodica $\tau_i$
    - **Periodo** $T_i$, tempo di computazione $C_i$, deadline relativa $D_i$.
    - Tempo di attivazione del primo job: $\Phi_i := a_{i,1}$ (detto ***fase*** del task).
    - Tempo di attivazione del k-esimo job con $k > 1$: $a_{i,k} := \Phi_i + (k-1) T_i$.
    - Deadline assoluta del k-esimo lavoro con $k > 1$: $d_{i,k} := a_{i,k} + D_i$.
    
![[Pasted image 20240923173855.png]]

---

#### Task periodico (3/3)

- Supporto per attività periodiche
    - Pseudo-codice che illustra un frammento di una tipica implementazione:
		*wait for activation(); 
		while(condition) {   
			...  
		wait_for_next_period();
		}`

- Nel periodo che va dall'invocazione di *wait_for_next_period()* fino all'inizio del periodo successivo, l'attività non è né attiva né bloccata, è **inattiva**!
- ![[Pasted image 20240923174335.png]]
---

### Stati dei Task

![[Pasted image 20240923174511.png]]

---

### Task aperiodico

- Un task **aperiodico** $\tau_i$ consiste in una sequenza infinita di job $\tau_{i1}, \tau_{i2}, \dots, \tau_{ik}$, che non sono attivati regolarmente.
- Un task **sporadico** $\tau_i$ è un task aperiodico i cui job consecutivi sono separati da un tempo minimo tra arrivi $T_i$. i.e., $a_{i,k+1} ≥ a_{i,k} + T_i$
-![[Pasted image 20240923174605.png]]

---

### Jitter

- Il jitter misura la variazione di un evento periodico.
	- **Jitter assoluto**: $\max_k {t_k - a_k} - \min_k {t_k - a_k}$ (massima differenza tra i tempi di attivazione effettivi e i tempi di attivazione pianificati.)
	- **Jitter relativo**: $\max_k {|(t_k - a_k) - (t_{k-1} - a_{k-1})|}$
![[Pasted image 20240923174623.png]]
---
#### Start time jitter 

- **Jitter assoluto del tempo di inizio**: Deviazione massima del tempo di inizio tra tutti i lavori.
    - $\max_k {s_{i,k} - a_{i,k}} - \min_k {s_{i,k} - a_{i,k}}$
- **Jitter relativo del tempo di inizio**: Deviazione massima del tempo di inizio tra due lavori consecutivi.
    - $\max_k {|(s_{i,k} - a_{i,k}) - (s_{i,k-1} - a_{i,k-1})|}$
    ![[Pasted image 20240923175222.png]]
#### Finishing time jitter 

- **Jitter assoluto del tempo di completamento**: Deviazione massima del tempo di completamento tra tutti i lavori.
    - $\max_k {f_{i,k} - a_{i,k}} - \min_k {f_{i,k} - a_{i,k}}$
- **Jitter relativo del tempo di completamento**: Deviazione massima del tempo di completamento tra due lavori consecutivi.
    - $\max_k {|(f_{i,k} - a_{i,k}) - (f_{i,k-1} - a_{i,k-1})|}$
    ![[Pasted image 20240923175423.png]]
#### Completion time jitter 

- **Jitter assoluto del tempo di completamento**: Deviazione massima del tempo di completamento tra tutti i lavori.
    - $\max_k {f_{i,k} - s_{i,k}} - \min_k {f_{i,k} - s_{i,k}}$
- **Jitter relativo del tempo di completamento**: Deviazione massima del tempo di completamento tra due lavori consecutivi.
    - $\max_k {|(f_{i,k} - s_{i,k}) - (f_{i,k-1} - s_{i,k-1})|}$
    ![[Pasted image 20240923175450.png]]
## Sintesi dei parametri di task

- **Parametri conosciuti offline** (specificati dal programmatore): 
	- periodo $T_i$
	- Tempo di calcolo $C_i$
	- Deadline relativa $D_i$.
- **Parametri conosciuti online** (dipendenti dallo scheduling e dall'attuale esecuzione): 
	- tempi di arrivo $a_i$ di inizio $s_i$, di completamento $f_i$, tempo di risposta $R_i$
	- laxity $X_i$ e laxity resuiduale $Yi$
	- lateness $L_i$, e tardiness $E_i$.
	- Start time jitter, finishing time jitter e completion time jitter
![[Pasted image 20240923175713.png]]
---

## Feasibility vs Schedulability (1/2)

Un **programma è fattibile** se tutte le sue constraint sono rispettate:
- - - **Constraint temporali**: attivazione, periodo, deadline, jitter.
    - **Constraint espliciti**: specificati direttamente nel sistema.
    - **Constraint impliciti**: non specificati ma necessari per soddisfare i requisiti prestazionali.
    - **Constraint di precedenza**: impongono un ordine di esecuzione, espressi tramite un **DAG**.
    - **Constraint di accesso alle risorse**: gestiscono la sincronizzazione nell’accesso a risorse condivise.
---

### Feasibility vs schedulability (2/2)

- Un insieme di task $\Gamma$ è detto **fattibile** se esiste un algoritmo che genera una schedulazione fattibile per $\Gamma$.
- Un insieme di task $\Gamma$ è detto **schedulabile** da un algoritmo $A$ se $A$ genera una schedulazione fattibile per $\Gamma$.
![[Pasted image 20240923180625.png]]
---

### Il problema della schedulazione

- Il problema della schedulazione consiste nel, dato un set di task $Γ$ , un set di processori $P$, un set di risorse $R$ e un set di vincoli $C$, trovare un'assegnazione di risorse che produca una schedulazione fattibile. 
- Il problema della schedulazione è NP-completo. (gli algoritmi di scheduling hanno un tempo di esecuzione esponenziale, nel numero di tasks)
- ![[Pasted image 20240923181117.png]]

---

### Ricapitolazione sulla complessità

- Un problema decisionale è NP se può essere risolto in tempo polinomiale da una macchina di Turing non deterministica.
- Un problema decisionale H è NP-hard, se ogni problema di decisione in NP, può essere ridotto in tempo polinomiale ad H
- Il problema decisionale sarà dunque NP-complete se è sia NP che NP-hard. 

---

## Tassonomia degli algoritmi di schedulazione

- **Preemptive vs non preemptive**: preemptive, un task può essere interrotto; non preemptive, un task non può essere interrotto.
- **Statico vs dinamico**:
	- **statico**, le decisioni sono prese basandosi su parametri fissi; 
	- **dinamico**, le decisioni sono basate su parametri che cambiano nel tempo.
- **Offline** vs **online**: 
	- Offline: decisioni prese prima dell'attivazione del compito (programmazione basata su tabelle)
	- Online: decisioni prese durante l'esecuzione in base ai compiti 

---

- Ottimale vs euristico:
	- **Ottimale**: genera una schedulazione che minimizza una funzione di costo definita da un criterio di ottimalità.
	- **Euristico**: genera una schedulazione secondo una funzione euristica che cerca di soddisfare un criterio di ottimalità, senza garanzia di successo.

- Schedulazione garantita vs best-effort
	- **Schedulazione garantita**: genera una schedulazione fattibile se esiste; necessaria per task hard real-time.
	- **Best-effort**: non garantisce una schedulazione fattibile; utile per task soft real-time; ottimizza la performance media.

- Algoritmo chiaroveggente
	- Conosce tutte le attivazioni future dei task.
	- Può essere usato per confrontare le performance.
---
## Classificazione algoritmi di scheduling

![[Pasted image 20240923181801.png]]
## Anomalie di schedulazione

- **Teorema (Graham, 1976)**: Se un insieme di task è schedulato in modo ottimale su un multiprocessore con assegnazione di priorità fissa, un numero fisso di processori, tempi di esecuzione fissi e vincoli di precedenza, allora aumentare il numero di processori, ridurre i tempi di esecuzione o ridurre i vincoli di precedenza può aumentare la lunghezza della schedulazione.
![[Pasted image 20240923181830.png]]
---
# Schedulazione di task periodici
## Schedulazione di task periodici: formulazione del problema (1/2)

- Un insieme di $n$ task periodici $\Gamma = {\tau_1, \dots, \tau_n}$, ciascuno caratterizzato da:
    - Tempo di arrivo iniziale (fase) $\Phi_i = a_{i,1}$
    - Tempo di esecuzione nel caso peggiore (WCET) $C_i$
    - Periodo di attivazione $T_i$
    - Deadline relativa $D_i \leq T_i$
    - Nessun vincolo di precedenza o di risorse.
    - ![[Pasted image 20240923182020.png]]

---

### Schedulazione di task periodici: formulazione del problema (2/2)

- Obiettivo: garantire che ogni job $\tau_{i,k}$ di ciascun task periodico $\tau_i$ sia attivato al tempo $a_{i,k} = \phi_i + (k - 1) T_i$ e completi entro il tempo $d_{i,k} = a_{i,k} + D_i$.

![[Pasted image 20240923182020.png]]

---

## Schedulazione di task periodici: parametri aggiuntivi

- **Iper-periodo $H$**: minimo intervallo di tempo dopo il quale la schedulazione si ripete (minimo comune multiplo dei periodi dei task).
- **Tempo di risposta di un job $R_{i,k}$**: $R_{i,k} = f_{i,k} - a_{i,k}$.
- **Tempo di risposta di un task** $R_{i} = max_{k}{R_{i,k}}$. 
	- Ovvero il massimo tempo di risposta fra tutti i job dei task
![[Pasted image 20240923182432.png]]
---
## Schedulazione di attività periodiche: istante critico di un'attività

- Il tempo di arrivo che produce il massimo tempo di risposta dell'attività.
- Si verifica quando l'attività arriva insieme ad altre attività con priorità più alta.
	- Considera l'interferenza di un'attività ad alta priorità $\tau_i$ su un'attività a bassa priorità $\tau_n$.
	- ![[Pasted image 20240923183243.png]]
	- Ridurre la fase di $\tau_i$ aumenta il tempo di risposta di $\tau_n$.
	- ![[Pasted image 20240923183300.png]]
	- Ridurre la fase di qualsiasi attività con priorità più alta aumenta il tempo di risposta di $\tau_n$.
## Schedulazione non-preemptive a orologio statico (1/2)

- Per task periodici con deadline relativa **uguale al periodo**.
- Le decisioni sono prese **offline** in istanti di tempo prestabiliti.
- ![[Pasted image 20240924222023.png]]
---
### Schedulazione non-preemptive a orologio statico (2/2)

- **Vantaggi**:
    - Implementazione semplice (non è necessario un sistema operativo in tempo reale).
    - Basso overhead a runtime.
    - Jitter molto ridotto.
- **Svantaggi**:
    - Non robusto durante sovraccarichi.
    - Difficile da espandere.
    - Task aperiodici non facili da gestire

---

## Schedulazione esecutiva ciclica (schedulazione a timeline)

- Uno degli algoritmi di schedulazione più usati nei sistemi militari di difesa e nei sistemi di controllo del traffico (ad esempio, Boeing 777, Space Shuttle).
- **Come funziona**:
	- Il tempo è diviso in intervalli (**slot temporali**) di uguale durata Δ (ciclo minore).
	- Uno o più task sono **allocati staticamente** a ciascuno slot temporale, assicurando che la somma dei tempi di esecuzione nel caso peggiore (WCET) in ciascuno slot non sia maggiore di Δ.
	- Esecuzione attivata da un **timer** per ciascun slot temporale.
	- Lo schedule si ripete dopo un intervallo di durata $T$ (**ciclo maggiore**).

**Valori tipici dei parametri**:

- Δ=gcd⁡{$T1,...,Tn$} (minimo comune divisore dei periodi dei task).
- T=\lcm{$T1,...,Tn$} (massimo comune multiplo dei periodi dei task).

---

### Esempio di schedulazione esecutiva ciclica

- Esempio con un insieme di tre task con i seguenti parametri:
    - Task $A$: WCET = 10, Periodo = 25
    - Task $B$: WCET = 10, Periodo = 50
    - Task $C$: WCET = 10, Periodo = 100

 - I parametri sono scelti in modo da garantire $C_A + C_B ≤ ∆$ e $C_A + C_C ≤ ∆$
	- Con Major cycle $T = 100$
	- e Minor cycle ∆ $= 25$
	
- ![[Pasted image 20240924222135.png]]
---

### Implementazione e codifica della schedulazione esecutiva ciclica

Un'immagine illustra un esempio di implementazione e codifica per la schedulazione esecutiva ciclica.
![[Pasted image 20240924222519.png]]

---
### Cyclic Executive Scheduling: Svantaggi

- Problemi durante **sovraccarichi** (esecuzione oltre i limiti dei task):
    - Lasciar continuare il task ⇒ possibile effetto domino sugli altri task.
    - Abortire il task ⇒ stato incoerente del sistema.
- Difficoltà nell'espandere lo scheduling in caso di cambiamenti nei **parametri dei task**:
    - Cambio del WCET: $C_B=20 ⇒ C_A+C_B >$ Δ, quindi occorre dividere $τ_B$ in due sottotask $τ_{B1}$ e $τ_{B2}$ con WCET pari a 15 e 5 rispettivamente, e ridisegnare lo schedule!
	![[Pasted image 20240924223316.png]]
    - Cambio del periodo: $T_B=40$ ⇒ Δ=5 $T=200$, il che richiede 40 **sincronizzazioni** per major cycle! Molto difficile ridisegnare lo schedule a mano.
- ![[Pasted image 20240924223516.png]]
## Fattore di utilizzo del processore $U$

- Frazione del tempo del processore speso nell'esecuzione del task set:
    - $U = \sum_{i=1}^{n} \frac{C_i}{T_i}$.
![[Pasted image 20240924223543.png]]
---

### Limite superiore $U_{ub}(\Gamma,A)$ del fattore di utilizzo del processore $U$

- Il **limite superiore** $U_{ub}(\Gamma,A)$ del fattore di utilizzo $U$ per un insieme di task $\Gamma$ sotto un algoritmo di schedulazione $A$.
	- Se $U = U_{ub}(\Gamma,A)$, l'insieme di task utilizza completamente il processore. Se il WCET aumenta, il set di task diventa infattibile.
	- Ogni set di task può avere un diverso limite superiore.
- Ad esempio: (processore assegnato ai task in ordine crescente per il periodo)
-![[Pasted image 20240924223949.png]]

---

### Limite superiore minimo $U_{lub}(A)$

- Limite superiore **minimo** $U_{lub}(A)$ del fattore di utilizzo sotto un algoritmo di schedulazione $A$. Definito come:  $Ulub​(A)=Γmin​Uub​(Γ,A)$
- Se $U \leq U_{lub}(A)$, l'insieme di task è **schedulabile** dall'algoritmo $A$, altrimenti se $U > 1$ non lo è.
- ![[Pasted image 20240924224305.png]]

---
### Massimo Valore di $Ulub(A)$

- **Teorema**: Se $U >1$ su di un task set $Γ$ il set di task non è fattibile.
-  **Dimostrazione**:
1. Se $U>1$, questo implica che il **tempo richiesto** dal set di task è **maggiore del tempo disponibile** sul processore:
	    $U>1⇒UH>H$ (dove H eˋ il tempo disponibile per il processore).
2.  Da qui si deriva: 
	    $∑(C_i/T_i)H > H$
    Dove $H/T_i$​ rappresenta il numero di volte che il task $τi$ viene eseguito nel periodo H, e $(H/T_i)C_i$​ è il tempo di computazione richiesto da $τ_i$ nel hyper-periodo.
    
3. Quindi: $∑(H/T_i)C_i > H$  rappresenta il tempo totale di computazione richiesto dall’insieme di task nel periodo H
4. **Conclusione**: Se il **tempo richiesto dal set di task** supera il **tempo disponibile del processore** H, allora il set di task non è fattibile.

- **Osservazione**:
	Questo risultato vale per **qualsiasi algoritmo di scheduling**: se la domanda eccede il tempo disponibile, nessun algoritmo sarà in grado di produrre uno schedule fattibile.
	
---	
## Schedulazione basata su priorità

- Come funziona:
    - Assegna priorità a ciascun task basandosi sui suoi vincoli temporali.
    - Verifica la fattibilità della schedulazione usando tecniche analitiche.
    - Esegue i task su un kernel priority based.
- Goal dell'analisi della schedulabilità: costruire un algoritmo di schedulabilità ottimale considerando l'uso del processore e calcolando il tempo di risposta per ogni task.
		![[Pasted image 20240924230602.png]]
---

### Schedulazione Rate Monotonic (RM)

- Algoritmo di schedulazione online, **statico** e preemptive.
- Per task puramente periodici
- Viene assegnata una **priorità fissa** inversamente proporzionale al periodo del task.

Ad esempio: (con priorità di $τ_a > τ_b > τ_c$ )
	![[Pasted image 20240924230756.png]]

---
#### RM: teorema di ottimalità (Liu & Layland, 1973)

- RM è **ottimale** in termini di fattibilità tra tutti gli algoritmi a **priorità fissa** per la schedulazione di task periodici con deadline uguale ai periodi.
	- Se Uno scheduling a priorità fissa è fattibile per un task set $Γ$ ⇒ allora anche risulta fattibile anche per la schedulazione Rate Monotic
	- Se invece uno scheduling RM non è fattibile per un task set $Γ$ ⇒ allora non sarà schedulabile (e quindi fattibile) per qualsiasi algoritmo a priorità fissa.
- Fissato che ogni task raggiunge il suo caso peggiore nel caso dell'istante critico sarà sufficiente dimostrare l'ottimalità nel caso dell'istante critico.
- Se Uno scheduling a priorità fissa è fattibile per un task set $Γ$ agli istanti critci ⇒ allora anche risulta fattibile anche per la schedulazione RM agli istanti critici.

---
#### Dimostrazione di ottimalità per il caso di due task
- Si consideri il caso di un task set $Γ$ composto da 2 task $τ_1$ e $τ_2$ con $T_1 < T_2$
- Se le priorità non vengono assegnate con scheduling RM ⇒ priorità $τ_2$  > priorità $τ_1$ 
	- Il task set sarà schedulabile all'istante critico se $C_1 + C_2 ≤ T_1$
	![[Pasted image 20240925192958.png]]
	- Dobbiamo quindi far vedere che se $C_1 + C_2 ≤ T_1$ ⇒ allora lo scheduling RM è fattibile per $Γ$ all'instante critico
---
- Prendiamo quindi il caso in cui tutti i periodi di $τ_1$ siano tutti contenuti i $T_2$
	- Definisco un fattore F come $F ∶= ⌊T2 /T1⌋$
- Assegnando le priorità nel caso RM ⇒ priorità $τ_1$  > priorità $τ_2$ 
- Ho quindi due casi:
	- Caso 1: $C_1 < T_2 − F T_1$, ovvero tutti i job del primo task rilasciati nell'intervallo $[0, T_2)$  sono completati prima che il secondo job del secondo task sia rilasciato
					![[Pasted image 20240925194540.png]]
		- Il task set sarà schedulabile se $(F + 1)C_1 + C_2 ≤ T_2$ 
		- Dimostreremo che $C_1 + C_2 ≤ T_1$ implica $(F + 1)C_1 + C_2 ≤ T_2$
	- Caso 2: $C_1 ≥ T_2 − F T_1$, ovvero alcuni job del primo task rilasciati nell'intervallo $[0, T_2)$  non sono completati prima che il secondo job del secondo task sia rilasciato
					- ![[Pasted image 20240925195043.png]]
		- ll task set sarà schedulabile se $FC_1 + C_2 ≤ FT_1$ 
		- Dimostreremo che $C_1 + C_2 ≤ T_1$ implica $FC_1 + C_2 ≤ FT_1$ 
---
- Caso 1: Dimostriamo che $C_1 + C_2 ≤ T_1 ⇒ (F + 1)C_1 + C_2 ≤ T_2$
	• $C_1 + C_2 ≤ T_1 ⇒ F C_1 + F C_2 ≤ F T1$ dato che F ≥ 1 (Possiamo moltiplicare tutto per F senza problemi)
	⇒ $F C_1 + C_2 ≤ F C_1 + F C_2 ≤ F T_1$ dato sempre che F ≥ 1
	⇒ $(F + 1)C_1 + C_2 ≤ F T1 + C1$ ⇒
	⇒ $(F + 1)C_1 + C_2 ≤ F T_1 + C_1 < T_2$ dato che nel caso 1 $C_1 < T_2 − F T_1$ ⇒
	⇒ $(F + 1)C_1 + C_2 < T_2$

- Caso 2: Dimostriamo che $C_1 + C_2 ≤ T_1 ⇒ F C_1 + C_2 ≤ F T_1$
	• $C_1 + C_2 ≤ T_1 ⇒ F C_1 + F C_2 ≤ F T_1 dato che F ≥ 1 ⇒
	⇒ $F C_1 + C_2 ≤ F C_1 + F C_2 ≤ F T_1$ dato che F ≥ 1 ⇒
	⇒ $F C_1 + C_2 ≤ F T_1$

--- 
#### Test di garanzia RM (Liu & Layland, 1973)

- Se $U \leq n(2^{1/n} - 1)$ per un insieme $\Gamma$ di $n$ task periodici puri, allora $\Gamma$ è schedulabile tramite RM.

- Il test è **solo sufficente**
- La complessità è polinomiale $O(n)$, rispetto al numero $n$ dei tasks
- La metodologia per dimostrarlo sarà:
	- Assegnare la priorità dei task secondo RM
	- Assumo che i che task arrivino tutti in modo simultaneo (worst case scenario per il task set)
	- Aumento i tempi di computazione in modo tale da usare completamente il processore
	- Calcolo l'upper bound $U_{ub}$ tramite $U$
	- Minimizzo  l'upper bound $U_{ub}$, rispetto a tutti gli altri parametri in modo da ottenere il $U{lub}$

---
- Considero il caso di un task set $Γ$ composto di 2 task periodici $τ_1$ e $τ_2$ con $T_1 < T_2$
- Il numero di periodi di $τ_1$ interamente contenuti in $τ_2$: $F∶=⌊T2/T1⌋$
- Abbiamo di nuovo i due casi: 
- Caso 1:
	 ![[Pasted image 20240925194540.png]] $C_1 < T_2 − F T_1$,
- Caso 2:
	- ![[Pasted image 20240925195043.png]] $C_1 ≥ T_2 − F T_1$
• In entrambi i casi, massimizziamo $C_2$ e deriviamo $Uub$ come funzione di $C_1$.
--- 
- Caso 1: $C_1 < T_2 − F T_1$, ovvero tutti i job del primo task rilasciati nell'intervallo $[0, T_2)$  sono completati prima che il secondo job del secondo task sia rilasciato
![[Pasted image 20240929173424.png]]
-> Guardando il diagramma nel caso 1 $C_2$ sarà al massimo il periodo rimanente fra $T_1$ e l'ultimo periodo di compitazione del primo task.
-> Sostituisco i fattori e con un po' di passaggi noto che la quantità fra le parentesi è negativa dato che prendo la parte intera inferiore dei due Periodi.
	-> $U{ub}$ diminuisce con l'aumentare di $C_1$
	-> Il valore minimo di $U{ub}$ sarà per $C_1 = T_2 - FT_1$ (che è anche il valore massimo che può raggiungere per il caso 1)
	![[Pasted image 20240929174250.png]]
---
- Caso 2: $C_1 ≥ T_2 − F T_1$, ovvero alcuni job del primo task rilasciati nell'intervallo $[0, T_2)$  non sono completati prima che il secondo job del secondo task sia rilasciato
![[Pasted image 20240929174542.png]]
-> Riguarda figura per $C_2$ (Da $FT_1$ verso sinistra ci sono esattamente F job di tempo $C_1$)
-> Con un po' di calcoli riguardante il fattore di utilizzo, risulta che la quantità fra parentesi è positiva, dunque $U_{ub}$ sale al crescere di $C_1$ e il minimo valore si avrà di nuovo per 
$C_1 = T_2 - F T_1$
![[Pasted image 20240929175150.png]]
___
- Calcolo infine il minimo valore di $U_{ub}$ rispetto a $C_1$: (Ovvero nel caso di $C_1 = T_2 - FT_1$)
![[Pasted image 20240929180227.png]]
-> Ripartiamo dal calcolo di Uub nel caso 2... 

---
- Chiamo poi la parte decimale T2/T1: G = T2/T1 - F
- Per cui ricalcolo la funzione Uub(min C1) in funzione di G:
![[Pasted image 20240929180718.png]]
-> dove G è compreso fra 0 e 1 (la quantità al numeratore è maggiore o uguale a 0), dunque Uub crescerà al crescere di F (?)

- Se riprendo la formula prima di Uub è vado a calcolarmi il caso di minimo per F allora ottengo ![[Pasted image 20240929183410.png]]
- Che derivato a sua volta per ottenere il minimo:
![[Pasted image 20240929183506.png]]

---
#### Test di garanzia RM: Caso particolare di task con periodici armonici
- Presi due task con periodi armonici, ovvero:
	- $T_1/T_2 ∈ N$ --> per cui anche il fattore F:= $⌊T_2/T_1⌋ = T_2/T_1$
	⇒ $U{lub} = T_1/T_2  ( F + (T_2/T_1 - F)^2 ) = 1$
- Per cui il fattore di utilizzo U = 1 diventa minimo e massimo nel caso di task con periodi armonici:![[Pasted image 20240929184209.png]]
---
#### Test di Garanzia RM: Dimostrazione per n task
- Ripartiamo per il caso di 2 tasks con $T_1 < T_2$
	- $C_1 = T_2 - FT_1$ e F = 1 => $T_2 < 2T_1$
	![[Pasted image 20240929184807.png]]
	- $C_1 = T_2 - FT_1 =$ (per F = 1 ) $T_2 - T_1$, $C_2 = F(T_1 - C_1) = T_1 - C_1 = T_1 - T_2 + T_1 = 2T_1 - T_2$
- E lo stesso per n tasks con $T_1 < T_2 < ... < T_n$ 
	![[Pasted image 20240929185259.png]]
- Con $T_n < 2T_1, C_1 = T_2 - T_1, C_2 = T_3 - T_2,$  ... $C_n = T_1 - (∑^{n−1}_ {i=1} C_i)= T_1 - (T_2 - T_1) - (T_3 - T_2)$ - ... $(T_n - T_{n-1}) = 2T_1 - T_n$
---
- Mi calcolo ora l'upper bound di U nel caso peggiore delle condizioni di schedulabiltà![[Pasted image 20240929185849.png]]
- e con un sacco di bei passaggi e anche una derivata parziale ottengo:![[Pasted image 20240929190007.png]]
--- 
- Risostituisco i risultati ottenuti e ottengo: ![[Pasted image 20240929190909.png]]
-> che appunto nel caso a due task -> n = 2 ci dà $U{lub} = 2(2^{1/2} - 1) = 0.83$
![[Pasted image 20240929191513.png]]

#### Test iperbolico RM (Bini et al., 2003)

- Se $\prod_{i=1}^{n} (U_i + 1) \leq 2$ per un insieme $\Gamma$ di $n$ task periodici puri, allora $\Gamma$ è schedulabile tramite RM.
	- Sempre nel caso peggiore di schulabilità per n task con  $T_1 < T_2 < ... < T_n$: se ho $T_n < 2T_1$ allora $C_1 = T_2 - T_1, C_2 = T_3 - T_2,$  ... $C_n = T_1 - (∑^{n−1}_ {i=1} C_i)= T_1 - (T_2 - T_1) - (T_3 - T_2)$ - ... $(T_n - T_{n-1}) = 2T_1 - T_n$
			![[Pasted image 20241001181518.png]]
---
	- Definisco $R_i = T_{i+1}/T_i ∀ i∈ {1, . . . , n − 1}$ 
		=> aggiungo e tolgo il periodo $T_i$ e per quanto visto sopra $C_i = T_{i+1} - T_i$ dunque ottengo $R_i = U_i + 1$ ma anche $∏^{n-1}_{i=1} R_i =T_n/T_1$ (fare moltiplicazione per controllare)
	+ Devo dimostrare quindi che la condizione di schedulabilità nel caso peggiore implica $\prod_{i=1}^{n} (U_i + 1) \leq 2$ 
		$∑^n_{i=1} C_i ≤ T_1$ => $∑^{n-1}_{i=1} C_i + C_n ≤ T_1$ => $C_n \leq T_1 - ∑^{n-1}_{i=1} C_i$ => $C_n \leq 2T_1 - T_n$ siccome $∑^{n-1}_{i=1} C_i = T_n - T_1$ nelle condizioni peggiori di schedulabità 
		=> Divido quindi il tutto per $T_n$ e ottengo $U_n \leq 2T_1 /T_n - 1 => U_n +1 \leq 2T_1/T_n$ che per la produttoria vista sopra mi fa ottenere $U_n \leq 2/  ∏^{n-1}_{i=1} R_i$ = (sostituisco gli Ri) e ottengo $U_n \leq 2/ ∏^{n-1}_{i=1} (U_i+1)$
		=> moltiplico da entrambe le parti per la quantità a denominatore e ottengo 
			$∏^{n}_{i=1} (U_i + 1) \leq 2$ 
---
#### Liu & Layland bound vs hyperbolic bound

**Il limite iperbolico è preciso**, cioè, se il limite iperbolico non è soddisfatto ⇒ esiste uno scheduling RM non fattibile con quella utilizzazione del processore.

- **Vantaggio ottenuto dal limite iperbolico (HB)** rispetto al limite di Liu & Layland (LL):
    - Rapporto tra gli ipervolumi nello spazio U dei set di task che risultano schedulabili utilizzando il limite HB rispetto a quelli schedulabili con il limite LL.
    - Questo rapporto **aumenta con n** e tende a $\sqrt{2}$​ quando n tende all'infinito.
			![[Pasted image 20241001184510.png]]
****
###  Schedulazione Deadline Monotonic (DM)

- Estensione di RM per task periodici con deadline vincolate (ossia, $D_i \leq T_i$).
	- Le deadline non sono più pari ai periodi
- Algoritmo di scheduling preemptive statico e parametri calcolati *online*
- Un task ha un **priorità fissa** inversamente proporzionale alla sua deadline *relativa*
	- Task con minore deadline relative vengono eseguiti prima
- Esempio: priorità $t_1 >$ priorità $t_2$![[Pasted image 20241006153448.png]]
---
#### **DM: ottimalità**  

Teorema (No dim)
- DM è ottimale in termini di fattibilità tra tutti gli algoritmi a **priorità fissa** (per la schedulazione di task periodici con deadline vincolate):
	- Se una schedulazione a priorità fissa è fattibile per un insieme di task $\Gamma$, allora la schedulazione DM è fattibile per $\Gamma$.
	- Se la schedulazione DM non è fattibile per un insieme di task $\Gamma$, allora nessuna schedulazione a priorità fissa è fattibile per $\Gamma$.
+ Nota che le due affermazioni sono equivalenti (a $\Rightarrow$ b se e solo se $\neg$b $\Rightarrow$ $\neg$a).
---
#### **DM: problema con il limite LL e il limite HB**

- Usa il limite LL (Liu & Layland) e il limite HB (Hyperbolic Bound) sostituendo i periodi con le deadline: il carico di lavoro del processore è sovrastimato
	$\Rightarrow$ il risultato del test è troppo pessimista!

- Esempio in cui i test basati sull'utilizzo del processore non sono conclusivi:  
	- Il limite LL non è soddisfatto:  $\frac{C_1}{D_1} + \frac{C_2}{D_2} = \frac{2}{3} + \frac{3}{6} = \frac{7}{6} > 1$
	- Il limite HB non è soddisfatto:  $\left( \frac{C_1}{D_1} + 1 \right) \left( \frac{C_2}{D_2} + 1 \right) = \left( \frac{2}{3} + 1 \right) \left( \frac{3}{6} + 1 \right) = \frac{5}{2} > 2$
- Ma l'insieme dei task è schedulabile!
	![[Pasted image 20241006153448.png]]

---
#### **DM: analisi del tempo di risposta (Audlsey et al, 1993)**  
- Per ogni task $\tau_i$:
	1. Si calcola l'interferenza $I_i$ dovuta ai task a priorità più alta nell'intervallo $[0, R_i]$: $I_i = \sum_{\tau_k | D_k < D_i} z_{ik} C_k$​ dove $z_{ik}$ è il numero di rilasci di $\tau_k$ in $[0, R_i]$. $\Rightarrow$ 
	   $\Rightarrow I_i = \sum_{k=1}^{i-1} \left\lceil \frac{R_i}{T_k} \right\rceil C_k​$ supponendo che i compiti siano ordinati per deadline relativa crescente 
	2. Calcola il tempo di risposta $R_i$:
		$R_i = C_i + I_i = C_i + \sum_{k=1}^{i-1} \left\lceil \frac{R_i}{T_k} \right\rceil C_k$ (1)
	3. Verifica che $R_i \leq D_i$ 
- Il tempo di risposta nel caso peggiore è il più piccolo valore che soddisfa l'equazione

---
##### **DM: Analisi del tempio di risposta - soluzione iterativa**

- La soluzione iterativa per derivare il più piccolo $R_i$ che soddisfa (1)
	- Passo 0: $R_i^{(0)} = \sum_{k=1}^{i}C_k$ (minimo tempo di risposta con l'arrivo dei task) 
	- Passo j: $R_i^{(j)} = C_i + I_i = C_i + \sum_{k=1}^{i-1} \left\lceil \frac{R_i^{(j-1)}}{T_k} \right\rceil C_k$ 
- Itera fino a che $R_i^{(j)} > R_i^{(j-1)}$ && $R_i^{(j)} \leq D_i$ $\forall j > 0$![[Pasted image 20241006162643.png]]
---
##### DM: Analisi del tempo di risposta - complessità
- L'algoritmo ha complessità **Pseudo-polinomiale** $O(n * N)$, rispetto al numero di elementi di un set di input per i valori del set di input
	- Complessità polinomiale nel numero $n$ di task 
	- Complessità polinomiale nel massimo numero $N$ di iterazioni per task, che dipendono principalmente dalla relazione fra i periodi dei task
--- 
#### **DM: esempio di un insieme di compiti non schedulabile**
![[Pasted image 20241006163226.png]]
- $R_1^{(0)} = C_1 = 2 < D_1$; $R_1^{(1)} = C_1 = 2 < D_1$; $\Rightarrow R_1 = 2$
- $R_2^{(0)} = C_1 + C_2 = 4 < D_2$; $R_2^{(1)} = C_2 + \left\lceil \frac{R_2^{(0)}}{T_1} \right\rceil C_1  = C_2 + C_1 = 4 < D_2$; $\Rightarrow R_2 = 4$
- $R_3^{(0)} = C_1 + C_2 + C_3 = 8 = D_3$; $R_3^{(1)} = C_3 + \left\lceil \frac{R_3^{(0)}}{T_1} \right\rceil C_1 + \left\lceil \frac{R_3^{(0)}}{T_2} \right\rceil C_2 = C_3 + C_1 + 2 C_2 = 10 > D_3$

---
##### **DM: esempio di un insieme di compiti non schedulabile (2/2)**
- Il tempo di risposta stimato aumenta a ogni rilascio del compito: $R_3 = 12$.              ![[Pasted image 20241006164325.png]]

---
#### **DM: esempio di un insieme di compiti schedulabile**
![[Pasted image 20241006170652.png]]
- I tempi di risposta di $\tau_1$ e $\tau_2$ rimangono gli stessi: $R_1 = 2 < D_1$, $R_2 = 4 < D_2$
- $R_3^{(0)} = C_1 + C_2 + C_3 = 6 < D_3$
- $R_3^{(1)} = C_3 + \left\lceil \frac{R_3^{(0)}}{T_1} \right\rceil C_1 + \left\lceil \frac{R_3^{(0)}}{T_2} \right\rceil C_2 = C_3 + C_1 + C_2 = 6 < D_3$
---
							![[Pasted image 20241006170938.png]]
---
### Schedulazione Earliest Deadline First (EDF)
	 
	 ![[Pasted image 20241006172843.png]]
 
- Algoritmo di schedulazione online, dinamico e preemptive.
- Scheduling per la gestione di task puramente periodici ($D_i = T_i$ per ogni task $\tau_i$)
- Ogni task ha una **priorità dinamica** inversamente proporzionale alla sua deadline assoluta.
- Esempio $C_1 = 3, T_1 = D_1 = 6; C_2 = 4, T_1 = D_1 = 9$
	![[Pasted image 20241006173836.png]]
---
#### Scheduling EDF vs Scheduling RM
- Se lo schedule EDF è fattibile per il task set precedente
- Per lo schedule RM, lo stesso task set non è fattibile ![[Pasted image 20241006174155.png]]
- I test basati su Liu & Layland e gli hyperbolic bounds sono inconclusivi, in quanto non consento di valutare la fattibilità di uno scheduling RM:
	- $U = C_1 / T_1 + C_2/T_2 = 3/6 + 4/9 = 0.944 > 2 (\sqrt2 - 1) = 0.028$
	- $(U_1 + 1)(U_2 +1) = (3/6+1)(4/9+1) = 13/6 > 2$

---
#### Test di garanzia EDF (Liu & Layland, 1973)

- Un insieme di task periodici puri è schedulabile tramite EDF se e solo se $U \leq 1$.
	- Il test è **necessario e sufficiente**
	- Complessità polinomiale $O(n)$ rispetto al numero $n$ di compiti
	- Necessità: se un insieme di task periodici è schedulabile con EDF $\Rightarrow U \leq 1$
	- Sufficienza: se  $U \leq 1 \Rightarrow$ un insieme di task puramente periodici è schedulabile tramite EDF

**Dimostrazione necessità**
- Se $U > 1$ allora $U \cdot T > T$ poiché $T = T_1 T_2 \dots T_n > 0$,
	=>  $\sum_{i=1}^{n} \frac{C_i}{T_i} T > T$ per definizione di $U$ => $\sum_{i=1}^{n} \frac{T}{T_i} C_i > T$
    => la domanda totale di risorse nel periodo $[0, T)$ è maggiore del tempo disponibile $T$,  => l'insieme dei task non è fattibile.
---
**Dimostrazione sufficienza (Per assurdo)**
- Si assume che l'insieme dei compiti non sia schedulabile con EDF e che $U < 1$:
	- $t_2$: il primo istante di tempo in cui una scadenza viene mancata.
	- $[t_1,t_2]$: è il più grande intervallo continuo di utilizzazione prima di $t_2$, nel quale sono eseguiti solo i job $\tau_{i,k}$ con tempo di arrivo $a_{i,k} \geq t_1$ e deadline assoluta $d_{i,k} \leq t_2$ 
	- $C_p(t_1, t_2)$: la richiesta del processore durante l'intervallo di tempo $[t_1,t_2]$ =>![[Pasted image 20241006181055.png]]
	- $C_p(t_1, t_2) > t_2 - t_1$ dato che una scadenza viene mancata a $t_2$
	![[Pasted image 20241006181152.png]]
	- $\Rightarrow t_2 - t_1 < C_p(t_1,t_2) \leq (t_2-t_1)U \Rightarrow U > 1$, che è una contraddizione.
--- 
#### Ottimalità EDF (Dertouzos, 1974)

- EDF è ottimale in termini di fattibilità tra **tutti gli algoritmi**.
	- Se uno schedule è fattibile per un task set $\Gamma$ => Anche lo scheduling EDF è fattibile per $\Gamma$ 
	- Se lo schedule EDF non è fattibile per un task $\Gamma$ => non esiste schedule fattibile per $\Gamma$
- Risultato indipendente dalla periodicità dei task
---
##### Dimostrazione Ottimalità EDF:

- Una schedulazione fattibile $\sigma$ per l'insieme di compiti $\Gamma$ è divisa in intervalli di tempo di un'unità di tempo:
	- $\sigma(t)$: compito eseguito durante l'intervallo $[t, t + 1)$
	- $E(t)$: indice del compito con la scadenza assoluta minima a $t$
	- fasads
	- sdasdas
- Lo schedule $\sigma$ è trasformato in uno schedule EDF $\sigma_{EDF}$![[Pasted image 20241006182210.png]]
---
			![[Pasted image 20241006182238.png]]
--- 
- Una trasposizione conserva la schedulabilità, cioè $\sigma_{EDF}$ è fattibile per $\Gamma$.
	- Se un intervallo di tempo di un task $\tau_i$ viene anticipato => la fattibilità di $\tau_i$ è preservata.
	-  Se un intervallo di tempo di un task $\tau_i$ viene posticipato a $t_E$ =>
		=> $t_E +1 \leq d_E$ con $d_E$ la più vicina deadline assoluta al tempo t
		=> siccome $\sigma$ è fattibile => $t_E +1 \leq d_E \leq d_i - \forall \tau_i$ per definizione di $d_E$ =>
		=> l'intervallo di tempo posticipato a $t_E$ è schedulabile. 
--- 
#### Ottimalità EDF rispetto alla minimizzazione del ritardo massimo (Jackson, 1955)

**Teorema**: Un insieme di $n$ task indipendenti, schedulato in ordine di deadline crescenti, minimizza la massima lateness $L_{max} = \max_{i \in {1,\dots,n}} {L_i}$.

- Risultato anche lui indipendente dalla periodicità
- Se l'algoritmo minimizza $L_{max}$ => è ottimale nel senso di feasibility (l'opposto non è sempre vero) 
- ![[Pasted image 20241006183331.png]]
--- 
Spazio per la dimostrazione... WIP

---

#### EDF con deadline vincolate (Baruah et al., 1990)

**Criterio della domanda del processore**:
Un insieme di task periodici ${\tau_1, \dots, \tau_n}$ con $D_i \leq T_i$ per ogni task $\tau_i$ è schedulabile da EDF se e solo se, in ogni intervallo di tempo $[t_1, t_2]$, la domanda del processore $g(t_1, t_2)$ non supera il tempo disponibile, cioè $g(t_1, t_2) \leq t_2 - t_1$ per ogni $t_1 < t_2$.

- La domanda del processore nell'intervallo $[t_1, t_2]$, è il tempo per processare richiesto dai job attivati in $[t_1, t_2]$, con una deadline assoluta $\leq t_2$:
	- $g(t_1,t_2) = \sum_{i-1}^{n}\eta_i(t_1,t_2)C_i$
- Con $\eta_i(t_1,t_2)$ che è il numero di job di $\tau_i$ che contribuisce alla richiesta in $[t_1,t_2]$:
	- $\eta_i(t_1,t_2) =  ∣{τ_{i,k} ∣ a_{i,k} ∈ [t_1 , t_2 ] ∧ d{i,k} ≤ t_2 }∣ = max(0, K_2^i − K_1^i )$
	- $K_2^i = ∣{τ_{i,k} ∣ a_{i,k} ∈ [\phi , t_2 ] ∧ d{i,k} ≤ t_2 }∣ = ⌊t_2 + T_i − D_i − \phi_i /Ti ⌋$
	- $K_1^i = ∣{τ_{i,k} ∣ a_{i,k} ∈ [\phi , t_1 ]}∣ = ⌈t_1 − \phi_i /T_i ⌉$
---
- $K_1^i = ∣{τ_{i,k} ∣ a_{i,k} ∈ [\phi , t_1 ]}∣ = ⌈t_1 − \phi_i /T_i ⌉$
![[Pasted image 20241007222057.png]]
--- 
- $K_2^i = ∣{τ_{i,k} ∣ a_{i,k} ∈ [\phi , t_2 ] ∧ d{i,k} ≤ t_2 }∣ = ⌊t_2 + T_i − D_i − \phi_i /Ti ⌋$
![[Pasted image 20241007222140.png]]
--- 
##### EDF con deadline vincolate: funzione di domanda vincolata

- **Scenario peggiore**: tutti i task sono attivati al tempo $t = 0$ (cioè $\phi_i = 0$ per ogni task $\tau_i$):
    - $dbf(t) = g(0,t) = \sum_{i-1}^{n}\eta_i(0,t)C_i = \sum_{i=1}^{n} \left\lfloor \frac{t + T_i - D_i}{T_i} \right\rfloor C_i$.

- Un set $n$ di task periodici sincronizzati(?)  con $D_i \leq T_i$ $\forall$ task $\tau_i$ è schedulabile da EDF se e solo se $dbf(t) \leq t$ $\forall t > 0$
			![[Pasted image 20241007222551.png]]

---
##### EDF con deadline vincolate: complessità sui bound

1.  Preso un insieme sincrono di task periodici => Verifico il criterio solo per  $t \leq H$ (dove $H$ è l'iper-periodo dell'insieme di compiti).
2. $dbf(t)$ è una funzione a gradino che aumenta quando $t$ è uguale a una deadline assoluta ⇒ se $dbf(t) < t$ per $t = d_i$ allora $dbf(t) < t$ $\forall t \mid d_i \leq t < d_{i+1}$ 
   ⇒ Verifico il criterio solo per i valori di $t$ uguali alle deadline assolute.
3. Verifico il criterio almeno fino a $d_{max} := \max_i {d_i} \leq H$.

---
4.  $dbf(t) = \sum_{i=1}^{n} \left\lfloor \frac{t + T_i - D_i}{T_i} \right\rfloor C_i \leq  \sum_{i=1}^{n}  \frac{t + T_i - D_i}{T_i} C_i = \sum{i=1}^{n}(T_i - D_i)U_i + tU$ => 
=> $G(0,t) = \sum{i=1}^{n}(T_i - D_i)U_i + tU$ è una funzione crescente con la pendenza $U$
=> se U < 1 allora $∃ t^⋆ ∣ G(0, t^⋆ ) = t^⋆$ dove $t^* = \sum_{i=1}^{n}(T_i - D_i)U_i/(1-U)$
=> $dbf(t) \leq G(0,t) \leq t$ $\forall t \geq t^*$ => mi basta verificare quindi il criterio solo per $t < t^*$
		![[Pasted image 20241007224836.png]]
---
- Riassumendo: come limitare la complessità?  
	- Verifico il criterio solo per $t \leq H$
	- Verifico il criterio solo per valori di t uguali alla sua deadline assoluta
	- Verifico il criterio almeno fino a $d_{max} = max_i(d_i) \leq H$
	- Verifico il criterio solo per $t < t^*$
	
**Test di domanda del processore**
Un insieme sincrono di $n$ task periodici {$\tau_1$, ... , $\tau_n$} con $D_i \leq T_i$ $\forall$ task $\tau_i$ è schedulabile da EDF se e solo se $U < 1$ e $dbf(t) \leq t$ $\forall t ∈ D$ con $D = \{d_i \mid d_i \leq \min \{d_{\text{max}}, t^*\}\}$ e $t^* = \sum{i=1}^{n}(T_i - D_i)U_i/(1-U)$

--- 

### RM vs EDF

- **Schedulazione RM**:
    - Meno efficiente in termini di utilizzo del processore. (nel caso peggiore vicino al 69%)
    - Più facile da implementare in Sistemi Operativi Real-Time commerciali
    - Politiche di priorità fisse, più semplici da predirre durante periodi di *overloads* ma meno flessibili.
- **Schedulazione EDF**:
    - Maggiore efficienza nell'utilizzo del processore (l'uso del processore e pari al 100%)
    - Minore numero di prelazioni => minore overhead dovuto ai cambi di contesto
    - Più flessibile durante periodi di overload (tutti i task sono eseguiti ad un ritmo più lento)
    - Richiede una gestione delle priorità dinamica, più complessa da implementare, ma che porta a un migliore capacità di risposta nel gestire task aperiodi e un controllo del jitter più uniforme.

---
### Scheduling dei task periodici: 

- 3 tipologie di scheduling
	1. Offline (scheduling pianificato temporalmente)
	2. Online static priority (RM, DM)
	3. Online dynamic priority (EDF)
- 3 tecniche di analisi di scheduling
	1. Basate sull'uso del processore
		- Bound di Liu & Layland (LL) per RM: $U \leq n(2^{1/n} - 1)$ (condizione sufficiente)
		- Hyperbolic bound (HB) per RM: $\prod_{i=1}^n(U_i + 1) \leq 2$ (condizione sufficiente)
		- Bound LL per task armonici: $U \leq 1$ (condizione necessaria e sufficente)
		- Bound EDF:  $U \leq 1$ (condizione necessaria e sufficente)
		- Complessità polinomiale $O(n)$ sul numero di task
	2. Response time analysis
		- $R_i \leq D_i$ $\forall i ∈\{1, ... , n\}$ con $R_i = C_i + \sum_{k=1}^{i-1}\left\lceil R_i/T_k \right\rceil C_k$ (necessaria e sufficiente)
		- Complessità Pseudo-polinomiale
	3. Processor demand alaysis
		- $dbf(t)\leq t$ $\forall t \in D$ (Necessario e sufficiente)
		- Complessità Pseudo-polinomiale
		
![[Pasted image 20241009083217.png]]
---
# Protocolli di accesso alle risorse
## Risorse

- Una **risorsa** è una qualsiasi struttura software usata da un task per far avanzare la sua esecuzione (ad esempio variabili, file, device, aree di memoria)
	- Risorsa **privata**: dedicata ad un singolo task
	- Risorsa **condivisa**: può essere usata da più task

- Una risorsa **esclusiva**: una risorsa condivisa protetta contro gli accessi concorrenti
	- **Protocolli di accesso alle risorse**: meccanismo che garantisce mutua esclusione
	- **Sezioni critiche**: un pezzo di codice eseguito sotto mutua esclusione

![[Pasted image 20241009083859.png]]

--- 
## Inversione di priorità

- L'inversione di priorità è un fenomeno che accade quando un **task ad alta priorità** è bloccato da un **task a bassa priorità** per un intervallo di ==durata indefinita==
	- Il **tempo di blocco** di un task è un ritardo causato da task a priorità minore
	- Ad esempio se $\tau_1$ e $\tau_3$ (con $P_1 > P_3$) condividono una risorsa gestita da un semaforo binario S
	- Il tempo di blocco di $\tau_1$ sarà pari al tempo che $\tau_3$ necessità per eseguire la sezione critica

	![[Pasted image 20241009084459.png]]
	
---
- Il tempo di blocco del task ad alta priorità non può essere ristretto dalla durata della sezione critica eseguita dal task a bassa priorità
	- Ad esempio se aggiungo un **task a media priorità** $\tau_2$ ($P_1 > P_2 > P_3$)
	- Il massimo tempo di blocco di $\tau_1$ dipende non solo dalla durata della sezione critica di $\tau_3$ ma anche dal WCET di $\tau_2$
- La soluzione al *blocco unbounded* è usare protocolli di accesso alle risorse.
--- 
## Protocolli di accesso alle risorse
### La formulazione del problema

- Preso un **Set di $n$ task periodici** $\Gamma = \{\tau_1, \ldots, \tau_n\}$, con ciascun compito $\tau_i$ caratterizzato da:
    - Fase $\Phi_i$, WCET $C_i$, periodo $T_i$, scadenza relativa $D_i \leq T_i$
    - Priorità **nominale** (statica, fissa) $P_i$ (assegnata dal programmatore)
    - Priorità **dinamica** (attiva) $p_i \geq P_i$ (inizializzata a $P_i$)

- **Set di $m$ risorse condivise** $\Psi = {R_1, \ldots, R_m}$
    - Ciascuna risorsa $R_k$ protetta da un diverso **semaforo binario** $S_k$
    
- **Assunzioni:**
    - $\tau_1, \ldots, \tau_n$ vengono rilasciati all’arrivo.
    - $\tau_1, \ldots, \tau_n$ hanno overhead del kernel pari a zero o trascurabile.
    - $\tau_1, \ldots, \tau_n$ hanno priorità nominali diverse.
    - $\tau_1, \ldots, \tau_n$ sono elencati in ordine crescente di priorità nominale (cioè $P_1 > \ldots > P_n$).
    - $\tau_1, \ldots, \tau_n$ si sospendono solo:
        - Per aspettare l’inizio del prossimo periodo.
        - Su semafori bloccati.
    - Le sezioni critiche sono protette da semafori binari e ==correttamente annidate==.
        - $z_{i,k}$: sezione critica del compito $\tau_i$ protetta dal semaforo binario $S_k$.
        - Per ogni coppia $z_{i,h}, z_{i,k}$, vale che $z_{i,h} \subset z_{i,k}$ o $z_{i,k} \subset z_{i,h}$ o $z_{i,h} \cap z_{i,k} = \emptyset$

---
- **Obiettivo:** derivare il **tempo massimo di blocco** $B_i$ che un compito $\tau_i$ può sperimentare.
    
- **Aspetti chiave del protocollo:**
    - **Regola di accesso:** decide se bloccare e quando.
    - **Regola di avanzamento:** decide come eseguire all'interno di una sezione critica.
    - **Regola di rilascio:** decide come ordinare le richieste pendenti dei compiti bloccati.
---
### Protocollo di Ereditarietà delle Priorità (PIP) (Sha et al., 1990)

- **Regola di accesso**: un task $\tau_i$ viene bloccato all'entrata di una sezione critica $z_{i,k}$ se la risorsa $R_k$ è già posseduta da un task di priorità inferiore $\tau_j$.
	- Il task $\tau_i$ si dice **bloccato** da $\tau_j$.
	- I task bloccati sono schedulati in base alla loro priorità dinamica.
	- I task bloccati con la stessa priorità sono schedulati in base alla regola First Come First Served (FCFS).
    
- **Regola di avanzamento**: all'interno di una sezione critica associata alla risorsa $R_k$, un task esegue con la priorità più alta dei task bloccati su $R_k$.
    - $\tau_j$ **eredita** la priorità più alta dei compiti che blocca: 
	    - $p_j=max⁡\{P_j,max⁡\{P_i∣τ_i$ bloccato su $R_k\}\}$
    - Proprietà di **transitività**: se $\tau_3$ blocca $\tau_2$ e $\tau_2$ blocca $\tau_1$, allora $p_3 = P_1$.
    
- **Regola di rilascio**: quando $\tau_j$ esce dalla sezione critica associata alla risorsa $R_k$:
    - Il semaforo $S_k$ viene sbloccato.
    - Il task con priorità più alta bloccato su $S_k$ (se presente) viene risvegliato.
    - Se nessun altro task è bloccato da $\tau_j$, allora $p_j = P_j$; altrimenti $\tau_j$ eredita la priorità più alta dei task che blocca.
---
#### Tipi di Blocco nel PIP

- **Blocco diretto**: si verifica quando un task ad alta priorità si blocca all'entrata della sezione critica di una risorsa già posseduta da un task a priorità inferiore.
    - È necessario per garantire la consistenza delle risorse condivise.
    
- **Push-through blocking**: si verifica quando un task a priorità media è bloccato da un task a bassa priorità che ha ereditato una priorità più alta da un compito.
    - È necessario per evitare inversione di priorità.
    
- Presi ad esempio $\tau_1$, $\tau_2$ ,$\tau_3$ con $P_1 > P_2 > P_3$ e $\tau_1$ e $\tau_3$ condividono la risorsa $R$
![[Pasted image 20241013220530.png]]
---
- 3 task $\tau_1$, $\tau_2$ ,$\tau_3$: $\tau_1$ e $\tau_3$ condividono la risorsa $R_a$ ;$\tau_2$ e $\tau_3$ condividono la risorsa $R_b$
![[Pasted image 20241013220705.png]]

---
- 3 task $\tau_1$, $\tau_2$ ,$\tau_3$: $\tau_1$ e $\tau_3$ condividono la risorsa $R_a$ ;$\tau_2$ e $\tau_3$ condividono la risorsa $R_b$
![[Pasted image 20241013220857.png]]
- Al tempo $t_4$, il task $\tau_3$ eredita la priorità del task $\tau_1$ tramite il task $\tau_2$
---
#### Proprietà PIP
##### PIP: Proprietà (1/5)

**Quando si verifica il blocco?**
- **Lemma 1**: Un semaforo $S_k$ può causare un push-through block a un task $\tau_i$ solo se $S_k$ è stato acquisito da un task con priorità inferiore a $P_i$ e da un task con priorità superiore a $P_i$.

- **Dimostrazione**: Assumiamo per assurdo che $S_k$ sia utilizzato da un compito $\tau_l$ con priorità inferiore a $P_i$, ma non da un compito con priorità superiore a $P_i$. In tal caso, $\tau_l$ non può ereditare una priorità superiore a $P_i$ e quindi $\tau_i$ farà prelazione su $\tau_l$.

--- 
##### PIP: Proprietà (2/5)

 **Quando si verifica l’ereditarietà transitoria della priorità?
- **Lemma 2**: L'ereditarietà transitoria della priorità può verificarsi solo nel caso di sezioni critiche annidate.

- **Dimostrazione**: L'ereditarietà transitoria si verifica quando un task ad alta priorità $\tau_h$ è bloccato da un task di priorità media $\tau_m$, che a sua volta è bloccato da un task di bassa priorità $\tau_l$. 
  => $\tau_m$ detiene un semaforo $S_a$ (dato che blocca $\tau_h$) e $\tau_l$ detiene un altro semaforo $S_b$ (dato che blocca $\tau_m$) 
  => $\tau_m$ ha tentato di bloccare $S_b$ all'interno della sezione critica protetta da $S_a$, quindi le due sezioni critiche sono annidate.

---
##### PIP: Proprietà (3/5)

**Quante volte può essere bloccato un task?**
- **Lemma 3**: Se ci sono $l_i$ task a priorità inferiore che possono bloccare un task $\tau_i$, 
	=> allora $\tau_i$ può essere bloccato per **al massimo** la durata di $l_i$ sezioni critiche (una per ciascun task a priorità inferiore, indipendentemente dal numero di semafori utilizzati da $\tau_i$).

- **Dimostrazione**: $\tau_i$ può essere bloccato da un compito di priorità inferiore $\tau_j$ solo se $\tau_i$ ha prelazionato $\tau_j$ all'interno di una sezione critica $z_{j,k}$ che può bloccare $\tau_i$. 
	=> Una volta che $\tau_j$ esce da $z_{j,k}$, => $\tau_i$ non può essere bloccato di nuovo da $\tau_j$. Pertanto, $\tau_i$ può essere bloccato al massimo $l_i$ volte.

---
##### PIP: Proprietà (4/5)

 **Quante volte può essere bloccato un task?**
- **Lemma 4**: Se ci sono $s_i$ semafori distinti che possono bloccare un task $\tau_i$
	=> allora $\tau_i$ può essere bloccato per al massimo la durata di $s_i$ sezioni critiche (una per ciascun semaforo, indipendentemente dal numero di sezioni critiche utilizzate da $\tau_i$).

- **Dimostrazione**: I semafori sono binari, quindi solo ==uno dei task a priorità inferiore==  $\tau_j$ può trovarsi in una sezione critica di blocco. Una volta che $\tau_j$ esce dalla sezione critica, $\tau_i$ non può essere bloccato di nuovo da $\tau_j$. 
  Pertanto, $\tau_i$ può essere bloccato al massimo $s_i$ volte.
---
##### PIP: Proprietà (5/5)

- **Quante volte può essere bloccato un task?**
    - **Teorema 1**: Sotto il Protocollo di Ereditarietà delle Priorità (PIP), un compito $\tau_i$ può essere bloccato per al massimo la durata di $\alpha_i = \min\{l_i, s_i\}$ sezioni critiche, dove:
        - $l_i$ è il numero di compiti a priorità inferiore che possono bloccare $\tau_i$.
        - $s_i$ è il numero di semafori che possono bloccare $\tau_i$.
    - **Dimostrazione**: La tesi segue direttamente dai Lemmi 3 e 4.

- Non riusciamo a predirre bound stretti sui tempi di blocco tramite questo teorema.
##### Protocollo di Ereditarietà delle Priorità (PIP): Riepilogo

- **Vantaggi:**    
    - Basso pessimismo (un compito viene bloccato ==solo quando necessario==).
    - Trasparenza per il programmatore.
    - Tempo di blocco limitato (al massimo la durata delle sezioni critiche $\alpha_i$).
    
- **Svantaggi:**
    - Il calcolo dei tempi di blocco è complesso (a causa di blocchi diretti, blocchi push-through, ereditarietà prioritaria transitiva).
    - Implementazione complicata (richiede modifiche alle strutture dati del kernel).
    - Suscettibile a **blocchi concatenati** (ogni compito $\tau_i$ bloccato $\alpha_i$ volte nel peggiore dei casi).
    - Non previene da casi di **deadlocks** causati da un uso errato dei semafori![[Pasted image 20241014084028.png]]
---
### Protocollo Priority Ceiling  (PCP)

- Il **priorità ceiling** $C(S_k)$ di un semaforo $S_k$ è la priorità massima tra quelle dei task che possono bloccare $S_k$, cioè $C(S_k) := \max_{i \in \{1, \ldots, n\}} \{P_i \mid \tau_i \text\{ utilizza \} S_k\}$.
    
- **Regola di accesso:** Un compito $\tau_i$ si blocca all'entrata di una sezione critica se la sua priorità non è superiore al massimo ceiling dei semafori bloccati da altri compiti, cioè $P_i \leq \max\{C(S_k) \mid S_k \text\{$ bloccato da compiti$\} \neq \tau_i\}$.
	- **Test di accesso per il PCP** per garantire una richiesta di blocco su un semaforo libero
	- Un task non può entrare in una sezione critica bloccata da un semaforo libero se sono presenti semafori bloccati che lo possono bloccare => una volta che un task entra nella sua sezione critica, non può essere bloccato da un task a bassa priorità fino al suo completamento

- La regola di avanzamento e di rilascio è la stessa di PIP (ripetuta sotto)
---
**Regola di avanzamento**: all'interno di una sezione critica associata alla risorsa $R_k$, un task esegue con la priorità più alta dei task bloccati su $R_k$.
    - $\tau_j$ **eredita** la priorità più alta dei compiti che blocca: 
	    - $p_j=max⁡\{P_j,max⁡\{P_i∣τ_i$ bloccato su $R_k\}\}$
    - Proprietà di **transitività**: se $\tau_3$ blocca $\tau_2$ e $\tau_2$ blocca $\tau_1$, allora $p_3 = P_1$.
    
- **Regola di rilascio**: quando $\tau_j$ esce dalla sezione critica associata alla risorsa $R_k$:
    - Il semaforo $S_k$ viene sbloccato.
    - Il task con priorità più alta bloccato su $S_k$ (se presente) viene risvegliato.
    - Se nessun altro task è bloccato da $\tau_j$, allora $p_j = P_j$; altrimenti $\tau_j$ eredita la priorità più alta dei task che blocca.    

---
#### (PCP): Ceiling blocking

- Il *Ceiling blocking* si verifica quando un task viene bloccato poiché non passa il test di accesso del PCP, cioè $P_i \leq \max\{C(S_k) \mid S_k \text\{$ bloccato da compiti $\} \neq \tau_i\}$.
	- Necessario per evitare deadlock e blocchi concatenati.

- L'esempio è come al solito di 3 task $\tau_1$, $\tau_2$ ,$\tau_3$: $\tau_1$ usa la risorsa $R_a$ e $R_b$ ;$\tau_2$ usa la risorsa $R_c$ e  $\tau_3$ usa la risorsa $R_b$ e $R_c$
![[Pasted image 20241014225850.png]]
---
#### Proprietà del PCP
##### Lemma 1
Se un task $\tau_k$ subisce preemption nella sua sezione critica da un task $\tau_i$ che entra nella sezione critica $z_{i,b} => \tau_k$ non può ereditare una priorità maggiore di $\tau_i$ fino a che $\tau_i$ finisce

**Dimostrazione**: 
- Se $\tau_k$ eredita una priorità maggiore di $\tau_i$ prima che $\tau_i$ completi => esisterà un task $\tau_h$ bloccato da $\tau_k \mid P_h \geq P_i$
- Se $\tau_i$ entra nella sua sezione critica => $P_i > C^*$ dove $C^*$ è per definizione il max ceiling dei semafori bloccati da task a priorità minore.
- Dunque, $P_h \geq P_i > C^*$ => $\tau_h$ non può essere bloccato da $\tau_k$ che è una contraddizione.
---
##### Lemma 2
Il Protocollo Priority ceiling previene i blocchi transitivi

**Dimostrazione**:
Se accade un blocco transitivo => esistono dei task $\tau_1, \tau_2, \tau_3 \mid P_1 > P_2 > P_3$ dove $\tau_1$ è bloccato da $\tau_2$, mentre $\tau_2$ è bloccato da $\tau_3$ 
=> $\tau_3$ dunque erediterà la priorità di $\tau_1$ => che contraddice il Lemma 1

---
##### Teorema 1:
Il PCP previene i deadlock.

 **Dimostrazione**: 
 Se si verifica un deadlock $\Rightarrow$ esistono task $\tau_1, \tau_2, \ldots, \tau_n$ con $P_1 > P_2 > \ldots > P_n$, dove $\tau_1$ è bloccato da $\tau_2$, $\tau_2$ è bloccato da $\tau_3$ e così via $\Rightarrow$ $\tau_n$ erediterà la priorità di $\tau_1$, contraddicendo il Lemma 1.

---
##### Teorema 2:
Un task sotto PCP può essere bloccato per al massimo la durata di una singola sezione critica.
    
**Dimostrazione**: 
- Sia $\tau_i$ un task bloccato da $\tau_1$ e da $\tau_2$ con $P_i > P_1 > P_2$
- Supponiamo $\tau_2$ entra per primo nella sua sezione critica bloccante
- Sia $C_2^*$ il massimo ceiling fra i semafori bloccati da $\tau_2$
- Se $\tau_1$ entra nella sua sezione critica $P_1 > C_2^*$
- Ma se $\tau_i$ può essere bloccato da $\tau_2$ => $P_i \leq C_2^*$
- Quindi $P_i \leq C_2^* < P_1$ che contraddice la prima assunzione.

- Il massimo tempo di blocco per ogni task è derivato in base al Teorema 2 

---

#### Riepilogo del PCP
- **Vantaggi:**
    - Limita il blocco alla durata di una sezione critica.
    - Previene deadlock e blocchi transitivi.
    
- **Svantaggi:**
    - Complesso da implementare.
    - Pessimistico (può causare blocchi non necessari).
    - Non trasparente per il programmatore (i ceiling devono essere specificati nel codice sorgente).

---
### Analisi di Schedulabilità per Task Periodici con Risorse Condivise

- **Blocchi senza limite** $\Rightarrow$ Task set non schedulabile.
- **Blocchi limitati** $\Rightarrow$ Estendere i test di schedulabilità per task indipendenti.
	- Garantisco un task alla volta
	- Prelazione da task con più alta priorità e blocco da task con bassa priorità
	- Le condizioni di blocco derivate nel caso peggiore che differisce per ogni task e non possono accadere simultaneamente => I test sono **solo sufficienti**
---

#### Test di scheduling estesi

- Analisi in base all'uso 
	- Test LL (Liu & Layland) per RM: Un set di tasks periodici $\{\tau_1, ... , \tau_n\}$ con fattori di blocco  e con $D_i = T_i$ $\forall$ task $\tau_i$ è schedulabile per RM se 	![[Pasted image 20241016080141.png]]
		
	- Test HB (Hyperbolic bound) per RM: Un set di tasks periodici $\{\tau_1, ... , \tau_n\}$ con fattori di blocco  e con $D_i = T_i$ $\forall$ task $\tau_i$ è schedulabile per RM se ![[Pasted image 20241016080305.png]]

	- Test LL per EDF: Un set di tasks periodici $\{\tau_1, ... , \tau_n\}$ con fattori di blocco  e con $D_i = T_i$ $\forall$ task $\tau_i$ è schedulabile per EDF se 
	 ![[Pasted image 20241016080531.png]]
---
	- Response time analysis
		- Un set di tasks periodici $\{\tau_1, ... , \tau_n\}$ con fattori di blocco  e con $D_i = T_i$ $\forall$ task $\tau_i$ è schedulabile per DM(Deadline Monotonic) se ![[Pasted image 20241016080901.png]]
		- La soluzione iterativa per calcolare $R_i$ ![[Pasted image 20241016081127.png]]
	
---
	- Processor demand analysis 
		- Un set di tasks periodici $\{\tau_1, ... , \tau_n\}$ con fattori di blocco  e con $D_i = T_i$ $\forall$ task $\tau_i$ è schedulabile per EDF se $U < 1$ e $dbf(t) + B(t) \leq t$ $\forall t \in D$
		- $dbf(t) = \sum_i ⌊ \frac{t + T_i - D_i}{T_i} C_i ⌋$
		- $B(t) = max_{i,j \mid i \ne j} \{ \beta_{ij} \mid D_i > t ∧ D_j \leq t\}$ è chiamato **funzione di blocco**
		- $\beta{ij}$ è il massimo tempo per il quale $t_i$ tiene una risorsa che è anche necessaria per $\tau_j$
		- $D = \{d_i \mid d_i \leq max \{D_{max}, min \{H, t^*\}\}\}$, $D_max = max_i\{D_i\}$
		- $H = lcm(T_1, ..., T_n)$, $t^* = \sum_i (T_i-D_i)U_i /(1-U)$

# Sistemi operativi Real-time
## Standard per RTOSs
### **Sistemi operativi**: kernel e chiamate di sistema

- Il kernel è il cuore del sistema operativo (OS).
	  - È la parte del codice dell'OS sempre residente in memoria.
	  - Funziona come interfaccia tra le applicazioni a livello utente e le risorse hardware.
- Non deve essere confuso con il BIOS (Basic Input/Output System), il software di base del processore responsabile dell'avvio del sistema.
- Fornisce le **chiamate di sistema** che permettono ai programmi a livello utente di accedere ai servizi dell'OS.
	  - Esse costituiscono un'interfaccia di programmazione delle applicazioni (API) e rappresentano l'unico punto di ingresso nel kernel.
			![[Pasted image 20241020231435.png]]
---	
### **Memoria**: spazio del kernel vs spazio utente

- **Spazio del kernel**: area di memoria dove è memorizzato ed eseguito il codice del kernel.
	  - Il kernel ha accesso a tutta la memoria (sia spazio del kernel che spazio utente).
	  - La modalità kernel è una modalità operativa privilegiata della CPU.
- **Spazio utente**: area di memoria dove è memorizzato ed eseguito il codice a livello utente.
	  - I programmi a livello utente hanno accesso solo allo spazio utente e possono accedere a una parte limitata del kernel tramite le chiamate di sistema.
	  - Se un programma a livello utente invoca una chiamata di sistema, viene inviato un **interrupt** software al kernel, che esegue il gestore appropriato e restituisce il controllo al programma utente.

---
### Sistemi operativi in tempo reale (RTOS)

- **OS di uso generale (GPOS)**: un sistema operativo non adatto per applicazioni in tempo reale.
- **Sistema operativo in tempo reale (RTOS)**: un OS adatto per applicazioni in tempo reale.
	  - **Hard Real-time**: mancare una scadenza può avere effetti catastrofici sul sistema (gestisce task RT rigidi, con tempo di reazione dell'ordine di $1 \text{ms}$ o meno).
	  - **Soft Real-time**: mancare una scadenza comporta una riduzione delle prestazioni (gestisce task RT morbidi, con tempo di reazione dell'ordine di $\leq 100 \text{ms}$ o meno).

- **Caratteristiche principali di un RTOS**
  - **Predicibilità**
  - Determinismo
  - Alte prestazioni
  - Funzionalità di sicurezza e protezione
  - Pianificazione basata su priorità
  - Ridotta impronta di memoria

---
### Standard per GPOS (General Purpose OS) e RTOS

- Definiscono (sintassi e semantica delle) chiamate di sistema.
- Forniscono **portabilità** delle applicazioni da una piattaforma all'altra.
	- Promuovono la competizione tra fornitori di kernel, aumentando la qualità delle piattaforme.
	- La portabilità è specificata a livello di codice sorgente, richiedendo la ricompilazione per ogni piattaforma.

- **Principali standard per GPOS e RTOS**
	  - POSIX
	  - RT-POSIX
	  - OSEK/VDX
	  - ARINC-APEX
	  - µITRON

---
### POSIX (Portable Operating System Interface per UniX)

- Famiglia di standard intesi a garantire la portabilità delle applicazioni a livello di codice sorgente e mantenere la compatibilità tra diversi OS.
- Sviluppato dal Portable Applications Standards Committee (PSSC) della IEEE Computer Society e formalmente indicato come IEEE Std 1003.
	  - **IEEE Std 1003.1**: servizi di base
	  - **IEEE Std 1003.1b**: estensioni per il tempo reale (pianificazione delle priorità, orologi e timer, semafori, ...).
	  - **IEEE Std 1003.1c**: estensioni per i thread
	  - **IEEE Std 1003.2**: shell e utilità

- Supporta vari livelli di **conformità** e il paradigma "**programmare per contratto**".

---
### RT-POSIX

- Estensione real-time di POSIX, che consente la portabilità delle applicazioni in tempo reale.
- Fornisce servizi per la **programmazione concorrente** e la **prevedibilità temporale**.
	  - Sincronizzazione di mutua esclusione tramite eredità di priorità.
	  - Code di messaggi prioritari per la comunicazione tra task.
	  - Pianificazione preemptiva a priorità fissa.

- Profili real-time definiti da POSIX.13:
  - **PSE51**: per piccoli sistemi embedded, supporta i thread ma non i processi.
  - **PSE52**: estende PSE51 con supporto per un file system semplificato.
  - **PSE53**: per grandi sistemi embedded, con supporto per processi multipli con sistema di protezione.
  - **PSE54**: per sistemi multiuso, supporta applicazioni composte da task real-time e non.

---
### Altri standard

- **OSEK/VDX**: standard per software applicativo automobilistico.
- **ARINC-APEX**: standard per software applicativo avionico, che descrive sistemi avionici e di cabina.
- **µITRON**: famiglia di standard per software applicativo embedded. (massimizza portabilità mantenendo scalabilità)

---
### Tipi di RTOS

- **RTOS commerciali**: VxWorks, QNX, Neutrino, OSE.
- **RTOS basati su Linux**: RTLinux, RTAI.
- **RTOS open-source e di ricerca**: SHARK, MaRTE, ERIKA.

---
## VxWorks

### **Caratteristiche principali di VxWorks**

- Sviluppato da WindRiver (sede centrale a Alameda, CA, USA)
- Supporto per 32/64 bit su Arm/Intel/MIPS/PowerPC
- RTOS proprietario, conforme a POSIX PSE52
- Separazione tra spazio kernel e spazio utente, con spazio utente opzionale
- Supporto per C/C++11/14, con possibilità di sviluppare moduli kernel in C++ e applicazioni utente
- Certificabile per la sicurezza: DO-178, ISO 26262, IEC 61508
- Sistema di build proprietario
- Shell del kernel
- IDE basato su Eclipse, con supporto per host Windows/Linux

---
### Esempi di applicazioni industriali che utilizzano VxWorks
![[Pasted image 20241020233243.png]]

---
### Orologio e pianificazione

- **L'orologio del kernel** determina la risoluzione delle azioni di pianificazione.
	- La frequenza predefinita dell'orologio del kernel è di $60 \text{Hz}$.
	- La frequenza minima e massima del kernel dipende dall'hardware.
- VxWorks supporta:
	  - Pianificazione preemptiva basata su priorità
	  - Pianificazione a turni (round-robin)
	  - Fino a $256$ livelli di priorità

---
### Comunicazione tra task

- VxWorks supporta:
	  - Memoria condivisa tra task (simile ai thread)
	  - Semafori binari e semafori contatori
	  - Mutex (interfacce POSIX)
	  - Code di messaggi e pipe (tubi?)
	  - Socket e chiamate di procedura remota (RPC)
	  - Segnali
- I semafori mutex supportano il Protocollo di Eredità delle Priorità (PIP)

---
## Introduzione alla programmazione in tempo reale: ripasso del linguaggio C

### **Il linguaggio di programmazione C**

- Un programma in C specifica una computazione attraverso 3 costrutti:
  - Variabili
  - Espressioni
  - Istruzioni

---

### 1/3: Variabili

- Una **Variabile** contiene un **Valore** di un certo **Tipo**
  - Il valore varia durante la computazione
  - Il tipo rimane invariato
  - Un **Tipo** definisce un insieme di valori e un insieme di operazioni

- Tipi base predefiniti: `int`, `float`, `char`, ... con modificatori
- Tipi definiti dall'utente: `struct` (vedi più avanti)
- Una variabile ha un **Ciclo di vita**:
  - Dichiarazione
  - Riferimento

---

### 2/3: Espressioni

- La **sintassi** di un'espressione combina costanti e riferimenti a variabili tramite operatori.
- La **semantica** di un'espressione consiste in due elementi:
  - Un'espressione restituisce un valore (di un certo tipo)
  - Un'espressione produce effetti collaterali sulle variabili

---

### 2/3: Espressioni - Funzioni

- Le funzioni sono un tipo di espressione
  - Sintassi: sono una combinazione di un nome costante con valori restituiti da espressioni (i parametri effettivi) tramite un operatore (`(...)`).
  - Semantica: restituiscono un valore e producono effetti collaterali.

---

### 3/3: Istruzioni

- Un'istruzione specifica due aspetti:
  - Le espressioni da valutare
  - La prossima istruzione da eseguire, che può dipendere dai valori restituiti dalle espressioni

---

### Sommario del linguaggio C

- Una storia serializzata (un percorso ragionevole per apprendere il linguaggio)
  - Tipi, valori e costanti
  - Variabili
  - Espressioni, effetti collaterali e valori restituiti
  - Puntatori
  - Array, allocazione statica o dinamica
  - Funzioni
  - Istruzioni
  - Tipi strutturati

---
# Temi avanzati sull'analisi della schedulabilità 

**Indice**
1. Introduzione
2. Reti di Petri
3. Reti di Petri temporali
4. Reti di Petri temporali preemptive
5. Utilizzo delle reti di Petri temporali preemptive nel ciclo di vita software V-Model
6. Automi temporizzati
---
## Introduzione

**Approcci analitici vs metodi basati su spazio degli stati**

- **Approcci analitici**
	  - Presuppongono task con un Tempo di Esecuzione nel Peggior Caso (WCET) deterministico.
	  - Forniscono risultati esatti per insiemi di task periodici e indipendenti.
	  - Forniscono risultati pessimisti per insiemi di task che includono task sporadici e dipendenze inter-task (e.g., sincronizzazioni tramite semaforo, precedenze di flusso di dati).
	  - Offrono test di schedulabilità efficienti.

- **Metodi basati su spazio degli stati**
	  - Considerano parametri temporali che variano all'interno di un intervallo minimo-massimo.
	  - Supportano la modellazione e l'analisi di una vasta classe di sistemi in tempo reale (e.g., insiemi di task in tempo reale, protocolli di comunicazione).
	  - Forniscono risultati esatti per qualsiasi insieme di task che può essere modellato e analizzato.
	  - Richiedono una complessità computazionale maggiore rispetto agli approcci analitici.

---
## Reti di Petri

**Sintassi delle Reti di Petri (1/2)**

- Le Reti di Petri (PN) supportano la rappresentazione di sistemi **concorrenti**.
- Una PN è una tupla $\langle P, T, A^-, A^+\rangle$ dove:
    - $P$ è l'insieme dei **posti** (cerchi), $T$ è l'insieme delle **transizioni** (barre), $P \cap T = \emptyset$
    - $A^- \subseteq P \times T$ è l'insieme delle **precondizioni** (archi diretti dai cerchi alle barre)
    - $A^+ \subseteq T \times P$ è l'insieme delle **postcondizioni** (archi diretti dalle barre ai cerchi)
- Una PN è un grafo bipartito diretto dove:
    - l'insieme dei vertici è $P \cup T$
    - l'insieme degli archi è $A^- \cup A^+$
    
		![[Pasted image 20241021164257.png]] 
---
**Sintassi delle Reti di Petri (2/2)**

- Un posto $p$ è detto un **posto di input** per una transizione $t$ se $(p,t) \in A^-$ (Ovvero se esiste un arco diretto da p a t)
	- Ad esempio $p0$ è un posto di input per $t0$
-  Un posto $p$ è detto un **posto di output** per una transizione $t$ se $(p,t) \in A^+$ (Ovvero se esiste un arco diretto da p a t)
	- Ad esempio $p1$ è un posto di input per $t0$
		
		![[Pasted image 20241021164257.png]] 
---
**Stato di una PN**
- Una **marcatura** $m: P \rightarrow \mathbb{N}$ assegna un numero naturale di **token** a ciascun posto.
	- I tokens non hanno identità
	- Ad esempio $p0$ e $p1$ contengono un token ciascuno
- Una transizione $t$ è **abilitata** da una marcatura $m$ se $m(p) > 0 \, \forall p \in P \mid (p, t) \in A^-$ (ovvero se e solo se $m$ assegna almeno un token a ogni posto di input di $t$)
	- Le transizioni abilitate rappresentano **eventi concorrenti**
	- Ad esempio $t0$ e $t2$ sono abilitati, $t1$ non è abilitato
- Lo **stato** di una PN è una tupla(singleton) $s = \langle m \rangle$ dove $m$ è una marcatura.
	- Una transizione è abilitata nello stato $s = \langle m \rangle$ se e solo se è abilitato da una marcatura $m$
	- Una transizione abilitata eventualmente spara o è disabilitata
	- Ad esempio lo stato corrente in questa PN è $s = \langle p0,p2 \rangle$
		![[Pasted image 20241021170229.png]]
---
**Semantica delle PN (1/2)**

- Un'**esecuzione** di una PN è un percorso $\omega = s_0 \xrightarrow{\gamma_1} s_1 \xrightarrow{\gamma_2} s_2 \xrightarrow{\gamma_3} \ldots$ tale che:
  - $s_0 = \langle m_0 \rangle$ è lo stato iniziale e $m_0$ è la marcatura iniziale.
  - $\gamma_i$ è la $i$-esima transizione attivata.
  - $s_i = \langle m_i \rangle$ è lo stato raggiunto dopo lo sparo di $\gamma_i$.
  - $\gamma_i$ è selezionata tra le transizioni abilitate nello stato $s_{i-1} = \langle m_{i-1}\rangle$.
  - Dopo lo sparo di $\gamma_i$, la nuova marcatura $m_i$ è derivata da $m_{i-1}$ da
	  1. Aver rimosso un token da ogni posto di input di $\gamma_i$ (ovvero $m_{tmp} = m_{i−1} (p) − 1 ∀ p | (p, γ_i ) ∈ A^− )$
	  2. Aver aggiunto un toker ad ogni posto di output di $\gamma_i$ (ovvero $m_i = m{tmp}(p) +11 ∀ p | (γ_i,p ) ∈ A^+$)
  - $\omega$ è un percorso finito o infinito
- Ad esempio: $\langle p0 p2\rangle →^{t0} \langle p1 p2\rangle →^{t2} \langle p1 p3\rangle →^{t1} \langle p0 p2\rangle$ è una sequenza finita
- 
			![[Pasted image 20241021170229.png]]
---
**Semantica delle PN (2/2)**

- Esempio 1: Rete di Petri che ammette infinite esecuzioni
	- Ad esempio: $\langle p0 p2\rangle →^{t0} \langle p1 p2\rangle →^{t2} \langle p1 p3\rangle →^{t1} \langle p0 p2\rangle$ è una sequenza finita
	- Ma la infinita ripetizione di $\omega$ è una esecuzione infinita
	
- Esempio 2: Rete di Petri che non ammette infinite esecuzioni
	- Ad esempio: $\langle p0 p2\rangle →^{t0} \langle p1 p2\rangle →^{t2} \langle p1 p3\rangle →^{t1} \langle\rangle$
	- Ad esempio: $\langle p0 p2\rangle →^{t2} \langle p0 p3\rangle →^{t0} \langle p1 p3\rangle →^{t1} \langle\rangle$
	
		![[Pasted image 20241021202840.png]]
---
**Grafo di raggiunbilità di un PN**

- L'insieme $R(m_0)$ delle marcatura che può essere raggiunto dalla marcatura iniziale $m_0$ è il minimo insieme delle marcature tale che:
	- $m_0 \in R(m_0)$
	- se $m_0 \in R(m_0) ∧ \langle m \rangle →^t \langle m' \rangle$ con $t\in T$ allora $m' \in R(m_0)$
- Se il **grafo di raggiungibilità** è un grafo diretto tale che:
	- $R(m_0)$ è l'insieme di vertici
	- L'insieme degli archi, include l'arco da $m_i$ a $m_j$ se e solo $\exists t \in T | \langle m_i \rangle →^t \langle m_j \rangle$ 
- Un percorso nel grafo raggiungibile identifica un esecuzione del PN 
 ![[Pasted image 20241021220706.png]] 
---
**Enumerazione del grafo di raggiungibilità**

![[Pasted image 20241021220804.png]]
Ecco la traduzione delle formule con il simbolo `$`:

---
**Il problema del produttore/consumatore (1/4)**

• Definizione del problema  
	• Un produttore produce oggetti e li inserisce in un buffer  
	• Un consumatore consuma oggetti e li rimuove dal buffer  
	• Il buffer può avere una capacità limitata  
	• Produzione e consumo sono in mutua esclusione (requisito di **sicurezza**)  
	• La produzione e il consumo si verificheranno eventualmente(requisito di **liveness**)   -> si intende che non ci può essere solo produzione o solo consumo
	   
• Soluzione del problema  
	• Utilizzare un semaforo binario per garantire la mutua esclusione  

---
**Il problema del produttore/consumatore (2/4)**

• Invarianti di posto  
	• $m(pWaiting) + m(pProducing) + m(pSignalling) = 1$ ∀ $m \in M$  
	• $m(cWaiting) + m(cProducing) + m(cSignalling) = 1$ ∀ $m \in M$  
	• $m(free) + m(busy) = 4$ ∀ $m \in M$ (4 è la **capacità del buffer**)  
	
• Il modello garantisce la mutua esclusione (requisito di sicurezza soddisfatto)  
• Il modello è però soggetto a **deadlock** (requisito di liveness non soddisfatto)  
	• Nessuna transizione abilitata in un qualsiasi marcatura nel caso $m | m(pProducing) = 1 \land m(busy) = 4$  (4 tokens in busy e 1 in producing)
	• Nessuna transizione abilitata in un qualsiasi marcatura nel caso $m | m(cConsuming) = 1 \land m(free) = 4$  (4 tokens in free e 1 in consuming)
	
![[Pasted image 20241021223042.png]]

---
**Il problema del produttore/consumatore (3/4)**

• Il modello garantisce la mutua esclusione (requisito di sicurezza soddisfatto)  
• Il modello previene il deadlock (requisito di liveness soddisfatto)  
• Il modello non può essere tradotto in codice real-time  
	• Il numero di prodotti correnti potrebbe essere rappresentato da una variabile condivisa $sv$  
	• Potrebbe verificarsi uno switch di contesto (a causa del semaforo occupato)  dopo che il produttore/consumatore ha letto la variabile e prima di modificarla  
![[Pasted image 20241021223215.png]]

---
**Il problema del produttore/consumatore (4/4)**
	
• Il modello garantisce la mutua esclusione (requisito di sicurezza soddisfatto)  
• Il modello previene il deadlock (requisito di liveness soddisfatto)  
• Il modello può essere tradotto in codice real-time  
	• La variabile condivisa è prima testata dal produttore/consumatore e poi modificata  

![[Pasted image 20241021223528.png]]

---
**Reti di Petri con archi inibitori (1/2)**

• Le reti di Petri con archi inibitori hanno l'espressività della macchina di Turing (le reti di Petri no)  
• Una rete di Petri con archi inibitori è una tupla $\langle P, T , A^- , A^+ , A^\bullet \rangle$ dove:  
	• $P$, $T$, $A^-$, $A^+$ sono gli elementi di una rete di Petri  
	• $A^\bullet \subseteq P \times T$ è l'insieme degli archi inibitori  (archi diretti con frecce a pallino da cerchi a barre)  
• Un posto $p$ è detto un posto inibitore per una transizione $t$ se $(p, t) \in A^\bullet$  
(i.e., se c'è un arco con pallino da $p$ a $t$)  
	• es.: la *lettura* è un posto inibitore per la transizione *writeWait*  
	• es.: la *scrittura* è un posto inibitore per la transizione *readWait*  

![[Pasted image 20241021223747.png]]

---

**Reti di Petri con archi inibitori (2/2)** 

• Una transizione $t$ è **abilitata** da una marcatura $m$ se e solo se:  
	• $m(p) > 0$ ∀ $p \in P | (p, t) \in A^-$  (i.e., $m$ assegna almeno un token a ogni posto di input di $t$)  
	• $m(p) = 0$ ∀ $p \in P | (p, t) \in A^\bullet$  (i.e., $m$ non assegna alcun token a ogni posto inibitore di $t$)  
• Esempio: sincronizzazione lettura-scrittura  
	• La transizione *readWait* non può avvenire se il posto *writing* contiene un token (i.e., un processo non è autorizzato a leggere se un altro processo sta scrivendo)  
	• La transizione *writeWait* non può avvenire se il posto *reading* contiene un token  (i.e., un processo non è autorizzato a scrivere se un altro processo sta leggendo)  

![[Pasted image 20241021223747.png]]

---

**Reti di Petri con priorità (1/2)**

• Le reti di Petri con priorità hanno l'espressività della macchina di Turing (le reti di Petri no)  
• Una rete di Petri con priorità è una tupla $\langle P, T , A^- , A^+ , Z \rangle$ dove:  
	• $P$, $T$, $A^-$, $A^+$ sono gli elementi di una rete di Petri  
	• $Z : T \to N$ associa a ogni transizione una **priorità** (possibilmente annotata accanto alla barra che rappresenta la transizione)  
	• Più basso è il numero di priorità, più alta è la priorità della transizione  
• Esempio: $t_0$ ha un livello di priorità maggiore di $t_2$  

![[Pasted image 20241021224221.png]]

---

**Reti di Petri con priorità (2/2)**

• Una transizione $t$ è **abilitata** da un marking $m$ se e solo se:  
	• $m(p) > 0$ ∀ $p \in P | (p, t) \in A^-$ (i.e., $m$ assegna almeno un token a ogni posto di input di $t$)  
	• ∀ $t' \in T | t \neq t'$, se $m(p) > 0$ ∀ $p \in P | (p, t') \in A^-$ allora $Z(t) < Z(t')$  (i.e., $t$ ha un livello di priorità maggiore rispetto a qualsiasi altra transizione con posti di input non vuoti)  
	
• Esempio: una singola transizione è abilitata in ogni marking raggiungibile  
![[Pasted image 20241021224334.png]]

---

**Reti di Petri con funzioni di abilitazione e aggiornamento (1/2)**  

• Migliorano la comodità di modellazione rispetto alle reti di Petri con archi inibitori  
• Non aumentano l'espressività del modello rispetto alle reti di Petri con archi inibitori

• Una rete di Petri con funzioni di abilitazione e aggiornamento è una tupla $\langle P, T , A^- , A^+ , E , U \rangle$:  
	• $P$, $T$, $A^-$, $A^+$ sono gli elementi di una rete di Petri  
	• $E$ associa a ciascuna transizione $t \in T$ una **funzione di abilitazione**  
	$E(t) : M \to \{true, false\}$, con $M$ l'insieme delle marcature raggiungibili  
	• $U$ associa a ciascuna transizione $t \in T$ una **funzione di aggiornamento** $U(t) : M \to M$  
	• $E(t)$ e $U(t)$ possono essere annotate accanto alla barra che rappresenta la transizione  
• Esempio  
	• $t_0$ ha una funzione di abilitazione che valuta a true se $p_0$ contiene un token  
	• $t_1$ ha una funzione di aggiornamento che assegna a una marcatura $m$ un' altra marcatura $m_0$  ottenuto da $m$ assegnando un token al posto $p_0$  

![[Pasted image 20241021224824.png]]

---
**Reti di Petri con funzioni di abilitazione e aggiornamento (2/2)**

• Una transizione $t$ è **abilitata** da una marcatura $m$ se e solo se:  
	• $m(p) > 0$ ∀ $p \in P | (p, t) \in A^-$ (i.e., $m$ assegna almeno un token a ogni posto di input di $t$)  
	• $E(t)(m) = true$ (i.e., la funzione di abilitazione di $t$ valuta a true in $m$)  
	
• Data una marcatura  $m_{i-1}$ e una transizione $\gamma_i$ abilitata da $m_{i-1}$,  la marcatura $m_i$ raggiunta dopo l'esecuzione di $\gamma_i$ è derivata da $m_{i-1}$ attraverso  
1. la rimozione di un token da ogni posto di input di $\gamma_i$  (i.e., $m_{tmp} = m_{i-1}(p) - 1$ ∀ $p | (p, \gamma_i) \in A^-$)  
2. l'aggiunta di un token a ogni posto di output di $\gamma_i$  (i.e., $m_{tmp2} = m_{tmp}(p) + 1$ ∀ $p | (\gamma_i, p) \in A^+$)  
3. l'applicazione della funzione di aggiornamento di $\gamma_i$ (i.e., $m_i = U(\gamma_i)(m_{tmp2})$)  
![[Pasted image 20241021225203.png]]

---
## Reti di Petri Temporali

**Sintassi delle Reti di Petri Temporali (TPN)**

- Le TPN (Time Petri Nets) estendono le PN (con archi inibitori) con il **tempo**.
- Una TPN è una tupla $\langle P, T, A^-, A^+, A^{\bullet}, EFT, LFT \rangle$ dove:
	- $P, T, A^-, A^+, A^{\bullet}$ sono gli elementi di una PN con archi inibitori
    - $EFT$ associa a ciascuna transizione $t$ un **tempo minimo di attivazione** $EFT(t) \in \mathbb{Q}_{\geq 0}$.
    - $LFT$ associa a ciascuna transizione $t$ un **tempo massimo di attivazione** $LFT(t) \in \mathbb{Q}_{\geq 0}$.
    - $EFT(t) \leq LFT(t)$ $\forall t \in T$
- Ad esempio
	- $t0$ ha il tempo minimo di attivazione uguale a 0 e il tempo massimo uguale a 1
	- $t1$ ha il tempo minimo di attivazione uguale a 2 e il tempo massimo uguale a 3
	- $t2$ ha il tempo minimo e massimo di attivazione uguale a zero![[Pasted image 20241022080721.png]]

---
**Stato di una TPN**

- Lo stato di una TPN è una coppia $\langle m, \tau \rangle$ dove:
	  - $m$ è una marcatura (rappresenta la posizione logica del sistema).
	  - $\tau$ associa a ciascuna transizione abilitata $t$ un **tempo di attivazione** $\tau(t) \in \mathbb{R}_{\geq 0}$.
  - Ad esempio:
	  - $t0$ può essere associato con il tempo di attivazione $\tau(t0) \in [0,1]$
	  - $t2$ può essere associato con il tempo di attivazione $\tau(t2) \in [2,3]$
  
- **Esempio**:  
  - $t_0$ può essere associata a un tempo di attivazione $\tau(t_0) \in [0, 1]$.
  - $t_1$ può essere associata a un tempo di attivazione $\tau(t_1) \in [2, 3]$.
![[Pasted image 20241022080721.png]]
---
 **Semantica delle TPN (1/5)**

- Semantica **forte** dei vincoli temporali
	  - Una transizione $t$ **non può essere attivata prima** che sia stata abilitata continuamente per un tempo $T_{min}$ non inferiore al suo tempo minimo di attivazione ($T_{min} \geq EFT(t)$).
	  - Una transizione $t$ **deve essere attivata** quando è stata abilitata continuamente per un tempo $T_{max}$ pari al suo tempo massimo di attivazione ($T_{max} = LFT(t)$).
- Una semantica debole dei vincoli temporali (non implementata dai TPNs)
	- Indica che una transizione non attivata entro il suo tempo massimo di attivazione non sarà in grado di attivarsi fino a quando sarà abilitata nuovamente

---
**Semantica delle TPN (2/5)**

- Come nelle PN con archi inibitori, una transizione $t$ è **abilitata** da una marcatura $m$ se:
	  - $m(p) > 0 \, \forall p \in P \mid (p, t) \in A^-$. (ogni token nei posti di input di t)
	  - $m(p) = 0 \, \forall p \in P \mid (p, t) \in A^{\bullet}$. (nessun token per ogni posto inibitore di t)

- Una transizione $t$ è **attivabile** in uno stato $s = \langle m, \tau \rangle$ se:
	  - $t$ è abilitata da $m$.
	  - $\tau(t) \leq \tau(t') \, \forall t' \in T$ abilitata da $m$. (ovvero il tempo di attivazione di t è non più grande del tempo di attivazione di qualsiasi altra transizione abilitata)

 - In qualsiasi possibile stato iniziale della TPN in esempio abbiamo:
	 - $t0$ e $t2$ entrambi abilitati
	 - $t0$ è attivabile mentre $t2$ non lo è
	![[Pasted image 20241022080721.png]]
---
**Semantica delle TPN (3/5)**

- L'attivazione di una transizione $t$ sostituisce $s_0 = \langle m_0, \tau_0 \rangle$ con $s_1 = \langle m_1, \tau_1 \rangle$.
	  - Come nelle PN, $m_1$ è derivata da $m_0$:
	    1. Rimuovendo un token da ciascun posto di ingresso di $t$.
	    2. Aggiungendo un token a ciascun posto di uscita di $t$.

- Una transizione $t'$ abilitata da $m_1$ è chiamata:
	- **Persistente** se abilitata da entrambe $m_0$ e $m_{tmp}$
	- **Attivata nuovamente(?)** se non è abilitata da $m_0$ oppure da $m_{tmp}$ , oppure se è la transizione attivata t ed è stata abilitata da $m_1$
- Una transizione sarà **disabilitata** se è abilitata da $m_0$ ma non da $m_1$
- $\tau_1$ è derivata da $\tau$:
	- Riducendo il tempo di attivazione di ogni transizione persistente del valore di $\tau_0(t)$ (ovvero $\tau_1(t') = \tau_0(t') - \tau_0(t)$ $\forall t' \in T \mid t'$ sia persistente in $m_1$)
	- Eliminando il tempo di attivazione di ogni transizione disabilitata dall'attivazione di t 
	- Campionando il tempo di attivazione di ogni nuova transizione abilitata $t'$ nel suo intervallo di attivazione(ovvero $\tau_1(t') \in [EFT(t'), LFT(t')]$ $\forall t' \in T \mid t'$ sia una nuova transizione abilitata in $m_1$)
---
**Semantica delle TPN (4/5)**

- Esempio TPN
	- $t0$ è l'unica transizione attivabile nello stato iniziale con la marcatura $p0p2$
	- L'attivazione di $t0$ in $\langle p0p2, \tau_0\rangle$ porta a $\langle p1p2, \tau_1\rangle$ con $\tau_1(t2) = \tau_0(t2) - \tau_0(t0)$ ![[Pasted image 20241022080721.png]]
---
**Semantica delle TPN (5/5)**

- Un'esecuzione di una TPN è un percorso $\omega = s_0 \xrightarrow{\gamma_1} s_1 \xrightarrow{\gamma_2} s_2 \xrightarrow{\gamma_3} \ldots$ tale che:
	  - $s_0 = \langle m_0, \tau_0 \rangle$ è lo stato iniziale.
	  - $\gamma_i$ è la $i$-esima transizione attivata.
	  - $s_i = \langle m_i, \tau_i \rangle$ è lo stato raggiunto dopo l'attivazione di $\gamma_i$.
	  - $\gamma_i$ è selezionata tra le transizioni abilitate nello stato $s_{i-1} = \langle m_{i-1}\rangle$.
	  - Dopo lo sparo di $\gamma_i$, la nuova marcatura $m_i$ è derivata da $m_{i-1}$ da
		  1. Aver rimosso un token da ogni posto di input di $\gamma_i$ (ovvero $m_{tmp} = m_{i−1} (p) − 1$  $∀ p | (p, γ_i ) ∈ A^− )$
		  2. Aver aggiunto un token ad ogni posto di output di $\gamma_i$ (ovvero $m_i = m_{tmp}(p) +1$ $∀ p | (γ_i,p ) ∈ A^+$)
	  - $\tau_i$ sarà derivata da $\tau_{i-1} da:
		 1. Aver ridotto il tempo di ogni transizione **persistente** del valore di $\tau_{i-1}(\gamma_i)$ (ovvero $\tau_i(t') = \tau_{i-1}(t')-\tau_{i-1}(\gamma_i)$ $\forall t' \in T\mid t'$ è persistente in $m_1$)
		 2. Eliminando il tempo di attivazione di ogni transizione **disabilitata** dall'attivazione di t 
		 3. Campionando il tempo di attivazione di ogni **nuova transizione abilitata** $t'$ nel suo intervallo di attivazione (ovvero $\tau_1(t') \in [EFT(t'), LFT(t')]$ $\forall t' \in T \mid t'$ sia una nuova transizione abilitata in $m_1$)
	  - $\omega$ è un percorso finito o infinito

---
 **Estensione della sintassi e semantica delle TPN**

- Le TPN potrebbero essere estese con funzioni di abilitazione, funzioni di aggiornamento e priorità.
	- Queste caratteristiche migliorerebbero la comodità di modellazione senza aumentare l'espressività del modello rispetto alle TPN.
![[Pasted image 20241022085550.png]]
---
 **Modellazione di insiemi di task in tempo reale con TPN: un esempio (1/4)**

- 3 task $P_1, P_2, P_3$ che contendono 3 risorse **non preemptabili** $R_1, R_2, R_3$:
	  - $P_1$ e $P_2$ sono hard real-time (obbligatori), $P_3$ è soft real-time (opzionale).

  - $P_1$ è periodico:
    - Periodo $T_1 = 9$
    - Scadenza relativa $D_1 = 8$
    - Jitter di avvio assoluto $J_1 \leq 1$
    - Computazione 1: $WCET \, C_{11} \in [2, 3]$, utilizza $R_1$
    - Computazione 2: $WCET \, C_{12} \in [1, 2]$, utilizza $R_1, R_2$![[Pasted image 20241022085722.png]]
  - $P_2$ è sporadico:
    - Tempo tra gli arrivi $T_2 \geq 8$
    - Scadenza relativa $D_2 = 8$
    - Computazione: $WCET \, C_{21} \in [1, 2]$, utilizza $R_1, R_3$![[Pasted image 20241022085756.png]]
  - $P_3$ è sporadico:
    - Tempo tra gli arrivi $T_3 \geq 6$
    - Scadenza relativa $D_3 = 6$
    - Computazione: $WCET \, C_{31} \in [1, 2]$, utilizza $R_2, R_3$
    - ![[Pasted image 20241022085823.png]]

---
**Modellazione di insiemi di task in tempo reale con TPN: un esempio (2/4)**

- La TPN può essere derivata automaticamente dalla timeline dei task.
![[Pasted image 20241022085857.png]]
---
**Modellazione di insiemi di task in tempo reale con TPN: un esempio (3/4)

- Remarks: 
	- Le TPN non riescono a catturare le deadline relative (proprietà da verificare)
	- Il modello include due tipi di non determinismo:
		- Nella selezione dei tempi di attivazione (non sotto controllo del designer)
		- Nel rifiuto dei job di $P_3$ (sotto controllo del designer )
		
****
**Modellazione di insiemi di task in tempo reale con TPN: un esempio (4/4)**

- A che domande l'analisi della modello del TPN può rispondere?
	- Se i job di $P_3$ vengono sempre rifiutati, i job di $P_1$ e $P_2$ rispettano sempre la scadenza?
	- Se i job di $P_3$ vengono sempre accettati, i job di $P_1$ e $P_2$ rispettano sempre la scadenza?
	- Esiste una strategia di accettazione rifiuto che garantisca le scadenza di $P_1$ e $P_2$
- A quali domande in generale un analisi della TPN può rispondere?
	- **Raggiungibilità temporizzata**: quali ordinamenti tra le transizioni sono realizzabili sotto i vincoli temporali del modello?
	- **Durata min/max**: qual è il tempo minimo e massimo per completare una sequenza di firing di transizioni?

---
**Analisi delle TPN: Preliminari(1/3)**

- I tempi di firing assumono valori in insiemi densi =>
    - La relazione di raggiungibilità tra stati non è esplicitamente enumerabile.
    - Lo spazio degli stati viene coperto attraverso **classi di equivalenza**, ognuna delle quali raccoglie una varietà continua di stati con la stessa marcatura ma un diverso vettore dei tempi di firing.
![[Pasted image 20241029134103.png]]

---
**Analisi delle TPN: Preliminari(2/3)**

- Una **classe di stato** è una coppia $S=⟨m,D⟩$ in cui:
    - $m$ è una marcatura (che rappresenta la posizione logica del sistema).
    - $D$ è un insieme continuo di valori per i tempi di firing delle transizioni abilitate, denominato **dominio di firing**.
    
- Uno stato $s = \langle m_s, \overrightarrow{\tau_s} \rangle$ è incluso in una classe di stato $S = \langle m, D \rangle$ se:
    - possiedono la stessa marcatura (ossia, $m_s = m$).
    - il vettore dei tempi di firing $\overrightarrow{\tau_s}$​​ soddisfa i vincoli di $D$ (ossia, $\overrightarrow{\tau_s} \in D$).
- La forma dei vincoli di $D$ dipendono da:
	- Il modo in cui i tempi di fire sono avanzati nella semantica della TPN
	- La semantica delle relazioni di raggiungibilità da stabilire sulle classi di stato
	- La forma dei vincoli nella classe d stato iniziale
---
**Analisi delle TPN: Preliminari(3/3)**

- Una classe di stato $S′$ è **raggiungibile** dalla classe $S$ attraverso la transizione $t (S\xrightarrow{t} S′)$  se e solo se contiene tutti e solo gli stati raggiungibili da qualche stato raccolto in $S$ tramite un firing fattibile di $t$, ovvero:
    - $S′$ è raggiungibile da $S$ attraverso $t$ se e solo se:
        - $\forall s' \in S', \exists s \in S \, | \, s \xrightarrow{t} s'$.
        - $s \in S \land s \xrightarrow{t} s' \Rightarrow s' \in S'$

- Relazione di raggiungibilità debole, detta **raggiungibilità AE**.
    - Non garantisce che ogni stato $s' \in S'$ sia raggiungibile da ogni stato $s \in S$.
    - Garantisce che per qualsiasi stato $s' \in S'$ esista almeno uno stato $s \in S$ e un tempo $\tau$ tale che $t$ possa essere fired da $s$ con tempo di firing $\tau$ producendo lo stato $s'$.

- Sufficiente per decidere proprietà di raggiungibilità sotto vincoli temporali.
    - Uno stato $s′$ è raggiungibile da qualche stato nella classe iniziale $S_0$ se e solo se $s′$ è contenuto in una classe $S$ raggiungibile da $S_0$​.
    - Un sequenza di firing $\rho$ è firable se e solo se esiste una classe $S'$ raggiungibile da $S_0$ dalla quale esiste un percorso che riproduce gli stessi eventi di $\rho$
    
---
 **Analisi del TPN - Introduzione intuitiva (1/5)**

- Modello TPN con 3 transizioni concorrenti.
		![[Pasted image 20241029141157.png]]

	- I tempi di firing delle transizioni abilitate inizialmente variano in un iper-rettangolo. 
	
		$D = \begin{cases} 0 \leq \tau_1 \leq 10 \\ 5 \leq \tau_2 \leq 15 \\ 12 \leq \tau_3 \leq 22 \end{cases}$​
	
---

**Analisi del TPN - Introduzione intuitiva (2/5)**

- L'ipotesi che $t_2$​ sia la prima a essere attivata restringe il dominio di firing:

	$D_{t_2} = \begin{cases} 0 \leq \tau_1 \leq 10 \\ 5 \leq \tau_2 \leq 15 \\ 12 \leq \tau_3 \leq 22 \\ \tau_2 - \tau_1 \leq 0 \\ \tau_2 - \tau_3 \leq 0 \end{cases}$​

---

**Analisi del TPN - Introduzione intuitiva (3/5)**

- Sia $t_1$ che $t_3$ sono persistenti, quindi i loro tempi di firing sono traslati di $\tau_2$​:
	- $\tau'_1 = \tau_1 - \tau_2 \Rightarrow \tau_1 = \tau'_1 + \tau_2$
	- $\tau'_3 = \tau_3 - \tau_2 \Rightarrow \tau_3 = \tau'_3 + \tau_2$​

- Sostituendo le variabili $D_{t_2}$ può essere scritto in modo equivalente come:
	- $D_{t_2} = \begin{cases} 0 \leq \tau_1' + \tau_2 \leq 10  \space (a) \\ 5 \leq \tau_2 \leq 15 \space (b) \\ 12 \leq \tau_3' + \tau_2 \leq 22  \space (c) \\   0 \leq  \tau_1' \space (d) \\  0 \leq \tau_3'  \space(e) \end{cases}$

---

**Analisi del TPN - Introduzione intuitiva (4/5)**

- $\tau_2$​ viene eliminato per ottenere un dominio $D'$che dipende solo dai tempi di firing delle transizioni abilitate, ovvero:
	- $\langle \tau'_1, \tau'_3 \rangle \in D'$ se e solo se esiste $\tau_2$​ tale che $\langle \tau'_1, \tau_2, \tau'_3 \rangle \in D_{t_2}$ 
		- $D_{t_2} = \begin{cases} -15 \leq \tau_1' \leq 5  \space (a+ (-b))  \\ -3 \leq \tau_3' + \tau_2 \leq 17  \space (c+(-b)) \\ -22 \leq \tau_1' - \tau_3' \leq -2 \space (a+(-c)) \\ 0 \leq  \tau_1' \space (d) \\  0 \leq \tau_3'  \space(e) \\ \\ 5 \leq \tau_2 \leq 15 \space (b)\end{cases}$

		- $D' = \begin{cases} -15 \leq \tau'_1 \leq 5 \\ -3 \leq \tau'_3 \leq 17 \\ -22 \leq \tau'_1 - \tau'_3 \leq -2 \\ 0 \leq \tau'_1 \\ 0 \leq \tau'_3 \end{cases}$

---

**Analisi del TPN - Introduzione intuitiva (5/5)**

- Cosa significa il l'insieme $D'$ ?
	- La classe successore contiene tutti e i soli stati raggiungibili dalla classe iniziale:
		- $\forall \langle \tau_1', \tau_2' \rangle \in D'$ $\exists \langle \tau_1, \tau_2, \tau_3 \rangle \in D$ tale che $\tau_1' = \tau_1 - \tau_2 \land \tau_3' = \tau_3 - \tau_2$
		- Questa è la relazione di raggiungibilità AE

- Mentre per quanto riguarda la forma dei vincoli di 
	- Il dominio di firing $D$ della classe iniziale è un iper-rettangolo.
	- $D′$ è un insieme di disuguaglianze che vincolano le differenze tra i tempi di firing.
	- La forma di $D$′ è detta **Difference Bounds Matrix (DBM)**.
	- La derivazione ripetuta porta a un poliedro convesso lineare generale? No.(supercazzola) 

---
**Difference Bounds Matrix: definizione**

- Una DBM $D$ nello spazio di un vettore di valori incogniti $\tau = \langle \tau_0, \tau_1, \ldots, \tau_N \rangle$  è un insieme di disuguaglianze lineari che vincolano la differenza tra gli elementi di $\tau$: 
	- $D = \begin{cases} \tau_i - \tau_j \leq b_{ij} & \forall i, j \in \{0, 1, \ldots, N - 1\} \cup \{\star\} \text{ con } i \neq j, b_{ij} \in \mathbb{R} \cup \{\infty\} \\ \tau_\star = 0 \end{cases}$

- $\tau_\star$​ è una variabile fittizia, detta anche **ground**, utilizzata per:
    - convertire i vincoli della forma $\tau_i \leq b_{i\star}$​ in vincoli diagonali  $\tau_i - \tau_\star \leq b_{i\star}$
    - convertire i vincoli della forma $\tau_i \geq b_{i\star}$​ in vincoli diagonali  $\tau_i - \tau_\star \geq b_{i\star}$
    
- L'insieme delle soluzioni di un insieme di disuguaglianze in forma DBM è chiamato **zona DBM**
![[Pasted image 20241029163332.png]]

---
**Difference Bounds Matrix: Forma Normale(1/2)**

- Possono insiemi di disequazioni differenti rappresentare lo stesso insieme di soluzioni?
	- Alcuni vincoli possono essere implicati dalla combinazione di altri vincoli
	- Lo stesso insieme di soluzioni può essere rappresentato da diversi coefficienti $b_{ij}$
![[Pasted image 20241029163807.png]]
- Una **Forma Normale** è introdotta quando ogni coefficiente $b_{ij}$ è massivamente stretto
	- Ovvero non può essere ridotto senza cambiare l'insieme delle soluzioni

---
**Difference Bounds Matrix: Forma Normale(2/2)**

- Una DBM in è in **forma normale** se $b_{ij}$ è il massimo valore di $\tau_i - \tau_j$ che può essere ottenuto dall'insieme $\forall i, j \in \{0, 1, \ldots, N - 1\} \cup \{\star\} \mid i \neq j$
		![[Pasted image 20241029164330.png]]

- Una DBM non vuota è rappresentata come un **grafo** per dimostrate che la forma normale:
	- Esiste ed è unica
	- Sia calcolata come la soluzione del problema del _shortest path_ in tempo $O(N^3)$

---
**Difference Bounds Matrix: Rappresentazione grafica**

- La DBM identificata dalla matrice dei coefficiente $b{ij} è biunivocamente associata ad un **grafo completo diretto segnato** $\langle V, E, b \rangle$ dove:
	- Il set dei vertici V, consiste dei valori non conosciuti $\tau_i$
	- Un arco diretto esiste tra ogni due vertici ovvero $E = V$ x $V$ 
	- L'arco dal vertice $\tau_j$ fino al vertice $\tau_i$ è segnato come $b_{ij}$

	![[Pasted image 20241029165410.png]]

---
**Difference Bounds Matrix: Proprietà (1/4)**

- **Lemma 1**
	Se una zona DBM non è vuota, allora il grafo corrispondente non include nessun ciclo dove la somma delle etichette sui bordi attraversati risulta negativa (non ci sono **cicli negativi**)

---
**Difference Bounds Matrix: Proprietà (2/4)**

- **Lemma 2**
	Una DBM è in forma normale se e solo se $b_{ij}$ è il percorso più breve nel grafo dal vertice $\tau_j$ al vertice $\tau_i$   $\forall i, j \in \{0, 1, \ldots, N - 1\} \cup \{\star\} \mid i \neq j$
	
---
**Difference Bounds Matrix: Proprietà (3/4)**

- **Lemma 3**
	I coefficienti $b_{ij}$ sono il percorso più breve fra due vertici $\tau_j$ e $\tau_i$ se e solo se $b_{ij} \leq b_{ik} + b_{kj}$  $\forall i, j, k \in \{0, 1, \ldots, N - 1\} \cup \{\star\} \mid i \neq j, i \neq k, j \neq k$

---
**Difference Bounds Matrix: Proprietà (4/4)**

- **Teorema**
	Una DBM è in forma normale se e solo $b_{ij} \leq b_{ik} + b_{kj}$ $\forall i, j, k \in \{0, 1, \ldots, N - 1\} \cup \{\star\} \mid i \neq j, i \neq k, j \neq k$

---
**Difference Bounds Matrix: Come calcolare la forma normale?**

- La forma normale può essere calcolata tramite l'algoritmo di **Floyd-Warshall**
	- N iterazioni indicizzate da $k = 0,1, ... , N-1$
	- All'iterazione k si deriva $b_{ij}^{k+1}$ definita come il percorso più breve da $\tau_j$ a $\tau_i$ che non visita nessun nodo intermedio con indice più grande di k
		- **Inizializzazione**: $b_{ij}^0$ è il valore iniziale del coefficiente $b_{ij}$
		- **Prima iterazione**(k = 0): $b_{ij}^1$ è  il percorso più breve da $\tau_j$ a $\tau_i$ che non visita nessun nodo intermedio con indice più grande di 0
		- **Ultima iterazione** (k = N- 1): $b_{ij}^N$ è  il percorso più breve da $\tau_j$ a $\tau_i$ 
-![[Pasted image 20241029173429.png]]

---
**Difference Bounds Matrix: decidere se vuoto**

- **Lemma 5**
	Se il grafo corrispondente a una DBM non è vuota, non include nessun cicli negativo, allora la zona DBM non è vuota
	
- **Lemma 6**
	Una zona DBM e non è vuota, se e solo se il grafo corrispondente non include nessun ciclo negativo

---
**Difference Bounds Matrix: Proiezione**

- Data una DBM $D$ nello spazio dei valori sconosciuti $\tau = \langle \tau_0, \tau_1, ...,  \tau_{N-1} \rangle$, la **proiezione** di $D$ sullo spazio di valori sconosciuti  $\tau_{↓0} = \langle \tau_1, ...,  \tau_{N-1} \rangle$, è 
	- $D_{↓0} = \{ \langle \tau_1, ...,  \tau_{N-1} \rangle \mid  \exists \tau_0 \in R \cup \{∞\} \text{tale che} \langle \tau_0, \tau_1, ...,  \tau_{N-1} \rangle \in D\}$ 
- La proiezione è usata nell'enumerazione della relazione di raggiungibilità fra le classi di stati
- La proiezione è implementata in modo efficiente su una zona DBM in forma normale

- Lemma 7
	Se una DBM $D$ nello spazio dei valori sconosciuti $\tau = \langle \tau_0, \tau_1, ...,  \tau_{N-1} \rangle$ è in forma normale, allora la matrice dei coefficienti della proiezione $D_{↓0}$ è ottenuta tramite la matrice dei coefficienti di $D$ eliminando la riga e la colonna degli zeri, ovvero il grafo $D_{↓0}$ è ottenuto dal grafo $D$ eliminando il nodo $\tau_0$ (senza cambiare i vincoli fra gli altri nodi)

--- 
**Analisi del TPN - Classe di stato iniziale**

- Assumiamo che il dominio di abilitazione $D$ della classe di stato iniziale $S=⟨m,D⟩$ sia rappresentato come un insieme di disuguaglianze lineari in forma normale DBM, cioè: $D=\{τ(t_i​)−τ(t_j​)≤b_{ij} ​∀ t_i​, t_j​∈T_e(m) ∪ \{t_∗\}$ con $i \neq j\}$ dove:
	- $b_{ij} \in R∪\{∞\}$
	- $T_e(m)$ è l'insieme delle transizioni abilitate dalla marcatura $m$
	- $\tau(t_i)$ è il tempo di attivazione della transizione $t_i$ $\forall t_i \in T_e(m)$
	- $t^*$ è l'evento fittizio di ingresso nella classe
	- $\tau(t^*)$ è il **ground** time al quale la classe è entrata

---
**Analisi del TPN: esistenza del successore**

- Una classe di stato $S = \langle m, D \rangle$ con $D$ in forma normale DBM ha un **successore** attraverso la transizione $t_0$ se e solo se $t_0$ è abilitata da $m$ e $D$ accetta soluzioni in cui $\tau(t_0)$ non è maggiore del tempo di attivazione di qualsiasi altra transizione abilitata, cioè, il **dominio di attivazione ristretto** $D_{t_0}$ ha un insieme di soluzioni non vuoto:
- $D_{t_0} = \begin{cases} \tau(t_i) - \tau(t_j) \leq b_{ij} \\ \tau(t_0) - \tau(t_h) \leq 0 \\ \forall \, t_i, t_j \in T_e(m) \cup \{t^*\} \, \text{con} \, t_i \neq t_j, \, \forall \, t_h \in T_e(m) \setminus \{t_0\} \end{cases}$

- **Lemma 8**  
	Una classe di stato  $S = \langle m, D \rangle$ con $D$ in forma normale DBM ha un successore attraverso la transizione $t_0$ se e solo se $t_0 \in T_e(m)$ e $b_{h0} \geq 0 \space \forall \space t_h \in T_e(m)$.

- **Rilevamento del successore**: complessità lineare rispetto al numero di transizioni abilitate.
- Come calcolare il dominio di attivazione $D'$ del successore $S'$ di $S$ attraverso $t_0$?
 
---
**Analisi TPN: calcolo del successore - condizionamento**

- Condiziona $D$ al fatto che $t_0$ si attivi per prima:
	- $D_{t_0} = \begin{cases} \tau(t_i) - \tau(t_j) \leq b_{ij} \\ \tau(t_0) - \tau(t_h) \leq 0 \\ \forall \, t_i, t_j \in T_e(m) \cup \{t^*\} \, | \, t_i \neq t_j, \\ \forall \, t_h \in T_e(m) \setminus \{t_0\} \end{cases}$ 
	     $= \begin{cases} \tau(t_i) - \tau(t_j) \leq b_{ij} \\ \tau(t_0) - \tau(t_h) \leq \min \{0, b_{0h} \} \\ \forall \, t_i, t_j \in T_e(m) \cup \{t^*\} \, | \, t_i \neq t_j, \\ \forall \, t_h \in T_e(m) \setminus \{t_0\} \end{cases}$

- Rappresenta $D_{t_0}$ in forma normale e siano $B_{ij}$ i suoi coefficienti (complessità quadratica rispetto al numero di transizioni abilitate): 
- $D_{t_0} = \begin{cases} \tau(t_i) - \tau(t_j) \leq B_{ij} \\ \tau(t_0) - \tau(t_i) \leq B_{0i} \\ \forall \, t_i, t_j \in T_e(m) \cup \{t^*\} , t_i \neq t_j, \, t_i \neq t_0 \end{cases}$

---
**Analisi TPN: calcolo del successore - avanzamento temporale**

- Si riduce i tempi di fire delle transizioni persistenti in $S_0$ del tempo trascorso in $S$, cioè, $\tau'(t_i) = \tau(t_i) - \tau(t_0)$ $\forall t_i \in T_e(m) \cap T_p(S_0) \setminus \{t_0\}$, dove $T_p(S_0)$ è l’insieme delle transizioni persistenti in $S_0$: ![[Pasted image 20241029231440.png]]

---
**Analisi del TPN - Successione di Computazione (Proiezione)**

- Eliminare il tempo di firing della transizione attivata tramite una proiezione: 
	- $D''_{t_0} = \begin{cases} \tau'(t_i) - \tau'(t_j) \leq B_{ij} \\ \tau'(t_i) \leq B_{i0} \\ -\tau'(t_i) \leq B_{0i} \\ \forall t_i, t_j \in T_e(m) \cup \{t_*\} \mid t_i \neq t_j, t_i \neq t_0 \end{cases}$
- Siano $C_{ij}$ i coefficiente in forma normale ovvero $C_{ij} = B_{ij}, C_{i*} = B_{i0}, C_{*i} = B_{0i}$:
	- $D''_{t_0} = \begin{cases} \tau'(t_i) - \tau'(t_j) \leq C_{ij} \\ \tau'(t_i) - \tau'(t_*) \leq C_{i*} \\ -\tau'(t_*) - \tau'(t_i) \leq C_{*i} \\ \forall t_i, t_j \in T_e(m) \cap T_p(S') \cup \{t_*\} \mid t_i \neq t_j, t_i \neq t_0 \end{cases}$
	(Con $T_p(S')$ insieme delle transizioni persistenti in S')
- I times-to-fire delle transizioni non abilitate da $m'$ possono essere eliminate in modo simile
---
**Analisi del TPN : Computazione delle Successioni - newly enabling

- Aggiungere il tempo di firing di ogni transizione appena abilitata:
	- $D' = \begin{cases} D''_{t_0} \\ \tau'(t_j) - \tau'(t_*) \leq LFT(t_j) \\ \tau'(t_*) - \tau'(t_j) \leq -EFT(t_j) \\ \forall t_j \in T_n(S') \end{cases}$
		Dove $T_n(S')$ è l'insieme delle transizione newly-enable in $S'$

- Il dominio di firing di $D'$ della classe successore $S'$ è sempre in forma normale! 
	- => La forma della DBM è chiusa rispetto ai passi per il calcolo del successore
	- => La relazione di raggiungibilità fra gli della classe può essere enumerata![[Pasted image 20241030082330.png]]

---
**Analisi del TPN : enumerazione spazio degli stati**

- L'enumerazione risiede nel **grafo della classe degli stati**
- Una **corsa simbolica** è un percorso nel grafo della classe degli stati
	- Rappresenta la varietà densa di corse firing dato un set di transizioni in un dato ordine qualitativo, con una varietà densa di timings fra due firings successivi
	- Ad esempio $S_0 \rightarrow^{t_0}  S_1 \rightarrow^{t_2} S_4 \rightarrow^{t_1} S_6$ 
![[Pasted image 20241030082856.png]]
---
**Dominio dei tempi di una corsa simbolica**

- Si consideri una cosa simbolica $\rho = S_0 \rightarrow^{t^0_{f(0)}} S_1 \rightarrow^{t^1_{f(1)}} S_2 ... S_{N-1} \rightarrow^{t^{N-1}_{f(N-1)}} S_N$ 
	- $S_0 = \langle m_0, D_0 \rangle$ è la classe di stato iniziale
	- $S_n = \langle m_n, D_n \rangle$ è la classe di stato n-esima visitata da $\rho \space \forall n \in \{ 1, ..., N\}$
	- $f(n)$ è l'indice della transizione fired nella classe stato $S_n$ $\forall n \in {0,1,..., N-1}$
	- $t_h^k$ è il tempo di fire della trasizione $t_h$ nella classe stato $S_k$ 
- Il dominio dei timings di $\rho$ è nella forma DBM:
	- $D_{\rho} = \begin{cases} D_{n} \\ \tau(t_{f(n)}^n) - \tau(t_i^n) \leq 0 \\ \tau(t^n_{f(n)}) = \tau(t^{n+1}_*) \\ \forall n \in \{0,1, ..., N-1\}, \forall t_i^n \in T_e(m) \end{cases}$
- I tempi di soggiorno in classi non sono indipendenti => Il caso peggiore  di completamento di $\rho$ può non essere la somma casi peggiori di soggiorno in $S_0, ..., S_{N-1}$
- Computazione di $D_{\rho}$: complessità $O(N^3)$
	- Notare che N è il numero di transizioni fired tra $\rho$
	- Il numero di transizione abilitate fra $\rho$ può essere $>> N$
---
**Modellazione di insiemi di task in tempo reale con TPN: un esempio (3/3)**

- Le 2 slide prima sono di riepilogo
- Entrambi i task hard real-time possono perdere la loro deadline:
- ![[Pasted image 20241030150031.png]]

- Come decidere l'accettazione rifiuto dei job di $P_3$ a runtime? Usando i tempi **attuali** di esecuzione per determinare se il fallimento simbolico delle runs sono fattibili!
	- Un Job di $P_3$ sarà rifiutato se un job di $P_1/P_2$ può perdere la sua deadline.

---
**Scheduling online in un sistema di analisi biologica (1/5)**

- Preso un sistema elettromeccanico per l'analisi immunoenzimatica
	- Ogni slot comprende diverse provette
	- Una pipetta e una testina può agire in modo simultaneo sulle provette
	
![[Pasted image 20241108175709.png]]	

---
**Scheduling online in un sistema di analisi biologica (2/5)**

- Un Esempio del problema di schedulabilità
- 4 jobs $J_1, J_2, J_3, J_4$ allocati su due macchine $M_1, M_2$
- $e$ indica il tempo di esecuzione, $r$ indica il tempo di rilascio
- $J_2$ è in mutua esclusione con $J_4$
- $J_2$ ha dei vincoli di precedenza rispetto al completamento di $J_1$ e $J_2$
- $J_4$ ha dei vincoli di precedenza rispetto al completamento di $J_3$

![[Pasted image 20241108180149.png]]

---
**Scheduling online in un sistema di analisi biologica (3/5)**

- Uno scheduling che minimizza il tempo di completamento totale
![[Pasted image 20241108180425.png]]

- Come ottenere tale schedule?

---
**Scheduling online in un sistema di analisi biologica (4/5)**

- Codifica TPN per sequenziare e vincolare temporalmente il problema di scheduling.
- L'esecuzione è corretta se e solo se non visita mai una classe di stato dove:
    - Il posto $p_2$​ ha un token mentre il posto $p_{2e}$ è vuoto.
    - I posti $p_2$​ e $p_4$​ contengono entrambi un token.

![[Pasted image 20241108180735.png]]

---
**Scheduling online in un sistema di analisi biologica (5/5)**

- Enumerazione del grafo delle classi di stato per derivare una sequenza.
- Ottimizzazione: enumerazione euristica del grafo delle classi di stato.
- Test su casi impegnativi (es., 24 azioni pipettatrici, 8 azioni di lettura).
- Più veloce comparato ad un tradizionale di model checking 
- Implementazione software su un sistema reale.

---
## Reti di Petri Temporali Preemptive (PTPN) (TBD - da riguardare)

- **Sintassi delle PTPN**
  - Le PTPN estendono le TPN con risorse.
  - Una PTPN è una tupla $\langle P, T, A^-, A^+, A^{\bullet}, EFT, LFT, Res, Req, Prio \rangle$ dove:
    - $Res$ è un insieme di risorse.
    - $Req$ associa a ciascuna transizione $t$ un sottoinsieme di risorse $Req(t) \subseteq Res$.
    - $Prio$ associa a ciascuna transizione $t$ una priorità $Prio(t) \in \mathbb{N}$ (più basso è il numero di priorità, più alto è il livello di priorità).

---

#### Stato di una PTPN

- Lo stato di una PTPN è una coppia $\langle m, \tau \rangle$ dove:
  - $m$ è una marcatura (rappresenta la posizione logica del sistema).
  - $\tau$ associa a ciascuna transizione abilitata $t$ un tempo di attivazione $\tau(t) \in \mathbb{R}_{\geq 0}$.
  
- **Esempio**:
  - $t_{10}$ può essere associata a un tempo di attivazione $\tau(t_{10}) = 5$.
  - $t_{20}$ può essere associata a un tempo di attivazione $\tau(t_{20}) \in [10, \infty]$.
  - $t_{30}$ può essere associata a un tempo di attivazione $\tau(t_{30}) = 15$.

---

### Semantica delle PTPN (1/5)

- Come nelle PN con archi inibitori, una transizione $t$ è abilitata da una marcatura $m$ se:
  - $m(p) > 0 \, \forall p \in P \mid (p, t) \in A^-$.
  - $m(p) = 0 \, \forall p \in P \mid (p, t) \in A^{\bullet}$.

- Una transizione $t$ è in progressione in una marcatura $m$ se:
  - È abilitata da $m$.
  - $Req(t) \cap Req(t') \neq \emptyset \Rightarrow Prio(t) < Prio(t') \, \forall t' \in T_e(m)$ (ovvero, ogni risorsa richiesta non è richiesta da un'altra transizione abilitata con livello di priorità più alto).

---

### Semantica delle PTPN (2/5)

- In ogni possibile stato iniziale dell'esempio di PTPN:
  - $t_{10}, t_{20}, t_{30}$ e $t_{11}$ sono in progressione.
  - $t_{21}$ e $t_{31}$ sono sospese.

---

### Semantica delle PTPN (3/5)

- L'attivazione di una transizione $t$ sostituisce $s_0 = \langle m_0, \tau_0 \rangle$ con $s_1 = \langle m_1, \tau_1 \rangle$.
  - Come nelle PN, $m_1$ è derivata da $m_0$:
    1. Rimuovendo un token da ciascun posto di ingresso di $t$.
    2. Aggiungendo un token a ciascun posto di uscita di $t$.

---

## Utilizzo delle PTPN nel ciclo di vita software V-Model

---
**Slide 96**  
**Modellazione e analisi di set di task in tempo reale con la teoria delle PTPN**

- Rappresentazione di set di task con politiche di scheduling **preemptive** 
	- es. scheduling preemptive a priorità fissa
- **Raggiungibilità temporale**: può il set di task raggiungere una condizione logica specifica?
	- es. verificare la correttezza della sequenza che non abbia inversione di priorità
- Analisi della tempestività: qual è il tempo minimo/massimo tra eventi specifici?
	- es. calcolare il miglior/peggior caso di tempo di completamento per ogni task

![[Pasted image 20241108183647.png]]

---
**Slide 97**  
**È solo una questione di verifica?**

- Le PTPN come nucleo formale di un approccio di Model Driven Development (MDD)
    - Derivazione automatica di PTPN da timeline
    - Generazione automatica di codice
    - Misura del tempo di esecuzione delle funzioni di ingresso
    - Selezione ed esecuzione dei casi di test
    - Verdetto dell'oracolo
    
- Organizzato in un ciclo di vita completo del software:
    - Basato sul V-Model industriale
    - Basato su standard normativi (RTCA-178B)
    - Formalizzato in termini di artefatti del profilo UML per MARTE (Modeling and Analysis of Real-Time and Embedded Systems)

---
**Slide 98**  
**V-Model**

- Riferimento per il ciclo di vita del software nei sistemi critici per la sicurezza (*safety critical*)
- Integrazione di *design e verifica* (sinistra/destra)
- Decomposizione dal sistema ai moduli (alto/basso)![[Pasted image 20241108183938.png]]

---
**Slide 99**  
**V-Model adattato secondo MIL-STD-498**

- Integrazione di metodi formali nel ciclo di sviluppo richiede metodi di SW engineering  senza interrompere i processi industriali
	- Il processo di sviluppo V-model è supportato dalla teoria PTPN
	- La documentazione MIL-STD-498 è supportata da UML-MARTE

![[Pasted image 20241108184351.png]]

---

**Slide 100**  
**Studio di caso**

- Sistema **elettro-ottico** di un veicolo militare, sviluppato da Selex-Galileo (ora Leonardo)
	- Garanzia di vantaggio sul campo di battaglia grazie a visione, immagini infrarosse e termiche, acquisizione di obiettivi a lungo raggio e puntamento preciso
	
- Il sistema Comprende:
    - **Unità ottica** (OU) fatta di sensori, camere e servo-motori
    - **Unità elettronica** (EU) responsabile per il controllo dei sensori e il processamento delle immagini
    - Unità di monitoraggio del sistema (SMU) che organizza l'intero sistema.

- L'EU tiene il ruolo fondamentale di ponte per la comunicazione fra SMU e OU
	- Ripassa i comandi mandati periodicamente dalla SMU alla OU
	- Manda i corrispondenti messaggi dell'OU all'SMU

- L'EU processa le immagini acquisite dall'OU e manda i risultati ottenuti all'SMU
- L'esperimento della metodologia formale nella costruzione dell'EU in un anno di ricerca in collaborazione con *Selex-Galileo* (ora Leonardo), fu supportato dall'iniziativa software del gruppo di FinMeccanica.

---
**Slide 101**  
**V-Model: SD1, SD2, SD3**

- **SD1** (System Requirements Analysis) - ambito del sistema  
  - Definisce i requisiti utente ad alto livello del sistema

- **SD2** (System Design) - ambito del sistema  
  - Identifica le unità di sistema e assegna loro i requisiti utente

- **SD3** (SW/HW Requirements Analysis) - dal sistema all'ambito delle unità  
  - Scompone ogni unità in Elementi di Configurazione Hardware (HCIs), Elementi di Configurazione Software (CSCIs) e Elementi di Configurazione Firmware (FCIs)
![[Pasted image 20241108190239.png]]
---
**Slide 102**  
**MIL-STD-498: Analisi e Progettazione Sistema/Sottosistema**

- Integra SD1, SD2 e la prima parte di SD3 (ambito del sistema)
- Produce la Descrizione del **Sistema/Sottosistema** (SSDD)
  - Rappresentata qui tramite diagramma UML-MARTE delle componenti del sistema

![[Pasted image 20241108190745.png]]

---
**Slide 102** 
**MIL-STD-498: Analisi Requisiti Software**

- Corrisponde alla seconda parte di SD3 (lo scope CSCI)
- Produce la Specifica dei Requisiti Software( SRS) per ogni CSCI e la Specifica dei Requisiti d'Interfaccia (IRS) per ogni unità software
	- Qui l'SRS è in una forma simile alle carte CRC (Class Resp. Collaboration)
		- es. carta CRC che specifica le capacità del sistema di Controllo CSCI (sinistro)
		- es. carta CRC che specifica le sottocapacità dell'SMU-OU-Comandi (destra) 

![[Pasted image 20241108191851.png]]

 ![[Pasted image 20241108191908.png]]

---
**Slide 103**  
**V-Model: SD4-SW, SD5-SW**

- **SD4-SW** (Preliminary SW Design) - ambito del componente SW  
  - Definisce **l'architettura SW** di ogni CSCI come un insieme di task di comunicazione con moduli funzionali e tempi di rilascio e scadenze prescritte

- **SD5-SW** (Detailed SW Design) - ambito del modulo SW  
  - Definisce il **design SW** di ogni CSCI assegnando risorse e requisiti di tempo a ciascun modulo software
  - Include la SD5.2-SW (Analisi dei requisiti di risorse e del tempo)
  
![[Pasted image 20241108192314.png]]

---
**Slide 105**  
**MIL-STD-498: Design del Software**

- Integra SD4-SW e SD5-SW
- Produce la Descrizione del Design del Software (SDD) -> Software Design Description
![[Pasted image 20241108192314.png]]

---
**Slide 106**  
**Design del SW: specifica semi-formale tramite UML-MARTE**

- Specifica dei requisiti **non funzionali** di ciascun CSCI  
  - Tramite diagramma UML-MARTE a oggetti per ogni task
  
![[Pasted image 20241108192617.png]]

- Specifica dei requisiti funzionali di ciascun CSCI  
  - Tramite diagramma UML-MARTE delle attività per ogni task

![[Pasted image 20241108192643.png]]

---
**Slide 107**  
**Design del SW: specifica semi-formale tramite timeline**

- Derivabile (manuale/automatica) dai diagrammi UML-MARTE

- Rappresenta sinteticamente e intuitivamente un insieme di task
- Non supporta la verifica automatizzata del modello

![[Pasted image 20241108192811.png]]

---
**Slide 108**  
**Design del SW: specifica formale tramite PTPNs**

- Derivabile (manuale/automatica) dalle timeline
- Supporta la verifica formale e i successivi passi di sviluppo

![[Pasted image 20241108193544.png]]

---
**Slide 109**  
**Design del SW: derivazione di PTPNs dalle timeline (1/3)**

- Rappresentazione dei rilasci di task
![[Pasted image 20241108193608.png]]
- Rappresentazione di task con più segmenti sequenziali
![[Pasted image 20241108193625.png]]
---

**Slide 110**  
**Design del SW: derivazione di PTPNs dalle timeline (2/3)**

- Rappresentazione dei task sincronizzati su un semaforo

![[Pasted image 20241108193707.png]]

---
**Slide 111**  
**Design del SW: derivazione di PTPNs dalle timeline (3/3)**

- Rappresentazione dei task sincronizzati su una mailbox

![[Pasted image 20241108193805.png]]

---
**Slide 112**  
**SD5.2-SW: Analisi delle risorse e dei requisiti di tempo**

- Simulazione del modello PTPN
	- Gioco interattivo di token online
	- Derivazione offline di statistiche
	
- Analisi dello spazio degli stati del modello PTPN
	  - Copertura esaustiva dello spazio degli stati (salvo esplosione dello stato)
	  - Verifica delle proprietà di sequenziamento e tempestività
	
![[Pasted image 20241108194300.png]]

---
**Slide 113**  
**V-Model: SD6-SW**

- SD6-SW: **Implementazione del software** - ambito del modulo SW
	  - Implementazione dell'architettura dei task set (architettura eseguibile)
	  - Test unitario (profilatura del tempo di esecuzione dei moduli a basso livello)
	  - Implementazione delle funzioni di ingresso (fuori dall'ambito del metodo)

![[Pasted image 20241108194536.png]]

---
**Slide 114**  
**MIL-STD-498: Codifica del software**

- Corrisponde alla prima parte di SD6-SW

- Produce l'architettura del task set di ogni CSCI (architettura dinamica)
	- Uno scheletro di **codice di controllo** che implementa il comportamento **non funzionale** dei task e invoca il **codice funzionale** delle funzioni di ingresso

---
**Slide 115**  
**Codifica del software: implementazione dell'architettura del task set (1/5)**

- Responsabilità
  - Rilasciare job di task in base alle loro politiche
  - Implementare operazioni su semafori e gestione delle priorità
  - Sequenziare l'invocazione delle funzioni di ingresso
  
- Struttura
  - Riflette la specifica della timeline
  - Basata su primitive convenzionali di un sistema operativo in tempo reale
  - Esperimenti su codice C per applicazioni a singolo processore (VxWorks, Linux RTAI)
  - è codice disciplinato oppure Model Driven Development (MDD)?

---
**Slide 116**  
**Codifica del software: implementazione dell'architettura dinamica (2/5)**

- Diagramma UML-MARTE della struttura dell'implementazione dell'architettura dinamica di un CSCI su **VxWorks 6.5**

![[Pasted image 20241108195409.png]]

---
**Slide 117**  
**Codifica del software: implementazione dell'architettura dinamica (3/5)**

- Diagramma UML-MARTE della struttura dell'implementazione dell'architettura dinamica di un CSCI su Linux-RTAI 3.3

![[Pasted image 20241108200115.png]]

---
**Slide 118**  
**Codifica del software: implementazione dell'architettura dinamica (4/5)**

- Frammento dell'architettura dinamica di un CSCI su **Linux-RTAI 3.3**
	- L'architettura del codice riflette il modello PTPN
	- Il programmatore mantiene il pieno controllo sul codice

![[Pasted image 20241108200223.png]]

---
**Slide 119**  
**Codifica del software: implementazione dell'architettura dinamica (5/5)**

- Emula il tempo di esecuzione delle funzioni di ingresso tramite una funzione di *busy-sleep* 
	- es. il loop deterministico che usa la cpu per tempo di exec controllato

- Consiste di una **architettura eseguibile** (Unified Process)
- Porta a una baseline per integrazioni incrementali delle funzioni di ingresso

![[Pasted image 20241108200923.png]]

---
**Slide 120**  
**MIL-STD-498: Prima parte del testing dell'HW-nel-loop**

- Corrisponde alla seconda parte del SD6-SDW

- Esegue **unit-testing**, cioè, il testing di ogni modulo SW (riferito anche ad unità di basso livello), nell'architettura dinamica di ogni CSCI
	- Include altri moduli SW emulati tramite funzioni di busy-sleep
	- Integra ogni modulo SW entro il range dei comportamenti che sono feasibile per la specifica => permette di evitare il noto problema della **determinazione dell'implementazione** con rispetto alla specifica

![[Pasted image 20241108194536.png]]

---
**Slide 121**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (1/6)**

- L'architettura eseguibile può essere automaticamente strumentata per produrre *log con timestamp* degli eventi corrispondenti alle transizioni nel modello PTPN
	- Consente la ricostruzione del tempo di esecuzione di ogni funzione di ingresso:
$$
 ET(t_{i}^n) = \sum_{k=n}^{K_{i,n}-1} c_{i,k} \cdot (\tau_{k+1} - \tau_{k})
$$
		- $t_i^n$ è l'istante della transizione $t_i$ newly-enabled nell'n-esimo stato visitato
		- $c_{i,k}$ è 1 o 0 se $t_i$ va avanti oppure è sospeso nell'k-esimo stato visitato
		- $K_{i,k}$ è l'indice (nella traccia) dello stato raggiunto tramite il firing di $t_i^n$ 
		- $\tau_k$ è il tempo di entrata nel k-esimo stato visitato, ovvero il k-esimo *timestamp*

- Identifica il comportamento dell'implementazione rispetto alla specifica

![[Pasted image 20241108202524.png]]

---
**Slide 122**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (2/6)**

- Approccio basato su **misurazione** per l'analisi del tempo di esecuzione
- Eseguito in modalità interrotta => considerando effetti di cambio di contesto, preemption, interruzioni hardware e software, cache e pipeline.
- Quale sarà l'impatto delle operazioni di logging sui tempi di esecuzione misurati?

---
**Slide 123**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (3/6)**

- Esegue un grande numero di ripetizioni per l'operazione di log (10,000)
	- Sequenza dei tempi di esecuzione osservati per l'operazione di log

- Approccio semplice ma grossolano, con logging che richiede decine di microsecondi
	- Intervalli di min-max associati con parametri temporali sono aumentati duranti cicli di raffinamento iterativi per l'architettura dinamica di ogni CSCI

![[Pasted image 20241109121613.png]]

---
**Slide 124**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (4/6)**

- Istogramma fra i tempi di rilascio osservati di un task periodico *Tsk2*
	- Il periodo nominale è pari a 20ms
	- Il periodo osservato rientra entro [19.920, 20.069] ms nel 98.9% dei casi
	
- La variabilità osservata non è trascurabile: che possiamo fare?
	- Sistemare l'implementazione: non praticabile dato che il jitter dipende dalle RTOS
	- Ridefinire il modello: non conveniente siccome aumenta la spazio degli stati!
	- Aggiungi un warning per le prossime tappe di testing
	
![[Pasted image 20241109122324.png]]

---
**Slide 125**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (5/6)**

- Istogramma dell'esecuzioni osservate dell'entry-point f122 di *Tsk1*
	- Tempo di esecuzione nominale entro l'intervallo [0.05, 0.2] ms
	- Riflette l'assenza delle alternative dipendenti dai dati, nell'implementazine della funzione di entry-point (altrimenti l'istogramma avrebbe avuto un maggiore supporto)

![[Pasted image 20241109122635.png]]

---
**Slide 126**  
**HW-in-the-loop testing: profilazione del tempo di esecuzione (6/6)**

- Istogramma dei tempi di esecuzione osservati delle operazioni di *wait* fatte dal task periodico *Tsk2* sul semaforo binario *sem3*
	- Il tempo speso per le operazioni del semaforo su VxWorks 6.5 non è trascurabile con rispetto all'ordine dei tempi di esecuzione delle funzioni entry-point

![[Pasted image 20241109122947.png]]

---
**Slide 127**  
**V-Model: prima parte di SD7-SW**

- Prima parte di SD7-SW: integrazione SW a livello di componente
- Corrisponde alla seconda parte del test dell' HW-in-the-loop nel MIL-STD-498
- Attività supportate dal nucleo formale delle PTPNs:
	- Selezione dei test case ed esecuzione
	- Verdetto dell'oracolo e valutazione del coverage

![[Pasted image 20241109123240.png]]

---
**Slide 128**  
**Modello di guasti e difetti**

- **Guasti**: scostamenti di un componente dalla prestazione prevista 
	- **Sequenze non ordinate**: un esecuzione che rompre la sequenza dei requirements
		- es. sequenza di chunk, semaforo e operazione di gestione della priorità, meccanismi di IPC, ...
	- **Violazioni temporali**: un parametro temporale che prendere valori fuori il suo intervallo nominale
		- es. release di un job prematuro, tempo di esecuzione $\notin$ [BCET, WCET]
	- **Miss della Deadline**: un job che rompe il suo requisito di tempo

- **Difetti**: errori in un componente che possono causare fallimenti al sistema
	- **Difetto nella programmazione dei task**: difetto nel controllo concorrente e nell'interazione dei task
		- es. le operazioni sui semafori non combinate per bene con la gestione della priorità, errato assegnamento della priorità, invocazione non sequenziata delle entry-points
	- **Cycle stealing**: la detrazione delle risorse computazioni dovuti a task addizionali, omessi intenzionalmente o non omessi nella specifica

- Le deadline mancate dai task ha pertinenza conctrattuale
- I fallimenti nelle sequenze/tempi die chunk ha pertinenza per il design e lo unit testing

- Il comportamento funzionale non è descritto

---
**Slide 129**  
**SD7-SW: quale astrazione per la selezione dei casi di test?**

- Gli standard di certificazione prescrivono criteri di copertura strutturale, misurati sul grafo di *controllo del flow* del codice
	- es. tutti gli statements, le decisioni, le condizioni modificate in base alle decisioni, ...
	- Usare efficacemente strutture di controllo e dipendenze del data-flow
	- Copertura limitata della varietà di comportamenti che risultano dalla concorrenza e esecuzione interrotta dell'architettura dinamica di ciascun CSCI
- Il **grafico delle classi di stato** (SCG) del modello PTPN di un CSCI è un astrazione efficace della varietà dei comportamenti della struttura dinamica CSCI 
	- Generatore di codice qualified => SCG fornisce una misura della coverage **strutturale**
	- Generatore di codice non qualified => SCG fornisce un astrazione funzionale

![[Pasted image 20241109131724.png]]

---
**Slide 130**  
**SD7-SW: criteri per la selezione dei casi di test sul SCG (1/3)**

- **Tutte le marcature**:
	- Richiede la coverage di ogni marcatura raggiungibile
	- Garantisce la coverage di tutti i possibili stati concorrenti, ovvero tutte le possibili combinazioni dei chunks che sono concorrentemente running/pronti/bloccati
	- Per ogni marcatura raggiungibile $m$, seleziona una qualsiasi classe $S_m$ con la marcatura $m$ e includi nella suite di test qualsiasi percorso da un *Controllable Starting Point* (CSP) a $S_m$
	- Complessità proporzionale al numero di marcature raggiugibili
	
- **Tutte le marcature ai bordi (include tutte le marcature)**: 
	- Richiede la coverage di ogni bordo fra due marcature raggiungibile
	- Garantisce la coverage fra tutte le possibile transizioni fra stati concorrenti,
		- es. preemptions che seguono i rilasci asincroni, il completamento di chunk, operazioni fra semafori e mailbox, operazioni di boost/deboost di priorità
	- Complessità proporzionale al numero di marcature raggiugibili, moltiplicato per il massimo numero di eventi in una marcatura (l'ultimo è $\leq$ numero di tasks)
	- Per ogni bordo fra due marcature $m_1$ e $m_2$, seleziona qualsiasi classe $S_1$ con la marcatura $m_1$ con un evento che porta alla classe $S_2$ con la marcatura $m_2$, e includere nella suite di test qualsiasi percorso che comincia da un CSP e coprire il bordo

---
**Slide 131**
**SD7-SW: Criteri per la Selezione dei Test Case sul SCG (2/3)**

- **Tutte le classi (include tutte le marcature):**
  - Richiede la copertura di ogni classe di stato raggiungibile.
  - Distingue gli stati concorrenti associati con timings differenti generati dall'esecuzione di diverse sequenze di transizione di firings
  - Aumenta la complessità con rispetto a tutte le marcature 

- **Tutti i bordi delle classi (include tutte le marcature-bordi):**
  - Richiede la copertura di ogni bordi fra le classi di stato raggiungibili.
  - Distingue gli stati di concorrenza associati con timings differenti generati dall'esecuzione di diverse sequenze di transizione di firings
  - Aumenta la complessità con rispetto al top di tutte le classi di archi.
  
---

**Slide 132: SD7-SW: Criteri per la Selezione dei Test Case sul SCG (3/3)**

- **Tutte le run simboliche (includendo le classi-bordi):**
  - Richiede la copertura di ogni run simbolica che comincia con un rilascio di un job e termina o con il suo completamento oppure con una deadline mancata.
  - Distingue gli stati concorrenti e le transizioni visitate in diverse esecuzioni del job
  - Aumenta la complessità con rispetto al top di tutte le classi di archi.
  
  - **Tutte le esecuzioni simboliche:**
  - Richiede la copertura di ogni sequenza di eventi che comincia con un rilascio di un job e termina o con il suo completamento oppure con una deadline mancata.
  - Non distingue i percorsi con la stessa sequenza di firing in diverse classi di partenza
  - Diminuisce la complessità di tutte le run simboliche
  
---
**Slide 133**
**SD7-SW: Strategie di Test Basate sulla Complessità del Modello**

- Come determinare certi input temporali che forzano **l'implementation Under Test** (IUT) a eseguire ogni test case selezionato?
	- Tempi di rilascio asincroni e periodici possono essere controllati
	- I tempi di computazione sono spesso non pratici da controllare
	- Problema della **determinazione** dell'implementazione con rispetto alla specifica
		- es. la specifica trascura le dipendenze eni tempi di esecuzione dei chunk, e gli intervalli temporali nominali di variazionie dei timer sono ampliati per rendere il modello robusto.

- **Test guidati** (opposti a test randomizzati)
	- Esplorano l'SCG per identificare le classi stato che possono essere selezionati come punti di partenza
	- Esplorano la PTPN analisi della traccia per derivare le restrizioni di tempo per la classi di partenza che possono portare all'esecuzioni di specifiche sequenze di transizioni di firings
	
---
**Slide 134**
**SD7-SW: Verdetto dell'oracolo e valutazione della copertura**

- Oracolo end-to-end
	- Verifico che le deadlines dei task end-to-end siano rispettate
	- Richiede la stampa dei log per i tempi dei rilasci dei job e il loro completamento

- Oracolo in sequenza 
	- Verifico che l'ordine qualitativo degli eventi è conforme alla specifica (ovvero esiste almeno un timing che rende la sequenza logged feasible)
	- Richiede il log di tutti gli eventi che corrispondono alle transizioni nel modello PTPN

- Oracolo temporizzato
	- Verifica che la sequenza logged sia una esecuzione feasibile per la specifica (ovvero verifica la ***relazione di inclusione timed trace***)
	- Richiede la stampo dei log di tutti gli eventi corrispondenti ad una transizione
	- Trova tutti i guasti trovati dall'oracolo in sequenza

---
**Slide 135**
**SD7-SW: I risultati sul caso di studio corrente**

- Testing del codice in ambienti simulati per il System Control del CSCI, codice integrato con entry-points *funzionali* dei suoi chunks
- Individuazione di una non sequenza di esecuzione
	- Causata da difetti di un task: due chunks sincronizzati su un semaforo non rappresentati esplicitamente nell'architettura dinamica
	- Risolta rappresentando il semaforo nella specifica dei task set e poi ripetendo la verifica formale
- Individuazione di violazioni nei time-frame
	- Causati da cycle stealing dovuto a un task VxWorks chiamato *tNetTask* che riporta servizi di processamento di pacchetti
	- Risolto assegnando all'SC task a priorità maggiore di *tNetTask*

---
**Slide 136**
**V-Model: seconda parte di SD7-SW, SD8, SD9**

- Seconda parte di SD7-SW: Integrazione Sw - scope di unità
	- Test d'integrazione per CSCIs, HCIc e FCIs per ogni unità
- SD8: Integrazione di sistema - scope di sistema
	- Test d'integrazione di ogni unità dentro al sistema
- SD9: Transizione all'utilizzo - scope di sistema
	- Metto il sistema completo in operazione al sito di applicazione inteso

- La seconda parte di SD7-SW e SD8 corrispondono alla System Integration e Testing del MIL-STD-498
- Tutte le attività sono fuori dallo scope della metodologia presentata

---
**Slide 137**
**Il testing è veramente necessario nel Model Drive Development? (MDD)**

- La verifica dell'architettura astrae dal numero di dettagli
	- Tempo di esecuzione delle operazioni (tempo di esecuzione che può essere trascurabile ma non zero), task addizionali, platform di deployment, cambi di contesto, ...
- La verifica architetturale può non essere esaustiva (esplosione dello spazio degli stati)
- Il testing in ogni caso è necessario per ragioni di certificazione (per buone ragioni)

![[Pasted image 20241109153811.png]]

---
## Automati Temporizzati

---

**Introduzione agli Automata Temporizzati (1/2)**

- Gli Automi Temporizzati supportano la rappresentazione di **sistemi concorrenti temporizzati**.
	- Espressività comparabile a quella delle Reti di Petri Temporizzate (TPNs).

- Un Automa Temporizzato (TA) è un automa finito arricchito con:
	  - un insieme di **orologi**,
	  - **vincoli temporali** sulle transizioni (chiamati anche guardie o condizioni abilitanti),
	  - **reset degli orologi** sulle transizioni.
	
- Un TA minimo: due posizioni $H$ e $K$, due orologi $x$ e $y$, una transizione da $H$ a $K$ (abilitata se $x > 0$, etichettata con l'azione $a$, con reset dell'orologio $y$ a $0$).
			- ![[Pasted image 20241118225640.png]]

---
**Introduzione agli Automata Temporizzati (2/2)**

- Il TA di un processo di riparazione.
	![[Pasted image 20241118225712.png]]

- Una possibile esecuzione del TA.
![[Pasted image 20241118225818.png]]

---
**Sintassi dei TA**

- Un TA è una tupla $\langle L, l_0 , \Sigma, X , E \rangle$ dove:
	  - $L$ è un insieme finito di **posizioni**
	  - $L_0 \subseteq L$ è l'insieme delle **posizioni iniziali**
	  - $\Sigma$ è un alfabeto finito di azioni
	  - $X$ è un insieme di orologi
	  - $E \subseteq L \times \Sigma \times G(X) \times 2^X \times L$ è un insieme di **archi** dove $G(X)$ è un insieme di **guardie** con sintassi $g := x \sim c | g \land g$ dove $x \in X$, $\sim \in \{<, \leq, =, >, \geq\}$, $c \in \mathbb{N}$ (cioè, una guardia è una congiunzione di vincoli atomici della forma $x \sim c$)

![[Pasted image 20241118230024.png]]

---
**Semantica dei TA (1/3)**

- Una **valutazione di orologio** $v \in \mathbb{R}_X^{\geq 0}$ assegna un valore a ciascun orologio.
	- Se una valutazione $v \in \mathbb{R}_X^{\geq 0}$ soddisfa una guardia $g \in G(X)$, allora si scrive $v \models g$.
	- $v + \tau$ denota la **valutazione** $(v + \tau)(x) = v(x) + \tau \quad \forall x \in X , \forall \tau \in \mathbb{R}^{\geq 0}$

- Lo stato di un TA è una coppia $(l, v)$ dove:
  - $l$ è una posizione
  - $v$ è una valutazione

- Esistono due tipi di transizione tra stati:
  - **Transizione di ritardo**: $(l, v) \xrightarrow{\tau} (l, v + \tau)$ per qualsiasi stato $(l, v)$ e qualsiasi ritardo $\tau \in \mathbb{R}^{\geq 0}$
  - **Transizione discreta**: $(l, v) \xrightarrow{a} (l', v')$ se $\exists (l, a, g, R, l') \in E$ tale che $v \models g$ e $v'(x) = 0$ se $x \in R$ e $v'(x) = v(x)$ se $x \notin R$

- Una **corsa** di un TA è una sequenza di transizioni alternate di ritardo e discrete:
  $(l_0, v_0) \xrightarrow{\tau_1} (l_0, v_0 + \tau_1) \xrightarrow{a_2} (l_1, v_1) \xrightarrow{\tau_2} (l_1, v_1 + \tau_2) \rightarrow{a_2} \dots \xrightarrow{a_k} (l_k, v_k)$
- O equivalentemente scritto come $(l_0, v_0) \xrightarrow{\tau_1, a_1} (l_1, v_1) \xrightarrow{\tau_2, a_2} \dots \xrightarrow{\tau_k, a_k} (l_k, v_k)$
  
---
**Semantica dei TA (2/3)**

- Una **sequenza temporale** è una sequenza finita non decrescente di valori reali non negativi, cioè $s = (t_1)(t_2) \dots (t_k)$ con $t_i \in \mathbb{R}_{\geq 0} \space \forall i \in \{1, \dots, k\}$

- Una **parola temporizzata** è una sequenza finita di coppie formate da un'azione e un valore temporale appartenente a una sequenza temporale, cioè $w = (a_1, t_1)(a_2, t_2) \dots (a_k, t_k)$ con $a_i \in \Sigma$ e con $(t_1)(t_2) \dots (t_k)$ che è una sequenza temporale

- Una parola temporizzata $w = (a_1, t_1)(a_2, t_2) \dots (a_k, t_k)$ è **accettata** da un TA se $\exists \rho = (l_0, v_0) \xrightarrow{\tau_1, a_1} (l_1, v_1) \dots \xrightarrow{\tau_k, a_k} (l_k, v_k)$ con $l_0 \in L_0$ e $t_i = \sum_{j=1}^i \tau_j$

- Il **linguaggio temporizzato accettato** di un TA è l'insieme delle parole temporizzate accettate

---
**Semantica dei TA (3/3)**

- Una corsa dell’esempio TA è $(l_0, (0, 0)) \xrightarrow{0.1, b} (l_0, (0.1, 0)) \xrightarrow{0.2, b} (l_0, (0.3, 0)) \xrightarrow{1, a} (l_0, (1.3, 1)) \xrightarrow{0.2, b} (l_0, (1.5, 0)) \xrightarrow{0, a} (l_1, (0, 0)) \xrightarrow{1, a} (l_2, (1, 1))$
- Una parola temporizzata accettata è $w = (b, 0.1)(b, 0.3)(a, 1.3)(b, 1.5)(b, 2.5)$

- Le guardie sempre vere e gli insieme vuoti di reset sono omessi nella rappresentazione

![[Pasted image 20241118231931.png]]

---
**Varianti delle TA nella letteratura (1/2)**

- Network di TA (NTA)
	- Prodotto (composizione parallela) di due o più TA con differenti insiemi di orologi 
	- Differenti semantiche a seconda del tipo della composizione
		- Composizione sincrona 
			![[Pasted image 20241118232926.png]]
		- Composizione asincrona
			![[Pasted image 20241118233000.png]]
		- Composizione con sincronizzazione esplicita
			![[Pasted image 20241118233045.png]]

---
**Varianti delle TA nella letteratura (2/2)**

- TA con vincoli diagonali
	- Le guardie hanno sintassi $g := x \sim c | x-y \sim | g \land g$ dove $x,y \in X$, $\sim \in \{<, \leq, =, >, \geq\}$, $c \in \mathbb{N}$ (cioè, una guardia è una congiunzione di vincoli atomici della forma $x \sim c$ e $x-y \sim c$).

- TA con epsilon transistions
	-  Le epsilon transitions sono silenziose o transizioni non osservabili

---
 **Partizionamento delle regioni (1/2)**
 
- $\forall g∈Gg \in Gg∈G$, sia ⟦g⟧ l'insieme delle valutazioni $\{v \in \mathbb{R}_{\geq 0}^X \mid v \models g \}$
- $\forall Y \subseteq X$, sia $[Y \leftarrow 0]$v la valutazione tale che:
	- $[Y←0]v(x)=0$ se $x∈Y$ e $[Y \leftarrow 0]v(x) = v(x)$ ​se $x∈X∖Y$.​

- Una **partizione finita** $R$ d $\mathbb{R}_{\geq 0}^X$​ è un **insieme di regioni** (per l'insieme delle guardie G) se:
    1. $\forall g∈G$ e R $\in R$: $⟦g⟧⊆R$ o $⟦g⟧∩R=\emptyset$
    2. $\forall$ R,R′ $\in R$  se $∃v∈R$ e $t \in \mathbb{R}_{\leq 0}$​ con $v+t \in$ R' => $\exists t' \in \mathbb{R}_{\geq 0}$ tale che $v' + t' \in$ R'  $\forall v' \in$ R
    3. $\forall$ R,R′ $\in R$, $\forall \space Y⊆X$, se R$_{[Y←0]} \cap$ R′≠∅ => R$_{[Y \leftarrow 0]} \subseteq$ R
	    - dove R$_{[Y←0]}$ è la regione ottenuta da R azzerando gli orologi in  $Y \in X$

- $R$ definisce una **relazione di equivalenza** sulle valutazioni.
	- Una **classe di equivalenza** è detta una regione.
    
- Se due valutazioni sono equivalenti, allora i loro comportamenti futuri sono equivalenti.
	1. Due valutazioni equivalenti soddisfano gli stessi vincoli sugli orologi.
	2. Il trascorrere del tempo non distingue tra due valutazioni equivalenti.
	3. Il reset degli orologi non distingue tra due valutazioni equivalenti.

---
 **Partizionamento delle regioni (2/2)**

- Due valutazioni $v$ e $v'$ con $v, v' \in \mathbb{R}_{\geq 0}^X$ sono equivalenti se $\forall x, y \in X$:
    - $v(x) > M \iff v'(x) > M$, dove $M$ è la costante massima per tutti gli orologi.
    - $v(x) \leq M \implies \lfloor v(x) \rfloor = \lfloor v'(x) \rfloor \land ({v(x)} = 0 \iff {v'(x)} = 0)$, dove ${v(x)}$ è la parte frazionaria di $v(x)$.
    - $v(x) \leq M \land v(y) \leq M \implies ({v(x)} \leq {v(y)} \iff {v'(x)} \leq {v'(y)})$.

- La partizione è compatibile con le condizioni 1,2 e 3 
- Partizionamento delle regioni senza diagonali per 2 orologi con costante massima 2![[Pasted image 20241119130346.png]]

- La forma di regioni **bounded** con due orologi e senza vincoli diagonali![[Pasted image 20241119130500.png]]

---
 **Grafo delle regioni**

- Un grafo delle regioni è un automa finito i cui stati sono le regioni e le cui transizioni sono definite come:
	- $R \xrightarrow{\tau} R'$ se $\exists v \in R, v' \in R', \tau \in \mathbb{R}_{\geq 0}$ tale che $v' = v + \tau$. In questo caso, $R'$ è il successore temporale di $R$.
	- $R \xrightarrow{Y} R'$ se $R_{[Y \leftarrow 0]} \subseteq R'$

- Rappresenta la possibile evoluzione dei tempi del sistema
- Partizionamento delle regioni senza diagonali per 2 orologi con costante massima 2![[Pasted image 20241119131256.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131434.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131524.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131556.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131739.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131653.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131809.png]]

---
**Grafo delle regioni**

![[Pasted image 20241119131848.png]]

---
**Regione di automazione**

- La regione di automazione è una automa finito nel quale gli stati sono $L$ x $R$ e dove le transizioni sono:
	- $(I,R) \xrightarrow{a} (I',R')$ se $\exists I \xrightarrow{g,a,Y} I'$ è una transizione nell'TA con R $\subseteq ⟦g⟧$ e R $\xrightarrow{Y}$R' è la transizione nel grafo delle regioni
	- $(I,R) \xrightarrow{\tau} (I',R')$ se R $\xrightarrow{\tau}$ R' è una transizione nel grafo delle regioni
- Ad esempio
	 ![[Pasted image 20241119153835.png]]

---
**Grafo delle zone**

- Il numero di regioni è **esponenziale** rispetto al numero di orologi e al valore massimo dei vincoli.
- Il **grafo delle zone** fornisce una codifica più efficiente:
    - Le zone sono rappresentazioni mediante matrici di vincoli di differenza (DBM), che rappresentano l'unione delle regioni.
- Ad esempio una TA è il suo grafo di zone![[Pasted image 20241119154038.png]]

---
**Uppaal: un tool per la modellazione è l'analisi delle NTA**

- **Uppaal** è uno strumento per la modellazione e l'analisi di reti di automi temporizzati (NTA). È sviluppato congiuntamente dall'Università di Uppsala e dall'Università di Aalborg.

- **Caratteristiche principali:**
  - **Modellazione**: editing grafico di NTA.
  - **Simulazione**: esecuzione manuale o casuale delle esecuzioni.
  - **Analisi**: verifica delle proprietà di raggiungibilità, sicurezza e vivibilità.
			![[Pasted image 20241119154348.png]]

---
**Uppal: verifica temporale delle formule logiche(1/2)**

- I primi connettivi temporali possono essere: 
	- A: tutti i percorsi dallo stato corrente
	- E: almeno un percorso dallo stato corrente
- I secondi connettivi temporali possono essere: 
	- X: prossimo stato
	- G: tutti gli stati futuri (denotati come [] in Uppaal)
	- F: alcuni stati futuri (denotati come <> in Uppaal)
	- U: finché 
  - Esempi (Assumendo il sistema sia in uno stato s):
    - $\phi$ è vero se e solo se è soddisfatto da s
    - AX$\phi$ è vero se e solo se $\phi$ è vero per ogni immediato stato successore di s
    - AG$\phi$ è vero se e solo se $\phi$ è vero per ogni stato successore di s
    - AF$\phi$ è vero se e solo se su tutti i percorsi che originano da s c'è uno stato dove $\phi$ finisce
    - A$\phi$U$\theta$ è vero se e solo se su tutti i percorsi da s soddisfa $\phi$ fino a che raggiungono uno stato dove $\theta$ finisce
    - EX$\phi$ è vero se e solo se $\phi$ è vero per almeno un immediato stato successore di s
    - ...

---
**Uppal: verifica temporale delle formule logiche(2/2)**

- Esempi (Assumendo il sistema sia in uno stato s):
    - A[]$\phi$ è vero se e solo se $\phi$ è vero in tutti gli stati di tutti percorsi da s
    - E<>$\phi$ è vero se e solo se $\phi$ è vero in alcuni stati di almeno un percorso da s
    - A<>$\phi$ è vero se e solo se $\phi$ è vero in alcuni stati di tutti i percorsi da s
    - E[]$\phi$ è vero se e solo se $\phi$  è vero in tutti gli stati di almeno un percorso da s
			![[Pasted image 20241119160500.png]]

---

# Introduzione al System Modeling Language

**Indice**

1. System Modeling Language
2. Un esempio nell'area dei sistemi cyber-physical

---
## System Modeling Language

**Cos'è l'ingegneria dei sistemi?**

- L'ingegneria dei sistemi è una disciplina che si concentra sulla progettazione e sull'applicazione dell'**intero sistema**, distinto dalle sue parti. Si occupa del problema nella sua totalità, considerando tutte le variabili e le sfaccettature (Federal Aviation Agency FAA-USA, Systems Engineering Manual, Definition by Simon Ramo, 2006 )

- L'ingegneria dei sistemi è un processo iterativo di sintesi, sviluppo e operatività di un **sistema reale** che soddisfa, in modo quasi ottimale, tutti i requisiti richiesti per il sistemaa (Howard Eisner, Essentials of Project and Systems Engineering Management, Wiley, 2002)

---
 **Modellazione dei Sistemi**
 
![[Pasted image 20241119162804.png]]

---
 **Vantaggi della Modellazione Basata sui Sistemi**

- Comprensione condivisa dei requisiti e del design del sistema
	- Validazione dei requisiti
	- Base comune per analisi e progettazione
	- Facilitazione nell'identificazione dei rischi

- Aiuto nella gestione di sistemi complessi
	- Separazione dei lavori secondo diverse visioni del modello integrato
	- Supporta la tracciabilità tramite modelli di sistemi gerarchici
	- Facilita l'impatto dell'analisi dei requisiti e cambiamenti del design
	- Supporto per lo sviluppo incrementale e acquisizione evoluzionaria

- Migliorata qualità del design
	- Riduzione degli errori e delle ambiguità
	-  Rappresentazione più completa 
	
- Supporta la verifica e validazione anticipata e continua per ridurre il rischio
- Fornisce valore attraverso il ciclo di vita (ad esempio formazione)
- Migliora acquisizione della conoscenza

---
**Linguaggio di Modellazione dei Sistemi (SysML)**

- Linguaggio grafico adottato dall'OMG nel 2006.

- Supporta specifica, analisi, progettazione, verifica e validazione di sistemi che includono hardware, software, dati, personale, procedure e strutture.

- è un liguaggio visuale di modellazione che fornisce:
    - **Semantica**: regole per creare modelli.
    - **Notazione**: rappresentazioni grafiche o testuali.
- Non è una metodologia o un tool (SysML è indipendente dalla metodologia e i tool)
- Estende un sottoinsieme di UML2
	- L'UML è un modello di linguaggio general-purpose, per lo sviluppo di applicazioni software (**Ingegneria del software**)

---
**SysML vs UML**

![[Pasted image 20241119164136.png]]

---
**I Quattro Pilastri di SysML**

- Un esempio di modellazione di un sistema ABS 

![[Pasted image 20241119164337.png]]

---
**Diagrammi strutturali**

![[Pasted image 20241119180405.png]]

---
**Package diagrams**

- Gli stessi di UML2
- Usati per organizzare il modello
	- Raggruppano i modelli in spazi di nomi
	- Spesso rappresentati in tool browser
	- Supportano la gestione della configurazione dei modelli (check-in/out)

- Il modello può essere organizzato in diversi modi
    - Gerarchia del sistema (es. enterprise, sistema, componente)
    - Tipi di diagrammi (requisiti, casi d'uso, comportamento)
    - Usare punti di vista per aumentare l'organizzazione del modello

---
**Blocchi**

- Elemento strutturale di base
- Definisce un insieme di features strutturali e funzionali per descrivere un sistema o elemento (software, hardware, dati, procedure, ...)
- Utilizzato sia nella progettazione fisica che logica
- Le sue caratteristiche possono essere descritte per diversi compartimenti standard
	- Proprietà (parti, riferimenti, valori, porte)
	- Operazione
	- Vincoli
	- Allocazioni da/per un altro elemento del modello (es. attività)
	- Requisiti che il blocco soddisfa
	- Compartimenti definiti dall'utente
- Può essere usato per specificate gerarchie e interconnessioni

---
**Diagrammi di Definizione dei Blocchi (BDD) e Diagrammi Interni dei Blocchi (IBD) (1/2)**

- Block Definition Diagram **BDD**: Mostra relazioni tra blocchi (composizione, associazione, specializzazione).
	- Stesso della definizione dei tipi (corrisponde al class diagram dell'UML)
	- Riusato in più contesti
	- Non può definire completamente le dipendenze di comunicazione è la struttura di composizione (no topologia)
	
- Un Internal Block Diagram **IBD**: Mostra la struttura interna di un blocco in termini di proprietà e connettori
	- Una parte è l'uso del blocco nel contesto di una composizione di blocchi (conosciuto come ruolo)
	- La struttura interna e la comunicazione & la topologia del segnalamento diventano esplicite

- Le porte specificano i punti d'interazione sui blocchi e le parti
	- Integrano comportamento con la struttura
	- Le porte standard specificano le operazioni richieste o apportate e o i segnali (componenti software usati)
	- Le porte dei flussi specificano cosa può transitare dentro/fuori di un blocco/porta (usati per i segnali e i flussi fisici)

---
**Diagrammi di Definizione dei Blocchi (BDD) e Diagrammi Interni dei Blocchi (IBD) (2/2)**

![[Pasted image 20241119173356.png]]

---
**Diagrammi Parametrici (Parametrci diagram) (1/2)**

- Utilizzati per esprimere vincoli (equazioni) tra proprietà di valore
	- Forniscono supporto per analisi ingegneristiche, (es. prestazioni, affidabilità)
	- Facilitano l'identificazione delle proprietà critiche delle prestazioni

- Rappresentano l'uso dei vincoli nel contesto di un'analisi.
	- I vincoli sono definiti tramite blocchi di vincolo che catturano equazioni.
	- Il linguaggio di espressione può essere formale o informale.
	- Il motore computazionale è fornito da strumenti di analisi specifici, non da SysML.
	- I parametri di vincolo sono associati alle proprietà di valore dei blocchi.

---
**Diagrammi Parametrici (2/2)**

![[Pasted image 20241119173758.png]]

---
**Diagrammi comportamentali**

![[Pasted image 20241119180506.png]]

---
**Diagrammi di Attività (Activity Diagrams)**

- Specificano la trasformazione degli input in output attraverso una sequenza controllata di azioni

- Simili ai flussi di dati, ma con estensioni per rappresentare una semantica più generale, inclusi modelli di flussi fisici continui

- Mostrano le responsabilità tramite partizioni di attività (swimlanes).
	- SysML supporta la modellazione del flusso continuo (sistemi a tempo continuo).
	- Allineati con tecniche classiche dell'ingegneria dei sistemi, come i diagrammi EFFBD (Enhanced Functional Flow Block Diagrams)

---
**Diagrammi di Sequenza (Sequence Diagram)**

- Rappresentano il comportamento basato su messaggi
	- Mostrano il flusso di controllo
	- Descrivono le interazioni tra parti

- Forniscono strumenti per rappresentare scenari complessi, come:
	  - Sequenze di riferimento
	  - Logica di controllo
	  - Decomposizione delle linee di vita

- Conosciuti anche come Diagrammi di Interazione o Interazioni

---
**Diagrammi a Stati (State Machine Diagram)**

- Utilizzati per rappresentare il ciclo di vita di un blocco

- Supportano la rappresentazione del comportamento basato su eventi (generalmente asincrono).
	- Transizione con trigger, guardia e azione.
	- Gli stati con entrata, uscita e attività di esecuzione
	- Supportano stati sequenziali annidati o stati concorrenti
	- Possono inviare/ricevere segnali tra blocchi durante le transizioni di stato
	- Cambiano eventi, eventi del tempo, eventi dei segnali

---
**Diagrammi dei Casi d'Uso (Use Case Diagrams)**

- Portano gli strumenti per descrivere le funzionalità di base del sistema in termini di utilizzi/obiettivi da parte degli attori
	- Il loro uso dipende dalla metodologia
	- Spesso accompagnati da descrizioni dei casi d'uso

- Le funzionalità comuni possono essere estese tramite relazioni "include" e "extend"

- Elaborati con altre rappresentazioni comportamentali per descrivere scenari dettagliati

- Non subiscono modifiche rispetto all'UML

---
**Costrutti cross-cutting**

![[Pasted image 20241119180603.png]]

---
**Allocazioni**

- Rappresentano relazioni generali che mappano un elemento del modello su un altro

- Tipi di allocazione:
	  - Comportamentale (funzione a componente)
	  - Strutturale (logico a fisico)
	  - Software a hardware

- Esplicitano allocazioni di attività delle strutture tramite swimlanes (cioè partizioni delle attività)
- Supportano rappresentazioni grafiche e tabellari

---
**Requisiti**

- Lo stereotipo "requirement" rappresenta un requisito basato su testo.
	- Include proprietà dell'ID e del testo
	- Può aggiungere proprietà definite dall'utente come metodi di verifica
	- Può aggiungere categorie di requisiti definiti dall'utente (es. funzionali, di interfaccia, di performance)
- La gerarchia dei requisiti descrive i requisiti contenuti in una specifica

- Le relazioni tra requisiti includono:
	  - DeriveReqt, Satisfy, Verify, Refine, Trace, Copy

---
**Diagramma dei requisiti**

![[Pasted image 20241119181451.png]]

---
**Papyrus**

- Uno strumento open source basato su Eclipse che fornisce un ambiente integrato per l'editing di modelli UML e SysML.
	- Sviluppato dal laboratorio di ingegneria dei sistemi della Commissione francese per l'energia atomica e le energie alternative.
- **Pagina ufficiale**: [https://www.eclipse.org/papyrus](https://www.eclipse.org/papyrus).
- Può essere utilizzato come strumento autonomo o come plugin per Eclipse.
![[Pasted image 20241119181757.png]]

---
**Papyrus: Come installare lo strumento**

1. Selezionare **Help → Install New Software**.
2. Nella sezione **Work with**, aggiungere il seguente link:
    - [http://download.eclipse.org/modeling/mdt/papyrus/updates/releases/2019-09](http://download.eclipse.org/modeling/mdt/papyrus/updates/releases/2019-09).
3. Selezionare **Add → Papyrus for UML** e avviare l'installazione.
4. Ripetere il processo per **SysML** aggiungendo il link:
    - [http://download.eclipse.org/modeling/mdt/papyrus/components/sysml14](http://download.eclipse.org/modeling/mdt/papyrus/components/sysml14).

---
## Un esempio nell'area dei sistemi cyber-physical

**Reti di distribuzione del gas**:

- Combinano l'analisi fisico-dinamica dei fluidi con procedure di gestione cibernetica.
- Obiettivo: valutare il rischio di **bassa pressione** nella fase transitoria dopo una riparazione.
- Analisi:
    - Analisi dinamica del comportamento del gas.
    - Analisi stocastica delle azioni di riparazione.
![[Pasted image 20241119182036.png]]
---
**Soluzione che combina analisi fluidodinamiche e stocastiche**

- Analisi fluido-dinamica del comportamento del gas
	- Deriva il rischio di bassa pressione (LPR) sperimentato in ogni stato fluido-dinamico

- L'analisi transitoria della procedura di riparazione
	- Deriva la probabilità transitoria  di ogni stato dinamico
	- Calcolo del rischio transitorio istantaneo:    
	    $∑_{γ∈Γ} If(e(m,γ),LPR_γ,0)$, dove:
	    - $\Gamma$ è insieme degli stati fluidodinamici.
	    - $LPR_γ$ è la misura del rischio in $\gamma \in \Gamma$
	    - $e(m,γ)$ è *vero* se la marcatura $m$ rappresenta lo stato γ, *falso* altrimenti

- La soluzione fornisce il **rischio di bassa pressione** atteso nel tempo.
    
	![[Pasted image 20241119182726.png]]
	![[Pasted image 20241119182914.png]]
---
**SysML: Diagrammi dei Casi d'Uso e Requisiti**

- Use Case Diagram dello scenario del tubo
![[Pasted image 20241119183108.png]]

- Tabella dei requisiti
![[Pasted image 20241119183140.png]]

---
**SysML: Diagrammi di Definizione dei Blocchi delle risolse coinvolte**

![[Pasted image 20241119183238.png]]

---
**SysML: Diagrammi a Stati della rete e del personale**

![[Pasted image 20241119183334.png]]

![[Pasted image 20241119183411.png]]

---
**SysML: Diagrammi di Attività della procedura di riparazione**

![[Pasted image 20241119183832.png]]
![[Pasted image 20241119183628.png]]
![[Pasted image 20241119183752.png]]

---
# Testing del Software

**Indice**

1. Concetti Base
2. Test del flusso di controllo
3. Test del flusso dei dati
4. Test degli stati finiti

---
## Concetti di base

**Natura e obiettivi del test del software**

- Il testing è un metodo di verifica
	- Punta a identificare i difetti in un’Implementation Under Test (IUT) attraverso esperimenti disciplinati e osservazioni dei malfunzionamenti
	- È un approccio dinamico (contrapposto all'ispezione statica)

- Ha limiti inerenti e capacità
	- Può dimostrare la presenza di difetti, ma non la loro assenza (E. Dijkstra, 1970).
	- È utile per fini formativi
	- è prescritto nella certificazione di sistemi critici per la sicurezza (es. RTCA-D0/178B per sistemi avionici).
	- Ma è anche un buon driver nella produzione del software (design per testability)

---
**Ontologia di difetti, malfunzionamenti ed errori**

- Tre concetti principali:
	  - **Malfunzionamento**: deviazione dai requisiti funzionali.
	  - **Difetto**: un elemento nell'implementazione che causa un malfunzionamento.
	  - **Errore**: passaggio nel processo che porta a un difetto.

- Un esempio (Ariane V, 1996):
	- Malfunzionamento: valore errato restituito dall’unità SW.
	- Difetto: tipo di dati non sufficiente per gestire l'intervallo richiesto.
	- Errore: specifica di requisiti errata non identificava correttamente l'intervallo dei valori di input.

---
**Ontologia di difetti e malfunzionamenti (1/3)**

- I tre concetti appartengono a differenti prospettive
  - Un **errore** si verifica durante un'**attività** del processo di sviluppo
  - Questo porta a un **difetto** nella struttura di un **componente**
  - Il difetto può causare un **malfunzionamento** (failure) rispetto a un **requisito funzionale**

![[Pasted image 20241119192951.png]]

---
**Ontologia di difetti e malfunzionamenti (2/3)**

- Filosocamente difficile definire un fallimento/malfunzionamento
	- Definizione concettuale di una sistemazione è più facile di quella di un fallimento

- Natura specifica del SW testing (?)
	- Molto meno legata all'invecchiamento e alla produzione fisica
	- La maggior parte dei fallimenti sono presenti per il design e il codice

---
**Ontologia di difetti e malfunzionamenti (3/3)**

- Una diversa ontologia è applicata nella Dependability Engineering
	- Un **Difetto** (o guasto) porta il sottosistema in uno stato di **Errore**...
	- ... che può portare al **Fallimento** del sottosistema
	- ... che può diventare un **Difetto** per un livello più alto del **Sistema**

- Ad esempio nell'Ariane V
	- Difetto: misura dell'unità di processamento ritorna valore sbagliato
	- Errore: stato inconsistente nell'unità di controllo dell'accellerazione angolare
	- Fallimento: shutdown del primo processore propagato ai livelli superiori come un Difetto...

- Principali differenze fra le due prospettive
	- Enfasi sullo stato comportamentale e sulla gerarchia sistema/sottosistema
	- Gli errori possono essere recuperati, apre la strada alla tolleranza dei difetti (Fault tollerance)

---
**Attività nella metodologia di test**
 
- Selezione dei casi di test
	- Definisce suite di test per rivelare potenziali difetti

- Generazione di input
	- Individua input che consentono l'esecuzione del caso di test

- Esecuzione dei casi di test
	- Utilizza driver, stub, script e strumenti come JUnit o Mockito per l'esecuzione della test suite
	
- Verdetto dell’oracolo
	- Determina se l'IUT ha passato un test, ovvero se i risultati del test soddisfano i requisiti funzionali.

- Debugging
	- Identifica le cause dei malfunzionamenti osservati

- Analisi di copertura
	- Valuta quanto i risultati del test coprano lo spazio comportamentale dell’IUT

---
**Osservazioni sulla selezione dei casi di test**

- Identifica una suite di test abile a rivelare tutti i possibili Difetti
- È lo step più caratterrizante della metodologia dei test
- Si basa su alcune astrazioni dello IUT ... e su alcuni criteri di copertura (coverage)

![[Pasted image 20241119201620.png]]

---
**Modello di difetto (Fault model)**

- **Abstraction** e **criteri di copertura** dipendono dal **modello di difetto**
	- Ovvero l’insieme dei **tipi di difetto** nell'IUT che vengono affrontati.
	- Il modello dipende dalle caratteristiche strutturali e funzionali dell’IUT.

		![[Pasted image 20241119201947.png]]
---
**Prospettiva funzionale vs prospettiva strutturale (1/2)**

- L'astrazione può prendere differenti prospettive

- **Funzionale** (black box) si riferisce alla specifica dell'IUT
	- Ad esempio gli use case diagrams, l'SRS prescitto nello standard MIL-STD-498, conceptual class diagram, ...

- **Strutturale** (white box) si riferisce all'implementazione dell'IUT
	- Ad esempio class diagrams, System Design Description (SDD) prescitto nello standard MIL-STD-498, codice sorgente o codice binario (?)

- **Architetturale** (grey box)  si riferisce all'archittetura dell'IUT
	- Ad esempio architectural design, System Subsytem Design Description (SSDD) e lo Interface Requirements Specification (IRS) dello standard MIL-STD-498, ...

- Il Model Driven Development (MDD) può offuscare il concetto, ad esempio il codice generato automaticamente dai requisiti del modello

---
**Prospettiva funzionale vs prospettiva strutturale (2/2)**

- Sul significato di "funzionale" nel l'ingegneria del software
	-  Requisiti funzionali, strutturali e di qualità . . .
	-  con caratteristiche di qualità definite dalla norma ISO/IEC 9126, ora sostituita dalla norma ISO/IEC 25010:2011 ...
	- e classificati come interni, esterni o in uso

- In Software Testing:
	-  La prospettiva funzionale si riferisce a qualsiasi requisito
	- La prospettiva strutturale si riferisce a qualsiasi aspetto dell'implementazione

![[Pasted image 20241119202923.png]]

---
**Osservazioni sulla generazione dei input**

- Identifica gli input che lasciano il sistema funzionare lungo un caso di prova
- É un caso di problema undecidibile
- Può non essere feasible
	- Per via dei percorsi unfeasible (comportamenti falsi) aggiunti nell'astrazione
- É collegata con la selezione dei test case
	- Un criterio di coverage può implementato da differenti Test suites, con differenti condizioni di path feasibility

![[Pasted image 20241120154425.png]]

---
**Osservazioni sul verdetto dell'oracolo**

- Decide se l'IUT passa un test
	- Cioè se il result dei test rispettano i requisiti funzionali

- Il verdetto dell'oracolo può essere inconclusivo
	- Per via del fatto che la risposta dello IUT può non essere controllata a piena

- È la parte più difficile da automatizzare
	- Ha bisogno di una rappresentazione eseguibile dei requisiti
		- es. usare un modulo Matlab come specifica per un programma c
	- É spesso eseguito manualmente in maniera tautologica:
		- giudica i risultati dei test in assenza di una specifica

---
**Osservazioni sul debugging**

- Riconduce i difetti funzionali osservati ai difetti strutturali

- Un difetto può essere associato con diversi difetti
	- Un malfunzionamento può risultare dall'interazione di diversi dettagli dell'IUT...
	- ... e può essere rimosso tramite l'applicazione congiunta di diversi aggiustamenti 
	- ... che successivamente aumentano il problema della regressione del testing(?) 

---
**Osservazioni sull'analisi del coverage**

- Valuta quanto i result dei test coprono lo spazio dei comportamenti dell'IUT

- La realizzazione è simile a quella della selezione dei casi di test
	- Misura con cui il risultato dei test copre l'astrazione dello IUT
	- Se lo IUT passa una test suite => Ho un giustificabile grado di confidenza sull'assenza di difetti residuali nell'IUT
	- Si basa sul grado di copertura di qualche Abstraction
	- Sottointende assunzioni sulla dimensione dell'Abstraction
	- Si basa su qualche strumentazione del codice (es. orientato all'aspetto (?))

- La selezione dei casi di test & l'analisi del coverage può mescolare le prospettive
	- Un esempio: seleziono dei test case dagli use case, e poi valuto la coverage su un astrazione basata sul codice (es. RTCA-DO/178B, RTCA-DO/178C)

---
## Test del flusso di controllo

**Introduzione**

- Fornisce un'astrazione, ovvero **grafo del flusso di controllo (CFG)**

- Fornisce una suite di criteri di copertura: **tutti i nodi**(all-nodes), **tutti i bordi**(all-edges), **tutti i percorsi**(all-paths), **Modified Condition Decision Coverage** (MCDC), ecc

- Applicabile sia alla selezione dei casi di test che all'analisi della copertura

- Applicabile sia nel prospettiva strutturale e nella prospettiva funzionale

---
**Grafo del Flusso di Controllo (CFG) (1/2)**

- I vertici possono essere **Linee di codice (Lines of Codes (LOCs))** oppure **blocchi base** 
	- I blocchi base sono insiemi massimali di istruzioni $\langle S_1, ... , S_N \rangle$ tale che:
		- $S_N$ è l'unico successore d'esecuzione di $S_{N-1}$
		- $S_{N-1}$ è l'unico predecessore d'esecuzione di $S_N$
	- Ovvero il massimo set di istruzioni che son eseguite sempre insieme
	- Ovvero senza etichette target, senza rami, break, istruzioni di return, ... massimale

- Gli archi rappresentano la successione d'esecuzione
	![[Pasted image 20241120175713.png]]

---
**Grafo del Flusso di Controllo (CFG) (2/2)**

- L'astrazione CFG toglie le dipendenze dei dati 

- Sottointende il fault model
	- Rappresenta i difetti che influenzano le guardie di controllo o le variabili di controllo usate nelle guardie, che  consente al'IUT di deviare dal flusso di controllo previsto

- Applicabile in differenti granelli di astrazione
	- LOCs, blocchi base, chiamate di funzione, invocazioni di servizi, ...

--- 
**Criteri di copertura: tutti i nodi**

- Tutti i nodi (a.k.a block coverage, statement coverage)
	- Ogni vertice del CFG deve essere visitato almeno una volta
	- Il minimum coverage necessario per assicurare che ogni linea di codice sia stata eseguita almeno una volta durante il testing
	- Sufficiente per certificare una grande classe di sistemi safety-critical

- Complessità O(N) dove N è il numero di nodi
	- In termini di numero di casi di test
	- ... sviluppare un programma in cui (?) ... 
	- ![[Pasted image 20241120182127.png]]
	
---
**Criteri di copertura: limiti di tutti i nodi**

- Non garantisce la copertura di tutti i bordi ![[Pasted image 20241120182320.png]]

- Non distingue come un ciclo è stato lasciato (guardia, break, return. goto)

- Non dipende dal numero di iterazioni in un ciclo, e ignora completamente la struttura dei dei do-while

- Nell'analisi del coverage, può non essere proporzianale alla complessità (numero di linee di codice non bilanciato su differenti rami)

---
**Criteri di copertura: tutti i bordi**

- Tutti bordi (a.k.a tutte le decisioni)
	- Ogni bordo del CFG deve essere percorso almeno una volta

- Tutti i bordi sottopongono i tutti i nodi
	- Possono differire con la presenza congiunta di rami e confluenze(?)

- La complessità è sempre $O(cN)$ dove c è il massimo grado in output delle istruzioni
	- $O(N)$ raggiunge ogni nodo, e da ogni nodo, c casi coprono tutti gli output

- Limiti di tutti i bordi
	- Non garantisce che le guardie siano testate sotto tutte le combinazioni che possono portare alla stessa decisione
	- Potrebbe essere rilevante se le guardie producono side effects
					 ![[Pasted image 20241120185842.png]]
		
---
**Criteri di copertura: condizioni multiple (1/2)**

- Estende la copertura di tutti i bordi includendo ogni decisione sotto tutte le condizioni delle guardie
	- Una condizione è una massima espressione senza connettivi Booleani

- Diventa rilevante quando una condizione di guardia può produrre side effects
 ![[Pasted image 20241120190514.png]]
- ... in congiunzione con shorts-circuits su un espressione

---
**Criteri di copertura: condizioni multiple (2/2)**

- Ma la complessità è $O(cN2^k)$ dove $k$ è il numero di condizioni in una guardia

- Per linguaggi con espressioni short-circuited, molti casi sono equivalenti 
	 ![[Pasted image 20241120191924.png]]

- Questo vale per c, c++, Java, ma non per Ada

---
**Copertura dei criteri: Modified Condition Decision Coverage (MCDC) (1/2)**

- Modified Condition Decision Coverage(MCDC)
	- Estende "tutti i bordi" richiedendo che ogni decisione sia coperta in modo che, in alcuni test, ogni **condizione** determini ogni decisione differente in entrambi i modi

![[Pasted image 20241120193623.png]]

---
**Copertura dei criteri: Modified Condition Decision Coverage (MCDC) (2/2)**

- Nei linguaggi con espressioni short-circuited, MCDC è equivalente a condizioni multiple

- La complessità è $O(ckN)$
	- $c$ è il numero di casi per ciascuna condizione
	- L'analisi per l'identificazione dei casi di test è $O(2^k)$
	
- Prescritta dal documento RTCA/DO-178B
	- Sviluppato da Boeing e adottato da RTCA (Radio Technical Commission for Aeronautics, US) e dall'European Organisation for Civil Aviation Equipment

---
**Copertura dei criteri: tutti i percorsi**

- Tutti i percorsi (a.k.a tutti i predicati)
	- ogni percorso differente è coperto da almeno un test
	- Complessità: $O(2^N)$ se non esistono cicli, non definita con cicli
	- È un concetto, non una pratica
	- Può diventare accessibile su astrazioni molto grosse

- Potrebbe non rivelare problemi a causa della correttezza incidentale

---
**Copertura dei criteri: Boundary Interior e Structured Path**

- **Boundary Interior** seleziona un sottoinsieme finito di tutti i percorsi coprendo classi di equivalenza nell'insieme dei percorsi
	- I test di confine sono percorsi che attraversano il ciclo solo una volta, con test differenti per ciascun percorso
	- I test interni sono percorsi che attraversano il ciclo più volte, con test differenti per ciascun percorso nella prima iterazione

- Il test dei percorsi strutturati estende il concetto da 1 a $k$ iterazioni

---
**Coverage criteria: Esempio di Boundary Interior**

![[Pasted image 20241120195725.png]]

---
## Test del flusso dei dati

**Test del flusso di dati**

- Analizza come i difetti possono propagarsi in malfunzionamenti osservabili
	- Un effetto collaterale difettoso su una variabile non è osservato fino a quando la variabile non è utilizzata
	- Il difetto può attivare un malfunzionamento o propagarsi ad altre variabili
 ![[Pasted image 20241120201957.png]]

- Applica percorsi che vanno da dove una variabile è influenzata a dove è utilizzata
	- Ovvero copre l'accoppiamento dei dati fra le istruzioni

- Applicabile sia alla selezione dei casi di test che all'analisi della copertura

- Prima nella prospettiva strutturale poi in quella funzionale

---
**Data Flow Graph (DFG)**

- Estende il grafo del flusso di controllo (CFG) con annotazioni **def-x** e **use-x** per ogni variabile **rilevante** x (non per tutte le variabili)

- Copre il DFG con una suite di criteri: **all-defs**, **all-uses**, **all-DU-paths**

- Utilizzabile sia per la selezione dei casi di test che per l'analisi della copertura

- Inizia con una prospettiva strutturale e può successivamente passare a una prospettiva funzionale

---
**Data Flow Graph (DFG): Annotazioni e concetti**

- **def-x**: punto in cui la variabile x è influenzata (side-effected)

- **use-x**: punto in cui il valore di x è utilizzato
	- **c-use-x**: utilizzo in espressioni fuori da guardie (computazionale)
	- **p-use-x**: utilizzo in guardie (predicativo)

- La distinzione tra **p-use** e **c-use** 
	- Non è basata sulla sintassi, ma sulle conseguenze:
	  - Un **p-use** può divergere nel flusso
	  - Un **c-use** può propagare

- Un **def-clear-path-x** è percorso aciclico che inizia con un **def-x**, termina con un **use-x** e non attraversa nessun altro **def-x**
			![[Pasted image 20241120222812.png]]
			
---
**Coverage Criteria: All-Def**

- **Copertura di tutte le definizioni**: per ogni definizione (**def**), almeno un percorso fino a un utilizzo (**use**)
			 ![[Pasted image 20241120223038.png]]

- **Slicing del programma**: ripetere questo per ogni variabile **rilevante**  x 

---
**Coverage Criteria: All-Uses**

- **Copertura di tutti gli utilizzi**: per ogni **def**, almeno un percorso per ciascun **use** raggiungibile tramite un **def-clear-path**

	![[Pasted image 20241120223405.png]]
	
---
**Coverage Criteria: All-DU-Paths**

- **Copertura di tutti i percorsi Def-Use**: tutti i **def-clear-paths** da ciascuna definizione a ciascun utilizzo raggiunto da quella definizione e ogni nodo successivo al **use**

	![[Pasted image 20241120223844.png]]

- Nota: i percorsi DU sono per definizione aciclici

---
**Coverage Criteria: Criteri di flusso di controllo vs flusso di dati (1/4)**

- **All-Def** non è confrontabile con **all-nodes** o **all-edges**
  - **All-def** non include tutti i nodi
  - ma non è incluso da **all-edges**

![[Pasted image 20241120224115.png]]

---
**Coverage Criteria: Criteri di flusso di controllo vs flusso di dati (2/4)**

- **All-Uses** include **all-edges**
  - Da qualsiasi **c-use**, si torna indietro per trovare un **def**; ci sarà almeno un percorso per la coppia **def-use** (non necessariamente il percorso trovato muovendosi all'indietro)
  - Se nessun def è trovato, si può dare un compiler warning
  - Per un qualsiasi **p-use**, si torna indietro a partire dal nodo di decisione

![[Pasted image 20241120224543.png]]

---
**Coverage Criteria: Criteri di flusso di controllo vs flusso di dati (3/4)**

![[Pasted image 20241120224650.png]]

---
**Coverage Criteria: Criteri di flusso di controllo vs flusso di dati (4/4)**

- All-p-uses restringe all-uses per coprire le coppie def e p-use

- All-p-uses-some-c-uses estende all-p-uses per coprire all-def
	- Riduce l'over-coverage di defs mantenendo la comparabilità

![[Pasted image 20241120224957.png]]
![[Pasted image 20241120225021.png]]

---
**Coverage Criteria: Complessità**

- La complessità di **All-Uses** è $O(hN^2)$, dove $h$ è il grado massimo di uscita di una istruzione
- Sufficiente: 
	- Non ci sono più di $O(N^2)$ coppie **def-use** in un grafo

![[Pasted image 20241120225139.png]]

- Necessario: 
	- Ci sono $O(N^2)$ coppie **def-use** in un grafo
	- Sebbene non ci siano programmi con tale grafo CFG
	- Ma, è possibile definire un programma in cui tutti gli utilizzi richiedano $O(N^2)$

![[Pasted image 20241120225417.png]]

---
**Test strutturale vs test funzionale**

- Il test strutturale appare più fondato
	- poiché l'implementazione è più formalmente specificata rispetto ai requisiti
	
- Ma la selezione dei casi di test strutturali è tautologica
    - Esempio: 
	    - $x = 100 \ldots \text{if}(x > 10) \to x = 1 \ldots \text{if}(x > 10) \to \text{fault covered}$
	    - $x = 100 \ldots \text{if}(x > 10) \to y = 100 \ldots \text{if}(x > 10) \to \text{fault not covered}$
	  - Non può rilevare funzioni mancanti

  - L'implementazione è più complessa dei requisiti
	- Meno accessibile a chi non è coinvolto nello sviluppo

- **Combinazione virtuosa**:
  - Selezione dei casi di test funzionali
  - Analisi della copertura strutturale

---
**Test del flusso di controllo e dei dati in prospettiva funzionale**

- Il test del flusso di controllo e dei dati può essere applicato anche in una prospettiva funzionale
	- Quando la specifica sottende un qualche tipo di flusso di controllo, con possibile rappresentazione esplicita delle dipendenze **def/use**

**Esempi notevoli**:
1. Diagramma di navigazione delle pagine di un'applicazione web
2. Specifica del diagramma di flusso dei dati
3. Flusso di eventi in un template dei casi d'uso (Use Case Template)
4. Flusso concorrente in un diagramma di attività (Activity Diagram)
5. Qualsiasi specifica eseguibile (es. prototipo Matlab)

---
**Generazione di casi di test dai casi d'uso (1/3)**

- **Diagrammi dei casi d'uso** (Use case diagrams)
  - Attori e casi d'uso, stereotipi come <<*includes*>> e <<*extends*>>
  - Livello di astrazione: user goal

- **Template dei casi d'uso**:
  - Specifica testuale dei casi d'uso, più o meno dettagliata
  - Include sempre un flusso di eventi (dialogo utente/sistema, flussi normali/alternativi)
  
- Non solo per lo sviluppo orientato agli oggetti
  - Si adatta bene in una specifica dei requisiti software (SRS - MIL-STD-498)

![[Pasted image 20241121124342.png]]

---
**Generazione di casi di test dai casi d'uso (2/3)**

- I flussi di base e alternativi identificano un **Control Flow Graph (CFG)**
  - Ma anche un **Data Flow Graph (DFG)**, quando i dati sono definiti/utilizzati in fasi diverse del flusso

![[Pasted image 20241121124529.png]]

---
**Generazione di casi di test dai casi d'uso (3/3)**

- I test possono essere selezionati sulla base della copertura di CFG o DFG
	- Più grossolani rispetto alle astrazioni strutturali e solitamente aciclici
	- La copertura può permettere criteri "costosi"
	- Può includere anche criteri funzionali (es. per cicli non deterministici)

- Un caso di test può coprire più flussi

- Uno scenario a livello utente(user-level) può coprire più flussi di diversi casi d'uso

![[Pasted image 20241121124958.png]]

---
**Generazione di casi di test dai diagrammi di attività (1/4)**

- **Diagrammi di attività UML (Activity Diagrams (ADs))** catturano il **flusso di controllo** e la **concorrenza**:
  - Attività, sequenza, inizio/fine, ramo, fork/join

- Derivati dai modelli concettuali delle **reti di Petri**:
  - Posti e token, transizioni, pre-condizioni e post-condizioni, firing

- Derivati dal **Specification and Description Language (SDL)**

- Ben adatti per specificare procedure, processi, flussi di lavoro e modellazione aziendale

- Diagrammi chiave nel **Systems Modeling Language (SysML)**

	![[Pasted image 20241121125320.png]]

---
**Generazione di casi di test dai diagrammi di attività (2/4)**

- **Swimlanes** allocano attività per gli attori e le risorse
	- Diverse partizioni (2 nell'esempio)

![[Pasted image 20241121125524.png]]

---
**Generazione di casi di test dai diagrammi di attività (3/4)**

- I messaggi permettono l'encoding dei segnali scambiati dai diversi processi (come nella semantica dell'SDL)

	![[Pasted image 20241121125658.png]]

---
**Generazione di casi di test dai diagrammi di attività (4/4)**

- Un Activity Diagram è naturalmente astratto da un DFG
	- Specificando il flusso di controllo
	- Specificando le dipendenze def/use fra attività successive oppure concorrenti

![[Pasted image 20241121130001.png]]

---
**Test di unità vs d'integrazione**

- Il test di unità riguarda i singoli componenti
	- Spesso prende una prospettiva strutturale, che dipende dalla decomposizione del design
	- Ad esempio usando *Junit* per singole classi Java oppure usando *Cantata* per testare singole funzioni di file c
	- Effettuato durante lo sviluppo, dalle stesse persone che hanno sviluppato e capito il codice, a meno di divieti nei requisiti di certificazione del processo
	- Senza valore contrattuale, a meno di essere stato prescritto nel modello del processo
	- Spesso con intento formativo, anche nel primo approccio di programmazione

- Il test d'integrazione riguarda diversi componenti
	- Spesso prende una prospettiva funzionale
	- Spesso ha un intento contrattuale, come nel test di accettazione

---
## Test degli stati finiti

**Sistemi reattivi**

- Mantengono un'interazione continua con l'ambiente, spesso solo parzialmente prevedibile, garantendo requisiti funzionali
	- Contrapposti ai sistemi trasformazionali (?)

- Rappresentano un'astrazione per una vasta classe di **sistemi cyber-fisici**:
    - Esempi: sistemi operativi, sistemi di controllo, componenti software embedded, ..., interfacce utente
	- Richiedono formalismi di specifica e metodi di verifica

---
**Macchine a stati finiti**

- Nella pratica industriale, una specifica ruota attorno a una **macchina a stati finiti (FSM)** definita come $\langle S, I, O, E \rangle$:
    - Un insieme di stati $S:\{S_0, S_1, S_2\}$, con stato iniziale $S_0 \in S$
    - Un insieme di input $I : \{a, b, c\}$
    - Un insieme di output $O:\{e, f\}$
    - Un insieme di transizioni $E \subseteq S \times I \times O \times S$

	![[Pasted image 20241121134441.png]]
	
---
**Implementazione e test delle macchine a stati finiti**

- Conseguenze sulla struttura dell’IUT:
    - Funzioni dipendenti dallo stato collegate alle transizioni...
    - Posizioni e istruzioni "goto", ... ,  pattern di stato

- Obiettivi e metodologia di testing:
    - **Conformance testing**: verifica che l’IUT si comporti secondo una macchina a stati finiti (FSM) specificata

---
**Testing di conformità per una macchina a stati finiti**

- Equivalenza tra una specifica $S$ e un IUT $I$:
    - Gli stati $s$ in $S$ e $i$ in $I$ sono *V-equivalenti* se, partendo da $s$ e $i$, la stessa sequenza di input di lunghezza $V$ produce la stessa sequenza di output
    - Gli stati sono equivalenti se sono V-equivalenti per qualsiasi V
    - Le FSM $S$ e $I$ sono equivalenti se i loro stati iniziali sono equivalenti

- Modello di difetto:
    - Output fault: lo stato successivo è corretto, ma l’**output** non lo è
    - Transfer fault: l’output è corretto, ma lo **stato successivo** non lo è
    - Output e Transfer fault possono succedere insieme
    - Ortogonale al Fault Model del testing del control/data flow

---
### Testing di conformità attraverso il metodo WP

- La specifica è una macchina a stati finiti (FSM):
    - **Completamente specificata**: accetta tutti gli input in ogni stato
    - **Osservabile**: in ogni stato, un output è emesso per ciascun input
    - **Deterministica**: una sola transizione e output per ogni stato e input
- L’IUT si comporta come una FSM non identificata:
    - Deterministica, completamente specificata e osservabile
    - La funzione di reset è corretta, ovvero riporta sempre allo stesso stato
    - Ha lo stesso numero di stati della specifica
    - Gli stati non sono osservabili, solo gli output lo sono
- Un tipo di **black-box testing**

---

### Identificazione (1/2)

- Il problema dell’identificazione:
    - Dopo il reset, l’IUT si trova in uno stato non identificato in {S0,S1,S2}\{S_0, S_1, S_2\}
    - L’applicazione di input differenti può disambiguare lo stato iniziale e gli stati visitati, in base agli output osservati

---

### Identificazione (2/2)

- È possibile che la sequenza non finisca mai?
    - Un sottoinsieme stretto sarà eventualmente incontrato, rilevando il ciclo illimitato
    - La dimostrazione di terminazione è simile al lemma di Karp & Miller per le reti di Petri

---

### Metodo W: insieme di caratterizzazione (1/2)

- **Passo 1**: selezionare un insieme di caratterizzazione WW:
    - Un insieme di sequenze di input che disambiguano lo stato iniziale
    - Esempi:
        - W={{a},{b}}W = \{\{a\}, \{b\}\}: rappresenta 2 sequenze di lunghezza 1
        - W={{aa}}W = \{\{aa\}\}: rappresenta 1 sequenza di lunghezza 2
        - W={{ab}}W = \{\{ab\}\}: rappresenta un’altra sequenza di lunghezza 2

---

### Metodo W: insieme di caratterizzazione (2/2)

- Trade-off tra la lunghezza e il numero di sequenze
    - Esempio: W={{a},{b}}W = \{\{a\}, \{b\}\} rispetto a W={{aa}}W = \{\{aa\}\}
- La complessità del reset può influenzare questa scelta (specialmente nei sistemi ciber-fisici)
- Una singola sequenza potrebbe non essere sempre fattibile

---

### Metodo W: copertura degli stati (1/4)

- **Passo 2**: selezionare una suite di test QQ con un caso di test per ogni stato della specifica (partendo dopo un reset)
    - Esempio: Q={{−},{b},{c}}Q = \{\{−\}, \{b\}, \{c\}\}
- Ottenere una copertura degli stati con la suite Q×WQ \times W:
    - Tutte le concatenazioni di un elemento di QQ e uno di WW
    - Esempio: per W={{a},{b}}W = \{\{a\}, \{b\}\}, Q×W={{−},{b},{c}}×{{a},{b}}={{a},{b},{ba},{bb},{ca},{cb}}Q \times W = \{\{−\}, \{b\}, \{c\}\} \times \{\{a\}, \{b\}\} = \{\{a\}, \{b\}, \{ba\}, \{bb\}, \{ca\}, \{cb\}\}

---

### Metodo W: copertura degli stati (2/4)

- Se l’IUT passa la suite di test Q×WQ \times W, allora ogni stato dell’IUT è identificato in modo unico e corretto
- QQ è costruito per terminare in ciascuno stato della specifica
- Il suffisso WW garantisce che lo stato corrisponda a quello nell’IUT
- Esempio: Q×W={{−},{b},{c}}×{{a},{b}}={{a},{b},{ba},{bb},{ca},{cb}}Q \times W = \{\{−\}, \{b\}, \{c\}\} \times \{\{a\}, \{b\}\} = \{\{a\}, \{b\}, \{ba\}, \{bb\}, \{ca\}, \{cb\}\}

---

### Metodo W: copertura degli stati (3/4)

- Esempio di rivelazione di un difetto di trasferimento nello stato S2S_2 attraverso {{c}}×W\{\{c\}\} \times W, poiché WW distingue S1S_1 da S2S_2

---

### Metodo W: copertura delle transizioni (4/4)

- **Passo 3**: selezionare una suite di test PP con un caso di test che attraversi ciascun bordo e termini dopo di esso
    - Esempio: P={{−},{a},{b},{c},{ba},{bb},{bc},{ca},{cb},{cc}}P = \{\{−\}, \{a\}, \{b\}, \{c\}, \{ba\}, \{bb\}, \{bc\}, \{ca\}, \{cb\}, \{cc\}\}
- Ottenere una copertura delle transizioni con P×WP \times W:
    - Tutte le concatenazioni di un elemento di PP e uno di WW
- La copertura delle transizioni rivelerà qualsiasi difetto di trasferimento o di output in ogni bordo della specifica

---

Se vuoi continuare o approfondire altri aspetti, fammi sapere!