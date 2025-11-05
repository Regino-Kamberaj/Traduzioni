# 14 - Modelli Ensemble
## Introduzione
---
**Il potere del consenso**

- Tutti i modelli di regressione e classificazione che abbiamo considerato finora sono singoli – adattiamo un modello e prevediamo usando un modello.
- Spesso possiamo migliorare i modelli singoli combinandone multipli.
- Potremmo addestrare $M$ modelli, e poi prendere la media delle loro previsioni.
- Oppure, potremmo addestrare modelli in sequenza e incoraggiare i modelli successivi a compensare gli errori commessi dai precedenti.
- Oppure, potremmo addestrare modelli multipli e poi selezionare il migliore per fare previsioni per un dato $x$.
- Tali modelli sono solitamente chiamati modelli ensemble poiché fanno previsioni basate su un insieme di modelli addestrati invece che su uno solo.

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

- Abbiamo visto tempo fa in una delle nostre prime lezioni come il campionamento di modelli multipli e la media aiuti a ridurre la varianza:
- Possiamo sfruttare questo senza un modello completamente Bayesiano?

	![[Pasted image 20250930120423.png]]

	4
---
**Campionamento Bootstrap**

- Consideriamo un problema di regressione in cui stiamo prevedendo un singolo target continuo.
- L'approccio di riduzione della varianza funzionava addestrando un modello a basso bias su dataset multipli e mediando gli output.
- In pratica abbiamo solo un dataset, tuttavia.
- Il metodo bootstrap funziona campionando $M$ dataset di dimensione $N' < N$ da $D$ con reinserimento.
- Ognuno di questi dataset bootstrap riflette la distribuzione sottostante di $D$ ma è incompleto.

	5
---
**Bootstrap aggregation (o bagging)**

- Possiamo quindi adattare un modello $y_m(x)$ a ogni dataset bootstrap (usando qualsiasi metodo).
- E poi formare il modello committee mediando gli $M$ modelli base:$$y_{\text{com}}(x) = \frac{1}{M} \sum_{m=1}^{M} y_m(x)$$
- Indichiamo con $h(x)$ la vera funzione di regressione che genera $D$.
- L'output di ogni modello può essere scritto come questa funzione vera più un errore:$$y_m(x) = h(x) + \epsilon_m(x)$$
- Nota che non abbiamo ancora fatto nulla – eccetto identificare l'errore in ognuno dei nostri modelli.

	6
---
**Quantificare l'errore**

- L'errore quadratico atteso di ogni modello è allora:$$\mathbb{E}_x \left[ \{ h(x) - y_m(x) \}^2 \right] = \mathbb{E}_x \left[ \varepsilon_m(x)^2 \right]$$
- E l'errore medio dei modelli individuali è: $$E_{\text{av}} = \frac{1}{M} \sum_{m=1}^{M} \mathbb{E}_x \left[ \varepsilon_m(x)^2 \right]$$
- Ancora, non abbiamo detto nulla di sconvolgente: l'errore quadratico medio commesso dai modelli è la media di tutti gli errori quadratici commessi dai modelli.

	7
---
**L'errore del committee**

- Possiamo calcolare l'errore atteso del committee similmente:$$E_{\text{com}} = \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M h(x) - y_m(x) \right\}^2 \right]$$$$= \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M \varepsilon_m(x) \right\}^2 \right]$$

- OK, ma elevare al quadrato quella $\sum$ sarà un gran casino...

	8
---
**L'errore del committee**

- Come possiamo superare questo? Risposta: assunzioni!$$E_{\text{com}} = \mathbb{E}_x \left[ \left\{ \frac{1}{M} \sum_{m=1}^M \varepsilon_m(x) \right\}^2 \right]$$

- Se assumiamo che gli errori siano a media zero e non correlati:$$\mathbb{E}_x [\varepsilon_m(x)] = 0$$$$\mathbb{E}_x [\varepsilon_m(x)\varepsilon_l(x)] = 0 \quad m \neq l$$
- Allora abbiamo:$$E_{\text{com}} = \frac{1}{M} E_{\text{av}}$$
	9
---
**Mediare modelli riduce l'errore atteso**

- Quindi se mediiamo $M$ modelli riduciamo l'errore atteso dei modelli singoli di un fattore $1/M$!$$E_{\text{com}} = \frac{1}{M} E_{\text{av}}$$
- Ricorda le assunzioni, però: gli errori sono quasi mai non correlati.
- Tuttavia, ci sono garanzie che l'errore del committee non supererà mai l'errore atteso del modello (cioè $E_{\text{com}} \leq E_{\text{av}}$).

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

- Questo è precisamente ciò che fa il boosting:
	
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
## Modelli ad Albero
---
**Partizionamento ricorsivo dello spazio**

- Possiamo pensare alla classificazione (anche regressione) come fare previsioni costanti su partizioni dello spazio di input:
	![[Pasted image 20251104230905.png]]
	
	17
---
**Alberi Decisionali**

- I modelli ad albero sono modelli semplici ma *ampiamente usati* che funzionano per partizionamento.
- Gli alberi allineati agli assi partizionano lo spazio in cuboidi allineati con gli assi.
- Sono modelli ensemble: un singolo modello è responsabile per ogni partizione.
- Per selezionare quale modello attraversiamo l'albero in un processo decisionale sequenziale.
- I modelli ad albero sono spesso considerati interpretabili dagli umani.
- Il modello che consideriamo è il Classification and Regression Tree (CART).

	18
---
**Apprendere un modello ad albero**

- Consideriamo ancora un problema di regressione con dataset $D = \{ (x_1, t_1), \ldots, (x_N, t_N) \}$  
  dove ora i nostri $t_n$ sono target continui.

- Vogliamo partizionare lo spazio $\mathbb{R}^D$ in modo che in ogni partizione la nostra stima del target lì minimizzi l'errore quadratico.

- Questo è piuttosto facile: abbiamo solo bisogno della media dei target $t_n$ di tutti i punti $x_n$ che cadono in quella partizione.

- Il vero problema è *come dovremmo determinare questo partizionamento*.

- Ottimizzare su tutti i possibili partizionamenti è combinatorialmente intrattabile, anche per alberi allineati agli assi...

	19
---
**Apprendimento greedy**

- Invece, useremo una politica ricorsiva e greedy:
  1. Inizia da un singolo nodo radice corrispondente all'intero spazio.
  2. Itera su ognuna delle $D$ possibili variabili di split:
    - 2.1 Considera ogni possibile soglia per dividere i dati in due insiemi.
    - 2.2 Seleziona quella che minimizza la somma degli errori quadratici negli split.
  3. Applica ricorsivamente questa procedura ai figli.

- Quando dovremmo fermare questa procedura?
- La solita strategia è sovrasegmentare lo spazio di input costruendo un albero profondo e ampio.
- Perché questo potrebbe essere problematico?
- E poi potare l'albero per bilanciare complessità e minimizzazione dell'errore sui dati di training.

	20
---
**Apprendimento greedy**

- Assumiamo di avere già un partizionamento (un albero), con nodi foglia indicizzati da $\tau = 1, \ldots, T$.
- Chiama la partizione corrispondente a ogni foglia $R_\tau$.
- La previsione ottimale e l'errore quadratico in ogni nodo sono: $$y_\tau = \frac{1}{N_\tau} \sum_{x_n \in R_\tau} t_n \quad Q_\tau(T) = \sum_{x_n \in R_\tau} (t_n - y_\tau)^2$$
- Quindi possiamo definire un criterio di potatura come: $$C(T) = \sum_{\tau=1}^{|T|} Q_\tau(T) + \lambda |T|$$
	21
---
**Per problemi di classificazione**

- Se abbiamo un problema di classificazione, dobbiamo solo cambiare l'errore.
- Definisci $p_{\tau k}$ come la proporzione di campioni di classe $k$ al nodo $\tau$.
- Per esempio l'entropia incrociata negativa: $$Q_\tau(T) = \sum_{k=1}^K p_{\tau k} \ln p_{\tau k}$$
- O l'indice di Gini: $$Q_\tau(T) = \sum_{k=1}^K p_{\tau k}(1 - p_{\tau k})$$
	22
---
## Considerazioni Conclusive
---
**Il potere del consenso (e della diversità!)**

- I modelli ensemble sono un potente strumento per combinare modelli semplici in modelli migliori.
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
- Il modello risultante è tipicamente semplice (almeno finora):$$f(x; w, b) = w^T x + b$$
- Una caratteristica di queste tecniche è che la "conoscenza" appresa dai dati è completamente incapsulata nei parametri.
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
- Se hai un problema di classificazione bilanciato (come la maggior parte che vedremo nei laboratori), usa l'accuratezza del classificatore:

$accuracy = \frac{\# \text{ campioni di test classificati correttamente}}{\# \text{ campioni di test}}$

- Perché questa potrebbe essere una metrica cattiva se il problema è sbilanciato?

	4
---
**Valutare i Classificatori: Matrici di Confusione**

- Un buon strumento per avere una panoramica dei tipi di errori che un classificatore sta facendo è la matrice di confusione:
	![[Pasted image 20251105223309.png]]
	
	5
---
**Valutare i Classificatori: Problemi Sbilanciati**

- Iniziamo sezionando le classificazioni:
  - Veri positivi (TP): abbiamo predetto sì, e il campione appartiene alla classe.
  - Veri negativi (TN): abbiamo predetto no, e il campione non appartiene alla classe.
  - Falsi positivi (FP): abbiamo predetto sì, ma il campione non appartiene alla classe – anche noto come errore di Tipo I.
  - Falsi negativi (FN): abbiamo predetto no, ma il campione appartiene alla classe – anche noto come errore di Tipo II.

- Possiamo allora definire alcune metriche utili per problemi sbilanciati: $$\text{Precisione}(c) = \frac{\text{TP}}{\text{TP} + \text{FP}}$$$$\text{Recall}(c) = \frac{\text{TP}}{\text{TP} + \text{FN}}$$$$\text{F1}(c) = 2\frac{\text{Precisione}(c) * \text{Recall}(c)}{\text{Precisione}(c) + \text{Recall}(c)}$$
	6
---
**Valutare i Classificatori: Problemi Sbilanciati**

- Di solito comprendiamo precisione e recall usando le curve Precision-Recall (PR) e/o Receiver-Operating Characteristic (ROC):

	![[Pasted image 20251105223507.png]]
	
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
- Stimiamo un piccolo numero di parametri di distribuzione (es. media e covarianza di Gaussiane).
- Una tale assunzione a priori di una forma distributiva è una limitazione di questi approcci.
- Specialmente quando queste assunzioni risultano inaccurate.

- Idea: possiamo fare a meno dell'assunzione parametrica, e lasciare semplicemente che i dati parlino da soli?

	9
---
**Istogrammi: stimatori di densità costanti a tratti**

- Un istogramma partiziona il dominio in bin di larghezza fissa.
- Contiamo poi il numero di osservazioni che cadono in ogni bin discreto.
- Possiamo trasformare questa rappresentazione in una densità di probabilità dividendo per il numero totale di osservazioni $N$ e la larghezza del bin $\Delta_i$: $$p_i = \frac{n_i}{N\Delta_i}$$
- Questo produce una densità $p(x)$ che è costante sulla larghezza di ogni bin (di solito $\Delta_i = \Delta$).

	10
---
**Istogrammi: stimatori di densità costanti a tratti**

- Questo dà uno stimatore di densità con un singolo iperparametro:

	![[Pasted image 20251105224554.png]]

	11
---
**Istogrammi: stimatori di densità costanti a tratti**

- La selezione di $\Delta$ è critica – troppo piccolo e lo stimatore ha alta varianza.
- Troppo grande e la curva è troppo liscia.
- Il modello è discontinuo ai bordi dei bin.
- I dati non sono necessari al tempo di test, ma gli istogrammi scalano molto male con la dimensione ($M^D$).

	![[Pasted image 20251105224554.png]]

	12
---
**Istogrammi: stimatori di densità costanti a tratti**

- Nonostante le loro limitazioni, gli istogrammi ci dicono qualcosa di importante sulla stima della densità.
- Per stimare la densità in un punto $x$ nel dominio, dovremmo guardare i punti dati che giacciono vicino a $x$.
- Questo uso della località assume che abbiamo una metrica di distanza significativa nel dominio (es. Euclidea).
- Diamo un'occhiata ad alcuni metodi nonparametrici comuni usati in Machine Learning.

	13
---
## Stima della Densità: Kernel Density Estimators
---
**Una digressione binomiale**

- Per motivare come possiamo estendere la nostra idea dell'istogramma a uno stimatore puramente locale, dobbiamo considerare la distribuzione binomiale.
- La distribuzione binomiale rappresenta la probabilità di vedere $m$ successi in una sequenza di $N$ prove di Bernoulli:$$\text{Bin}(m|N, \mu) = \binom{N}{m} \mu^m (1 - \mu)^{(N - m)}$$
$$\mathbb{E}(m) = \sum_{m=0}^{N} m \text{Bin}(m|N, \mu) = N\mu$$

	14
---
Una digressione binomiale

- La binomiale è unimodale e in qualche modo simile a una Gaussiana:

	![[Pasted image 20251105224901.png]]

	15
---
**Generalizzando**

- Assumiamo di avere osservazioni estratte da una densità sconosciuta $p(x)$ in uno spazio Euclideo $D$-dimensionale.
- Simile a un istogramma, consideriamo una piccola regione $\mathcal{R}$ attorno a $x$.
- La massa di probabilità associata con $\mathcal{R}$ è$$P = \int_{\mathcal{R}} p(x) dx$$
- Se abbiamo $N$ osservazioni estratte da $p(x)$, ognuna ha probabilità $P$ di cadere in $\mathcal{R}$.
- Quindi, il numero totale di punti $K$ che cadono in $\mathcal{R}$ sarà distribuito binomialmente:$$\text{Bin}(K|N, P) = \binom{N}{K} P^K (1 - P)^{(N-K)}$$
	16
---
**Generalizzando**

- Usando le formule per media e varianza della Binomiale possiamo analizzare la frazione di punti che cadono in $R$: $$\mathbb{E}(K/N) = P$$$$\text{var}(K/N) = \frac{P(1-P)}{N}$$
- Per $N$ grande questa distribuzione sarà concentrata attorno a $P$ e quindi:$$K \approx NP$$
	17
---
**Generalizzando**

- Per $N$ grande questa distribuzione sarà concentrata attorno a $P$ e quindi:$$K \approx NP$$
- D'altra parte, possiamo assumere $R$ con volume $V$ sia sufficientemente piccolo (e quindi $p(x)$ è costante) e quindi: $$P \approx p(x)V$$
- Portandoci a: $$p(x) \approx \frac{K}{NV}$$
	18
---
**Generalizzando**

- Nota che questa stima di $p(x)$ è basata su due assunzioni contraddittorie:
  - Che $R$ sia sufficientemente piccolo e quindi $p(x)$ è costante in esso.
  - Che $R$ sia sufficientemente grande in modo che il numero di punti che cadono in esso siano sufficienti a picco la binomiale.

- Questo ci lascia con due scelte:
  1. Fissare $K$ e lasciare che i dati determinino cosa $V$ dovrebbe essere (Nearest Neighbors).
  2. Fissare $V$ e lasciare che i dati determinino cosa $K$ dovrebbe essere (Kernel Density Estimation).

	19
---
**Kernel Density Estimation**

- Prendiamo $R$ come un ipercubo unitario centrato all'origine.
- Questo è convenientemente descritto dalla funzione kernel:$$k(u) =
\begin{cases} 
1 & \text{se } |u_i| \leq 1/2, \text{ per } i = 1, \ldots, D \\
0 & \text{altrimenti}
\end{cases}$$
- Quindi, per qualsiasi punto $x$, $k((x - x_n)/h) = 1$ se il punto $x_n$ giace dentro un ipercubo con dimensione $h$ centrato su $x$.
- Il numero totale di punti $K$ che giacciono in tale ipercubo attorno a $x$ è allora:$$K = \sum_{n=1}^{N} k \left( \frac{x - x_n}{h} \right)$$
	20
---
**Kernel Density Estimation**

- Tornando alla nostra equazione per $p(x)$, abbiamo: $$p(x) = \frac{K}{NV} = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{h^D} k \left( \frac{x - x_n}{h} \right)$$
- Questo soffre ancora di discontinuità ai bordi dell'ipercubo, quindi un kernel più comune è il Gaussiano: $$p(x) = \frac{1}{N} \sum_{n=1}^{N} \frac{1}{(2\pi h^2)^{D/2}} \exp \left\{ \frac{||x - x_n||^2}{2h^2} \right\}$$
	21
---
**Kernel Density Estimation**

- Questo è chiamato Kernel Density Estimator (o di Parzen).
- L'iperparametro $h$ è chiamato bandwidth del kernel che controlla la quantità di smoothing che viene eseguita.
- Le funzioni kernel dovrebbero soddisfare: $$k(u) \geq 0, \, \int uk(u)du = 0, \, \text{e} \, \int k(u)du = 1$$
 - Questi tipi di approcci sono spesso chiamati metodi locali perché per stimare $p(x)$ guardano i dati vicini a $x$.

	22
---
**Kernel Density Estimation**

![[Pasted image 20251105225455.png]]

	23
---

## Regressione Kernel di Nadaraya-Watson
---
**Località in x e y**

- Possiamo applicare questo tipo di metodo locale a problemi di regressione.
- Ricordiamo che un predittore ottimale per la regressione è: $$\mathbb{E}(t | \mathbf{x}) = \int t p(t | \mathbf{x}) dt = \int t \frac{p(\mathbf{x}, t)}{p(\mathbf{x})} dt$$
- Ora usiamo le Kernel Density Estimates come approssimazioni: $$\hat{p}(\mathbf{x}, t) = \frac{1}{N} \sum_{n=1}^{N} k_h (\mathbf{x} - \mathbf{x}_n) k_h (t - t_n)$$$$\hat{p}(\mathbf{x}) = \frac{1}{N} \sum_{n=1}^{N} k_h (\mathbf{x} - \mathbf{x}_n)$$
	24
---
**Nadaraya-Watson: regressione localmente pesata**

- La nostra approssimazione dello stimatore ottimale è ora: $$\mathbb{E}(t \mid x) = \int t \frac{p(x, t)}{p(x)} dt$$$$= \int t \frac{1}{N} \sum_{n=1}^{N} k_h (x - x_n) k_h (t - t_n) d t$$$$= \frac{\sum_{n=1}^{N} k_h (x - x_n) \int t k_h (t - t_n) d t}{\sum_{n=1}^{N} k_h (x - x_n)}$$$$= \frac{\sum_{n=1}^{N} k_h (x - x_n) t_n}{\sum_{n=1}^{N} k_h (x - x_n)}$$
	25
---
**Uno stimatore approssimativamente ottimale**

![[Pasted image 20251105230051.png]]

	26
---

## K-Nearest Neighbors

---
**Il problema di $h$**

- Un problema con la Kernel Density Estimation è che il bandwidth $h$ è fissato per tutti i kernel.
- Se abbiamo parti dello spazio con molti campioni, questo può portare a oversmoothing e perdita di dettaglio se $h$ è troppo grande.
- Se riduciamo $h$, in regioni a bassa densità avremo stime rumorose.
- E se, invece di fissare $V$ (tramite il bandwidth) e derivare un'espressione per $K$, fissassimo $K$ e andassimo nella direzione opposta.

	27
---
**K-Nearest Neighbors**

- L'approccio K-Nearest Neighbors è algoritmico:
  - Fissiamo $K$ e consideriamo una ipersfera attorno a un punto $x$ dove vogliamo stimare $p(x)$.
  - Aumentiamo poi il raggio di questa ipersfera fino a quando esattamente $K$ punti dal training set sono dentro di essa.
  - Calcoliamo poi $p(x) = \frac{K}{NV}$ per $V$ uguale al volume dell'ipersfera risultante.

	28
---
**K-Nearest Neighbors**

- Questo approccio è discontinuo e rumoroso per la stima della densità:

	![[Pasted image 20251105230215.png]]

	29
---
**K-Nearest Neighbors Classification**

- L'approccio K-Nearest Neighbors (KNN) è un metodo molto conveniente per la classificazione, tuttavia.
- Intuitivamente, facciamo una stima di densità KNN per ogni densità condizionata alla classe, e poi applichiamo la Regola di Bayes.
- Supponiamo di avere $N_k$ esempi da ogni classe $k$ (quindi $\sum_{k} N_k = N$).
- Per classificare un nuovo punto $x$ facciamo il trucco dell'ipersfera assumendo che il volume necessario attorno a $x$ per includere $K$ punti sia $V_x$.
- Se in questa ipersfera abbiamo $K_k$ punti dalla classe $k$: $$p(x | C_k) = \frac{K_k}{N_k V_x}$$
- La densità marginale e i prior di classe sono similmente stimati:$$p(x) = \frac{K}{N V_x} \quad p(C_k) = \frac{N_k}{N}$$
	30
---
K-Nearest Neighbors Classification

- Entra Bayes:$$p(C_k | x) = \frac{p(x | C_k) p(C_k)}{p(x)} = \frac{K_k}{K}$$
	![[Pasted image 20251105230403.png]]

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
---

