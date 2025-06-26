Local Interpretable Model agnostic Explaination (LIME) è una tecnica di local surrogate models del 2016 per l'[outcam explaination](regio/Explainability/Metodi.md#Outcam%20explaination) nel campo dell'[explainability](regio/Explainability/Explainability.md).
- Come explanator usa un modello interpretabile. Solitamente si usa un modello lineare.
- È model agnostic, cioè valido per tutti i tipi di black box.
- Va bene qualunque tipo di dato.
# Idea
Supponiamo di avere una black box che produce una superficie di separazione molto complessa e non lineare.
Se voglio spiegare un'istanza posso creare un modello lineare che mi approssima la black box solo in un introno di quella istanza.
##### Fidelity locale
È importante osservare che la fidelity del modello interpretabile è buona solo localmente al punto da spiegare: un modello lineare approssima bene un modello complesso solo localmente.
Globalmente però la fidelity potrebbe essere, e solitamente lo è, anche pessima.
##### Discretizzazione
LIME lavora in modo discreto: il modello lineare che spiega la black box viene addestrato su features discrete, in particolare binarie.
# Algoritmo
L'algoritmo si basa su $explaination(x)=\displaystyle\arg\min_{g\in G}L(f,g,\pi_x)+\Omega(g)$.
A grandi linee l'algoritmo:
- Genera un insieme di dati perturbando leggermente l'esempio che vogliamo spiegare $x$. Questi nuovi dati saranno vicini a $x$.
- Addestro un modello lineare su questo dataset generato, in modo che questo approssimi bene la black box localmente.
##### Ingredienti
- $x\in \mathbb{R}^d$ è l'input da spiegare definito in uno spazio a $d$ dimensioni. È la rappresentazione originale del dato.
	LIME richiede di definire una rappresentazione interpretabile $x'\in\{0,1\}^{d'}$ definita a partire da $x$ in una dimensione $d'$.
	- Ad esempio, sia $x$ una classica immagine di partenza con dimensione $V\times H\times 3$. Si genera una sua rappresentazione $x'$ costituita da superpixel a colore costante, cioè da gruppi di pixel dove all'interno il colore è lo stesso (cioè un solo canale e non più tre). Questo permette di semplificare la rappresentazione e renderla più capibile.
	- Ad esempio, per dati tabulari la perturbazione consiste nel sostituire un valore 1 con uno 0.
- $G$ è una famiglia di modelli interpretabili.
	LIME nasce per usare modelli lineari, ma l'algoritmo vale anche se voglio usare alberi o altri modelli interpretabili.
- $f$ è la black box.
- $g$ è il modello interpretabile.
- $\pi_x$ è la proximity function.
	Ci serve per definire la distanza di un campione generato con l'input $x$. Un esempio è definirla come una distanza gaussiana $\pi_x(z)=exp(-D(x,z)^2/\sigma)$, dove $D$ può essere la distanza del coseno.
- $L$ è la loss usata per l'addestramento di $g$ ed è usata per garantire la local fidelity.
	È definita come $L(f,g,\pi_x)=\displaystyle\sum_{z,z'\in Z}\pi_x(z)(f(z)-g(z'))^2$, dove $Z$ è il vicinato di $x$, $z$ è la rappresentazione originale di un valore campionato e $z'$ la sua rappresentazione interpretabile.
	In pratica voglio minimizzare l'errore quadratico tra il valore predetto dalla black box sulla rappresentazione originale e quello predetto dal modello interpretabile sulla rappresentazione interpretabile. Si pesa questo errore secondo la vicinanza con il punto da spiegare $x$.
- $\Omega(g)$ è un regolarizzatore lasso che limita la complessità di $g$, cioè assicura che $g$ sia interpretabile.
	È definita come $\Omega(g)=\infty\cdot\mathbb{1}[||w_g||_0>k]$: il regolarizzatore da un contributo infinito se il vettore dei pesi $w_g$ del modello interpretabile non è sparso almeno quanto $k$, cioè se il numero di valori diversi da 0 è più di $k$. Il valore di $k$ è un iperparametro.
	Nella pratica è il numero di parole per il testo, di superpixel per immagini o il numero di features per dati tabulari.
##### Pseudo codice
- Input:
	- La black box $f$.
	- Il numero $N$ di campioni nel vicinato.
	- L'istanza da spiegare $x$ e la sua versione interpretabile $x'$.
	- La funzione distanza $\pi_x$.
	- La lunghezza della spiegazione $k$.
	- Tecnica per passare da $z'$ a $z$.
- $Z\leftarrow\{\}$.
- $for\ i\cdots,N:$ (ciclo che genera i campioni)
	- $z_i'\leftarrow samplearound(x')$
	- $Z\leftarrow Z\cup\{(z_i,z_i',\pi_x(z_i))\}$
- $w\leftarrow k-lasso(Z,k)$ (addestramento del modello interpretabile)
##### Costo
Usando l'hw dell'articolo si ha un costo rispetto al tempo di:
- Con una random forest composta da 1000 alberi e $N=5000$ ci vogliono 3 secondi.
- Con una inception network e $N=5000$ ci vogliono 10 minuti.
# Submodular pick (SP-LIME)
Siccome il costo in tempo di LIME è comunque abbastanza alto, ci interessa trovare quegli esempi da spiegare che possono permettere all'utente di capire al meglio possibile la black box.
L'algoritmo SP trova applicazione quando un utente ha un budget $B$ di tempo limitato per capire come funziona il modello black box.
##### Idea
Viene costruita una matrice dove sulle righe ho gli esempi che voglio spiegare e sulle colonne le features.
Applicando LIME è come se evidenziasse per ogni esempio le celle relative alle features che sono state maggiormente usate per spiegare quell'esempio. Quello che questo algoritmo fa è [massimizzare la coverege](regio/Explainability/File/SP%20LIME.png) delle features importanti sulla base degli esempi di test: in pratica calcoliamo la spiegazione per ogni esempio del test set e poi scegliamo quegli esempi che coprono tutte (o la maggior parte) delle features più importanti, cioè quelle maggiormente usate da tutti gli esempi.