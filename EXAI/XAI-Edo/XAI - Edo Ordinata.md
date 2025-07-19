# Primo capitolo

L'explainable AI (XAI) produce e integra modelli di intelligenza artificiale per rendere interpretabile la logica interna e il risultato degli algoritmi, rendendo il processo comprensibile agli esseri umani.

Se un modello non fa parte di questa categoria si parla di **black-box** model.
Nel processo decisionale dovremmo tendere a favore dei modelli black-box solo se le prestazioni motivano questa scelta. 

![[explainability vs performance.png]]

Non ci sono infatti motivi per non andare verso un modello XAI se non per le prestazioni: siccome con i modelli XAI lavoriamo maggiormente sui dati, durante la costruzione del modello si può capire se il dataset è affetto da *bias*, se abbiamo formulato male il problema, o in generale il perché di una determinata risposta da parte del modello!
## Paradosso di Hans

Un uomo aveva un cavallo che reputava molto intelligente a livello scientifico: se gli veniva posta una domanda di tipo matematico allora rispondeva, battendo lo zoccolo per contare, bene; se però l'interlocutore si allontanava e non lo poteva vedere, ma lo poteva solo sentire, allora rispondeva male. 
La verità è che non aveva un'intelligenza matematica ma osservava molto bene il comportamento dell'interlocutore per rispondere bene.
Il risultato è che si parla di *paradosso di Hans* quando un agente da un risultato giusto ma per il motivo sbagliato. Altro motivo per cui un modello di XAI è da preferire è appunto il perché può capitare che un modello ci dia un output corretto ma il procedimento è sbagliato! => senza una motivazione non ce ne possiamo accorgere!
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

### Explainability

Quando si parla di explainability nel campo della [XAI](XAI/XAI.md) si intende la spiegazione delle decisioni prese dai modelli.
#### Explainability vs performace

In letteratura c'è un dibattito sul concetto per cui c'è una relazione inversa tra le performance e l'explainability di un modello. Un [grafico](XAI/File/explainability%20vs%20performance.png) molto comune in letteratura evidenzia quali modelli hanno delle prestazioni migliori rispetto alla explainability.
Il punto è che non c'è nessun teorema a favore di questa tesi. In alcune situazioni si riesce a ottenere modelli di XAI le cui performance sono paragonabili ai modelli blackbox.
#### Tecniche

Ci sono tre tecniche per valutare l'explainability di un modello, cioè se la spiegazione che ci da una blackbox è soddisfacente.
##### Application grounded evaluation

Utilizza umani esperti nell'applicazione su cui il modello lavora e richiede istanze (i.e., samples di test) reali. Ha costi elevati a causa dell'utilizzo di esperti (che costano) e di esempi di test reali.
Per valutare la spiegazione si possono confrontare le spiegazioni del modello e dell'esperto sulle stesse istanze di test o chidere all'esperto di valutare la spiegazione data dal modello.
##### Human gounded evaluation

Utilizza umani su applicazioni non tecniche e richiede quindi task reali ma semplici (non praticabile se l'applicazione richiede tecnicismo).
Ha costi meno elevati perché non sono interessati esperti e gli umani che valutano hanno costi ragionevoli.
##### Functionally grounded evaluation

Non utilizza umani e si devono usare task proxy.
È una tecnica valida quando non si possono usare umani perché non sarebbe fair, oppure quando non abbiamo un modello prontissimo per i costi degli esperti ma vogliamo avere una certa sicurezza sulla sua bontà.
#### Parametri

I parametri usati per spiegare l'explainability si possono distingue in due tipi.
##### Quantitativi

Sono parametri che devono essere valutati da umani.
- Completezza
	Una spiegazione potrebbe essere corretta ma non completa.
	Ad esempio un esperto potrebbe osservare anche altri parti che una mappa di salienza non mette in evidenza.
- Semplicità e complessità
	Rasoio di Occam: la spiegazione migliore spesso è quella più semplice.
	Dobbiamo in questo caso definire quando una spiegazione è semplice (e.g., per un albero di decisione la profondità).
- Plausibilità
	Misura quanto un utente è convinto dalla spiegazione del modello.
	In un articolo viene mostrata una [relazione tra accuracy e plausibility](XAI/File/accuracy%20vs%20plausibility.jpeg): se l'accuracy è molto elevata e un utente non è assolutamente convinto dalla spiegazione, allora può essere che il modello ha trovato qualcosa che l'umano non aveva notato.
- Generalizzazione
	Quanto quella spiegazione funziona bene su dati nuovi.
	È l’overfitting delle spiegazioni.
- Rilevanza
	Le spiegazioni sono rilevanti per un determinato dominio. Ci sono domini molto tecnici che hanno bisogno di spiegazioni ad hoc.
##### Ausiliari

Sono parametri che non coinvolgono umani.
- Sensibilità
	Quanto un modello è sensibile alla perturbazione di una feature.
	Ad esempio su un dataset di 1000 esempi quante volte cambiando una feature mi cambia l’output.
- Continuità
	Se ho due esempi simili, vorrei che questi avessero spiegazioni simili.
	Voglio che una spiegazione sia comune a una regione di spazio.
- Consistenza
	Vorrei che modelli diversi mi dessero la stessa motivazione per lo stesso input.
- Costo computazionale
	Quanto è costoso avere una spiegazione. Può succedere che il costo della spiegazione sia più oneroso del costo dell'output.
- Correttezza
	Si spiega da se.
	Non sempre è possibile però avere una verità assoluta con cui confrontare la spiegazione. Ad esempio due medici possono spiegare un risultato in modi diversi.
### Interpretability

Quando si parla di [explainability](regio/Explainability/Explainability.md) si intende la spiegazione delle decisioni prese dai modelli. Alcuni modelli sono spiegabili per costruzione (by design); in questo caso si parla di interpretability.



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

I modelli lineari calcolano l'output come $f(x)=\sum_{i=1}^P\beta_ix_i+\beta_0$, dove $P$ è il numero di features.
I modelli lineari sono molto interpretabili perché i coefficienti $\beta_i$ mi dicono il peso di ogni features, cioè mi dicono l'impatto che ha una modifica di $x_i$ sul risultato; in pratica se $x_i$ incrementa di una unità allora $f(x)$ incrementa di $\beta_i$.
Il problema dei modelli lineari è dato dal fatto che ==il mondo non è lineare==. Non riescono infatti a imparare la variazione dell'output rispetto alla variazione di più features contemporaneamente.
## Modelli Interpretabili per design

I seguenti modelli si basano, chi più chi meno, sugli [alberi di decisione](Decision%20tree.md):
- [Rule-based system](regio/Interpretability/Rule-based%20system.md)
- [Rule fit](regio/Interpretability/Rule%20fit.md)
- [GOSDT]
- [Generalized additive models (GAMs)](regio/Interpretability/Generalized%20additive%20models%20(GAMs).md)
- [Prototype base systems]

Inoltre appartengono a questa categoria i modelli basati sull'**ILP** ([Inductive Logic Programming])

### Alberi di decisione

Gli **alberi di decisione** sono un metodo molto utilizzato in **machine learning** e **data mining** per la classificazione e la regressione. Sono modelli semplici da capire e interpretare, che mimano una sequenza di decisioni logiche. 
Tipicamente usati per **Dati Tabulari**, mostrano una grossa interpretabilità

![[Screenshot 2025-07-12 at 11.11.49.png]]

È una struttura ad albero dove:
- Ogni **nodo interno** rappresenta una **domanda o condizione** su una caratteristica dei dati (es. "Età > 30?").
- Ogni **ramo** rappresenta un **risultato** possibile della condizione.
- Ogni **foglia** rappresenta una **classe** (in classificazione) o un **valore numerico** (in regressione).
    
In questo esempio:
- Le domande sono basate su **feature** (es. reddito, durata credito).
- Le foglie sono le **decisioni finali** (approva o rifiuta).

L’albero viene costruito scegliendo, ad ogni nodo, la domanda che meglio **separa i dati** in base al criterio scelto. I più comuni:
- **Gini index** (usato ad es. in CART) -> misura l'impurità di certi nodi a seconda di quanti esempi appartengano o meno ad una classe:
	- Se in un nodo ci sono solo esempi di una **sola classe**, l'impurità è **zero** (nodo "puro").
	- Se ci sono più classi mischiate, l'impurità è **alta**.
	- L’obiettivo durante la costruzione dell’albero è **minimizzare** l’impurità dopo ogni split.
    
	Per un nodo con K classi:$$Gini\,index=1−\sum_{i=1}^Kp_i^2$$
	dove:
	- $p_i$ è la proporzione degli esempi della classe i nel nodo.
	Un valore vicino a 0.5 indica una distribuzione **mista**, quindi alta impurità.
- **Entropia** (usato in ID3, C4.5) -> misura il contenuto informativo di un nodo, più alta è l'entropia è più il nodo è impuro, ha maggior contenuto informativo
- **Errore di classificazione**
- Per la regressione: **varianza** o **errore quadratico medio (MSE)**

I processi classici per imparare alberi di decisione (in maniera **greedy**) sono: CART, C4.5 etc...
- Tipicamente le divisioni sono **"a gradini"**, quindi meno precise rispetto ad altri metodi per dati continui e relazioni lineari, nonostante questo è in grado di gestire sia dati categorici che numerici
- Sensibile ai cambiamenti nei dati, e non stabile ai cambiamenti nel training set.
- Si raggiunge una profondità massima, che all'aumentare di questa aumenta di complessità
- Può **overfittare** facilmente (diventa troppo complesso).
- Può essere usato per estrarre **regole decisionali**. (vedi dopo)

### Rule-based system

I rule-based system sono modelli usati nel campo dell'explainable AI per la loro grande [interpretability](regio/Interpretability/Interpretability.md).
Sono sistemi che prendono decisioni sulla base di regole (decision rule)
$if (condizione),then (predizione)$, dove la condizione, che può essere composta anche da più predicati in AND, è detta antecedente e la predizione è detta conseguente.
##### Conseguenze
- Vantaggi
	- Alta interpretabilità.
	- Espressività di un [decision tree](Decision%20tree.md) ma **con regole più compatte** (più corte). In queste tecniche infatti non ci sono sotto alberi che si ripetono come nei decision tree.
	- Velocità dell'inferenza molto elevata. Solitamente non ci sono modelli più veloci.
	- Sono sparsi, cioè usano poche features.
- Svantaggi
	- Adatti solamente alla **classificazione**, a meno di quantizzare l'output della regressione. Per quantizzazione si intende trasformare un insieme continuo in un insieme discreto.
	- Le features devono essere categoriche e non numeriche. Se sono numeri allora si devono raggruppare i valori divisi da una soglia per ottenere delle classi. (in modo simile agli alberi di decisione)
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

Per imparare le regole ci sono varie strategie. Le principali sono:
- [Sequential covering]
- [Bayesian rule lists]
##### Sequenzial covering

Questo tipo di algoritmo è un algoritmo greedy (come quelli basati sui [decision tree](Decision%20tree.md)). Intuitivamente l'algoritmo:
- Inizializza una lista di regole $ruleList$ vuota.
- Impara una regola $r_j$ da $D$. (come vedi dopo)
- Finché il criterio di arresto non è soddisfatto:
	- Aggiungo $r_j$ a $ruleList$.
	- Rimuovo gli esempi coperti da $r_j$ da $D$.
	- Apprendo un'altra regola $r_j$ da $D$.
- Si restituisce $ruleList$.
###### Imparare regole

Tipicamente per apprendere una regola si apprende un [albero di decisione](Decision%20tree.md) (e.g., con l'algoritmo cart che è veloce) e poi si estrae la regola definita dal ==percorso che comprende per ogni livello il nodo più puro== (secondo la definizione del [gini index](Decision%20tree.md#Score/Metriche)).
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
- Si estraggono dei patterns frequenti sui dati iniziali (ad esempio usando *apriori* oppure *fp-growth* -> algoritmi di data mining). Per pattern si intende un insieme di condizioni messe in AND; per frequente si intende che questo è verificato da un numero di dati maggiore di una data soglia. In pratica è l'insieme da cui definire le regole.
- Generare una lista di regole iniziale.
	Questa generazione avviene campionando su una distribuzione a priori, costruita con l'obiettivo di generare **poche regole e corte**; il numero e la lunghezza delle regole sono gli *iperparametri* della distribuzione. 
- Si **modifica** la lista aggiungendo, rimuovendo o modificando regole della lista.
- Si sceglie la migliore lista secondo la posterior probability distribution ottenuta tramite la regola di bayes. $$P(d|x,y,A,\alpha,\lambda,\eta)\propto P(d|x,y,\alpha)\cdot P(d|A,\lambda,\eta)$$
###### Posterior

La posterior è definita da $P(d|x,y,A,\alpha,\lambda,\eta)$ e mi dice quanto è ==probabile la decision list $d$ dati quei dati e la conoscenza a priori sulle liste.==
Si può dimostrare che $P(d|x,y,A,\alpha,\lambda,\eta)\propto P(d|x,y,\alpha)\cdot P(d|A,\lambda,\eta)$, cioè che è direttamente proporzionale a due fattori: 
- una *likelihood* sui dati, ovvero la probabilità di osservare certi data under different parameter values of a statistical model. (nel nostro la scelta delle classi da rappresentare)
- la probabilità della decision list dati gli iperparametri delle liste.

Si vede allora che la posterior è alta se $d$ classifica bene i dati (dalla likelihood) e ha delle caratteristiche che corrispondono a quelle della prior, cioè quelle che abbiamo definito come parametri per ottenere la lista di regole(dalla prior).

In particolare gli elementi sono:
- $d$ è la decision list.
- Dati
	- $x$ sono le features.
	- $y$ è il target.
	- $A$ è l'insieme di pattern frequenti trovati.
- Iperparametri
	- $\alpha$ sono gli iperparametri di una distribuzione di dirichlet. Per semplicità possiamo dire che $\alpha$ è un vettore di pesi da attribuire alle classi; la scelta tipica è $\alpha=1^c$, con $c$ numero di classi.
	- $\lambda$ è il prior sul **numero di regole**, in particolare il valore atteso.
	- $\eta$ è il prior sulla lunghezza delle regole, in particolare il valore atteso.
##### Algoritmo

- Pre-mining dei pattern $A$ con FP-growth (un algoritmo simile a [A-Priory](A-Priory%20algorithm.md), non da sapere).
- Si sceglie il **numero di regole** $m$ (ovvero la lunghezza della lista) da una distribuzione di poisson con parametro $\lambda$. 
	- Se lambda è basso allora ho meno regole. Questo passo ci introduce la stocasticità perchè campioniamo da delle distribuzioni. 
- Per ogni regola $j=1,\cdots,m$:
	- Si sceglie la l**unghezza della regola** con $l_j$ da una poisson con parametro $\eta$ (prior sulla lunghezza delle regole). Altro punto in cui si introduce stocasticità.
	- Si scelgono da $A$ un insieme di condizioni (messe in AND) di lunghezza $l_j$.
- Adesso ho trovato **la decision list iniziale** e vado avanti in un **processo iterativo**.
	- Tramite il metodo montecarlo ==si seleziona in modo casuale se aggiungere, togliere e modificare== le regole della decision list e si produce un grande numero di altre decision list.
	- Dato che abbiamo finito la $k$-esima iterazione, per ogni decision list prodotta $d^{k+1}$ si ==calcola la sua posterior== $p(d^{k+1}|\cdots)$ e si memorizza la decision list che ha la posterior più alta in questa iterazione.
- Calcola la decisione list finale come $$d^*=\displaystyle\arg\max_{k}P(d^k|\cdots)$$, cioè la migliore tra tutte quelle memorizzate durante il processo iterativo.

Riassumendo i vantaggi delle Liste di decisione sono:
- Interpretabilità
- Espressività come alberi di decisione ma più compatte
- Inferenza veloce -> predefined rules and straightforward logic. Each rule is typically structured as an "if-then" statement, allowing the system to quickly match conditions with corresponding actions without complex calculations. 
- Modelli sparsi (con poche feature attive)

Ma i contro principali sono:
- Non posso fare regressione (a meno di quantizzare)
- Le feature non possono essere numeriche
- Si modellano difficilmente le relazioni lineari -> possibile soluzione è usare[RuleFit]

### RuleFit
##### Idea
L'idea alla base di rule fit è mappare lo spazio delle features tramite delle regole, ovvero usare le regole come features di un modello lineare; in pratica l'antecedente (insieme di condizioni sulle features originali messe in AND) di una regola diventa la nuova features, e se una regola vale allora la feature ha valore positivo.
In questo modo il modello diventa ==non lineare nello spazio delle features originale==, ma lineare nel nuovo spazio.
#### Algoritmo

L'algoritmo rule fit aggiunge un termine alla classica [funzione lineare](regio/Interpretability/Interpretability.md#Modelli%20lineari) e quindi l'output viene calcolato come $$f(x)=\beta_0+\sum_{i=0}^P\beta_ix_i+\sum_{j=1}^R\alpha_jr_j$$dove $r_j$ è la $j$-esima regola e $\alpha_j$ è il peso corrispondente.
##### Apprendimento regole

Per apprendere le regole fit rule utilizza un metodo ensamble (combinazioni di modelli diversi), come può essere una random forest o un gradient boosting (comunque deve essere un insieme di alberi).
##### Recup su metodi [ensemble]:

- [Random forest]: Si basa sulla creazione di molti alberi decisionali (da qui il termine "foresta"). Ogni albero viene addestrato su un **sottoinsieme casuale dei dati** e utilizza ==una selezione casuale delle features per prendere decisioni==. Il risultato finale si ottiene combinando le previsioni di tutti gli alberi: per la classificazione si usa la modalità ==(la classe più frequente)==, per la regressione la media.

- [Gradient Boosting] : Si basa sul concetto di "boosting", che consiste nel combinare più modelli deboli (solitamente alberi decisionali poco profondi) per creare un modello più forte e preciso. Il processo si svolge in modo iterativo: ==ad ogni iterazione viene aggiunto un nuovo modello che cerca di correggere gli errori commessi dai modelli precedenti==. Questo avviene calcolando i residui (le differenze tra le predizioni e i valori reali) e **addestrando** il nuovo modello per prevedere questi errori. I risultati vengono poi combinati attraverso una somma ponderata. Un aspetto fondamentale del Gradient Boosting è l'uso della discesa del gradiente per ottimizzare la funzione di perdita, da cui deriva il nome.
	![[Screenshot 2025-07-12 at 19.20.38.png]]
	
=> La differenza principale fra i due è che se *random forest* viene fatto in parallelo, *gradient boosting* è fatto in sequenza e il modello finale è una combinazione pesata (somma o media) dei vari alberi generati
##### Loss

Per imparare $\alpha$ e $\beta$ della funzione che poi genera l'output usiamo:$$\alpha^*,\beta^*=\displaystyle\arg\min_{\alpha,\beta}\sum_{i=1}^nL(y_i,f(x_i))+\lambda(\sum_{i=1}^P|\beta_i|+\sum_{j=1}^R|\alpha_j|)$$
dove l'iperparametro $\lambda$ (*lasso regularizer*), gestisce la sparsità della soluzione, ==cioè la quantità di regole che vogliamo aggiungere==: un valore alto indica poche regole.
Questo ha senso perché vogliamo che il nostro output, cioè $f(x)$, sia determinato da poche regole, in modo che sia più interpretabile; se avessimo infatti una soluzione con molto regole allora il modello sarebbe poco interpretabile.

##### **Vantaggi di RuleFit**

- **Interpretabilità**: Le regole sono espresse in linguaggio naturale.
- **Performance**: Combina la flessibilità degli alberi con la stabilità della regressione.
- **Feature Importance**: Mostra l'importanza delle regole e delle variabili originali, allo stesso modo di un modello lineare!
Allo stesso tempo, la scelta sul numero di regole e sulla loro lunghezza rimane un punto aperto... aumentare il numero di regole può comportare una maggiore accuratezza a patto però di perdere sia in efficienza che interpretabilità
#### Librerie (per i modelli visti)
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

Gli approcci per ottenere di albero di decisione visti sono greedy, in quanto considerano per ogni split, il valore migliore a seconda del parametro scelto (tipo Gini Index o information Gain Ratio). Approcci dunque che falliscono nell'ottimizzare **la funzione di costo totale** dell'intero albero, e non sono pensati per ottimizzare una qualsiasi metrica di performance.
Infine l'ottimizzazione di un albero di decisione completo è un problema *NP-complete*

- In generale per gli alberi, vale:

![[Screenshot 2025-07-12 at 16.36.24.png]]
$\lambda \,, D$ sono gli iperparametri usati per controllare **sparsità** e **costo computazionale**

**GOSDT (Generalized Optimal Sparse Decision Trees)** è un algoritmo progettato per costruire alberi **decisionali ottimali**, bilanciando accuratezza predittiva e semplicità del modello. Ecco come funziona in breve:

1. **Ottimizzazione Globale**:  
   A differenza degli alberi decisionali tradizionali (come CART o C4.5), che usano approcci *greedy*, GOSDT cerca l'albero con la **migliore combinazione di accuratezza e semplicità** tramite ottimizzazione matematica, viene infatti ottimazzata la funzione scritta sopra, stando attenti a considerare sia il numero di foglie che la profondità dell'albero ottimale. 

2. **Regolarizzazione Sparsa**:  
   Introduce un termine di regolarizzazione per penalizzare alberi complessi, favorendo strutture più piccole e interpretabili, evitando l'overfitting.

3. **Efficienza Computazionale**:  
   Usa tecniche come *bounds* (limiti superiori/inferiori) e *pruning* dinamico **per ridurre lo spazio di ricerca,** (tipico della programmazione dinamica) rendendo possibile trovare soluzioni ottimali anche per dataset di medie dimensioni. 

4. **Interpretabilità**:  
   Produce alberi compatti e facili da comprendere, mantenendo prestazioni competitive con modelli più complessi (es. random forest o reti neurali).

**Vantaggi**:  
- Alberi ottimali (non subottimali come nei metodi greedy).  
- Modelli interpretabili con buona accuratezza.  

**Svantaggi**:  
- Computazionalmente costoso per dataset molto grandi.  

L'algoritmo segue le seguenti idee di base:

- Serve binarizzare i miei dati, secondo i valori di determinate feature

![[GOSDT binary data inefficient.jpeg]]

- A quel punto rappresento i problemi in forma binaria: secondo la divisione dei miei dati, tramite vettori binari contenenti una serie di 1/0 se appartenente o meno ad una determinata classe

![[GOSDT banary problem representation.jpeg]]

- Uso una coda con priorità $Q$ per gestire l'espansione dei problemi candidati
- Considero un grafo di dipendenza per rappresentare tutti i sottoproblemi da risolvere
- Infine, uso tecniche di *pruning* per calcolare lower/upper bound dei problemi (nodi)

Vedi esempio: ![[GOSDT computazione esempio.pdf]]
Formula per il calcolo di Lower e Upper Bound:
![[Pasted image 20250712162415.png]]
##### Algoritmo GOSDT

![[GOSDT algoritmo.jpeg]]

### Generalized additive models (GAM)

I GAMs sono modelli usati nel campo dell'[interpretability](regio/Interpretability/Interpretability.md).
Sono modelli adatti quando si lavora con dati tabulari e sono molto buoni quando le features sono continue; nel caso discreto (features categoriche) allora la $f_i$ sarà una funzione a gradini (istogramma).
##### Idea

L'idea dei GAMs deriva dal voler mantenere l'interpretabilità dei [modelli lineari](regio/Interpretability/Interpretability.md#Modelli%20lineari) $y=f(x)=\sum_{i=1}^P\beta_ix_i+\beta_0$ aggiungendo una qualche complessità.

Questi modelli ottengono il target $y$ ==in modo additivo==, dove i vari termini sono risultati di **modelli** complessi (volendo anche non lineari) **indipendenti**, ==valutati su una singola feature==.

Il modello GAM generale può essere descritto da $$y=g(\sum_{i=1}^Pf_i(x_i))  =>  g(y)=\sum_{i=1}^Pf_i(x_i) $$dove:
- $P$ è il **numero di features**;
- La funzione $g$ è detta **link function** che può essere:
	- l'*identità* e in quel caso si ha una **regressione** fatta "in modo additivo"; 
	- *la sigmoide* allora abbiamo una **classificazione** (una specie di regressione logistica additiva??)
- Mentre le $f_i$ sono dette **shape function** => se questo sono non lineari, il modello è non lineare.

##### Interpretabilità

Hanno un'ottima interpretabilità perché possiamo definire l'impatto ==che ogni feature ha sull'output==; anche se ogni $f_i$ è molto complessa possiamo analizzarla indipendentemente dalle altre tramite un grafico **in una variabile**.
- Ha un'**interpretabilità locale** perché durante l'inferenza ci fa vedere ==su un singolo esempio il contributo di ogni features.==
	![[Screenshot 2025-07-12 at 20.00.44.png]]
	Ogni feature ha un proprio grafico!

- Ha un'**interpretabilità globale** perché ho la $f$ in forma analitica, sia per tutte le features messe insieme che per la singola feature. Riesco quindi a osservare ==quanto la features contribuisce al valore finale== rispetto a tutti i valori possibili.
	![[Pasted image 20250712200633.png]]

##### Bias

Questi modelli spesso ci ==offrono punti di vista che le sole statistiche descrittive non mettono in evidenza==; è infatti ottimo per capire come i dati sono costruiti.

In presenza di bias nei dati (es: un asmatico può avere meno rischio rispetto a una persona sana alla contrazione di una polmonite; ovviamente non è così ma se i dati ci dicono questo allora il modello apprenderà questo; il motivo per cui invece succede è che un asmatico viene curato più di una persona sana alla contrazione della polmonite), un esperto può cambiare la predizione del modello modificando direttamente ==la funzione che agisce sulla feature che è responsabile dell'introduzione del bias==.

![[Pasted image 20250712200847.png]]

L'esperto guardando i grafici può quindi interpretarli
##### $GA^2M$

Il problema che si può osservare è che il modello ==non osserva relazioni tra più features contemporaneamente==, nel caso alcuni contributi siano in relazione fra di loro, questi me li perderò nella scelta del modello-

Nella versione base è vero, ma questo si può implementare facendo si che ogni **shape function** agisca anche su più variabili; in questo caso il modello si può definire come: $$y=g(\sum_{k=1}^Pf_k(x_k)+\sum_{k_1=1}^P\sum_{k_2=k_1+1}f_{k_1k_2}(x_{k_1},x_{k_2}))$$Il problema nasce se le possibili coppie sono troppe; in questo caso si usa un iperparametro che agisca **sul numero massimo di coppie analizzate**; queste saranno scelte tramite una qualche euristica.
Se però osserviamo molte variabili (solitamente già per più di due), ==allora perdiamo l'interpretabilità del modello.==

![[Screenshot 2025-07-12 at 20.00.44.png]]

- Le *heatmaps* sono necessarie per mostrare le dipendenze fra le features
#### Explainable Boosting Machine

Una specifica implementazione delle GAMs sono le *Explainable Boosting Machine* (EBM), dove ogni $f_i$ è un ensamble di [alberi di decisione](Decision%20tree.md) addestrati tramite una tecnica di [gradient boosting](Ensamble.md#Gradient%20boosting).

![[EBM training.png]]

Se consideriamo una regressione, l'algoritmo che apprende una EBM è:
- $f_j=0$ per ogni features $j$.
	- Stiamo mettendo a 0 tutte le predizioni sulle singole features.
- for $m=1$ to $M$, dove $M$ è il numero di iterazioni ($M$ è l'upper bound, ==ma possiamo anche fermarci prima se il modello non sta imparando più di una data soglia==):
	- for $j=1$ to $P$, dove $P$ è il numero di features (si impara un albero $S$ basandosi su una features alla volta):
		- Si impara un residuo (rispetto al target): $$R=\{x_{ij},y_i-\sum_{k=1}^{m-1}f_k\}_{i=1}^n$$dove la somma delle varie $f_k$ sono ==quanto appreso da tutti gli alberi precedenti== (sia iterazioni precedenti sia di features precedenti); in pratica i target sono quanto manca al totale da apprendere.
		- Si impara una *shape function* $S$ (che nelle EBM sono alberi) che usa $R$ come training set.
		- Si aggiorna $f_j=f_j+S$. => ogni feature è somma dei vari alberi ottenuti sequenzialmente per ogni iterazione su quella determinta feature
##### Funzionamento

Quello che stiamo facendo è quindi produrre un albero per ogni features e questo impara quanto **non aveva imparato l'albero prima**; questo concetto è detto residuo, il quale passa anche da iterazione a iterazione e non solo da features a features, altrimenti si inizierebbe da capo.
Al termine di tutte le iterazioni avremo molti alberi per ogni features; sommandoli tutti si ottiene il grafico in relazione della features.
Il modello finale che predice invece è ottenuto ==sommando tutti i risultati che si ottengono dai modelli== che analizzano la singola features.
##### Residuo

Quello che succede al residuo è che a ogni passaggio di features **può aumentare o diminuire**, ma alla fine convergerà.
Questo succede perché il modello alla prima features ha imparato qualcosa, ma quando corregge la sua idea osservando solo la features successiva potrebbe peggiorare quanto imparato dalla prima features. Quando all'iterazione successiva torniamo a osservare la prima features il residuo potrebbe essere molto diverso da quello che aveva lasciato.

#### Neural additive models

Sono modelli i cui *termini additivi* sono prodotti da **delle reti neurali**.
##### Architettura

Questo ha senso per le GAMs, non ci dicono in che modo implementare le $f_i$, ma ci dicono solo che sono funzioni più o meno complesse; le reti neurali sono delle approssimazioni universali di funzioni (?) e quindi ha senso usarle.

In questa situazione è che le reti hanno un solo neurone nel primo layer, che corrisponde alla singola feature analizzata, vengono infatti create delle sottoreti (di complessità a piacere) per ogni singola feature => reti che sono parallelizzabili (e scalabili) su GPU. 
- buono per le performance! (a patto di reti non troppo complesse) => e inoltre mantengo l'interpretabilità dei GAMs

I contributi sono quindi sommati nel layer di uscita, per la previsione finale $$g(E[y])=β_0​+f_1​(x_1​)+f_2​(x_2​)+⋯+f_p​(x_p​)$$
##### Attivazione

Invece che usare la funzione di attivazione [ReLU](Neurone%20artificiale.md#ReLU), questi modelli solitamente utilizzano la funzione [ExU](Neurone%20artificiale.md#ExU).
Il motivo di questa scelta è data dal fatto che nei grafici con cui osserviamo la variazione dell'output rispetto a una features ci interessa particolarmente le variazione repentine per piccole variazioni dell'input; questa activation function permette di ottenere proprio questo vantaggio.

![[Pasted image 20250712211908.png]]
#### **Librerie**:
- [InterpretML](https://interpret.ml)
	È la miglior libreria per quanto riguarda le boosting machine ma ci sono altri modelli, comprese tecniche per spiegare modelli black box.
	- Si integra perfettamente con scikitlearn.
	- Solitamente gli iperparametri di default della classe $ExplainableBoostingMachine$ funzionano molto bene.
	- L'output è fatto benissimo e ci da una spiegazione ben fatta dell'importanza delle features con un menù a tendina con grafici e distribuzione per ogni features.

### Prototype based systems

#### L'idea di base: KNN: K-Nearest Neighbors

Da un dataset di esempi, classifico un un ulteriore esempio in base ai K esempi più vicini all'esempio da classificare, prendendo le decisioni in base a votazioni/medie pesate.

Dal punto di vista dell'interpretabilità, questo è un risultato interessante in quanto tramite gli esempi più similari nel training data riesco a dare una spiegazione

Questo risulta intuitivo per alcuni tipi di dati => ad esempio per le immagini!
Rimane comunque una spiegazione di tipo locale e non globale, e inoltre diventa complicato da interpretare con molte features.

*K-nearest neighbors* è un istanza dei modelli di tipo *case-based reasoning* => dove si confronta con casi del passato per la mia spiegazione. 
#### ProtoPNet

Prendono quindi ispirazione da qui le *ProtoPNet*, che sono architetture basate su reti neurali
##### Architettura

L'architettura di una ProtoPNet è formata di 3 parti:
- [Convolutional neural network] $f$
	- con parametro $W_{conv}$ , per estrarre il numero di *filtri*
- [Prototype layer] $g_p$
	- con parametro $W_h$ , per il numero di nodi
- [Fully connected layer] $h$ 

![[Screenshot 2025-07-13 at 11.18.30.png]]

Presa quindi un immagine $f(x)$ genero in output dalla *rete convoluzionale* una serie di $D$ filtri di dimensione $HxW$. Insieme di filtri che vengono quindi chiamati *prototipi* che sono in numero: $$P = \{P_j\}_{j=1}^m \,, \text{ con } \, m = m_k \, x \, K$$
Dove:
- $m_k$ sono il numero di prototipi per classe
- $K$ sono il numero di classi
- Ogni prototipo $P_j$ ha dimensione $H_1$ x $W_1$ x $D$ , con $H_1 \leq H$ e $W_1 \leq W$ , ovvero imparo solo un pezzettino della mia immagine detto *patch* (utili per analizzare **pattern locali**, come bordi, texture, ecc...) , oppure l'immagine per intero.

##### Inferenza

![[Pasted image 20250713121238.png]]

Partendo un'immagine di test $x'$:
1. Applico l'architettura convoluzionale, da cui estraggo le mie patch/mappe di features.
2. Il modello seleziona un certo numero di prototipi (nel nostro caso $m$)
3. Calcolo le distanze su tutti i prototipi come: $$ S = \frac{1}{dist(z',P_j)}$$ ottenedo così uno *score di similarità* 
4. Faccio scorrere la patch su tutta l'immagine, calcolo le distanze e cerco le migliori similarità fra immagine di partenza e prototipo. Sostanzialmente mi dicono: "Quanto vedi di un certa cosa in quel immagine?"
5. Eseguo un operazione di *max pooling* da cui ricavo fuori le varie $S_{p_1}, ... , S_{p_m}$, in questa operazione si prende il max dello score come minimo della distanza.![[Pasted image 20250713122109.png]] Più la distanza aumenta e meno sarà la similarità.
6. Quantità di *score* che vengono infine usate come input per il layer fully connected.

Esempi:

![[02_Interpretable_by_design-26 2.pdf]]

##### Training

La parte di addestramento viene eseguita in 3 steps (che possono essere iterati):
1. ***Stocastic gradient Descent*** per tutti i layer eccetto l'ultimo, viene eseguita un ottimizzazione congiunta fra i pesi dell'architettura convoluzionale $W_{conv}$ e dei prototipi $\{p_j\}_{j=1}^m$. Lascio invece "frozen" i pesi dell'ultimo layer $h$ , [smart initialization](https://www.google.com/search?client=safari&rls=en&q=smart+initializion&ie=UTF-8&oe=UTF-8&safe=active) . La funzione obbiettivo da ottimizzare è $$ min_{W_{conv}, \{P_j\}} \\\ \frac{1}{n} \sum_{i =1}^n L(h \, o \, g_p \, o \, f(x_i), y_i) + \lambda_1 clst + \lambda_2 sep$$dove:
	![[Pasted image 20250713124835.png]]
	![[Pasted image 20250713124940.png]]
	Aggiungo dei termini regolarizzatori alla *loss di classificazione*, con l'obiettivo di:
	- **Minimizzare** la distanza dei patch rispetto ai prototipi delle classi alle quali appartiene l'immagine.
	- **Massimizzare** la distanza dei patch rispetto ai prototipi delle classi alle quali **non appartiene** l'immagine.
  
2. Eseguo un operazione di ***Prototype projection*** dove ogni $P_j$ viene sostituito:![[Pasted image 20250713125957.png]] 
	Vado alla ricerca della patch che assomiglia di più al prototipo della classe K, ==ho dunque una spiegazione su come viene classifica una certa patch.== 
	
	Notare che alla fine non ho la garanzia che una patch mi porti ad una confidenza su una delle immagini del training set, la patch è ottenuta come il minimo dei parametri ma non ho garanzie che si avvicini il più possibile al prototipo di una certa classe. 
	L'operazione di proiezione nella quale si approssimano i vari pesi, può avere problemi di perdità di ottimalità, ho comunque un teorema che mi assicura la non perdità di accutezza. 
3. ***Last layer convex optimization***: in maniera opposta al primo passaggio, si esegue l'ottimizzazione solo per l'ultimo layer, tenendo "frozen" in questo caso la parte delle reti convoluzionali e dei prototipi. $$ min_{W_h} \\\ \frac{1}{n} \sum_{i =1}^n L(h \, o \, g_p \, o \, f(x_i), y_i) + \lambda \sum_{i=1}^K \sum_{j \,  \text{t.c} \, p_j \notin P_K} | W_h ^{(K,j)}|$$ Con l'obiettivo di portare a zero il termine regolarizzatore, per tutti i prototipi non appartenenti alla relativa classe.

### Inductive Logic Programming

Si individuano delle **teorie logiche** sui dati, delle formalizzazioni che portano a regole e predicati/clausole per poter fare operazioni di classificazione.
Tramite descrizioni del mondo riesco a indurre delle regole, ottenute attraverso predicati.

#### Logic Programming

Linguaggio non imperativo ma dichiariativo, ovvero al posto di dare dei comandi fornisco delle spiegazioni di cosa devo fare, specificando la lista di regole/comandi da eseguire, come fa ad esempio SQL.
Il linguaggio più famoso di questo tipo è il *Prolog* (1970)
##### Sintassi 

- **Variabili**: simboli in maiuscolo ad es. "X,Y"
- **Costanti**: simboli in minuscolo ad es. "alice,bob"
- **Predicati**: in minuscolo ad es: "father/2",
- **Termini**: una variabile oppure una costante oppure funzione con $n$ argomenti seguita da una tupla di $n$ valori
- **Atomi**: formula del tipo $p(t_1,..., t_n)$ dove p è un predicato e $t_1,...,t_n$ sono i termini, ad esempio: "father(X,Y), father(X,alice), father(bob,alice)" sono tutti atomi e inoltre se i termini sono solo costanti si dice *ground*
- **Negazione**: si ottiene dal *not* seguito da un atomo ad es: "not father(bob,alice)"
- **Letterale**: un atomo o la sua negazione
- **Clausola** (o regola): $h_1,...,h_m :- b_1,...,b_n$ , diviso in testa (head) e corpo (body), dove entrambi sono fatte di *letterali*
	- Caso particolare è l'*horn clause*, che ha **un solo letterale positivo** in testa
	- Come per gli atomi, se ci sono solo costanti si parla di *ground clause*
	- Valgono le regole di *de Morgan*, ovvero la negazione di and diventa l'or di not dei letterali![[Pasted image 20250713164124.png]]
- **Teoria**: definita come l'insieme di clausole

##### Semantica

Si basa sul concetto di:
1. [Herbrand Universe] U: Il primo è l'insieme di tutti i possibili *termini ground* che possono essere formati con le costanti (e le funzione)
	- Ad esempio: "{alice, bob, carl, david, object1, object2, ...}"
2. [Herbrand Base]: La **base di Herbrand** è invece l'insieme di tutti i possibili *atomi ground* che possono essere formati con la lista di predicati/funzioni insieme a l'Herbrand Universe U 
	- Ad esempio: "{happy(alice), happy(bob), happy(carl), healthy(alice), ...}"
3. [Herbrand Interpretation]: da un valore di verità a ==tutti gli elementi presenti nella base di Herbrand==
	- Ad esempio: "happy(alice) => TRUE - happy(bob) => FALSE"

##### Esempio

![[Pasted image 20250713165904.png]]
Per closed-World assumption si intende che ciò che viene scritto è vero, il resto (spazi vuoti lasciati apposta) non lo è.

Vorrei dunque imparare una teoria per spiegare il predicato "happy/1", ho quindi un obiettivo di una sola clausola, e nostro caso la soluzione è $$happy(X) :- healthy(X), passedexam(X).$$
Il concetto è simile a quello di prendere una feature come target e il resto lo uso come spiegazione!

Diremo quindi una *herbrand interpretation* è un modello per la clausola $c$ se $c$ è soddisfatta per tutti i *groundings*(i fatti). Ovvero se la clausola risulta soddisfatta per ogni costante nella base di herbrand.
+ Si parlerà di **Entailment*** (implicazione) nel caso in cui ogni modello di T è anche un modello per $c$ 
	![[Screenshot 2025-07-13 at 17.11.44.png]]

##### Learning In ILP Systems

Vediamo 2 modi per fare addestramento in sistemi ILP:
1. [Learning from Entailment] (LFE)
2. [Learning from interpretations] (LFI)
3. Esistono altri ma poco usati

###### Learning From Entailment

- Presa una *Knowledge base* B, fatta di:
	- Una lista di predicati ground, tipo costanti o variabili (le mie features)
	- Una lista di clausole (relazioni fra le features) 
- Gli esempi positivi $E^+$ e quelli negativi $E^-$, riguardanti un determinato target (che vogliamo imparare) => esempi positivi e negativi che formano una singola interpretazione, ad esempio:
	![[Pasted image 20250713175257.png]]
	(vale ancora closed world assumption per B)

L'obiettivo è quello di **imparare una teoria logica** (ovvero una collezione di regole) che spieghi il concetto target, ovvero:
- Dati $B, E^+, E^-$ trovare un ipotesi $h \in H$ tale che:
	- $\forall e \in E^+$ $h u H \, |= e$ (Complete)
	- $\forall e \in E^-$ $h u H \, /= e$ (Consistent)
=> Ovvero vorrei che la teoria sia:
- **Completa**: copra tutti gli esempi positivi
- **Consistente**: eviti tutti gli esempi negativi

###### Learning From Interpretations

Allo stesso modo:
- Dati $B, E^+, E^-$ (stavolta insieme di fatti da diverse interpretazioni) trovare un ipotesi $h \in H$ (dallo *spazio delle ipotesi*)tale che:
	- $\forall e \in E^+$ $H u B \, |= e$ => "e" è un *modello* di $HuB$ 
	- $\forall e \in E^-$ $H u B \, /= e$ => "e" non è un *modello* di $HuB$ 

In questo caso:
- B rimane lo stesso a LFE
- $E^+$ sono le interpretazioni che **soddisfano la teoria** 
- $E^-$ sono le interpretazioni che **non** soddisfano la teoria 
Ad esempio:
![[Screenshot 2025-07-13 at 18.22.57.png]]

L'idea è quella di avere una teoria che sia **vera** per ogni interpretazione in $E^+$, se infatti avessi un mondo in cui "alice e carl" siano "happy" e il resto no la teoria deve valere!

##### ILP System

I passi da seguire per usare un sistema ILP sono:
1. Definisco il *learning setting* , tipo LFE o LFI oppure altro ancora
2. Su questo baso il mio *representation language*, ovvero come rappresentare la *background knowledge* e se ho particolari regole da seguire sull'espressione del linguaggio (ipotesi e background knowledge)
3. Definisco il *Language Bias*, ovvero come definisco il mio *spazio delle ipotesi*
4. *Metodo di Ricerca*: come si cerca nello spazio delle ipotesi appena definito

![[Screenshot 2025-07-13 at 18.46.19.png]]

##### Aleph (2001)

Esempio di ILP system, che segue l'impostazione di LFE, i passi da seguire sono:
1. Scegli un esempio positivo da generalizzare
2. Costruisci la clausola ==più specifica possibile==, che sia comunque **consistente** con il bias del linguaggio, e **implichi un esempio** (questa è detta *bottom clause*). Ad esempio "happy(X) :- healthy(Y)" è vietato dal language bias.
3. Una volta costruita la clausola più specifica, si cerca una più **generica** e che abbia uno **score migliore**: $P - N$, con P il numero di esempi positivi coperti e N quelli negativi coperti dalla stessa clausola
4. Aggiungo la clausola a $H$ e rimuovo ==tutti gli esempi positivi==, coperti dalla clausola, infine ritorno allo step 1 fino ad ottenere la clausola fino dove ho coperto tutti gli esempi

+Nel caso di *Aleph* l'algoritmo di ricerca è guidato da una *bottom clause* che contiene tutti i predicati che appartengono all'esempio scelto in partenza, ad esempio:
![[Screenshot 2025-07-13 at 18.44.54.png]]

+[Problema dei treni di michalski](https://www.sfu.ca/iat813/lectures/lecture5.html) => difficile da risolvere con rete neurale per il grande numero di feature ma fattibile con ILP

![[Screenshot 2025-07-13 at 21.58.45.png]]

# Approcci Neuro-Simbolici

Un problema che il campo dell'AI vuole risolvere è ==cercare di utilizzare la stessa struttura e modi di fare del nostro cervello==. In merito a questo ci sono due tipi di approcci, quello [simbolico] e quello [connessionista] (sub-simbolico).
Queste due tecniche hanno sia differenze filosofiche che tecniche: non ce ne c'è una meglio o peggio, ma dipende dal caso d'uso.
## Simbolici

Il **ragionamento** avviene tramite la ==manipolazione di simboli== rappresentati tramite qualche formalismo.
### Conseguenze

- Si basa sulla [logica](XAI/ILP/Programmazione%20logica.md) e si vuole quindi sfruttare una *background knowledge.* 
- È **molto interpretabile**, come abbiamo visto per gli [ILP system](XAI/ILP/ILP%20system.md).
- ==Ha bisogno di features discrete== (valori finiti ed enumerabili). Diventa complesso, ma fattibile, il reasoning con valori numerici => non sempre la realtà 
- è divisa in due valori categorici...
- Non è un buon approccio quando abbiamo grandi quantità di dati. ==Come abbiamo visto per [Aleph system](XAI/ILP/ILP%20system.md#Aleph%20system) si deve costruire i *predicati grounded* (**quelli con tutte le clausole**) e questo porta a poca efficienza se abbiamo molti dati.== Questo è spesso il **collo di bottiglia** degli approcci simbolici, esistono però:
	- Tecniche smart per evitare di generare tutti i predicati
	- Sfruttare simmetrie e patterns/templates.
- Sono metodi soggetti al rumore. Se una regola vale ma non per tutti gli esempi, allora il modello imparerà quella regole e anche un'altra, in modo da coprire tutti gli esempi. (??)
## Connessionisti

Il **ragionamento** avviene tramite ==l'elaborazione del segnale tra unità fondamentali **interconnesse**==. Vogliamo in questo modo replicare il ragionamento che avviene nel nostro cervello. Si basa sulle **reti neurali**.
### Conseguenze

- Utile quando non abbiamo **una grande conoscenza di base**. I modelli scoprono infatti dei pattern in questi in modo non supervisionato.
	- Lo svantaggio sta che imparano anche i [bias](XAI/Bias.md) presenti nei dati.
- ==Non si devono codificare i dati== in qualche modo, ma il modello apprende da dati raw.
- Servono una **grande** quantità di dati, lavora meglio con grandi collezioni di dati => gli algoritmi tipicamente riescono a distribuire i dati!
- ==Non si ha una grande perdita di prestazioni== se nei dati viene introdotto del **rumore**. Le prestazioni decadono in modo lineare rispetto al rumore. => gestisce incertezza e dati rumorosi (*graceful degradation*)
- Spesso però sono visti come una "black box" => **mancano di interpretabilità**!

Ci chiediamo dunque:
-  Abbiamo davvero bisogno (come umani) di grandi collezioni di dati per imparare?
- Come possiamo acquisire skills di **generalizzazione**?
- Possiamo facilmente definire **regole** che guidano le nostre decisioni?
- Possiamo facilmente descrivere i dati tramite un formalismo simbolico?
## Unione - Combinare addestramento e ragionamento

Supponiamo di avere tre ingredienti: i metodi simbolici, quelli connessionisti e quello probabilistici. A seconda di come li uniamo otteniamo tecniche diverse.
Oggi questi mondi si incontrano sempre di più. In modo tale da sfruttare i punti di forza dei vari approcci

![[Pasted image 20250714153543.png]]

Le principali divisioni sono:
- [Machine/deep learning]:
	- Si ricava dall'unione degli approcci probabilistici e neurali. Ci sono solo features e variabili aleatorie, ma non simboli. Esistono soluzioni che permettono anche un po' di reasoning, come i LLM.
- [SRL/StarAI]:
	- È la *Statistical Relational AI* e unisce metodi probabilistici e simbolici. Un esempio è una [Markov Logic Networks](regio/Approcci%20neuro-simbolici/Markov%20Logic%20Networks.md).
- [Neural Symbolic Computation (NeSy)]:
	- Unisce metodi neurali e simbolici. Un esempio di questo tipo è [KBANNs](regio/Approcci%20neuro-simbolici/KBANNs.md) 

### NeSy

Altra branca di ricerca, con l'idea di combinare la logica con neuroscienza cognitiva.

L'obiettivo (come per le *KBAANs*) era quello di combinare **modelli neurali** e **approcci simbolici** per addestramento ragionamento, dunque di:
- Fare enconding della Knowledge nell'architettura della rete
- Usare un termine **regolarizzatore** per codificare le regole
- **Legare** le computazioni neurali con le regole

Da notare però che: iniettare knowledge nella rete neurale, e lasciare fare alla rete il resto può non essere sufficiente => rischio di perdere la parte di ragionamento e spiegazione!

Come usare la logica?
- Tipo una programma neurale(?) => questa è l'idea per le KBANN
- Come regolarizzatore?
	- In questo caso oltre la loss di classificazione standard aggiungo un termine aggiuntivo di penalità sulle ==soluzioni che portano a rompere alcuni vincoli== semantici (perdite sulla semantica(?)). $$Loss = ClassificationLoss + \lambda SemanticLoss$$
Ad esempio:
![[Pasted image 20250714165521.png]]
![[Pasted image 20250714165532.png]]

In questo caso ho tradotto la logica nella rete, in una funzione di loss differenziabile => ragionamento logico(?) => adesso ho un vincolo meno rigido!
#### Knowledge Base ANN (KBANN)

È uno dei primi tentativi (1994) di unire le tecniche basate sugli [approcci simbolici e quelli neurali](regio/Approcci%20neuro-simbolici/Approcci%20neuro-simbolici.md#Neural%20Symbolic%20Computation%20(NeSy)) inglobando le informazioni della conoscenza di base (espressa tramite la logica) **nell'architettura della rete**. 
Il risultato è una rete neurale, la background knowledge viene persa totalmente.

![[Pasted image 20250714155431.png]]
#### Idea

L'idea è quella di iniettare la conoscenza simbolica nelle reti neurali. Quindi si costruisce una rete neurale ad-hoc, che si basa su una background knowledge. La conoscenza di base su un qualche dominio è rappresentata tramite il **simbolismo** e quindi si basa sulla [logica](XAI/ILP/Programmazione%20logica.md).
Sulla base di questa conoscenza si costruisce una **rete neurale ad-hoc** (iniziale), che permetta di rappresentare esattamente quella logica:
- le variabili (i.e. la testa di una regola) diventano i neuroni; 
- gli archi uscenti dai neuroni sono le ==relazioni tra testa e coda di una regola==, cioè i neuroni al livello sottostante sono gli elementi della coda della regola.

![[esempio KBANN.png]]

In questa costruzione posso aggiungere **altre regole con nuovi elementi** nella testa che esprimono le stesse cose; in questo modo si può imparare poi nuova conoscenza.

Aggiungo inoltre tutte le connessioni in modo da creare una rete *fully connected*; in questo modo la rete è più semplice da addestrare tramite la back propagation e posso apprendere più cose. 
I pesi di queste connessioni saranno inizializzati **a valori molto piccoli**, contro le connessione reali (presenti nella background knowledge) che avranno pesi più grandi.
(punto a favore dell'interpretabilità!)
Questa rete viene poi addestrata tramite degli esempi di training.

Questo fu un primo tentativo di "ibridazione", ma con limiti: le reti diventano abbastanza ccomplesse e la logica può perdersi durante l'apprendimento.
### SRL/StarAI

Più recenti tentativi di combinare **Logica e Probabilità**.
L'obiettivo è quello di mettere insieme logica di primo ordine e modelli grafici per addestramento e ragionamento:
- Sfruttare a pieno la **potenza espressiva** della logica
- Gestire l'incertezza con **modelli grafici**
- Combinare inferenza **logica e probabilistica**, dove:
	- **Inferenza logica**: inferire il valore di verità su alcuni fatti logici, in base ad un collezione di fatti e regole
	- **Inferenza probabilistica**: inferire la distribuzione a posteriore di variabili aleatorie non osservate, date quelle già osservate.

+Esempio di inferenza logica:
- **Regola**:  
  ```prolog
  likesmovie(X,M) :- moviegenre(M,G), likesgenre(X,G).  
  likesmovie(X,M) :- friends(X,Y), likesmovie(Y,M).
  ```
- **Fatti noti**:  
  ```prolog
  moviegenre(bladerunner, scifi).  
  likesgenre(alice, scifi).  
  friends(alice, bob).
  ```
- **Fatto derivato (inferito)**:  
  ```prolog
  likesmovie(alice, bladerunner).  % Per la prima regola
  likesmovie(bob, bladerunner).    % Per la seconda regola (se bob non ha likesgenre diretto)
  ```

**Come funziona?**  
- **Forward Chaining**: Parte dai fatti e applica regole fino a trovare conclusioni.  
- **Backward Chaining**: Parte da un goal (es. `likesmovie(bob, bladerunner)`) e verifica se è supportato dai fatti. (non c'è spazio per incertezza o eccezioni)

Esempio di questo caso sono le [Markov Logic Networks]
#### Markov Logic Networks (skip this)

È un modello derivato dall'unione di [approcci statistici e simbolici](regio/Approcci%20neuro-simbolici/Approcci%20neuro-simbolici.md#StarAI). Se la logica impone **vincoli hard** sul set delle possibili parole, in questo caso si sfruttano **vincoli soft**
##### Definizione

Una *Markov Logic Network* è definita:
- da un **insieme di regole** 
- dei **pesi**, uno associato a ogni regola 
=> più il peso di una regola è alto più voglio che la regola sia vera. In questo caso dunque se ho una parola che viola una formula(regola?) è meno probabile ma non impossibile!

+Esempio:
![[Pasted image 20250714172049.png]]

Più alto il peso associato e più ho un mondo dove la regola è vera => il peso della regola è dato in base al numero di esempi che questa soddisfa.

+Notare che per le MLN, in maniera opposta a *ProbLog*(estensione di prolog con le probabilità), le costanti sono in maiuscolo e la variabili in minuscolo 

##### Applicazioni

- Inferenza
	Siccome ogni regola ha un peso, posso voler dedurre la probabilità che qualcosa di non noto sia vero. Non ho una certezza (come nella logica pura), ma una probabilità associata a un evento.
- Learning
	Se ho un dataset posso imparare i pesi. Più complesso è imparare le regole.
 
 Come visto in precedenza il processo di inferenza è fatto usando i pesi in modo probabilistico: ovvero dati un set di fatti conosciuti, le regole pesate sono usate per inferire il valore di verità di altre query (fatti)
	![[Pasted image 20250714173014.png]]

Il problema non è risolvibile in forma chiusa, dunque si usano algoritmi approssimati. Ad esempio si usa [MaxWalkSAT] (1996) => *stocastic local search*: minimizza la somma su clausole non soddisfatte.

Altro problema: abbiamo bisogno di fare il ground della knowledge base nei predicati(?) => spesso diventa pesante per requisiti di memoria e tempo(?) => si fa inferenza insieme sia sui pesi che le regole da una collezione di predicati osservati => Ground-Specific MLNs => estensione di MLN che inserisce reti neurali per calcolare i pesi => evito di dover calcolare le grounded rules!

+**ProbLog/DeepProbLog**:

- **ProbLog**: Estende Prolog con probabilità (es. `0.8::likes(X,M)`).
    
- **DeepProbLog**: Sostituisce probabilità con output di reti neurali. Non utilizzabile per fare classificazione
# Metodi spiegabili a posteriori

## Classificazione metodi

Esistono 3 tipologie di metodi per fare una spiegazione a posteriori di un qualsiasi modello **non interpretabile**, ad esempio reti neurali o altri sistemi complessi:
1. [Model Explanation] => spiegazione di tipo **globale**, si vuole trovare una spiegazione totale del modello nel suo complesso. 
2. [Outcome Explanation] => spiegazione **locale**, l'obiettivo è dare ==una spiegazione della singola istanza di test==. 
3. [Model Inspection] => spiegazione **ibrida**, si vuole fornire una spiegazione di alcune caratteristiche generali del modello, usando comunque tecniche locali, ad esempio importanza delle features.

In generali in tutti e tre i casi abbiamo in input:
- Una Black Box $b$
- Un Dataset $X$, oppure un singolo esempio $x$ del Dataset.

(1.) => In questo caso il problema consiste nel trovare una spiegazione $E \in \xi$, attraverso un ***predittore* globale interpretabile** $C_g$ tale che: $$C_g = f(b,X)$$In quel caso diremo che la spiegazione $E$ è ottenuta da $C_g$ se:
$$E=\xi_g(C_g,X)$$
=> $\xi_g$ è la nostra logica di explanation. 
In questo caso la nostra spiegazione dipende dal dominio scelto!

+Notare che trovare un modello interpretabile che spieghi totalmente la black-box addestrata su di un certo dataset non è la stessa cosa di addestrare una certa rete neurale => il nostro goal infatti è il perchè di quel modello non del dataset! 

Spesso può capitare che non ho il dataset di partenza con cui la rete è stata addestrata (Il dataset nostro di input non per forza corrisponde a quello con cui la rete è stata addestrata).
Le uniche cose che posso fare è quindi fare domande alla rete e vedere che risposte dà => cercando di "capire" le risposte del modello. Ottenuti classificatore e dati, cerco un meccanismo logico che mi porta ad una spiegazione. Ad esempio: se il nostro predittore $C_g$ è un albero di decisione => la spiegazione $\xi_g$ sarà estratta da un insieme di regole.

(2.) => Il problema consiste nel trovare **una spiegazione** $e \in \xi$ appartenente all'insieme di *domini iterpretabili*, tramite un ***predittore* locale interpretabile** $C_e$ tale che: $$C_l = f(b,x)$$
Diremo che una spiegazione $e$ è ottenuta da $C_l$ se: $$e=\xi_l(C_l,x)$$per una qualche logica di spiegazione $\xi_e$

=> Il clssificatore passa da globale a **locale** => imparo ogni volta un qualcosa che mi deve classificare un solo determinato esempio => abbasso di molto la complessità per l'*explanation*. 
=> Un esempio che segue questo ragionamento è il metodo dei prototipi visti per le [KNN] => sfrutto proprio i prototipi per fare *outcome explanation*!

(3.) Fare *model inspection* significa offrire all'utente una rappresentazione di alcune proprietà della black box => ovvero: $$r = f(b,X)$$
Rappresentazione di qualche proprietà di $b$ usando il processo $f$

### Tassonomia tecniche XAI

Le tecniche di XAI dipendono da:
- Il tipo del problema, ad esempio:
	- Regressione o classificazione
- Il tipo di modello per la spiegazione, ad esempio:
	- Albero di decisione
	- Logica 
	- Modello lineare
- Il tipo della black-box, se:
	- Agnostico => le mie tecniche di spiegazione sono valide per qualsiasi tipo di rete
	- Specifico
- Il tipo di dato:
	- Testo
	- Immagini
	- Tabulari

Fra i modelli per la spiegazione (*explanator*), troviamo:
- [Alberi di decisione]
- [Regole di decisione]
- [Importanza delle features] => misuro l'importanza delle features all'interno del mio sistema **black-box**, per fare predizione
- [Mappe di salienza]
- [Analisi di sensitività] => cambiando input, vedo quanto cambia output
- [Partial Dependecy plots] => come cambia l'uscita in funzione dei cambiamenti su una delle variabili  => grafici per fare spiegazione
- [Prototipi] => usare esempi analoghi per mostrare il perchè di una certa classificazione
- [Activation maximization] => Quali parti di una rete neurale si attivano di più in corrispondenza di certi input?

## Global Model Explanation

Preso un qualsiasi sistema *black-box* trovare un **sistema interpretabile** che approssima il sistema black-box non è molto semplice => questi algoritmi non vengono dunque usati moltissimo, a differenza di (2.) e (3.) => dove magari avere la risposta del perché di un caso specifico può essere molto di aiuto.

### Trepan (1996)

In questo caso:
- Si usa come *explanator* => gli alberi
- è specifico solo per i modelli fatti con le reti neurali(anche generalizzabili)
- I dati stanno in forma tabellare

L'idea dell'algoritmo è quindi:
- Sottoponi esempi di test alla rete neurale => costruisco così il mio dataset $(x_i, y_i)$ con rispettivamente l'esempio di test e il valore predetto dalla rete. => userò questo dataset per fare il training del mio modello. 
	=> notare, come fatto notare precedentemente, le $y_i$ non sono per forza le stesse che la rete ha preso in input, ma sono semplicemente quelle che manda in output.
- Identifica gli esempi rilevanti (i nostri prototipi), e dai a loro un importanza maggiore durante il training => ad esempio casi in cui cambia la funzione di decisione della rete => *relevant examples*
- Impara un albero sopra la rete => dunque con alta fede rispetto questo => *tree* con *high fidelity* => ovvero che le predizioni siano il più possibili vicine a quelle della rete

+Notare che l'idea di fare domande alla rete e ottenere un dataset per addestare un predittore globale $C_g$ è un idea generale e non solo usata in Trepan.

### PALM (2017)

Stavolta:
- oltre agli **alberi** come explanator **uso dei sottomodelli**
- Il modello ottenuto è **agnostico**
- é valido con qualsiasi tipo di dati

L'algoritmo si ispira al [K-means clustering]:
- All'inizio partiziono i dati i K gruppi
- Si imparano K *sotto-modelli* diversi (anche black-box) 
	=> con questi riclassifico i dati associandoli al **miglior** sotto-modello che li classifica meglio.
	=> A seconda di come sono stati classificati ricalcolo la partizione => se sono stati classificati correttamente li lascio dove sono, altrimenti rifaccio la partizione e rialleno i sotto-modelli.

L'interpretabilità stà nel come viene fatta la partizione => questa viene fatta a stile albero o lista di regole, ad esempio: "se x ha febbre > di ... e pressione > di ... => va nel sotto-problema X". Farò finire i miei esempi in una delle K categorie/modelli creati.
![[Pasted image 20250715165232.png]]
Questo è molto utile per *debuggare* delle classificazioni errate => riesco a risalire a quale sia il sotto-modello responsabile!

### LImiti delle spiegazioni globali

In generale per ottenere delle spiegazioni di tipo globale:
1. Fai domande alla *black box* per le predizioni
2. Addestra un predittore sul dataset da (1.)
3. Controlla che il modello imparato è allineato con la black box: $C_g \approx b$ 

Arriverò mai a perfetto allineamento?? Boh dipende spesso dai dati scelti => non posso avere grosse garanzie che il mio modello funzioni bene oltre ai dati scelti... che succede per i dati fuori dalla distribuzione??

I limiti delle spiegazioni globali sono quindi:
- Rischio di *approssimare e oversemplificare*
- Rimangono comunque difficili da interpretare(?) => avere un albero che approssima una rete neurale, può portare ad un albero troppo profondo e quindi di poca interpretabilità! 
- Infine c'è una forte dipendenza sui dati scelti.

## Outcome Explanations

Fra i modelli **locali** abbiamo:
- [Modelli locali surrogati]()
	=> Si cerca un modello interpretabile "nel vicinato" dell'istanza di test => trovo un insieme di vicini che mi motivano il fatto che quell'esempio sia valido in quell'intorno 
	=> Esempio di questo tipo è [LIME]
- [Feature Perturbation/removal]() 
	=> Vado a vedere che succede se cambio/rimovo una certa feature => se l'outcome cambia di molto la feature ha molta importanza
	=> Esempio di questo tipo è **PREDDIFF** => da cui si ricava [SHAP]
- [Mappe di Salienza]()
	=>Evidenzio le porzioni dell'input che sono più rilevanti per fare predizione => ad esempio quali pixel di un immagino oppure quali parole all'interno di una frase
	=> Esempi di questo tipo sono [CAM] oppure [GradCAM]
### LIME

["Why should I trust you? Explain the predictions of any classifier"](https://dl.acm.org/doi/10.1145/2939672.2939778)

**Local Interpretable Model-agnostic Explaination** (LIME) è una tecnica di local surrogate models del 2016 per l'[outcome explaination](regio/Explainability/Metodi.md#Outcam%20explaination) nel campo dell'[explainability](regio/Explainability/Explainability.md).
- Come *explanator* usa un modello interpretabile => Solitamente si usa un modello lineare.
- È model agnostic, cioè valido per tutti i tipi di black box.
- Va bene qualunque tipo di dato.
#### Idea

Supponiamo di avere una black box che produce una superficie di separazione molto complessa e non lineare.
Se voglio spiegare un'istanza posso creare un modello lineare ==che mi approssima la black box solo in un intorno di quella istanza.==

![[Pasted image 20250715181609.png]]

=> il modello lineare è il modello + semplice che approssima la black box!

È importante osservare che la *fidelity* del modello interpretabile è buona solo ==localmente al punto da spiegare==: un modello lineare approssima bene un modello complesso solo localmente.
Globalmente però la fidelity potrebbe essere, e solitamente lo è, anche pessima => global fideliy e local fidelty sono diverse fra loro!

=> Genero quindi i miei campioni tramite *perturbazione* nell'intorno dell'istanza di test (che vogliamo spiegare) => dati che saranno tutti vicini all'istanza di test
=> Addestro quindi un modello lineare, che è interpretabile e approssima bene la black-box nella località della predizione

La nostra funzione obiettivo sarà quindi: $$explanation(x)=\displaystyle\arg\min_{g\in G}L(f,g,\pi_x)+\Omega(g)$$
Dove:
- $x$ è la nostra istanza di test da spiegare
- $G$ è la famiglia di modelli interpretabili  (nel nostro caso modelli lineari, ma valido anche per altri modelli interpretabili)
- $L$ è la loss per la ***local fidelity*** => quanto approssimo bene la black-box (nell'intorno di x), dove:
	- $f$ è la black-box
	- $g$ è il nostro nuovo modello interpretabile
	- $\pi_x$ è detta *proximity function* => mi dà una misura della distanza
- $\Omega$ è il termini *regolarizzatore* sulla complessità di $g$ => serve per garantire interpretabilità di $g$
#### Ingredienti dell'algoritmo

LIME lavora in modo discreto: il modello lineare che spiega la black box viene addestrato su **features discrete**, in particolare binarie.

Gli ingredienti richiesti quindi sono:
1. Una *rappresentazione interpretabile* $x'\in\{0,1\}^{d'}$ definita a partire da $x$ in una dimensione $d'$.
	- Se $x\in \mathbb{R}^d$ è l'input da spiegare definito in uno spazio a $d$ dimensioni. Questa va portata ad uno spazio più piccolo di dimensione $d'$:
		- Ad esempio, sia $x$ una classica immagine di partenza con dimensione $W\times H\times 3$ (l'ultimo è per l'RGB) => Si genera una sua rappresentazione $x'$ costituita da **superpixel** a colore costante, cioè da gruppi di pixel dove all'interno il colore è lo stesso (cioè un solo canale e non più tre)
		=> In generale se più pixel condividono una particolare caratteristica => divido ad esempio l'immagine di partenza in regioni na seconda di certe caratteristiche presenti
		- Per i testi invece esistono spazi di parole fra loro vicine dal punto di vista semantico 
			=> *embeddings*: rappresentazioni di testo in uno spazio compatto  => molto più piccolo rispetto ad un vocabolario
		=> Questo permette di semplificare la rappresentazione e renderla più capibile.  Si va a guardare semplicemente se una determinata caratteristica è presente o meno nel mio esempio![[Pasted image 20250715185131.png]]
		- Oppure ad esempio, per dati tabulari la perturbazione consiste nel sostituire un valore 1 con uno 0.

2. Ci serve definire la proximity function $\pi_x$, per definire la distanza di un campione generato attorno l'input $x$ (*locality*):
	- Un esempio è definirla come una *distanza gaussiana* $$\pi_x(z)=exp(-D(x,z)^2/\sigma^2)$$dove $D$ può essere:
		- la [distanza del coseno] per i testi,
		- [L2] per le immagini 
	  e $\sigma$ è un iperparametro.

3.  La Loss di classificazione $L$, usata per addestrare $g$ e garantire *local fidelity* possiamo definirla come: $$L(f,g,\pi_x)=\displaystyle\sum_{z,z'\in Z}\pi_x(z)(f(z)-g(z'))^2$$dove:
	- $Z$ è il vicinato di $x$
	- $z$ è la rappresentazione originale di un valore campionato (ottenuto tramite perturbazione)
	- $z'$ la sua rappresentazione interpretabile.

	In pratica voglio minimizzare [l'errore quadratico] tra il valore predetto dalla black box sulla **rappresentazione originale** (chiedo alla black box di classificarmelo) e quello predetto dal modello interpretabile sulla **rappresentazione interpretabile** 
	=> Si pesa questo errore secondo la vicinanza con il punto da spiegare $x$:
	- Ovvero misuro la distanza fra x con z e x' con z'

4. $\Omega(g)$ è un regolarizzatore [lasso] che ==limita la complessità di $g$, cioè assicura che $g$ sia interpretabile.==
	È definita come: $$\Omega(g)=\infty\cdot\mathbb{1}[||W_g||_0>k]$$Il regolarizzatore da un contributo infinito se il **vettore dei pesi** $W_g$ del modello interpretabile non è **sparso** almeno quanto $k$, cioè se il numero di valori diversi da 0 è più di $k$. Il valore di $k$ è un iperparametro.
	Nella pratica è il numero di parole per il testo, di superpixel per immagini o il numero di features per dati tabulari => dunque voglio un modello lineare che usi al + K feature, se  ho K o più feature attive pagherò infinito! (zero altrimenti)
##### Pseudo codice - LIME algorithm

- Input:
	- La black box $f$.
	- Il numero $N$ di campioni nel vicinato.
	- L'istanza da spiegare $x$ e la sua versione interpretabile $x'$.
	- La funzione distanza $\pi_x$. (*proximiy*)
	- La **lunghezza della spiegazione** $k$.
	- Tecnica per passare da $z'$ a $z$.
- $Z\leftarrow\{\}$. 
- $for\ i\cdots,N:$ (ciclo che genera i campioni)
	- $z_i'\leftarrow samplearound(x')$ //effetto la perturbazione rimuovendo gli 1 dalla rappresentazione interpretabile
	- $Z\leftarrow Z\cup\{(z_i,z_i',\pi_x(z_i))\}$ //gli $z_i'$ sono le features mentre $f(z_i)$ i target
- $W \leftarrow K-lasso(Z,K)$ (addestramento del modello interpretabile)

Alla fine le **feature più importanti** nel modello semplice (es. i coefficienti della regressione) diventano la spiegazione per la previsione originale => come capisco quali sono le feature più importanti? quelle che uso per classificare l'esempio di partenza => cerco di ottenere similarità al target!
##### Costo

Usando l'hw dell'articolo (si parla di 10 anni fà) si ha un costo rispetto al tempo di:
- Con una *random forest* composta da 1000 alberi e $N=5000$ ci vogliono 3 secondi.
- Con una *inception network* e $N=5000$ ci vogliono 10 minuti.
=> risolvere anche un solo problema di explanaibility può essere costoso!
##### Submodular pick (SP-LIME)

Siccome il costo in tempo di LIME è comunque abbastanza alto, ci interessa trovare quegli esempi da spiegare che possono permettere ==all'utente di capire al meglio possibile la black box.== Anche se il numero di esempi lo scegliamo a priori e di queste ne vengono estratte per tutti le spiegazioni, possiamo decidere di mostrare all'utente solo una parte di questi => quelli che consideriamo più importanti, ovvero i più rappresentativi.

Leggersi infatti tutte le spiegazioni e poi valutarle ha comunque un determinato costo. L'algoritmo SP trova applicazione quando un utente ha un budget $B$ di tempo limitato per capire come funziona il modello black box.
##### Idea

Viene costruita una matrice dove sulle righe ho gli esempi che voglio spiegare e sulle colonne le features. 

![[SP LIME.png]]

Applicando LIME è come se evidenziasse per ogni esempio le celle relative alle features che sono state usate per spiegare quell'esempio. 
Quello che fa l'algoritmo è [massimizzare la coverege](regio/Explainability/File/SP%20LIME.png) delle features importanti sulla base degli esempi di test: in pratica calcoliamo la spiegazione per ogni esempio del test set e poi scegliamo quegli esempi che coprono tutte (**o la maggior parte**) delle features più importanti, cioè quelle maggiormente usate da tutti gli esempi. => è dunque un problema di ottimizzazione dove dato il budget si cerca di massimizzare la coverage delle feature che gli esempi coprono ma minimizzando questi ultimi, rientrando nel Budget di partenza.

### PredDiff 

Sempre un algoritmo di spiegazione locale => *outcome explanation* => ma collegato alla feature importance.

L'idea è quella di calcolare l'importanza di un attributo $A_i$ , per predizione di un determinato esempio $x$: $$\text{PredDiff}_i(x)= f(x) - f(x / A_i)$$
Ovvero tolgo all'istanza l'informazione di $A_i$ e nel calcolo la differenza.

Vorrei comunque che la $f$ rimanga la stessa => ma togliendo una feature rischio di dover riaddestrare la rete!

Potrei quindi pensare di quantificarlo come: $$\text{PredDiff}_i(x) = p(y=c |x) - p(y= c | x / A_i)$$ Come calcolo quindi l'altra quantità? (L'*infoDiff* si ottiene applicando i logaritmi alle prob)

Come posso simulare la rimozione di una feature?
=> Un idea potrebbe essere quella di simulare la rimozione con il contributo medio dei valori della feature. $$p(y | x / A_i) = \sum_{s=1}^{m_i} p (A_i=a_s) \times p(y| x \leftarrow A_i =a_s)$$ Dove:
- $m_i$ sono il numero di possibili valori di  $A_i$ nel training set
- Il secondo termine vado a guardare quando l'istanza di test abbia o meno per la colonna i-esima di A il valore di quella feature.

#### Pregi vs Difetti
- Il metodo è agnostico sul modello => positivo
- Ma non si considera l'interazione sulle feature => negativo
- Può capitare che la perturbazione delle features crei dati non realistici => in quanto considero appunto una feature alla volta e non insieme. => da qui i tentativi di miglioramento del metodo che hanno portato a *SHAP*

### SHAP

*Shapley Additive Explanation* 
=> "[A unified approach to interpreting model predictions](https://proceedings.neurips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf)"
#### Teoria dei giochi cooperativa

Skippo l'esempio del [dilemma del prigioniero](https://it.wikipedia.org/wiki/Dilemma_del_prigioniero)

Supponiamo di avere un insieme di giocatori $D = \{1,...,,d\}$ . Un **gioco** è dato specificando un valore per ogni possibile *coalizione* $S \subset D$ . Descrivo quindi una funzione caratteristica $v$ come: $$ v: 2^D \rightarrow \mathbb{R}$$ Che rappresenta il nostro *payoff*

Ad esempio, ho degli impiegati in azienda:
![[Pasted image 20250716180934.png]]
Mi chiedo quale potrebbe essere la combinazione di impiegati che mi porta ad un miglior profitto in azienda? 
=> Se dunque ho dei profitti come li ripartisco fra i giocatori/impiegati? => da qui vengono fuori gli [shapley values], derivati da un insieme di [assiomi di equità]

Prima però associo alle coalizioni il premio (funzione caratteristica):
- $v(D)$ => *grand coalition* => tutto l'insieme
- $v(\mathbb{0})$ => *null coalition*
- $v(S)$ => *arbitrat coalition* => una coalizione del insieme

Sia quindi $G$ l'insieme di tutti i giochi di $d$ giocatori, lo *shapley value* assegna un array di crediti (profitti) per ogni gioco => in $\mathbb{R}^d$ un credito per ogni giocatore: $$\phi: G \leftarrow \mathbb{R}^d$$ => nell'esempio i giochi sono tutte le coalizioni.

Per un gioco $v$, gli *shapley values* sono: $$\phi_1(v), ... , \phi_d(v)$$
##### Assiomi di equità

1. **Efficienza** => i crediti devono sommare al valore della *grande coalizione*: $$\sum_{i\in D} \phi_i (v) = v(D) - v(0)$$
2. **Simmetria** => se 2 giocatori sono interscambiabili ovvero: $$v(S \cup \{i\}) = v(S \cup \{j\}) \ \forall S \subset D$$ Allora vale: $$\phi_i(v) = \phi_j(v)$$
3. **Giocatore nullo** => se un giocatore non dà contributo allora ha "simmetria zero" $$v(S \cup \{i\}) = v(S) \ \forall S \subset D \Rightarrow \phi_i(v) = 0$$
4. **Linearità** => la distribuzione di crediti segue una legge lineare:$$\phi(c_1v_1 + c_2v_2) = c_1\phi(v_1) +c_2\phi(v_2)$$
Si può dimostrare che lo *shapley value* $\phi : G \rightarrow \mathbb{R}^d$ è l'unica funzione che soddisfa queste proprietà: $$\phi_j = \frac{1}{d} \sum_{S \subset D/j} \frac{1}{\binom{d-1}{|s|}} (v(S \cup \{i\}) - v(S))$$ Dove: 
- La somma è una media pesata sulle coalizioni
- Il peso è dato da 1 fratto tutti i modi di scegliere |s| giocatori da d-1 (j è escluso)
- Calcolo poi il contributo per aver aggiunto il giocatore $j$

Riformulando un po': $$\phi_j = \frac{1}{d} \sum_{S \subset D/j} \frac{|s|!(d-1-|s|)!}{(d-1)!} (v(S \cup \{i\}) - v(S))$$$$\phi_j =  \sum_{S \subset D/j} \frac{|s|!(d-1-|s|)!}{d!} (v(S \cup \{i\}) - v(S))$$
##### Esempio:
$d=3$ , giocatori{ 1,2,3}, come calcolo lo shapley value per il secondo giocatore?
=> quante coalizioni senza {2} ? => {0}, {1}, {3}, {1,3} => l'ordine conta! 
(guarda la formula sopra) 

![[Screenshot 2025-07-16 at 22.43.32.png]]
=> queste sono tutte le mie $\phi$ => le funzioni caratteristiche sono date in partenza.

#### Shapley Values per ML

Applicando la teoria di giochi al machine learning: 
- I nostri **players** equivalgono alle **features**
- il **profitto** sarà il *model behaviour* ovvero come risponde il modello tipo loss o accuracy; 
- gli shapley values servono a quantificare **l'impatto delle features**

Tramite gli shapley values, il metodo SHAP riesce quindi a spiegare l'uscita individuale (ma anche quella globale => sommando i vari contributi) usando un **additive feature attribution**.

Il modello risultante è dunque: $$f(\hat{x}) = \phi + \sum_{j=1}^d \phi_j \hat{x}_j'$$ Dove:
- $f$ è la solita black-box, da spiegare
- $\hat{x}$ è la istanza di test, mentre $\hat{x}'$ è la rappresentazione interpretabile (varia in base alla black box da spiegare), in particolare è il **vettore delle coalizioni** 
	![[Pasted image 20250716231527.png]]  => gli 1 sono i giocatori (features presenti nella coalizione)
- $\phi_0$ è valore iniziale ed è preso come il valore atteso dell'instanza di test => $E[f(x)]$ 

Gli shapley values spiegano quindi la differenza fra il valore predetto $f(\hat{x})$ e la "predizione media"
![[SHAP interpretazione.png]]
=> notare che posso anche avere dei contributi negativi!

##### Problemi

L'esatta computazione degli shapley values => necessita di enumerare **tutte le possibili combinazioni di features** per poter stimare il contributo di ognuna di esse. 
Questa porta ad una complessità di $2^d$ con d numero di feature =>  con $d = 20$ il problema non è fattibile!

Abbiamo dunque bisogno di metodi di approssimazione! 
=> si usa una procedura di sampling per le coalizioni => invece di enumerarle tutte alcune (o tutte?) le predico ?

Molti modi di implementare questo sono:
- Model Agnostic => [Kernel SHAP] (molto simile a LIME)
- Model Specific => [Tree SHAP] o [Deep SHAP]

##### Kernel SHAP

Tecnica per stimare i contributi delle feature per una predizione di $x$ come un approssimazione degli **shapley values esatti**.

Se su LIME avevo $$explanation(x)=\displaystyle\arg\min_{g\in G}L(f,g,\pi_x)+\Omega(g)$$
In questo caso pongo $\Omega(g) = 0$, la Loss rimane  $$L(f,g,\pi_x)=\displaystyle\sum_{z,z'\in Z}\pi_x(z)(f(z)-g(z'))^2$$Mentre la funzione di distanza diventa: $$\pi_x(z') = \frac{d-1}{\binom{d}{|z'|}|z'| (d-|z'|)} $$
=> Allora in questo caso, l'algoritmo di LIME trova come vettore di pesi $W$, un approx degli shapley values!
=> Shapley values che rispetto a lime non hanno l'ipotesi di una spiegazione breve/compatta a $K$ feature => non ho vincoli sul contributo delle feature!

###### Sketch algoritmo

1. Si campionano gli esempi => ovvero campiono le coalizioni $$ z_k' \in \{0,1\}^d \ k \in \{1, ..., N\}$$ dove N è il numero di campioni generati
	![[Pasted image 20250717153616.png]]
	
2.  Calcola $f$ per i campioni (nello spazio di partenza): $$h_x(z_k'):\{0,1\}^d \rightarrow \mathbb{R}^p$$ con $p$ il numero di feature nello spazio di partenza. (in linea di principio $d$ e $p$ sono uguali)
	=> trasformo in un vettore su cui posso calcolare la $f$
	La funzione $h_x$: 
	- Mappa gli "1" ai **valori originali** della feature $x$
	- Mappa gli "0" ad un valore random del training set => campiono dal training set i valori di un **esempio di training**, ottengo cosi (guarda esempio sopra):
	![[Pasted image 20250717154645.png]]
	Questo per dati tabulari... che succede per le immagini?![[Pasted image 20250717155215.png]] Una volta campionata la coalizione $z'_k$, la funzione $h$ seleziona le parti da tenere e quali da campionare => in quest'ultimo caso vado a generare tante immagini perturbate dove tolgo dei pesi. Da qui ne calcolo la $f$ e vado a capire le feature più importanti!
	
3. Si calcola il peso $\pi$ della coalizione come con la funzione di distanza vista prima:$$\pi_x(z') = \frac{d-1}{\binom{d}{|z'|}|z'| (d-|z'|)}$$ in particolare $|z'|$ mi restituisce il numero di elementi non a zero a in $z'$ 

4. Si *fitta* tramite un modello lineare pesato:$$L(f,g,\pi_x)=\displaystyle\sum_{z,z'\in Z}\pi_x(z)(f(z)-g(z'))^2$$ e come visto primo ho un analogia a LIME se non che pongo $\Omega(g)=0$  => ovvero non pongo nessun limite sul numero di feature $K$ usate nelle spiegazioni

5. Ritorno i coefficienti del modello lineare appreso ==come un approx degli shapley values== $\phi$ => la j-esima componente nel modello lineare è lo shapley value della j-esima feature $\phi_j$ 
	=> Si può ottenere una misura globale dell'importanza delle feature come media del valore assoluto degli shapley values su tutti i dati: $$ I_j = \frac{1}{n} \sum_{i=1}^n |\phi_j^{(i)}|$$ vengono presi anche gli shapley values negativi ma messi in valore assoluto

#### Additive feature attributions

Esistono 3 proprietà equivalenti agli assiomi di equità, validi sugli shapley values:
1. Accuratezza locale
2. *Missingness*
3. Consistenza

La proprietà (1.) ci dice che $g$ modello di spiegazione locale => approssima $f$ localmente: $$f(x) = g(z') = \phi_0 + \sum_{i=1}^d\phi_i z_i'$$
La proprietà (2.): se una feature è mancante =>  $z_i' = 0$ , siccome il suo contributo è zero => $\phi_i=0$ allora non ha impatto!

La proprietà (3.) ci dice che comunque scelti due modelli $f_1$ e $f_2$ se il contributo di una feature in $f_1$ è più grande che in $f_2$ allora: $$\phi_j(f_1,x) \geq \phi_j(f_2,x)$$
ovvero: $$f_1(x)-f_1(x/j) \geq f_2(x) - f_2(x/j)$$
=> Anche qui gli shapley values sono le uniche funzioni a soddisfare (1.)-(2.)-(3.). Sono valide anche per lime solo se $\Omega(g) = 0$ e $\pi$ è scelto come in SHAP => con il coeff. binomiale.

### Metodi Basati sul gradiente

Si vuole fare spiegazioni locali per reti profonde. L'idea è quella di usare l'informazioni che ci dà il gradiente rispetto all'input iniziale => per capire quali sono le feature più significativi per quella uscita.

I diversi approcci si basano sui modi in cui viene calcolato il gradiente. In questi casi la nostra spiegazione sarà grande quanto l'input, se ad esempio ho in input un immagine => posso ottenere una mappa che associa ad ogni singolo pixel un determinato peso di importanza. 

![[Pasted image 20250717171329.png]]

Questo è esattamente quello che si chiama [mappa di salienza] => ovvero un immagine con stessa dimensione dell'immagine di input dove ogni pixel ha colore per ogni livello di explanation. 

Messe poi una sopra l'altra i pixel più colorati sono quelli con maggiore importanza per la spiegazione => *mappe di aggregazione*. Metodi che si prestano bene per dati con una certa sequenzialità di parole o pixel. 
Analizzando come i cambiamenti sull'input hanno un impatto sulla rete.

#### Vanilla gradient

Preso $F_c(x)$ ovvero l'output di un rete neurale per una classe c, consideriamo l'approssimazione al primo ordine di taylor $F_c(x) \approx wx+b$ , dove il peso $w$ vale: $$w = \frac{\delta F_c(x)}{\delta x}|_{x_0}$$Calcolata nel punto (o il pixel) $x_0$ che ci interessa.

**Gradienti grandi** indicano che piccoli cambiamenti in quelle zone (features), ovvero piccoli cambiamenti nell'input, corrispondono a **grandi cambiamenti nell'output**.

I gradienti ci dicono quali feature hanno la più ripida direzione locale, relativa alla predizione del modello => in un dato punto lungo la funzione di predizione ho la direzione di cambiamento più grande

#### Mappe di Salienza

Presa una immagine di input $I_0 \in \mathbb{R}^{W\times H \times K}$ , dove $K$ corrisponde al numero di canali => 3 per Immagini RGB 
=> si passa alle mappe di salienza di dimensione $$M \in \mathbb{R}^{W\times H}$$ dove: $$M_{ij} = max| W_{ijk}|$$
=> si effettua un operazione di [pooling] => dove si riduce lo spazio delle feature.

Effettuo un operazione di *feature maps* => guardo nel'intorno di pixel e faccio un operazione di aggregazione => tramite max/avg e mediamente mi basta che sia estratta la feature di interesse.

Un modo di ottenere le mappe di salienza è quindi tramite *vanilla grad*, mappe però che risultano essere molto **rumorose**... si studiano quindi modi per ridurre il rumore sulle mappe di salienza: 
- [Smooth-grad]
- [GradCAM] e le varie versioni come [Guided GradCAM]

##### Smooth-grad

"Si aggiunge rumore per rimuovere rumore" => aggiungo rumore su diverse copie dell'input iniziale.
Fatto quindi vanilla grad, della mappa di salienza ottenuta ne faccio la media, aggiungendo ad ogni copia della varianza/rumore => ottengo così delle immagini che non cambiano di molto ma hanno comunque impatto sull'output:$$W = \frac{1}{N} \sum_{i=1}^N \nabla_x F_c(x+\epsilon)$$con $\epsilon$ il rumore aggiunto, che insieme a $N$ costituiscono gli iperparametri del modello

##### GradCAM 

*Gradient - Class Activation Mapping*

![[Pasted image 20250717182805.png]]

Presa la solita immagine di input, eseguo $n$ volte delle [convoluzioni] => segue un operazione di [pooling] => che insieme ad altre operazioni di convoluzione porta ad una rete *fully connected* [MLP] (Multi layer perceptron => rete fully connected con funzioni di attivazioni non lineari)  => e quindi l'output finale.

GradCAM invece si ferma prima di eseguire lo step della rete fully connected.

Da un immagine di input $I_0$ => se la dò in pasto ad una [CNN] => questa produce mappe in uscita di dimensione $P\times Q$ dove $P << W$ e $Q<<H$ 

![[Pasted image 20250717183731.png]]

Si hanno delle misure di gradiente + grossolane => ma anche più robuste in quanto + aggregate => ci si ferma infatti all'ultima uscita del filtro convoluziona => ovvero non si fa backpropagation fino all'input, ma ci si ferma all'output dell'ultimo layer convoluzionale.

###### Algoritmo

Riassumendo quanto abbiamo detto: Gradcam calcola i gradienti indietro fino all'input/pixel ma fino all'output dell'ultimo layer della rete convoluzionale.

$K$ è il nostro iperparametro della architettura della rete => ovvero serve a scegliere il numero di mappe all'ultimo layer convoluzionale. In particolare ciascun $K$ è fatta nel seguente modo: 
![[Pasted image 20250718153919.png]]

=> GradCAM calcola per ogni *superpixel* (ovvero un insieme di pixel dell'immagine originale) la quantità:$$\frac{\delta F_c}{\delta A_{ij}^h}$$ ovvero deriva l'input di partenza secondo il singolo elemento h-esimo della *feature map*
![[Pasted image 20250718154207.png]]

Ottengo quindi la mia mappa di salienza come: $$S_{\text{Gradcam}}^C = ReLU(\sum_h \alpha_h^CA^h) \ (*)$$ con $\alpha_h^C$ i parametri calcolati da GradCAM

I passi da seguire, per calcolare i parametri, sono dunque:
1. Dò in input alla rete l'immagine da calcolare => forward pass
2. Prendo l'uscita della classe C (prima di calcolare il [softmax](https://www.google.com/search?q=softmax&oq=softmax&gs_lcrp=EgZjaHJvbWUyDggAEEUYJxg5GIAEGIoFMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMjU4N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8)) => $y^C$
3. Imposto gli score delle altre classi a zero
4. Faccio backpropagation fino all'ultmo layer convoluzionale $\frac{\delta y^C}{\delta A_{ij}^h}$
5. Calcolo l'importance di una feature map $A^h$ per la classe C come:$$\alpha_h^C = \frac{1}{Z} \sum_{u,v}\frac{\delta y^C}{\delta A_{uv}^h}$$ovvero la ottengo come media fra tutti i superpixel ($Z \in [0,1]$ è un fattore di normalizzazione)
6. Trovo la mappa di salienza $S$ con la formula vista prima (*)

+Notare che in realtà la mappa di salienza ottenuta in questo modo non ha stesse dimensioni dell'immagine di partenza => si esegue quindi un [upsample](https://www.google.com/search?q=upsample+immagini&sca_esv=b3f6a4e4ace9f962&sxsrf=AE3TifN0QjPmu7hBbsEaOz3DcnXdjjIuDQ%3A1752847484030&ei=fFR6aObLAd3r7_UPpOjdwAY&ved=0ahUKEwjm-YXdycaOAxXd9bsIHSR0F2gQ4dUDCBA&uact=5&oq=upsample+immagini&gs_lp=Egxnd3Mtd2l6LXNlcnAiEXVwc2FtcGxlIGltbWFnaW5pMgUQIRigATIFECEYoAEyBRAhGKABSIwLUL0BWJoJcAF4AZABAJgBlQGgAboIqgEDMC45uAEDyAEA-AEBmAIKoAKiC8ICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIFEAAYgATCAggQABiABBjLAcICBhAAGBYYHsICCRAAGIAEGBMYDcICCBAAGBMYDRgemAMAiAYBkAYKkgcEMC4xMKAH0imyBwMwLjm4B7kKwgcHMy01LjMuMsgHjwI&sclient=gws-wiz-serp) => dove si allarga alle dimensioni dell'immagine di partenza.

##### Guided GradCAM

L'idea è di combinare le spiegazioni ottenute da GradCAM più grossolane, con quelle ottenute a livello di pixel da un metodo tipo Vanilla Grad.
La mappa di salienza ottenuta è quindi: $$S_{ggc} = upsample(S_{GC}) \ (*) \ S_{VG}$$ ovvero si fa una moltiplicazione elemento per elemento fra le mappe di salienza ottenute da **GradCAM** e **Vanilla Grad**

##### Sanity Checks for saliency maps

Vengono proprosti 2 test sperimentali per **valutare** la bontà delle mappe di salienza:

1. Si compara una mappa di salienza di una rete addestrata su un qualche dataset/task con una rete inizializzata in modo random => Se non vedo differenze la mappa differenza non può essere una buona spiegazione **di quel modello**
2. Comparo una mappa di salienza sempre di una rete addestrata su un certo dataset/task ma con una rete addestrata sulle stesse immagini di input con le *labels* permutate in modo randomico => Se stavolta non vedo nessuna differenza la mappa di salienza non può essere una buona spiegazione **di quel particolare dataset**

=> Fra i vari test si nota che vanilla, smoothgrad e gradCAM passano i test mentre guided gradCAM no
=> inoltre non possiamo estendere il risultato del test da un dataset al caso generale => potremmo comunque dire che i metodi basati sul gradiente forniscono una buona spiegazione del modello se passano questi test => quantificare quanto buona sia questa spiegazione è un altro problema!

### Attention

["Attention is all you need"](https://arxiv.org/abs/1706.03762)
https://arxiv.org/abs/1706.03762

L'attention è un layer speciale delle reti neurali => usato spesso nel caso di sequenze come parole in una frase o *patches* in un immagine.

=> nato per reti ricorrenti tipo task di traduzione di testi => compara porzioni dell'input.

Si può interpretare l'attention come una sorta di spiegazione intrinseca del modello? => L'attention vorrebbe in qualche modo replicare quello che fa l'attenzione umana, ovvero pongo l'attenzione su parti di un testo/immagini => pesi dell'attenzione sono pesi associati a delle porzioni dell'input => utile quindi non solo alla classificazione ma anche alla spiegazione!

Ad esempio:
![[Pasted image 20250718164556.png]]
=> dò maggiore peso alle parole che più mi influenzano la mia decisione

Oppure per le immagini:
![[Pasted image 20250718164738.png]]

Oppure ancora per una traduzione:
![[Pasted image 20250718164813.png]]
=> le frecce rappresentano l'attention => *processo selettivo* per trovare le parti che servono ad un task a compiere una determinata azione => con l'obiettivo di dare un peso ad ogni parte.

#### Algoritmo

Più formalmente, faccio ***mapping*** fra query $Q$ e chiave $K$ per calcolare degli score di **similarità** => score che sono dati in pasto ad una *softmax* (normalizzatore) produrre un **insieme di pesi di attention**:![[Pasted image 20250718165653.png]]
=> l'exp mi aiuta a dare una spinta in più a quelli più probabili

Supponiamo quindi di avere un insieme di chiavi $\alpha$, a cui sono associate dei valori => tipo una memoria con coppie chiavi valori. 
Il meccanismo dell'attention segue i seguenti passi:
	=> prende la query e attraverso una qualche **funzione di attention** $f_{att}$ => genera uno **score di similarità** fra la chiave $K_i$ e la query $q$.
	=> Punteggio di similarità che viene normalizzato tramite una funzione di *softmax* => producendo il valore di **peso di attention** $\alpha_i$, 
	=> Peso  che viene moltiplicato per il rispettivo valore associato alla chiave $v_i$ producendo il **context vector** => vettore che nel valutare il mio contesto, pesa ciascun valore del mio set di chiavi.	
	![[Screenshot 2025-07-19 at 17.20.05.png]]

+Esempio (nel caso di *self attention* => chiavi e valori coincidono)

![[Pasted image 20250719172158.png]]
Le chiavi saranno tutte le parole della frase. Dunque una volta presa la *rappresentazione vettoriale* (tramite ad esempio [embedding](https://aws.amazon.com/it/what-is/embeddings-in-machine-learning/#:~:text=Gli%20embedding%20sono%20rappresentazioni%20numeriche,lo%20fanno%20gli%20esseri%20umani.)) per ogni parola, pongo in queste rappresentazioni in "memoria" => e calcolo tramite la funzione di attention i miei pesi di attenzione (*attention weights*) $\alpha_i$     ![[Pasted image 20250719172924.png]]  => pesi con cui mi costruisco il *context vector* (come somma pesata di tutte le parole)![[Pasted image 20250719173148.png]] 
In questo caso per la parola "book"

Rimane da capire come calcolare lo score di similarità:
- **Additive**: $$\alpha = softmax(w_3^T tanh(w_1K+w_2Q)$$ dove $w_1, w_2, w_3$ sono i parametri che si possono allenare => per modulare misura similarità
- **Dot-product**:$$$\alpha = softmax(\frac{KQ}{\sqrt{m}})$$ dove $m$ è il size dell'insieme delle chiavi.
- In generale: $$\alpha_i = \frac{exp(f_{att}(K_i,q))}{\sum_j exp(f_{att}(K_j,q))}$$
=> l'idea generale è che il peso deve essere maggiore a quei valori con le chiavi più simili alla query.

#### L'attention come explanation

Visto il suo algoritmo vien da chiedersi => "is attention explanation?"
Ovvero possiamo interpretare gli *attention weights* come un elemento che porta a spiegazioni?

Visto l'uso della rete di attention => usata nella maggior parte delle reti neurali odierne come negli [LLM](https://www.hpe.com/it/it/what-is/large-language-model.html#:~:text=Un%20Large%20Language%20Model%20(LLM)%20è%20una%20tecnologia%20AI%20avanzata,le%20complessità%20del%20linguaggio%20naturale.), [CNN](https://www.ibm.com/it-it/think/topics/convolutional-neural-networks) e [Transformers](https://aws.amazon.com/it/what-is/transformers-in-artificial-intelligence/), se fosse interpretabile sarebbe una notizia positiva!

Andando però a guardare come sono nate => ovvero come upgrade per le reti ricorrenti => non vi era alcun obiettivo di explanaibility!

Sono dunque stati proposti due lavori al riguardo:
- [Attention in not explanation](https://arxiv.org/abs/1902.10186)
- [Attention is not not explanation](https://arxiv.org/abs/1908.04626)

Nel primo articolo vengono fatti 2 esperimenti:
1. Misurano quanto gli attention weights correlano con altre tecniche di **feature importance** 
2. Provano a fare un *shuffling* randomico dei pesi per vedere quanto cambia l'output, usando anche *adversarial shuffling* => modifico pesi come se fosse fatto intenzionalmente ovvero dò più importanza a ciò che non lo dovrebbe avere

=> in entrambi i casi i risultati non sono un granchè... nel primo caso infatti ho una correlazione bassa e nell'altro caso l'uscita non cambia significativamente => layer di attenzione non fornisce spiegazione!

+Nel secondo articolo invece si riguardano i test e si cerca di spiegare i motivi per cui non abbia potuto funzionare:
	=> Come prima obiezione mostrano che la correlazione può essere bassa anche per altri metodi di feature importance (non solo per attention)
	=> Nel secondo caso invece parlano di spiegazioni *fedeli* e *plausibili*:
		- Con **fedeli** si intende che le spiegazioni motivano il comportamento **reale** della black box
		- Mentre le **plausibili** sono convincenti per l'utente
	=> Se dunque la spiegazione fedele è unica, a questa possono corrispondere più spiegazioni plausibili => le quali sono + semplici, meno specifiche ma comunque convincenti
	=> La spiegazione fornita dalla rete di attention può essere una spiegazione plausibile, mentre nel primo articolo gli esperimenti consideravano solo quelle fedeli!

+Notare che nemmeno LIME spesso è in grado di fornire spiegazioni fedeli => si spera appunto che valga il principio di località e che il numero $K$ di iperparametri coincida con il numero di features della black box...

+Il dibattito va dunque avanti => alcuni lavori fanno vedere di esempi di correlazioni fra parole non molto buone per le spiegazioni...
## Model Inspection

Tecnica di explanability che forniscono spiegazioni non globali, ma che danno caratteristiche globali della black box. 
I metodi che vedremo sono simili a quelli per fare *data visualization*. Sono 3 famiglie di plot che si definiscono in maniera "uno a partire dall'altro"
### Ceteris Paribus Plots

Dal latino: "a parità di tutto il resto" => "a parità di tutte le condizioni".
è una tecnica model agnostic ma locale.

L'idea: parte da una solita istanza di test => scelgo una feature di cui vogliamo fare il plot => a questa gli diamo tutto il range dei possibili valori => dal minimo al massimo di tutta la griglia di valori => e guardo il risultato dell'output della block box per ogni valore 
=> tipo "per un passeggero del titanic" => "se avesse avuto 5 anni" => poi "se avesse avuto 10" e cosi via... => "si sarebbe salvato?"

Si costruisce un plot per ogni feature dato un esempio di test => in sequenza:
- Si fa una perturbazione del valore di una feature
- Provo una griglia di possibili valori
- Dò in pasto il campione modificato alla black box
- Disegno il grafico

Abbiamo quindi due casi a seconda dei valori assunti dalla feature:
1. Se la feature è **continua**:
	=> Dato un punto $\hat{x}$ da spiegare e una feature $j$ da usare
	=> Creo una griglia di valori $z_1, ... , z_k$ (con $k$ iperparametro), dove tipicamente:
	- $z_1 = min(x_j)$ e $z_k = max(x_j)$ del training set 
	=> Per ogni $z_i$:
		=> Creo un nuovo punto (*data point*) $x' = \hat{x}_{x_j = z_i}$ => rischio però di creare casi molto *spuri* non correlati molto con gli altri => occhio a prendere valori estremi => posso avere dei picchi sul grafico!
		=> Calcolo $f(x')$
		=> Disegno il punto $(z_i, f(x'))$
	=> Disegno anche i punti originali!
	
![[Ceteris paribus Plot.png]]
=> Si possono notare alcuni punti dai quali in poi non cambiano i valori dell'output

2. Se la feature è **categorica** (discreta):
	 => Vale la stessa cosa di prima ma stavolta disegneremo un barplot 
	 ![[Pasted image 20250719130149.png]]

Lo svantaggio come detto prima è che le perturbazioni possono generare campioni non realistici!

Riaussumendo: Ceteris Paribus Plots come un plot per ogni feature e per ogni punto di esempio => con l'obiettivo di mostrare come cambia il target del nostro classificatore se cambiamo il valore di quella feature nel singolo esempio.

### Individual Conditional Expectation (ICE)

Si riprendono tutti i plot di Ceteris paribus plots, ma stavolta ==tutti insieme== nello stesso plot!
![[Pasted image 20250719191448.png]]
=> grafici che si accavallano fra di loro => difficili da leggere, ma danno comunque idea del trend

Per migliorare la leggibilità, possiamo far partire tutti gli *ice plots* da uno stesso punto (ovvero zero) => sottraendo il delta rispetto al valore che la feature prende a $x_{min}$ ![[Pasted image 20250719192027.png]]
Questo secondo plot è detto ***centered-ice***, ed è ottenuto appunto togliendo ad ogni feature j-esima nel punto $x_{min}$ la differenza fra il target e il valore del target quando la feature j-esima ha valore $x_{min}$: $$C-ICE_j(\hat{x}) = ICE_j(\hat{x})-f(\hat{x}_{x_j = x_{min}})$$
### Partial Dependence Plot (PDP)

Sempre a partire dai ceteris paribus plots, ne faccio la media => ovvero faccio la media degli ICE plots di solito non risulta centrato...

+é possibile analizzare in questo caso coppie di variabili di features => in quel caso si usano visualizzano delle [heatmaps] 

+Libreria DALEX(?)

### Permutation Feature Importance

Provo a misurare l'importanza delle feature facendo ==una permutazione dei valori== della feature (in tutti gli esempi del test set) stessa ma senza riaddestrare il modello. L'obiettivo è spiegare delle caratteristiche del modello dunque è anche questa è una tecnica di *model inspection* 

Data una black box $f$ e un test set $X$, calcolo l'importanza di ogni feature j-esima, permutando i valori nella colonna $X_j$
![[Pasted image 20250719194713.png]] 
=> Guardo che succede cambiando i valori nella colonna scelta. In particolare mi calcolo:
- Un errore originale (nel test set di partenza): $$Error_{origin}= \frac{1}{N_{test}}\sum_iL(y_i, f(x_i))$$
- Un errore dopo la permutazione: $$Error_{Perm(j)}= \frac{1}{N_{test}}\sum_iL(y_i, f(x_i^{P_j}))$$
Ottengo quindi la mia **feature importance** come rapporto fra i due errori: $$FeatureImp(j) = \frac{Error_{orig}}{Error_{Perm(j)}}$$Se dunque variando i valori di una feature si nota un grosso impatto => le performance cambiano considerevolmente!

#### Ground-Wise permutation

+Bisogna comunque stare attenti (come già visto) a non creare esempi troppo discordanti da quelli di partenza => posso quindi fare la permutazione della feature j-esima solo all'interno di un gruppo di esempi => ad esempio un gruppo di esempi comuni
![[Pasted image 20250719200347.png]] 
Ad esempio dopo aver diviso in gruppi di esempi => ne considero solo un gruppo.

## Concept-Based models

In generale sono tecniche che cercano di ottenere spiegazioni **in termini di concetti** che si attivano durante il processo decisionale.
Solitamente è una tecnica usata per le reti neurali.
### Concept bottleneck model

![[Concept bottleneck model.png]]

È un modello strutturato con più layer:
- Concept encoder $g$
	Solitamente è una CNN che prende l'input e produce un **vettore di concetti**.
- Linear layer $f$
	Prende la lista di concetti ed esegue la **classificazione** vera e propria. Deve essere semplice: un MLP o meglio anche un semplice layer lineare; se è troppo complesso il modello diventa non spiegabile. => classificatore è una funziona composta! $f(g(x))$
	
![[Screenshot 2025-07-19 at 20.28.52.png]]
#### Esempio

Se ho un'immagine di una mela, vorrei che la CNN mi restituisca un vettore di informazioni legate ad essa: rosso si, tondo si, quadrato no, blu no, e così via. A questo punto la mia spiegazione è il vettore dei concetti.
#### Osservazioni

- La lista di concetti è definita in fase di progettazione e i concetti devono essere [supervisionati] (ovvero dati di input e output abbinati etichettati => molto oneroso!). Ci deve essere quindi un train set di dati annotati con il vettore dei concetti, cioè dove l'etichetta non è la classe ma il vettore. => vettore dei concetti risultante deve essere più possibili elaborato!
- La spiegazione, supponendo la semplicità del layer lineare, deriva dal vettore dei concetti che viene associato all'input.

#### Learning

Vediamo come si addestra il modello.
##### Independent

Il concept encoder $g$ e il layer lineare $f$ sono addestrati indipendentemente (eventualmente anche in parallelo):
- Si addestra il concept encoder $g$ con i concetti come target. Si tratta di una classificazione multilabel, cioè dove si possono attivare più concetti.
- Si addestra il layer lineare $f$ dandogli in input i **concetti veri**, cioè un vettore binario. In pratica l'input dell'addestramento di $f$ ==è il target dell'addestramento di $g$.== (e non quello che ho in output da $g$)
##### Sequential

Il concept encoder e il layer lineare $f$ sono addestrati in **modo sequenziale**:
- Si addestra prima il concept layer $g$. Solo dopo aver finito di addestrare $g$ si passano i concetti predetti come addestramento di $f$. 
- Gli input dell'addestramento del layer lineare $f$ derivano dall'output di $g$ => non posso addestrare la $f$ prima di aver finito di addestrare $g$
##### Joint

Si tratta il modello come fosse **un singolo layer**, incapsulando l'obiettivo nella loss: $$L=L_{target}+\lambda(L_{concept})$$ dove:
- $L_{target}$ è la classica **loss sull'output** (i.e. la classificazione finale), cioè $L_{target}(y_i,f(g(x_i)))$.
- $L_{concept}$ è la loss sui concetti, cioè $L_{concept}(c_i,(g(x_i))$, dove $c_i$ sono i concetti.
##### Conseguenze

![[Pasted image 20250719204018.png]]
- Per la versione join se si usa un $\lambda$ piccolo, allora potrei avere più errori sui concetti, cioè sulle spiegazioni; quando $\lambda$ cresce invece potrei avere più errori sulla classificazione finale.
- Solitamente i primi due metodi tendono a imparare meglio i concetti, cioè la spiegazione. 

Questi portano ad avere un po' di **errore sulla classificazione** => questo perché meno concept error si e più si ha libertà nella scelta dei concetti da mantenere per fare classificazione!   (problema di allineamento? da capire); tale errore diminuisce sempre più quanto il *dizionario dei concetti* è grande, in quanto aggiungo concetti aggiuntivi per coprire più variabilità nei dati.  (cioè diminuisce se i concetti legati all'input non semplifica troppo l'input stesso (?))