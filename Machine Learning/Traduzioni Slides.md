# 1 - Introduzione
---

**Fondamenti di Apprendimento Automatico:**

**Introduzione e Concetti di Base**

Prof. Andrew D. Bagdanov (andrew.bagdanov AT unifi.it)

**UNIVERSITÀ**
**DEGLI STUDI**
**FIRENZE**

**DINFO**

**DIPARTIMENTO DI**
**INGEGNERIA**
**DELL'INFORMAZIONE**

---
## Introduzione

---
**Obiettivi della Lezione**

Alla fine di questa lezione avrete:

- Sviluppato **intuizioni di base** su cosa sia l'Apprendimento Automatico.
- Compreso come la vostra padronanza degli argomenti del corso sarà misurata nell'esame finale.
- Compreso la formulazione della Minimizzazione del Rischio Empirico dell'apprendimento.
- Acquisito intuizioni di base sui componenti principali dell'approccio di minimizzazione del rischio e su cosa significano.

	2
---

**Il mondo di "domani"**

- Link al video

	![[Pasted image 20250917223153.png]]

	3
---
**Cos'è l'Apprendimento Automatico?**

“Ho studiato tutte le carte celesti disponibili di pianeti e stelle e nessuna corrisponde alle altre. Ci sono tante misurazioni e metodi quanti sono gli astronomi e tutti sono in disaccordo. Ciò che serve è un progetto a lungo termine con l'obiettivo di mappare i cieli condotto da una singola località per un periodo di diversi anni.”

	- Tycho Brahe, 1563 (età 17 anni).
(Tycho dice mannagg ar cazzo non ci sono abbastanza dati)

- Il termine Apprendimento Automatico risale ad Arthur Samuel negli anni '50.
- Negli anni successivi il suo ambito si è espanso e contratto.
- Un modo di pensare l'apprendimento automatico è:

	$$\text{Apprendimento Automatico} = \text{(Statistica Computazionale + Ottimizzazione)} + \text{Dati (di solito molti)}$$

	4
---
**Cos'è l'Apprendimento Automatico?**

“Si dice che un programma per computer apprenda dall'esperienza E rispetto ad alcune classi di compiti T e **misura di performance** P se la sua performance nei compiti in T, misurata da P, migliora con l'esperienza E.” => tipo vedo se aumenta accuratezza di classificazione

	- Tom Mitchell, 1987

- Questa definizione è simile alle definizioni (moderne) di Intelligenza Artificiale. 
- Cioè, è operativa invece che cognitiva.
- Alan Turing iniziò questa tendenza cambiando la domanda da “Le macchine possono pensare?” a “Le macchine possono fare ciò che noi (come entità pensanti) possiamo fare?”.

	5
--- 
**Apprendimento supervisionato versus non supervisionato**

- L'Apprendimento Automatico è (molto approssimativamente) diviso in due macro categorie di approcci di apprendimento:
  - **Apprendimento Supervisionato**: a volte chiamato “apprendere da un insegnante” si riferisce a una classe di approcci che mirano ad apprendere a predire output da *input* partendo da un dataset di input e output accoppiati. => immagine e questa è un immagine di un gatto"
  - **Apprendimento Non Supervisionato**: che invece cerca di apprendere “qualcosa” da dati di input **non etichettati** – cioè, senza etichette pre-specificate. => tipo GPT, tanti dati senza supervisore => self supervisor

- In questo corso introduttivo ci limiteremo per lo più all'apprendimento supervisionato.
- Nota che esiste, in effetti, uno spettro completo di regimi di supervisione: supervisionato, debolmente supervisionato, semi-supervisionato, auto-supervisionato, non supervisionato. (algoritmi non supervisionati ci so a data mining)

	6
---
**Apprendimento supervisionato: un esempio**

- Supponiamo di analizzare la correlazione tra **altezza** e **peso**.
- (A parte: useremo spesso esempi sintetici di questo tipo per illustrare concetti e tecniche chiave.)
- E supponiamo di avere solo due punti dati:
  $$ (67.9, 170.85) \text{ e } (61.9, 122.5)$$

- Idealmente, desideriamo inferire una **relazione** tra altezza e peso che spieghi i dati.
- Un buon primo passo è di solito visualizzare.

	7
---
**Apprendimento supervisionato: un esempio**

• Quindi, abbiamo una situazione come questa…
• Cosa possiamo fare?

![[Pasted image 20250917230650.png]]

	8
---
**Apprendimento supervisionato: un esempio**

- Beh, un po' di algebra delle scuole medie ci permette di connettere i punti:  $$y = 8.013x - 373.247$$ perché questo modello? => tipo perché non una parabola? 
=> la retta è il modello più semplice! => con due sole variabili!

![[Pasted image 20250917230839.png]]

	9
---
**Apprendimento supervisionato: un esempio**

- Ora supponiamo di avere molti più dati.
- Il nostro “modello” generalizza?

![[Pasted image 20250917231024.png]]

- In alcune parti potremmo fare meglio in altre peggio... Come migliorare? avendo più punti e solo con due parametri devo decidere quale sia il miglior modello che generalizza i dati.

	10
----
## Organizzazione e Obiettivi del Corso

---
**Prerequisiti (Matematica)**

- Questo corso richiede un certo grado di maturità matematica, così come una padronanza delle basi della programmazione, degli algoritmi e delle strutture dati.

- I **Concetti Matematici** Chiave che dovreste conoscere includono:
  - Cos'è il rango di una matrice. Cosa significa essere rank-deficient (a rango carente)?
  - Cosa sono gli autovalori e gli autovettori di una matrice? Cosa significano?
  - Cos'è il gradiente di una funzione multivariata? In quale direzione punta? => direzione nel quale la direzione è più ripida.
  - Cos'è un prodotto scalare (punto) tra due vettori?  
  - Cos'è la norma di un vettore? Cosa ha a che fare con il prodotto scalare?

	11
---
**Prerequisiti (Statistica e Teoria della Probabilità)**

- I Concetti **Statistici** Chiave che dovreste conoscere includono:
  - Cos'è la Regola della **Somma della probabilità**? E la Regola del Prodotto?
  - Cosa hanno a che fare queste regole con le **funzioni di densità** di probabilità Congiunta, Condizionata e Marginale?
  - Cos'è la **Regola di Bayes**? Cosa significa e come possiamo derivarla?
  - Cos'è una Variabile Casuale? Cos'è il Valore Atteso di una (funzione di una) variabile casuale?

	12
---
**Prerequisiti (Informatica)**

- Le competenze chiave dell'Informatica sono più difficili da elencare:
  - Dovete avere una padronanza operativa di almeno un linguaggio di programmazione di alto livello (preferibilmente uno dinamico come Python, R, Matlab o Lisp).
  - Le sessioni di laboratorio saranno svolte utilizzando Python e il suo eccellente ecosistema per la programmazione numerica.
  - Per favore utilizzate Questo Autovalutazione delle Competenze di Programmazione per verificare che la vostra conoscenza e competenza sia almeno da qualche parte tra i livelli A2 e B1.

	13
---
**Organizzazione**

Questo corso è sui **Fondamenti dell'Apprendimento Automatico**, e in esso tratteremo:

- Fondamenti dei Fondamenti: teoria della probabilità e statistica per l'apprendimento automatico, distribuzioni di probabilità, basi della teoria dell'informazione (NO), interpretazioni bayesiane versus frequentiste, modelli lineari per la regressione, modelli lineari per la classificazione, la scomposizione bias-varianza, overfitting e underfitting, regolarizzazione del modello, modelli generativi probabilistici, modelli discriminativi probabilistici, **Stima di Massima Verosimiglianza** (Likelihood) (MLE), inferenza Massima a Posteriori (MAP), inferenza bayesiana. => primo modulo su regressione e classificazione

- Apprendimento Automatico: **Macchine a Vettori di Supporto** (SVM), modelli kernel, modelli grafici (NO), alberi decisionali, metodi ensemble, boosting, bagging, media bayesiana di modelli, foreste casuali, Expectation Maximization (EM), stima della densità di misture.

	14
---
**Organizzazione**

- Apprendimento Profondo(Deep Learning): modelli connessionisti, regole di apprendimento hebbiane, il percettrone, reti neurali, Discesa del Gradiente Stocastica (SGD), l'algoritmo di Backpropagation, il Percettrone Multistrato (MLP), gradienti che svaniscono ed esplodenti, dimensione del modello e regolarizzazione, regolarizzazione della rete.
- Argomenti Speciali e Applicazioni: Reti Neurali Ricorrenti a Memoria a Lungo-Termine (LSTM) (NO), elaborazione del linguaggio naturale e modelli linguistici (Transformers), Reti Neurali Convoluzionali (CNN), apprendimento auto-supervisionato, apprendimento continuo, adattamento del dominio, transfer learning.
- Strumenti, Tecniche e Best Practices: programmazione numerica, visualizzazione, diagnostica del modello e monitoraggio dell'addestramento, scikit-learn (buono per per documentazione), PyTorch(framework scelto principalmente per machine learning).

	15
---
**Una Timeline Approssimativa del Materiale**

 - **Parte I:** Apprendimento Automatico Classico
	- Preliminari: La matematica, concetti fondamentali, notazione e tecniche utili.
	- Modelli Lineari: Modelli “semplici” per regressione e classificazione, interpretazioni geometriche e probabilistiche, modelli generativi e discriminativi, regolarizzazione e conoscenza a priori.
	- Metodi Kernel: La Macchina a Vettori di Supporto (SVM) lineare, problemi non linearmente separabili e rilassamento, il kernel trick e SVM non lineari.
	- Metodi Locali: Metodi dei Vicini Più Prossimi, stima della densità non parametrica.
	- Apprendimento Non Supervisionato: Analisi delle Componenti Principali (PCA), Modelli di Mistura Gaussiana (GMM), l'algoritmo Expectation-Maximization (EM).

- **Parte II**: Apprendimento Profondo
	- Modelli Connessionisti: Storia, apprendimento hebbiano, il Percettrone e l'apprendimento basato su gradiente.
	- Reti Profonde: Percettroni Multistrato (MLP), Reti Neurali Convoluzionali (CNN).
	- Argomenti Avanzati: Reti Neurali Ricorrenti a Memoria a Lungo-Termine (LSTM), Transfer learning, Apprendimento auto-supervisionato, Transformers.

	16
---
**Laboratori**

- Quest'anno ci saranno quattro (4) sessioni di laboratorio focalizzate su argomenti chiave:
  - Modelli lineari per regressione e classificazione
  - Apprendimento non supervisionato
  - Apprendimento Profondo I
  - Apprendimento Profondo II

- Nelle sessioni di laboratorio (sempre di martedì /forse giovedì) lavoreremo insieme su una serie di problemi.

- Una settimana prima pubblicherò i laboratori e un breve tutorial per iniziare.

- Sottometterete le vostre soluzioni *individuali* ai laboratori dopo 7-10 giorni – ci sarà un piccolo bonus per chi sottomette le soluzioni dei lab in tempo.

- Verranno utilizzati solo *i tre (3) voti più alti dei laboratori* (cioè potete saltarne uno).

	17
---
**Valutazione dello Studente**

- La valutazione finale si basa su diverse componenti:

| Tipo         | Componente                 | Peso                                         |
| ------------ | -------------------------- | -------------------------------------------- |
| Obbligatorio | Laboratorio/Compiti a casa | \(1/3 (+1/30 \, $\text{bonus puntualità})$\) |
| Opzionale    | Esame Scritto Intermedio   | \(1/3\)                                      |
| Obbligatorio | Esame Scritto Finale       | \(1/3 \, ($\text{o}$ \, 2/3)\)               |
| Opzionale    | Esame Orale Finale         | \($\pm 1/30$ \, ($\text{per la lode})$\)     |

- Importante: Il voto dell'esame intermedio è valido per i primi quattro appelli finali successivi alla fine del corso (cioè fino e incluso l'appello di Pasqua).
- Importante: Se usate il voto dell'esame intermedio, l'esame finale coprirà solo la seconda metà del corso. Altrimenti, l'esame finale è comprensivo.

	18
---
**Obiettivi di Alto Livello**

- L'Apprendimento Automatico è un campo ampio e molto attivo.
- A un livello base, riguarda l'apprendere da dati di addestramento per fare inferenze su nuovi dati.
- Questa descrizione piuttosto vaga articola già concetti chiave che studieremo in dettaglio.
- Per impiegare l'Apprendimento Automatico nella pratica, dobbiamo familiarizzare con alcuni strumenti teorici.
- Questi strumenti ci aiuteranno a modellare problemi di apprendimento, valutare le performance dei sistemi di apprendimento e quantificare la fiducia nelle nostre soluzioni.

	19
---
**Obiettivi: Teoria e Pratica**

Facciamo un passo indietro e pensiamo a obiettivi più astratti:

- In questo corso daremo un'occhiata relativamente approfondita a diverse teorie fondamentali dell'Apprendimento Automatico.
- La teoria è importante, ma non è tutto.
- Probabilmente il 95% delle volte non avete esplicitamente bisogno di teorie sofisticate.
- Tuttavia, per quel 5% rimanente diventa improvvisamente indispensabile – specialmente quando si cerca di capire perché le cose non funzionano come previsto.
- Quindi, non preoccupatevi se non afferrate ogni intuizione o derivazione dalle versioni abbreviate qui. (il bro ci dirà cosa è effettivamente più importante)
- Assimilate, costruite intuizione sulla teoria che informerà la vostra pratica.
	
	20
---
**Buoni libri**

- Tre grandi libri di ML (e un libro autorevole sul deep learning):
  - C. M. Bishop, *Pattern Recognition and Machine Learning*. Springer, 2006.
  - D. MacKay, *Information Theory, Inference and Learning Algorithms*. Cambridge University Press, 2003.
  - Zhang et al., *Dive into Deep Learning*, 2023.

- Il primo è un testo classico sul ML, ed è la base del trattamento (e di molti dei grafici) che uso qui.

- Il libro di Bishop è anche liberamente disponibile (edizione 2006) online a Questo Link

- Il secondo libro è pieno di eccellenti intuizioni sulle relazioni tra ottimizzazione, teoria dell'informazione e inferenza bayesiana.

- Il terzo è una grande risorsa online per tutti i tipi di deep learning.

	21
---
**Ma... Sembra un sacco di lavoro.**

- Corretto. In questo corso chiedo molte cose diverse per raggiungere i nostri obiettivi di apprendimento.
- Ma, analizziamolo:
  - 25 ore/CFU × 6 CFU = 150 ore totali
  - 8 ore di lezione in aula/CFU × 6 CFU = 48 ore totali in aula
  - Restano: 102 ore totali di studio indipendente per lab e preparazione esame

- Tuttavia,
  - 10-15 ore di laboratorio in aula.
  - La sottomissione puntuale dei lab contribuisce per il 33+% al voto finale.
  - In più, 4-6 ore di sessioni di preparazione all'esame (esercitazioni).

- Il punto: L'organizzazione del corso è progettata per aiutarvi a avere successo, e ad averlo in tempo.

	22
---
**Buone e cattive notizie (per lo più buone, davvero)**

- Tutti facciamo un respiro profondo prima di continuare a leggere:

I vostri giorni di apprendimento in ambienti di apprendimento strutturati sono (quasi) finiti.
=> Define your learning objectives? 

	23
---
**Cosa ci si aspetta da voi (e dal vostro professore (io))**

- Possiede conoscenza e intuizione dimostrabili, basate sulla conoscenza e intuizione a livello di Laurea Triennale che la superano e/o approfondiscono, oltre a fornire una base o un'opportunità per dare un contributo originale allo sviluppo e/o applicazione di idee, spesso in un contesto di ricerca.
- È in grado di applicare conoscenza, intuizione e capacità di problem solving in circostanze nuove o sconosciute in un contesto più ampio (o multidisciplinare) relativo al campo di competenza; è in grado di integrare conoscenze e gestire materie complesse.
- È in grado di formulare giudizi sulla base di informazioni incomplete o limitate, tenendo conto delle responsabilità sociali ed etiche associate all'applicazione delle proprie conoscenze e giudizi.
- È in grado di comunicare conclusioni, così come le conoscenze, motivazioni e considerazioni che le sottendono, in modo chiaro e non ambiguo a un pubblico di specialisti o non specialisti.
- Possiede le capacità di apprendimento che gli/le permettono di intraprendere uno studio successivo con un carattere largamente auto-diretto o autonomo.

	24
---
## Generalizzare la nostra Intuizione

---
**Apprendimento Automatico in (un guscio di noce matematicamente denso)**

Gli ingredienti:

- Uno spazio di input $\mathcal{X}$ (spesso $\mathbb{R}^m$ e uno spazio di output $\mathcal{Y}$ (spesso $\mathbb{R}^n$).

- Un'**assunzione generativa** di una funzione (per la relazione fra i due spazi) $h : \mathcal{X} \to \mathcal{Y}$ (spesso $y = h(x) + \varepsilon$). => voglio capire quale sia h, tramite $\epsilon$ aggiungo un po' di rumore/confusione

- Una **densità di probabilità congiunta** sconosciuta $p(x, y)$ su $\mathcal{X}$ e $\mathcal{Y}$. => mi aspetto qualche relazione fra i due spazi
- Uno spazio di ipotesi $\mathcal{H}$ di funzioni da $\mathcal{X}$ a $\mathcal{Y}$. 
- Una **funzione di perdita** $\mathcal{L} : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$. => cerco la funzione migliore che approssima all'interno del mio spazio di Ipotesi => certe volte chiamata risk function => funzione di perdita alta quando la nostra funzione non si comporta bene!

Un obiettivo di apprendimento:

- Assumendo che la vera $h \in \mathcal{H}$, possiamo semplicemente:
$$h^* = \arg \min_{h \in \mathcal{H}} \mathbb{E}_p[\mathcal{L}(h(x), y)] =$$ $$\arg \min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$
Problema di minimizzazione => integro su tutti i valori x,y => expectation di una loss value tramite una likelihood sui dati => cerco di penalizzare il più possibile quei valori che hanno una alta similirità ma anche un loss value molto alta! (vado a vedere il valore restituito da h e confronto con y) => questo fra tutte le combinazioni di x e y 

	25
---
**Abbiamo finito?**

- **Possiamo andare a casa?**$$h^* = \arg\min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$
- Non possiamo ancora andare a casa. Cominciamo con la grande incognita $p$ => non sappiamo appunto la relazione fra x e y => è quella che vogliamo scoprire!

- Senza informazioni su $p$ dobbiamo ricorrere al **campionamento**:  $$(x_i, y_i) \in \mathcal{X} \times \mathcal{Y}, \text{ per } i \in \{1, \ldots, N\}$$
- Importante: $(x_i, y_i) \sim p(x, y)$

- Possiamo allora approssimare l'obiettivo con la perdita attesa empirica(empirical expected loss/empirical risk minimization): $$h^* = \arg\min_{h \in \mathcal{H}} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}(h(x_i), y_i)$$
	26
---
**Abbiamo finito ora?**

- **Bene. Ora possiamo andare a casa?** $$h^* = \arg\min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$$$\approx \arg\min_{h \in \mathcal{H}} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}(h(x_i), y_i)$$
- Non possiamo.
- E riguardo a $\mathcal{L}$ ?
- E riguardo a $\mathcal{H}$ ?

Scegliendo ad esempio un h* che sia esattamente y e una loss qualsiasi (tipo quadratica)... rischio di avere un modello che approssima troppo => extreme over-fitting

- E riguardo a quella spaventosa minimizzazione?
- Infine, e riguardo a $\mathcal{X}$ e $\mathcal{Y}$ => occhio alle rappresentazioni fra spazio di partenza e fine => tipo immagini e classificazione come output => che cosa devo avere come output?

	27
---
**Generalizzare**

- Torniamo all'esempio semplice, ma cosa succede se abbiamo dati distribuiti come sotto?
- Processo: $y = f(x) + \varepsilon$ (dove $\varepsilon$ è rumore gaussiano).

	![[Pasted image 20250918100418.png]]
	=> Notare che il rumore ci aiuta a non essere troppo precisi nel trovare il modello corretto => utile per generalizzare

	28
---
**Generalizzare**

- Il nostro obiettivo è sfruttare questo training set per fare previsioni.
- Cioè, predire il target $\hat{y} = f(\hat{x})$ per nuovi $\hat{x}$.
- Nel fare questo stiamo implicitamente cercando di apprendere quale sia la underlying $f$.
- L'apprendimento dovrebbe essere indipendente da $\varepsilon$ (che non vogliamo catturare).

	![[Pasted image 20250925103824.png]]

	29
---
**Un diverso tipo di problema**

- A volte vogliamo capire come i dati sono generati da $N$ sorgenti.
- Con l'obiettivo di discriminare le sorgenti l'una dall'altra.

	![[Pasted image 20250918110847.png]]

	30
---
**Discriminare**

- Idea generale: trovare un **iperpiano** separatore.
- Cioè, uno che **separi una classe dall'altra**.

	![[Pasted image 20250918111902.png]]

	31
---
**Ma quale?**

- Quale è il discriminante “migliore”?
- Cosa significa addirittura migliore qui?

	![[Pasted image 20250918111941.png]]

	=> Ci viene così in aiuto la loss function => per scegliere quale retta preferire rispetto ad un altra!
	
	32
---
**Due visioni (e l'obbligatorio esempio del lancio della moneta)**

- Supponiamo di avere una moneta e vogliamo decidere se è equa o no.
- Qualcuno ha eseguito un esperimento da cui ha derivato questa stima:

	![[Pasted image 20250918112120.png]]
	testa vs croce => quanto è credibile questo outcome? 
	
	33
---
**Due visioni**

- E se i dati fossero riassunti invece in questo modo.
- Questo ti fa ripensare la tua inferenza sulla moneta?

	![[Pasted image 20250918112324.png]]
	Forse meglio questo... anche qui come scelgo l'approccio migliore?

	33
---
**Due visioni**

- Quando stimiamo i parametri di un modello (a volte riferito come inferenza), dobbiamo applicare tutto ciò che sappiamo.
- In particolare, dobbiamo stare attenti a quantificare ogni volta possibile la nostra fiducia nell'accuratezza delle nostre inferenze.

	![[Pasted image 20250918112610.png]]

	34
---
**Un esempio motivante**

- Tornando al nostro semplice problema di *regressione*: osserviamo una variabile di input a valori reali $x$ e vogliamo predire una **variabile target** a valori reali $t$.

- Ai fini della dimostrazione, consideriamo un esempio artificiale di dati generati sinteticamente: $y = f(x|w) + \varepsilon$ (con **w** il vettore dei parametri del modello)
	 => il rumore ci ha portato a questi dati

- Ci viene dato un **training set** di coppie \((x, y)\) campionate da $p(x, y)$.
- Obiettivo: apprendere la funzione sottostante $f$ che ha generato questi dati.
- In questo modo, per $\hat{x}$ non visto possiamo usare $f(\hat{x}|w^*)$ per predire il target $\hat{y}$.

	![[Pasted image 20250918113923.png]]

	36
---
**Un esempio motivante**

- Modelliamo questo problema come uno di "fitting di curve", per esempio usando un modello polinomiale: $$y(x|w) = w_0 + w_1x + w_2x^2 + \cdots w_Mx^M$$$$= \sum_{j=0}^M w_j x^j$$ mi diventa  semplicemente il prodotto dei due vettori **x** e **w** => ottengo un qualsiasi polinomio di qualsiasi grado

- Nota come, anche se $y(x|w)$ è una funzione **non lineare** di $x$ , è una **funzione lineare** nei coefficienti $w$ (cioè i parametri del modello).

- Per *apprendimento* intendiamo stimare i parametri “migliori” $w$  dal dataset
  $D = \{(x_i, y_i) \mid i = 1, \ldots, N\}.$

	37
---
**Un esempio motivante**

- Cosa significa **buono** in questo contesto?
- Beh, possiamo cominciare pensando di misurare **l'errore nella funzione** stimata in termini dei dati osservati:$$\mathcal{L}(w|D) = \frac{1}{2} \sum_{(x,t)\in D} \{y(x,w) - t\}^2$$
- Che è una funzione **quadratica** in $w$, (e anche monotona) quindi le sue derivate sono lineari => funzione anche convessa => ha un unico minimizzatore!
- E $\mathcal{L}(w|D)$ ha un unico minimizzatore $w^*$.  => minore è la loss e migliore è modello  => sempre se abbiamo scelto una buona loss => avere loss pari a zero può essere segno di overfitting
- Abbiamo finito?
	![[Pasted image 20250925104216.png]]

	38
---
**Un esempio motivante**

- Non abbiamo finito. C'è un *iperparametro* del nostro modello che abbiamo convenientemente dimenticato: l'ordine del polinomio $M$.
	![[Pasted image 20250925104352.png]]
	Sembra abbastanza buona...
	
	![[Pasted image 20250925104416.png]]Qui la loss è anche zero => ma le prossime predizioni non sono molto buone... sulla scelta della M bisogna stare attenti al rischio di overfitting...

	39-40
---
**Un esempio motivante**

- Il problema rimanente è la selezione del modello, ed è un elemento fondamentale dell'apprendimento automatico. Come potremmo affrontarlo?
- Otteniamo intuizione sull'**underfitting** e sull'**overfitting** disegnando un test set indipendente e tracciando $$E_{RMS} = \sqrt{2\mathcal{L}(w^*|D)/N}$$
	![[Pasted image 20250925104512.png]]
	=> esempio di crossvalidation => validation curve => fittiamo il modello alla crescita del grado del polinomio... ad un certo punto noto che il polinomio non generalizza più! compie grossi errori nella fase di test!
	
	41-42
---
## La Gen-X Insegna alla Gen-Y e alla Gen-Z (su X, Y e Z)

---
**Un po' di me**

- Foto di bagdy => piazza della signorina lololol

	43
---
**I primi anni: anni '80 e '90 (big math)**

**Matematica: grandi cardinali e determinacy**

- Il mio primo amore è stata la matematica, che ho studiato alla University of Nevada, Las Vegas (sì, quella Las Vegas).
- Specificamente, teoria descrittiva degli insiemi e la relazione tra Ipotesi dei Grandi Cardinali, determinacy di giochi semplici su insiemi di numeri reali, e la consistenza di tutta la matematica.

	44
---
**I primi anni: anni '80 e '90 (elaborazione di immagini)**

**Matematica: grandi cardinali e determinacy**

- In parallelo, ho lavorato su problemi di stima di immagini low-level.
- Specificamente, sulla stima di orientamenti locali e globali in immagini di documenti scannerizzati.
- La novità all'epoca, era investigare come stimare in domini compressi.

	45
---
**Gli anni di Amsterdam: primi anni 2000 (visione)**

- Nel 1999 mi sono trasferito in Europa per un dottorato in Analisi di Informazione Multimediale alla *Universiteit van Amsterdam*:
  - Visione low-level: gradient boosting e inversione di mezzitoni.
  - Morfologia matematica: analisi granulometrica della struttura profonda dell'immagine.
  - Modelli a grafo: analisi del layout di immagini con First-order Gaussian Graphs.
  - Programmazione funzionale: modelli formali di programmi di visione.

	46
---
**Non c'è tempo, lasciatemi riassumere...**

- Anni '60 (California): Nato, Los Angeles.
- Anni '70 (Washington): Manovale, Washington rurale.
- Anni '80 (Las Vegas): Studente delle superiori; Deadhead; game designer e programmatore per Westwood Studios; utente Emacs.
- Anni '90 (Las Vegas): Musicista semi-professionista; barista; buttafuori di pub sportivi; contatore di auto; tutor di matematica; studente doppia Laurea/Magistrale in Matematica/Informatica; Senior Network Analysis, US Department of Energy.
- Primi anni 2000 (Amsterdam): PhD, University of Amsterdam; utente Emacs; Deadhead.
- Tardi anni 2000 (New York/Firenze/Roma): Postdoc Renselaer Polytechnic Institute; Deadhead; postdoc Università di Firenze; Capo Sviluppo Senior, Organizzazione per il Cibo e l'Agricoltura delle Nazioni Unite.
- Primi anni 2010 (Firenze/Barcellona): Capo Progetto, Computer Vision Center, Barcellona; Professore a contratto, Universitat Autonoma de Barcelona; Capo Unità di Ricerca, MICC, Università di Firenze, Borsista Ramon y Cajal, Computer Vision Center, Barcellona; utente Emacs; Deadhead.
- Oggi: Professore DINFO, Università di Firenze; utente Emacs; Deadhead.

	47
---
**Sì, ma cosa fai, tipo adesso?**

- In questo momento la mia ricerca si focalizza su problemi di **apprendimento continuo** in visione artificiale e linguaggio:

![[Pasted image 20250923123304.png]]
 => passando a risolvere task B rischio di dimenticarmi i parametri ottenuti come migliori per il task A => cerco delle soluzioni che mi soddisfano entrambi i task
 
	48
---
**Inoltre, giochi!**

- Con un dottorando (Alessandro Sestini) ricerco anche tecniche di Apprendimento per Rinforzo Profondo (*Deep reinforcement learning*) per costruire Agenti Non Giocatore (NPA) intelligenti.
	
	![[Pasted image 20250923123424.png]]

	49
---
**Filosofia e stile di insegnamento**

- L'apprendimento è più efficace quando è uno scambio interattivo piuttosto che uno stare-lì-e-ascoltare passivo.
- Il mio lavoro come professore è mettere la mia conoscenza a vostra disposizione.
- Il vostro lavoro è succhiare ogni ultimo bit di conoscenza da me in queste lezioni.
- Se non capite qualcosa, interrompetemi e chiedetemi di chiarire.
- [ Parabola del 'ne so così tanto' ]

	50
---
## Osservazioni Conclusive

---
**Costruzione di Comunità: Il Discord UniFI AI**

- Abbiamo creato un Server Discord per ospitare discussioni sull'Intelligenza Artificiale.
- C'è un canale dedicato per il corso di Fondamenti di Apprendimento Automatico (FML).
- Per favore unitevi, e sentitevi liberi di usare questo server per condividere, scambiare informazioni, chiedere aiuto e per chiacchiere generiche relative a ML, AI, dataset, qualsiasi cosa.
- Importante: questo è un forum pubblico, quindi siate gentili, siate rispettosi e divertitevi.

https://discord.gg/tUkgrgXdXE
	
	51
---
**La strada da percorrere**

- Nella prossima lezione tratteremo alcune preliminari (per lo più matematiche) che saranno utili durante tutto il corso.
- Più specificamente, tratterò alcuni concetti fondamentali di algebra lineare, statistica e probabilità, e le importanti proprietà della distribuzione Gaussiana.
- Costruiremo anche un'intuizione sul perché l'Apprendimento Automatico è difficile attraverso un'analisi della Maledizione della Dimensionalità.

“Tycho possiede le osservazioni più accurate del mondo, ma gli manca un architetto capace di costruire un edificio partendo dai suoi dati.” => keplero letteramente machine learning prima di tutti

– Johannes Keppler

	52
---
**Letture e Compiti a Casa**

- **Lettura Assegnata**:
	- Bishop: Capitolo 1 (1.1, 1.3, 1.4)

- **Compiti a Casa**:

1. Familiarizzate con l'UCI Machine Learning Repository di dataset liberamente disponibili per la ricerca sul ML.

2. Meditate sull'esempio del lancio della moneta e pensate a come potremmo mitigare i problemi discussi durante la lezione (cioè come prendere pulitamente in considerazione la nostra confidenza sulla nostra stima).
   Suggerimento: Pensatela come un problema di stima sequenziale e usate la Regola di Bayes.

	53
---

# 2 - Preliminari Matematici

---
## Introduzione

---
**Obiettivi della lezione**

Alla fine di questa lezione avrete:

- Rinfrescato la memoria sui concetti e operazioni di base dell'algebra lineare.
- Rinfrescato la memoria sulle regole di base della teoria della probabilità, cioè le regole della somma e del prodotto.
- Rinfrescato la memoria sulle probabilità condizionate e il teorema di Bayes.
- Acquisito un'intuizione di base sulla teoria decisionale probabilistica.
- Compreso intuitivamente la Maledizione della Dimensionalità.

	2
---
**La matematica del 21esimo secolo**

- Padroneggiare l'apprendimento automatico contemporaneo richiede una gamma di strumenti e discipline...

	![[Pasted image 20250923144539.png]]
	
	3
---
 **Algebra lineare**

- Skyler Speakerman si è recentemente riferito all'Algebra Lineare come alla *matematica per il 21esimo Secolo*.
- Questo potrebbe essere leggermente iperbolico, ma l'algebra lineare è assolutamente centrale per il moderno apprendimento automatico.
- L'algebra lineare ci permette di trattare dati ad alta dimensionalità in modo formale e preciso.
- Ci permetterà di modellare gli input agli algoritmi di ML come punti in spazi ad alta dimensionalità.
- E successivamente di modellare trasformazioni funzionali di questi input in spazi delle caratteristiche.
- E infine, di modellare le trasformazioni successive che portano agli output (es. decisioni o azioni o stime).

	4
---
**Algebra lineare (continua)**

- Cos'è un'**immagine**? È una **struttura dati**, con larghezza e altezza e profondità, più un array corrispondente di dati grezzi?
- Possiamo continuare... Cos'è una registrazione audio? O un documento di testo.
- Piuttosto che definire strutture *ad hoc*, vogliamo trattare tutto allo stesso modo.

- Un'immagine a colori 512 × 512 è un vettore in uno spazio vettoriale $512 \times 512 \times 3$ -dimensionale. => tipo un vettore con associato ad ogni pixel i valori di r-g-b => vettore molto grande ma comunque un vettore! (vectorized/linearized version) => ci posso fare quindi operazioni matriciali! 

	5
---
**Probabilità e statistica**

- Forse un po' a sorpresa, probabilità e statistica sono **meno importanti** per il moderno apprendimento automatico. => danno comunque tool importanti per ML
- A volte vorremo dare un'interpretazione probabilistica a un modello o a un output del modello.
- Tuttavia, la maggior parte dei modelli di deep learning sono definiti come pure trasformazioni di input in output.
- Spesso, queste interpretazioni probabilistiche sono mere finzioni convenienti.
- Come vedremo, statistica e probabilità sono molto utili come strumenti per analizzare i risultati.

	6
---
**Probabilità e statistica (continua)**

- Per molti problemi vorremo che i nostri modelli producano una **distribuzione di probabilità** sui possibili esiti.
- Prendiamo un semplice problema di classificazione: data un'immagine in input, stimare quale cifra è raffigurata.

	![[Pasted image 20250923145034.png]]
	=> somma delle probabilità dovrebbe dare 1...

	7
---
**Probabilità e statistica**

- Per altri problemi potremmo voler *qualificare* gli output del modello.
- Questo è il caso in molti problemi di regressione dove gli output in alcuni punti potrebbero essere **più certi** di altri. => in questi casi ho informazioni locali

	![[Pasted image 20250923145127.png]]
	=> dove area più ristretta vorrei più confidenza perchè magari ho più dati di input e viceversa meno confidenza (area più larga) per meno dati

	8
---
**Calcolo e ottimizzazione**

- Molti (beh, la maggior parte) problemi di apprendimento sono formulati come problemi di **ottimizzazione** in (potenzialmente moltissime) variabili multiple.
- Ciò significa che apprendere significa stimare questi problemi **minimizzando una qualche funzione obiettivo**. => funzione di *discesa* del gradiente => problema di local/global minimum oppure di divergenza

	![[Pasted image 20250923145225.png]]

	9
---
## Preliminari Matematici: Algebra Lineare

---
**Vettori e spazi vettoriali**

- Vettori e spazi vettoriali sono fondamentali per l'algebra lineare.
- I vettori descrivono linee, piani e iperpiani nello spazio.
- Ci permettono di eseguire calcoli che esplorano relazioni in spazi multi-dimensionali.
- Nella sua forma più semplice, un vettore è un oggetto matematico che ha sia **magnitudine** che **direzione**.
- Scriviamo i vettori usando una varietà di notazioni, ma di solito li scriveremo così:
$$v = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

- Il simbolo in grassetto ci fa sapere che è un **vettore**.

	10
---
**Vettori e spazi vettoriali (continua)**

- Cosa significa avere *direzione* e *magnitudine*?
- Beh, aiuta guardare una visualizzazione (in al massimo tre dimensioni):

	![[Pasted image 20250923150215.png]]
	
	11
---
**Vettori e spazi vettoriali (continua)**

- Più formalmente, diciamo che **v** è un vettore in $n$ dimensioni (o piuttosto, **v** è un vettore nello spazio vettoriale $\mathbb{R}^n$) se: $$v = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n
\end{bmatrix}$$
- per $v_i \in \mathbb{R}$. Nota che usiamo simboli regolari (cioè non in grassetto) per riferirci ai singoli elementi di **v**.

	12
---
**Operazioni sui vettori**

- **Definizione (Operazioni vettoriali fondamentali)**
	- **Addizione vettoriale**: se **u** e **v** sono vettori in $\mathbb{R}^n$, allora anche $w = u + v$ lo è (dove definiamo $w_i = u_i + v_i$).
	- **Moltiplicazione per scalare**: se **v** è un vettore in $\mathbb{R}^n$, allora anche **w** = c**v** lo è per qualsiasi $c \in \mathbb{R}$ (definiamo $w_i = cv_i$). => "scalare perché scalano il vettore"
	- **Prodotto scalare** (punto): se **u**  e **v** sono vettori in $\mathbb{R}^n$ , definiamo il prodotto scalare o punto come: $$u \cdot v = \sum_{i=1}^{n} u_i v_i$$
	- **Norma vettoriale** (o magnitudine, o lunghezza): se **v** è un vettore in $\mathbb{R}^n$, allora definiamo la norma o lunghezza di **v** come:$$\|u\| = \sqrt{u \cdot u}$$ (norma euclidea di default)
	13
---
**Visualizzare i vettori (in 2D)**

- L'addizione vettoriale è facile da interpretare in 2D:

	![[Pasted image 20250923152032.png]]

	14
---
**Visualizzare il prodotto scalare**

- Il prodotto scalare o punto è correlato alle direzioni e alle magnitudini dei due vettori:

	![[Pasted image 20250923152116.png]]
	=> proietto un vettore sull'altro... => uso la direzione di **b** per misurare **a**
	
- Infatti, è facile ricavare il coseno tra due vettori qualsiasi.
- Nota che queste proprietà si generalizzano a **qualsiasi numero di dimensioni**.

- Domanda: come possiamo testare se due vettori sono perpendicolari (ortogonali)? => prodotto scalare nullo!

	15
---
**Formalizzare l'intuizione** (skippata)

- **Definizione** (Mappa Bilineare)
	Una funzione $\Omega : V \times V \to \mathbb{R}$ è una mappa bilineare dallo spazio vettoriale $V$ a $\mathbb{R}$ se e solo se:$$\Omega(\lambda x + \psi y, z) = \lambda \Omega(x, z) + \psi \Omega(y, z)$$ $$\Omega(x, \lambda y + \psi z) = \lambda \Omega(x, y) + \psi \Omega(x, z)$$	per qualsiasi $x, y, z \in V$.

- $\Omega$ è chiamata **simmetrica** se $\Omega(x, y) = \Omega(y, x)$ per tutti $x, y \in V$.
- $\Omega$ è chiamata definita positiva se:$$\Omega(x, x) \geq 0 \space \forall \space x, \text{ e } \Omega(x, x) = 0 \text{ sse } x = 0$$
	16
---
**Formalizzare l'intuizione**

**Definizione (Prodotto Interno e Spazio con Prodotto Interno)**

- Sia **V** un qualsiasi spazio vettoriale e $\Omega : V \times V \to \mathbb{R}$ una qualsiasi mappa *bilineare* da **V** a $\mathbb{R}$. Allora:
	- Se $\Omega$ è simmetrica e definita positiva, $\Omega$ è chiamata un *prodotto interno* su **V**. Di solito scriviamo $\langle x,y\rangle$ invece di $\Omega(x,y)$.
	- La coppia $(V,\Omega)$ (o $(V,\langle\cdot,\cdot\rangle)$ ) per prodotto interno $\Omega$ è chiamata **spazio con prodotto interno** o *spazio vettoriale con prodotto interno*. Se: $$\Omega(x,y) = x^Ty \space ,  (V,\Omega)$$ è chiamato **spazio vettoriale euclideo**.

- I prodotti interni ci permettono di formalizzare le nostre intuizioni geometriche su lunghezza, ortogonalità e distanza.

	17
---
**Proiezioni ortogonali**


//Inserire sketch se lo fa

	18
--- 
**Matrici: basi**

- Una matrice dispone i numeri in righe e colonne, così:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$

- Nota che le matrici sono generalmente nominate con una **lettera maiuscola** in grassetto. Ci riferiamo agli elementi della matrice usando l'equivalente minuscolo con un pedice indicatore di riga e colonna: $$A = \begin{bmatrix}
a_{1,1} & a_{1,2} & a_{1,3} \\
a_{2,1} & a_{2,2} & a_{2,3}
\end{bmatrix}$$
- Qui diciamo che **A** è una matrice di dimensione $2 \times 3$.
- Equivalentemente: $A \in \mathbb{R}^{2 \times 3}$.

	19
----
**Matrici: operazioni aritmetiche**

- Le matrici supportano operazioni aritmetiche comuni:
  - Per sommare due matrici della stessa dimensione, basta sommare gli elementi corrispondenti in ogni matrice:$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} + \begin{bmatrix} 6 & 5 & 4 \\ 3 & 2 & 1 \end{bmatrix} = \begin{bmatrix} 7 & 7 & 7 \\ 7 & 7 & 7 \end{bmatrix}$$
- Ogni matrice ha due righe di tre colonne (quindi le descriviamo come matrici $2 \times 3$).
- Sommare matrici **A** + **B**  risulta in una nuova matrice **C** dove $c_{i,j} = a_{i,j} + b_{i,j}$.
- Questa definizione elemento per elemento si generalizza a sottrazione, moltiplicazione e divisione.

	20
---
**Matrici: operazioni aritmetiche (continua)**

- Negli esempi precedenti, siamo stati in grado di aggiungere e sottrarre le matrici, perché gli operandi (le matrici su cui operiamo) sono conformi per l'operazione specifica (in questo caso, addizione o sottrazione).
- Per essere conformi per addizione e sottrazione, gli operandi devono avere lo stesso numero di righe e colonne
- Ci sono diversi requisiti di *conformabilità* per altre operazioni, come la moltiplicazione di matrici.

	21
---
**Matrici: operazioni aritmetiche unarie**

- La negazione di una matrice è solo una matrice con il segno di ogni elemento invertito:$$C = \begin{bmatrix} -5 & -3 & -1 \\ 1 & 3 & 5 \end{bmatrix}$$ $$-C = \begin{bmatrix} 5 & 3 & 1 \\ -1 & -3 & -5 \end{bmatrix}$$
- La trasposta di una matrice scambia l'orientamento delle sue righe e colonne.
- Lo indichi con un apice **T**, così: $$\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}^T = \begin{bmatrix}1 & 4 \\2 & 5 \\3 & 6\end{bmatrix}$$
	22
---
**Matrici: moltiplicazione di matrici**

- Moltiplicare le matrici è un po' più complesso dell'aritmetica elemento per elemento vista finora.
- Ci sono due casi da considerare, la moltiplicazione per scalare (moltiplicare una matrice per un singolo numero)$$2 \times \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 6 \\ 8 & 10 & 12 \end{bmatrix}$$
- E la moltiplicazione di matrici per prodotto scalare: $$\text{AB} = \text{C}, \quad \text{dove } c_{i,j} = \sum_{k=1}^{n} a_{i,k} b_{k,j}$$
- Cosa possiamo inferire sulle dimensioni conformi di A e B? Qual è la dimensione di C. => per essere conforme l'altezza delle matrici deve essere la stessa => stesso k

	23
---
**Matrici: la moltiplicazione è solo prodotti scalari**

- Per moltiplicare due matrici, stiamo in realtà calcolando il prodotto scalare di righe e colonne.
- Eseguiamo questa operazione applicando la regola RC - moltiplicando sempre (facendo il punto) Righe per Colonne.
- Perché funzioni, il numero di colonne nella prima matrice deve essere lo stesso del numero di righe nella seconda matrice in modo che le matrici siano conformi.
- Un esempio:$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \cdot
\begin{bmatrix} 9 & 8 \\ 7 & 6 \\ 5 & 4 \end{bmatrix} = \begin{bmatrix} 7 & 7 \\ 7 & 7 \end{bmatrix}$$
	=>  Faccio prodotto scalare fra vettori!
	
	24
---
**Matrici: inverse**

- La matrice identità **I**  è una matrice quadrata con tutti uno sulla diagonale e zero ovunque.
- Quindi, **IA** = **AI**, e **Iv** = **v**.
- L'inversa di una matrice quadrata **A** è denotata $A^{-1}$.
- $A^{-1}$ è l'unica (se esiste) matrice tale che:$$A^{-1}A = AA^{-1} = I$$
	25
---
**Matrici: risolvere sistemi di equazioni**

- Possiamo ora usarlo a nostro vantaggio: $$\begin{bmatrix} 67.9 & 1.0 \\ 67.9 & 1.0 \end{bmatrix} \begin{bmatrix} m \\ b \end{bmatrix} = \begin{bmatrix} 170.85 \\ 122.50 \end{bmatrix} $$
-  Moltiplicando entrambi i lati per l'inversa: $$\begin{bmatrix} 67.9 & 1.0 \\ 67.9 & 1.0 \end{bmatrix}^{-1} \begin{bmatrix} 67.9 & 1.0 \\ 67.9 & 1.0 \end{bmatrix} \begin{bmatrix} m \\ b \end{bmatrix} = \begin{bmatrix} 67.9 & 1.0 \\ 67.9 & 1.0 \end{bmatrix}^{-1} \begin{bmatrix} 170.85 \\ 122.50 \end{bmatrix} $$
- E abbiamo: $$I \begin{bmatrix} m \\ b \end{bmatrix} = \begin{bmatrix} 67.9 & 1.0 \\ 67.9 & 1.0 \end{bmatrix}^{-1} \begin{bmatrix} 170.85 \\ 122.50 \end{bmatrix} $$
	26
---
**Matrici: lineare versus affine**

- La moltiplicazione di matrici calcola **trasformazioni lineari** di spazi vettoriali.
- Siamo anche interessati a trasformazioni affini che non preservano necessariamente l'origine:

- Una trasformazione affine è una trasformazione **lineare** seguita da una traslazione: $$f(x) = Ax + b$$
- Nota: una trasformazione affine in **n** dimensioni può essere modellata da una trasformazione lineare in **n + 1** dimensioni.  => utile anche per le trasformazioni lineari!

	27
---
**Tensori: Una struttura generale per dati densi**

- Non c'è niente di magico in una dimensione (vettori) o due dimensioni (matrici).
- In effetti, gli strumenti che usiamo sono completamente generici in quanto possiamo definire array densi e omogenei di dati numerici di qualsiasi dimensionalità.
- Il termine generico per questo è tensore, e tutta la matematica si generalizza a dimensioni arbitrarie.

- Esempio: un'immagine a colori è naturalmente modellata come un tensore in tre dimensioni (due spaziali, una cromatica).
 
- Esempio: un batch di b immagini a colori di dimensione $32 \times 32$ è facilmente modellato semplicemente aggiungendo una nuova dimensione:  **B** $\in \mathbb{R}^{b \times 32 \times 32 \times 3}$.

	28
---
## Preliminari Matematici: Probabilità e Statistica

--- 
**Teoria della probabilità: un esempio motivante**

Consideriamo il classico esempio dell'Urna:

- Abbiamo due urne (rossa e blu) i cui contenuti esatti sono sconosciuti, ma che contengono pezzi di frutta (mele e arance).
- Si estrae un pezzo di frutta da un'urna scelta a caso, diciamo con probabilità 0.4 e 0.6.

	![[Pasted image 20250925113459.png]]

	29
---
**Teoria della probabilità: un esempio motivante**

Consideriamo il classico esempio dell'Urna (scatola):

- In questo caso abbiamo una variabile casuale **B** (box) definita dalla sua distribuzione:
  $p(B = \text{blu}) = 0.6 \, \text{e} \, p(B = \text{rosso}) = 0.4$

- Abbiamo anche una variabile casuale **F** (frutta) che dipende da **B** – dipendente perché la sua distribuzione dipende dalla scatola scelta.
	
	![[Pasted image 20250925113459.png]]
	
	30
---
**Teoria della probabilità: un esempio motivante**

Consideriamo il classico esempio dell'Urna (scatola):

- Qual è la probabilità complessiva di scegliere una mela? (cioè $p(F = \text{mela})$ – una probabilità che chiaramente dipende anche da $p(B)$).
- Se la frutta scelta è un'arancia, qual è la probabilità che provenga dalla scatola blu (cioè $p(B = \text{blu} | F = \text{arancia})$)
	
	![[Pasted image 20250925113459.png]]

	31
---
**Teoria della probabilità: un esempio motivante**

La distribuzione congiunta di due variabili casuali:

- La chiave per analizzare tali domande è la distribuzione di probabilità congiunta di tutte le variabili coinvolte.
- Deriveremo le regole della somma e del prodotto della teoria della probabilità (che sono probabilmente più vicine alle \( F = ma \) e \( V = IR \) del ML).

	32
---
**Il caso generale**

Consideriamo il caso generale:

- Come stimiamo la distribuzione congiunta delle variabili casuali  **X** e **Y** (senza alcuna conoscenza a priori)?
- Preleviamo un campione:  $\{(x_i, y_i) \mid i = 1, 2, \ldots N\}$  estratto indipendentemente dalla distribuzione congiunta \( p(X, Y) \) e facciamo un istogramma.

	![[Pasted image 20250925114033.png]]

	33
---
**Il caso generale**

- Consideriamo il caso generale:
	- Definiamo $n_{ij}$ come il numero di campioni che cadono nella cella (i, j) – cioè la cella corrispondente a $(x_i, y_j)$ – dell'istogramma.
	- Inoltre: ci sarà il numero totale di volte che **X** assume il valore $x_i$ e $r_j$ il numero totale di volte che **Y** assume il valore $y_j$

	![[Pasted image 20250925114033.png]]
	
	34
---
**Il caso generale**

Questo istogramma cattura (beh, stima) tutto ciò di cui abbiamo bisogno:

- La probabilità *congiunta* **p(X, Y)** è: $$p(X = x_i, Y = y_j) = \frac{n_{ij}}{N}$$

- La probabilità *marginale* di **X** che assume valore $x_i$ è: $$p(X = x_i) = \frac{c_i}{N} = \sum_j p(X = x_i, Y = x_j)$$
	35
---
**Il caso generale**

Ora, vediamo come **condizionare** le probabilità:

- Guarda solo quegli eventi congiunti per cui $X = x_i$.
- Scriviamo la frazione di tali eventi per cui  $Y = y_j$ come: $$p(Y = y_j | X = x_i) = \frac{n_{ij}}{c_i}$$
- Possiamo derivarlo dalla probabilità congiunta:$$p(X = x_i, Y = y_j) = \frac{n_{ij}}{N} = \frac{n_{ij}}{c_i} \cdot \frac{c_i}{N} = p(Y = y_j | X = x_i) p(X = x_i)$$
	![[Pasted image 20250925114033.png]]

	36
---
**Teoria della Probabilità per l'Apprendimento Automatico**

- Invocheremo frequentemente le due regole della probabilità:
	- regola della **somma**: $$p(X) = \sum_{Y} p(X, Y)$$
	- regola del **prodotto**:  $$p(X, Y) = p(Y | X)p(X)$$

- E useremo frequentemente la regola di *Bayes*: $$p(Y | X) = \frac{p(X | Y)p(Y)}{p(X)}$$

- Questo assume un significato speciale quando applicato all'*inferenza parametrica*:  $$p(\mathbf{w} | \mathcal{D}) = \frac{p(\mathcal{D} | \mathbf{w})p(\mathbf{w})}{p(\mathcal{D})}$$$$\text{posterior} \propto \text{verosimiglianza dei dati (likelihood)} \times \text{prior}$$
	37
---
**Teoria della Probabilità per l'Apprendimento Automatico**

- Un'operazione importante usando le probabilità è trovare **medie pesate** di funzioni:$$  \mathbb{E}[f] = \sum_{x} p(x) f(x) \quad (\text{o} \int p(x) f(x) dx)$$
- In entrambi i casi, se abbiamo un campione finito di **N** punti dalla distribuzione **p(x)** possiamo approssimare l'*aspettativa*:$$\mathbb{E}[f] \approx \sum_{i} p(x_i) f(x_i)$$
- La **distribuzione Gaussiana** sarà nostra amica, quindi le *covarianze* sono importanti:$$  \text{cov}(x,x) = \mathbb{E}_x \{ [x - \mathbb{E}[x]] \} \{ x^T - \mathbb{E}[x^T] \} \\
    = \mathbb{E}_x [xx^T] - \mathbb{E}[x] \mathbb{E}[x^T]$$
	38
---
**La distribuzione Gaussiana (a proposito di covarianza)**

- La distribuzione Gaussiana *univariata* è super importante:$$\mathcal{N}(x | \mu, \sigma) = \frac{1}{(2\pi\sigma^2)^{1/2}} \exp\{-\frac{1}{2\sigma^2}(x - \mu)^2\}$$=> al limite aumentando la $\sigma$ si passa alla distribuzione uniforme

- Così come la distribuzione Gaussiana *multivariata*, che useremo estesamente:$$\mathcal{N}(x | \mu, \Sigma) = \frac{1}{(2\pi)^{D/2}} \frac{1}{|\Sigma|^{1/2}} \exp\{-\frac{1}{2}(x - \mu)^T\Sigma^{-1}(x - \mu)\}$$ => forma quadratica ma su più dimensioni

- Qui $\mu$ è un vettore $D$ dimensionale (**la media**) e $\Sigma$ è la *matrice di covarianza* $D \times D$. => di solito simmetrica (diagonale) e positiva => allineati agli assi x e y => altrimenti per trovare le direzioni si trovano tramite autovettori

	39
---
**Teoria decisionale e classificazione supervisionata** (skipped da qui in poi)

- Proviamo ad espandere la nostra crescente intuizione per includere problemi di classificazione.
- La teoria della probabilità ci dà un modo principiato per rappresentare e quantificare l'incertezza, quindi usiamola!

- Supponiamo di avere un input **x** insieme a un vettore **y** di variabili target.
- Per problemi di regressione, **y** saranno variabili continue, mentre per problemi di classificazione rappresenterà etichette di classe.

- La distribuzione congiunta **p(x, y)** ci dà un quadro completo dell'incertezza associata a queste variabili.

	40
---
**Teoria decisionale e classificazione supervisionata**

- Come esempio, supponiamo che **x** sia una radiografia a 512 × 512 pixel di un paziente e vogliamo decidere se il paziente ha il cancro: $$f(x) = \begin{cases}  0 & \text{se il paziente ha il cancro} \\ 1 & \text{altrimenti} \end{cases}$$- Come potrebbe apparire il nostro **dataset**? Beh, probabilmente un insieme di coppie: $$\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N)\}$$
- Dobbiamo prima affrontare il problema dell'*inferenza*: determinare la distribuzione congiunta $p(x, y)$  (di solito estremamente difficile).
- Poi dobbiamo decidere come agire in modo ottimale per un specifico p(**x'**, y) (spesso molto facile).

	41
---
**Teoria decisionale e classificazione supervisionata**

- Quindi, quando otteniamo un'immagine **x**, il nostro obiettivo è decidere a quale delle due classi appartiene.
- Possiamo derivare informazioni su questa decisione dalla distribuzione *posterior*:
$$p(C_k | x) = \frac{p(x | C_k) p(C_k)}{p(x)} \\
= \frac{\text{verosimiglianza dei dati } \text{x} \text{ prior}}{\text{evidenza}}$$

- Ma, la domanda saliente rimane: **come decidiamo?**

	42
---
**Teoria decisionale e classificazione supervisionata**

La decisione ottimale *teorica*:

- Minimizzare il tasso di *classificazione errata* atteso.
$$p(\text{errata class.}) = p(x \in \mathcal{R}_1, C_2) + p(x \in \mathcal{R}_2, C_1)$$
$$= \int_{\mathcal{R}_1} p(x, C_2) dx + \int_{\mathcal{R}_2} p(x, C_1) dx$$
	![[Pasted image 20250925231256.png]]
	
	43
---
**Teoria decisionale e classificazione supervisionata**

- **Opzione 1**: stimare le densità condizionate di classe $p(x|C_k)$ individualmente, insieme alle probabilità a priori $p(C_k)$, poi usare il teorema di Bayes per calcolare la *posterior*.
$$p(C_k|x) = \frac{p(x|C_k)p(C_k)}{p(x)}$$

- Opzione 2: **stimare** direttamente le probabilità posterior.

- Opzione 3: saltare tutto il mumbo jumbo bayesiano e stimare direttamente una *funzione discriminante*.
	
	44
---
**Teoria decisionale e classificazione supervisionata**

- Ci sono ragioni pratiche per scegliere un approccio:
	![[Pasted image 20250925231937.png]]

	45
---
**La Maledizione della Dimensionalità**

- Considera un problema di classificazione a 3 classi con misere due dimensioni di input:
	=> nearest neighbour classification (?)
	
	![[Pasted image 20250925232135.png]]
	
	46
---
**La Maledizione della Dimensionalità**

- Man mano che aggiungiamo dimensioni di input, il numero di "bins" in qualsiasi discretizzazione dello spazio cresce esponenzialmente. =>  ma quello dei dati non cresce allo stesso modo! => rischio di un sacco di bins vuoti!

- La morale: arricchire l'input (aggiungendo dimensioni) ==non rende il nostro problema più facile==.

	![[Pasted image 20250925232256.png]]

	47
---
## Allineamento Notazionale e La Strada da Percorrere

---
**Allineamento Notazionale**

- I vettori saranno denotati in carattere minuscolo, romano, grassetto: **x**.
- Tutti i vettori sono assunti essere vettori colonna.
- Lettere maiuscole, grassetto romano denotano matrici: **M**.
- La trasposta di vettori e matrici è indicata dall'apice **T**: $x^T, M^T$.
- La notazione $(w_1, \ldots, w_n)$ denota un vettore riga di *n* dimensioni.
- Il corrispondente vettore colonna è scritto come $w = (w_1, \ldots, w_n)^T$.
- Il valore atteso di $f(x, y)$ rispetto a una v.c. **x** è scritta come $\mathbb{E}_x[f(x, y)]$.
- Se **x** è condizionata su z, il valore atteso condizionato è $\mathbb{E}_x[f(x) | z]$
- La *varianza* di f(x) \) è denotata da $var[f(x)]$, e la *covarianza* come $cov[x, y]$.

	48
---
**La strada da percorrere**

- In questa lezione abbiamo visto una breve panoramica di alto livello di alcuni dei concetti base di algebra lineare e teoria della probabilità.
- Questa è solo teoria sufficiente per farci iniziare il nostro viaggio nell'Apprendimento Automatico.
- Introdurremo, secondo necessità, concetti più avanzati man mano che procediamo (es. ottimizzazione basata su gradiente, proprietà speciali della densità Gaussiana, spazi di Hilbert, ecc.).
- Prossimamente:
  - Ci tufferemo in uno studio di modelli lineari per la regressione.
  - Vedremo come modellare previsioni di output continui usando funzioni lineari dell'input.
  - Vedremo come adattare questi modelli, come proiezioni di base non lineari possono arricchirli e come quantificare la fiducia nelle loro previsioni.

	49
---
## Compiti a Casa e Letture

---
**Compiti a Casa e Letture**

- **Lettura Assegnata:**
	- Bishop: Capitoli 1 e 2 (1.5, 2.3)

**Compiti a Casa:**
1. Una mappa lineare \(\pi : V \to U\) da uno spazio vettoriale \(V\) a uno spazio vettoriale \(U\) è chiamata proiezione se \(\pi \circ \pi = \pi\) (cioè \(\pi\) è idempotente). Dimostra che la proiezione ortogonale da \(V\) su un sottospazio \(U\) è effettivamente una proiezione.

2. Mostra che la moda di una distribuzione Gaussiana \(\mathcal{N}(\mu, \sigma)\) è data da \(\mu\).

	50
---

#Ecco la traduzione del file `03-LinearModelsRegression.pdf` con le formule racchiuse tra `$` come richiesto per Obsidian:

---

[file name]: 03-LinearModelsRegression.pdf
[file content begin]
===== Pagina 1 =====

**Fondamenti di Apprendimento Automatico:**

**Regressione Lineare, dalla Geometria alla Massima Verosimiglianza**

Prof. Andrew D. Bagdanov (andrew.bagdanov AT unifi.it)

**UNIVERSITÀ**
**DEGLI STUDI**
**FIRENZE**

**DINFO**

**DIPARTIMENTO DI**
**INGEGNERIA**

===== Pagina 2 =====

# 3 - Regressione Lineare dalla geometria alla massima verosimiglianza
---
## Introduzione

---
**Obiettivi della lezione**

Alla fine di questa lezione avrete:

- Compreso l'approccio **geometrico** ai problemi di regressione lineare come applicazione dell'adattamento di curve.
- Compreso la formulazione probabilistica della regressione lineare e saprete come viene derivata la Stima di Massima Verosimiglianza dei parametri del modello.
- Riconosciuto quando avviene underfitting e overfitting dei modelli.
- Compreso come la **regolarizzazione** può essere usata per limitare dolcemente la capacità dei nostri modelli e mitigare l'overfitting.

	2
---
**Motivazioni**

- Tenete a mente mentre lavoriamo attraverso la lezione di oggi che ci stiamo dirigendo verso un modello probabilistico.
- Inizieremo, tuttavia, con un modello geometrico semplice su cui baseremo le nostre intuizioni.
- Interessante, continueremo a tornare su questo modello "semplice" e verificheremo che le nostre intuizioni sono solide anche da una prospettiva probabilistica.

	3
---
## Regressione Lineare come Adattamento di Curve Geometrico

---
**Regressione Lineare dalle basi**

- Iniziamo il nostro studio dei modelli lineari per la regressione da una prospettiva **geometrica**, dalle basi => in base ai dati che abbiamo
- Definiremo il problema di apprendimento come uno di trovare ==i parametri ottimali== $w$ di uno spazio di ipotesi parametrizzato $\mathcal{H}$.
- Ottimale sarà determinare (per ora) in termini di un  semplice errore geometrico semplice su un campione finito di osservazioni.
	
	4
---
**Uno spazio di ipotesi parametrico, lineare**

- Considera prima la classe dei problemi di regressione univariata (un unico target per un singolo input) dove osserviamo coppie di osservazioni $(x_i, t_i)$, dove:
  - $x_i \in \mathbb{R}$ sono osservazioni della variabile **indipendente**.
  - $t_i \in \mathbb{R}$ sono osservazioni della variabile **dipendente**. => t per variabile target

- Assumiamo che la variabile dipendente sia relazionata alla variabile indipendente tramite una funzione $f$ che è sconosciuta **ma lineare** nei suoi parametri $\mathbf{w}$:$$y(x | \mathbf{w}) = w_0 + w_1 x$$$$= \mathbf{w}^T \begin{bmatrix} 1 \\ x \end{bmatrix}$$
	=> posso rappresentare dunque qualsiasi funzione lineare => ovvero qualsiasi retta!
	
	5
---
**Quantificare la bontà di una soluzione**

- OK, abbiamo alcuni dati (cioè osservazioni della variabile indipendente e dipendente).
- E abbiamo uno **spazio di ipotesi** convenientemente parametrizzato da **w**.
- Per apprendere effettivamente qualcosa (cioè adattare il modello ai dati) abbiamo poi bisogno di una qualche sorta di *perdita* $\mathcal{L}$.
- Questa perdita dovrebbe misurare la *cattiveria* di un'ipotesi arbitraria $w'$ – cioè, **alta perdita** indica un cattivo adattamento e bassa perdita uno buono.
- Sarà una funzione dei parametri candidati e dei dati osservati  $D = \{(x_i, t_i) \mid i = 1, \ldots N\};$ $$E(w \mid D) = \frac{1}{2} \sum_{i=1}^{N} [y(x_i|w) - t_i]^2$$	=> provo a calcolare la somma degli errori quadrati => come distanza dei nostri punti dalla retta => metti sketch 
	=> primo esempio di Loss => in regressione si parla di *error function* => come mai il quadrato? beh vorrei solo valori positivi ma anche una funzione semplice da derivare => per il problema di minimizzazione => trovare il $w$ che minimizza la funzione
	
	6
---
**Regressione Lineare: una Critica della Ragione Pura**

- Esamineremo più in dettaglio questa scelta di **perdita**.
- Ma, per ora consideriamo le proprietà, buone e cattive, di questa formulazione. $$E(w | D) = \sum_{i=1}^{N} [(w_0 + w_i x_i) - t_i]^2$$ $$\nabla_w \ E(w | D) =\frac{1}{2} \sum_{i=1}^{N} \nabla_w \ [(w_0 + w_i x_i) - t_i]^2$$ => per la linearità della derivazione
 $$= \sum_{i=1}^{N}[(w_0 + w_i x_i) - t_i] \ \nabla_w \ [(w_0 + w_i x_i) - t_i]$$
$$= \sum_{i=1}^{N}e_i[1 \ x_i]^T$$ => avendo sostituito la prima parte con la funzione di errore

=> $w_{t+1} = w_t - \eta \nabla E(w_t | D)$ => metodo di discesa del gradiente => $\eta$ controlla quanto ci muoviamo in direzione dell'antigradiente => *learning rate* => difficile da parametrizzare! 

	7
---
## Regressione Lineare e Stima di Massima Verosimiglianza

---
**Stima di Massima Verosimiglianza (MLE) e Minimi Quadrati**

- La nostra interpretazione geometrica è un esempio di stima puntuale dei parametri del modello: ci dà una soluzione $w^*$ che è un **singolo punto** nello spazio dei parametri.

- Vorremmo spostarci verso un modello probabilistico di regressione lineare.
- Questo dovrebbe, idealmente:
  - Permetterci di ragionare probabilisticamente sulla qualità della nostra soluzione.
  - Permetterci di **quantificare la fiducia** nella qualità delle singole previsioni.
  - Permetterci di "infornare" **conoscenza a priori** su soluzioni probabili. 

- Il nostro primo passo è la Stima di Massima Verosimiglianza (MLE) dei parametri ottimali $w$ dati i dati osservati $D$. => stavolta vogliamo stimare la massima verosimiglianza per i dati generati
- Primo, **irrobustiamo** un po' il nostro modello per permettere funzioni polinomiali dell'input.

	8
---
**Modelli lineari con funzioni di base**

- Il modello lineare più semplice per la regressione usa solo combinazioni lineari delle variabili di input $x = (x_1, \ldots, x_D)^T$:$$y(x | w) = w_0 + w_1 x_1 + \ldots + w_D x_D$$ $$= \mathbf{w}^T \begin{bmatrix} 1 \\ x_1 \\ ... \\ x_D  \end{bmatrix}$$
 => si passa a punti in $D$ dimensioni => dopo due si parla di iperpiano che divide i nostri punti

- Questa è una **funzione lineare** sia in $w$ (buono => permette di derivare e riottenere la nostra funzione di error di partenza!) che in $x$ (molto limitante!).

- Quindi, possiamo permettere combinazioni lineari di funzioni **non lineari** fisse dell'input:$$y(x | w) = w_0 + \sum_{j=1}^{M-1} w_j \phi_j(x)$$
	=> Aggiungo *funzioni base* (che producono un singolo scalare) come $\phi_0 (x) = 1$, $\phi_1(x) = x$ ... faccio il "basis mapping" $$ \phi(x) = \begin{bmatrix} \phi_0(x) \\ \phi_1(x) \\ ... \end{bmatrix}$$	$$y(x| \mathbf{w},D)= \mathbf{w}^T \mathbf{\phi(x)}$$
	9
---
**Modelli lineari con funzioni di base**

- $w_0$ è conosciuto come parametro di bias e permette per qualsiasi offset fisso nell'output.
- È spesso conveniente definire una funzione di base fittizia $\phi_0(x) = 1$ così possiamo scrivere in modo compatto:$$y(x | w) = \sum_{j=0}^{M-1} w_j \phi_j(x)= w^T \phi(x)$$

- Dove $w = (w_0, \ldots, w_{M-1})^T$ e $\phi = (\phi_0, \ldots, \phi_{M-1})^T$
- Funzioni di base comuni: $$\phi_i(x) = x^i \quad \phi_i = \exp\{-\frac{(x - \mu_i)^2}{2s^2}\} \quad \phi_i(x) = \tanh(x)$$
				Polinomiale                 Gaussiana                       Sigmoide
	=> con la gaussiana possiamo tipo prendere diverse medie e vedere a quale si avvicina di più (inserire sketch) => mapping di uno scalare ad un vettore di 3 valori => quanti sceglierne (scelta sull'M) ? boh si vedrà dopo con crossvalidation

	10
---
**Massima verosimiglianza e minimi quadrati**

- Pulito, ma dove sono le nostre *probabilità* in tutto questo?!
- Torniamo alla nostra assunzione originale che la nostra variabile *target* è la realizzazione di una funzione *deterministica* $y(x| w)$ con rumore gaussiano additivo:$$t = y(x | w) + \epsilon$$
- Dove $\epsilon$ è una variabile casuale gaussiana **a media zero**, con **precisione** $\beta$. => precisione che nella gaussiana è inversamente proporzionale alla varianza $\sigma$ => $\beta \prop \frac{1}{\sigma^2}$

- Così, possiamo scrivere:$$p(t | x, w, \beta) = \mathcal{N}(t | y(x | w), \beta^{-1})$$
- Ottimo! Una distribuzione di probabilità! Ora apprendiamo qualcosa dai dati...

	11
---
**Massima verosimiglianza e minimi quadrati**

- Se togli via tutto il "mumbo jumbo" fantasioso, quello che stiamo facendo è piuttosto letterale e intuitivo.
- In qualsiasi punto $x_0$, il nostro predittore **qualifica la sua previsione** piazzando una Gaussiana attorno ad essa. 

	![[Pasted image 20250929221506.png]]

	12
---
**Massima verosimiglianza e minimi quadrati**

- Ora considera un dataset di input $X = \{x_1, \ldots, x_N\}$
- Insieme a valori target corrispondenti $t = (t_1, \ldots, t_N)^T$.
- Assumendo che questi campioni siano tutti identicamente e indipendentemente estratti da $p(t | x, w, \beta)$, possiamo scrivere:$$p(t | X, w, \beta) = \prod_{n=1}^N \mathcal{N}(t_n | y(x_n, w), \beta^{-1})$$ => dati X,w,$\beta$ calcola la probabilità di ottenere i miei punti target secondo la legge delle probabilità indipendenti	$$= \prod_{n=1}^N \mathcal{N}(t_n | w^T \phi(x_n), \beta^{-1})$$=> se ci sono punti molto distanti a probabilità zero => la probabilità si abbassa molto!

- E abbiamo un'espressione di verosimiglianza (molto scomoda) per i nostri dati sotto un modello specifico. => potenzialmente i punti sono parecchi => prodotto incoveniente => rischio di avere problemi di underflow per valori molto prossimi a zero

	13
---
**Massima verosimiglianza e minimi quadrati**

- Per la maggior parte dei problemi di apprendimento supervisionato non siamo interessati a modellare la distribuzione degli input.
- Quindi X apparirà sempre nelle variabili condizionanti e per ora lo ometteremo per sgomberare la notazione.
- Prendere i logaritmi aiuta a semplificare la verosimiglianza (grazie in parte alla forma esponenziale della Gaussiana):$$\ln p(t |X, w, \beta) = \sum_{n=1}^{N} \ln \mathcal{N}(t_n | w^T \phi(x_n), \beta^{-1})$$ => il logaritmo di prodotti diventa una somma di logaritmi => ottengo una gaussiana univariata (riguarda gaussiana) => exponenziale sparisce!
$$= \frac{N}{2} (\ln \beta - \ln(2\pi)) - \frac{\beta}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2$$
	=> prima parte che non dipende dalla scelta del modello => la seconda invece è proprio la nostra funzione di errore che con il meno sarà appunto minimizzata (per trovare il max)

	14
---
**Massima verosimiglianza e minimi quadrati**

- Massimizziamo questa *verosimiglianza* in $w$. Prima il gradiente:$$\nabla \ln p(t | w, \beta) = \beta \sum_{n=1}^{N} [t_n - w^T \phi(x_n)] \phi(x_n)^T$$
- E impostiamolo a **zero**:$$0 = \sum_{n=1}^{N} t_n \phi(x_n)^T - w^T \left( \sum_{n=1}^{N} \phi(x_n) \phi(x_n)^T \right)$$
- Che dopo aver risolto per $w$ ci dà:$$w_{ML} = (\Phi^T \Phi)^{-1} \Phi^T t$$
	15
---
**Massima verosimiglianza e minimi quadrati**

- Questa soluzione $(\Phi^T\Phi)^{-1}\Phi^T$ usa la matrice del disegno:
$$\Phi = \begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1) & \cdots & \phi_{M-1}(x_1)\\
\phi_0(x_2) & \phi_1(x_2) & \cdots & \phi_{M-1}(x_2)\\
\vdots & \vdots & \ddots & \vdots\\
\phi_0(x_N) & \phi_1(x_N) & \cdots & \phi_{M-1}(x_N)
\end{pmatrix}$$
=> **le righe corrispondono ai singoli dati** => una riga per ogni punto nel dataset (x1, x2, ...) => e la funzione base applicata ai punti => transposed e messa in una matrice

- Un modo facile per pensare a $\Phi$:
  - Una riga è la valutazione di tutte le funzioni di base sul corrispondente campione di training (dimensionalità M).
  - Una colonna è la corrispondente funzione di base valutata su tutti i campioni di training (dimensionalità N).
- $\Phi^{\dagger} \equiv (\Phi^T\Phi)^{-1}\Phi^T$ è chiamata Pseudo-Inversa di Moore-Penrose.

	16
---
**Minimi quadrati regolarizzati**

- Quindi, cosa succede se abbiamo dati distribuiti così:

	![[Pasted image 20250929224958.png]]
	
- Quale potrebbe essere una buona base? Possiamo recuperare il nostro approccio di adattamento di curve?
- Risposta breve: Sì! Abbiamo appena visto un esempio di base polinomiale!

	17
---
**Minimi quadrati regolarizzati**

- OK, andiamo in città:

	![[Pasted image 20250929225544.png]]

	18
---
**Minimi quadrati regolarizzati**

- OK, andiamo in città (quadratica):

	![[Pasted image 20250929225838.png]]

	19
---
**Minimi quadrati regolarizzati**

- OK, andiamo in città (cubica):

	![[Pasted image 20250929230401.png]]

---
**Minimi quadrati regolarizzati**

- OK, andiamo davvero in città (**grado 20**):

	![[Pasted image 20250929230446.png]]
	=> Clear signs di overfitting!
	
	21
---
**Minimi quadrati regolarizzati: over- e under-fitting**

- Qual è il **risultato migliore**? Cosa significa migliore qui? => aumentando il grado aumento la likelihood... 
- Vediamo in questi grafici esempi sia di overfitting (quando M è troppo grande) che di underfitting (quando M è troppo piccolo).
- Questi risultati potrebbero sembrare contro intuitivi: dopo tutto, uno spazio di ipotesi polinomiale di **grado 10** contiene anche tutti i polinomi di grado minore.
- Perché i minimi quadrati non trovano la soluzione giusta se impostiamo $M = 100$ (per esempio)?
- La risposta ha a che fare con la capacità del modello e il fatto che il **rumore** nelle nostre osservazioni è facilmente catturato da un modello potente. 

	22
---
**Minimi quadrati regolarizzati**

- Possiamo ottenere qualche intuizione ispezionando la **magnitudine** dei parametri stimati massimizzando la verosimiglianza.

	![[Pasted image 20250929230908.png]]

	=> Voglio capire almeno quando sto overfittando... => al grado 9 ho bisogno di grandi valori per far passare esattamente nei punti => vado fuori scala 
	=> Possiamo pensare di tenere le nostre soluzioni entro un certo range di valori

	23
---
**Minimi quadrati regolarizzati**

- Considereremo obiettivi di regressione di questa forma:  $$E_D(\mathbf{w}) + \lambda E_W(\mathbf{w})$$
- Dove $E_D$ continuerà ad essere il nostro **errore ai minimi quadrati** con funzioni di base $\phi$. => dipendente dal Dataset e i parametri del modello

- Il termine $E_W$ è chiamato *regolarizzatore* dei pesi (o solo regolarizzatore), e uno molto comune è la norma al quadrato dei pesi del modello: $$E_W(\mathbf{w}) = \frac{1}{2} \mathbf{w}^T \mathbf{w} = || \mathbf{x}||_2^2$$ => dipende solo dai parametri (i pesi) => questo esempio è regolarizzatore L2

- Quindi, la funzione di **errore totale da minimizzare** diventa:$$E(\mathbf{w}) = \frac{1}{2} \sum_{n=1}^{N} \{ t_n - \mathbf{w}^T \phi(\mathbf{x_n}) \}^2 + \frac{\lambda}{2} \mathbf{w}^T \mathbf{w}$$=> $\lambda$ serve a scegliere il range di valori da accettare (intensity of the regularizator)=> in questo modo tutti i valori troppo al di fuori del range vengono pagati tanto!

	24
---
**Minimi quadrati regolarizzati**

- Questa funzione di errore regolarizzata: $$E(w) = \frac{1}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2 + \frac{\lambda}{2} w^T w$$
- È ancora una funzione quadratica in $w$, e la $w$ ottimale è:$$w_{ML} = (\lambda I + \Phi^T \Phi)^{-1} \Phi^T t$$ => notare che l'aggiunta della costante aiuta a rendere invertibile la matrice

- La stima di Massima Verosimiglianza del parametro di imprecisione $\beta$ può anche essere derivata massimizzando $p(t | w, \beta)$ rispetto a $\beta$:$$\frac{1}{\beta_{ML}} = \frac{1}{N} \sum_{i=1}^{N} [t_n - w_{ML}^T \phi(x_i)]^2$$

	25
---
**Demo Live!**

- Diamo un'occhiata a come funzionano i minimi quadrati regolarizzati in pratica.
- [FAI PARTIRE LA DEMO ORA]
	=> Aumentare la regolarizzazione può portare ad underfitting...

- Best practice è partire da un modello semplice tenere fissa la regolarizzazione è aumentare fino a quando si trova il modello migliore... anche se la scelta migliore dei parametri deriva dal cross-validation...

	26
---
**Minimi quadrati regolarizzati**

- Un errore regolarizzato più generale è: $$\frac{1}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2 + \frac{\lambda}{2} \sum_{j=1}^{M} |w_j|^q$$
	![[Pasted image 20250929231614.png]]

	=> Per q=1 si parla di "sparse solution"... q=2 => small norm solution
	27
---
**Minimi quadrati regolarizzati**

- Un errore regolarizzato più generale è: $$\frac{1}{2} \sum_{n=1}^{N} [t_n - w^T \phi(x_n)]^2 + \frac{\lambda}{2} \sum_{j=1}^{M} |w_j|^q$$
	![[Pasted image 20250929231658.png]] (da sostuire con sketch)
	=> bisogna trovare quindi il punto migliore sia per $E_D$ che $E_W$:
		=> Nel primo caso lo trovo equidistante a 1
		=> Nel secondo caso si nota che alcuni parametri saranno a zero! => sparse solution!

	28
---
## Osservazioni conclusive

---
**Vecchia Cara Regressione Lineare (tm)**

- Oggi abbiamo dato un'occhiata abbastanza approfondita alla regressione lineare.
- Ricorda che lineare è in qualche modo un *misnomer*: qualsiasi cosa che è lineare nei parametri del modello, è una regressione lineare.
- In effetti, abbiamo visto quanto è flessibile la regressione lineare **con funzioni di base**.
- Quindi possiamo adattare modelli non lineari ai dati usando la pura regressione lineare.
- La soluzione di **Massima Verosimiglianza** ha anche una forma analitica, che è semplicemente extra bella. => si ritorna alla squared error function!
- Con questo modello di adattamento di curve (le spline sono in realtà un'istanza di questo) possiamo adattare molti fenomeni.

	29
---
**La strada da percorrere**

- Gli stimatori puramente geometrici e MLE che abbiamo sviluppato sono esempi di stime puntuali.
- Risultano in un singolo punto nello spazio dei parametri che è una stima ottimale (per qualche appropriata definizione di "ottimale").
- Ma, non possiamo portare tutti i nostri strumenti statistici all'opera e quantificare vari tipi di fiducia.
- Nella prossima lezione svilupperemo una teoria bayesiana della regressione lineare che affronta questo problema.

	30
---
**Letture e Compiti a Casa**

- Lettura Assegnata:
	- **Bishop:** Capitolo 3 (3.1, 3.2, 3.3)

- Compiti a Casa:
	1. Come la scala delle nostre caratteristiche di input influisce sulle formulazioni di regressione lineare che abbiamo visto in questa lezione? Cioè, se la scala delle nostre caratteristiche di input e target è $O(1)$ o $O(\text{1e6})$, fa qualche differenza?

	2. La scala delle nostre caratteristiche di input conta di più (o di meno) se usiamo minimi quadrati regolarizzati?

	3. Perché sarebbe problematico se, quando si usa una base polinomiale di grado $K$ per la regressione, la matrice del disegno $\Phi$ è a rango carente (cioè rango($\Phi$) < $K$)?

	31
---

# 4 - Regressione Lineare Bayesiana

---
## Introduzione

---
**Frequentista versus Bayesiano**

- Nella lezione precedente abbiamo visto come l'interpretazione geometrica dell'errore del modello può essere usata per derivare un regressore lineare intuitivo.
- Abbiamo anche visto come "irrobustire" la nostra rappresentazione usando un embedding esplicito degli input in uno spazio non lineare.
- Abbiamo poi aggiunto una patina probabilistica al nostro modello per derivare una Stima di Massima Verosimiglianza dei parametri del modello "migliori".
- Questo modello di inferenza frequentista ha molti vantaggi e svantaggi.
- Oggi deriveremo un'interpretazione bayesiana completa dell'inferenza e guarderemo ai suoi vantaggi.
- Prima, diamo un'occhiata a uno strumento concettuale importante per comprendere la relazione tra bias e varianza nei modelli.

	2
---
**Obiettivi della lezione**

Alla fine di questa lezione avrete:

- Compreso la relazione tra bias e varianza nei modelli.
- Compreso il tradeoff tra bias e varianza.
- Riconosciuto la differenza tra stime puntuali come Massima Verosimiglianza e il trattamento bayesiano completo della regressione lineare.
- Compreso come l'inferenza bayesiana ci permette di incorporare (richiede, in realtà) informazione a priori sui parametri del modello.
- Compreso come l'inferenza bayesiana ci permette sia di quantificare che di aggiornare la nostra fiducia nelle previsioni del modello.

	3
---
## La Scomposizione Bias-Varianza

---
**Regolarizzazione. A cosa serve?**

- Questa discussione sulla regolarizzazione delle soluzioni ai problemi dei minimi quadrati ci porta naturalmente a uno strumento concettuale importante nell'Apprendimento Automatico.
- Fino ad ora abbiamo, in qualche modo implicitamente, assunto che le funzioni di base siano in qualche modo fisse nella forma e nel numero.
- Abbiamo già visto accenni del problema dell'overfitting: se usiamo un modello che è in qualche modo troppo complesso, possiamo abbattere l'errore di training quanto vogliamo.
- La regolarizzazione può controllare la complessità, ma questo lascia ancora molte domande:
  - Cosa dovrebbe essere $\lambda$?
  - Quale dovrebbe essere il mio modello base (prima della regolarizzazione)?
- Sviluppiamo (vagamente) un po' di teoria per aiutarci ad analizzare questo problema.

	4
---
**Un ottimo teorico**

- Per funzioni di perdita quadratiche possiamo mostrare che il predittore ottimale è dato da:
  $h(x) = \mathbb{E}[t | x] = \int tp(t | x)dt$

- Che è solo l'aspettativa condizionata di $t$ dato $x$.

- Nota che non abbiamo fatto niente con questo risultato: il punto dell'Apprendimento Automatico, in un certo senso, è di stimare questo $p(t | x)$.

- Cioè, vogliamo fare qualcosa come trovare un $y$ che minimizzi questo errore:
  $\{y(x; D) - h(x)\}^2$

- Questo esprime la perdita inflitta per un singolo input $x$ quando si usa la stima $y(x; D)$.

	5
---
**Bias, varianza e rumore irriducibile**

- Prendendo l'aspettativa rispetto a $D$ e considerando tutti i possibili input, arriviamo (alla fine) a qualcosa che assomiglia a: 
	- perdita attesa $= \text{(bias)}^2 + \text{varianza} + \text{rumore}$, dove:$$\text{(bias)}^2 = \int \left\{ \mathbb{E}_D [y(x; D)] - h(x) \right\}^2 p(x) dx$$$$\text{varianza} = \int \mathbb{E}_D \left[ \{ y(x; D) - \mathbb{E}_D [y(x; D)] \}^2 \right] p(x) dx$$$$\text{rumore} = \int \int \{ h(x) - t \}^2 dx dt$$
	6
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- Bassa complessità, implica alto bias e bassa varianza:

	![[Pasted image 20250930120147.png]]
	
	7
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- Rilassando il coefficiente di regolarizzazione, si riduce il bias e aumenta la varianza:

	![[Pasted image 20250930120342.png]]

	8
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- Rilassando il coefficiente di regolarizzazione, si riduce il bias e aumenta la varianza:

	![[Pasted image 20250930120423.png]]

	9
---
**Regolarizzazione, bias e varianza**

- Tutto questo è molto bello, ma questi integrali sono completamente intrattabili.
- Questi integrali sono medie su dataset, quindi dovremmo avere un ensemble di dataset indipendenti...
- Ed è quasi impossibile stimare robustamente bias e varianza.
- Vedremo metodi più pratici per stimare tradeoff empirici ottimali.

	![[Pasted image 20250930120608.png]]

	10
---
## Regressione Lineare Bayesiana

---
**Non sono felice**

- Potremmo guardare questi risultati di regressione e, sebbene belli, concludere: Non sono felice.
- Perché potremmo non essere felici? Abbiamo sviluppato un insieme di strumenti matematici sofisticati per stimare funzioni dai dati. Che cosa vuoi di più?

	11
---
**Si tratta di fiducia**

- Tutto questo macchinario matematico sofisticato di massima verosimiglianza è fantastico, ma non ci aiuta veramente a capire quanto dovremmo credere in una particolare soluzione.
- In questo caso, la fiducia assume tutta una serie di significati utili:
  - La mia regressione restituisce un $w_{ML}$ dai dati $D$. Fantastico, ma quanto è affidabile quel $w_{ML}$, davvero? Quanto credo che sia vicino al vero $w^*$ che assumiamo abbia generato $D$.
  - Prevedo un $t$ su qualche nuovo input $x'$ usando $t' = y(x', w_{ML})$. Fantastico, ma quanto credo in questo $t'$? Questa fiducia è costante in tutto lo spazio di input?
  - E se ho conoscenza a priori (cioè una credenza sulla mia distribuzione dei parametri $p(w)$) posso incorporarla nella mia stima di $w_{ML}$?
- L'ampia classe delle tecniche bayesiane ci dà esattamente questi strumenti sfruttando verosimiglianza, prior ed evidenza.

	12
---
**A volte si tratta anche di apprendimento sequenziale...**

- E se addestrassimo un modello usando dati $D_1$.
- Poi, domani, qualcuno ci rovescia addosso nuovi dati $D_2$.
- Cosa possiamo fare? Dobbiamo addestrare l'intero modello da zero usando $D = \bigcup_i D_i$?

	13
---
**La distribuzione dei parametri**

- Vogliamo quantificare la nostra fiducia in un modello specifico $w^*$ stimato da $D$.
- Ricorda sempre la tua regola di Bayes: $$p(w | t) = \frac{\text{verosimiglianza dei dati} \times \text{prior}}{\text{evidenza}}$$
- Abbiamo già derivato una verosimiglianza per i dati dato il modello:$$p(t | w, \beta) = \prod_{n=1}^{N} \mathcal{N}(t_n | w^T \phi(x_n), \beta^{-1})$$
- Abbiamo bisogno di una distribuzione **prior** $p(w)$ che esprima la nostra credenza a priori sui valori probabili che $w$ potrebbe assumere.
- Nota la forma della verosimiglianza dei dati e che la moltiplicheremo con questo prior.

	14
---
**La distribuzione dei parametri**

- Scegliamo il nostro prior prima di tutto in modo che sia un'aspettativa ragionevole.
- Per esempio, potremmo aspettarci che i nostri pesi siano *vicini* a zero, in media, con una certa varianza attesa attorno a zero.
- Scegliamo anche la forma del nostro prior in modo che "giochi bene" con la verosimiglianza: $$p(w | \alpha) = \mathcal{N}(w | 0, \alpha^{-1})$$
- Questo è un *Prior Coniugato Gaussiano*, che significa semplicemente che quando lo moltiplichiamo con una verosimiglianza gaussiana, il posterior risultante è anche gaussiano: $$p(w | t) = p(t | w, \beta^{-1}) p(w | \alpha)$$                                                                            $= \mathcal{N}(w | m_N, S_N),$
						dove     $m_N = \beta S_N \Phi^T t$ 
						e            $S_N^{-1} = \alpha I + \beta \Phi^T \Phi$$

	15
---
**La distribuzione dei parametri**

- Mantenere tutto bello e gaussiano ha molti vantaggi – il log posterior è: $$\ln p(w | t) = -\frac{\beta}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2 - \frac{\alpha}{2} w^T w + const$$
- Ti sembra familiare?

	16
---
**La distribuzione dei parametri**

- Mantenere tutto bello e gaussiano ha molti vantaggi – il log posterior è: $$\ln p(w | t) = -\frac{\beta}{2} \sum_{n=1}^{N} \{t_n - w^T \phi(x_n)\}^2 - \frac{\alpha}{2} w^T w + const$$
- Massimizzare questo posterior produce la stessa soluzione del nostro minimi quadrati regolarizzato "normale" con $\lambda = \alpha / \beta!$

- Ma nota che abbiamo qualcosa intrinsecamente più potente qui.

- Abbiamo raggiunto alcuni dei nostri obiettivi:
  - Possiamo quantificare la fiducia in una soluzione $w^*$ (dovrebbe essere chiaro).
  - Possiamo anche apprendere in modo incrementale quando arrivano nuovi dati (probabilmente non così chiaro).

- Diamo un'occhiata a un semplice esempio di adattamento di una linea...

	17
---
**La distribuzione dei parametri**

- Iniziamo senza dati... Quindi, ci rimane il posterior uguale al prior.
- Quando iniziamo a osservare dati, usiamo la regola di Bayes per aggiornare la credenza.
	
	![[Pasted image 20250930124127.png]]

	18
---
**La distribuzione dei parametri**

- Man mano che continuiamo a osservare dati, continuiamo a usare la regola di Bayes per aggiornare la credenza.
- Alla fine, la varianza si riduce e ci stabilizziamo su una stima posterior attorno alla soluzione ML.

	![[Pasted image 20250930124230.png]]

	19
---
**Distribuzione predittiva**

- Nota che non abbiamo detto niente sulle previsioni dal nostro modello.
- Se produco un output $y(x, w^*)$, quanto sono felice con esso? Dipende da $x$ in qualche modo?
- In pratica, non ci importerebbe meno del valore effettivo di $w$, vogliamo solo previsioni!
- Definiamo allora la distribuzione predittiva come: $$p(t | \mathbf{t}, \alpha, \beta) = \int p(t | w, \beta) p(w | \mathbf{t}, \alpha, \beta) dw$$
- Il primo modo di guardare questo è come una media (cioè aspettativa) di verosimiglianze condizionate, dove l'aspettativa è rispetto al posterior (distribuzione dei parametri).

	20
---
**Distribuzione predittiva**

- Se scaviamo nella natura gaussiana di entrambe queste, e notiamo che la distribuzione predittiva è una convoluzione di due gaussiane, possiamo derivare una forma analitica: $$p(t | \mathbf{t}, \alpha, \beta) = N(t | m_N^T \phi(x), \sigma_N^2(x)),$$                                                     dove $\sigma_N^2(x) = \frac{1}{\beta} + \phi(x)^T S_N \phi(x)$

- $1/\beta$ rappresenta il rumore nei nostri dati, e $\sigma_N^2$ rappresenta l'incertezza nella nostra stima dei parametri.

- Nota anche che $\sigma_{N+1}^2(x) < \sigma_N^2(x)$, quindi più dati sono sempre una cosa buona.

	21
---
**Distribuzione predittiva**

- Ora stiamo davvero dicendo qualcosa di utile sugli output del modello:

	![[Pasted image 20250930143351.png]]

	22
---
**Distribuzione predittiva**

- Ora stiamo davvero dicendo qualcosa di utile sugli output del modello:

	![[Pasted image 20250930143404.png]]

	23
---
**Distribuzione predittiva**

- E sulla varianza del modello (campionando dal posterior su $w$):

	![[Pasted image 20250930143514.png]]

	24
---
**Distribuzione predittiva**

- E sulla varianza del modello (campionando dal posterior su w):
	
	![[Pasted image 20250930143632.png]]

*Il miglior regolarizzatore sono sempre più dati annotati.*
*- Geoffrey Hinton (probabilmente).*

	25
---
## Osservazioni conclusive

---
**Regressione lineare in tre atti**

- Abbiamo visto (almeno) tre visioni della regressione lineare:
   - La visione puramente geometrica;
   - La visione di Massima Verosimiglianza; e
   - La visione Bayesiana.

- Questo sfiora appena la superficie di ciò che è possibile, ma è una buona fondazione.
- Interessante, le soluzioni per tutte e tre le visioni sono identiche.
- Ognuna ha, tuttavia, diversi vantaggi e svantaggi: una stima puntuale è efficiente, mentre l'inferenza bayesiana completa ha più funzionalità.
- Importante: il trattamento bayesiano completo è possibile in forma analitica solo a causa delle scelte che abbiamo fatto sul prior sui pesi e sul rumore delle osservazioni.

	26
---
**La strada da percorrere**

- Prossimo volgeremo la nostra attenzione ai modelli lineari per la classificazione.
- Ancora, inizieremo con un modello geometrico di funzioni discriminanti.
- Poi procederemo ad applicare ragionamento probabilistico e bayesiano sulla base della nostra intuizione.
- Sebbene i modelli lineari siano semplici, sono anche spesso molto efficaci e la loro semplice formulazione ammette inferenza semplice e robusta.
- Questa semplicità inferenziale la dovremo lasciare alle spalle quando passeremo a modelli più complessi.

	27
---
**Letture e Compiti a Casa**

- **Lettura Assegnata:**
	- Bishop: Capitolo 3 (3.1, 3.2, 3.3) – questi sono gli stessi dell'ultima lezione!

- **Compiti a Casa:**
	- Vedi l'accompagnamento Jupyter Notebook nel Moodle (quando lo carico).

	28
---

# 5 - Modelli Lineari per la classificazione

---
## Introduzione
---
**Classificazione e superfici decisionali**

- L'obiettivo della classificazione è prendere un vettore di input $x$ e assegnarlo a una delle $K$ classi.
- Denotiamo queste classi come $C_k$ per $k \in \{1, \ldots, K\}$.
- L'ambiente più semplice è la classificazione a singola etichetta dove ogni $x$ appartiene esattamente a una classe.
- Così lo spazio di input è diviso in regioni decisionali i cui confini sono chiamati bordi decisionali o superfici decisionali.
- Considereremo prima modelli lineari dove queste superfici decisionali sono funzioni lineari dell'input $x$.
- Dati le cui classi possono essere separate esattamente con superfici decisionali lineari sono chiamati linearmente separabili.

	2
---
**Obiettivi della lezione**

Alla fine di questa lezione avrete:

- Compreso la geometria delle funzioni discriminanti lineari e come interpretarle.
- Compreso come applicare i minimi quadrati per stimare i parametri di modelli discriminanti lineari.
- Compreso le limitazioni dei minimi quadrati per l'adattamento di modelli di classificazione.
- Compreso come il Discriminante Lineare di Fisher affronta alcune delle carenze dei minimi quadrati trovando una direzione "migliore" per la discriminazione.

	3
---
## Funzioni Discriminanti Lineari
---

**Funzioni discriminanti per due classi**

- La rappresentazione più semplice per un discriminante è una funzione lineare:$$y(x) = w^Tx + w_0$$
- Ancora, $w$ è il vettore dei pesi e $w_0$ è un bias scalare.
- Per la classificazione, il bias negativo è a volte chiamato soglia.
- La regola decisionale: $$\text{classe}(x) = \begin{cases} C_1 & \text{se } w^Tx + w_0 \geq 0 \\ C_2 & \text{se } w^Tx + w_0 < 0 \end{cases}$$
- La distanza normale dall'origine alla superficie decisionale è:$$\frac{w^Tx}{||w||} = -\frac{w_0}{||w||}$$
	4
---
**La geometria dei discriminanti lineari**

- Questa è la grafica a cui penso quando voglio ricordare come funziona la geometria del discriminante lineare:

	![[Pasted image 20251001223839.png]]

	5
---
**Incorporare il bias nella base**

- Come con la regressione, a volte è conveniente usare una notazione compatta.
- Quindi, introduciamo una dimensione fittizia $x_0 = 1$ e definiamo:
						$\hat{w} = (w_0, w)^T$
					
						$\tilde{x} = (x_0 = 1, x)^T$
					
			così che $y(x) = \hat{w}^T \tilde{x}$

- Quindi le superfici decisionali in questo spazio sono iperpiani $D$ dimensionali passanti per l'origine dello spazio aumentato $D + 1$ dimensionale.

	6
---

**Classi multiple**

- OK, ma i problemi a due classi sono davvero noiosi. E se ne abbiamo di più?
- Potremmo usare $K - 1$ classificatori, ognuno risolvendo un problema a due classi separando una classe $C_k$ dai punti non in quella classe.
- Questo è noto come classificatore one-versus-rest:

	![[Pasted image 20251001224446.png]]
	
	7
---
**Classi multiple**

- Torniamo alla lavagna... Usa $K(K-1)/2$ funzioni discriminanti binarie.
- Una per ogni coppia di classi:

	![[Pasted image 20251001224540.png]]

	8
---
**Classi multiple**

- Possiamo evitare tutti questi problemi se usiamo un singolo discriminante a K classi impiegando $k$ funzioni lineari:$$y_k(x) = w_k^T x + w_{k0}$$
- Che possiamo anche impacchettare insieme in una singola moltiplicazione di matrici:$$y(x) = \tilde{W}^T \tilde{x}$$
- Ora assegniamo semplicemente $x$ alla classe $C_k$ se $y_k(x) \geq y_j(x)$ per tutti $j \neq k$.

	9
---
**Bordi decisionali per classi multiple**

- Poiché stiamo prendendo un max su funzioni lineari, abbiamo regioni decisionali semplicemente connesse e convesse:

	![[Pasted image 20251001225538.png]]
	
	10
---
## Minimi Quadrati per la Classificazione
---

**Un modello lineare compatto**

- Per la regressione, i modelli lineari con una misura di errore ai minimi quadrati hanno portato a una semplice soluzione in forma chiusa.
- Quindi, vediamo se possiamo riuscire a fare lo stesso trucco qui.
- Ogni classe è descritta dal proprio modello lineare:$$y_{k}(x) = w_{k}^{T}x + w_{k0}$$
- O, ancora meglio:$$y(x) = \tilde{W}^{T}\tilde{x}$$
- È utile pensare a cosa sono le colonne di $\tilde{W}$.
- Inoltre, quali dovrebbero essere i nostri target per la classificazione?

	11
---
**Una soluzione analitica**

- Risolviamo per $\tilde{W}$ minimizzando un errore somma-dei-quadrati.
- Considera un training set $\{x_n, t_n\}$ per $n \in \{1, \ldots, N\}$.
- E definisci una matrice $T$ la cui riga $n^{esima}$ è $t_n^T$.
- Insieme a una corrispondente matrice $\tilde{X}$ la cui riga $n^{esima}$ è $\tilde{x}_n^T$.
- Possiamo allora scrivere la funzione di errore come:$$E(\tilde{W}) = \frac{1}{2}Tr\left\{(\tilde{X}\tilde{W} - T)^T(\tilde{X}\tilde{W} - T)\right\}$$
- Impostando il gradiente rispetto a $\tilde{W}$ a zero e risolvendo, arriviamo a:$$\tilde{W} = (\tilde{X}^T\tilde{X})^{-1}\tilde{X}^TT = \tilde{X}^{\dagger}T$$ 

	12
---
**Una soluzione analitica**

- Quindi abbiamo una bella forma analitica per un classificatore a K classi da dati:
  $y(x) = \tilde{W}^T \tilde{x} = T^T (\tilde{X}^{\dagger})^T \tilde{x}$

- Tuttavia, non è un classificatore molto buono:

	![[Pasted image 20251001230826.png]]

	13
---
## Discriminante Lineare di Fisher
---

**Classificazione lineare come riduzione di dimensionalità**

- Un modo di pensare alla classificazione lineare con discriminanti è come una riduzione di dimensionalità a una dimensione.
- Diamo un'occhiata ad alcuni esempi motivanti di questo...

	14
---
**Separare le medie**

- La nostra prima strategia potrebbe essere di calcolare le medie di ogni classe nello spazio delle feature:$$\mathbf{m}_1 = \frac{1}{N_1} \sum_{n=1}^{N_1} x_{1,n}, \quad \mathbf{m}_2 = \frac{1}{N_2} \sum_{n=1}^{N_2} x_{2,n}$$
- E poi calcolare $\mathbf{w}$ in modo che la proiezione di questi due punti su di esso massimizzi la distanza tra le proiezioni:$$\mathbf{w}^T \mathbf{m}_2 - \mathbf{w}^T \mathbf{m}_1 = \mathbf{w}^T (\mathbf{m}_2 - \mathbf{m}_1)$$
- Qualcuno vede un problema nel massimizzare questa espressione?

	15
---
**Separare le medie**

- La nostra prima strategia potrebbe essere di calcolare le medie di ogni classe nello spazio delle feature:$$m_1 = \frac{1}{N_1} \sum_{n=1}^{N_1} x_{1,n}, \quad m_2 = \frac{1}{N_2} \sum_{n=1}^{N_2} x_{2,n}$$
- E poi calcolare $w$ in modo che la proiezione di questi due punti su di esso massimizzi la distanza tra le proiezioni:$$w^T m_2 - w^T m_1 = w^T (m_2 - m_1)$$
- Qualcuno vede un problema nel massimizzare questa espressione?
- Possiamo imporre il vincolo che $||w||_2 = 1$ nell'ottimizzazione (usando un moltiplicatore di Lagrange).
- Il risultato è, non a sorpresa: $w \propto (m_2 - m_1)$

	16
---
**Separare le medie**

- Va bene? Cosa non funziona?

	![[Pasted image 20251001231132.png]]

	17
---
**Tenere conto dell'anisotropia**

- Entrambe le distribuzioni di classe hanno matrici di covarianza fortemente non diagonali.
- L'intuizione di Fisher era di massimizzare la varianza inter-classe, mentre simultaneamente minimizzava la varianza intra-classe nello spazio proiettato, 1-dimensionale.
- La varianza within-class – anche chiamata compattezza – è:$$S_k^2 = \sum_{n=1}^{N_k} (w^T x_{k,n} - w^T m_k)^2$$
- Il Criterio di Fisher è allora il rapporto tra la varianza between-class e la varianza within-class:$$J(w) = \frac{(w^T m_2 - w^T m_1)^2}{S_1^2 + S_2^2}$$
	18
---
**Generalizzando**

- Possiamo rendere between e within più espliciti scrivendo:$$J(w) = \frac{w^T S_B w}{w^T S_W w} \quad (\text{vedi Eq 4.27 e 4.28 in Bishop})$$
- Dove qui $S_B$ è la covarianza between-class, e $S_W$ è la within-class.

- Dopo aver differenziato e manipolato i termini, troviamo:$$(w^T S_B w) S_W w = (w^T S_W w) S_B w$$
- Non ci interessa (per ora) la scala di $w$, quindi dopo aver eliminato i fattori scalari e moltiplicato per $S_W^{-1}$:$$w \propto S_W^{-1}(m_2 - m_1)$$
	19
---
**Discriminante Lineare di Fisher per due classi**

- Che funziona molto meglio:

	![[Pasted image 20251001231407.png]]

	20
---
**Relazione con i minimi quadrati**

- L'approccio dei minimi quadrati alla classificazione basata su discriminanti lineari si basa sull'apprendere funzioni lineari che siano il più vicine possibile all'insieme dei valori target.
- Il Criterio di Fisher, invece, cerca di massimizzare la separazione delle classi nello spazio discriminante.
- Per il problema a due classi, possiamo mostrare che il discriminante di Fisher è in realtà un caso speciale del vecchio minimi quadrati.
- Invece di usare un target di 1 per le probabilità target one-hot, useremo:$$t_n = \begin{cases} \frac{N}{N_1} & \text{se } x_n \in C_1 \\ -\frac{N}{N_2} & \text{se } x_n \in C_2 \end{cases}$$
- Questa è una stima del prior reciproco per ogni classe.

	21
---
**Relazione con i minimi quadrati**

- Il nostro errore è ancora minimi quadrati:$$E = \frac{1}{2} \sum_{n=1}^{N} (w^T x_n + w_0 - t_n)^2$$
- Impostando i gradienti a zero rispetto a $w_0$ e $w$:$$\sum_{n=1}^{N} (w^T x_n + w_0 - t_n) = 0$$$$\sum_{n=1}^{N} (w^T x_n + w_0 - t_n)x_n = 0$$
	22
---
**Relazione con i minimi quadrati**

- Risolvendo, troviamo (usando liberamente l'espressione per i nuovi target):$$w_0 = -\frac{w^T (N_1 m_1 + N_2 m_2)}{N}$$
- E per la direzione:$$w \propto S^{-1}_W (m_2 - m_1)$$
	23
---
## Osservazioni Conclusive
---
**Discriminanti lineari**

- In questa introduzione abbiamo guardato i discriminanti lineari per la classificazione supervisionata.
- Questi approcci sono approssimativamente equivalenti agli approcci geometrici per la regressione lineare.
- In realtà, sono più simili alle soluzioni di massima verosimiglianza per la regressione, ma dobbiamo ancora aggiungere un'interpretazione probabilistica.
- È importante avere una sensazione per la geometria dei discriminanti lineari.

- Proiettiamo gli input sui pesi del modello $w$.
- Questo vettore peso $w$ è perpendicolare alla superficie discriminante.
- Un discriminante lineare riduce implicitamente a un problema di soglia unidimensionale.

	24
---
**I minimi quadrati fanno schifo come classificatore**

- La classificazione con minimi quadrati ha svantaggi significativi – più notablemente la sua sensibilità agli outlier.
- Come vedremo, stiamo implicitamente facendo assunzioni sulla forma delle distribuzioni di classe quando usiamo i minimi quadrati.
- Ciononostante, manteniamo ancora la soluzione in forma chiusa analitica offerta dai minimi quadrati.

	25
---
**Discriminante Lineare di Fisher**

- Se ruotiamo lo spazio in modo da massimizzare certe proprietà delle proiezioni di classe, possiamo fare meglio.
- Questo è ciò che fa il Criterio di Fisher: massimizzare la varianza between-class, mentre minimizza la varianza within-class.
- Fare questo migliora significativamente le performance di classificazione lineare.
- Ma, mantiene ancora le belle proprietà analitiche dei minimi quadrati.

	26
---
**La strada da percorrere**

- Seguendo il nostro sviluppo per la regressione, nella prossima lezione daremo un'occhiata ai modelli probabilistici per la classificazione.
- Guarderemo la classificazione da prospettive generative e discriminative.
- E svilupperemo un approccio completamente bayesiano alla classificazione.
- Questi modelli manterranno le proprietà lineari che siamo venuti a conoscere e amare, e ammetteranno soluzioni analitiche date alcune assunzioni chiave.

	27
---
**Il Perceptron**

- C'è un altro importante approccio geometrico alla classificazione con discriminanti lineari.
- L'Algoritmo Perceptron è un importante precursore delle moderne Reti Neurali Artificiali (ANN).
- Infatti, il Perceptron – cioè una funzione discriminante lineare – è il blocco fondamentale dei moderni modelli di reti neurali.
- Ritarderemo, tuttavia, la nostra discussione sul Perceptron finché non staremo per tuffarci nei moderni modelli di Deep Learning.

	28
---
**Letture e Compiti a Casa**

- Lettura Assegnata:
	- Bishop: Capitolo 4 (4.1 – 4.1.6)

	29
---
# 6 - 


