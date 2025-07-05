# Primo capitolo

L'explainable AI (XAI) produce e integra modelli di intelligenza artificiale per rendere interpretabile la logica interna e il risultato degli algoritmi, rendendo il processo comprensibile agli esseri umani. Se un modello non fa parte di questa categoria si parla di black-box model.
Nel processo decisionale dovremmo tendere a favore dei modelli black-box solo se le prestazioni motivano questa scelta. Non ci sono infatti motivi per non andare verso un modello XAI se non per le prestazioni: siccome con i modelli XAI lavoriamo maggiormente sui dati, durante la costruzione del modello si può capire se il dataset è affetto da bias, se abbiamo formulato male il problema.
##### Paradosso di Hans
Un uomo aveva un cavallo che reputava molto intelligente a livello scientifico: se gli veniva posta una domanda di tipo matematico allora rispondeva, battendo lo zoccolo per contare, bene; se però l'interlocutore si allontanava e non lo poteva vedere, ma lo poteva solo sentire, allora rispondeva male. La verità è che non aveva un'intelligenza matematica ma osservava molto bene il comportamento dell'interlocutore per rispondere bene.
Il risultato è che si parla di paradosso di Hans quando un agente da un risultato giusto ma per il motivo sbagliato.
### Motivazioni

Le motivazioni principali per cui ci servono motivi spiegabili sono:
- Capire le decisioni
	Ci interessa capire perché un modello ha preso una decisione e non ne ha presa un'altra.
- Migliorare
	Si parla di "human in the loop" quando dopo che il modello ha preso una decisione, l'uomo da il proprio feedback, che finisce nei dati di addestramento. In questo modo di possono produrre modelli personalizzati per una situazione, cioè si possono integrare informazioni che a priori non erano rappresentabili.
- Fiducia
	Se un modello è spiegabile allora possiamo riporre un certo grado di fiducia.
	Questo non vuol dire che se un modello è spiegabile allora è degno di fiducia, ma possiamo capire anche quando non fidarsi.
### Problemi
- Costruzione dei dati
	Un esempio è quello in cui un sistema predice il rischio di un paziente affetto da polmonite. Dai risultati del sistema si osserva che se una persona è asmatica allora ha un basso rischio (basso rischio si intende che poi sta male); questo sarebbe contro intuitivo per ogni dottore.
	Il motivo di questo è che se una persona asmatica ha una polmonite viene curato subito e ha un trattamento privilegiato e quindi alla fine non sta male.
	Tutto questo succede perché nei dati c'è la relazione per cui le persone con asma non stanno male nel lungo periodo, ma questo avviene perché vengono visitate tempestivamente e perché hanno in realtà un rischio alto.
- Blackbox ingannati
	I modelli blackbox possono essere ingannati.
	Un esempio sono gli esempi avversari: abbiamo un immagine $x$ a cui viene applicato un rumore $\epsilon$; il modello predice $x$ con una certa probabilità, ma se valuta $x+\epsilon$ allora predice altro con una probabilità molto più alta.
- [Bias](regio/Bias.md)

### AI Act
L'AI Act definisce 4 livelli di rischio nell'utilizzo dei modelli: si va dal livello più basso in cui sono contenuti gli scenari deve gli uomini non sono coinvolti (es: industria e giochi), fino al livello più alto in cui le persone sono centrali (es: riconoscimento facciale).
L'articolo 13 dell'AI Act afferma che "i sistemi di intelligenza artificiale ad alto rischio devono essere progettati e sviluppati in modo tale da garantire che il loro funzionamento sia abbastanza trasparente per consentire agli sviluppatoti di interpretare l'output di un sistema e utilizzarlo in modo appropriato".
### Interpretability/Explainability

Quando si parla di [explainability](regio/Explainability/Explainability.md) si intende la spiegazione delle decisioni prese dai modelli. Alcuni modelli sono spiegabili per costruzione (by design); in questo caso si parla di interpretability.

![[explainability vs performance.png]]

## Bias

Un bias è definito come un errore sistematico nel processo decisionale che porta a un risultato [unfair](regio/Fairness.md).
Nel mondo del ML la previsione del modello viene presa basandosi sui dati del train set; se questi dati contengono dei bias allora l'outcome sarà unfair.
- Un esempio è che se passiamo una foto di un matrimonio occidentale allora ci dice che è un matrimonio, ma la foto è di un matrimonio orientale allora ci dice che sono persone.
- Un altro esempio è che se i dati esprimono (e succede davvero) che le donne hanno uno stipendio più basso, allora i modelli di raccomandazione propongono alle donne dei lavori con stipendio più basso.
- Se un dataset contiene foto di lupi dove nella maggior parte i lupi sono sulla neve, allora se chiediamo di classificare un Husky sulla neve ci darà che è un lupo.
### Bias nei dati

Vediamo alcuni tipi di bias nei dati.
- Sampling
	È detto bias di campionamento è succede quando il train set non è ottenuto in modo casuale dalla distribuzione della popolazione, ma ci sono alcune categorie di individui che hanno più probabilità di essere campionate.
	È quindi un problema di come sono raccolti i dati.
- Representation
	Avviene quando ci sono delle sotto popolazioni che sono rappresentate meno. È un concetto molto simile al sampling, ma qua l'attenzione è sulle sotto popolazioni e non sul campionamento in generale
- Artefatti
	Si presenta quando c'è una correlazione tra artefatti (e.g. patch in una foto) e classe di appartenenza del sample.
	In pratica il modello usa l'artefatto per classificare i futuri samples.
### Bias negli algoritmi

Vediamo alcuni tipi di bias negli algorimi.
- Algoritmico
	Non ci sono bias nei dati, ma è l'algoritmo che introduce dei bias per come è costruito.
- D'interazione
	Quando il bias proviene dall'interazione dell'algoritmo verso alcune categorie di utenti.
- Di conferma
	Se chi ha progettato l'algoritmo ha introddo un bias perché il suo pensiero è affetto da bias.
- Generativo
	Se i dati hanno dei bias e un modello generativo genera risposte affetti da questi bias. È strettamente legato ai modelli generativi.

## Data analysis

La data analysis utilizza metodi statistici e visuali per spiegare le correlazioni dei dati. I dati statistici se non usati insieme a quelli visuali potrebbero non fornire una soluzione corretta ed esatta; tramite la visualizzazione si possono osservare cose che le sole statistiche non ci dicono, come in [questo esempio](regio/File/data%20analysis%20example.pdf) (non da sapere).

![[data analysis example.pdf]]

+ Esempio di unfairness

![[esempio paradosso di simpson.pdf]]
### Plot

Solitamente i grafici sono utili per mostrare relazioni tra due variabili. Non è solitamente consigliato mostrare relazioni tra più di due variabili; se siamo molto bravi a fare grafici multidimensionali e interattivi allora si può fare, però è difficile.
Un modo per mettere in relazione tre variabili è usare i colori: sulle ascisse e orinate ho due variabili; la terza è espressa nello spazio definito dalle altre due tramite colori.
Le librerie più usate sono:
- Le classiche e quelle su cui si appoggiano le altre sono Pandas, numpy e matplotlib.
- Quelle più moderne sono seaborn, plotly (per grafici interattivi) e vega-altair (più avanzata).
- Le più specifiche per il ML e la XAI sono ydata-profling, FACETS e KNIME.
#### Scatter plot

È usato per mettere in relazione due variabili continue $x$ e $y$ ([grafico](regio/File/scatter%20plot.png)), dove ogni punto sul piano è dato dalla coppia $(x,y)$; se usato per variabili discrete allora vengono delle barre di samples.

![[scatter plot.png]]

Si possono mettere insieme più scatter plot in una [matrice](regio/File/scatter%20plot%20matrix.png) $n\times n$, in modo da avere a vista più coppie di variabili.

![[scatter plot matrix.png]]

È usato per rappresentare pattern o outliers.
#### Bar plot

Mette in relazione la grandezza (quantità, media, varianza) di una variabile rispetto a un insieme di categorie discrete ([grafico](regio/File/bar%20plot.png)).

![[bar plot.png]]
#### Istogramma

Rappresenta la distribuzione di una variabile continua: sulle ascisse abbiamo i valori delle variabili suddivise in bin, sulle ordinate la densità rispetto a ogni bin.
Usato per comprendere la distribuzione dei samples.
![[istogramma.png]]
#### Box plot

Sulle ascisse ci sono le categorie discrete e sulle ordinate la distribuzione delle variabili. Il [box](regio/File/box%20plot.png) rappresenta il primo e terzo quartile, con la mediana nel mezzo; i baffi rapprensetano l'estensione della distribuzione; gli outliers sono rappresnetati da pallini esterni ai baffi.
Usato per capire la distribuzione dei samples e rappresentare gli outliers.

![[box plot.png]]

# Interpretabilità 

Alcuni modelli sono spiegabili per costruzione (by design); in questo caso si parla di interpretability.
## ![[incremental featurs deletion.jpeg]]

![[accuracy vs plausibility.jpeg]]

## Modelli lineari

I modelli lineari calcolano l'output come $f(x)=\sum_{i=1}^P\beta_ix_i+\beta_0$, dove $P$ è il numero di featues. I modelli lineari sono molto interpretabili perché i coefficienti $\beta_i$ mi dicono il peso di ogni features, cioè mi dicono l'impatto che ha una modifica di $x_i$ sul risultato; in pratica se $x_i$ incrementa di una unità allora $f(x)$ incrementa di $\beta_i$.
Il problema dei modelli lineari è dato dal fatto che il mondo non è lineare. Non riescono infatti a imparare la variazione dell'output rispetto alla variazione di più features contemporaneamente.
## Modelli

I segurenti modelli si basano, chi più chi meno, sugli [alberi di decisione](Decision%20tree.md):
- [Rule-based system](regio/Interpretability/Rule-based%20system.md)
- [Rule fit](regio/Interpretability/Rule%20fit.md)
- [Generalized additive models (GAMs)](regio/Interpretability/Generalized%20additive%20models%20(GAMs).md)

### Rule-based system

I rule-based system sono modelli usati nel campo dell'explainable AI per la loro grande [interpretability](regio/Interpretability/Interpretability.md).
Sono sistemi che prendono decisioni sulla base di regole (decision rule)
$if (condizione),then (predizione)$, dove la condizione, che può essere composta anche da più predicati in AND, è detta antecedente e la predizione è detta conseguente.
##### Conseguenze
- Vantaggi
	- Alta interpretabilità.
	- Espressività di un [decision tree](Decision%20tree.md) ma con regole più compatte (più corte). In queste tecniche infatti non ci sono sotto alberi che si ripetono come nei decision tree.
	- Velocità dell'inferenza molto elevata. Solitamente non ci sono modelli più veloci.
	- Sono sparsi, cioè usano poche features.
- Svantaggi
	- Adatti solamente alla classificazione, a meno di quantizzare l'output della regressione. Per quantizzazione si intende trasformare un insieme continuo in un insieme discreto.
	- Le features devono essere categoriche e non numeriche. Se sono numeri allora si devono raggruppare i valori divisi da una soglia per ottenere delle classi.
#### Valutazione regole

La bontà di una decision rule si può valutare sulla base di due misure:
- Supporto/copertura (coverage)
	È la percentuale di esempi per cui è vero l'antecedente. Non stiamo verificando che la predizione sia buona.
- Accuratezza (confidence)
	È la percentuale di esempi coperti dalla regola (samples per cui vale l'antecedente) che sono classificati correttamente.
##### Compromesso

Si può dimostrare che se il supporto diminuisce allora si può far crescere l'accuratezza e se l'accuratezza diminuisce si può far crescere il supporto.
Intuitivamente una regola può essere molto precisa (molte espressioni booleane in AND) e quindi comprire pochi sample; per una regola di questo tipo però mi aspetto che la percentuale di samples classificati correttamente sia massima.
Ragionamento opposto invece per una regola generale e corta.
#### Combinazione regole

Una regola non può ne coprire tutti i samples ne tutte le classi. Per questo devo definire un modo per mettere insieme più regole, in modo che quando devo fare inferenza su un nuovo sample possa utilizzarne eventualmente più di una.
##### Decision list

Le decision list sono quelle più usate.
È una lista ordinata di regole; durante l'inferenza si applica il conseguente relativo al primo antecedente soddisfatto dal sample in esame.
Ci può essere overlapping tra regole, ma questo è risolto selezionando la prima che è verificata.
La decision list ha una struttura del tipo sottostante. Osserviamo che nel caso in cui nessun antecedente sia stato soddisfatto allora si stabilisce una regola di defult; questa solitamente è scelta in modo che copra la maggior parte dei samples non coperti dagli antecenti precedenti.
- $if (condition1), then (predition1)$
- $else\ if(codition2), then (prediction2)$
- $\cdots$
- $else(none\ of\ above), then (preditionN)$
##### Decision set

È un insieme di regole, per cui non c'è un ordine; durante l'inferenza si devono valutare tutte le regole.
Se c'è overlapping tra le regole e più antecedenti sono verificati allora si stabilisce il conseguente da selezionare tramite una votazione. Un esempio è associare a ogni regola un peso.
Il decision set ha una struttura del tipo sottostante. Come nelle decision list si applica la regola di default se nessun antecedente è soddisfatto.
- $if (condition1), then (predition1)$
- $if(codition2), then (prediction2)$
- $\cdots$
- $if (none\ of\ above), then (preditionN)$

#### Apprendimento

Per imparare le regole ci sono varie strategie.
##### Sequenzial covering

Questo tipo di algoritmo è un algoritmo greedy (come quelli basati sui [decision tree](Decision%20tree.md)). Intuitivamente l'algoritmo:
- Inizializza una lista di regole $ruleList$ vuota.
- Impara una regola $r_j$ da $D$.
- Finché il criterio di arresto non è soddisfatto:
	- Aggiungo $r_j$ a $ruleList$.
	- Rimuovo i sample coperti da $r_j$ da $D$.
	- Apprendo un'altra regola $r_j$ da $D$.
- Si restituisce $ruleList$.
###### Imparare regole

Tipicamente per apprendere una regola si apprende un [albero di decisione](Decision%20tree.md) (e.g., con l'algoritmo cart che è veloce) e poi si estrae la regola definita dal percorso che comprende per ogni livello il nodo più puro (secondo la definizione del [gini index](Decision%20tree.md#Score/Metriche)).
###### Criterio di arresto

Possiamo considerare due criteri di arresto:
- Le nuove regole non sono regole buone, cioè i nodi generati dall'albero di decisione non sono molto puri.
- Sono rimasti pochi samples da coprire.
###### Combinazione di regole

L'implementazione, usata soprattutto durante l'inferenza, segue la struttura delle decision list.
Questo è necessario in quanto l'algoritmo è greedy: le regole imparate potrebbero sovrapporsi e tramite la lista prendiamo solo la prima regola il cui antecedente è verificato.
##### Bayesian/scalable rule list

È una tecnica che usa delle decision list e un approccio bayesiano, cioè usa una conoscenza a priori per determinare le miglior lista tra quelle possibili.
L'algoritmo ad alto livello si articola in:
- Generare una lista di regole iniziale.
	Questa generazione avviene campionando su una distribuzione a priori, costruita con l'obiettivo di generare poche regole e corte; il numero e la lunghezza delle regole sono gli iperparametri della distribuzione.
- Si modifica la lista aggiungendo, rimuovendo o modificando regole della lista.
- Si sceglie la migliore lista secondo la postirior probability distribuzion ottenuta tramite la regola di bayes.
###### Posterior

La posterior è definita da $P(d|x,y,A,\alpha,\lambda,\eta)$ e mi dice quanto è probabile la decision list $d$ dati quei dati e la conoscenza a priori sulle liste.
Si può dimostrare che $P(d|x,y,A,\alpha,\lambda,\eta)\propto P(d|x,y,\alpha)\cdot P(d|A,\lambda,\eta)$, cioè che è direttamente proporzionale a due fattori: una likeliwood sui dati e la probabilità della decision list dati gli iperparametri delle liste. Si vede allora che la posterior è alta se $d$ classifica bene i dati (dalla likeliwood) e ha delle caratteristiche che corrispondono a quelle della prior, cioè quelle che abbiamo definito (dalla prior).
In particolare gli elementi sono:
- $d$ è la decision list.
- Dati
	- $x$ sono le features.
	- $y$ è il target.
	- $A$ è un insieme di pattern frequenti trovati con un qualche algoritmo di data mining (es: [A-Priory](A-Priory%20algorithm.md), FP-growth). Per pattern si intende un insieme di condizioni messe in AND; per frequente si intende che questo è verificato da un numero di dati maggiore di una data soglia. In pratica è l'insieme da cui definire le regole.
- Iperparametri
	- $\alpha$ sono gli iperparametri di una distribuzione di dirichlet. Per semplicità possiamo dire che $\alpha$ è un vettore di pesi da attribuire alle classi; la scelta tipica è $\alpha=1^c$, con $c$ numero di classi.
	- $\lambda$ è il prior sul numero di regole, in particolare il valore atteso.
	- $\eta$ è il prior sulla lunghezza delle regole, in particolare il valore atteso.
##### Algoritmo

- Pre-mining dei pattern $A$ con FP-growth (un algoritmo simile a [A-Priory](A-Priory%20algorithm.md), non da sapere).
- Si sceglie il numero di regole $m$ da una distribuzione di poisson con parametro $\lambda$. Se lambda è basso allora ho meno regole. Questo passo ci introduce la stocasticità perchè campioniamo da delle distribuzioni. 
- Per ogni regola $j=1,\cdots,m$:
	- Si sceglie la lunghezza della regola con $l_j$ da una poisson con parameto $\eta$. Altro punto in cui si introduce stocasticità.
	- Si scelgono da $A$ un insieme di condizioni (messe in AND) di lunghezza $l_j$.
- Adesso ho trovato la decision list iniziale e vado avanti in un processo iterativo.
	- Tramite il metodo montecarlo si seleziona in modo casuale se aggiungere, togliere e modificare le regole della decision list e si produce un grande numero di altre decision list.
	- Dato che abbiamo finito la $k$-esima iterazione, per ogni decision list prodotta $d^{k+1}$ si calcola la sua posterior $p(d^{k+1}|\cdots)$ e si memorizza la decision list che ha la posterior più alta in questa iterazione.
- Calcola la decisione list finale come $d^*=\displaystyle\arg\max_{k}P(d^k|\cdots)$, cioè la migliore tra tutte quelle memorizzate durante il processo iterativo.

Sono modelli [interpretabili](regio/Interpretability/Interpretability.md) che, rispetto ai [rule-based system](regio/Interpretability/Rule-based%20system.md), vogliono aggiungere la non linearità.

### RuleFit
##### Idea
L'idea alla base di rule fit è mappare lo spazio delle features tramite delle regole; in pratica l'antecedente (insieme di condizioni sulle features originali messe in AND) di una regola diventa la nuova features. In questo modo il modello diventa non lineare nello spazio delle features originale, ma lineare nel nuovo spazio.
#### Algoritmo
L'algoritmo rule fit aggiunge un termine alla classica [funzione lineare](regio/Interpretability/Interpretability.md#Modelli%20lineari) e quindi l'output viene calcolato come $f(x)=\beta_0+\sum_{i=0}^P\beta_ix_i+\sum_{j=1}^R\alpha_jr_j$, dove $r_j$ è la $j$-esima regola e $\alpha_j$ è il peso corrispondente.
##### Apprendimento regole
Per apprendere le regole fit rule utilizza un metodo ensamble, come può essere una random forest o un gradient boosting (comunque deve essere un insieme di alberi).
##### Loss
Per imparare $\alpha$ e $\beta$ della funzione che poi genera l'output usiamo
$\alpha^*,\beta^*=\displaystyle\arg\min_{\alpha,\beta}\sum_{i=1}^nL(y_i,f(x_i))+\lambda(\sum_{i=1}^P|\beta_i|+\sum_{j=1}^R|\alpha_j|)$, dove l'iperparametro $\lambda$ (lasso regularizer), gestisce la sparsità della soluzione, cioè la quantità di regole che vogliamo: un valore alto indica poche regole.
Questo ha senso perché vogliamo che il nostro output, cioè $f(x)$, sia determinato da poche regole, in modo che sia più interpretabile; se avessimo infatti una soluzione con molto regole allora il modello sarebbe poco interpretabile.
#### Librerie
##### [Rulefit](https://github.com/christophM/rulefit)
- L'output è il meno interpretabile. È solamente un print dell'antecedente della regola che è stata tramutata in una feature.
- Un oggetto rulefit ha un oggetto al suo interno che ha le features sotto forma di regole usate.
##### [H20](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/modeling.html#h2orulefitestimator)
È dentro una libreria h2o, una libreria alternativa a skilearn che ha molti modelli di machine learning.
- È il più completo ma richiede i suoi frame per gestire i dataset.
- L'output è molto comprensibile.
	- Il coefficiente indica cosa succede al risultato se la features aumenta: se è positivo allora indica di quanto è il risultato aumenta all'aumentare del valore della features; vicersa se è negativo. 
	- Il supporto è una percentuale del numero di esempi che hanno usato quella feature. Diventa rilevante quando abbiamo una regola e non quando abbiamo una singola features (sarà sempre 1); in questo caso ci dice la percentuale di samples che soddisfano la regola.
- Se impostiamo un parametro lambda alto allora vuol dire spingere sul regolarizzatore del lasso e quindi volere poche features attive. Per fare le cose bene dobbiamo valutare più lambda ad esempio tramite cross validation (o se il dataset è piccolo anche su un solo validation set).
##### [iModels](https://github.com/christophM/rulefit)
È una libreria che contiene [molti modelli](https://github.com/csinva/imodels?tab=readme-ov-file) interpretabili.
- Ha un output molto ben fatto.
- È una via di mezzo tra la completezza di h2o e un'integrazione con scikitlearn. 

### GOSDT

![[GOSDT binary data inefficient.jpeg]]
![[GOSDT banary problem representation.jpeg]]


Vedi esempio: ![[GOSDT computazione esempio.pdf]]

##### Algoritmo GOSDT
![[GOSDT algoritmo.jpeg]]

### Generalized additive models (GAM)