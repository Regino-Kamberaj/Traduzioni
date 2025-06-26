I GAMs sono modelli usati nel campo dell'[interpretability](regio/Interpretability/Interpretability.md).
Sono modelli adatti quando si lavora con dati tabulari e sono molto buoni quando le features sono continue; nel caso discreto (features categoriche) allora la $f_i$ sarà una funzione a gradini (istogramma).
##### Idea
L'idea dei GAMs deriva dal voler mantenere l'interpretabilità dei [modelli lineari](regio/Interpretability/Interpretability.md#Modelli%20lineari) $y=f(x)=\sum_{i=1}^P\beta_ix_i+\beta_0$ aggiungendo una qualche complessità.
Questi modelli ottengono il target $y$ in modo additivo, dove i vari termini sono risultati di modelli complessi (volendo anche non lineari) indipendenti, valutati su una singola feature.
Il modello GAM generale può essere descritto da $y=g(\sum_{i=1}^Pf_i(x_i))$, dove $P$ è il numero di features; la funzione $g$ è detta link function, mentre le $f_i$ sono dette shape function. Se $g$ è l'identità allora abbiamo una regressione fatta in modo additivo; se $g$ è la sigmoide allora abbiamo una classificazione (una specie di regressione logistica additiva).
##### Interpretabilità
Hanno un'ottima interpretabilità perché possiamo definire l'impatto che ogni feature ha sull'output; anche se ogni $f_i$ è molto complessa possiamo analizzarla indipendentemente dalle altre tramite un grafico in una variabile.
- Ha un'interpretabilità locale perché durante l'inferenza ci va vedere su un singolo esempio il contributo di ogni features.
- Ha un'interpretabili globale perché ho la $f$ in forma analitica, sia per tutte le features messe insieme che per la singola feature. Riesco quindi a osservare quanto la features contribuisce al valore finale rispetto a tutti i valori possibili.
##### Bias
Questi modelli spesso ci offrono punti di vista che le sole statistiche descrittive non mettono in evidenza; è infatti ottimo per capire come i dati sono costruiti.
In presenza di bias nei dati (es: un asmatico può avere meno rischio rispetto a una persona sana alla contrazione di una polmonite; ovviamente non è così ma se i dati ci dicono questo allora il modello apprenderà questo; il motivo per cui invece succede è che un asmatico viene curato più di una persona sana alla contrazione della polmonite), un esperto può cambiare la predizione del modello modificando direttamente la funzione che agisce sulla feature che è responsabile dell'introduzione del bias.
##### $GA^2M$
Il problema che si può osservare è che il modello non osserva relazioni tra più di una fetures contemporaneamente.
Nella versione base è vero, ma questo si può implementare facendo si che ogni shape function agisca anche su più variabili; in questo caso il modello si può definire come $y=g(\sum_{k=1}^Pf_k(x_k)+\sum_{k_1=1}^P\sum_{k_2=k_1+1}f_{k_1k_2}(x_{k_1},x_{k_2}))$. Il problema nasce se le possibili coppie sono troppe; in questo caso si usa un iperparametro che agisca sul numero massimo di coppie analizzate; queste saranno scelte tramite una qualche euristica.
Se però osserviamo molte variabili (solitamente già per più di due), allora perdiamo l'interpretabilità del modello.
# Explainable Boosting Machine
Una specifica implementazione delle GAMs sono le Explainable Boosting Machine (EBM), dove ogni $f_i$ è un ensamble di [alberi di decisione](Decision%20tree.md) aaddestratitramite una tecnica di [gradient boosting](Ensamble.md#Gradient%20boosting).
![EBM training](regio/Interpretability/File/EBM%20training.png)
Se consideriamo una regressione, l'algoritmo che apprende una EBM è:
- $f_j=0$ per ogni features $j$. Stiamo mettendo a 0 tutte le predizioni sulle singole features.
- for $m=1$ to $M$, dove $M$ è il numero di iterazioni ($M$ è l'upper bound, ma possiamo anche fermarci prima se il modello non sta imparando più di una data soglia):
	- for $j=1$ to $P$, dove $P$ è il numero di features (si impara un albero $S$ basandosi su una features alla volta):
		- Si impara un residuo $R=\{x_{ij},y_i-\sum_{k=1}^{m-1}f_k\}_{i=1}^n$, dove la somma delle varie $f_k$ sono quanto appreso da tutti gli alberi precedenti (sia iterazioni precedenti sia di features precedenti); in pratica i target sono quanto manca al totale da apprendere.
		- Si impara una shape function $S$ (che nelle EBM sono alberi) che usa $R$ come training set.
		- Si aggiorna $f_j=f_j+S$.
##### Funzionamento
Quello che stiamo facendo è quindi produrre un albero per features e questo impara quanto non aveva imparato l'albero prima; questo concetto è detto residuo, il quale passa anche da iterazione a iterazione e non solo da features a features, altrimenti si inizierebbe da capo.
Al termine di tutte le iterazioni avremo molti alberi per ogni features; sommandoli tutti si ottiene il grafico in relazione della features.
Il modello che predice invece è ottenuto sommando tutti i risultati che si ottengono dai modelli che analizzano la singola features.
##### Residuo
Quello che succede al residuo è che a ogni passaggio di features può aumentare o diminuire, ma alla fine convergerà.
Questo succede perché il modello alla prima features ha imparato qualcosa, ma quando corregge la sua idea osservando solo la features successiva potrebbe peggiorare quanto imparato dalla prima features. Quando all'iterazione successiva torniamo a osservare la prima features il residuo potrebbe essere molto diverso da quello che aveva lasciato.
# Neural additive models
Sono modelli i cui termini additivi sono prodotti da delle reti neurali.
##### Architettura
Questo ha senso per le GAMs non ci dicono in che modo implementare le $f_i$, ma ci dicono solo che sono funzioni più o meno complesse; le reti neurali sono degli approssimatomi universali di funzioni e quindi ha senso usarle.
La cosa più strana in questa situazione è che le reti hanno un solo neurone nel primo layer, che corrisponde alla singola feature analizzata.
##### Attivazione
Invece che usare la funzione di attivazione [ReLU](Neurone%20artificiale.md#ReLU), questi modelli solitamente utilizzano la funzione [ExU](Neurone%20artificiale.md#ExU).
Il motivo di qusta scelta è data dal fatto che nei grafici con cui osserviamo la variazione dell'output rispetto a una features ci interessa particolarmente le variazione repentine per piccole variazioni dell'input; questa activation function permette di ottenere proprio questo vantaggio.
# Libreire
##### [InterpretML](https://interpret.ml)
È la miglior libreria per quanto riguarda le boosting machine ma ci sono altri modelli, comprese tecniche per spiegare modelli black box.
- Si integra perfettamente con scikitlearn.
- Solitamente gli iperparametri di default della classe $ExplainableBoostingMachine$ funzionano molto bene.
- L'output è fatto benissimo e ci da una spiegazione ben fatta dell'importanza delle features con un menù a tendina con grafici e distribuzione per ogni features.