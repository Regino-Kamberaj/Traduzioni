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
# Valutazione regole
La bontà di una decision rule si può valutare sulla base di due misure:
- Supporto/copertura (coverage)
	È la percentuale di esempi per cui è vero l'antecedente. Non stiamo verificando che la predizione sia buona.
- Accuratezza (confidence)
	È la percentuale di esempi coperti dalla regola (samples per cui vale l'antecedente) che sono classificati correttamente.
##### Compromesso
Si può dimostrare che se il supporto diminuisce allora si può far crescere l'accuratezza e se l'accuratezza diminuisce si può far crescere il supporto.
Intuitivamente una regola può essere molto precisa (molte espressioni booleane in AND) e quindi comprire pochi sample; per una regola di questo tipo però mi aspetto che la percentuale di samples classificati correttamente sia massima.
Ragionamento opposto invece per una regola generale e corta.
# Combinazione regole
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
# Apprendimento
Per imparare le regole ci sono varie strategie.
### Sequenzial covering
Questo tipo di algoritmo è un algoritmo greedy (come quelli basati sui [decision tree](Decision%20tree.md)). Intuitivamente l'algoritmo:
- Inizializza una lista di regole $ruleList$ vuota.
- Impara una regola $r_j$ da $D$.
- Finché il criterio di arresto non è soddisfatto:
	- Aggiungo $r_j$ a $ruleList$.
	- Rimuovo i sample coperti da $r_j$ da $D$.
	- Apprendo un'altra regola $r_j$ da $D$.
- Si restituisce $ruleList$.
##### Imparare regole
Tipicamente per apprendere una regola si apprende un [albero di decisione](Decision%20tree.md) (e.g., con l'algoritmo cart che è veloce) e poi si estrae la regola definita dal percorso che comprende per ogni livello il nodo più puro (secondo la definizione del [gini index](Decision%20tree.md#Score/Metriche)).
##### Criterio di arresto
Possiamo considerare due criteri di arresto:
- Le nuove regole non sono regole buone, cioè i nodi generati dall'albero di decisione non sono molto puri.
- Sono rimasti pochi samples da coprire.
##### Combinazione di regole
L'implementazione, usata soprattutto durante l'inferenza, segue la struttura delle decision list.
Questo è necessario in quanto l'algoritmo è greedy: le regole imparate potrebbero sovrapporsi e tramite la lista prendiamo solo la prima regola il cui antecedente è verificato.
### Bayesian/scalable rule list
È una tecnica che usa delle decision list e un approccio bayesiano, cioè usa una conoscenza a priori per determinare le miglior lista tra quelle possibili.
L'algoritmo ad alto livello si articola in:
- Generare una lista di regole iniziale.
	Questa generazione avviene campionando su una distribuzione a priori, costruita con l'obiettivo di generare poche regole e corte; il numero e la lunghezza delle regole sono gli iperparametri della distribuzione.
- Si modifica la lista aggiungendo, rimuovendo o modificando regole della lista.
- Si sceglie la migliore lista secondo la postirior probability distribuzion ottenuta tramite la regola di bayes.
##### Posterior
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