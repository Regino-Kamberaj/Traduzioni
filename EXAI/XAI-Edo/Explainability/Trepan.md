È una tecnica del 1996 di [Global model explanation](regio/Explainability/Metodi.md#Global%20model%20explanation) per il campo dell'[Explainability](regio/Explainability/Explainability.md).
# Caratteristiche
- Come explanator usa un albero.
- È pensato per black box che sono reti neurali, ma si può anche genaralizzare.
- È pensato per dati tabulari.
# Algortimo
- Si sottopone alla rete delle query su dei test samples.
- Tramite queste query riesco a costruire un dataset $(x_i, y_i)$, dove $x_i$ è un test sample e $y_i$ è il valore predetto dalla black box. Osserviamo che le varie $y_i$ potrebbero essere anche sbagliate: sono quelle predette.
- Si identificano degli esempi rilevanti (chiamati prototipi) e gli diamo più importanza durante il training dell'albero.
- Si addestra un albero sul dataset trovato in modo che abbia un'alta fidelity rispetto alla rete (cioè le predizioni devono essere il più simile possibile) e che utilizzi i pesi associati ai dati del dataset prodotto.