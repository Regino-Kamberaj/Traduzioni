# Introduzione
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

# Preliminari Matematici

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

- Questo assume un significato speciale quando applicato all'*inferenza parametrica*:  $$p(\mathbf{w} | \mathcal{D}) = \frac{p(\mathcal{D} | \mathbf{w})p(\mathbf{w})}{p(\mathcal{D})}$$$$\text{posterior} \propto \text{verosimiglianza dei dati} \times \text{prior}$$
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

- La distribuzione Gaussiana *univariata* è super importante:$$\mathcal{N}(x | \mu, \sigma) = \frac{1}{(2\pi\sigma^2)^{1/2}} \exp\{-\frac{1}{2\sigma^2}(x - \mu)^2\}$$
- Così come la distribuzione Gaussiana *multivariata*, che useremo estesamente:$$\mathcal{N}(x | \mu, \Sigma) = \frac{1}{(2\pi)^{D/2}} \frac{1}{|\Sigma|^{1/2}} \exp\{-\frac{1}{2}(x - \mu)^T\Sigma^{-1}(x - \mu)\}$$
- Qui $\mu$ è un vettore $D$ dimensionale (**la media**) e $\Sigma$ è la *matrice di covarianza* $D \times D$.

	39
---
**Teoria decisionale e classificazione supervisionata**

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
