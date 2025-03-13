
---
# **00 – Informazioni Amministrative**  

MSc in Intelligenza Artificiale  
MSc in Ingegneria Informatica  
**Marco Lippi**  
📧 [marco.lippi@unifi.it](mailto:marco.lippi@unifi.it)

---
**Indice dei contenuti**

## ▶ Organizzazione del corso

---
**Contenuto del corso (1/5)**

Introduzione e concetti generali
- Intelligenza artificiale sicura e affidabile: motivazioni e sfide
- Intelligenza artificiale spiegabile: tassonomia, metriche
- Interpretabilità progettuale
- Spiegabilità dei modelli black-box
- Applicazioni: giustizia, medicina, sistemi critici per la sicurezza

---
**Contenuto del corso (2/5)**

Modelli interpretabili
- Approcci iniziali: alberi decisionali, modelli lineari generalizzati, liste di regole
- Explainable Boosting Machines
- Modelli basati su prototipi, incorporamento di concetti
- Alberi decisionali ottimali
- Programmazione logica induttiva
- Argomentazione

---
**Contenuto del corso (3/5)**

Spiegazioni post-hoc
- SHAP
- LIME
- Attenzione, mappe di salienza
- Analisi di sensibilità

---
**Contenuto del corso (4/5)**

Intelligenza artificiale neuro-simbolica
- Combinazione di IA simbolica e sottosimbolica
- Logica di Markov, DeepProbLog
- Modelli a colli di bottiglia concettuali

---
**Contenuto del corso (5/5)**

Applicazioni e sessioni pratiche
- Librerie Python per metodi specifici
- Manipolazione e visualizzazione dei dati
- Ispezione dei modelli
- Presentazione dei risultati, calcolo delle metriche
- Problemi reali e casi studio

---
**Orario delle lezioni**

📌 **Lezioni:**
- Martedì, 14:00-16:00, aula S12 @ Santa Marta (14:00-15:30)
- Giovedì, 16:00-18:00, aula 177 @ Santa Marta (16:00-17:30)

📌 **Orario di ricevimento:**
- Martedì, 11:30-13:30 (ufficio @ DINFO, Santa Marta)
- Oppure su appuntamento via email
- In ogni caso, scrivetemi sempre in anticipo!

---
**Materiale didattico**

Il materiale didattico sarà disponibile su **Moodle**:
- Slide (a volte contenenti solo riassunti degli argomenti)
- Appunti dalle lavagne
- Riferimenti a articoli scientifici e capitoli di libri

📢 **Iscrivetevi alla pagina Moodle per:**
- Informazioni sul corso
- Variazioni di orario, annunci
- Aggiornamenti del materiale didattico
- Informazioni sull’organizzazione dell’esame

---
**Esame**

L’esame consiste in una prova orale sui contenuti del corso:
- **Iscrizione** tramite SOL
- **Date disponibili:**
    - Estate: 17 giugno, 1° luglio, 21 luglio
    - Autunno: 1° settembre
    - Inverno/primavera: date da definire

---
**Progetti di laboratorio**

Gli studenti che hanno scelto il **Laboratorio (3 CFU)** nel loro piano di studi svolgeranno un progetto sull’applicazione delle tecniche di **XAI** a problemi reali:

- Diritto
- Medicina
- Sistemi critici per la sicurezza
- Astronomia
- Bibliometria
- …

---

# **01 – Introduzione**  

---
**Indice dei contenuti**

▶ Concetti generali  
▶ Bias e correttezza  
▶ Valutazione  
▶ Analisi esplorativa dei dati  
▶ Esempi

---

## ▶ Concetti generali  

---
**Crediti**

Queste slide sono in gran parte un adattamento di materiale esistente, tra cui:

- _Explainable Artificial Intelligence_ (F. Lecue et al., 2023)
- _Explainable and Trustworthy Artificial Intelligence_ (Politecnico di Torino, 2023)
- _Explainable AI_ (Harvard University, 2023)

🔗 **Riferimenti:**

- [XAI Tutorial 2023](https://xaitutorial2023.github.io/)
- [Politecnico di Torino](https://dbdmg.polito.it/dbdmg_web/2024/explainable-and-trustworthy-ai-2023-2024/)
- [Interpretable ML Class](https://interpretable-ml-class.github.io/)

---
**Cos'è XAI?**

![[Pasted image 20250311082740.png]]

L'Intelligenza Artificiale Spiegabile (_Explainable AI_, XAI) studia e sviluppa **metodi** per rendere **accessibile** e **interpretabile** la logica interna e i risultati dei modelli di intelligenza artificiale, rendendoli **comprensibili agli esseri umani**.

---
**Modelli "scatola nera"**

![[Pasted image 20250311082850.png]]

---
**Modelli "scatola nera"**

![[Pasted image 20250311082923.png]]

---
**Perché abbiamo bisogno della XAI?**

1️⃣ **Per comprendere le decisioni dell'IA**  

![[Pasted image 20250311083033.png]]

---
**Perché abbiamo bisogno della XAI?**

2️⃣ **Per migliorare i modelli di IA**  

![[Pasted image 20250311083124.png]]

---
**Perché abbiamo bisogno della XAI?**

3️⃣ **Per costruire sistemi di IA affidabili e sicuri**

![[Pasted image 20250311083138.png]]

---
**Il problema dell'allineamento**

📖 _"Se utilizziamo un meccanismo che non possiamo controllare in modo efficace… dobbiamo essere certi che lo scopo inserito nella macchina sia quello che desideriamo davvero."_                                         — Norbert Wiener, 1960

---
**Il problema dell'allineamento**

🤖 _Le Tre Leggi della Robotica_ (Isaac Asimov, 1942):  
	1.  Un robot non può arrecare danno a un essere umano, né permettere che un essere umano subisca danni per la sua inazione.  
	2. Un robot deve obbedire agli ordini impartiti dagli esseri umani, a meno che ciò non contrasti con la Prima Legge. 
	3. Un robot deve proteggere la propria esistenza, purché questa protezione non contrasti con la Prima o la Seconda Legge.

---
**Rischi e pericoli dell'uso (o abuso) dell'IA**

![[Pasted image 20250311083519.png]]

---
**Rischi e pericoli dell'uso (o abuso) dell'IA**

![[Pasted image 20250311083536.png]]

---
**Rischi e pericoli dell'uso (o abuso) dell'IA**

![[Pasted image 20250311083915.png]]

---
**Rischi e pericoli dell'uso (o abuso) dell'IA**

**Esempio: Predizione del rischio di polmonite con IA**
Un modello di IA potrebbe imparare erroneamente che i pazienti asmatici hanno un rischio minore di complicazioni perché sono ricoverati **direttamente in terapia intensiva**. Questo porta a conclusioni fuorvianti se si considerano solo i dati storici!

---
**Modelli black-box possono essere presi in giro**

![[Pasted image 20250311084154.png]]

---
**Bias nei dati**

📌 "Perché dovrei fidarmi del tuo modello?" (Ribeiro et al.)  

![[Pasted image 20250311084216.png]]

---
**Bias nei dati**

![[Pasted image 20250311084252.png]]

---
**Tipologie di Bias nei dati**

![[Pasted image 20250311084406.png]]

- **Bias di rappresentazione:** il dataset non rappresenta accuratamente la popolazione.

---
**Tipologie di Bias nei dati**

![[Pasted image 20250311084550.png]]

 - **Bias di campionamento:** alcuni gruppi hanno maggiore probabilità di essere selezionati.
---
**Tipologie di Bias nei dati**

![[Pasted image 20250311084626.png]]

- **Bias di aggregazione:** trarre conclusioni su individui basandosi su dati aggregati (es. Paradosso di Simpson).

---
**Tipologie di Bias nei dati**

![[Pasted image 20250311084702.png]]

- **Bias di artefatto:** correlazioni spurie tra caratteristiche e etichette.

---
**Regolamentazioni sull'IA**

📜 **Regolamento Generale sulla Protezione dei Dati (GDPR)**  

![[Pasted image 20250311155811.png]]

---
**Regolamentazioni sull'IA**

📜 **AI Act (Articolo 13, UE)**  
🔎 I sistemi di IA ad alto rischio devono essere progettati in modo trasparente e accompagnati da istruzioni chiare.

---
**Regolamentazioni sull'IA**

![[Pasted image 20250311155927.png]]

---
**Interpretabilità vs. Spiegabilità**

📌 Alcuni modelli sono **inherently interpretable**, (non necessitano di essere spiegati) come:
- Alberi decisionali
- Modelli lineari
- Sistemi basati su regole
- Programmazione logica induttiva

---
**Interpretabilità vs. Spiegabilità**

Alcuni dicono che esiste un trade-off fra interpretabilità e accuratezza... è davvero il caso?

![[Pasted image 20250311160053.png]]

- Non sempre! Se un modello interpretabile è anche accurato, dovrebbe essere preferito!
- Si usa un modello black-box solo se è necessario... oppure se è l'unico modello disponibile
- Altrimenti prova a costruire delle spiegazioni post-hoc

---
**Tassonomia degli approcci**

📌 **Interpretabili per progettazione:**
- Alberi decisionali
- Sistemi basati su regole(liste, regole)
- Modelli lineari generalizzati
- Programmazione logica induttiva

---

📌 **Spiegazioni post-hoc per modelli black-box:**
- **Spiegazione globale:** costruzione di un modello interpretabile che approssima il sistema.
- **Ispezione del modello:** analisi delle proprietà di un modello opaco, o delle sue predizioni.
- **Spiegazione dell’output:** non ha l'obiettivo di ricostruire il modello opaco del sistema, ma di dare spiegazione di singole predizioni.

---
## ▶ Bias e correttezza nell’IA

---
**Bias**

"Il bias è un errore sistematico nei processi decisionali che porta a risultati ingiusti." (definizione di E.Ferrara, 2023)

Un sistema di machine learning impara e replica patterns di bias presenti nei dati di addestramento.
Identificare e classificare bias è importante per garantire decisioni eque e affidabili.

---
**Tipologie di bias nei dati**

- **Bias di campionamento**:
	Si verifica quando i dati di addestramento non rappresentano in modo casuale l’intera popolazione, cioè alcuni gruppi hanno una probabilità più alta di essere selezionati.  (esempio: Il sondaggio _Literary Digest_ per le elezioni presidenziali USA del 1936, basato su un campione non rappresentativo)

- **Bias di rappresentazione**:
	Simile al bias di campionamento, si verifica quando il dataset non riflette accuratamente la popolazione, ad esempio escludendo o sottorappresentando alcuni sottogruppi.  (Esempio: Dataset di riconoscimento immagini con scarsa rappresentazione di culture non occidentali (_es. ImageNet_))

- **Bias di artefatto**:
	Si verifica quando esistono correlazioni spurie tra caratteristiche dei dati e le etichette, portando il modello a prendere decisioni errate.

-  **Bias di aggregazione**  
	Si verifica quando si fanno inferenze sugli individui basandosi su statistiche aggregate dell’intera popolazione.  
	- Esempio: Il **paradosso di Simpson**.

---
**Bias nei dati: Paradosso di Simpson**

![[Pasted image 20250311174619.png]]

---
**Bias nei dati: Paradosso di Simpson**

![[Pasted image 20250311174647.png]]

---
**Bias nei dati: Paradosso di Simpson**

Qual è il miglior trattamento per una malattia?
- Il **trattamento A** sembra il migliore considerando alcuni gruppi di pazienti.
- Il **trattamento B** sembra il migliore guardando i dati aggregati.

Il paradosso di Simpson si verifica quando una tendenza osservata in più gruppi scompare o si inverte quando i gruppi vengono combinati.

---
**Bias nei dati: Paradosso di Simpson**

Una **Variabile confondente**  è una variabile che influenza sia la variabile indipendente che quella dipendente, causando il paradosso.  

![[Pasted image 20250311174836.png]]

Ad esempio: nello studio sulle malattie renali, la **dimensione dei calcoli renali** ha influenzato la scelta del trattamento (i casi più semplici erano trattati con il metodo B).

---
**Bias nei dati: Paradosso di Simpson**

![[Pasted image 20250311174943.png]]

---
**Bias nei dati: Paradosso di Simpson**

![[Pasted image 20250311175007.png]]

---
**Bias nei dati: Paradosso di Simpson**

**Principio della cosa sicura(?)**

Un azione A che aumenta la probabilità di un evento E in ogni sottopopolazione deve anche aumentare la probabilità di E nell'intera popolazione, in questo modo l'azione non cambia la distribuzione delle sottopopolazioni.

---
**Bias negli algoritmi**

📌 **Bias algoritmico**: 
	Si verifica quando il bias non è presente nei dati, ma è introdotto dall'algoritmo stesso. 
	**Esempio:** Software antiplagio che penalizza maggiormente le persone non madrelingua inglese perché compara sequenze di testo più lunghe.

📌 **Bias da interazione**: 
	Si verifica quando l'interazione con gli esseri umani porta il modello a sviluppare comportamenti discriminatori.  
	**Esempio:** Un chatbot che risponde in modo diverso agli uomini e alle donne.

---
**Bias negli algoritmi**

📌 **Bias di conferma**:  
	Accade quando un sistema di IA viene utilizzato per **rafforzare pregiudizi preesistenti** nei dati o nei suoi utenti.  
	**Esempio:** Algoritmi di selezione del personale che premiano candidati con caratteristiche simili ai dipendenti già assunti.

📌 **Bias generativo**:  
	Si verifica quando un modello generativo produce contenuti che riflettono in modo sproporzionato certi attributi, prospettive o pattern presenti nei dati di addestramento.  
	**Esempio:** Un generatore di immagini che produce sempre figure maschili per il ruolo di "CEO" e femminili per "infermiere".

---
**Concetti di correttezza**

Il bias può facilmente portare a decisioni ingiuste. Ma **come possiamo definire la correttezza?**  

📌 **Definizione:** _La correttezza è l’assenza di pregiudizi o favoritismi nei confronti di un individuo o gruppo, basati su caratteristiche innate o acquisite._

Esistono molte metriche per misurare la **correttezza**. La maggior parte di queste sono basate sull'esistenza di una macchina di machine learning che modella la probabilità P di una classe positiva e le sue relazioni con qualche attributo protetto A.

---
**Correttezza**

📌 **Equalized Odds** 

Un predittore soddisfa equalized odds con rispetto all'attributo protetto $A$ e outcome $Y$, se $Y$ e $A$ sono indipendenti condizionalmente da $\hat{Y}$
	
	$P( \hat{Y} = 1 | A = 0, Y = \gamma) = P(\hat{Y} = 0 | A = 1, Y = \gamma) \space \gamma \in \{0,1\}$

Un predittore soddisfa questa proprietà se la probabilità di classificare correttamente un'istanza positiva (TP) e la probabilità di classificare erroneamente un'istanza negativa (FP) sono le stesse per i gruppi protetti e non protetti.

Gruppi protetti e non dovrebbero avere stessi tassi di  ottenere TP e FP

---
**Correttezza**

📌 **Equal Opportunity** 

Un predittore binario $Y$ soddisfa Equal opportunity con rispetto a $A$ e $Y$ se:

	$P( \hat{Y} = 1 | A = 0, Y = 1) = P(\hat{Y} = 0 | A = 1, Y = 1)$

Un predittore soddisfa questa proprietà se la probabilità di classificare correttamente un'istanza positiva è la stessa per i gruppi protetti e non protetti.

Gruppi protetti e non dovrebbero avere stessi tassi di TP

---
**Correttezza**

📌 **Parità Demografica (Demographic Parity)**  

Un predittore $Y$ soddisfa demographic parity se:

	$P( \hat{Y} | A = 0) = P(\hat{Y}| A = 1)$
	
Un predittore soddisfa questa proprietà se la probabilità (in questo caso likelihood) di ottenere un esito positivo è la stessa indipendentemente dall'appartenenza a un gruppo protetto.

---
**Metodi per garantire la correttezza**

📌 **Fairness through awareness**  
	Un algoritmo è equo se assegna risultati simili a individui con caratteristiche simili, secondo una metrica di somiglianza definita per il compito specifico.

📌 **Fairness through unawareness**  
	Un algoritmo è equo se **non utilizza** esplicitamente caratteristiche protette nella presa di decisione.

---
**Metodi per garantire la correttezza**

📌 **Altri criteri di correttezza**
- **Uguaglianza di trattamento**
- **Equità nei test**
- **Correttezza controfattuale**
- **Equità nei domini relazionali**
- **Parità statistica condizionale**

---
**Come applicare la correttezza nei modelli?**

Come gestire il bias?

1. **Pre-processing:** Modificare i dati prima dell’addestramento per eliminare discriminazioni. 
2. **In-processing:** Modificare gli algoritmi di apprendimento per garantire equità (ad es. cambiando la funzione obiettivo o introducendo vincoli).  
3. **Post-processing:** Intervenire dopo l’addestramento, ad esempio correggendo le predizioni tramite set di validazione.

---
## ▶ Valutazione

---
**Valutazione della spiegabilità**

**Valutare la spiegabilità e l'interpretabilità non è semplice!**  
Ci sono diversi approcci per affrontare il problema:

- Il sistema funziona come previsto?
- Gli utenti del sistema vengono trattati equamente?
- Il sistema è conforme alla normativa?
- Le spiegazioni devono essere valutate nel contesto dell’applicazione?
- Possiamo usare misure quantitative per valutare le spiegazioni?
- Alcune spiegazioni sono migliori di altre?

---
**Valutazione della spiegabilità**

![[Pasted image 20250312185203.png]]

---

**Tipologie di valutazione della spiegabilità**

📌 **Valutazione basata su applicazioni reali (Application-grounded evaluation)**  

- Persone reali, task reali  
- Esperimenti condotti con esperti del dominio su un **compito reale**.  
- Metodo più affidabile, ma anche il più costoso.

---
**Tipologie di valutazione della spiegabilità**

📌 **Valutazione con utenti umani generici (Human-grounded evaluation)**  

- Esperimenti con **non esperti**, su compiti semplificati vicini all’applicazione reale.  
- Permette di testare un **numero maggiore di utenti**, ma è meno preciso (anche se meno costoso)

---
**Tipologie di valutazione della spiegabilità**

📌 **Valutazione basata su metriche computazionali (Functionally-grounded evaluation)**  

- **Non richiede esperimenti con esseri umani**, utile quando non etico o replicabile.  
- Usa metriche **computazionali di proxy**, come l’importanza delle caratteristiche.  
- Utile quando il modello è già stato **validato da esperti umani**. Oppure quando un metodo non è ancora maturo

---
**Valutazione della spiegabilità**

📌 **Metriche di valutazione quantitativa** (Metriche con contributo umano):
- **Completezza:** La spiegazione è completa per l’utente?
- **Semplicità:** Preferenza per spiegazioni più semplici (_Rasoio di Occam_).
- **Comprensibilità:** Quanto tempo impiega un essere umano a capire la spiegazione?
- **Plausibilità:** Quanto la spiegazione è convincente per l’utente?
- **Simulabilità:** L’utente può applicare la spiegazione su nuovi dati?
- **Rilevanza:** Metodologie specifiche per diversi settori (clinico, giuridico, ecc.).

---
**Valutazione della spiegabilità**

 📌 **Metriche ausiliarie (proxy):**
- **Sensibilità:** Quanto un modello è influenzato da un determinato attributo?
- **Continuità:** Esempi simili dovrebbero avere spiegazioni simili.
- **Consistenza:** La spiegazione è coerente tra diversi modelli?
- **Costo computazionale:** Quanto tempo richiede il calcolo della spiegazione?
- **Correttezza:** Confronto con un _ground-truth_ noto.

---

## ▶ Analisi esplorativa dei dati

---
📌 **Principali tecniche di visualizzazione dati:**

- **Analisi univariata:** statistiche descrittive, istogrammi, box plot, ecc.
- **Analisi multivariata:** correlazioni, interazioni tra variabili, ecc.
- **Distribuzione dei dati:** verifica delle caratteristiche di ciascuna feature.
- **Identificazione di outlier:** rilevamento di dati anomali o rumorosi.

---
**Visualizzazione dati**

Attenzione alle statistiche descrittive!

📌 **Esempio: Il quartetto di Anscombe**  

![[Pasted image 20250313144804.png]]

Il quartetto di Anscombe è un insieme di **quattro dataset** creati in modo che abbiano le **stesse statistiche riassuntive (media, varianza, correlazione), ma distribuzioni molto diverse**.

![[Pasted image 20250313144856.png]]

⚠️ Questo dimostra che **guardare solo le statistiche numeriche può essere fuorviante**: è sempre necessaria un'analisi visiva dei dati.

![[Pasted image 20250313144924.png]]

---
**Visualizzazione dati**

📌 **Strumenti per la visualizzazione dei dati**

![[Pasted image 20250313145033.png]]

📌 **Librerie Python più utilizzate:**  
- **Classiche:** `pandas`, `numpy`, `matplotlib`  
- **Più recenti:** `seaborn`, `plotly`, `vega-altair`  
- **Specializzate:** `ydata-profiling`, `FACETS`, `KNIME`  
- **Strumenti interattivi** per l’analisi dinamica dei dati

🔗 **Riferimento:** [Distill - Interactive Data Communication](https://distill.pub/2020/communicating-with-interactive-articles/)

---

## ▶ Esempi

---
📌 **Importanza delle caratteristiche (Feature Importance)**  

![[Pasted image 20250313145134.png]]

✔️ Indica quanto ogni variabile contribuisce alla predizione del modello.

--- 
📌 **Mappe di attenzione (Attention Maps)**  

![[Pasted image 20250313145214.png]]

✔️ Visualizzano quali parti dell’input il modello considera più rilevanti.

---

📌 **Mappe di salienza (Saliency Maps)**  

![[Pasted image 20250313145243.png]]

✔️ Evidenziano le aree più influenti dell’immagine per una predizione.

---
📌 **LIME (Local Interpretable Model-agnostic Explanations)**  

![[Pasted image 20250313145315.png]]

✔️ Genera spiegazioni interpretabili per singole predizioni dei modelli _black-box_.

---
📌 **SHAP (Shapley Additive Explanations)**  

![[Pasted image 20250313145349.png]]

✔️ Metodo basato sulla teoria dei giochi per assegnare **valori di contributo equi** a ciascuna caratteristica del modello.

---

