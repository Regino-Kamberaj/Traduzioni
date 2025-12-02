# 14 - Modelli Ensemble
## Introduzione
---
**Il potere del consenso**

- Tutti i modelli di regressione e classificazione che abbiamo considerato finora sono singoli – adattiamo **un modello** e prevediamo usando un modello.
- Spesso possiamo migliorare i modelli singoli **combinandone multipli**.
- Potremmo addestrare $M$ **modelli**, e poi prendere la media delle loro previsioni.
- Oppure, potremmo addestrare **modelli in sequenza** e incoraggiare i modelli successivi a compensare gli errori commessi dai precedenti. => boosting
- Oppure, potremmo addestrare modelli multipli e poi selezionare il migliore per fare previsioni per un dato $x$.
- Tali modelli sono solitamente chiamati **modelli ensemble** poiché fanno previsioni basate su un insieme di modelli addestrati invece che su uno solo.

	2
---
**Obiettivi della lezione**

Dopo questa lezione:

- Comprenderete come il bagging (o bootstrap aggregation) possa essere usato per generare dataset multipli da uno singolo.
- Comprenderete come i committee sono formati addestrando modelli multipli su dataset bootstrap.
- Comprenderete come e perché i committee riducono l'errore del modello attraverso la media.
- Comprenderete come il boosting funziona per addestrare una sequenza di weak learner e come questi learner sono combinati in un committee più forte tramite pesatura.
- Comprenderete come i modelli ad albero partizionano lo spazio in regioni cuboidi e come apprendere la loro struttura e parametri.

	3
---
## Committee e Bagging
---
**Il potere del consenso**

- Abbiamo visto tempo fa in una delle nostre prime lezioni come il campionamento di modelli multipli e la **media** aiuti a ridurre la varianza: => anche bayes faceva così => cosindera tutti i possibili i modelli e poi ne faceva la media => intrattabile però 
- Possiamo sfruttare questo senza un modello **completamente** Bayesiano?

	![[Pasted image 20250930120423.png]]

	4
---
**Campionamento Bootstrap**

- Consideriamo un problema di regressione in cui stiamo prevedendo un singolo target continuo.
- L'approccio di riduzione della varianza funzionava addestrando un modello a **basso bias** su dataset multipli e mediando gli output.
- In pratica abbiamo solo un dataset, tuttavia.
- Il *metodo bootstrap* funziona campionando $M$ dataset di dimensione $N' < N$ da $D$ con **reinserimento**. => tipo abbiamo diverse copie di uno stesso dato e alcuni dataset hanno dati che altri non hanno
- Ognuno di questi dataset bootstrap riflette la distribuzione sottostante di $D$ ma è incompleto.

	5
---
**Bootstrap aggregation (o bagging)**

- Possiamo quindi adattare un modello $y_m(x)$ a ogni **dataset bootstrap** (usando qualsiasi metodo).
- E poi formare il modello *committee* mediando gli $M$ **modelli base**:$$y_{\text{com}}(x) = \frac{1}{M} \sum_{m=1}^{M} y_m(x)$$ => si fa la media di tutte le predizioni
- Perchè può essere una buona idea?
- Indichiamo con $h(x)$ la **vera** funzione di regressione che genera $D$.
- L'output di ogni modello può essere scritto come questa funzione vera **più un errore**:$$y_m(x) = h(x) + \epsilon_m(x)$$ => tipo misuro la differenza rispetto al modello reale
- Nota che non abbiamo ancora fatto nulla – eccetto identificare l'errore in ognuno dei nostri modelli.

	6
---
**Quantificare l'errore**

- L'errore quadratico **atteso** di ogni modello è allora:$$\mathbb{E}_x \left[ \{ h(x) - y_m(x) \}^2 \right] = \mathbb{E}_x \left[ \varepsilon_m(x)^2 \right]$$
- E l'errore medio dei modelli individuali è: (su tutti gli errori)$$E_{\text{av}} = \frac{1}{M} \sum_{m=1}^{M} \mathbb{E}_x \left[ \varepsilon_m(x)^2 \right]$$
- Ancora, non abbiamo detto nulla di sconvolgente: l'errore quadratico medio commesso dai modelli è la media di tutti gli errori quadratici commessi dai modelli.

	7
---
**L'errore del committee**

- Possiamo calcolare l'errore atteso del committee similmente:$$E_{\text{com}} = \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M h(x) - y_m(x) \right\}^2 \right]$$ =>sostanzialmente porto dentro h(x)$$= \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M \varepsilon_m(x) \right\}^2 \right]$$ => si risemplifica e ottengo l'errore solo che in questo il quadrato sta fuori => $(\varepsilon_1 +\varepsilon_2 +---)^2$

- OK, ma elevare al quadrato quella $\sum$ sarà un gran casino...

	8
---
**L'errore del committee**

- Come possiamo superare questo? Risposta: assunzioni!$$E_{\text{com}} = \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M \varepsilon_m(x) \right\}^2 \right]$$

- Se assumiamo che gli errori:
	- **siano a media zero**:(ogni errore individuale ha aspettativa nulla) $$\mathbb{E}_x [\varepsilon_m(x)] = 0$$
	- e non correlati:$$\mathbb{E}_x [\varepsilon_m(x)\varepsilon_n(x)] - \mathbb{E}_x [\varepsilon_m(x)] \mathbb{E}_x [\varepsilon_n(x)] = 0 \quad m \neq n$$
- Allora abbiamo:(aggiungi sketch)$$E_{\text{com}} = \frac{1}{M} E_{\text{av}}$$ => mi rimane l'unico caso in cui m=n(il resto è zero) => in cui ho della varianza

	9
---
**Mediare modelli riduce l'errore atteso**

- Quindi se mediiamo $M$ modelli ==riduciamo l'errore atteso dei modelli singoli di un fattore ==$1/M$!$$E_{\text{com}} = \frac{1}{M} E_{\text{av}}$$ => questo quante volte voglio ma...
- Ricorda le assunzioni, però: gli errori **sono quasi mai non correlati**. => serve che siano correlati fra di loro!
- Tuttavia, ci sono garanzie che l'errore del committee ==non supererà mai l'errore atteso del modello== (cioè $E_{\text{com}} \leq E_{\text{av}}$). => buona cosa dei modelli committee! => dividere il dataset, fittare il dataset e fare la media riduce l'errore! => un buon es sarebbe dimostrare che il commitee di un modello di regressione lineare è ancora un modello di regressione lineare nello spazio originale. da M modelli ne possiamo comunque trarre un linear model

	10
---
## (SKIPPABLE) Boosting
---
**SKIPPABLE Media pesata**

- Il modello committee calcola una semplice media sui modelli base$$y_{\text{com}}(x) = \frac{1}{M} \sum_{m=1}^{M} y_m(x)$$
- Questi modelli sono adattati tramite bagging: campioni multipli dal training set con reinserimento.
- I modelli base sono addestrati indipendentemente sui dataset bootstrap (cioè i campioni dal bagging).
- E se non trattassimo tutti i modelli come uguali nel committee?
- E se li addestrassimo in sequenza in modo che "si aiutino a vicenda" in qualche modo?

	11
---
**SKIPPABLE Boosting**

- Questo è precisamente ciò che fa il **boosting**: => non ho più indipendenza dei modelli!
	
	![[Pasted image 20251104230108.png]]

	12
---
**SKIPPABLE AdaBoost**

- L'algoritmo AdaBoost fa questo per problemi di classificazione binaria.
- Assumiamo di avere un dataset $D = \{(x_1, t_1), \ldots, (x_N, t_N)\}$ per $t_n \in \{-1, 1\}$.
- L'idea di AdaBoost:
  - Associamo ad ogni campione un peso, che inizialmente è $\frac{1}{N}$.
  - Assumiamo di avere un modo per addestrare un classificatore base con campioni pesati.
  - Dopo aver addestrato $M$ classificatori base li combiniamo in un committee con coefficienti che danno pesi diversi ad ogni classificatore.

- Nota: nel boosting, questi classificatori base sono solitamente chiamati weak learner.

	13
---
**SKIPPABLE AdaBoost**

- **AdaBoost**:
	1. Inizializza i coefficienti di pesatura dei dati $\{w_n\}$ impostando $w_n^{(1)} = 1/N$ per $n = 1, \ldots, N$.
	2. Per $m = 1, \ldots, M$:
	   (a) Adatta un classificatore $y_m(\mathbf{x})$ ai dati di training minimizzando la funzione di errore pesata:$$J_m = \sum_{n=1}^{N} w_n^{(m)} I(y_m(\mathbf{x}_n) \neq t_n)$$    dove $I(y_m(\mathbf{x}_n) \neq t_n)$ è la funzione indicatrice e vale 1 quando $y_m(\mathbf{x}_n) \neq t_n$ e 0 altrimenti.

	 (b) Valuta le quantità:$$\varepsilon_m = \frac{\sum_{n=1}^{N} w_n^{(m)} I(y_m(\mathbf{x}_n) \neq t_n)}{\sum_{n=1}^{N} w_n^{(m)}}$$   e poi usale per valutare $\alpha_m = \ln \left\{ \frac{1 - \varepsilon_m}{\varepsilon_m} \right\}$   (14.17)

	 (c) Aggiorna i coefficienti di pesatura dei dati:$$w_n^{(m+1)} = w_n^{(m)} \exp \left( \alpha_m I(y_m(\mathbf{x}_n) \neq t_n) \right)$$      (14.18)

	3. Fai previsioni usando il modello finale, che è dato da$$Y_M(\mathbf{x}) = \text{sign} \left( \sum_{m=1}^{M} \alpha_m y_m(\mathbf{x}) \right)$$    (14.19)

	14
---
**SKIPPABLE AdaBoost**

- Gli $\varepsilon_m$ rappresentano i tassi di errore (pesati) del classificatore $y_m$.
- I coefficienti di pesatura $\alpha_m$ assegnano peso maggiore ai classificatori più accurati in (14.19).
- E sono usati per dare peso maggiore ai campioni misclassificati in (14.18).
- AdaBoost funziona molto bene in pratica, specialmente con molti, potenzialmente molto weak learner.

	15
---
**SKIPPABLE AdaBoost**

![[Pasted image 20251104230718.png]]

	16
---
## Modelli ad Albero (facili da interpretare!)
---
**Partizionamento ricorsivo dello spazio**

- Possiamo pensare alla **classificazione** (anche regressione) come fare previsioni **costanti** ==su partizioni dello spazio di input==: => si usa treshold values sulle previsioni => le regioni trovate hanno valori costanti in output

	![[Pasted image 20251104230905.png]] => si usa l'albero per rappresentare le partizioni dello spazio di input

- Quali sono i parametri del modello? Sono i valori di treshold da imparare => come sceglierli? 
- La depth dell'albero ovvero quando fermarsi invece sono degli iperparametri da decidere
	
	17
---
**Alberi Decisionali**

- I modelli ad albero sono modelli semplici ma *ampiamente usati* che funzionano per partizionamento.
- Gli **alberi allineati** agli assi partizionano lo spazio in cuboidi allineati(tipo iper-rettangoli) con gli assi.
- Sono **modelli ensemble**: un singolo modello è responsabile per ogni partizione.
- Per selezionare quale modello attraversiamo l'albero in un processo decisionale sequenziale.
- I modelli ad albero sono spesso considerati **interpretabili dagli umani**.
- Il modello che consideriamo è il *Classification and Regression Tree* (CART).

	18
---
**Apprendere un modello ad albero**

- Consideriamo ancora un problema di **regressione** con dataset $D = \{ (x_1, t_1), \ldots, (x_N, t_N) \}$  
  dove ora i nostri $t_n$ sono target continui.

- Vogliamo partizionare lo spazio $\mathbb{R}^D$ in modo che in ogni partizione la nostra stima del target lì **minimizzi l'errore quadratico**.

- Questo è piuttosto facile: abbiamo solo bisogno della **media** dei target $t_n$ di tutti i punti $x_n$ che cadono in quella partizione.

- Il vero problema è *come dovremmo determinare questo partizionamento*. => quale sarà la migliore la partizione??

- Ottimizzare su tutti i possibili partizionamenti è combinatorialmente intrattabile, anche per alberi allineati agli assi...

	19
---
**Apprendimento greedy**

- Invece, useremo una politica **ricorsiva** e **greedy**:
  1. Inizia da un singolo **nodo radice** corrispondente all'intero spazio.
  2. Itera su ognuna delle $D$ possibili variabili di split: (ordiniamo tutto il nostro dataset secondo le input variables => metti sketch)
    - 2.1 Considera ogni possibile soglia per dividere i dati in due insiemi. => divido in modo tale da non riottenere gli insieme di partenza
    - 2.2 Seleziona quella che **minimizza la somma degli errori** quadratici negli split. => per insiemi con un solo elemento l'errore è nullo  => ocho però rischio overfitting!
  3. Applica ricorsivamente questa procedura ai figli.

- ==Quando dovremmo fermare questa procedura==?
- La solita strategia è sovrasegmentare lo spazio di input costruendo un albero profondo e ampio.
- Perché questo potrebbe essere problematico?
- E poi **potare** l'albero per bilanciare **complessità** e **minimizzazione dell'errore sui dati** di training. => come definire il pruning criteria?

	20
---
**Apprendimento greedy**

- Assumiamo di avere già un partizionamento (un albero), con nodi foglia indicizzati da $\tau = 1, \ldots, T$.
- Chiama la partizione corrispondente a ogni foglia $R_\tau$.
- La **previsione ottimale** e l'**errore quadratico** in ogni nodo sono: $$y_\tau = \frac{1}{N_\tau} \sum_{x_n \in R_\tau} t_n$$ $$\quad Q_\tau(T) = \sum_{x_n \in R_\tau} (t_n - y_\tau)^2$$
- Quindi possiamo definire un **criterio di potatura** come: $$C(T) = \sum_{\tau=1}^{|T|} Q_\tau(T) + \lambda |T|$$
	=> Più salgo in alto nella potatura e più aumento l'errore...
	
	21
---
**Per problemi di classificazione**

- Se abbiamo un problema di **classificazione**, dobbiamo solo cambiare l'errore.
- Definisci $p_{\tau k}$ come la proporzione di campioni di classe $k$ al nodo $\tau$. => si usano le probabilità sulle classi => considero diversi pruning...
- Per esempio l'**entropia incrociata negativa**: $$Q_\tau(T) = \sum_{k=1}^K p_{\tau k} \ln p_{\tau k}$$
- O l'indice di Gini: $$Q_\tau(T) = \sum_{k=1}^K p_{\tau k}(1 - p_{\tau k})$$
	22
---
## Considerazioni Conclusive
---
**Il potere del consenso (e della diversità!)**

- I **modelli ensemble** sono un potente strumento per combinare modelli semplici in modelli migliori.
- I committee riducono il tasso di errore medio – ma solo se le assunzioni sono valide.
- Gli alberi sono modelli interpretabili che partizionano lo spazio di input in regioni omogenee.

	23
---
**Letture e Compiti**

- Lettura Raccomandata:
	- Bishop: Capitolo 14 (14.1, 14.2, 14.3, 14.4, 14.5)
	- Guida Utente di Scikit-learn (capitolo 1.11)

	24
---

# 10 - Metodi Nonparametrici
---
## Introduzione
---
**Motivazioni**

- Abbiamo visto una varietà di metodi per classificazione e regressione.
- Finora, tutti sono quelli che sono noti come metodi parametrici.
- Questi metodi si concentrano sull'apprendimento stimando i parametri ottimali del modello (in qualche modo).
- Il modello risultante è tipicamente semplice (almeno finora):$$f(\mathbf{x}; \mathbf{w}, b) = \mathbf{w}^T x + b$$
- Una caratteristica di queste tecniche è che la "conoscenza" appresa dai dati è **completamente incapsulata** nei parametri.
- Questo è a volte chiamato collo di bottiglia e può aiutare la generalizzazione.

	2
---
**Obiettivi della lezione**

Dopo questa lezione:
- Comprenderete come valutare le prestazioni di un classificatore.
- Comprenderete le basi degli stimatori di densità kernel e come usarli per modellare funzioni di densità di probabilità.
- Comprenderete come l'approccio della stima di densità kernel può essere applicato a problemi di regressione (es. Nadaraya-Watson).
- Comprenderete come funziona l'algoritmo Nearest-neighbor in teoria e in pratica.

	3
---
## Argomenti Residuali: Valutazione dei Classificatori
---
**Valutare i Classificatori: Problemi Bilanciati**

- Come misuriamo le prestazioni dei classificatori addestrati?
- Se hai un problema di classificazione **bilanciato** (come la maggior parte che vedremo nei laboratori), usa l'accuratezza del classificatore:$$accuracy = \frac{\# \text{ campioni di test classificati correttamente}}{\# \text{ campioni di test}}$$
- Perché questa potrebbe essere una metrica cattiva se il problema è **sbilanciato**? => che  succede ad esempio nel caso di face-detection => _sliding window_ => muovo la window sulla mia immagine => brute-force approach => un sacco di window, inoltre posso anche cambiare le dimensioni della mia finestra... Come valutare il mio classificatore ? se uso questa accuracy => questa rimmarrà principalmente a zero!! => ho pochi casi in cui vedo facce! rispetto ai casi in cui non le vedo...

	4
---
**Valutare i Classificatori: Matrici di Confusione**

- Un buon strumento per avere una panoramica dei tipi di errori che un classificatore sta facendo è la **matrice di confusione**: 

	![[Pasted image 20251105223309.png]] => ci permette di dare accuracy diverse alle classi... occhio però ai falsi positivi... anche se pochi moltiplicati per le diverse windows diventano molti!
	
	5
---
**Valutare i Classificatori: Problemi Sbilanciati**

- Iniziamo sezionando le classificazioni: (metriche utili solo nel caso di classificazione binaria => si fa tutto rispetto ad una delle due classi) (metti sketch)
  - **Veri positivi** (TP): abbiamo predetto sì, e il campione appartiene alla classe.
  - **Veri negativi** (TN): abbiamo predetto no, e il campione non appartiene alla classe.
  - **Falsi positivi** (FP): abbiamo predetto sì, ma il campione non appartiene alla classe – anche noto come errore di Tipo I.
  - **Falsi negativi** (FN): abbiamo predetto no, ma il campione appartiene alla classe – anche noto come errore di Tipo II.

- Possiamo allora definire alcune metriche utili per problemi sbilanciati: $$\text{Precisione}(c) = \frac{\text{TP}}{\text{TP} + \text{FP}}$$ => per tutti i casi in cui classifico per la classe positiva => quanto sono preciso
$$\text{Recall}(c) = \frac{\text{TP}}{\text{TP} + \text{FN}}$$=> di tutti i casi in cui classifico correttamente quanto fanno parte della classe positiva?
$$\text{F1}(c) = 2\frac{\text{Precisione}(c) * \text{Recall}(c)}{\text{Precisione}(c) + \text{Recall}(c)}$$ => notare il parametro c...

	6
---
**Valutare i Classificatori: Problemi Sbilanciati**

- Di solito comprendiamo precisione e recall usando le curve **Precision-Recall** (PR) e/o **Receiver-Operating Characteristic** (ROC):

	![[Pasted image 20251105223507.png]] 
	=> Parto da precision estremamente corretta => e aumentando il treshold diminuisco la precisione aumentando il recall => vorremmo avere una curva che rimane piatta fino a un certo punto in cui cade tutta insieme => classificatore ideale

+Sketch => una volta ordinati i dati si considera diversi treshold e guardo se rispetto alle mio classificazioni effettivamente rispetto o meno le classi... recall che mi dice appunto quanti di tutti i classicati positivamente ne sono classificati correttamente
=> di solito precision-recall curve definita su tutti i punti => ad ogni punto di recall posso ottenere la precision => posso scegliere il mio treshold cercando di ottimizzare il tradeoff fra precision e recall
=> una buona metrica è quindi l'area sotto la curva (AUC) => dove la migliore è quella con precision sempre a 1 fino a recall a 1 => max l'area...

+Altro esempio è la ROC curve dopo a seconda del numero di false positive ottengo i true positive...


	7
---
**Valutare i Classificatori: Analisi**

- La metrica di valutazione da usare è di solito chiara dato il tipo di problema (classificazione, regressione, retrieval) e la distribuzione dei dati di training (bilanciata, sbilanciata).
- Ottenere una stima affidabile di un classificatore può essere complicato in quanto chiaramente dipende dalla tua divisione train/test.
- Questo diventa il problema centrale quando si esegue la selezione del modello tramite cross-validation.
- In sklearn: sklearn.metrics

	8
---

## Stima della densità: Istogrammi Rivisitati
---
**Il problema con i modelli parametrici**

- I modelli probabilistici che abbiamo studiato finora sono basati su modelli parametrici.
- Stimiamo **un piccolo numero di parametri** di distribuzione (es. media e covarianza di Gaussiane in bayes).
- Una tale **assunzione a priori di una forma distributiva** è una limitazione di questi approcci. =>  nella realtà dati multimodali? => ovvero diverse medie => moda e media non coincidono
- Specialmente quando queste assunzioni risultano inaccurate.

- Idea: possiamo fare a meno dell'assunzione parametrica, e lasciare semplicemente che i dati parlino da soli?

	9
---
**Istogrammi: stimatori di densità costanti a tratti**

- Un istogramma partiziona il dominio in **bin** di larghezza fissa.
- Contiamo poi il ==numero di osservazioni che cadono in ogni bin== discreto.
- Possiamo trasformare questa rappresentazione in una **densità di probabilità** dividendo per il **numero totale di osservazioni** $N$ e la **larghezza** del bin $\Delta_i$: $$p_i = \frac{n_i}{N\Delta_i}$$
- Questo produce una densità $p(x)$ che è costante sulla larghezza di ogni bin (di solito $\Delta_i = \Delta$). => integrandola su tutti i bin si riottene 1 (+sketch) => funzione piece-wise constant => discontinua

	10
---
**Istogrammi: stimatori di densità costanti a tratti**

- Questo dà uno stimatore di densità con un singolo iperparametro: => l'unico iperparamentro è dunque la larghezza dei bins

	![[Pasted image 20251105224554.png]] (in verde la true density => dove i dati sono campionati)

	11
---
**Istogrammi: stimatori di densità costanti a tratti**

- La selezione di $\Delta$ è **critica** – troppo piccolo e lo stimatore ha alta varianza. => troppo dipendente da questo!
- Troppo grande e la curva è troppo liscia. => histogram ha smoothing effect
- Il modello è discontinuo ai bordi dei bin.
- I dati non sono necessari al tempo di test (vantaggio => guardo i bins piuttosto che tutti i dati), ma gli istogrammi scalano molto male con la dimensione ($M^D$). => si ritorna a curse of dimensionality

	![[Pasted image 20251105224554.png]]

	12
---
**Istogrammi: stimatori di densità costanti a tratti**

- Nonostante le loro limitazioni, gli istogrammi ci dicono qualcosa di importante sulla **stima della densità**.
- Per stimare la densità in un punto $x$ nel dominio, dovremmo ==guardare i punti dati che giacciono vicino== a $x$.
- Questo uso della località assume che abbiamo una metrica di distanza significativa nel dominio (es. Euclidea). => $||\mathbf{x}  - \mathbf{y}||$ => che succede però se una dimensione ha una scala molto più grande rispetto all'altra? vince sempre quella con scala più grande! => la distanza sarà sempre più piccola in questo caso (anisotropic?) => importante scalare i dati
- Diamo un'occhiata ad alcuni metodi nonparametrici comuni usati in Machine Learning.

	13
---

## Stima della Densità: Kernel Density Estimators
---
**Una digressione binomiale**

- Per motivare come possiamo estendere la nostra idea dell'istogramma a uno stimatore puramente locale, dobbiamo considerare la distribuzione binomiale.
- La **distribuzione binomiale** rappresenta la probabilità di vedere $m$ **successi** in una sequenza di $N$ **prove** di Bernoulli:$$\text{Bin}(m|N, \mu) = \binom{N}{m} \mu^m (1 - \mu)^{(N - m)}$$ => $\mu$ è la likelihood dei successi
$$\mathbb{E}(m) = \sum_{m=0}^{N} m \text{Bin}(m|N, \mu) = N\mu$$

	14
---
Una digressione binomiale

- La binomiale è unimodale e in qualche modo simile a una **Gaussiana**:

	![[Pasted image 20251105224901.png]]

	15
---
**Generalizzando**

- Assumiamo di avere osservazioni estratte da una **densità sconosciuta** $p(x)$ in uno spazio Euclideo $D$-dimensionale.
- Simile a un istogramma, consideriamo **una piccola regione** $\mathcal{R}$ attorno a $x$. (metti sketch)
- La **massa di probabilità** (tipo likelihood) associata con $\mathcal{R}$ è$$P = \int_{\mathcal{R}} p(x) dx$$ => probabilità di *cadere* in quella regione
- Se abbiamo $N$ osservazioni estratte da $p(x)$, ognuna ha probabilità $P$ di cadere in $\mathcal{R}$.
- Quindi, il numero totale di punti $K$ che cadono in $\mathcal{R}$ sarà **distribuito binomialmente**: => per bernoulli (o sono dentro la regione o non ci sono in N test)$$\text{Bin}(K|N, P) = \binom{N}{K} P^K (1 - P)^{(N-K)}$$
	16
---
**Generalizzando**

- Usando le formule per media e varianza della Binomiale possiamo analizzare la frazione di punti che cadono in $R$: (K out of N)$$\mathbb{E}(K/N) = P$$ $$\text{var}(K/N) = \frac{P(1-P)}{N}$$
- Per $N$ grande questa distribuzione sarà **concentrata** attorno a $P$ e quindi:$$K \approx NP$$ => varianza che diventa sempre più stretta(sketch)... il numero dei punti diventa quindi N per il numero di punti che ci aspettiamo cadano nella regione! 

	17
---
**Generalizzando**

- Per $N$ grande questa distribuzione sarà **concentrata** attorno a $P$ e quindi:$$K \approx NP$$
- D'altra parte, possiamo assumere $R$ con volume $V$ sia sufficientemente piccolo (e quindi $p(x)$ è **costante**) e quindi: $$P \approx p(x)V$$ => la prob diventa costante!
- Portandoci a: $$p(x) \approx \frac{K}{NV}$$ => numero di punti che cadono nella regione fratto numero di tentativi e il volume => tipo stesso caso degli istogrammi!

	18
---
**Generalizzando**

- Nota che questa stima di $p(x)$ è basata su due assunzioni contraddittorie:
  - Che $R$ sia sufficientemente piccolo e quindi $p(x)$ è costante in esso.
  - Che $R$ sia sufficientemente grande in modo che il numero di punti che cadono in esso siano sufficienti a picco la binomiale. => per avere un estimate con un senso

- Questo ci lascia con due scelte:
  1. ==Fissare $K$== e lasciare che i dati determinino cosa $V$ dovrebbe essere (**Nearest Neighbors**).
  2. ==Fissare $V$== e lasciare che i dati determinino cosa $K$ dovrebbe essere (**Kernel Density Estimation**).

	19
---
**Kernel Density Estimation**

- Prendiamo $R$ come un ipercubo unitario centrato all'origine.
- Questo è convenientemente descritto dalla **funzione kernel**:$$k(u) =
\begin{cases} 
1 & \text{se } |u_i| \leq 1/2, \text{ per } i = 1, \ldots, D \\
0 & \text{altrimenti}
\end{cases}$$
- Quindi, per qualsiasi punto $x$, $k((x - x_n)/h) = 1$ se il punto $x_n$ giace dentro un ipercubo con dimensione $h$ centrato su $x$. (metti sketch) => si può traslare e scalare il nostro ipercubo a piacimento per qualsiasi punto nello spazio => tipo standard gaussian distribution ma nel caso discreto.
- Il numero totale di punti $K$ che giacciono in tale ipercubo attorno a $x$ è allora: $$K = \sum_{n=1}^{N} k \left( \frac{x - x_n}{h} \right)$$ => si sommano sul kernel!

	20
---
**Kernel Density Estimation**

- Tornando alla nostra equazione per $p(x)$, abbiamo: $$p(x) = \frac{K}{NV} = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{h^D} k \left( \frac{x - x_n}{h} \right)$$ => purely local version di un istogramma 
- Questo soffre ancora di ==discontinuità ai bordi dell'ipercubo== (sketch) => dovuto al modo in cui abbiamo definito il kernel, quindi un kernel più comune è il **Gaussiano**: $$p(x) = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{(2\pi h^2)^{D/2}} \exp \left\{ - \frac{||x - x_n||^2}{2h^2} \right\}$$ (altro sketch) => gaussian centrato in x => misuro quanto i punti vicini contribuiscono alla mia densità => considero il contributo di tutti i punti! => parzen kernel density estimator! => buono perchè infinitamente derivabile!

	21
---
**Kernel Density Estimation**

- Questo è chiamato Kernel Density Estimator (o di Parzen).
- L'iperparametro $h$ è chiamato bandwidth del kernel che controlla la quantità di smoothing che viene eseguita.
- Le funzioni kernel dovrebbero soddisfare:  $$k(u) \geq 0, \, \int uk(u)du = 0, \, \text{e} \, \int k(u)du = 1$$ (kernel simmetrico => media a zero, positivo e la somma deve fare 1)
 - Questi tipi di approcci sono spesso chiamati metodi locali perché per stimare $p(x)$ guardano i dati vicini a $x$.

	22
---
**Kernel Density Estimation**

![[Pasted image 20251105225455.png]] 
=> a seconda del bandwith scelto ottengo diversi casi => scegliere h molto stretto può capitare nell'avere tante piccole gaussiane in tutti i punti e niente intorno!

+ Altro grosso problema... => devo fare la somma su tutti i punti del mio dataset!! => problema che scala male!

	23
---

## Regressione Kernel di Nadaraya-Watson
---
**Località in x e y**

- Possiamo applicare questo tipo di metodo locale a **problemi di regressione.**
- Ricordiamo che un predittore ottimale per la regressione è: $$\mathbb{E}(t | \mathbf{x}) = \int t p(t | \mathbf{x}) dt = \int t \frac{p(\mathbf{x}, t)}{p(\mathbf{x})} dt$$
- ==Ora usiamo le Kernel Density Estimates come approssimazioni==: (tolgo l'h a scalare ma c'è)$$\hat{p}(\mathbf{x}, t) = \frac{1}{N} \sum_{n=1}^{N} k_h (\mathbf{x} - \mathbf{x}_n) k_h (t - t_n)$$ => faccio la joint probability di due gaussiane anche con bandwith diverso (a seconda dello scale dei dati => target vs features) $$\hat{p}(\mathbf{x}) = \frac{1}{N} \sum_{n=1}^{N} k_h (\mathbf{x} - \mathbf{x}_n)$$
	24
---
**Nadaraya-Watson: regressione localmente pesata**

- La nostra approssimazione dello stimatore ottimale è ora: $$\mathbb{E}(t \mid x) = \int t \frac{p(x, t)}{p(x)} dt$$$$= \int t \frac{1}{N} \sum_{n=1}^{N} \frac{k_h (x - x_n) k_h (t - t_n)}{p(x)} d t$$ma solo una parte dipende da t!$$= \frac{\sum_{n=1}^{N} k_h (x - x_n) \int t k_h (t - t_n) d t}{\sum_{n=1}^{N} k_h (x - x_n)}$$ riottengo l'expected value del kernel di $t_n$ $$= \frac{\sum_{n=1}^{N} k_h (x - x_n) t_n}{\sum_{n=1}^{N} k_h (x - x_n)}$$ => quanto contribuisce un punto $x_n$ => me lo dice appunto il kernel!  => metti sketch => kernel mi dice appunto il suo peso!

	25
---
**Uno stimatore approssimativamente ottimale**

![[Pasted image 20251105230051.png]]

	26
---

## K-Nearest Neighbors
---
**Il problema di $h$**

- Un problema con la Kernel Density Estimation è che il bandwidth $h$ è **fissato per tutti i kernel**.
- Se abbiamo parti dello spazio con molti campioni, questo può portare a oversmoothing e perdita di dettaglio se $h$ è troppo grande!
- Se riduciamo $h$, in regioni a bassa densità avremo **stime rumorose**.
- E se, invece di fissare $V$ (tramite il bandwidth) e derivare un'espressione per $K$, fissassimo $K$ e andassimo nella direzione opposta.

	27
---
**K-Nearest Neighbors**

- L'approccio K-Nearest Neighbors è algoritmico: (parto da un certo numero di punti e vedo performance...)
  - Fissiamo $K$ e consideriamo una ipersfera attorno a un punto $x$ dove vogliamo stimare $p(x)$.
  - Aumentiamo poi il raggio di questa ipersfera fino a quando esattamente $K$ punti dal training set sono dentro di essa.
  - Calcoliamo poi $p(x) = \frac{K}{NV}$ per $V$ uguale al volume dell'**ipersfera** risultante.

	28
---
**K-Nearest Neighbors**

- Questo approccio è **discontinuo** e **rumoroso** per la ==stima della densità==:

	![[Pasted image 20251105230215.png]]

	29
---
**K-Nearest Neighbors Classification**

- L'approccio K-Nearest Neighbors (KNN) è un metodo molto conveniente per la classificazione, tuttavia.
- Intuitivamente, facciamo una stima di densità KNN per ogni **densità condizionata** alla classe, e poi applichiamo la Regola di Bayes.
- Supponiamo di avere $N_k$ esempi da ogni classe $k$ (quindi $\sum_{k} N_k = N$).
- Per classificare un nuovo punto $x$ facciamo il trucco dell'ipersfera assumendo che il volume necessario attorno a $x$ per includere $K$ punti sia $V_x$.
- Se in questa ipersfera abbiamo $K_k$ punti dalla classe $k$: $$p(x | C_k) = \frac{K_k}{N_k V_x}$$ conto i punti di una certa classe e divido per un fattore costante

- La **densità marginale** e i prior di classe sono similmente stimati:$$p(x) = \frac{K}{N V_x} \quad p(C_k) = \frac{N_k}{N}$$ => ho tutti gli strumenti per ottenere una posterior!

	30
---
K-Nearest Neighbors Classification

- Entra Bayes:$$p(C_k | x) = \frac{p(x | C_k) p(C_k)}{p(x)} = \frac{K_k}{K}$$
	![[Pasted image 20251105230403.png]]
	=> ogni classe prende un "voto" a seconda del kernel scelto => ottengo anche un classificatore non lineare! => è un classificatore bayes optimal nel limite di infiniti dati

	31
---

## Considerazioni Conclusive
---
**Metodi locali**

- In questa lezione abbiamo visto diversi metodi nonparametrici e locali per:
   - Stimare densità (Kernel Density Estimation).
   - Regressione (Nadaraya-Watson)
   - Classificazione (K-Nearest Neighbors).

- Queste tecniche sono semplici e intuitive e spiegabili.

- Hanno un piccolo (ma importante!) numero di iperparametri: il bandwidth del kernel $h$ (spesso più di uno), o il numero di vicini $K$.

- Questi metodi hanno belle proprietà di convergenza (es. K-Nearest Neighbors è quasi-ottimale per $K = 1$ quando $N \to \infty$).
- Questi metodi tuttavia hanno un enorme svantaggio pratico?

- *L'ha visto qualcuno già?*

	32
---
**Inefficienza spaziale**

- Per fare previsioni, tutti questi metodi richiedono che tutti i dati di training siano disponibili al momento dell'inferenza.
- In pratica, tipicamente usiamo una struttura dati (es. un KD-tree o Ball-Tree) per recuperare efficientemente e approssimativamente i $K$ punti in $D$ più vicini a un punto $x$.

	![[Pasted image 20251105230608.png]]
	
	33
---
**Letture e Compiti**

- Lettura Raccomandata:
	- Bishop: Capitolo 2 (2.5), Capitolo 6 (6.3)
	- Guida Utente di Scikit-learn (sezioni 2.8, 1.3, 1.6)

 - Compiti:
	1. Prova un classificatore K-Nearest Neighbor sui problemi di classificazione (sintetici e reali) del laboratorio sulla Classificazione. Visualizza il confine decisionale e osserva le differenze qualitative (con $K$ variabile) tra esso e quello di una SVM o un classificatore generativo Bayesiano.
	2. Implementa il Nadaraya-Watson Kernel Regressor con un Kernel Gaussiano. Usalo per stimare un regressore per l'esempio nel laboratorio di Regressione Lineare. Come dovrebbe essere regolato il parametro di bandwidth $h$?

	34

# 20 - Introduzioni al Deep Learing

![[20-IntroDeepLearning.pdf]]

# 21 - Deep Learning e algoritmo di Backpropagation

## Introduzione
---
**Obiettivi della lezione**

Dopo questa lezione saprete:

- Capire come le reti ReLU (con almeno uno strato nascosto) possano approssimare con precisione desiderata qualsiasi funzione continua su un dominio compatto.
- Capire come la **backpropagation** possa essere usata per calcolare in modo automatico ed efficiente i gradienti delle reti neurali.
- Capire alcune delle insidie dell'Algoritmo di Backpropagation e come vengono mitigate nella pratica.

+Sketch => gli hidden layer preactivations non dipendono da tutti i parametri del modello! => se dunque vogliamo calcolare il gradiente $\nabla_{\theta} f(\mathbf{x}, \theta)$ potremmo suddividere questo secondo la chain rule su più parti => $$= \sigma' (f_{out}(\mathbf{z}, \theta)) \nabla_{\theta}f_{out}(\mathbf{z},\theta) = \sigma' (f_{out}(\mathbf{z}, \theta)) f'_{out}(\mathbf{z},\theta)\sigma' (f_{h}(\mathbf{x}, \theta))f'_h(\mathbf{x},\theta)$$ => Ho un prodotto fra derivate di funzioni lineari e funzioni di attivazione => a seconda del numero di layer avrò sempre più livelli della chain rule...

+Occhio però che se ho valori molto grandi (o molto piccoli) per la funzione di attivazione (caso della sigmoide) la loro derivata tende a zero => ho problemi di underflow/overflow in precisione! => *vanishing gradients* => bisogna stare attenti al magnitude dei valori per le funzioni di attivazione!

	2
---

## Le Reti Neurali sono Approssimatori Universali di Funzioni
---
**Una funzione di esempio**

- Considera una funzione $f[x, \phi]$ che mappa un input scalare $x$ a un output scalare $y$.
- Questa funzione ha dieci parametri $\phi = \{ \phi_0, \phi_1, \phi_2, \phi_3, \theta_{10}, \theta_{11}, \theta_{20}, \theta_{21}, \theta_{30}, \theta_{31} \}$ (ho dei pesi e i bias dei layer nascosti) => ho un solo hidden layer e 3 neuroni
- La definizione di $f[x, \phi]$ è: $$y = f[x, \phi]$$$$= \phi_0 + \phi_1 \sigma [\theta_{10} + \theta_{11}x] + \phi_2 \sigma [\theta_{20} + \theta_{21}x] + \phi_3 \sigma [\theta_{30} + \theta_{31}x]$$
- La funzione di attivazione $\sigma$ che considereremo sarà l'Unità Lineare Rettificata (ReLU): $$\sigma[z] = \text{ReLU}[z] = \max(0, z) = 
\begin{cases} 
0 & \text{se } z < 0 \\
z & \text{altrimenti}
\end{cases}$$+ Sketch relu => ha discontinuità in zero ma fino a che hai input positivi ottieni derivate lineari.
---
**Una funzione di esempio**

- Implementiamo questa funzione e vediamo quale famiglia rappresenta:

```python
def random_parameters(hidden=4):
  W1 = np.random.normal(size=(hidden,1))
  b1 = np.random.normal(size=(hidden,1))
  W2 = np.random.normal(size=(hidden,1))
  b2 = np.random.normal()
  return (W1, b1, W2, b2)

def relu(z):
    return np.maximum(z, 0.0)

def f(x, W1, b1, W2, b2):
    return W2.T @ relu((W1*x.T + b1)) + b2
```

---
**Una funzione di esempio**

- Visualizzando alcune istanze casuali:
	![[Pasted image 20251118090954.png]] => piecewise linear functions

---
**Una funzione di esempio**

- Questa funzione rappresenta la famiglia parametrica di funzioni con al **massimo quattro segmenti lineari**. => regioni in cui la funzione è lineare
- Cioè, la famiglia di funzioni lineari a tratti con fino a quattro regioni lineari. => applicando ReLU ne aggiungo quindi la non linearità (mantenendo magnitudine e direzione)
- È utile scomporre il calcolo di $f[x, \phi]$ calcolando prima le quantità nascoste: 
	- $h_1 = \sigma [\theta_{10} + \theta_{11}x]$
	- $h_2 = \sigma [\theta_{20} + \theta_{21}x]$
	- $h_3 = \sigma [\theta_{30} + \theta_{31}x]$.

- Poi le combiniamo con: $$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$$
---
**Una rete superficiale (shallow)**

- Ogni regione lineare corrisponde a un pattern di attivazione nelle unità nascoste.
- Quando un'unità viene "clippata" dall'attivazione ReLU, la definiamo inattiva.
- La pendenza di ogni regione è determinata dalle pendenze originali $\theta_{*1}$ degli input attivi per questa regione e dai pesi $\phi_{*}$ applicati successivamente.
- Ogni unità nascosta contribuisce con un "gomito" (joint) alla funzione, quindi con tre unità nascoste possono esserci quattro regioni lineari.

---
**Il Teorema di Approssimazione Universale (versione shallow)**

- Se generalizziamo questo a $D$ unità nascoste: $$h_d = \sigma[\theta_{d0} + \theta_{d1}x] \text{ per } d \in \{1, \ldots, D\}$$
- E le combiniamo nello stesso modo: $$y = \phi_0 + \sum_{d=1}^{D}\phi_d h_d$$
- Il numero di unità nascoste in una rete shallow è una misura della capacità della rete. => quante piecewise region functions posso creare! => sostanzialmente creo dei pezzettini che mi approssimano la funzione a seconda delle hidden units usate (+ sketch) => anche se come visto prima non funziona per tutti ma varia a seconda dei parametri di quanti neuroni mi rimangono attivi.
- Con capacità sufficiente, una rete shallow può descrivere qualsiasi funzione continua 1D definita su un sottoinsieme compatto della retta reale con precisione arbitraria.

---
**Il Teorema di Approssimazione Universale (versione shallow)**

- Cosa succede se aumentiamo il numero di unità nascoste a 1000?
	![[Pasted image 20251118092143.png]]

	9
---
**L'Umile Rete Neurale**

- Ovviamente stiamo descrivendo la stessa architettura che già conosciamo:
	![[Pasted image 20251118092218.png]](magari oltre alla depth posso anche anche aumentare la width della mia hidden layer

- Di solito pensiamo in termini di figure più semplice sulla destra
- Importante: Il teorema di approssimazione Universale dice che esiste una rete con un singolo hidden layer per qualche D unità nascoste che approssima qualsiasi funzione continua $f$ per ogni precisione desiderata

	10
---

## L'Algoritmo di Backpropagation
---
**Un'altra rete giocattolo**

- Considera la seguente funzione: $$f[x, \phi] = \beta_3 + \omega_3 \cdot \cos \left[ \beta_2 + \omega_2 \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 x \right] \right] \right]$$

- Questa è una composizione delle funzioni $\cos[\bullet], \exp[\bullet], \sin[\bullet]$.
- Con parametri $\phi = \{\beta_0, \omega_0, \beta_1, \omega_1, \beta_2, \omega_2, \beta_3, \omega_3\}$.
- Supponiamo di avere una funzione di perdita ai minimi quadrati: $\ell_i = (f[x_i, \phi] - y_i)^2$. (single sample loss)
- E che conosciamo i valori correnti di $\beta_0, \beta_1, \beta_2, \beta_3, \omega_0, \omega_1, \omega_2, \omega_3, x_i$, e $y_i$.
- Potremmo ovviamente calcolare $\ell_i$, ma siamo invece interessati a calcolare come piccoli cambiamenti nei parametri $\phi$ cambino $\ell_i$.

	11
---
**Il calcolo manuale è una rottura**

- Potremmo calcolare le espressioni per le derivate parziali a **mano**:

$\frac{\partial \ell_i}{\partial \omega_0} = -2 \left( \beta_3 + \omega_3 \cdot \cos \left[ \beta_2 + \omega_2 \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 \cdot x_i \right] \right] \right] - y_i \right)$

$\omega_1 \omega_2 \omega_3 \cdot x_i \cdot \cos \left[ \beta_0 + \omega_0 \cdot x_i \right] \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 \cdot x_i \right] \right]$

$\cdot \sin \left[ \beta_2 + \omega_2 \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 \cdot x_i \right] \right] \right]$.

- Ma questo è ==una rottura== e – cosa più importante – estremamente ridondante! (also error prone)

- Vediamo se possiamo derivare un algoritmo generico per calcolare le derivate di funzioni come questa...

	12
---
**Il Grafo Computazionale di** $f[x, \phi]$

- La chiave sta nel modo in cui scomponiamo questa composizione di funzioni:  
  $f[x, \phi] = \beta_3 + \omega_3 \cdot \cos \left[ \beta_2 + \omega_2 \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 x \right] \right] \right]$

+Metti sketch (potrei fare la stessa cosa con le matrici al posto dei scalare)
+Faccio quindi anche il calcolo della loss => come la minimizzo? => come ne calcolo il gradiente? => faccio backpropragation => per calcolare la derivata parziale sfrutto la chain rule ma anche per calcolare la derivata parziali dell'output ne rifaccio la chain rule! => tornando indietro ad ogni layer => questo sarà dipendente dall'activation fino a quel punto! => il forward pass è quindi salvarsi tutte le funzioni di attivazioni => mentre il backward pass è come faccio il calcolo delle mie derivate parziali

	13
---
**FORWARD: Scomporre il grafo del calcolo**

- Per primo, scriviamo il calcolo di $\ell_i$ come una sequenza di passi intermedi:
	- $f[x_i, \phi] = \beta_3 + \omega_3 \cdot \cos \left[ \beta_2 + \omega_2 \cdot \exp \left[ \beta_1 + \omega_1 \cdot \sin \left[ \beta_0 + \omega_0 x_i \right] \right] \right]$
	- $f_0 = \beta_0 + \omega_0 x_i$
	- $h_1 = \sin [f_0]$
	- $f_1 = \beta_1 + \omega_1 h_1$
	- $h_2 = \exp [f_1]$
	- $f_2 = \beta_2 + \omega_2 h_2$
	- $h_3 = \cos [f_2]$
	- $f_3 = \beta_3 + \omega_3 h_3 \, (\equiv f[x_i, \phi])$
	- $l_i = (f_3 - y_i)^2$

	14
---
**BACKWARD: La regola della catena**

- Successivamente, calcoliamo le derivate di $\ell_i$ rispetto alle quantità intermedie **in ordine inverso**:  $$\frac{\partial \ell_i}{\partial f_3}, \quad \frac{\partial \ell_i}{\partial h_3}, \quad \frac{\partial \ell_i}{\partial f_2}, \quad \frac{\partial \ell_i}{\partial h_2}, \quad \frac{\partial \ell_i}{\partial f_1}, \quad \frac{\partial \ell_i}{\partial h_1}, \quad \text{e} \quad \frac{\partial \ell_i}{\partial f_0}$$
- La prima di queste è semplice:$$\frac{\partial \ell_i}{\partial f_3} = 2(f_3 - y)$$
- Lavorando all'indietro, la seconda può essere calcolata usando la regola della catena: $$\frac{\partial \ell_i}{\partial h_3} = \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3}$$ => ma la prima di queste l'ho già calcolata! (parte a destra)
---
**BACKWARD: Intuizione**

- Questo primo passo all'indietro è: $$\frac{\partial \ell_i}{\partial h_3} = \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3}$$
- Il lato sinistro chiede come $\ell_i$ cambia quando $h_3$ cambia.
- Il lato destro dice che possiamo scomporre questo in:
  1. Come $\ell_i$ cambia quando $f_3$ cambia; e
  2. Come $f_3$ cambia quando $h_3$ cambia.

- Otteniamo una **catena di eventi**: $h_3$ cambia $f_3$, che cambia $\ell_i$, e le derivate rappresentano gli effetti di questa catena.
- Nota che abbiamo già calcolato $f_3$ e la prima di queste derivate $2(f_3 - y)$.

---
**BACKWARD: Continuiamo semplicemente**

- Continuiamo a calcolare le derivate dell'output rispetto alle quantità intermedie: 
	- $\frac{\partial \ell_i}{\partial f_2} = \frac{\partial h_3}{\partial f_2} \left( \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3} \right)$
	- $\frac{\partial \ell_i}{\partial h_2} = \frac{\partial f_2}{\partial h_2} \left( \frac{\partial h_3}{\partial f_2} \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3} \right)$
	- $\frac{\partial \ell_i}{\partial f_1} = \frac{\partial h_2}{\partial f_1} \left( \frac{\partial f_2}{\partial h_2} \frac{\partial h_3}{\partial f_2} \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3} \right)$
	- $\frac{\partial \ell_i}{\partial h_1} = \frac{\partial f_1}{\partial h_1} \left( \frac{\partial h_2}{\partial f_1} \frac{\partial f_2}{\partial h_2} \frac{\partial h_3}{\partial f_2} \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3} \right)$
	- $\frac{\partial \ell_i}{\partial f_0} = \frac{\partial h_1}{\partial f_0} \left( \frac{\partial f_1}{\partial h_1} \frac{\partial h_2}{\partial f_1} \frac{\partial f_2}{\partial h_2} \frac{\partial h_3}{\partial f_2} \frac{\partial f_3}{\partial h_3} \frac{\partial \ell_i}{\partial f_3} \right)$

	17
---
**BACKWARD: Ma... la loss? E la forward pass?!**

- Dobbiamo ancora calcolare come la perdita $\ell_i$ cambia in termini di cambiamenti ai parametri $\beta_k$ e $\omega_k!$

- Ancora una volta, applichiamo la regola della catena: $$\frac{\partial l_i}{\partial \beta_k} = \frac{\partial f_k}{\partial \beta_k} \frac{\partial \ell_i}{\partial f_k}$$$$\frac{\partial l_i}{\partial \omega_k} = \frac{\partial f_k}{\partial \omega_k} \frac{\partial \ell_i}{\partial f_k}$$

- E ancora: abbiamo già calcolato $\frac{\partial \ell_i}{\partial f_k}$!
- Per $k > 0$ abbiamo:$$\frac{\partial f_k}{\partial \beta_k} = 1 \text{ e } \frac{\partial f_k}{\partial w_k} = h_k$$
	18
---
**L'Algoritmo di Backpropagation Illustrato**

- Passo 1: Calcola la forward pass (passaggio in avanti).
	![[Pasted image 20251118095135.png]]

- Passo 2: Propaga all'indietro i gradienti delle attivazioni intermedie.
	![[Pasted image 20251118095144.png]]

- Passo 3: Calcola le derivate parziali finali.
	![[Pasted image 20251118095200.png]]

+metti sketch => derivata rispetto al bias... è 1!! => avrò sempre prodotti di qualcosa che abbiamo già e derivata parziale rispetto al parametro considerato! => che appunto nel caso lineare abbiamo bisogno di queste nel forward activation, mentre per i bias no siccome la loro derivata è 1

	19
---
## Riflessioni sulla Backpropagation
---
**Riflessioni: problemi con la backprop**

- Se l'algoritmo di backpropagation è così "semplice", perché non abbiamo usato le reti neurali dagli anni '70?
- Ci sono una serie di problemi:
  - **Unità saturanti**: molte funzioni di attivazione sono "piatte" nei loro valori estremi – questo risulta in gradienti quasi zero.
  - **Gradienti che svaniscono (Vanishing gradients):** la backprop crea una lunga catena di gradienti moltiplicati – tutti tipicamente molto piccoli. => gradient starts collapsing!

- Soluzione Parziale: usare funzioni di attivazione non saturanti:
	![[Pasted image 20251118095932.png]]

	20
---
**Riflessioni: altri problemi con la backprop**

- Un altro problema è l'overparameterization: i (molto spesso) numerosi parametri nelle reti neurali possono portare a un facile overfitting.
- Buon esercizio: contare il numero di pesi in un MLP (Multi-Layer Perceptron).
- Soluzione parziale: usare la regolarizzazione per controllare la magnitudine dei pesi nella rete.

	21
---
**Riflessioni: Discesa Stocastica del Gradiente (SGD)** skipped

- Problema: cosa succede se $N$ (il numero di campioni di training) è molto grande?
- Beh, finiamo per fare passi molto lenti – ogni iterazione della discesa del gradiente è una media sull'intero dataset.
- Soluzione: approssimare il gradiente vero con il gradiente su un singolo esempio di training.

 - **Discesa Stocastica del Gradiente Online**
	- Scegli un vettore iniziale di parametri $\theta$ e un learning rate $\eta$.
	- Ripeti fino a quando non viene trovato un minimo approssimativo:
	   1. Mescola casualmente i campioni di training in $D$.
	   2. Per ogni $(x,y)\in D$:
		    $\theta := \theta - \eta \nabla_\theta \mathcal{L}(\{x,y\};\theta)$

	22
---
**Riflessioni: Discesa Stocastica del Gradiente (continua)**

- Un altro problema: valutare il gradiente su esempi singoli porta a passi molto rumorosi nello spazio dei parametri.
- Un trucco per mitigare questo è usare il momentum: mantenere una media mobile dei gradienti che viene aggiornata lentamente.
- Un'altra soluzione è usare i mini-batch: invece di un singolo campione, fare la media dei gradienti su un piccolo batch di campioni.
- È comune usare una combinazione di mini-batch e momentum per stabilizzare l'addestramento.

	23
---
**Riflessioni: Terminologia**

- Alcuni termini utili per l'ottimizzazione nel deep learning:
  - 1 epoca (epoch): un passaggio completo sui dati.
  - 1 iterazione: un singolo passo di gradiente.
  - N: numero di campioni di training.
  - B: dimensione del batch (batch size).

| Algoritmo                 | Iterazioni per epoca |
|---------------------------|---------------------|
| Batch Gradient Descent    | 1                   |
| Stochastic Gradient Descent (SGD) | $N$             |
| Mini-batch Gradient Descent | $\frac{N}{B}$   |

	24
---
## Discussione
---
**Riflessioni sulla backpropagation**

- Il riutilizzo efficiente di calcoli parziali durante il calcolo dei gradienti nei grafi computazionali è stato scoperto ripetutamente [Werbos (1974), Bryson et al. (1979), LeCun (1985), e Parker (1985)].

- La descrizione più celebre di questa idea fu di Rumelhart et al. (1985), che coniarono anche il termine "backpropagation".

- Questo lavoro diede il via a una nuova fase della ricerca sulle reti neurali: per la prima volta, era *pratico addestrare reti con strati nascosti*.

- I progressi si bloccarono a causa (in retrospettiva) della mancanza di dati di addestramento, della potenza computazionale limitata e dell'uso di attivazioni sigmoide.

- Applicazioni come NLP e Computer Vision non si basarono su modelli di reti neurali fino ai notevoli risultati di classificazione delle immagini di Krizhevsky et al. (2012).

	25
---
**Le reti neurali e le vicissitudini della storia**

- La ricerca sulle reti neurali fu effettivamente bloccata dal circa 1969 fino agli anni '80.
- Le difficoltà nell'addestrare le reti (anche quelle con un solo strato nascosto) ne impedirono l'uso e lo sviluppo diffusi.
- Esse rappresentano, tuttavia, una famiglia estremamente potente di funzioni che possiamo usare per modellare mappature complesse e non lineari dall'input all'output.
- Addestrarle richiede ancora una delicata combinazione di arte, background matematico e molta pazienza.
- La scoperta dell'algoritmo di backpropagation fu una pietra miliare importante, e per usare (e debugare) efficacemente i loop di addestramento, è essenziale sapere come funziona.

	26
---
**La Strada Avanti**

- Nella prossima lezione esamineremo alcune diverse architetture per le Reti Neurali Profonde (Deep Neural Networks).
- Nello specifico, vedremo come le Reti Neurali Convoluzionali (CNNs) possono essere usate per processare efficientemente i dati immagine.
- E vedremo come le CNNs sono in realtà solo Multilayer Perceptrons travestiti.
- Esamineremo anche più da vicino alcune delle insidiLa Strada Avantie nell'addestrare reti profonde, e il bagaglio di trucchi che usiamo per evitarle (o per uscirne).

	27

# 22 - CNN - Convolutional Neural Networks

## Una Critica della Ragion Pura
---

[[22-CNNs.pdf]]

- Sono principalmente immagini 

	2-13
---
**Riconoscimento visivo: modelli impliciti**

- Consideriamo una configurazione più o meno standard di apprendimento supervisionato per la classificazione visiva.
- Possiamo immaginare una semplice pipeline come quella qui sotto.
- Ogni fase ha il suo spazio di progettazione e scelte critiche da compiere.
- Questo appealed allo scienziato informatico in noi poiché stiamo effettivamente dividendo, modularizzando e (si spera) conquistando.

	![[Pasted image 20251125143604.png]]
	
	14
---
**Riconoscimento visivo: perché è difficile?**

- È apparso un articolo nel 2000 che riassumeva lo stato dell'arte nel riconoscimento visivo [Smeulders et al., 2000].
- Ha introdotto il divario sensoriale nella conversazione sul riconoscimento visivo:

*Il divario sensoriale è il divario tra l'oggetto nel mondo e le informazioni in una descrizione (computazionale) derivata da una registrazione di quella scena.*

- Pensateci un momento: lavoriamo sempre con una ricostruzione imperfetta del mondo reale.
- Le immagini hanno una risoluzione finita, sono soggette a rumore, sono acquisite con un sensore che è un altro oggetto libero nel mondo.
- Questo divario sensoriale deve essere superato per rendere il riconoscimento degli oggetti invariante rispetto agli artefatti incidentali della scena.

	15
---
**Il divario semantico**

- L'altro concetto chiave è il divario semantico:

*Il divario semantico è la mancanza di coincidenza tra le informazioni che si possono estrarre dai dati visivi e l'interpretazione che gli stessi dati hanno per un utente in una data situazione.*

![[Pasted image 20251125143921.png]]

	16
---
**Il divario semantico**

![[22-CNNs.pdf]]

- Immagine dell'illusione di Adelson: scacchiera con quadrati A e B che appaiono di grigio diverso ma sono identici
- Oppure fragole rosse ma non ci sono pixel rossi nell'immagine

	17-18-19
---
**Contesto storico: Borsa delle Caratteristiche (Bag of Features)**

- Questo era lo stato dell'arte nel 2011:
	
	![[Pasted image 20251125144404.png]]

	19
---
**Contesto storico: Questo era un "gatto"**

![[Pasted image 20251125145819.png]]

	20
---
**Contesto storico: Ora "impara"**

- Ad ogni rappresentazione di immagine era associata una (o più) etichette.
- Poi le forniamo in input ad una SVM multi-classe.

	![[Pasted image 20251125145850.png]]

	21
---
**Contesto storico: Una ricetta**

- Poi restituiva i confini decisionali ottimali tra tutte le classi (e tutte le altre).
- Il processo è importante:
  1. Primo: estrarre una rappresentazione artigianale di punti fiduciali.
  2. Poi: codificarli in una rappresentazione globale dell'immagine.
  3. Poi: adattare una SVM (con o senza kernel).

- Pro: l'apprendimento effettivo ha pochi iperparametri (di solito solo uno).
- Contro: molti elementi artigianali con molti (praticamente infiniti) iperparametri.
- Contro: l'apprendimento è separato dalla rappresentazione.

	22
---
**Obiettivi della lezione**

Alla fine della lezione dovreste:

- Comprendere le motivazioni storiche del *problema generale della visione artificiale* e il ruolo centrale svolto dal divario semantico.
- Comprendere le differenze e le somiglianze tra le architetture dei modelli Perceptron Multistrato (MLP) e Rete Neurale Convoluzionale (CNN).
- Comprendere alcuni dei recenti sviluppi storici e delle innovazioni tecnologiche che hanno reso possibile il *Rinascimento del Deep Learning*.
- Comprendere le due famiglie fondamentali di architetture CNN e cosa le distingue l'una dall'altra.
- Comprendere alcuni dei "trucchi" necessari per rendere le CNN efficaci nella pratica.

	23
---

## Connectionismo: Da MLP a CNN
---
**L'attrattiva dell'apprendimento end-to-end**

- Gli MLP hanno una serie di caratteristiche estremamente attraenti:
  - È un modello end-to-end: possiamo addestrare tutto nel modello utilizzando un unico algoritmo di ottimizzazione.
  - Gli MLP apprendono rappresentazioni dell'input e del classificatore.

- Perché non possiamo semplicemente usare questo modello per i problemi di riconoscimento delle immagini?
- Un MLP dovrebbe essere in grado di apprendere rappresentazioni di caratteristiche che a loro volta sono buone rappresentazioni per la classificazione.
- Perché questo è problematico?
- NOTA: Il trattamento e molte figure in questa sezione sono tratti dall'eccellente libro *Understanding Deep Learning*, di Simon Prince.
- Raccomando caldamente questo libro.

	24
---
**Su invarianza ed equivarianza**

- Una funzione $f[x]$ è invariante alla trasformazione $t[x]$ se $f[t[x]] = f[x]$.
- Una funzione $f[x]$ è equivariante alla trasformazione $t[x]$ se $f[t[x]] = t f[x]$.

	![[Pasted image 20251125150129.png]]

	25
---
**Convoluzioni unidimensionali**

- L'operatore di convoluzione calcola una somma pesata dei valori vicini: $$h_i = \sigma[\beta_i + w_1x_{i-1} + w_2x_i + w_3x_{i+1}]$$$$= \sigma[\beta + \sum_{j=1}^3 w_jx_{i+j-1}]$$
	![[Pasted image 20251125150224.png]]
	
	26
---

![[22-CNNs.pdf]]


	26-30
---
**Da MLP a CNN (che sono ancora in realtà MLP)**

- Un layer convoluzionale è un layer fully-connected con i pesi condivisi tra le diverse posizioni dell'immagine.
- L'input di dimensione $w \times h \times c$ viene trasformato in un output di dimensione $w \times h \times c'$.
- Gli output sono chiamati mappe di caratteristiche e sono derivati dalla convoluzione dell'immagine con $d'$ tensori 3D di dimensione $u \times v \times d$.
- Quindi, il numero di parametri è "solo" $(u * v * c' * c) + c'$.

	![[Pasted image 20251125150518.png]]

	31
---
**Una CNN è davvero un MLP (travestito)**
- Ma quello non sembra affatto un MLP…

	![[Pasted image 20251125150610.png]]

	32
---
**L'ingrediente finale: Layer di Pooling**

- L'apprendimento di rappresentazioni funziona creando un collo di bottiglia semantico.
- Forziamo la rete ad estrarre rappresentazioni significative che catturino caratteristiche semanticas.
- Nelle CNN lo facciamo tramite Sotto-campionamento, Max Pooling e Mean Pooling:

	![[Pasted image 20251125150657.png]]

- Ora esamineremo alcune architetture CNN reali che renderanno tutto più chiaro.

	33
---

## AlexNet: Lo sparo che si è sentito in tutto il mondo
---
**AlexNet: Contesto**

- Daremo ora un'occhiata alla submission della International Large Scale Visual Recognition Competition (ILSVRC) che ha cambiato tutto [Krizhevsky et al., 2012].
- Questa architettura affronta sistematicamente la maggior parte dei problemi legati all'addestramento di grandi architetture di rete su grandi dataset.
- È una Rete Neurale Convoluzionale (CNN) universalmente chiamata AlexNet.
- È anche una Rete Profonda perché ha molti layer nascosti.


	34
---
**AlexNet: L'Architettura**

-  Esaminiamo prima l'architettura complessiva e poi analizziamo in dettaglio come ogni componente affronta problemi specifici.
- È anche utile esaminare come i dati fluiscono attraverso la rete.

	![[Pasted image 20251125150842.png]]

	35
---
**AlexNet: Pooling delle Caratteristiche**

- Come nel modello Bag-of-Words, possiamo fare il pooling delle caratteristiche locali.
- AlexNet utilizza regioni di pooling $3 \times 3$ con un passo (stride) di 2 pixel.
  - Ciò significa che dopo alcuni layer convoluzionali la dimensione della mappa di caratteristiche è ridotta di un fattore 2.
  - Usano il max pooling: in ogni mappa di caratteristiche, mantieni il valore massimo in ogni regione di pooling $3 \times 3$ sovrapposta (in ogni mappa di caratteristiche).
  - Questo aiuta a contenere la dimensione delle mappe di caratteristiche propagate attraverso la rete.
  - E aiuta anche a costruire rappresentazioni di livello superiore dell'immagine.
  - Questo perché dimezzare la risoluzione dell'immagine equivale a raddoppiare la dimensione delle convoluzioni successive.

	36
---
**AlexNet: Saturazione delle Unità**

- Un'altra innovazione in AlexNet è l'uso della funzione di attivazione Rectified Linear Unit (ReLU). $$\sigma(x) = \max(0, x)$$
- Questa funzione di attivazione non satura come le sigmoidi.
- Il risultato è un accelerazione di 6 volte nell'addestramento.

	![[Pasted image 20251125151433.png]]
---
**AlexNet: Ridurre l'Overfitting**

- Anche con la condivisione dei pesi convoluzionali, AlexNet ha ancora 60M di parametri.
- Per ridurre l'overfitting, gli autori usano due trucchi extra (ormai standard):
  - Data augmentation: vengono generate traslazioni e riflessioni casuali delle immagini di input, più variazioni casuali nelle direzioni principali dello spazio RGB.
  - Dropout: un trucco avanzato della comunità delle Reti Neurali che rimuove casualmente metà degli input a layer selezionati durante il training.

	38
---
**AlexNet: Altri Trucchi**

- L'articolo su AlexNet è un'ottima risorsa perché spiega tutti i trucchi necessari per far apprendere una rete profonda:
  - Local response normalization: mantiene sotto controllo la variazione locale nelle mappe di caratteristiche (sezione 3.3).
  - Momentum: limita l'effetto "skateboard" quando si seguono valli nella superficie di loss, equivalente alla regolarizzazione L1 (o L2) dei pesi (sezione 5).
  - Mini-batch Stochastic Gradient Descent (SGD): con 1.2M campioni di training, non possiamo considerare l'intero dataset in un unico batch; invece, campioniamo casualmente mini-batch di 128 immagini (sezione 5).
  - Multiple GPUs: AlexNet era troppo grande per stare in una singola GPU (nel 2012), quindi le mappe di caratteristiche sono divise su due GPU (sezione 3.2).
  - Model averaging: i risultati state-of-the-art si ottengono addestrando multiple CNN e mediando gli output.

	39
---
**AlexNet: Risultati**

- La prova è nel pudding:

| Modello        | Top-1 (val) | Top-5 (val) | Top-5 (test) |
| -------------- | ----------- | ----------- | ------------ |
| SIFT + FVs [7] | —           | —           | 26.2%        |
| 1 CNN          | 40.7%       | 18.2%       |              |
| 5 CNNs         | 38.1%       | 16.4%       | 16.4%        |
| 1 CNN*         | 39.0%       | 16.6%       |              |
| 7 CNNs*        | 36.7%       | 15.4%       | 15.3%        |

- E nelle rappresentazioni che la rete apprende:

	![[Pasted image 20251125151534.png]]

	40
---
**AlexNet: Riflessioni**

- AlexNet ha sconvolto il mondo del riconoscimento degli oggetti.
- Molti elementi del modello non sono realmente nuovi.
- Tuttavia, questo è stato il primo lavoro a dimostrare in modo convincente come sistemi di riconoscimento oggetti all'avanguardia possano essere addestrati end-to-end su problemi reali.
- Ciò è stato reso possibile da una serie di sviluppi concomitanti:
  - La disponibilità di enormi quantità di dati annotati (ImageNet, con 1.2M immagini di training).
  - GPU moderne, che rendono le convoluzioni super veloci.
  - Decenni di persistente sviluppo teorico (ReLU, backprop veloce, dropout, ecc.).

	41
---
**Riflessioni: Le CNN sono davvero grandi**

- Una delle prime osservazioni che si possono fare sulle CNN è che hanno un ENORME numero di parametri.
- Anche reti state-of-the-art di dimensioni modeste possono avere dell'ordine di 150 milioni di parametri addestrabili.
- Adattare tali modelli richiede enormi quantità di dati di training etichettati.

	![[Pasted image 20251125151847.png]]

	42
---

## La Famiglia delle Reti Molto Profonde
---
**VGG: Convoluzioni piccole, più profondità**

- Ora che abbiamo AlexNet come punto di riferimento, possiamo guardare ad altre architetture CNN state-of-the-art.
- La Famiglia di Reti VGG (VGG = Visual Geometry Group di Oxford) è un raffinamento dello stile AlexNet di CNN [Simonyan e Zisserman, 2014].
- In questo lavoro gli autori hanno svolto un'esplorazione approfondita dello spazio dei parametri architetturali.
- Hanno variato iperparametri (es. numero di layer, dimensione delle convoluzioni, ecc.).
- E hanno stabilito un nuovo baseline per il riconoscimento oggetti basato su CNN.


	43
---
**VGG: L'impostazione**

- L'input alle reti è un tensore immagine fisso, $224 \times 224 \times 3$.
- Il valore medio RGB viene prima sottratto da tutte le immagini di training per centrare i dati. => pixelwise mean and std
- Tutte le **convoluzioni** hanno dimensione $3 \times 3 \times d$ o $1 \times 1 \times d$ (d è un numero arbitrario di mappe di caratteristiche) con un passo (stride) di 1. 
- L'idea è: se hai bisogno di convoluzioni più grandi, ==basta andare più in profondità.==
- Il max pooling viene eseguito su finestre non sovrapposte $2 \times 2$ con un passo di 2 (riduzione di 2x nella dimensione).
- Tutti i layer nascosti utilizzano una funzione di attivazione ReLU, ma **non effettuano la local response normalization.**

	44
---
**VGG: Le configurazioni**

- Sono state considerate le seguenti configurazioni:

	![[Pasted image 20251125152053.png]]
	=> l'ultima parte della rete è la stessa di AlexNet => FC-1000 è un classificatore
	=> sono comunque reti ancora più profonde e con ancora più parametri...
	
	45
---
**VGG: training**

- La procedura di addestramento è simile ad AlexNet:
  - L'addestramento viene effettuato ottimizzando l'obiettivo di regressione logistica multinomiale utilizzando la discesa del gradiente mini-batch.
  - Il training è stato regolarizzato con decadimento del peso (weight decay) => ovvero reg L2 e **dropout** sui primi due layer fully-connected.
  - Il learning rate è stato inizialmente impostato a $10^{-2}$ e diminuito di un fattore 10 quando l'accuratezza sul validation set smetteva di migliorare.
  - L'apprendimento è stato fermato dopo 370K iterazioni (74 epoche).

- Inizializzazione:
  - Le CNN sono estremamente sensibili all'inizializzazione dei pesi. => altrimenti il learning va molto più lentamente! => queste dipendono da numero di input-output e inizializzazione gaussiana
  - Per l'addestramento delle reti VGG, gli autori usano una combinazione di inizializzazione casuale e pre-training.


	46
---
**VGG: Dimensione dell'immagine di training**

- Nota che le immagini di training sono tutte scalate a $224 \times 224$ pixel prima di passarle attraverso la rete. => se le convoluzioni possono prendere qualsiasi input => non vale la stessa cosa per i layer fully connected => ai quali applichiamo flattened => tied to a single input size?
- Questo è lo stesso di AlexNet, e chiaramente può influenzare il contenuto dell'immagine introducendo artefatti (considera immagini ritratto). => questo perchè bisogna fare scaling
- Nelle reti VGG, le immagini vengono scalate *isotropicamente* in modo che la dimensione più piccola abbia una dimensione fissa.  => prendo una piccola parte dell'immagine
- Poi una sotto-immagine di dimensione $224 \times 224$ viene ritagliata casualmente dall'immagine scalata.
- Gli autori hanno valutato il ridimensionamento casuale tra **256** e 384 pixel per la dimensione più piccola. => dimensione più piccola sia della dimensione desiderata


	47
---
**VGG: Dimensione dell'immagine di test**

- Al momento del test, vengono valutate cinque strategie per il ridimensionamento dell'immagine:
  - Dense: la rete è completamente convolutionalizzata (lo spiegherò nella prossima slide), valutata densamente sull'immagine di input, e i risultati sono pooled globalmente.
  - Single-scale: viene utilizzata una singola scala isotropica.
  - Multi-scale: come al momento del training, le immagini vengono scalate a tre scale isotropiche discrete.
  - **Multi-crop**: da un output fully-convolutional vengono prese multiple ritagli (crop) casuali per il average pooling.  => strategia comune è fare random crops => e fare average del risultato


	48
---
**VGG: Fully-convolutionalization**

-  Di seguito è mostrato un diagramma di una tipica ConvNet.
- Come possiamo renderla ==indipendente dalla dimensione dell'immagine?==

![[Pasted image 20251125152232.png]]
=> Mlp che prende in input immagini di 224/32 = 7 x 224x32 = 7

- SI può pensare di considerare il primo layer di MLP come layer di convoluzione di dimensione 7x7x4096 (numero di output) => guardo a finestre di pixel di 7x7 e produco 4096 features per ogni patches => quello successivo come 1x1x4096 e infine 1x1x1000 => cosa fa convoluzione 1x1? considero tutti i pixel e faccio combinazione lineare di tutte le features! => a cui applico poi funzione di attivazione non lineare

	49
---
**VGG: Risultati**

- Anche considerando solo una singola scala di input, i risultati sono impressionanti.
- Nota: **più profondo è meglio**, LRN non aiuta, il jittering di scala al test time sì.

| Configurazione ConvNet (Tabella 1) | lato minore immagine train ($S$) | errore top-1 val. (%) | errore top-5 val. (%) |
| ---------------------------------- | -------------------------------- | --------------------- | --------------------- |
| A                                  | 256                              | 29.6                  | 10.4                  |
| A-LRN                              | 256                              | 29.7                  | 10.5                  |
| B                                  | 256                              | 28.7                  | 9.9                   |
| C                                  | 384                              | 28.1                  | 9.3                   |
| D                                  | [256;512]                        | 27.3                  | 8.8                   |
| E                                  | [256;512]                        | 27.0                  | 8.8                   |

	50
---
**VGG: Risultati**

- L'uso di **scale multiple** porta a performance ancora migliori:

	![[Pasted image 20251125152408.png]]

- Così come la fusione di multiple strategie di cropping:

	![[Pasted image 20251125152424.png]]

- Notare che sono tutti risultati fatti per una sola rete => non vengono ancora usati modelli unsamble

	51
---
**VGG: Noi versus Loro**

- Infine, la media di modelli (model averaging) su modelli multi-scala, multi-crop porta a performance state-of-the-art:

	![[Pasted image 20251125152504.png]]

	52
---
**VGG: Analisi**

- In questo articolo gli autori hanno migliorato significativamente rispetto alla generazione precedente andando più in profondità.
- Ancora una volta, la maggior parte delle idee non sono nuove, ma l'esplorazione sistematica dello spazio di progettazione ha portato a miglioramenti significativi.
- Nota che le reti sono più profonde, ma hanno un'impronta di memoria più piccola al momento del training grazie ad un bilanciamento attento della dimensione delle mappe di caratteristiche.
- La valutazione densa (dense evaluation) della rete al momento del test può anche aumentare le performance, portando a reti fully convolutional che sono indipendenti dalla dimensione dell'immagine di input.
- L'architettura è ancora una classica ConvNet.

	53
---

## Reti Residuali Profonde: Sempre più Profonde
---
**ResNets: Introduzione**

- Da quanto visto finora, sembra che reti più profonde generalizzino meglio.
- Quindi, possiamo semplicemente ==continuare ad impilare sempre più layer a==lla fine delle nostre CNN? => possiamo aumentare ancora le performance della rete?
- A parte le complicazioni computazionali (la memoria della GPU è finita), sembra che "dovrebbe funzionare e basta".
- Esamineremo ora la nostra ultima architettura di rete state-of-the-art (conosciuta come ResNet) che esamina questa questione in dettaglio [He et al., 2016].


	54
---
**ResNets: Più profondo non è meglio?**

- Pensiero pre-ResNet: *Le reti più profonde dovrebbero sempre performare meglio – almeno sui dati di training.*

![[Pasted image 20251127092244.png]]

=> notare che in realtà non stiamo overfittando => ma allora che succede?

	55
---
**ResNets: Aspetta, l'errore di training non dovrebbe essere più basso?**

- Usando una costruzione artificiale, vediamo che almeno l'errore di training non dovrebbe aumentare con la profondità.
- Basta copiare i pesi pre-addestrati da una rete normale in una rete più profonda con nuovi pesi inizializzati casualmente.

	![[Pasted image 20251127092336.png]]

	56
---
**ResNets: Obiettivi e Residui**

- Diciamo che la rete sta apprendendo verso una qualche rappresentazione di caratteristiche ottimale $H(x)$.
- La natura composizionale e feed-forward della CNN non aiuta realmente.

	![[Pasted image 20251127092420.png]]

=> Più calcolo i gradienti e più è probabile che alcuni di questi si azzerano!

	57
---
**ResNets: Obiettivi e Residui**

- Diciamo che la rete sta apprendendo verso una qualche rappresentazione di caratteristiche ottimale $H(x)$.
- La natura composizionale e feed-forward della CNN non aiuta realmente.
- Invece, possiamo aiutare la rete non richiedendole di passare attraverso tante informazioni.
- Passa $x$ in avanti e aggiungilo all'output del blocco residuo – ora abbiamo "solo" bisogno di apprendere $H(x) - x$, il residuo $F(x)$.

	![[Pasted image 20251127092657.png]]

- L'idea è di aggiungere una skip connection => in modo tale che l'ultimo blocco non calcola l'intero target => ma solo la differenza (residual) fra target e funzione calcolata

- Facendo questo ho un ulteriore calcolo da fare per il gradiente => aggiungo info

	57
---
**ResNets: Confronto**

-  Ecco un confronto di VGG19 e ResNet-34:

(Diagramma delle architetture a confronto, che mostra come ResNet-34 sia più profonda ma abbia una complessità computazionale simile a VGG-19)

![[Pasted image 20251127093025.png]]

=> rete ancora più connessa! (scaling fra i blocchi per il residual connection) => non mi porto avanti tutti i residui ma li calcolo via via => altrimenti denseNets

	58
---
**ResNets: Modularità Parametrica**

- E questo è un modo comune di rappresentare parametricamente le varie configurazioni ResNet:

	![[Pasted image 20251127093457.png]]

- Notare non è presente MaxPooling => ma strided convolutions (cazzata?)
- Infine non ho un fully connected MLP classifier => ma eseguo Average Pool =>  dove ogni vettore di pixel corrisponde al pixel di partenza => e di questi ne viene prese la media => avg pooling toglie quindi spatial dimension

	59
---
**ResNets: Risultati**

- **Le connessioni residue sono estremamente efficaci:**

![[Pasted image 20251127094001.png]]
=> Nelle ResNets, l'errore di training e test diminuisce all'aumentare dei layer, fino a 110 layer! 

	60
---
**ResNet: Risultati**

- E la prova, come sempre, è nel pudding:

	![[Pasted image 20251127094113.png]]
	=> Parto da shallow nets con SVM e vado avanti...

	Resnet a 152 layers... sarà vero?? => da ResNet 50 in poi non ottengo prestazioni molto migliori...
	
	61
---

## CNN: I Trucchi del Mestiere
---
**CNN: Come si addestrano le CNN?**

- Le CNN funzionano alla granCNN: I Trucchi del Mestierede, ma non è sempre rose e fiori farle funzionare.
- La comunità ha sviluppato una serie di trucchi, tecniche ed euristiche che si sono dimostrate utili.
- Esaminiamone alcuni.

	62
---
**CNN: Batch Normalization**

![[Pasted image 20251127094546.png]]

=> Okay dopo backprop faccio cambiamento ai pesi => ma fino a dove scendo di livelli nel fare i cambiamenti? 
=> boh non so come si passa a normalizzare e std il minibatch durante fase di training => aggiungo ulteriori parametri... => finito il training calcolo e salvo tutte le medie e le std dei vari layer per?...

	63
---
**CNN: Dropout (un'altra idea "folle")**

![[Pasted image 20251127095103.png]]

- Con una potenza di calcolo illimitata, il modo migliore per "regolarizzare" un modello di dimensione fissa è fare la media delle previsioni di tutte le possibili impostazioni dei parametri, pesando ogni impostazione in base ==alla sua probabilità a posteriori== dati i dati di training. => tipo bayesian viewpoint – Srivastava et al. [2014]

- Ci si rende conto che alcuni neuroni danno stesse info rispetto ad altri  (per metà del train questi non sono attivi) => posso pensare di eliminare metà delle attivazioni nel forward in modo randomico
- => oppure calcolare tutte le attivazioni ma dividerle per 2...

+ Model.eval() vs model.train() 

	64
---
**CNN: Cosa Sta Succedendo?**

- Ricordate che prima ho menzionato che uno dei pregiudizi contro l'uso delle reti neurali era la mancanza di interpretabilità.
- Non appena sono iniziati ad arrivare i risultati spettacolari delle CNN sul riconoscimento oggetti, i ricercatori hanno iniziato ad inventare nuovi modi per interpretare le viscere di queste enormi reti.
- Al giorno d'oggi ci sono molti strumenti e trucchi che puoi usare per capire cosa ha appreso la rete.

	65
---
**CNN: Cosa Sta Succedendo**

- Un lavoro pionieristico ha esaminato proprio questo problema e l'articolo contiene un sacco di analisi interessanti su come funzionano queste reti [Zeiler e Fergus, 2014].
- Parlerò solo di come le visualizzazioni delle attivazioni delle mappe di caratteristiche dimostrano cosa sta succedendo.

	![[Pasted image 20251127095620.png]]

	=> Dato il filtro => ottengo dei sample patches che rispondono a questi filtri... andando avanti con la rete ottengo immagini più  ragionevoli dal punto di vista semantico
	
	66
---
**CNN: Cosa Sta Succedendo**

- Man mano che andiamo più in profondità nella rete, le attivazioni delle caratteristiche corrispondono a semantiche di livello superiore.

	![[Pasted image 20251127100227.png]]

	=> Filtri che appunto vanno a guardare a caratteristiche dell'immagine...

	67
---
**CNN: Cosa Sta Succedendo**

- Fino a quando le caratteristiche non indicano realmente la presenza di "occhi" e "facce di gatto", ecc.

	![[Pasted image 20251127100406.png]]

	68
---
**CNN: Cosa Sta Succedendo**

- L'algoritmo Grad-CAM è un modo intuitivo per visualizzare, beh, cosa rende una mucca, una mucca [Selvaraju et al., 2017]:

![[Pasted image 20251127100438.png]]
=> ho una rete già addestrata in partenza => chiedo alla rete di mostrarmi dove si trova un particolare oggetto nell'immagine e questa cerca particolari feature in questa.

	69
---
**CNN: Cosa Sta Succedendo**

- L'algoritmo Grad-CAM è un modo intuitivo per visualizzare, beh, cosa rende una mucca, una mucca [Selvaraju et al., 2017]:

![[Pasted image 20251127100704.png]]

	69
---

## Discussione
---
**Discussione: Il peso della supervisione**

- Quanto valgono davvero 1.5M di annotazioni [Zhang et al., 2016]?

- Se le etichette sono equamente probabili, un insieme casuale di etichette ImageNet contiene circa $1.5\text{M} \ast \log_2(1000) \approx 15\text{Mbit}$.

	![[Pasted image 20251127110842.png]]

	=> Semantic gap => un sacco di info da comprimere in pochi bit... => extremely  easy to over fit! => se usiamo un piccolo dataset facile overfit
	
	70
---
**Discussione: Lo stato dell'arte**

- Abbiamo fatto molta strada in pochi anni.

	![[Pasted image 20251127111001.png]]
	
- Grafico di **Accuratezza Top-1 (%)** vs **Numero di Parametri**:
	- AlexNet: ~60% accuratezza, ~60M parametri
	- VGG-16: ~70% accuratezza, ~130M parametri  
	- ResNet-50: ~75% accuratezza, ~25M parametri
	- DenseNet-121: ~75% accuratezza, ~8M parametri

=> Ormai i transformes hanno billions di parametri! => giganteschi

	71
---
**Discussione: CNN e la strada da percorrere**

![[Pasted image 20251127111212.png]]

	72
---
**Bibliografia i**

- Riferimenti:
	- A. Canziani, A. Paszke, and E. Culurciello. An analysis of deep neural network models for practical applications. arXiv preprint arXiv:1605.07678, 2016.
	- M. A. Fischler and R. A. Elschlager. The representation and matching of pictorial structures. *IEEE Transactions on computers*, (1):67–92, 1973.
	- K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 770–778, 2016.
	- S. Ioffe and C. Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. arXiv preprint arXiv:1502.03167, 2015.
	- A. Krizhevsky, I. Sutskever, and G. E. Hinton. Imagenet classification with deep convolutional neural networks. In *Advances in neural information processing systems*, pages 1097–1105, 2012.

	73
---
**Bibliografia ii**

- D. Marr. Vision: A computational investigation into the human representation and processing of visual information, 1982.
- L. G. Roberts. *Machine perception of three-dimensional solids*. PhD thesis, Massachusetts Institute of Technology, 1963.
- R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra. Grad-cam: Visual explanations from deep networks via gradient-based localization. In *Proceedings of the IEEE International Conference on Computer Vision*, pages 618–626, 2017.
- K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. *arXiv preprint arXiv:1409.1556*, 2014.
- A. W. Smeulders, M. Worring, S. Santini, A. Gupta, and R. Jain. Content-based image retrieval at the end of the early years. *IEEE Transactions on Pattern Analysis & Machine Intelligence*, (12):1349–1380, 2000.
- N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov. Dropout: A simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research*, 15:1929–1958, 2014. URL http://jmlr.org/papers/v15/srivastava14a.html.

	74
---
**Bibliografia III**

- M. D. Zeiler and R. Fergus. Visualizing and understanding convolutional networks. In *European conference on computer vision*, pages 818–833. Springer, 2014.
- C. Zhang, S. Bengio, M. Hardt, B. Recht, and O. Vinyals. Understanding deep learning requires rethinking generalization. *arXiv preprint arXiv:1611.03530*, 2016.

	75
---

# 23 - CNN: Temi avanzati

![[23-CNNs-Part2.pdf]]