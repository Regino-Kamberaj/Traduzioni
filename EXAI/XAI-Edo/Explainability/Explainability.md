Quando si parla di explainability nel campo della [XAI](XAI/XAI.md) si intende la spiegazione delle decisioni prese dai modelli.
# Explainability vs performace
In letteratura c'è un dibattito sul concetto per cui c'è una relazione inversa tra le performance e l'explainability di un modello. Un [grafico](XAI/File/explainability%20vs%20performance.png) molto comune in letteratura evidenzia quali modelli hanno delle prestazioni migliori rispetto alla explainability.
Il punto è che non c'è nessun teorema a favore di questa tesi. In alcune situazioni si riesce a ottenere modelli di XAI le cui performance sono paragonabili ai modelli blackbox.
# Tecniche
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
# Parametri
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