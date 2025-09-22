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

---

**Il mondo di "domani"**

- Link al video

![[Pasted image 20250917223153.png]]

---
**Cos'è l'Apprendimento Automatico?**

“Ho studiato tutte le carte celesti disponibili di pianeti e stelle e nessuna corrisponde alle altre. Ci sono tante misurazioni e metodi quanti sono gli astronomi e tutti sono in disaccordo. Ciò che serve è un progetto a lungo termine con l'obiettivo di mappare i cieli condotto da una singola località per un periodo di diversi anni.”

	- Tycho Brahe, 1563 (età 17 anni).
(Tycho dice mannagg ar cazzo non ci sono abbastanza dati)

- Il termine Apprendimento Automatico risale ad Arthur Samuel negli anni '50.
- Negli anni successivi il suo ambito si è espanso e contratto.
- Un modo di pensare l'apprendimento automatico è:

$$\text{Apprendimento Automatico} = \text{(Statistica Computazionale + Ottimizzazione)} + \text{Dati (di solito molti)}$$

---
**Cos'è l'Apprendimento Automatico?**

“Si dice che un programma per computer apprenda dall'esperienza E rispetto ad alcune classi di compiti T e **misura di performance** P se la sua performance nei compiti in T, misurata da P, migliora con l'esperienza E.” => tipo vedo se aumenta accuratezza di classificazione

	- Tom Mitchell, 1987

- Questa definizione è simile alle definizioni (moderne) di Intelligenza Artificiale. 
- Cioè, è operativa invece che cognitiva.
- Alan Turing iniziò questa tendenza cambiando la domanda da “Le macchine possono pensare?” a “Le macchine possono fare ciò che noi (come entità pensanti) possiamo fare?”.

--- 
**Apprendimento supervisionato versus non supervisionato**

- L'Apprendimento Automatico è (molto approssimativamente) diviso in due macro categorie di approcci di apprendimento:
  - **Apprendimento Supervisionato**: a volte chiamato “apprendere da un insegnante” si riferisce a una classe di approcci che mirano ad apprendere a predire output da *input* partendo da un dataset di input e output accoppiati. => immagine e questa è un immagine di un gatto"
  - **Apprendimento Non Supervisionato**: che invece cerca di apprendere “qualcosa” da dati di input **non etichettati** – cioè, senza etichette pre-specificate. => tipo GPT, tanti dati senza supervisore => self supervisor

- In questo corso introduttivo ci limiteremo per lo più all'apprendimento supervisionato.
- Nota che esiste, in effetti, uno spettro completo di regimi di supervisione: supervisionato, debolmente supervisionato, semi-supervisionato, auto-supervisionato, non supervisionato. (algoritmi non supervisionati ci so a data mining)

---
**Apprendimento supervisionato: un esempio**

- Supponiamo di analizzare la correlazione tra **altezza** e **peso**.
- (A parte: useremo spesso esempi sintetici di questo tipo per illustrare concetti e tecniche chiave.)
- E supponiamo di avere solo due punti dati:
  $$ (67.9, 170.85) \text{ e } (61.9, 122.5)$$

- Idealmente, desideriamo inferire una **relazione** tra altezza e peso che spieghi i dati.
- Un buon primo passo è di solito visualizzare.

---
**Apprendimento supervisionato: un esempio**

• Quindi, abbiamo una situazione come questa…
• Cosa possiamo fare?

![[Pasted image 20250917230650.png]]

---
**Apprendimento supervisionato: un esempio**

- Beh, un po' di algebra delle scuole medie ci permette di connettere i punti:  $$y = 8.013x - 373.247$$ perché questo modello? => tipo perché non una parabola? 
=> la retta è il modello più semplice! => con due sole variabili!

![[Pasted image 20250917230839.png]]

---
**Apprendimento supervisionato: un esempio**

- Ora supponiamo di avere molti più dati.
- Il nostro “modello” generalizza?

![[Pasted image 20250917231024.png]]

In alcune parti potremmo fare meglio in altre peggio... Come migliorare? avendo più punti e solo con due parametri devo decidere quale sia il miglior modello che generalizza i dati.

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

---
**Prerequisiti (Statistica e Teoria della Probabilità)**

- I Concetti **Statistici** Chiave che dovreste conoscere includono:
  - Cos'è la Regola della **Somma della probabilità**? E la Regola del Prodotto?
  - Cosa hanno a che fare queste regole con le **funzioni di densità** di probabilità Congiunta, Condizionata e Marginale?
  - Cos'è la **Regola di Bayes**? Cosa significa e come possiamo derivarla?
  - Cos'è una Variabile Casuale? Cos'è il Valore Atteso di una (funzione di una) variabile casuale?

---
**Prerequisiti (Informatica)**

- Le competenze chiave dell'Informatica sono più difficili da elencare:
  - Dovete avere una padronanza operativa di almeno un linguaggio di programmazione di alto livello (preferibilmente uno dinamico come Python, R, Matlab o Lisp).
  - Le sessioni di laboratorio saranno svolte utilizzando Python e il suo eccellente ecosistema per la programmazione numerica.
  - Per favore utilizzate Questo Autovalutazione delle Competenze di Programmazione per verificare che la vostra conoscenza e competenza sia almeno da qualche parte tra i livelli A2 e B1.

---
**Organizzazione**

Questo corso è sui **Fondamenti dell'Apprendimento Automatico**, e in esso tratteremo:

- Fondamenti dei Fondamenti: teoria della probabilità e statistica per l'apprendimento automatico, distribuzioni di probabilità, basi della teoria dell'informazione (NO), interpretazioni bayesiane versus frequentiste, modelli lineari per la regressione, modelli lineari per la classificazione, la scomposizione bias-varianza, overfitting e underfitting, regolarizzazione del modello, modelli generativi probabilistici, modelli discriminativi probabilistici, **Stima di Massima Verosimiglianza** (Likelihood) (MLE), inferenza Massima a Posteriori (MAP), inferenza bayesiana. => primo modulo su regressione e classificazione

- Apprendimento Automatico: **Macchine a Vettori di Supporto** (SVM), modelli kernel, modelli grafici (NO), alberi decisionali, metodi ensemble, boosting, bagging, media bayesiana di modelli, foreste casuali, Expectation Maximization (EM), stima della densità di misture.

---
**Organizzazione**

- Apprendimento Profondo(Deep Learning): modelli connessionisti, regole di apprendimento hebbiane, il percettrone, reti neurali, Discesa del Gradiente Stocastica (SGD), l'algoritmo di Backpropagation, il Percettrone Multistrato (MLP), gradienti che svaniscono ed esplodenti, dimensione del modello e regolarizzazione, regolarizzazione della rete.
- Argomenti Speciali e Applicazioni: Reti Neurali Ricorrenti a Memoria a Lungo-Termine (LSTM) (NO), elaborazione del linguaggio naturale e modelli linguistici (Transformers), Reti Neurali Convoluzionali (CNN), apprendimento auto-supervisionato, apprendimento continuo, adattamento del dominio, transfer learning.
- Strumenti, Tecniche e Best Practices: programmazione numerica, visualizzazione, diagnostica del modello e monitoraggio dell'addestramento, scikit-learn (buono per per documentazione), PyTorch(framework scelto principalmente per machine learning).

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
 
---
**Obiettivi di Alto Livello**

- L'Apprendimento Automatico è un campo ampio e molto attivo.
- A un livello base, riguarda l'apprendere da dati di addestramento per fare inferenze su nuovi dati.
- Questa descrizione piuttosto vaga articola già concetti chiave che studieremo in dettaglio.
- Per impiegare l'Apprendimento Automatico nella pratica, dobbiamo familiarizzare con alcuni strumenti teorici.
- Questi strumenti ci aiuteranno a modellare problemi di apprendimento, valutare le performance dei sistemi di apprendimento e quantificare la fiducia nelle nostre soluzioni.

---
**Obiettivi: Teoria e Pratica**

Facciamo un passo indietro e pensiamo a obiettivi più astratti:

- In questo corso daremo un'occhiata relativamente approfondita a diverse teorie fondamentali dell'Apprendimento Automatico.
- La teoria è importante, ma non è tutto.
- Probabilmente il 95% delle volte non avete esplicitamente bisogno di teorie sofisticate.
- Tuttavia, per quel 5% rimanente diventa improvvisamente indispensabile – specialmente quando si cerca di capire perché le cose non funzionano come previsto.
- Quindi, non preoccupatevi se non afferrate ogni intuizione o derivazione dalle versioni abbreviate qui. (il bro ci dirà cosa è effettivamente più importante)
- Assimilate, costruite intuizione sulla teoria che informerà la vostra pratica.

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

---
**Buone e cattive notizie (per lo più buone, davvero)**

- Tutti facciamo un respiro profondo prima di continuare a leggere:

I vostri giorni di apprendimento in ambienti di apprendimento strutturati sono (quasi) finiti.
=> Define your learning objectives? 

---
**Cosa ci si aspetta da voi (e dal vostro professore (io))**

- Possiede conoscenza e intuizione dimostrabili, basate sulla conoscenza e intuizione a livello di Laurea Triennale che la superano e/o approfondiscono, oltre a fornire una base o un'opportunità per dare un contributo originale allo sviluppo e/o applicazione di idee, spesso in un contesto di ricerca.
- È in grado di applicare conoscenza, intuizione e capacità di problem solving in circostanze nuove o sconosciute in un contesto più ampio (o multidisciplinare) relativo al campo di competenza; è in grado di integrare conoscenze e gestire materie complesse.
- È in grado di formulare giudizi sulla base di informazioni incomplete o limitate, tenendo conto delle responsabilità sociali ed etiche associate all'applicazione delle proprie conoscenze e giudizi.
- È in grado di comunicare conclusioni, così come le conoscenze, motivazioni e considerazioni che le sottendono, in modo chiaro e non ambiguo a un pubblico di specialisti o non specialisti.
- Possiede le capacità di apprendimento che gli/le permettono di intraprendere uno studio successivo con un carattere largamente auto-diretto o autonomo.

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

---
**Abbiamo finito?**

- **Possiamo andare a casa?**$$h^* = \arg\min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$
- Non possiamo ancora andare a casa. Cominciamo con la grande incognita $p$ => non sappiamo appunto la relazione fra x e y => è quella che vogliamo scoprire!

- Senza informazioni su $p$ dobbiamo ricorrere al **campionamento**:  $$(x_i, y_i) \in \mathcal{X} \times \mathcal{Y}, \text{ per } i \in \{1, \ldots, N\}$$
- Importante: $(x_i, y_i) \sim p(x, y)$

- Possiamo allora approssimare l'obiettivo con la perdita attesa empirica(empirical expected loss/empirical risk minimization): $$h^* = \arg\min_{h \in \mathcal{H}} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}(h(x_i), y_i)$$
---
**Abbiamo finito ora?**

- **Bene. Ora possiamo andare a casa?** $$h^* = \arg\min_{h \in \mathcal{H}} \int \mathcal{L}(h(x), y) p(x, y) dxdy$$$$\approx \arg\min_{h \in \mathcal{H}} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}(h(x_i), y_i)$$
- Non possiamo.
- E riguardo a $\mathcal{L}$ ?
- E riguardo a $\mathcal{H}$ ?

Scegliendo ad esempio un h* che sia esattamente y e una loss qualsiasi (tipo quadratica)... rischio di avere un modello che approssima troppo => extreme over-fitting

- E riguardo a quella spaventosa minimizzazione?
- Infine, e riguardo a $\mathcal{X}$ e $\mathcal{Y}$ => occhio alle rappresentazioni fra spazio di partenza e fine => tipo immagini e classificazione come output => che cosa devo avere come output?

---
**Generalizzare**

- Torniamo all'esempio semplice, ma cosa succede se abbiamo dati distribuiti come sotto?
- Processo: $y = f(x) + \varepsilon$ (dove $\varepsilon$ è rumore gaussiano).

![[Pasted image 20250918100418.png]]
=> Notare che il rumore ci aiuta a non essere troppo precisi nel trovare il modello corretto => utile per generalizzare

---
**Generalizzare**

- Il nostro obiettivo è sfruttare questo training set per fare previsioni.
- Cioè, predire il target $\hat{y} = f(\hat{x})$ per nuovi $\hat{x}$.
- Nel fare questo stiamo implicitamente cercando di apprendere quale sia la underlying $f$.
- L'apprendimento dovrebbe essere indipendente da $\varepsilon$ (che non vogliamo catturare).

---
**Un diverso tipo di problema**

- A volte vogliamo capire come i dati sono generati da $N$ sorgenti.
- Con l'obiettivo di discriminare le sorgenti l'una dall'altra.

![[Pasted image 20250918110847.png]]

---
**Discriminare**

- Idea generale: trovare un **iperpiano** separatore.
- Cioè, uno che separi una classe dall'altra.

![[Pasted image 20250918111902.png]]

---
# Ma quale?

- Quale è il discriminante “migliore”?
- Cosa significa addirittura migliore qui?

![[Pasted image 20250918111941.png]]

---
**Due visioni (e l'obbligatorio esempio del lancio della moneta)**

- Supponiamo di avere una moneta e vogliamo decidere se è equa o no.
- Qualcuno ha eseguito un esperimento da cui ha derivato questa stima:

![[Pasted image 20250918112120.png]]

---
**Due visioni**

- E se i dati fossero riassunti invece in questo modo.
- Questo ti fa ripensare la tua inferenza sulla moneta?

![[Pasted image 20250918112324.png]]

---
**Due visioni**

- Quando stimiamo i parametri di un modello (a volte riferito come inferenza), dobbiamo applicare tutto ciò che sappiamo.
- In particolare, dobbiamo stare attenti a quantificare ogni volta possibile la nostra fiducia nell'accuratezza delle nostre inferenze.

![[Pasted image 20250918112610.png]]

---
**Un esempio motivante**

- Tornando al nostro semplice problema di regressione: osserviamo una variabile di input a valori reali $x$ e vogliamo predire una variabile target a valori reali $t$.

- Ai fini della dimostrazione, consideriamo un esempio artificiale di dati generati sinteticamente: $y = f(x|w) + \varepsilon$

- Ci viene dato un training set di coppie \((x, y)\) campionate da \( p(x, y) \).
- Obiettivo: apprendere la funzione sottostante $f$ che ha generato questi dati.
- In questo modo, per $\hat{x}$ non visto possiamo usare $f(\hat{x}|w^*)$ per predire il target $\hat{y}$.

![[Pasted image 20250918113923.png]]

---
# Un esempio motivante

- Modelliamo questo problema come uno di fitting di curve, per esempio usando un modello polinomiale:

\[y(x|w) = w_0 + w_1x + w_2x^2 + \cdots w_Mx^M\]

\[= \sum_{j=0}^M w_j x^j\]

- Nota come, anche se \( y(x|w) \) è una funzione non lineare di \( x \), è una funzione lineare nei coefficienti \( w \) (cioè i parametri del modello).

- Per apprendimento intendiamo stimare i parametri “migliori” \( w \) dal dataset
  \[  D = \{(x_i, y_i) \mid i = 1, \ldots, N\}.\]

37

===== Pagina 51 =====

# Un esempio motivante

- Cosa significa buono in questo contesto?
- Beh, possiamo cominciare pensando di misurare l'errore nella funzione stimata in termini dei dati osservati:

\[\mathcal{L}(w|D) = \frac{1}{2} \sum_{(x,t)\in D} \{y(x,w) - t\}^2\]

- Che è una funzione quadratica in \( w \), quindi le sue derivate sono lineari.
- E \(\mathcal{L}(w|D)\) ha un unico minimizzatore \( w^* \).
- Abbiamo finito?

===== Pagina 52 =====

# Un esempio motivante

- Non abbiamo finito. C'è un iperparametro del nostro modello che abbiamo convenientemente dimenticato: l'ordine del polinomio \( M \).

\[M = 0\]

\[t\]

\[0\]

\[-1\]

\[0\]

\[x\]

\[1\]

\[t\]

\[0\]

\[-1\]

\[0\]

\[x\]

\[1\]

\[M = 1\]

39

===== Pagina 53 =====

# Un esempio motivante

- Non abbiamo finito. C'è un iperparametro del nostro modello che abbiamo convenientemente dimenticato: l'ordine del polinomio \( M \).

\[M = 3\]

\[t\]

\[0\]

\[x\]

\[1\]

\[t\]

\[0\]

\[-1\]

\[0\]

\[x\]

\[1\]

\[M = 9\]

40

===== Pagina 54 =====

**Un esempio motivante**

- Il problema rimanente è la selezione del modello, ed è un elemento fondamentale dell'apprendimento automatico. Come potremmo affrontarlo?

41

===== Pagina 55 =====

# Un esempio motivante

- Il problema rimanente è la selezione del modello, ed è un elemento fondamentale dell'apprendimento automatico. Come potremmo affrontarlo?
- Otteniamo intuizione sull'underfitting e sull'overfitting disegnando un test set indipendente e tracciando \( E_{RMS} = \sqrt{2\ell(w^*|D)}/N \)

---

### Diagramma
- **Training Test**
  - \( E_{RMS} \)
  - \( 0.5 \)
  - \( 0 \)
  - \( 3 \)
  - \( M \)
  - \( 6 \)
  - \( 9 \)

===== Pagina 56 =====

**La Gen-X Insegna alla Gen-Y e alla Gen-Z**
**(su X, Y e Z)**

===== Pagina 57 =====

**Un po' di me**

>

>

>

===== Pagina 58 =====

**I primi anni: anni '80 e '90 (big math)**

Matematica: grandi cardinali e determinacy

- Il mio primo amore è stata la matematica, che ho studiato alla University of Nevada, Las Vegas (sì, quella Las Vegas).
- Specificamente, teoria descrittiva degli insiemi e la relazione tra Ipotesi dei Grandi Cardinali, determinacy di giochi semplici su insiemi di numeri reali, e la consistenza di tutta la matematica.

===== Pagina 59 [text layer] =====

**I primi anni: anni '80 e '90 (elaborazione di immagini)**
Matematica: grandi cardinali e determinacy
- In parallelo, ho lavorato su problemi di stima di immagini low-level.
- Specificamente, sulla stima di orientamenti locali e globali in immagini di documenti scannerizzati.
- La novità all'epoca, era investigare come stimare in domini compressi.
45

===== Pagina 60 =====

# Gli anni di Amsterdam: primi anni 2000 (visione)

- Nel 1999 mi sono trasferito in Europa per un dottorato in Analisi di Informazione Multimediale alla *Universiteit van Amsterdam*:
  - Visione low-level: gradient boosting e inversione di mezzitoni.
  - Morfologia matematica: analisi granulometrica della struttura profonda dell'immagine.
  - Modelli a grafo: analisi del layout di immagini con First-order Gaussian Graphs.
  - Programmazione funzionale: modelli formali di programmi di visione.

46

===== Pagina 61 =====

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

===== Pagina 62 =====

**Sì, ma cosa fai, tipo adesso?**

- In questo momento la mia ricerca si focalizza su problemi di apprendimento continuo in visione artificiale e linguaggio:

Task A (appross. diagonale)

Task B

Task A

Task B

Task A

Task B

===== Pagina 63 =====

**Inoltre, giochi!**

- Con un dottorando (Alessandro Sestini) ricerco anche tecniche di Apprendimento per Rinforzo Profondo per costruire Agenti Non Giocatore (NPA) intelligenti.

---

**Livello 10**

**DeepCrawl**

HP: 20120
Gwenf. Ltd
Rip: 1641, Amp 2
Nessuno

Azioni

49

===== Pagina 64 =====

# Filosofia e stile di insegnamento

- L'apprendimento è più efficace quando è uno scambio interattivo piuttosto che uno stare-lì-e-ascoltare passivo.
- Il mio lavoro come professore è mettere la mia conoscenza a vostra disposizione.
- Il vostro lavoro è succhiare ogni ultimo bit di conoscenza da me in queste lezioni.
- Se non capite qualcosa, interrompetemi e chiedetemi di chiarire.
- [ Parabola del 'ne so così tanto' ]

50

===== Pagina 65 =====

**Osservazioni Conclusive**

===== Pagina 66 =====

# Costruzione di Comunità: Il Discord UniFI AI

- Abbiamo creato un Server Discord per ospitare discussioni sull'Intelligenza Artificiale.
- C'è un canale dedicato per il corso di Fondamenti di Apprendimento Automatico (FML).
- Per favore unitevi, e sentitevi liberi di usare questo server per condividere, scambiare informazioni, chiedere aiuto e per chiacchiere generiche relative a ML, AI, dataset, qualsiasi cosa.
- Importante: questo è un forum pubblico, quindi siate gentili, siate rispettosi e divertitevi.

https://discord.gg/tUkgrgXdXE
51

===== Pagina 67 =====

**La strada da percorrere**

- Nella prossima lezione tratteremo alcune preliminari (per lo più matematiche) che saranno utili durante tutto il corso.
- Più specificamente, tratterò alcuni concetti fondamentali di algebra lineare, statistica e probabilità, e le importanti proprietà della distribuzione Gaussiana.
- Costruiremo anche un'intuizione sul perché l'Apprendimento Automatico è difficile attraverso un'analisi della Maledizione della Dimensionalità.

“Tycho possiede le osservazioni più accurate del mondo, ma gli manca un architetto capace di costruire un edificio partendo dai suoi dati.”

– Johannes Keppler

52

===== Pagina 68 =====

# Letture e Compiti a Casa

## Lettura Assegnata:

- Bishop: Capitolo 1 (1.1, 1.3, 1.4)

## Compiti a Casa:

1. Familiarizzate con l'UCI Machine Learning Repository di dataset liberamente disponibili per la ricerca sul ML.

2. Meditate sull'esempio del lancio della moneta e pensate a come potremmo mitigare i problemi discussi durante la lezione (cioè come prendere pulitamente in considerazione la nostra confidenza sulla nostra stima).
   Suggerimento: Pensatela come un problema di stima sequenziale e usate la Regola di Bayes.

53

[file content end]
---

Ho mantenuto i termini tecnici in inglese (Machine Learning, overfitting, input, output, dataset, ecc.) come è comune nella letteratura accademica italiana, ma ho tradotto tutto il resto in modo letterale. Ho anche mantenuto la struttura con i segni `#` e `##` per i titoli e le formule matematiche intatte.