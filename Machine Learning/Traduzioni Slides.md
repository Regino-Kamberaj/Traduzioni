**Fondamenti di Apprendimento Automatico:**

Prof. Andrew D. Bagdanov (andrew.bagdanov AT unifi.it)

**UNIVERSITÀ**
**DEGLI STUDI**
**FIRENZE**

**DINFO**

**DIPARTIMENTO DI**
**INGEGNERIA**
**DELL'INFORMAZIONE**

Ricorda
![[Pasted image 20251024225359.png]]

---
# 1 - Introduzione

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
- Un modo di pensare l'apprendimento automatico è: $\text{Apprendimento Automatico} = \text{(Statistica Computazionale + Ottimizzazione)}$ 
						$+ \text{Dati (di solito molti)}$

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

-  Quindi, abbiamo una situazione come questa…
-  Cosa possiamo fare?

	![[Pasted image 20250917230650.png]]

	8
---
**Apprendimento supervisionato: un esempio**

- Beh, un po' di algebra delle scuole medie ci permette di connettere i punti:  $$y = 8.013x - 373.247$$ perché questo modello? => tipo perché non una parabola?  => la retta è il modello più semplice! => con due sole variabili!

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

- **Parte II**: Apprendimento Profondo (deep learning)
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

- I vostri giorni di apprendimento in ambienti di apprendimento strutturati sono (quasi) finiti. => Define your learning objectives? 

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
- Una **funzione di perdita** $\mathcal{L} : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$. => cerco la funzione migliore che approssima all'interno del mio spazio di Ipotesi => certe volte chiamata *risk function* => funzione di perdita alta quando la nostra funzione non si comporta bene!

Un obiettivo di apprendimento:

- Assumendo che la vera $h \in \mathcal{H}$, possiamo semplicemente:$$h^* = \arg \min_{h \in \mathcal{H}} \mathbb{E}_p[\mathcal{L}(h(x), y)] =$$ $$= \arg \min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$
- Problema di minimizzazione => integro su tutti i valori x,y => expectation di una loss value tramite una **likelihood sui dati** => cerco di penalizzare il più possibile quei valori che hanno una alta similarità ma anche un loss value molto alta! (vado a vedere il valore restituito da h e confronto con y) => questo fra tutte le combinazioni di x e y 

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

Scegliendo ad esempio un h* che sia esattamente y e una loss qualsiasi (tipo quadratica)... rischio di avere un modello **che approssima troppo** => extreme over-fitting

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

- Non abbiamo finito. C'è un *iperparametro* del nostro modello che abbiamo convenientemente dimenticato: **l'ordine del polinomio $M$.**

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
- Questo è il caso in molti problemi di regressione dove gli output in ==alcuni punti potrebbero essere **più certi** di altri.== => in questi casi ho informazioni locali

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

- **Definizione (Prodotto Interno e Spazio con Prodotto Interno)**
	- Sia **V** un qualsiasi spazio vettoriale e $\Omega : V \times V \to \mathbb{R}$ una qualsiasi mappa *bilineare* da **V** a $\mathbb{R}$ Allora:
		- Se $\Omega$ è simmetrica e definita positiva, $\Omega$ è chiamata un *prodotto interno* su **V**. Di solito scriviamo $\langle x,y\rangle$ invece di $\Omega(x,y)$.
		- La coppia $(V,\Omega)$ (o $(V,\langle\cdot,\cdot\rangle)$ ) per prodotto interno $\Omega$ è chiamata **spazio con prodotto interno** o *spazio vettoriale con prodotto interno*. Se: $$\Omega(x,y) = x^Ty \space ,  (V,\Omega)$$ è chiamato **spazio vettoriale euclideo**.

- I prodotti interni ci permettono di formalizzare le nostre intuizioni geometriche su lunghezza, ortogonalità e distanza.

	17
---
**Proiezioni ortogonali**

- //Inserire sketch se lo fa

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
    = \mathbb{E}_x [\mathbf{x}\mathbf{x}^T] - \mathbb{E}[\mathbf{x}] \mathbb{E}[\mathbf{x}^T]$$
	38
---
**La distribuzione Gaussiana (a proposito di covarianza)**

- La distribuzione Gaussiana *univariata* è super importante:$$\mathcal{N}(x | \mu, \sigma) = \frac{1}{(2\pi\sigma^2)^{1/2}} \exp\{-\frac{1}{2\sigma^2}(x - \mu)^2\}$$=> al limite aumentando la $\sigma$ si passa alla distribuzione uniforme

- Così come la distribuzione Gaussiana *multivariata*, che useremo estesamente:$$\mathcal{N}(x | \mu, \mathbf{\Sigma}) = \frac{1}{(2\pi)^{D/2}} \frac{1}{|\mathbf{\Sigma}|^{1/2}} \exp\{-\frac{1}{2}(x - \mu)^T\mathbf{\Sigma}^{-1}(x - \mu)\}$$ => forma quadratica ma su più dimensioni

- Qui $\mu$ è un vettore $D$ dimensionale (**la media**) e $\mathbf{\Sigma}$ è la *matrice di covarianza* $D \times D$. => di solito simmetrica (diagonale) e positiva => allineati agli assi x e y => altrimenti per trovare le direzioni si trovano tramite autovettori

	39
---
**Teoria decisionale e classificazione supervisionata** (skipped da qui in poi)

- Proviamo ad espandere la nostra crescente intuizione per includere **problemi di classificazione.**
- La teoria della probabilità ci dà un modo disciplinato per rappresentare e **quantificare l'incertezza,** quindi usiamola!

- Supponiamo di avere un input **x** insieme a un vettore **y** di variabili target.
- Per problemi di regressione, **y** saranno variabili continue, mentre per problemi di classificazione rappresenterà **etichette di classe**.

- La distribuzione congiunta **p(x, y)** ci dà un quadro completo dell'incertezza associata a queste variabili.

	40
---
**Teoria decisionale e classificazione supervisionata**

- Come esempio, supponiamo che **x** sia una radiografia a 512 × 512 pixel di un paziente e vogliamo decidere se il paziente ha il cancro: $$f(x) = \begin{cases}  0 & \text{se il paziente ha il cancro} \\ 1 & \text{altrimenti} \end{cases}$$
- Come potrebbe apparire il nostro **dataset**? Beh, probabilmente un insieme di coppie: $$\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N)\}$$
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

- Minimizzare il tasso di *classificazione errata* (misclassification) atteso.
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

2. Mostra che la moda di una distribuzione Gaussiana $\mathcal{N}(\mu, \sigma)$ è data da $\mu$.

	50
---
# 3 - Regressione Lineare dalla geometria alla massima verosimiglianza

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

- Consideriamo prima la classe dei problemi di regressione univariata (un unico target per un singolo input) dove osserviamo coppie di osservazioni $(x_i, t_i)$, dove:
  - $x_i \in \mathbb{R}$ sono osservazioni della variabile **indipendente**.
  - $t_i \in \mathbb{R}$ sono osservazioni della variabile **dipendente**. => t per variabile target

- Assumiamo che la variabile dipendente sia in relazione con la variabile indipendente tramite una funzione $f$ che è sconosciuta **ma lineare** nei suoi parametri $\mathbf{w}$:$$y(x | \mathbf{w}) = w_0 + w_1 x = \mathbf{w}^T \begin{bmatrix} 1 \\ x \end{bmatrix}$$
	=> posso rappresentare dunque qualsiasi funzione lineare => ovvero qualsiasi retta!
	
	5
---
**Quantificare la bontà di una soluzione**

- OK, abbiamo alcuni dati (cioè osservazioni della variabile indipendente e dipendente).
- E abbiamo uno **spazio di ipotesi** convenientemente parametrizzato da **w**.
- Per apprendere effettivamente qualcosa (cioè adattare il modello ai dati) abbiamo poi bisogno di una qualche sorta di *perdita*(loss) $\mathcal{L}$.
- Questa perdita dovrebbe misurare la *cattiveria* di un'ipotesi arbitraria $w'$ – cioè, **alta perdita** indica un cattivo adattamento e bassa perdita uno buono.

- Sarà una funzione dei **parametri candidati** e dei dati osservati  $D = \{(x_i, t_i) \mid i = 1, \ldots N\};$ $$E(w \mid D) = \frac{1}{2} \sum_{i=1}^{N} [y(x_i|w) - t_i]^2$$=> provo a calcolare la somma degli errori quadrati => come distanza dei nostri punti alla retta

	![[Pasted image 20251004225236.png]]
	=> primo esempio di Loss => in regressione si parla di *error function* => come mai il quadrato? beh vorrei solo valori positivi ma anche una funzione semplice da derivare => per il problema di minimizzazione => trovare il $w$ che minimizza la funzione
	
	6
---
**Regressione Lineare: una Critica della Ragione Pura**

- Esamineremo più in dettaglio questa scelta di **perdita**.
- Ma, per ora consideriamo le proprietà, buone e cattive, di questa formulazione. $$E(\mathbf{w} | D) = \sum_{i=1}^{N} [(w_0 + w_i x_i) - t_i]^2$$ ne considero la derivata secondo la direzione $\mathbf{w}$
 $$\nabla_w \ E(\mathbf{w} | D) =\frac{1}{2} \sum_{i=1}^{N} \nabla_w \ [(w_0 + w_i x_i) - t_i]^2$$ => per la linearità della derivazione
 $$= \sum_{i=1}^{N}[(w_0 + w_i x_i) - t_i] \ \nabla_w \ [(w_0 + w_i x_i) - t_i]$$
$$= \sum_{i=1}^{N}e_i[1 \ x_i]^T$$ => avendo sostituito la prima parte con la funzione di errore, mentre la derivata della seconda parte si riottene semplicemente $x_i$ (il resto rimane costante)
=> Ma $$w_{t+1} = w_t - \eta \nabla E(w_t | D)$$ => rappresenta esattamente il metodo di discesa del gradiente => $\eta$ controlla quanto ci muoviamo in direzione dell'antigradiente => *learning rate* => difficile da parametrizzare! => si rischia di "saltare" il punto di minimo

	7
---parametri saranno a zero
## Regressione Lineare e Stima di Massima Verosimiglianza
---
**Stima di Massima Verosimiglianza (MLE) e Minimi Quadrati**

- La nostra interpretazione geometrica è un esempio di stima puntuale dei parametri del modello: ci dà una soluzione $w^*$ che è un **singolo punto** nello spazio dei parametri.

- Vorremmo spostarci verso un modello **probabilistico** di regressione lineare.
- Questo dovrebbe, idealmente:
  - Permetterci di ragionare probabilisticamente sulla ==qualità della nostra soluzione==.
  - Permetterci di **quantificare la fiducia** nella qualità delle singole previsioni.
  - Permetterci di "infornare" **conoscenza a priori** su soluzioni probabili. 

- Il nostro primo passo è la *Stima di Massima Verosimiglianza* (MLE - maximum likelihood estimation) dei parametri ottimali $w$ dati i dati osservati $D$. => stavolta vogliamo stimare la massima verosimiglianza per i dati generati dai parametri scelti.
- Primo, **irrobustiamo** un po' il nostro modello per permettere funzioni polinomiali dell'input.

	8
---
**Modelli lineari con funzioni di base**

- Il modello lineare più semplice per la regressione usa solo combinazioni lineari delle variabili di input $x = (x_1, \ldots, x_D)^T$:$$y(x | w) = w_0 + w_1 x_1 + \ldots + w_D x_D$$ $$= \mathbf{w}^T \begin{bmatrix} 1 \\ x_1 \\ ... \\ x_D  \end{bmatrix}$$
 => si passa a punti in $D$ dimensioni => dopo due si parla di iperpiano che divide i nostri punti (prima consideravamo rette e via via aumentavamo il grado => qui si aumentano le dimensioni)

- Questa è una **funzione lineare** sia in $w$ (buono => permette di derivare e riottenere la nostra funzione di error di partenza) che in $x$ (molto limitante!).

- Quindi, possiamo permettere combinazioni lineari di funzioni **non lineari** fisse dell'input:$$y(\mathbf{x} | \mathbf{w}) = w_0 + \sum_{j=1}^{M-1} w_j \phi_j(x)$$
	=> Aggiungo *funzioni base* (che producono un singolo scalare) come $\phi_0 (x) = 1$, $\phi_1(x) = x$ ... faccio il "basis mapping" $$\phi(x) = \begin{bmatrix} \phi_0(x) \\ \phi_1(x) \\ ... \end{bmatrix}$$ tipo $$\phi(x) = \begin{bmatrix} 1 \\ x \\ x^2 \\ x^3 \end{bmatrix}$$
- Riassumendo: $$y(\mathbf{x}| \mathbf{w},D)= \mathbf{w}^T \mathbf{\phi(x)}$$
	9
---
**Modelli lineari con funzioni di base**

- $w_0$ è conosciuto come parametro di bias e permette per qualsiasi offset fisso nell'output.
- È spesso conveniente definire una funzione di base fittizia $\phi_0(x) = 1$ così possiamo scrivere in modo compatto:$$y(\mathbf{x} | \mathbf{w}) = \sum_{j=0}^{M-1} w_j \phi_j(x)= \mathbf{w}^T \mathbf{\phi(x)}$$
- Dove $w = (w_0, \ldots, w_{M-1})^T$ e $\phi = (\phi_0, \ldots, \phi_{M-1})^T$
- Funzioni di base comuni: $$\phi_i(x) = x^i \quad \phi_i = \exp\{-\frac{(x - \mu_i)^2}{2s^2}\} \quad \phi_i(x) = \tanh(x)$$
				Polinomiale                 Gaussiana                       Funzione di squashing
				
	=> con la gaussiana possiamo tipo prendere diverse medie e vedere a quale si avvicina di più al nostro punto target
	 ![[Pasted image 20251004234754.png]]
	=> mapping di uno scalare ad un vettore di 3 valori => quanti sceglierne (scelta sull'M) ? boh si vedrà dopo con crossvalidation

	10
---
**Massima verosimiglianza e minimi quadrati**

- Pulito, ma dove sono le nostre *probabilità* in tutto questo?!
- Torniamo alla nostra assunzione originale che la nostra variabile *target* è la realizzazione di una funzione *deterministica* $y(\mathbf{x}| \mathbf{w})$ con rumore gaussiano additivo:$$t = y(\mathbf{x} | \mathbf{w}) + \epsilon$$
- Dove $\epsilon$ è una variabile casuale gaussiana **a media zero**, con **precisione** $\beta$. => precisione che nella gaussiana è inversamente proporzionale alla varianza $\sigma$ => $\beta \propto \frac{1}{\sigma^2}$

- Così, possiamo scrivere:$$p(t | \mathbf{x}, \mathbf{w}, \beta) = \mathcal{N}(t \ | \ y(\mathbf{x} | \mathbf{w}), \beta^{-1})$$
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

- Ora considera un dataset di input $\mathbf{X} = \{x_1, \ldots, x_N\}$
- Insieme a valori target corrispondenti $t = (t_1, \ldots, t_N)^T$.
- Assumendo che questi campioni siano tutti **identicamente e indipendentemente** estratti da $p(t | \mathbf{x}, \mathbf{w}, \beta)$, possiamo scrivere:$$p(t | \mathbf{X}, \mathbf{w}, \beta) = \prod_{n=1}^N \mathcal{N}(t_n | y(\mathbf{x_n}, \mathbf{w}), \beta^{-1})$$ => dati **X**,**w**,$\beta$ calcolo la probabilità di ottenere i miei punti target secondo la legge delle probabilità indipendenti	$$= \prod_{n=1}^N \mathcal{N}(t_n | \mathbf{w}^T \phi(\mathbf{x}_n), \beta^{-1})$$=> se ci sono punti molto distanti a probabilità zero => la probabilità si abbassa molto!

- E abbiamo un'espressione di verosimiglianza (likelihood) molto scomoda per i nostri dati sotto un modello specifico. => potenzialmente i punti sono parecchi => prodotto incoveniente => rischio di avere problemi di underflow per valori molto prossimi a zero

	13
---
**Massima verosimiglianza e minimi quadrati**

- Per la maggior parte dei problemi di apprendimento supervisionato non siamo interessati a modellare la distribuzione degli input.
- Quindi X apparirà sempre nelle variabili condizionanti e per ora lo ometteremo per sgomberare la notazione.
- Prendere i logaritmi aiuta a semplificare la verosimiglianza (grazie in parte alla forma esponenziale della Gaussiana):$$\ln p(t |X, w, \beta) = \sum_{n=1}^{N} \ln \mathcal{N}(t_n | w^T \phi(x_n), \beta^{-1})$$ => il logaritmo di prodotti diventa una somma di logaritmi => ottengo una gaussiana univariata (riguarda gaussiana) => esponenziale sparisce!
$$= \frac{N}{2} (\ln \beta - \ln(2\pi)) - \frac{\beta}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2$$
	=> prima parte che non dipende dalla scelta del modello => **la seconda invece è proprio la nostra funzione di errore** (vista geometricamente) che con il meno sarà appunto minimizzata (per trovare il max => vogliamo max questa probabilità)

	14
---
**Massima verosimiglianza e minimi quadrati**

- Massimizziamo questa *verosimiglianza* in $\mathbf{w}$. Prima il gradiente:$$\nabla \ln p(t | w, \beta) = \beta \sum_{n=1}^{N} [t_n - w^T \phi(x_n)] \phi(x_n)^T$$
- E impostiamolo a **zero**:$$0 = \sum_{n=1}^{N} t_n \phi(x_n)^T - w^T \left( \sum_{n=1}^{N} \phi(x_n) \phi(x_n)^T \right)$$
- Che dopo aver risolto per $\mathbf{w}$ ci dà:$$\mathbf{w}_{ML} = (\Phi^T \Phi)^{-1} \Phi^T t$$
	15
---
**Massima verosimiglianza e minimi quadrati**

- Questa soluzione $(\Phi^T\Phi)^{-1}\Phi^T$ usa la matrice del disegno (*design matrix* ?):
$$\Phi = \begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1) & \cdots & \phi_{M-1}(x_1)\\
\phi_0(x_2) & \phi_1(x_2) & \cdots & \phi_{M-1}(x_2)\\
\vdots & \vdots & \ddots & \vdots\\
\phi_0(x_N) & \phi_1(x_N) & \cdots & \phi_{M-1}(x_N)
\end{pmatrix}$$
=> **le righe corrispondono ai singoli dati** => una riga per ogni punto nel dataset (x1, x2, ...) => e la funzione base applicata ai punti => transposed e messa in una matrice

- Un modo facile per pensare a $\Phi$:
  - Una **riga** è la ==valutazione di **tutte** le funzioni di base== sul corrispondente campione di training (dimensionalità M).
  - Una **colonna** è **la corrispondente** funzione di base valutata su tutti i campioni di training (dimensionalità N).
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

	=> Voglio capire almeno quando sto overfittando... => al grado 9 ho bisogno di grandi valori per far passare esattamente nei punti => vado fuori scala => in genere vado molto male quando ottengo dei valori di magnitudine molto grandi
	=> Possiamo pensare di tenere le nostre soluzioni entro un certo range di valori.

	23
---
**Minimi quadrati regolarizzati**

- Considereremo obiettivi di regressione di questa forma:  $$E_D(\mathbf{w}) + \lambda E_W(\mathbf{w})$$
- Dove $E_D$ continuerà ad essere il nostro **errore ai minimi quadrati** con funzioni di base $\phi$. => dipendente dal Dataset e i parametri del modello

- Il termine $E_W$ è chiamato *regolarizzatore* dei pesi (o solo regolarizzatore), e uno molto comune è la norma al quadrato dei pesi del modello: $$E_W(\mathbf{w}) = \frac{1}{2} \mathbf{w}^T \mathbf{w} = || \mathbf{x}||_2^2$$ => ==dipende solo dai parametri ==(i pesi) => questo esempio è regolarizzatore L2

- Quindi, la funzione di **errore totale da minimizzare** diventa:$$E(\mathbf{w}) = \frac{1}{2} \sum_{n=1}^{N} \{ t_n - \mathbf{w}^T \phi(\mathbf{x_n}) \}^2 + \frac{\lambda}{2} \mathbf{w}^T \mathbf{w}$$=> $\lambda$ serve a scegliere il range di valori da accettare (intensity of the regularizator) => in questo modo tutti i valori troppo al di fuori del range vengono pagati tanto!

	24
---
**Minimi quadrati regolarizzati**

- Questa funzione di errore regolarizzata: $$E(w) = \frac{1}{2} \sum_{n=1}^{N} \{ t_n - \mathbf{w}^T \phi(x_n) \}^2 + \frac{\lambda}{2} \mathbf{w}^T \mathbf{w}$$
- È ancora una funzione quadratica in $\mathbf{w}$, e la $\mathbf{w}$ ottimale è:$$\mathbf{w}_{ML} = (\lambda I + \Phi^T \Phi)^{-1} \Phi^T t$$ => notare che l'aggiunta della costante aiuta a rendere invertibile la matrice!

- La stima di Massima Verosimiglianza del parametro di imprecisione $\beta$ può anche essere derivata massimizzando $p(t | w, \beta)$ rispetto a $\beta$:$$\frac{1}{\beta_{ML}} = \frac{1}{N} \sum_{i=1}^{N} [t_n - \mathbf{w}_{ML}^T \phi(x_i)]^2$$
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

- Un errore regolarizzato più **generale** è: $$\frac{1}{2} \sum_{n=1}^{N} \{ t_n - w^T \phi(x_n) \}^2 + \frac{\lambda}{2} \sum_{j=1}^{M} |w_j|^q$$
	![[Pasted image 20250929231614.png]]

	=> Per q=1 si parla di "sparse solution" => accetto punti anche con valori dei parametri nulli
	=> Per q=2 => small norm (magnitude) solution
	27
---
**Minimi quadrati regolarizzati**

- Un errore regolarizzato più generale è:
	 ![[Pasted image 20251005175435.png]]
	=> bisogna trovare quindi il punto migliore sia per $E_D$ che $E_W$:
		=> Nel primo caso lo trovo equidistante a 1
		=> Nel secondo caso si nota che alcuni ==parametri saranno a zero==! => sparse solution!

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
- Con questo modello di adattamento di curve (le spline sono in realtà un'istanza di questo) possiamo ==adattare molti fenomeni==.

	29
---
**La strada da percorrere**

- Gli stimatori puramente geometrici e MLE che abbiamo sviluppato sono esempi di **stime puntuali**.
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
- Riconosciuto la differenza tra stime puntuali come **Massima Verosimiglianza** e il trattamento bayesiano completo della regressione lineare.
- Comprendere come l'inferenza bayesiana ci permette di incorporare (richiede, in realtà) informazione a priori sui parametri del modello.
- Comprendere come l'inferenza bayesiana ci permette sia di quantificare che di aggiornare la nostra fiducia nelle previsioni del modello.

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

- Per funzioni di perdita quadratiche possiamo mostrare che il **predittore ottimale** è dato da:$$h(x) = \mathbb{E}[t | \mathbf{x}] = \int tp(t | \mathbf{x})dt$$
- Che è solo l'*aspettativa condizionata* di $t$ dato $x$.

- Nota che non abbiamo fatto niente con questo risultato: il punto dell'Apprendimento Automatico, in un certo senso, è di stimare questo $p(t | x)$.

- Cioè, vogliamo fare qualcosa come trovare un $y$ che minimizzi questo errore:$$\{y(\mathbf{x}; D) - h(\mathbf{x})\}^2$$
- Questo esprime la **perdita** "inflitta" per un singolo input **x** quando si usa la stima $y(\mathbf{x}; D)$.

	5
---
**Bias, varianza e rumore irriducibile**

- Prendendo l'expectation rispetto a $D$ e considerando tutti i possibili input, arriviamo (alla fine) a qualcosa che assomiglia a: 
	- **perdita attesa** $= \text{(bias)}^2 + \text{varianza} + \text{rumore}$, dove:$$\text{(bias)}^2 = \int \left\{ \mathbb{E}_D [y(x; D)] - h(x) \right\}^2 p(x) dx$$ che misura la distanza del predittore dall'aspettativa sull'intero dataset. => ovvero quanto preferiamo soluzioni precise/specifiche => un bias molto alto indica che qualsiasi input restituisce lo stesso valore$$\text{varianza} = \int \mathbb{E}_D \left[ \{ y(x; D) - \mathbb{E}_D [y(x; D)] \}^2 \right] p(x) dx$$ Ovvero quanto un modello si adatta ad uno specifico dataset 
	=> faccio la media su tutti i campioni e la faccio pesare secondo la sua distribuzione di probabilità 
		![[Pasted image 20251023223934.png]]
	$$\text{rumore} = \int \int \{ h(x) - t \}^2 dx dt$$
	=> Errore irriducibile sempre presente 

+ I primi due parametri controllano la regolarizzazione (il bias) e il complessità del modello (la varianza) => se aumenta il bias diminuisce la complessità del modello e viceversa...
	
	6
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- Bassa complessità, implica **alto bias** e bassa varianza: (a destra c'è la media dei modelli)

	![[Pasted image 20250930120147.png]]
	
	7
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- **Rilassando il coefficiente di regolarizzazione**, si riduce il bias e aumenta la varianza:

	![[Pasted image 20250930120342.png]]

	8
---
**Regolarizzazione, bias e varianza**

- Bias e varianza dipendono dalla complessità del modello.
- Rilassando il coefficiente di regolarizzazione, si riduce il bias e aumenta la varianza:

	![[Pasted image 20250930120423.png]]

	=> Va sempre meglio? boh dipende dal numero di dati... se pochi si tende a overfittare troppi se tanti avere grossa regolarizzazione porta a scartarne tanti
	
	9
---
**Regolarizzazione, bias e varianza**

- Tutto questo è molto bello, **ma questi integrali sono completamente intrattabili.** => dovrei ogni volta calcolarli ==su tutto il dataset..==.
- Questi integrali sono medie su dataset, quindi dovremmo avere un **ensemble di dataset** indipendenti...
- Ed è quasi impossibile stimare in modo robusto bias e varianza.
- Vedremo metodi più pratici per stimare tradeoff empirici ottimali.

	![[Pasted image 20250930120608.png]]

	+Ho un punto ottimale dove cambiano le cose: 
		![[Pasted image 20251025230402.png]]  
	=> come trovarlo? boh prova via esperimenti

	10
---
## Regressione Lineare Bayesiana
---

- (Prima esempio coin flip => calcolo MLE da inserire => alla fine arrivo alla prob come numero di teste / numero di teste+croci ![[Pasted image 20251025230845.png]]
	Dopo un po' di passaggi... (si deriva è pone la derivata a zero)
	![[Pasted image 20251025231304.png]]

- Si considerano quindi 2 approcci:
	- Approccio frequentista => si assume che il Dataset sia generato da uno specifico (ma sconosciuto) $\theta$
	- Approccio Bayesiano => Assumi che $\theta$ sia preso da una distribuzione non conosciuta su $[0,1]$ (distribuzione parametrica) => a quel punto stima quella distribuzione => ==non abbiamo una singola risposta ma varie soluzioni che ci possono andare bene.==

- Sostanzialmente al posto di trovare la $\theta$ dato il campione di dati => vogliamo trovare la distribuzione dei dati, data la probabilità a priori $\theta$ => questo mi dà la possibilità di capire come il modello si ==adatta a particolari probabilità==

	![[Pasted image 20251025231437.png]]
	
- Vale per bayes quindi $$P(\theta|D) = \frac{P(D|\theta) P(\theta)}{P(D)}$$dove $P(D)= \int P(D,\theta) d \theta$ => difficile nel deep learning in quanto devo calcolare appunto su tutti i dati...
- Mi evito così di dover guardare ai parametri del modello... 
- Quale potrebbe essere la *prior*? la beta ha proprietà carine da vedere successivamente => ==*conjugate prior* per la binomiale== => invece di fare i prodotti faccio le somme su diversi dati => in pratica da una binomiale riottengo la beta da poter riapplicare 

	+Aggiungere passaggi sulla dimostrazione della proporzionalità 
	![[Pasted image 20251025232507.png]]	
	+Disegno sulla *Beta* => a seconda dei risultati ottengo certe prior => fino a che al limite perdo l'importanza della prior sul modello => se nell'approccio frequentista non ho una prior qui si... al limite la MLE solution è la stessa di quella dell'approccio bayesiano => ==ottengo una distribuzione prior che non mi dà nessuna informazione== 
	
---
**Non sono felice**

- Potremmo guardare questi risultati di regressione e, sebbene belli, concludere: Non sono felice.
- Perché potremmo non essere felici? Abbiamo sviluppato un insieme di strumenti matematici sofisticati per stimare funzioni dai dati. Che cosa vuoi di più?

	11
---
**Si tratta di fiducia**

- Tutto questo macchinario matematico sofisticato di massima verosimiglianza è fantastico, ma non ci aiuta veramente a capire quanto dovremmo credere in una particolare soluzione.
- In questo caso, la fiducia assume tutta una serie di significati utili:
  - La mia regressione restituisce un $\mathbf{w}_{ML}$ dai dati $D$. Fantastico, ==ma quanto è affidabile quel== $\mathbf{w}_{ML}$, davvero? Quanto credo che sia vicino al vero $\mathbf{w}^*$ che assumiamo abbia generato $D$.
  - Prevedo un $t$ su qualche nuovo input $\mathbf{x}'$ usando $t' = y(\mathbf{x}', \mathbf{w}_{ML})$. Fantastico, ma quanto credo in questo $t'$? Questa fiducia è costante in tutto lo spazio di input?
  - E se ho conoscenza a priori (cioè una credenza sulla mia distribuzione dei parametri $p(w)$) posso incorporarla nella mia stima di $w_{ML}$? (al momento no)
- L'ampia classe delle tecniche bayesiane ci dà **esattamente questi strumenti sfruttando verosimiglianza, prior ed evidenza.**

	12
---
**A volte si tratta anche di apprendimento sequenziale...**

- E se addestrassimo un modello usando dati $D_1$.
- Poi, domani, qualcuno ci rovescia addosso nuovi dati $D_2$.
- Cosa possiamo fare? Dobbiamo addestrare l'intero modello da zero usando $D = \bigcup_i D_i$? 

	=> Anche qui abbiamo un approccio sequenziale ma stavolta sulla prior....
	
	13
---
**La distribuzione dei parametri**

- Vogliamo quantificare la nostra fiducia **in un modello** specifico $w^*$ stimato da $D$. => usiamo la probabilità!
- Ricorda sempre la tua regola di Bayes: $$p(\mathbf{w} | t) = \frac{\text{verosimiglianza dei dati} \times \text{prior}}{\text{evidenza}}$$
- Abbiamo già derivato una **verosimiglianza** per i dati, **dato il modello**:$$p(t | \mathbf{w}, \beta) = \prod_{n=1}^{N} \mathcal{N}(t_n | \mathbf{w}^T \phi(x_n), \beta^{-1})$$
- Abbiamo bisogno di una distribuzione **prior** $p(\mathbf{w})$ che esprima la nostra credenza a priori sui valori probabili che $\mathbf{w}$ potrebbe assumere. => vogliamo scegliere ==quindi una prior che "reagisca" bene con la nostra likelihood==
- Nota la forma della verosimiglianza dei dati e che la moltiplicheremo con questo prior. 

	14
---
**La distribuzione dei parametri**

- Scegliamo il nostro prior prima di tutto in modo che sia un'aspettativa ragionevole.
- Per esempio, potremmo aspettarci che i nostri pesi siano *vicini* a zero, in media (non necessario ma aiuta con la modellazione => alcune volte si standardizzano i dati per farsi che siano in questo modo), **con una certa varianza attesa attorno a zero**.
- Scegliamo anche la forma del nostro prior in modo che "giochi bene" con la verosimiglianza: $$p(\mathbf{w} | \alpha) = \mathcal{N}(\mathbf{w}  | 0, \alpha^{-1}I)$$
- Questo è un *Prior Coniugato Gaussiano*, che significa semplicemente che quando lo moltiplichiamo con una verosimiglianza gaussiana, ==il posterior risultante è anche gaussiano:==$$p(\mathbf{w}  | t) = p(t | \mathbf{w} , \beta^{-1}) p(\mathbf{w}  | \alpha)$$$$= \mathcal{N}(\mathbf{w}  | m_N, S_N),$$	dove $$m_N = \beta S_N \Phi^T t$$	e $$S_N^{-1} = \alpha I + \beta \Phi^T \Phi$$	 => ottengo *multivariate gaussian*, in alcuni casi anche in più dimensioni

	15
---
**La distribuzione dei parametri**

- Mantenere tutto bello e gaussiano ha molti vantaggi – il log posterior è: $$\ln p(\mathbf{w} | t) = -\frac{\beta}{2} \sum_{n=1}^{N} \{ t_n - \mathbf{w} ^T \phi(x_n) \}^2 - \frac{\alpha}{2} \mathbf{w} ^T \mathbf{w}  + \text{const}$$ (il log di un prodotto è la somma dei log... in questo caso likelihood e prior tolte le costanti)
- Ti sembra familiare? => riottengo lo **squared error** e il termine regolarizzatore $||\mathbf{w}||^2$ => solo che aggiungo i termini probabilistici secondo $\alpha$ e $\beta$

	16
---
**La distribuzione dei parametri**

- Mantenere tutto bello e gaussiano ha molti vantaggi – il log posterior è: $$\ln p(w | t) = -\frac{\beta}{2} \sum_{n=1}^{N} \{t_n - w^T \phi(x_n)\}^2 - \frac{\alpha}{2} w^T w + const$$
- Massimizzare questo posterior produce la stessa soluzione del nostro **minimi quadrati regolarizzato** "normale" con $\lambda = \alpha / \beta!$ dove ricordiamo:
	- $\alpha$ rappresenta la precisione del prior
	- $\beta$ invece per la precisione sui dati (likelihood)

- Ma nota che abbiamo qualcosa intrinsecamente più potente qui.

- Abbiamo raggiunto alcuni dei nostri obiettivi:
  - Possiamo **quantificare la fiducia** in una soluzione $w^*$ (dovrebbe essere chiaro).
  - Possiamo anche **apprendere in modo incrementale** quando arrivano nuovi dati (probabilmente non così chiaro).
  => in fin dei conti la MAP (maximum a prior) estimation di $\mathbf{w}^*$ con $\mathcal{N}(w|0, \alpha \mathcal{I})$ prior è equivalente alla regolarizazzione secondo MLE (con least squares) => **massimizzare** il posterior equivale a **minimizzare** l'errore regolarizzato (e massimizzare la verosimiglianza dell'estimatore)
	=> La reg L2 è equivalente ad avere un prior gaussiano sui pesi di incertezza $\alpha$
	
- Diamo un'occhiata a un semplice esempio di adattamento di una linea...

	17
---
**La distribuzione dei parametri**

- Iniziamo senza dati... Quindi, ci rimane ==il posterior uguale al prior.==
- Quando iniziamo a osservare dati, usiamo la regola di Bayes per aggiornare la credenza.
	
	![[Pasted image 20250930124127.png]]
	=> parto da una likelihood nulla e solo una prior con uno spazio di dati => campiono quindi dalla prior ottenendo la nostra likelihood => a questo punto comincio a osservare i dati => data likelihood fra $w_0$ e $w_1$ => aggiorno la mia prior/posterior moltiplicando la prior per la likelihood => update della belief a seconda dei dati osservati e così via osservando altri dati...

	18
---
**La distribuzione dei parametri**

- Man mano che continuiamo a osservare dati, continuiamo a usare la regola di Bayes per aggiornare la credenza.
- Alla fine, la ==varianza si riduce== e ci stabilizziamo **su una stima posterior attorno alla soluzione ML.** => la posterior ci dice qualcosa sulla distribuzione dei nostri dati => si capisce dunque se possiamo essere confident dei nostri dati e fermarci oppure continuare con altre osservazioni

	![[Pasted image 20250930124230.png]]

	19
---
**Distribuzione predittiva**

- Nota che non abbiamo detto niente sulle previsioni dal nostro modello.
- Se produco un output $y(\mathbf{x}, \mathbf{w}^*)$, quanto "sono felice" con esso? Dipende da **x** in qualche modo?
- In pratica, non ci importerebbe meno del valore effettivo di **w**, vogliamo solo le previsioni! => e quanto ci posso credere in queste previsioni...

- Definiamo allora la **distribuzione predittiva** come: $$p(t | \mathbf{t}, \alpha, \beta) = \int p(t | \mathbf{w}, \beta) p(\mathbf{w} | \mathbf{t}, \alpha, \beta) d\mathbf{w}$$ => moltiplico per la posterior parameter density => how **likely** are this parameters => sostanzialmente dato ogni scelta dei parametri (e quindi della retta generata) la moltiplico per la probabilità di quanto siano probabili questi parametri dati i "parametri" considerati => ogni retta è pesata per la sua probabilità => passiamo da un unica soluzione puntuale ad un insieme di possibili soluzioni

- Il primo modo di guardare questo è **come una media (cioè aspettativa) di verosimiglianze condizionate**, dove l'aspettativa è rispetto al posterior (distribuzione dei parametri). => prediction su un insieme di modelli...
	=> notare ho due gaussiane => si fa la convoluzione di due gaussiane riottenendo una gaussiana
	
	20
---
**Distribuzione predittiva**

- Se scaviamo nella natura gaussiana di entrambe queste, e notiamo che la distribuzione predittiva è una *convoluzione* di due gaussiane, possiamo derivare una forma analitica: $$p(t | \mathbf{t}, \alpha, \beta) = \mathcal{N}(t | m_N^T \phi(\mathbf{x}), \sigma_N^2(\mathbf{x})),$$                                                     dove $\sigma_N^2(\mathbf{x}) = \frac{1}{\beta} + \phi(\mathbf{x})^T S_N \phi(\mathbf{x})$

- $1/\beta$ rappresenta il **rumore** nei nostri dati, e $\sigma_N^2$ rappresenta l'incertezza ==nella nostra stima dei parametri.== => adesso anche la varianza dipende dai nostri dati! (ricordo che $S_n$ rappresenta l'informazione che ho dai dati) => si misura quindi quanto vale la varianza nella nostra stima dei parametri

- Nota anche che $\sigma_{N+1}^2(x) < \sigma_N^2(x)$, quindi più dati sono sempre una cosa buona.

	21
---
**Distribuzione predittiva**

- Ora stiamo davvero dicendo qualcosa di utile sugli output del modello: (in rosso la curva predittiva)
	![[Pasted image 20250930143351.png]]

	=> Posso dire dove sono abbastanza confident o meno della mia previsione => a seconda di dove ho il mio support => sostanzialmente più dati ho e più sono confident => dunque restiringo la zona di supporto => meno confidenza ho è più sarà ampia la zona di supporto => zona di supporto data come intervalli di confidenza +/- 2 deviazioni?
	
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

- E sulla varianza del modello (campionando dalla posterior su w):
	![[Pasted image 20250930143632.png]]

- *Il miglior regolarizzatore sono sempre più dati annotati.*
	*- Geoffrey Hinton (probabilmente).*

	=> Aumentando il numero di dati diminuisco l'incertezza sulla prior/posterior e dunque tendo verso un modello frequentista con prior nulla!
	
	25
---
## Osservazioni conclusive
---
**Regressione lineare in tre atti**

- Abbiamo visto (almeno) tre visioni della regressione lineare:
   - La visione puramente geometrica; => disegno retta più vicina ai punti
   - La visione di Massima Verosimiglianza;  => disegno retta con parametri più probabili secondo i dati
   - La visione Bayesiana. => aggiorno le mie credenze secondo i dati ricevuti

- Questo sfiora appena la superficie di ciò che è possibile, ma è una buona fondazione.
- Interessante, le soluzioni per tutte e tre le visioni sono identiche.
- Ognuna ha, tuttavia, diversi vantaggi e svantaggi: una stima puntuale è efficiente, mentre l'inferenza bayesiana completa ha più funzionalità. => arrivo a distribuzioni complete (se ci arrivo)
- Importante: ==il trattamento bayesiano completo è possibile in forma analitica solo a causa delle scelte che abbiamo fatto sul prior sui pesi e sul rumore delle osservazioni.==

	26
---
**La strada da percorrere**

- Prossimo volgeremo la nostra attenzione ai modelli lineari per la classificazione.
- Ancora, inizieremo con un modello geometrico di funzioni discriminanti.
- Poi procederemo ad applicare ragionamento probabilistico e bayesiano sulla base della nostra intuizione.
- Sebbene i modelli lineari siano semplici, sono anche spesso molto efficaci e la loro semplice formulazione ammette inferenza **semplice e robusta**.
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

## Introduzione
---
**Classificazione e superfici decisionali**

- L'obiettivo della classificazione è prendere un vettore di input $\mathbf{x}$ e ==assegnarlo a una delle $K$ classi.==
- Denotiamo queste classi come $C_k$ per $k \in \{1, \ldots, K\}$. => *multi-class* oppure *single label classification*
- L'ambiente più semplice è la classificazione a singola etichetta dove ogni $\mathbf{x}$ appartiene esattamente a una classe.
- Così lo spazio di input è diviso in **regioni decisionali** i cui confini sono chiamati *bordi decisionali o superfici decisionali.*
- Considereremo prima modelli lineari dove queste superfici decisionali sono funzioni lineari dell'input $\mathbf{x}$.
- Dati le cui classi ==possono essere separate== esattamente con superfici decisionali lineari sono chiamati **linearmente separabili**. => esistono classi in cui non è assolutamente possibili separabili le classi in modo lineare => che fare? usare sempre rette oppure modelli più complessi? 
	
	![[Pasted image 20251025001614.png]]
	
	2
---
**Obiettivi della lezione**

Alla fine di questa lezione avrete:

- Compreso la **geometria** delle funzioni discriminanti lineari e come interpretarle. => inner product of vectors
- Compreso come applicare i **minimi quadrati** per stimare i parametri di modelli discriminanti lineari.
- Compreso le limitazioni dei minimi quadrati per l'adattamento di modelli di classificazione.
- Compreso come il *Discriminante Lineare di Fisher* affronta alcune delle carenze dei minimi quadrati trovando una direzione "migliore" per la discriminazione.

	3
---
## Funzioni Discriminanti Lineari
---
**Funzioni discriminanti per due classi**

- La rappresentazione più semplice per un **discriminante** è una funzione lineare:$$y(\mathbf{x}) = \mathbf{w}^Tx + \mathbf{w}_0$$
- Ancora, $\mathbf{w}$ è il vettore dei pesi e $w_0$ è un *bias* **scalare**.
- Per la classificazione, il bias negativo è a volte chiamato soglia.
- La regola decisionale: $$\text{classe}(\mathbf{x}) = \begin{cases} C_1 & \text{se } \mathbf{w}^T\mathbf{x} + \mathbf{w}_0 \geq 0 \\ C_2 & \text{se } \mathbf{w}^T\mathbf{x} + \mathbf{w}_0 < 0 \end{cases}$$ ovvero:$$\text{classe}(\mathbf{x}) = \begin{cases} C_1 & \text{se } \mathbf{w}^T\mathbf{x} \geq - w_0  \\ C_2 & \text{se } \mathbf{w}^T\mathbf{x}   < - w_0 \end{cases}$$=> creo due regioni di spazio a seconda dei valori => al confine che succede? non si sà => "we just flip a coin"

- Notare passo da dimensione 2 a una singola dimensione => il prodotto scalare restituisce appunto uno scalare! 
	![[Pasted image 20251025163237.png]]Il bias può appunto spostarsi rispetto all'origine
		
- La **distanza normale** dall'origine alla superficie decisionale è:$$\frac{\mathbf{w}^T\mathbf{x}}{||\mathbf{w}||} = -\frac{w_0}{||\mathbf{w}||}$$ => normata in quanto **non ci interessa la norma di w**	
	
	4
---
**La geometria dei discriminanti lineari**

- Questa è la grafica a cui penso quando voglio ricordare come funziona la geometria del discriminante lineare:

	![[Pasted image 20251001223839.png]]
=> Partiamo guardando il vettore **w** => questo risulta perpendicolare al *decision boundary* => se prendiamo due punti $x_a$ e $x_b$ avremmo: $$\mathbf{w}^T\mathbf{x_a} = \mathbf{w}^T\mathbf{x_b} = 0$$ $$\mathbf{w}^T(\mathbf{x_a} - \mathbf{x_b}) = 0$$=> dunque $\mathbf{w}^T$ risulta perpendicolare alla *decision surface*  
	![[Pasted image 20251025164144.png]]
	
- Ci chiediamo poi quanto risulta distante **x** dalla nostra *decision surface* => faccio di nuovo prodotto scalare sulla direzione di **w** => vorremo però che questa distanza sia indipendente dalle norme dei vettori => farò quindi la normalizzazione per $||\mathbf{w}||$  
- Lunghezza che sarà complessiva dall'origine => dunque per ottenere solo la distanza tolgo il mio $w_0$ che è appunto la ==traslazione del piano dall'origine.==

	5
---
**Incorporare il bias nella base**

- Come con la regressione, a volte è conveniente usare una notazione compatta.
- Quindi, introduciamo una dimensione fittizia $x_0 = 1$ e definiamo:
						$\tilde{\mathbf{w}} = [w_0, \mathbf{w}]^T$
					
						$\tilde{x} = [x_0 = 1, \mathbf{x}]^T$
					
	così che                             $y(\mathbf{x}) = \tilde{\mathbf{w}}^T \tilde{\mathbf{x}}$ => embedding

- Quindi le superfici decisionali in questo spazio sono ==iperpiani $D$ dimensional== passanti per l'origine dello spazio (non ho più il bias) aumentato $D + 1$ dimensionale.  => non solo conveniente per la notazione ma anche per le computazioni

	6
---
**Classi multiple**

- OK, ma i problemi a due classi sono davvero noiosi. E se ne abbiamo di più?
- Potremmo usare $K - 1$ classificatori, ognuno risolvendo un problema a due classi separando una classe $C_k$ dai punti non in quella classe.
- Questo è noto come classificatore *one-versus-rest*(ovr): => tengo un esempio come quello della mia classe mentre il resto degli esempi è delle altre

	![[Pasted image 20251001224446.png]] => La zona verde prende i casi sia di classe C1 che classe C2... 

	7
---
**Classi multiple**

- Torniamo alla lavagna... Usa $K(K-1)/2$ funzioni discriminanti binarie. => one-versus-one => una classe "contro" un altra 
- Una per ogni **coppia** di classi:

	![[Pasted image 20251001224540.png]]
	=> in questa regione dovremmo classificare $C_1$ e $C_2$ e $C_3$  => potremmo incastrarci in zone ambigue => vorremmo ridurre questa regione ad un singolo punto.

	8
---
**Classi multiple**

- Possiamo evitare tutti questi problemi se usiamo un **singolo** discriminante **a K classi** impiegando $k$ funzioni lineari:$$y_k(\mathbf{x}) = \mathbf{w}_k^T \mathbf{x} + w_{k0}$$
- Che possiamo anche impacchettare insieme in una ==singola moltiplicazione di matrici==:

	![[Pasted image 20251025170619.png]]
	=> nel prodotto ottengo le varie $y_k(\mathbf{x})$
	
	![[Pasted image 20251025170741.png]]

- Ora assegniamo semplicemente $\mathbf{x}$ alla classe $C_k$ se $y_k(\mathbf{x}) \geq y_j(\mathbf{x})$ per tutti $j \neq k$. => sostanzialmente vado alla ricerca di $\text{argmax}_k \ y_k(\mathbf{x})$ => ovvero della superficie che massimizza

	9
---
**Bordi decisionali per classi multiple**

- Poiché stiamo prendendo un max **su funzioni lineari**, abbiamo regioni decisionali semplicemente connesse e **convesse**:

	![[Pasted image 20251001225538.png]]
	=> presi qualsiasi due punti sulla retta che traccio $y_k(\hat{\mathbf{x}})$ **rimane il massimo** => in particolare ==ho un solo valore massimo per ogni regione== => tranne nei punti di incontro delle regioni => lì ho ancora ambiguità su quale sia il valore massimo
	
	![[Pasted image 20251025171828.png]]
	=> Per risolvere quindi i casi di classificazione negativa rispetto alle 3 regioni => diremo semplicemente che assocerò il punto alla classe che risulta con ==distanza negativa minore.== => risulterà come la più vicina alla classe. 
	
	10
---
## Minimi Quadrati per la Classificazione
---
**Un modello lineare compatto**

- Per la regressione, i modelli lineari con una misura di errore ai minimi quadrati hanno portato a una semplice soluzione **in forma chiusa**.
- Quindi, vediamo se possiamo riuscire a fare lo stesso trucco qui.
- Ogni classe è descritta dal proprio modello lineare:$$y_{k}(\mathbf{x}) = \mathbf{w}_{k}^{T}\mathbf{x} + w_{k0}$$
- O, ancora meglio:$$y(\mathbf{x}) = \tilde{W}^{T}\tilde{\mathbf{x}}$$
- È utile pensare a cosa sono le **colonne** di $\tilde{W}$
- Inoltre, quali dovrebbero essere i nostri **target** per la classificazione? 

	![[Pasted image 20251025175928.png]]

	=> parto da una y dove per colonna mi dice ==l'esempio a quale classe appartiene==. => il prodotto fra "W^T" e "x" mi restituisce dunque il risultato del classificatore => ogni campione avrà un **solo risultato positivo** o un solo risultato negativo

	11
---
**Una soluzione analitica**

- Risolviamo per $\tilde{W}$ minimizzando l'errore per la somma dei quadrati.
- 
- Considera un training set $\{x_n, t_n\}$ per $n \in \{1, \ldots, N\}$.
- E definisci una matrice $T$  la cui riga $n^{esima}$ è $t_n^T$. (vedi sketch di sopra)
- Insieme a una corrispondente matrice $\tilde{X}$ la cui riga $n^{esima}$ è $\tilde{x}_n^T$.
	![[Pasted image 20251025180544.png]]
	
- Possiamo allora scrivere la funzione di errore come:$$E(\tilde{W}) = \frac{1}{2}Tr\left\{(\tilde{X}\tilde{W} - T)^T(\tilde{X}\tilde{W} - T)\right\}$$ (Tr era la traccia della matrice) $$E(\tilde{W}) = \sum_{n=1}^N \sum_{k=1}^K (\tilde{W}^T \tilde{x}_n - t_n)^2_k$$ => che è appunto la somma dei quadrati degli errori.

- Impostando il gradiente rispetto a $\tilde{W}$ a zero e risolvendo, arriviamo a:$$\tilde{W} = (\tilde{X}^T\tilde{X})^{-1}\tilde{X}^TT = \tilde{X}^{\dagger}T$$
	12
---
**Una soluzione analitica**

- Quindi abbiamo una bella forma analitica per un **classificatore a K classi** da dati:$$y(x) = \tilde{W}^T \tilde{x} = T^T (\tilde{X}^{\dagger})^T \tilde{x}$$
- Tuttavia, non è un classificatore molto buono: => highly sensed agli outliers... cerco di classificare correttamente gli esempi outlier che mi portano a modificare il discriminante...

	![[Pasted image 20251001230826.png]]

- Da qui un primo problema => **Least squares** sta facendo assunzione implicite => tipo ==non ci sono outliers== e noise di tipo gaussiano sui dati...
- Un altro problema sono però gli *hard targets*: classifico in modo diretto solo come 0 o 1

	13
---
## Discriminante Lineare di Fisher
---
**Classificazione lineare come riduzione di dimensionalità**

- Un modo di pensare alla **classificazione lineare** con discriminanti è come una riduzione di dimensionalità a **una** dimensione. => che direzione prendere con w? => **come capisco quale w divide al meglio i punti**? Andiamo a guardare una w che separa al meglio i *centroidi* dei nostri punti.
	![[Pasted image 20251025185224.png]]
	
- Diamo un'occhiata ad alcuni esempi motivanti di questo...

	14
---
**Separare le medie**

- La nostra prima strategia potrebbe essere di calcolare le **medie** di ogni classe nello spazio delle feature:$$\mathbf{m}_1 = \frac{1}{N_1} \sum_{n=1}^{N_1} x_{1,n}, \quad \mathbf{m}_2 = \frac{1}{N_2} \sum_{n=1}^{N_2} x_{2,n}$$
- E poi calcolare $\mathbf{w}$ in modo che la proiezione di questi due punti su di esso **massimizzi** la distanza tra le proiezioni: $$\mathbf{w}^T \mathbf{m}_2 - \mathbf{w}^T \mathbf{m}_1 = \mathbf{w}^T (\mathbf{m}_2 - \mathbf{m}_1)$$ (per trovare il nostro piano che massimizzi la distanza fra i centroidi)

- Qualcuno vede un problema nel **massimizzare** questa espressione? => può andare all'infinito anche così...  devo limitare la norma altrimenti non ho soluzioni => non arrivo mai ad un massimo! => mi basta portare la norma all'infinito per avere una soluzione maggiore

	15
---
**Separare le medie**

- La nostra prima strategia potrebbe essere di calcolare le medie di ogni classe nello spazio delle feature:$$m_1 = \frac{1}{N_1} \sum_{n=1}^{N_1} x_{1,n}, \quad m_2 = \frac{1}{N_2} \sum_{n=1}^{N_2} x_{2,n}$$
- E poi calcolare $\mathbf{w}$ in modo che la **proiezione** di questi due punti su di esso massimizzi **la distanza** tra le proiezioni:$$\mathbf{w}^T m_2 - \mathbf{w}^T m_1 = \mathbf{w}^T (m_2 - m_1)$$
- Qualcuno vede un problema nel massimizzare questa espressione?
- Possiamo imporre il **vincolo** che $||w||_2 = 1$ nell'ottimizzazione (usando un moltiplicatore di Lagrange).
- Il risultato è, non a sorpresa: $w \propto (m_2 - m_1)$

	16
---
**Separare le medie**

- Va bene? Cosa non funziona?

	![[Pasted image 20251001231132.png]]
	=> Questo perchè non si considera la forma delle distribuzioni! => si cercano quelle che direzioni che mantengono più compatte (quindi abbassano) la varianza delle classi
	
	17
---
**Tenere conto dell'anisotropia**

- Entrambe le distribuzioni di classe hanno matrici di covarianza fortemente non diagonali.
- L'intuizione di Fisher era di:
	- **massimizzare** la varianza *inter-classe*, => ovvero la distanza fra le medie fra classi
	- mentre simultaneamente **minimizzava** la varianza *intra-classe* nello spazio proiettato, 1-dimensionale. => ovvero la varianza dentro ogni classe.

- La varianza within-class – anche chiamata **compattezza** – è:$$s_k^2 = \sum_{n=1}^{N_k} (\mathbf{w}^T \mathbf{x}_{k,n} - \mathbf{w}^T m_k)^2$$ => misuro nello spazio proiettato (ovvero i punti sulla mia **w**) quanto risulta mia distanza e ne prendo il quadrato

- Il Criterio di Fisher è allora il rapporto tra la varianza **between-class** e la varianza **within-class**:$$J(\mathbf{w}) = \frac{(\mathbf{w}^T m_2 - \mathbf{w}^T m_1)^2}{s_1^2 + s_2^2}$$
	=> Sostanzialmente oltre alla direzione che massimizza la distanza fra le medie delle due classi si cerca l'angolazione da cui i due gruppi appiano più compatti e quindi più separati => con minor sovrapposizione!
	
	18
---
**Generalizzando** (skipped)

- Possiamo rendere between e within più espliciti scrivendo:$$J(w) = \frac{w^T S_B w}{w^T S_W w} \quad (\text{vedi Eq 4.27 e 4.28 in Bishop})$$
- Dove qui $S_B$ è la **covarianza** between-class, e $S_W$ è la within-class.

- Dopo aver differenziato e manipolato i termini, troviamo:$$(w^T S_B w) S_W w = (w^T S_W w) S_B w$$
- Non ci interessa (per ora) la scala di $w$, quindi dopo aver eliminato i fattori scalari e moltiplicato per $S_W^{-1}$:$$w \propto S_W^{-1}(m_2 - m_1)$$
	19
---
**Discriminante Lineare di Fisher per due classi**

- Che funziona molto meglio:

	![[Pasted image 20251001231407.png]]

	20
---
**Relazione con i minimi quadrati** (boh si possono fare anche con i quadrati ma skipped also)

- L'approccio dei minimi quadrati alla classificazione basata su discriminanti lineari si basa sull'apprendere funzioni lineari che siano il più **vicine** possibile all'insieme dei valori target.
- Il Criterio di Fisher, invece, cerca di massimizzare ==la separazione delle classi== nello spazio discriminante.

- Per il problema a due classi, possiamo mostrare che il discriminante di Fisher è in realtà un caso speciale del vecchio minimi quadrati.
- Invece di usare un target di 1 per le probabilità target one-hot, useremo:$$t_n = \begin{cases} \frac{N}{N_1} & \text{se } x_n \in C_1 \\ -\frac{N}{N_2} & \text{se } x_n \in C_2 \end{cases}$$
- Questa è una stima del prior reciproco per ogni classe.

	21
---
**Relazione con i minimi quadrati**

- Il nostro errore è ancora minimi quadrati:$$E = \frac{1}{2} \sum_{n=1}^{N} (\mathbf{w}^T \mathbf{x}_n + w_0 - t_n)^2$$
- Impostando i gradienti a zero rispetto a $w_0$ e $w$:$$\sum_{n=1}^{N} (\mathbf{w}^T \mathbf{x}_n + w_0 - t_n)= 0$$$$\sum_{n=1}^{N} (\mathbf{w}^T \mathbf{x}_n + w_0 - t_n)\mathbf{x}_n = 0$$
	22
---
**Relazione con i minimi quadrati**

- Risolvendo, troviamo (usando liberamente l'espressione per i nuovi target):$$w_0 = -\frac{\mathbf{w}^T (N_1 m_1 + N_2 m_2)}{N}$$
- E per la direzione:$$\mathbf{w} \propto S^{-1}_W (m_2 - m_1)$$
	23
---
## Osservazioni Conclusive
---
**Discriminanti lineari**

- In questa introduzione abbiamo guardato i discriminanti lineari per la classificazione supervisionata.
- Questi approcci sono approssimativamente equivalenti agli approcci geometrici per la regressione lineare.
- In realtà, sono più simili alle soluzioni di **massima verosimiglianza per la regressione**, ma dobbiamo ancora aggiungere un'interpretazione probabilistica.
- È importante avere una sensazione per la **geometria** dei discriminanti lineari.
	- Proiettiamo gli **input** sui pesi del modello $\mathbf{w}$.
	- Questo vettore dei pesi $\mathbf{w}$ è ==perpendicolare alla superficie discriminante==.
	- Un discriminante lineare riduce implicitamente a un problema di soglia **unidimensionale**.

	24
---
**I minimi quadrati fanno schifo come classificatore**

- La classificazione con **minimi quadrati** ha svantaggi significativi => decent superfici di separazioni – ma ha notevolmente sensibilità agli outlier.
- Come vedremo, stiamo implicitamente facendo assunzioni sulla **forma delle distribuzioni di classe** quando usiamo i minimi quadrati.
- Ciononostante, manteniamo ancora la soluzione in **forma chiusa** analitica offerta dai minimi quadrati.

	25
---
**Discriminante Lineare di Fisher**

- Se ruotiamo lo spazio in modo da massimizzare certe proprietà delle proiezioni di classe, possiamo fare meglio.
- Questo è ciò che fa il Criterio di Fisher: -
	- **massimizzare** la varianza *between-class* => le medie delle classi
	- mentre **minimizza** la varianza *within-class*. => le varianze delle classi stesse
	=> Ci dà un modo di valutare le diverse direzioni!

- Fare questo ==migliora significativamente le performance di classificazione lineare.==
- Ma, mantiene ancora le belle proprietà analitiche dei minimi quadrati.

	26
---
**La strada da percorrere**

- Seguendo il nostro sviluppo per la regressione, nella prossima lezione daremo un'occhiata ai modelli **probabilistici** per la classificazione.
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
# 6 - Modelli Lineari per la classificazione - Modelli probabilistici

Recup di quanto visto per ora:
- Regressione Lineare base => $\phi(\mathbf{x}) = \mathbf{x}$ e $R(\mathbf{w}) = 0$
- Regressione Lineare polinomiale => $\phi(\mathbf{x}) = [1 \space \mathbf{x} \space \mathbf{x^2}]^T$ e $R(\mathbf{w}) = 0$
- Regressione Lineare Ridge => $\phi(\mathbf{x}) = \mathbf{x}$ e $R(\mathbf{w}) = ||\mathbf{w}||_2^2$
- Least Squares => Si usa la regressione lineare per fare classificazione.
## Introduzione
---
**Approcci probabilistici alla classificazione**

- Nella scorsa lezione abbiamo esaminato i modelli lineari per la classificazione da una prospettiva puramente geometrica.
- Come la regressione ai minimi quadrati, questi ==mancano della capacità di quantificare la fiducia nelle loro previsioni.==
- In questa lezione esamineremo la classificazione lineare da tre prospettive probabilistiche:
  - **Generativa**: in cui una **verosimiglianza** dei dati ==condizionata alla classe== e dei ==prior sulle classi== verranno utilizzati per derivare una regola di classificazione.
  - **Discriminativa**: in cui la **distribuzione posteriori** delle classi viene stimata **direttamente**.
  - **Bayesiana**: in cui approssimiamo la **distribuzione dei parametri** dalla verosimiglianza dei dati e dal **prior** e poi **integriamo** per fare previsioni.

	2
---
**Obiettivi della lezione**

Alla fine di questa lezione:

- Comprenderete l'**approccio generativo** alla classificazione e come i discriminanti lineari e quadratici derivino da assunzioni sulle verosimiglianze condizionate alla classe.
- Comprenderete l'**approccio discriminativo** della *regressione logistica* (porta a questa) alla classificazione e come la loss di *log-verosimiglianza negativa* possa essere utilizzata per addestrarlo.
- Comprenderete le basi (e i limiti) dell'approccio bayesiano alla classificazione e perché sia necessaria l'inferenza approssimata.

	3
---
## Modelli Probabilistici Generativi
---
**Ancora, dove sono le probabilità?!**

- Ancora una volta, ci troviamo con un bel modello, ma completamente incapace di fornire una qualsiasi **misura di fiducia**.
- Considereremo ora un tipo specifico di visione **generativa** che porterà naturalmente (tramite la regola di Bayes) proprio a una tale misura.
- Come abbiamo visto per i modelli di regressione lineare, troveremo anche connessioni tra le visioni probabilistica e geometrica.

	4
---
**Un modello generativo** 

- Per problemi a $K = 2$ classi, possiamo scrivere il **posterior per la classe** $C_1$ come (da bayes): $$p(C_1 | \mathbf{x}) = \frac{p(\mathbf{x} | C_1)p(C_1)}{p(\mathbf{x} | C_1)p(C_1) + p(\mathbf{x} | C_2)p(C_2)} = \frac{1}{1 + \exp(-a(\mathbf{x}))} \equiv \sigma(a(x))$$(sotto ho $p(\mathbf{x}) = \sum_{i=1}^{C_n} p(\mathbf{x, C_i}$)
per $$a(\mathbf{x}) = \ln{\frac{p(\mathbf{x} | C_1)p(C_1)}{p(\mathbf{x} | C_2)p(C_2)}}$$ => detta *log posterior ratio*

- Scrivere il posterior in questo modo potrebbe sembrare una perdita di tempo.
- Tuttavia, vedremo che questo aiuta a generalizzare i nostri risultati, specialmente quando $a(\mathbf{x})$ ha una forma semplice.

	5
---
$\sigma$, un vecchio amico

- La funzione $\sigma(\cdot)$ è nota come funzione **sigmoide logistica**. $$\sigma(x)=\frac{1}{1+e^{-x}}$$
- Svolge un ruolo importante in molti modelli di classificazione.
- È molto importante per le Reti Neurali Artificiali.

	![[Pasted image 20251011193638.png]]

	6
---
**Problemi a K classi**

- Per il caso di $K > 2$: $$p(C_k | x) = \frac{p(x | C_k) p(C_k)}{\sum_j p(x | C_j) p(C_j)} = \frac{\exp(a_k)}{\sum_j \exp(a_j)}$$ dove $a_k$ è sempre la nostra log posterior probability di $C_k$ 
- Questo è noto come *esponenziale normalizzato* o **funzione softmax**. => sopra ho una log posterior probability della classe $C_k$ 
- Vediamo cosa succede per una scelta specifica di $a_k$.

	7
---
**Modelli generativi con input continui**

- Possiamo assumere che le densità condizionate alla classe (un altro nome per la verosimiglianza) siano **Gaussiane** con **matrici di covarianza uguali**:

- Quindi, la **densità** per la classe $C_k$ è: $$p(x | C_k) = \frac{1}{(2\pi)^{D/2}|\Sigma|^{-1}} \exp\left\{-\frac{1}{2}(x - \mu_k)^T\Sigma^{-1}(x - \mu_k)\right\}$$ => per ogni classe ho ==una particolare media== => ma la **covarianza** rimane la stessa (notare non ha il pedice per la classe)

	![[Pasted image 20251026180920.png]]

- Se consideriamo **solo la prima classe**, e ricordando l'analisi che abbiamo fatto sulla forma del posterior, abbiamo:$$p(C_1 | \mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0) = \sigma(a(\mathbf{x}))$$dove $\mathbf{w} = \Sigma^{-1}(\mu_1 - \mu_2)$ e $w_0 = -\frac{1}{2}\mu_1^T\Sigma^{-1}\mu_1 + \frac{1}{2}\mu_2^T\Sigma^{-1}\mu_2 + \ln\frac{p(C_1)}{p(C_2)}$
	(tutto questo ottenuto valutando $p(C_1|x)$ con il log posterior ratio tramite gaussiane)

	+Se vuoi rifare i passaggi guarda sketch su slides 

	8
---
**Modelli generativi con input continui**

- I termini quadratici in $\mathbf{x}$ si sono cancellati (a causa del $\Sigma$ comune).
- Le frontiere di decisione(boundaries) **sono lineari** nello spazio di input.

	![[Pasted image 20251011194038.png]]
	A sinistra ho appunto $P(C_1|\mathbf{x})$ combined con $P(C_2|\mathbf{x})$  => ottengo una frontiera di decisione lineare! => dipendente unicamente dalle due medie

+ Prendendo una direzione perpendicolare alla superficie di separazione e proiettando i punti di una della due classi, cosa otteniamo? esattamente la sigmoide!

	![[Pasted image 20251026182151.png]]
	
- A seconda delle probabilità delle due classi il boundary sarà spostato verso una delle classi => nel caso invece di $P(C_1) = P(C_2) = 0.5$ (caso non informativo) alla il boundary sarà esattamente a metà => si può dunque modificare queste probabilità come una sorta di iperparametro in modo tale da avere particolari boundary

	9
---
**Modelli generativi con input continui**

- Per il caso generale di K classi, usiamo il **softmax** invece della sigmoide.
- Abbiamo:$$a_k(\mathbf{x}) = \mathbf{w}_k^T \mathbf{x} + w_{k0}$$dove $\mathbf{w_k} = \sum^{-1} \mu_k$ e $w_{k0} = \frac{1}{2} \mu_k^T \sum^{-1} \mu_k + \ln p(C_k)$ (questo per ogni classe k)

- Le frontiere di decisione risultanti sono dove due dei posteriori sono uguali.
- Questo corrisponde al tasso di errata classificazione minimo (ancora una funzione lineare di $x$).

+ Ma perchè si parla di modello generativo? 

	![[Pasted image 20251026182554.png]]
	+ I Dati sono generati da un processo generativo (Dirichlet process) => per fare il passaggio successivo dal dataset stimo quindi le **medie** (come centroidi) e la **Covarianza** (per ottenerne una faccio la trasposizione all'origine), dunque le prior delle classi e a quel punto ho tutti i miei strumenti per generare il mio modello

	10
---
**Modelli generativi con input continui**

- Se rilassiamo il requisito che tutte le matrici di covarianza siano uguali(non sempre si può fare quest'ipotesi), ==i termini quadratici non si cancellano più==. 

	 ![[Pasted image 20251026183608.png]]
- Il risultato è un classificatore di Bayes **quadratico**. ( e non più lineare)

	![[Pasted image 20251011194251.png]]

	11
---
## Modelli Probabilistici Discriminativi
---
**Generative versus discriminative**

- Abbiamo visto che la probabilità posterior in un problema a 2 classi può essere scritta come una **sigmoide** logistica di ==**una funzione lineare** di **x**.==
- Analogamente, per il caso multi-classe abbiamo una funzione **softmax** su una funzione lineare di **x**.
- Questi sono esempi di quelli che sono noti come modelli lineari generalizzati.
- Per scelte specifiche delle distribuzioni condizionate alla classe possiamo **usare la massima verosimiglianza** per stimare i loro parametri (e quelli dei prior).
- Questi sono a volte chiamati modelli generativi, perché potremmo generare campioni **x** campionando dal **marginale** $p(x)$. ?
- E se, invece, usassimo **direttamente la forma funzionale** del modello lineare generalizzato per discriminare? => saltiamo direttamente alla distribuzione di x date le classi. => stimo direttamente il valore di $P(C_1|\mathbf{x})$

	12
---
**Funzioni di base fisse**

- Abbiamo sviluppato tutti i classificatori per lavorare direttamente sull'input originale $\mathbf{x}$. => che succede se i dati ==non sono linearmente separabili==? => dove metterò il mio treshold??

- Tuttavia, tutto ciò che abbiamo derivato funziona ugualmente bene se usiamo un vettore di funzioni di base $\phi(x)$.  => provo ad usare polinomi 

	![[Pasted image 20251026184832.png]] 
	=> dati diventano separabili!  => questo è chiamato un *explicit embedding* (lo stesso dello functional basis mapping)

- Le frontiere risultanti sono lineari nello spazio delle feature $\phi$, ma ==non lineari nello spazio originale== => parto da un original input space non lineare ==ma arrivo comunque a frontiere lineari==! => giustamente parto da dati non separabili linearmente ma almeno arrivo frontiere lineari!

	![[Pasted image 20251011194425.png]]

	13
---
**Regressione logistica**

- Abbiamo appena visto che possiamo scrivere il **posterior** per un problema a 2 classi come: $$p(C_1 | \phi) = \sigma(\mathbf{w}^T\phi)$$
- Questo è chiamato (in modo confusionario) un modello di **regressione logistica**.
- Per uno spazio delle feature $M$-dimensionale, questo modello ha **M parametri** => ==tanti quanti la dimensione delle funzioni base==. 
- Il modello generativo richiederebbe $2M$ parametri per le medie, più $M(M+1)/2$ parametri per la matrice di covarianza. => se ho un problema a grandi dimensioni potrei avere problemi! => approccio da non seguire...

- Possiamo usare la **Massima Verosimiglianza** per adattare i parametri di questo modello, grazie alla forma conveniente della derivata della sigmoide logistica:$$\frac{d}{da}\sigma(a) = \sigma(a)(1 - \sigma(a))$$
	14
---
**Regressione logistica**

- Per il dataset $D = \{\phi_n, t_n\}$ (assumo che sia i.i.d), dove $t_n \in \{0, 1\}$ e $\phi_n = \phi(x_n)$, la verosimiglianza è: $$p(\mathbf{t} | \mathbf{w}) = \prod_{n=1}^{N} y_n^{t_n} \{1 - y_n\}^{1 - t_n}$$dove $\mathbf{t} = (t_1, t_2, \ldots t_N)^T$ e $y_n = p(C_1 | \phi_n) = \sigma(\mathbf{w}^T \phi_n)$ => output del modello per parametri **w**
- Dunque se appartiene alla classe uno vorremo che $y_n$ sia parecchio alta, viceversa bassa per spingere $1 -y_n$ per darlo alle altre classi

- Per la nostra funzione di errore useremo la **Log-verosimiglianza Negativa** (o binary cross-entropy Loss):  => prodotti diventano somme:$$E(\mathbf{w}) = -\ln p(\mathbf{t} | \mathbf{w}) = -\sum_{n=1}^{N} \{t_n \ln y_n + (1 - t_n) \ln(1 - y_n)\}$$ => tramite log passo a ==somma di termini== => $t_n$ vengono usati come switches per i termini.

	15
---
**Regressione logistica**

- Scrivendo la funzione di errore in questo modo: $$E(\mathbf{w}) = -\sum_{n=1}^{N} \{ t_n \ln y_n + (1 - t_n) \ln (1 - y_n) \}$$
- E ricordando che $y_n = \sigma (\mathbf{w}^T \phi_n)$.
- E usando la nostra osservazione sulla derivata della sigmoide logistica:$$\frac{d}{da} \sigma (a) = \sigma (a)(1 - \sigma (a))$$
- Ci permette di vedere più esplicitamente la connessione tra verosimiglianza e pesi $\mathbf{w}$$$\nabla_{\mathbf{w}} E(\mathbf{w}) = \sum_{n=1}^{N} (y_n - t_n) \phi_n$$=> $\nabla_{\mathbf{w}} E(\mathbf{w}) =-\nabla_{\mathbf{w}}\sum_{n=1}^{N} \{ t_n \ln y_n + (1 - t_n) \ln (1 - y_n) \} =$ 
		$-\nabla_{\mathbf{w}}\sum_{n=1}^{N} \{ t_n \ln \sigma(\mathbf{w}^T\phi_n) + (1 - t_n) \ln (1 - \sigma(\mathbf{w}^T\phi_n) \} =$
		$\sum_{n=1}^{N} [ t_n \frac{1}{\sigma(\mathbf{w}^T\phi_n)}\sigma(\mathbf{w}^T\phi_n)(1- \sigma(\mathbf{w}^T\phi_n))(-\phi_n)$ $+ (1 - t_n) \frac{1}{\sigma(\mathbf{w}^T\phi_n)}\sigma(\mathbf{w}^T\phi_n)(1- \sigma(\mathbf{w}^T\phi_n))(\phi_n)]=$ $\sum_{n=1}^{N}\phi_n[y_n - t_ny_n-t_n+t_ny_n] = \sum_{n=1}^{N}\phi_n[y_n -t_n]$

	=> Riottengo una **combinazione lineare** delle funzioni base! => vale infatti: $$y_n - t_n = \sigma (\mathbf{w}^T \phi_n) - t_n$$ => ovvero i coefficienti sono esattamente i residui rispetto ai nostri target!
	
- Non esiste però soluzione analitica per la ricerca del minimo => la funzione sigmoide non è lineare!! => anche se infatti è derivabile non permette soluzioni in forma chiusa per il massimo. => si può risolvere solo numericamente => ad esempio con Newton.
	
	16
---
**Regressione logistica**

- Qui vediamo perché il modello è chiamato regressione logistica: $$\nabla_{\mathbf{w}} E(\mathbf{w}) = \sum_{n=1}^{N} (y_n - t_n) \phi_n$$
- Questo è lo stesso aggiornamento di ==apprendimento sequenziale per la regressione lineare== con funzioni di base fisse $\phi$.
- E vediamo che l'obiettivo è *regredire* il target $t_n \in \{0, 1\}$ da $\phi(x)$.

+ Mettendo a confronto:

| **Regressione Lineare**                                              | **Regressione Logistica**                                                                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Errore quadratico $$E(w)=\frac{1}{2}\sum_{n=1}^N(w^T\phi_n -t_n)^2$$ | Log-verosimiglianza (negativa) $$E(w)=-\sum_{n=1}^N[t_n\mathcal{ln}( \sigma(w^T\phi_n)) + (1-t_n)\mathcal{ln}(1- \sigma(w^T\phi_n))]$$ |
| **Equazioni lineari**                                                | **Equazioni non lineari**                                                                                                              |
| **Soluzione in forma chiusa**                                        | **Soluzione numerica iterativa**                                                                                                       |
| $$w=(Φ^TΦ)^{−1}Φ^Tt$$                                                | $$w_{t+1}​=w_t​−η∇E(w_t​)$$                                                                                                            |


- Nota: questa soluzione di Massima Verosimiglianza è ==altamente soggetta a overfitting== quando $C_1$ e $C_2$ sono linearmente separabili.
- In questo caso, $||w||_2$ andrà all'infinito, convergendo a una stima posterior in cui per tutti $x$, e per qualche $k$, $p(C_k | x) = 1$. => all'infinito avrò al posto della sigmoide la step function!

	![[Pasted image 20251027213228.png]]
	
	17
---
## Regressione Logistica Bayesiana
---
**La ricetta per il ML Bayesiano**

- Abbiamo sviluppato un passo verso una ricetta per l'apprendimento bayesiano completo nella nostra discussione sulla regressione.
- Proviamo ad applicarla al nostro problema di classificazione:
  1. Decidere un prior $p(\mathbf{w})$.
  2. Massimizzare il posterior risultante per arrivare a una distribuzione dei parametri $p(\mathbf{w} | \mathbf{t})$.
  3. Derivare la distribuzione predittiva $p(C_k | \mathbf{\Phi}, \mathbf{t})$ che possiamo usare su nuovi dati $\phi(x)$.

- Il passo 1 è "facile" – sebbene sia una delle critiche principali dell'apprendimento bayesiano. => assunzioni sulla prior
- I passi 2 e 3 sono, sfortunatamente, **intrattabili**: la distribuzione posterior sui parametri **non è più Gaussiana**. => non abbiamo conoscenze sulla forma inoltre abbiamo una non linearità

- Vediamo cosa possiamo fare.

	18
---
**L'approssimazione di Laplace**

- Primo, assumiamo un prior Gaussiano: $p(\mathbf{w}) = \mathcal{N}(\mathbf{w} | m_0, S_0)$.
- Primo passo, approssimare la distribuzione dei parametri.
- Un metodo semplice è noto come **Approssimazione di Laplace** che usa la migliore approssimazione Gaussiana.$$q(\mathbf{w}) = \mathcal{N}(\mathbf{w} | \mathbf{w}_{MAP}, S_N)$$
- Dove i **parametri** sono derivati dalla stima Maximum a Posteriori (MAP) della media e della covarianza ottenuta minimizzando un'approssimazione del secondo ordine del vero posterior.

	19
---
**L'approssimazione di Laplace**

- Ecco un esempio di approssimazione di $p(z) \propto \exp(-z^2/2) \sigma(20z+4)$:

	![[Pasted image 20251011195804.png]]
	=> beh vicina ma non esatta.

	20
---
**La distribuzione predittiva** (skipped)

- Armati di questa approssimazione possiamo ora scrivere la **distribuzione predittiva** (approssimata):$$p(C_1 | \phi, \mathbf{t}) = \int p(C_1 | \phi, \mathbf{w})p(\mathbf{w} | \mathbf{t})d\mathbf{w} \approx \int \sigma(\mathbf{w}^T\phi)q(\mathbf{w})d\mathbf{w}$$
- Questa è una convoluzione di una sigmoide logistica e di una Gaussiana, che può essere approssimata (dopo derivazioni molto lunghe) come: $$p(C_1 | \phi, \mathbf{t}) \approx \sigma(\kappa(\sigma_a^2)\mu_a)$$dove $\kappa(\sigma^2) = (1 + \pi\sigma_a^2/8)^{-1/2}$  
- per $\sigma_a^2 = \text{var}[a] = \phi^T S_N\phi$ e $\mu_a = \mathbf{w}_{MAP}^T \phi$

	21
---
## Considerazioni Conclusive
---
**Modelli probabilistici generativi**

- La visione generativa di $p(C_k | x)$ è allettante per una serie di ragioni.
- Sotto la stima di Massima Verosimiglianza dei parametri, **stimiamo** semplicemente una **distribuzione per le verosimiglianze** condizionate alla classe $p(x|C_k)$ e per i prior $p(C_k)$.
- ==Per il caso Gaussiano==, queste stime risultano essere quelle "usuali".
	- Se assumiamo ==covarianza uguale== per tutte le classi, il risultato è un **classificatore lineare**.
	- Invece, se stimiamo un $\Sigma_k$ per ogni classe il classificatore risultante è **quadratico** nell'input.

	22
---
**Regressione Logistica**

- La regressione logistica è un modello estremamente importante perché quasi tutte le Deep Neural Networks per la classificazione eseguono una regressione logistica multi-classe. => ==evita di fare i calcoli per la distribuzione per le verosimiglianze dei dati.==
- Una Deep Network stima l'embedding delle feature $\phi(x)$, poi viene applicata una funzione lineare e il softmax.
- Quindi viene applicata una loss di *Log-verosimiglianza Negativa* – anche nota come Entropia Incrociata. (cross entropy)
- Nonostante i suoi problemi, è un modello abbastanza adatto per l'ottimizzazione incrementale basata sul gradiente.
- Importante: il fatto che le uscite sommino a uno, significa poco in termini di interpretazione probabilistica del risultato.

+ Riassumendo:
	+ Modelli generativi modellano tutta la distribuzione dei dati => capendo come sono fatti i dati di ogni classe (media, covarianza e prior) e quindi con la possibilità di generarne dei nuovi (campionando dalla Gaussiana ottenuta secondo la distribuzione dei dati)
	+ Modelli discriminativi invece modellano solo il confine decisionale => capiscono come separare le classi, e non hanno l'obiettivo di generare nuovi dati! 

	23
---
**Regressione Logistica Bayesiana**

- L'inferenza bayesiana esatta è **intrattabile** a causa della complessità della verosimiglianza dei dati.
- E della necessità di normalizzare il posterior – non possiamo più ignorare il fattore di evidenza nella regola di Bayes.
- Ci sono tecniche molto sofisticate **per approssimare** i posterior normalizzati:
  - Metodo di Laplace: approssimare con una Gaussiana.
  - Inferenza Variazionale: adattare una distribuzione proxy al posterior.
  - Metodi Monte Carlo: usare il campionamento di Markov per l'integrazione.
	=> Al momento tecniche solo approx che però dovessero portare a risulatati soddisfacenti potrebbe portare a grosse novità nel campo del ml => in quanto evito tutti i passaggi iniziali sui dati!

	24
---
**Letture e Compiti**

Lettura Raccomandata:

- Bishop: Capitolo 4 (4.2, 4.3, 4.4*, 4.5*)

	+Notare che per tutti i modelli considerati fino adesso qualsiasi dato ha stesso peso/importanza per la scelta dei parametri/boundary dei nostri dati => questo fa sì che i nostro modello sia molto soggetto agli outliers!

	25
---
# 7 - SVM Lineare

## Introduzione
---
**Motivazioni**

- Consideriamo un semplice problema di classificazione linearmente separabile:

	![[Pasted image 20251013223453.png]]
	=> Quanti piani ci sono ? beh infiniti che dividano le due classi => quale sarà il migliore?
	
	2
---
**Motivazioni: un approccio probabilistico**

- Abbiamo strumenti per questi problemi, ad esempio un **discriminante lineare generativo**:

	![[Pasted image 20251013224603.png]]

	3
---
**Motivazioni: sensibilità agli outlier**

- Un problema con molti approcci probabilistici è la **sensibilità agli outlier**:

	![[Pasted image 20251013225123.png]] 
	=> Il discriminante viene mandato giù e non diventa più un buon classificatore => basta un solo outlier a far abbassare la media e quindi il boundary (hyperplane) => ho infatti una dipendenza da tutti i punti del mio train set!
	=>Notare che anche media e covarianza non diventano più molto rappresentativi della classe
	
	4
---
**Motivazioni: sensibilità agli outlier**

- L'effetto sull'iperpiano separatore è più evidente da vicino:

	![[Pasted image 20251013225156.png]]

	5
---
**Motivazioni: alcuni outlier sono peggiori di altri...**

- I metodi che trattano tutti i campioni allo stesso modo possono degradare rapidamente:
	
	![[Pasted image 20251013225235.png]] 
	- In questo caso è presente un outlier nel punto -50 che fa variare completamente la media => me ne basta anche uno solo!
	- Il piano separatore non ha alcun senso! 

- Un' idea può essere l'outlier remover => elimino i dati considerati come meno probabili

	6
---
**Motivazioni: classificatori a margine, qualche intuizione**

- Possiamo riformulare un obiettivo di classificazione in termini del **solo margine**? => dove metto la decision boundary?? => da cosa è supportata la mia decisione? => i margini!
- Concettualmente vogliamo trovare la "strada" con margini massimi rispetto alla decision boundary => ma allo stesso tempo che separa perfettamente i dati
- Margini come distanza dal discriminant al punto più vicino

	![[Pasted image 20251013223453.png]]

	![[Pasted image 20251028163711.png]]
	=> I 3/4 punti sui margini saranno gli unici punti che definiscono il margin plane
	=> Aggiungendo outliers a punti infiniti non cambia la cosa in quanto il piano è definito in quel modo!
	
	7
---
**Obiettivi della lezione**

Dopo questa lezione:

- Avrete acquisito una comprensione più profonda della geometria della classificazione e di come il ridimensionamento del margine sia correlato al parametro $\mathbf{w}$ del discriminante lineare.
- Comprenderete la **forma primale** del Classificatore a Margine Massimo – noto anche come Macchina a Vettori di Supporto (SVM).
- Comprenderete come la **forma duale** della SVM sia derivata dal Lagrangiano della formulazione del margine massimo.
- Comprenderete come le variabili slack possono essere introdotte nella formulazione SVM per gestire dataset non linearmente separabili. => permette di separare linearmente le due classi!
- Sarete in grado di interpretare le variabili duali e come identificano i vettori di supporto nel training set.

	8
---
## Il Margine
---
**Preliminari: un po' di algebra lineare**

- Definizione (Mappa Bilineare)
	Una funzione $\Omega : V \times V \to \mathbb{R}$ è una *mappa bilineare* dallo spazio vettoriale $V$ a $\mathbb{R}$ se e solo se:$$\Omega(\lambda x + \psi y, z) = \lambda \Omega(x, z) + \psi \Omega(y, z)$$$$\Omega(x, \lambda y + \psi z) = \lambda \Omega(x, y) + \psi \Omega(x, z)$$per ogni $x, y, z \in V$.

	- $\Omega$ è chiamata simmetrica se $\Omega(x, y) = \Omega(y, x)$ per tutti $x, y \in V$.  
	- $\Omega$ è chiamata definita positiva se:$$\Omega(x, x) \geq 0 \text{ per tutti } x, \text{ e } \Omega(x, x) = 0 \text{ se e solo se } x = 0$$
	9
---
**Preliminari: un po' di algebra lineare**

- **Definizione (Prodotto Interno e Spazio con Prodotto Interno)**
	Sia $V$ uno spazio vettoriale qualsiasi e $\Omega : V \times V \to \mathbb{R}$ una mappa bilineare da $V$ a $\mathbb{R}$. Allora:
	- Se $\Omega$ è simmetrica e definita positiva, $\Omega$ è chiamata prodotto interno su $V$. Di solito scriviamo $\langle x,y\rangle$ invece di $\Omega(x,y)$.
	- La coppia $(V,\Omega)$ (o $(V,\langle\cdot,\cdot\rangle)$) per il prodotto interno $\Omega$ è chiamata spazio con prodotto interno o spazio vettoriale con prodotto interno. Se $\Omega(x,y) = x^Ty$, $(V,\Omega)$ è chiamato spazio vettoriale Euclideo.

- I prodotti interni ci permettono di formalizzare le nostre intuizioni geometriche su **lunghezza, ortogonalità e distanza**.

	10
---
## Classificatori a Margine Massimo
---
**Il problema di classificazione (geometrico)**

- Un modo utile di pensare alla classificazione è che:
  1. Rappresentiamo i dati in $\mathbb{R}^D$.
  2. Partizioniamo $\mathbb{R}^D$ in modo tale che campioni con la stessa etichetta (e nessun campione con etichette diverse) cadano nella stessa partizione.

- Considereremo un partizionamento conveniente – quello di separare $\mathbb{R}^D$ in due metà usando un iperpiano separatore.

- Consideriamo una funzione $f: \mathbb{R}^D \to \mathbb{R}$ definita come:$$f(\mathbf{x}; \mathbf{w}, b) = \langle \mathbf{w}, \mathbf{x} \rangle + b$$
- Definiamo un **iperpiano** che partiziona il nostro spazio usando $f$ come: $$H = \{\mathbf{x} | f(\mathbf{x}; \mathbf{w}, b) = \langle \mathbf{w}, \mathbf{x} \rangle + b = 0\}$$	=> Sottospazio a valori nulli!
	- Come capisco che questo è l'iperpiano che separa? è questo perpendicolare a **w**??

	11
---
**La relazione tra w e H**

- La risposta è si! => L'iperpiano definito da w e b è perpendicolare a w.w
- Per vederlo, prendiamo due punti qualsiasi $x_1$ e $x_2$ in H e consideriamo:$$f(\mathbf{x_1}) - f(\mathbf{x_2}) = \langle \mathbf{w}, \mathbf{x_1} \rangle + b - \langle \mathbf{w}, x_2 \rangle - b = \langle \mathbf{w}, \mathbf{x_1} - \mathbf{x_2} \rangle$$ => ma siccome entrambi i punti fanno parte del piano allora per entrambi $f(x_i) = 0$, dunque l'inner product fra **w** e $\mathbf{x_1}-\mathbf{x_2}$ è pari a zero! => H contiene tutti qui vettori la cui loro differenza moltiplicata per **w** è nulla! => tutto quello che sta sul piano è perpendicolare a **w**

	12
---
**Come usiamo w e b**

- Quando ci viene presentato un campione di test $x$, lo classificheremo in base a **quale lato dell'iperpiano** giace: $$\text{class}(x) = \begin{cases} +1 & \text{se } f(x; w, b) \geq 0 \\ -1 & \text{se } f(x; w, b) < 0 \end{cases}$$
- Quando addestriamo su dati $\{(x_i, y_i) | i = 1, \ldots, N\}$, cerchiamo $w$ e $b$ tali che tutti i campioni cadano sul lato corretto dell'iperpiano:$$\langle w, x_i \rangle + b \geq 0 \quad \text{quando} \quad y_i = +1$$$$\langle w, x_i \rangle + b < 0 \quad \text{quando} \quad y_i = -1$$
	=> Se classe positiva discriminante positivo e vicercersa

- Queste condizioni sono spesso combinate nella forma più compatta:$$y_i(\langle w, x_i \rangle + b) \geq 0$$ per ogni $n \in \{1,...,N\}$ => notare la scelta del +/- 1 per avere esempi positivi e negativi (invece del semplice 0/1) => in questo modo escludo quelli che non soddisfano la condizione => inoltre posso compattare le due condizioni a una sola

	13
---
**Il margine**

- Il margine è definito come la **==distanza** tra un iperpiano separatore e il **punto** più vicino ad esso==.
- Il nostro obiettivo è massimizzare questa distanza, => in ogni situazione bisogna preferire l'iperpiano che massimizza il margin => in modo tale da separare al meglio le classi

	![[Pasted image 20251013230630.png]] => notare adesso soddisfo da entrambe le parti

- Quanto vale la distanza fra l'iperpiano e i punti??

	14
---
**Massimizzare il margine**

- La distanza **perpendicolare** tra qualsiasi punto $x_n$ e un iperpiano definito da $\langle w, x \rangle + b = 0$ è:  $$\frac{y_n(\langle w, x_n \rangle + b)}{||w||}$$ => sostanzialmente è una proiezione ortogonale dove moltiplico per il segno a seconda della posizione del punto. 
  => divido per la norma di **w** in modo tale da non avere influenza su quanto è grande questo => misuro in modo unitario!

- Vogliamo **massimizzare** la **minima** di queste distanze:$$\arg \max_{w, b} \left\{ \frac{1}{||w||} \min_{n} [y_n(\langle w, x_n \rangle + b)] \right\}$$ => vogliamo trovare w e b che massimizzano la distanza al punto (o i punti) più vicino 
  soggetto ai vincoli che $y_n(\langle w, x \rangle + b) \geq 0$ => questo per ogni punto! classificatori che non soddisfano verranno scartati!

- Questo è un problema di ottimizzazione **scomodo** a causa del **max/min** e **del punto più vicino che cambia.** => muovendo la discriminant function cambia il punto/punti più vicini ad esso

	15
---
**Massimizzare il margine**

- Notiamo, tuttavia, che possiamo **scalare** liberamente $\mathbf{w}$ e $b$ ==senza cambiare la distanza tra punti e iperpiano==. => verificare! (devono essere scalati allo stesso modo) => moltiplicando per uno scalare il sottospazio rimane lo stesso
- Quindi, possiamo scalare in modo che $\langle w, x_a \rangle + b = 1$ (1)  per il punto più vicino $x_a$.

- Sia $r$ la distanza ortogonale da $x_a$ all'iperpiano.

	![[Pasted image 20251028182044.png]]
	
- Allora, la proiezione ortogonale di $x_a$ sull'iperpiano è: $$x_a' = x_a - r \frac{\mathbf{w}}{||\mathbf{w}||}$$ => normalizzo per avere tutto unitario	
	
- Sostituiamo questo nel fatto che $x_a'$ **giace sull'iperpiano**: $$\langle \mathbf{w}, x_a - r \frac{\mathbf{w}}{||\mathbf{w}||} \rangle + b = 0$$
	16
---
**Massimizzare il margine**

- Sostituiamo questo nel fatto che $x_a'$ giace sull'iperpiano:  $$\langle \mathbf{w}, x_a - r\frac{\mathbf{w}}{||\mathbf{w}||} \rangle + b = 0$$- Ora, sfruttando la **bilinearità** del prodotto interno: $$\langle \mathbf{w}, x_a \rangle + b - r\frac{\langle \mathbf{w}, \mathbf{w} \rangle}{||\mathbf{w}||} = 0$$- Ricordando che $x_a$ giace sul margine (abbiamo scalato il margine a 1 (1) ), arriviamo a: $$r = \frac{1}{||\mathbf{w}||}$$
- Notare che imporre il vincolo richiesto significa chiedere anche di avere la norma di w pari a 1!

	17
---
**La forma canonica della SVM a Margine Rigido**

- Combinando la massimizzazione del margine con i vincoli arriviamo a:$$\max_{\mathbf{w},b} \frac{1}{||\mathbf{w}||}$$soggetto a  $y_n(\langle \mathbf{w}, x_n \rangle + b) \geq 1 \text{ per tutti } n = 1, \ldots, N$ 
	=> Ricordiamo che l'obiettivo era max il margine => ma anche quello di classificare in modo corretto tutti gli esempi

- Oppure, la più comune rappresentazione canonica della ***SVM a Margine Rigido***:$$\min_{\mathbf{w},b} \frac{1}{2}||\mathbf{w}||^2$$soggetto a  $y_n(\langle \mathbf{w}, x_n \rangle + b) \geq 1 \text{ per tutti } n = 1, \ldots, N$ => notare che però può capitare di avere un punto a distanza $c$ che scalandolo porta a una norma minore! => contraddizione! => ho trovato una soluzione migliore rispetto alla precedente.
- Ho un problema convesso quadratico con vincoli lineari => soluzione in $\mathcal{O}(D^3)$ => in questa forma è detta **forma primale**

	18
---
**Trovare w e b**

- Abbiamo un problema di programmazione **quadratica convessa in $D$ variabili con vincoli lineari**. (D+1 per definire la direzione del piano) => abbiamo detto esistono soluzioni in $O(D^3)$ per tante variabili diventa un po' difficile da gestire...

- Per risolvere un tale problema, possiamo formare la **funzione Lagrangiana**: $$L(w, b, a) = \frac{1}{2} ||w||^2 - \sum_{n=1}^{N} a_n \left\{ y_n(\langle w, x_n \rangle + b) - 1 \right\}$$ => aggiungo nuove variabili $a_n$ (variabili duali) => per togliere il vincolo di disuguaglianza

- Impostando $\frac{\partial}{\partial \mathbf{w}} L = 0$ e $\frac{\partial}{\partial b} L = 0$ (derivate parziali) otteniamo:$$\mathbf{w} = \sum_{n=1}^{N} a_n y_n \mathbf{x}_n$$ => le variabili primale sono espresse come dati e variabili duali		 $$0 = \sum_{n=1}^{N} a_n y_n$$

	19
---
**Trovare w e b**

- Sostituendo questo valore di **w** e il vincolo su $\sum_n a_n y_n$ nel **Lagrangiano**: $$\max_a \left\{ \sum_{n=1}^N a_n - \frac{1}{2} \sum_{n=1}^N \sum_{m=1}^N a_n a_m y_n y_m \langle x_n, x_m \rangle \right\}$$soggetto a $a_n \geq 0$, per $n = 1, \ldots, N$ $$\sum_{n=1}^N a_n y_n = 0$$
- Questa è la rappresentazione **duale della SVM a Margine Rigido,** ancora un problema di programmazione quadratica, ==ma in $N$ variabili==  
- La complessità per risolvere problemi quadratici in $N$ variabili è $\mathcal{O}(N^3)$. => passo da D a N variabili! => ovvero il numero dei nostri punti. => a seconda delle dimensioni del problema vedo quale strategia conviene usare!
- Guardando sulla forma del problema le nostre variabili interagiscono solo nella seconda parte e non nel vincolo => ho solo un prodotto interno delle coppie di $x_n$

	20
---
**Usare la SVM: il "Supporto" nelle Macchine a Vettori di Supporto** 

=> Se geometricamente i vettori di supporto sono quelli che supportano il margin... cosa sono numericamente?

- Per usare il classificatore (con un nuovo punto **x**) sostituiamo nuovamente il nostro **w** nella funzione di decisione:$$f(x) = \sum_{n=1}^{N} a_n y_n \langle x, x_n \rangle + b$$
- Le condizioni di Karush-Kuhn-Tucker (KKT) significano che la soluzione soddisfa:
	- $a_n \geq 0$
	- $y_n f(x_n) - 1 \geq 0$
	- $a_n \{ y_n f(x_n) - 1 \} = 0$

- Quindi, per tutti $n$ o $a_n = 0$ o $y_n f(x_n) = 1$. => ogni punto nel dataset avremo o una variabile lagrangiana a zero oppure la distanza dal discriminante è pari a 1 => ==questi sono dunque i vettori a supporto del margine!== (vettori a variabili duali non nulle => contribuiscono nella somma! => le altre non hanno effetto sul classificatore!)

	![[Pasted image 20251028232658.png]]
	
- Gli $x_n$ per cui $a_n > 0$ e $y_n f(x_n) = 1$ sono chiamati vettori di supporto. => tutto il resto dei punti con il duale a zero non va a contribuire per la nostra funzione di decisione! => la posizione dei nostri margini è individuata solo tramite i vettori di supporto

	21
---
**Macchine a Kernel Sparse (aka SVM)**

- Nota che solo i vettori di supporto contribuiscono alla classificazione:$$f(x) = \sum_{n=1}^{N} a_n y_n \langle x, x_n \rangle + b = \sum_{m \in SV} a_m y_m \langle x, x_m \rangle + b$$
- Questo è il motivo per cui le SVM sono anche più generalmente conosciute come **Macchine a Kernel Sparse**. => uso solo un sottoinsieme dei punti per ottenere il mio classificatore!
- (Vedremo da dove viene il kernel nella prossima lezione...)

	22
---
**SVM e classificazione robusta**

- Abbiamo un classificatore lineare che ora è **robusto** agli outlier:

	![[Pasted image 20251015222528.png]] => in blu i vettori a supporto!

	23
---
## Il Classificatore a Margine Morbido
---
**Distribuzioni di classe sovrapposte**

- Fino ad ora abbiamo assunto che il nostro problema sia **linearmente separabile**.
- Questo, chiaramente, quasi **mai accade**. => non sempre risolvibili con decision boundaries lineari

	![[Pasted image 20251015222642.png]]

	24
---
**Consentire misclassificazioni dei campioni di training**

- Per consentire la possibilità che alcuni campioni di training siano **misclassificati**, introduciamo variabili slack $\xi_n$: $$\xi_n = 
\begin{cases} 
0 & \text{se } x_n \text{ è sul o sul lato corretto del margine} \\
|y_n - \langle w, x_n \rangle + b| & \text{altrimenti}
\end{cases}$$ => Se sbaglio misuro quanto ho sbagliato! 
	![[Pasted image 20251015222743.png]] 
	=> mi dicono quindi quanto sono lontano dalla corretta classificazione! => prendiamo in considerazione anche questi punti anche se non classificati correttamente! => se sono sul margine la distanza è esattamente 1 altrimenti maggiore o minore a seconda di dove si trova! 

	25
---
**Il problema di ottimizzazione con slack**

- Il nuovo problema di ottimizzazione diventa: $$\min_{\mathbf{w},b} \frac{1}{2} ||\mathbf{w}||^2 + C \sum_{n=1}^{N} \xi_n$$soggetto a $y_n(\langle \mathbf{w}, x_n \rangle + b) \geq 1 - \xi_n$ per tutti $n = 1, \ldots, N$ => quello che mi dice il problema è quindi classifica il più possibile correttamente ma tieni il classificatore "semplice" => ovvero paga un costo il più basso possibile per ciò che sbagli => il tutto secondo il parametro C => che mi serve a dire quanto voglio pagare per gli errori!

- E dopo aver formato il Lagrangiano e risolto per le variabili duali (Bishop pagine 332-334): => si può rifare anche qui il duale $$\max_a \left\{ \sum_{n=1}^{N} a_n - \frac{1}{2} \sum_{n=1}^{N} \sum_{m=1}^{N} a_n a_m y_n y_m \langle x_n, x_m \rangle \right\}$$soggetto a $0 \leq a_n \leq C$, per $n = 1, \ldots, N$ $$\sum_{n=1}^{N} a_n y_n = 0$$ => si arriva alla stessa soluzione solo che ho un altro limite sulle variabili duali
	
	26
---
**La soluzione a Margine Morbido**

- La forma del risultato è quasi identica al caso a margine rigido.
- Nota, tuttavia, che i vettori di supporto ora includono **campioni misclassificati**.
- Poiché la penalità per la misclassificazione scala **linearmente** con $\xi$, la SVM a margine morbido **non è robusta agli outlier**. => ottengo errori numerici andando a rilassare i margini

	![[Pasted image 20251015222929.png]]

	=> Si ottiene un modello più complesso in quanto ho un altro parametro da prendere in considerazione! => a seconda di come scelgo C ci sarà uno shift dei margin...
	
	27
---
## Considerazioni Conclusive
---
**La Macchina a Vettori di Supporto**

- La SVM lineare è un classificatore potente che è robusto agli outlier (nel caso a margine rigido).
- Può essere adattata per gestire problemi che non sono linearmente separabili.
- Ma questo ha il costo di introdurre un iperparametro $C$ che bilancia il costo della misclassificazione con la massimizzazione del margine.
- Il vero vantaggio della SVM è che è un problema quadratico convesso che ha una soluzione unica e ammette algoritmi efficienti.
- Nella prossima lezione vedremo come possiamo estendere questa teoria a frontiere di decisione non lineari.

	28
---
**Letture e Compiti**

- Lettura Raccomandata:
	- Bishop: Capitolo 7 (7.1), Capitolo 6 (6.1, 6.2)

- Compiti:
	- Mostrare che $\Omega(x, y) = x^Ty$ è un prodotto interno.
	- Mostrare che, per $V = \mathbb{R}^2$, $\Omega(x, y) = x_1y_1 - (x_1y_2 + x_2y_1) + 2x_2y_2$ è un prodotto interno.
	- Mostrare che possiamo scalare il margine di una costante arbitraria $\gamma$ (cioè   $y_n(\langle w, x_n \rangle + b) \geq \gamma$) e la soluzione per l'iperpiano a margine massimo non cambia.

	29
---
# 8 - Il trick del Kernel e SVMs Non-lineari

## Introduzione
---
**Motivazioni**

- Ora abbiamo un modo per adattare modelli lineari per problemi di classificazione:

	![[Pasted image 20251029220829.png]]

	2
---
**Considerazioni**

- Possiamo estendere questo modello per catturare frontiere di decisione **non lineari** in qualche modo?
- Forse come abbiamo fatto con il *classificatore generativo quadratico*? O con i minimi quadrati?
- C'è un modo per farlo senza complicare l'elegante forma degli obiettivi di apprendimento?
- Non è immediatamente evidente come dovremmo farlo...

	3
---
**Obiettivi della lezione**

Dopo questa lezione:

- Comprenderete come l'apprendimento dei parametri della SVM lineare possa essere visto come un problema di minimizzazione della loss.
- Comprenderete come la massimizzazione del margine sia equivalente alla regolarizzazione della formulazione di minimizzazione della loss.
- Riconoscerete come i prodotti interni possano essere sostituiti con valutazioni del kernel nella formulazione duale della SVM.
- Comprenderete come le SVM non lineari possano essere adattate usando un kernel appropriato.
- Sarete in grado di applicare SVM lineari e non lineari nella pratica per risolvere problemi di classificazione.

	4
---

## Un'altra Vista della SVM Primal
---
**SVM tramite Minimizzazione del Rischio Empirico**

- Possiamo derivare la Macchina a Vettori di Supporto ideando un rischio empirico invece di analizzare il margine.
- Torniamo alla nostra classe di ipotesi $\mathcal{H}$ di funzioni discriminanti lineari:$$f(x) = \langle w, x \rangle + b$$
- Ma quale dovrebbe essere la nostra funzione di loss per $\mathcal{H}$ e un dataset  
  $D = \{ (x_n, y_n) | n = 1, \ldots N \}$?

- Ricordiamo che la loss ideale sarebbe la loss zero-uno:$$\mathcal{L}(w, b; D) = \sum_{n=1}^{N} 1(f(x_n) \neq y_n)$$
- Sfortunatamente, ricordiamo anche che questo risulta in un problema di ottimizzazione combinatoria che è NP-difficile...

	5
---
**SVM tramite Minimizzazione del Rischio Empirico**

- Quindi, quale dovrebbe essere la loss che risulta nella stessa SVM?
- Considerando gli errori fatti da una SVM: crescono linearmente con quanto sono lontani dal lato corretto del margine.
- Ciò di cui abbiamo bisogno è noto come **hinge loss**: $$\mathcal{L}(w, b; D) = \sum_{n=1}^{N} \max\{0, 1 - y_n(\langle w, x_n \rangle + b)\}$$$$= \sum_{n=1}^{N} \ell(x_n, y_n),$$dove $$\ell(x, y) = 
\begin{cases} 
0 & \text{se } y(\langle w, x \rangle + b) \geq 1 \\ 
1 - y(\langle w, x \rangle + b) & \text{se } y(\langle w, x \rangle + b) < 1 
\end{cases}$$
	![[Pasted image 20251029221515.png]]
	=> questo mi dice => se mi classifichi correttamente non paghi nulla (vince lo zero) => viceversa se ottieni un valore negativo paghi una penalità sempre più alta a seconda del valore che ottieni...
	
	6
---
**SVM tramite Minimizzazione del Rischio Empirico**
$$\mathcal{L}(w, b; D) = \sum_{n=1}^{N} \max\{0, 1 - y_n(\langle w, x_n \rangle + b)\}$$

- Questo merita considerazione:

	![[Pasted image 20251029222225.png]]
	=> L'hinge loss non contribuisce in alcun modo per gli esempi classificati correttamente!

	7
---
**SVM tramite Minimizzazione del Rischio Empirico**

- Ci manca solo un pezzo del puzzle di ottimizzazione: il controllo della complessità del modello.
- Ma sappiamo come farlo dalla nostra discussione sulla regressione lineare:$$(w^*, b^*) = \arg\min_{w, b} \frac{1}{2} ||w||^2 + C \sum_{n=1}^{N} \max\{0, 1 - y_n(\langle w, x_n \rangle + b)\}$$
- Abbiamo un problema di ottimizzazione non vincolato (ma ancora convesso) espresso in termini di una loss e un regolarizzatore.
- Quindi: *la massimizzazione del margine può essere vista come regolarizzazione*.
- L'iperparametro $C$ è usato per pesare la loss invece di $\lambda$ per il regolarizzatore.
- Tuttavia, siamo limitati alla forma primal della SVM...

	8
---

## Uno Sguardo più Dettagliato alla Forma Duale della SVM
---
**Un Esercizio di Pattern Matching**

- Torniamo alla forma duale della SVM:$$\max_{a} \left\{ \sum_{n=1}^{N} a_n - \frac{1}{2} \sum_{n=1}^{N} \sum_{m=1}^{N} a_n a_m y_n y_m \langle x_n, x_m \rangle \right\}$$soggetto a  $0 \leq a_n \leq C, \text{ per } n = 1, \ldots, N$ $$\sum_{n=1}^{N} a_n y_n = 0$$
- Nota che ==l'*unico* uso dei campioni di input è nel prodotto interno.==
- Questo significa che per apprendere abbiamo solo bisogno di calcolare prodotti interni tra i nostri campioni di input $x_n$.

	9
---
**Embedding esplicito**

- Ehi! Probabilmente possiamo usare un embedding esplicito $\phi : \mathbb{R}^D \to \mathcal{H}$ dei nostri dati in un nuovo spazio.
- Lo abbiamo già fatto con un **embedding polinomiale**...
- Il nuovo problema di ottimizzazione:$$\max_{a} \left\{ \sum_{n=1}^{N} a_n - \frac{1}{2} \sum_{n=1}^{N} \sum_{m=1}^{N} a_n a_m y_n y_m \langle \phi(\mathbf{x}_n), \phi(\mathbf{x}_m) \rangle_\mathcal{H} \right\}$$soggetto a  $0 \leq a_n \leq C, \text{ per } n = 1, \ldots, N$ $$\sum_{n=1}^{N} a_n y_n = 0$$
- Finché $(\mathcal{H}, \langle \cdot, \cdot \rangle_\mathcal{H})$ è uno spazio con prodotto interno, siamo a posto.

	10
---
**Embedding espliciti = Mappe di feature**

- **Embedding espliciti come questo sono solitamente chiamati mappe di feature.**  
- Stiamo mappando una rappresentazione di feature in uno spazio a un'altra rappresentazione di feature in un nuovo spazio.  
- Nota che non ci sono limitazioni sulla forma della mappa di feature $\phi$.  
- Il vantaggio principale della mappatura esplicita delle feature è che siamo liberi di usare combinazioni non lineari delle feature di input.  
- Il classificatore risultante è lineare nel "nuovo" spazio delle feature, ma **non lineare** in quello originale.

	11
---
**Non solo rose e fiori**

- Considera la mappa di feature polinomiale di grado $n$ da $\mathbb{R}^D \to \mathbb{R}^K$
- Domanda: cos'è $K$? Quanti monomi di grado $\leq n$ ci sono in $D$ variabili di input?
- Risposta:$$\binom{D+n-1}{n} = \frac{1}{(D-1)!}(n+1)^{D-1}$$ => può capitare di arrivare a milioni di parametri => overfitting! 

	![[Pasted image 20251029224033.png]]

	12
---
**Siamo fregati?**

- Beh, questo sembra senza speranza...
- Se incorporo esplicitamente i miei dati, (letteralmente) esplodo la mia complessità spaziale.
- C'è un modo per aggirare questa esplosione?
- Se ci pensate, vi ho già dato un enorme spoiler...

	13
---

## Il Kernel Trick
---
**Abbiamo solo bisogno delle valutazioni del prodotto interno**

- Tornando alla formulazione duale:$$\max_{a} \left\{ \sum_{n=1}^{N} a_n - \frac{1}{2} \sum_{n=1}^{N} \sum_{m=1}^{N} a_n a_m y_n y_m \langle \phi(\mathbf{x}_n), \phi(\mathbf{x}_m) \rangle_\mathcal{H} \right\}$$  soggetto a $0 \leq a_n \leq C$, per $n = 1, \ldots, N$ $$\sum_{n=1}^{N} a_n y_n = 0$$
- Osserviamo che non abbiamo bisogno degli embedding $\phi(\mathbf{x}_n)$ e $\phi(\mathbf{x}_m)$.
- Tutto ciò di cui abbiamo realmente bisogno è $\langle \phi(\mathbf{x}_n), \phi(\mathbf{x}_m) \rangle$.
- Diamogli un nome (beh, due, più o meno):  $$k(\mathbf{x}, \mathbf{z}) = \langle \phi(\mathbf{x}), \phi(\mathbf{z}) \rangle_\mathcal{H} \quad (\text{funzione kernel } k)$$$$K[n, m] = \langle \phi(\mathbf{x}_n), \phi(\mathbf{x}_m) \rangle_\mathcal{H} \quad (\text{matrix kernel o di Gram } K)$$ => quando serve faccio riferimento alla matrice kernel!

	14
---
**Forme duali di modelli lineari**

- Spesso la forma **duale** dei modelli lineari (ad esempio la SVM, ma vedi anche Bishop, capitolo 6.1) si basa solo su combinazioni lineari della funzione kernel $k$.
- La simmetria del prodotto interno implica che $k$ e $K$ sono simmetrici.
- La definitezza positiva del prodotto interno implica che $K$ è una matrice semidefinita positiva (cioè $x^TKx \geq 0 \, \forall x$).
- La funzione kernel più semplice è il kernel lineare:  $$k(x,z) = x^Tz, \quad \text{corrispondente a } \phi(x) = x$$
- Il kernel trick (chiamato anche kernel substitution) si riferisce all'uso di funzioni kernel per sostituire i prodotti interni in modelli altrimenti lineari.

	15
---
**Costruire kernel**

- Naturalmente, se la mappa di feature $\phi$ è trattabile, possiamo semplicemente usarla per definire il kernel corrispondente:  $$k(x,z) = \langle \phi(x), \phi(z) \rangle \, (\text{ovvio})$$
- Ciò che vogliamo realmente è costruire kernel direttamente ed evitare l'embedding.
- Considera questo esempio (assumendo $V = \mathbb{R}^2$):  $$k(x,z) = (x^Tz)^2$$$$= (x_1 z_1 + x_2 z_2)^2 = ...$$$$= (x_1^2, \sqrt{2} x_1 x_2, x_2^2)(z_1^2, \sqrt{2} z_1 z_2, z_2^2)^T$$
- Quindi,   $k(x,z) = (x^Tz)^2$  corrisponde all'**embedding polinomiale** !  
  $\phi(x) = (x_1^2, \sqrt{2} x_1 x_2, x_2^2)$ => tutti termini di secondo grado...

	16
---
**Costruire kernel**

- Possiamo combinare kernel in modi che preservano la semidefinitezza positiva:
Tramite kernel function possiamo implicitamente mappare i nostri dati in spazi a più dimensioni!

 - Tecniche per Costruire Nuovi Kernel.
	 - Dati kernel validi $k_1(x, x')$ e $k_2(x, x')$, i seguenti nuovi kernel saranno anche validi:
		- $k(x, x') = ck_1(x, x') \tag{6.13}$
		- $k(x, x') = f(x)k_1(x, x')f(x') \tag{6.14}$
		- $k(x, x') = q(k_1(x, x')) \tag{6.15}$
		- $k(x, x') = \exp(k_1(x, x')) \tag{6.16}$
		- $k(x, x') = k_1(x, x') + k_2(x, x') \tag{6.17}$
		- $k(x, x') = k_1(x, x')k_2(x, x') \tag{6.18}$
		- $k(x, x') = k_3(\phi(x), \phi(x')) \tag{6.19}$
		- $k(x, x') = x^T A x' \tag{6.20}$
		- $k(x, x') = k_a(x_a, x_a') + k_b(x_b, x_b') \tag{6.21}$
		- $k(x, x') = k_a(x_a, x_a')k_b(x_b, x_b') \tag{6.22}$
	
	dove $c > 0$ è una costante, $f(\cdot)$ è una qualsiasi funzione, $q(\cdot)$ è un polinomio con coefficienti non negativi, $\phi(x)$ è una funzione da $x$ a $\mathbb{R}^M$, $k_3(\cdot, \cdot)$ è un kernel valido in $\mathbb{R}^M$, $A$ è una matrice simmetrica semidefinita positiva, $x_a$ e $x_b$ sono variabili (non necessariamente disgiunte) con $x = (x_a, x_b)$, e $k_a$ e $k_b$ sono funzioni kernel valide nei rispettivi spazi.

	17
---
**Costruire kernel**

- Un kernel molto comunemente usato è il Gaussiano: $$k(x, z) = \exp\left\{-\frac{\|x - z\|^2}{2\sigma^2}\right\}$$
- Possiamo vedere che è un kernel usando la tabella della slide precedente e espandendo il quadrato dentro l'esponenziale: $$k(x, z) = \exp(-x^Tx/2\sigma^2)\exp(x^Tz/\sigma^2)\exp(-z^Tz/2\sigma^2)$$
- È abbastanza facile mostrare che questo corrisponde a un embedding $\phi(\cdot)$ che mappa su uno spazio delle feature *infinito* dimensionale.

---
**E allora?**

- Dobbiamo solo fare lievi aggiustamenti al nostro problema di apprendimento$$\max_a \left\{ \sum_{n=1}^N a_n - \frac{1}{2} \sum_{n=1}^N \sum_{m=1}^N a_n a_m y_n y_m k(x_n, x_m) \right\}$$soggetto a $0 \leq a_n \leq C$, per $n = 1, \ldots, N$ $$\sum_{n=1}^N a_n y_n = 0$$
- E al nostro classificatore: $$f(x) = \sum_{n=1}^N a_n y_n k(x, x_n) + b$$$$= \sum_{z \in SV} a_n y_n k(x, z) + b$$
	19
---

## Macchine a Vettori di Supporto nella Pratica
---
**Il Caso Multiclasse**

- Ehi, aspetta un minuto... Abbiamo sviluppato le SVM solo per problemi di classificazione binaria.
- Per il problema multiclasse generale, di solito usiamo un classificatore one-versus-rest e prendiamo semplicemente l'output massimo come nostra regola decisionale.

	![[Pasted image 20251001224446.png]]

	20
---
**Avvertenze**

- Le complessità temporali e spaziali dei risolutori SVM possono essere imprevedibili se non sapete cosa state facendo (cosa che ora tutti dovremmo sapere!).
- La complessità temporale varierà in termini di quale risolutore viene usato.
- Fortunatamente, ci sono molti pacchetti solidi disponibili per addestrare le SVM usando varie tecniche.

	21
---
**LibLinear**

- LibLinear è un risolutore SVM robusto e veloce con una storia molto lunga.
- Il suo focus principale è risolvere la formulazione dell'obiettivo primal.
- Può passare a un risolutore dual coordinate descent per problemi su larga scala.
- Può sfruttare macchine multi-core (utile per il caso multiclasse).

- `class sklearn.svm.LinearSVC(`
    `penalty='l2', loss='squared_hinge',`
    `dual=True, tol=0.0001, C=1.0,`
    `multi_class='ovr', fit_intercept=True,`
    `intercept_scaling=1,`
    `class_weight=None, verbose=0,`
    `random_state=None, max_iter=1000` `)`
	
	22
---
**LibSVM**

- LibSVM (dalle stesse brave persone che ci hanno portato LibLinear) è un risolutore SVM con una storia ancora più lunga.
- È un risolutore dual, quindi sebbene fornisca flessibilità tramite il kernel trick, può scalare male in spazio (o tempo se K non è precalcolata).
- Supporta un'ENORME varietà di formulazioni alternative dell'obiettivo SVM.

- `class sklearn.svm.SVC(
    C=1.0, kernel='rbf',
    degree=3, gamma='scale', coef0=0.0,
    shrinking=True, probability=False, tol=0.001,
    cache_size=200, class_weight=None, verbose=False,
    max_iter=-1, decision_function_shape='ovr',
    break_ties=False, random_state=None	)`

	23
---
**Risolutori Stochastic Gradient**

- Per dataset molto grandi, l'opzione migliore è spesso risolvere direttamente la forma primal usando la Minimizzazione del Rischio Empirico.
- Stochastic Gradient Descent (ne parleremo meglio quando arriveremo al Deep Learning) implementa questo in modo efficiente e sequenziale.

- `class sklearn.linear_model.SGDClassifier(
    loss='hinge', *, penalty='l2', alpha=0.0001,
    l1_ratio=0.15, fit_intercept=True, max_iter=1000,
    tol=0.001, shuffle=True, verbose=0, epsilon=0.1,
    n_jobs=None, random_state=None, learning_rate='optimal',
    eta0=0.0, power_t=0.5, early_stopping=False,
    validation_fraction=0.1, n_iter_no_change=5,
    class_weight=None, warm_start=False, average=False)`

	24
---
**Kernel Personalizzati**

- Per i risolutori duali la selezione del kernel è chiave (e di solito richiede un'ampia crossvalidazione!)

`kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’}, default='rbf'`

- Specifica il tipo di kernel da usare nell'algoritmo. Deve essere uno tra ‘linear’, ‘poly’, ‘rbf’, 'sigmoid’, ‘precomputed’ o un callable. Se non viene fornito nessuno, verrà usato ‘rbf’. Se viene fornito un callable, viene usato per pre-calcolare la matrice kernel dalle matrici di dati; quella matrice dovrebbe essere un array di forma (n_samples, n_samples).

	25
---
**Macchine a kernel e complessità del modello**

- Il **kernel trick** è un altro modo per affrontare il caso non linearmente separabile.
- È il modo principale per aumentare la complessità del modello senza cambiare la formulazione del modello sottostante.
	
	![[Pasted image 20251029231028.png]]

	26
---

## Considerazioni Conclusive
---
**La Macchina a Vettori di Supporto**

- Alla fine, le Macchine a Vettori di Supporto sono sempre macchine di apprendimento lineari (in qualche spazio).
- Il kernel trick ci permette di definire un problema di apprendimento lineare (in uno spazio *potenzialmente infinito dimensionale*) che è non lineare nello spazio originale.
- Come sempre, bisogna prestare attenzione quando si applica la SVM nella pratica.
- Sapere come funzionano le formulazioni primal e dual renderà le loro prestazioni e robustezza molto più prevedibili nella pratica.

	27
---
**Letture e Compiti**

- Lettura Raccomandata:
	- Bishop: Capitolo 7 (7.1), Capitolo 6 (6.1, 6.2)

- Compiti:
	- Convinciti che l'embedding $\phi(\cdot)$ corrispondente al kernel Gaussiano è infinito dimensionale.

	28
---

# 9 - 