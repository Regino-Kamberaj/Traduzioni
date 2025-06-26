Sono modelli [interpretabili](regio/Interpretability/Interpretability.md) che, rispetto ai [rule-based system](regio/Interpretability/Rule-based%20system.md), vogliono aggiungere la non linearità.
##### Idea
L'idea alla base di rule fit è mappare lo spazio delle features tramite delle regole; in pratica l'antecedente (insieme di condizioni sulle features originali messe in AND) di una regola diventa la nuova features. In questo modo il modello diventa non lineare nello spazio delle features originale, ma lineare nel nuovo spazio.
# Algoritmo
L'algoritmo rule fit aggiunge un termine alla classica [funzione lineare](regio/Interpretability/Interpretability.md#Modelli%20lineari) e quindi l'output viene calcolato come $f(x)=\beta_0+\sum_{i=0}^P\beta_ix_i+\sum_{j=1}^R\alpha_jr_j$, dove $r_j$ è la $j$-esima regola e $\alpha_j$ è il peso corrispondente.
##### Apprendimento regole
Per apprendere le regole fit rule utilizza un metodo ensamble, come può essere una random forest o un gradient boosting (comunque deve essere un insieme di alberi).
##### Loss
Per imparare $\alpha$ e $\beta$ della funzione che poi genera l'output usiamo
$\alpha^*,\beta^*=\displaystyle\arg\min_{\alpha,\beta}\sum_{i=1}^nL(y_i,f(x_i))+\lambda(\sum_{i=1}^P|\beta_i|+\sum_{j=1}^R|\alpha_j|)$, dove l'iperparametro $\lambda$ (lasso regularizer), gestisce la sparsità della soluzione, cioè la quantità di regole che vogliamo: un valore alto indica poche regole.
Questo ha senso perché vogliamo che il nostro output, cioè $f(x)$, sia determinato da poche regole, in modo che sia più interpretabile; se avessimo infatti una soluzione con molto regole allora il modello sarebbe poco interpretabile.
# Librerie
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