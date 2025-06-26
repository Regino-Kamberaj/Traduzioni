In generale sono tecniche che cercano di ottenere spiegazioni in termini di concetti che si attivano durante il processo decisionale.
Solitamente è una tecnica usata per le reti neurali.
# Concept bottleneck model
![Concept bottleneck model](regio/Explainability/File/Concept%20bottleneck%20model.png)
È un modello strutturato con più layer:
- Concept encoder $g$
	Solitamente è una CNN che prende l'input e produce un vettore di concetti.
- Linear layer $f$
	Prende la lista di concetti ed esegue la classificazione vera e propria. Deve essere semplice: un MLP o meglio anche un semplice layer lineare; se è troppo complesso il modello diventa non spiegabile.
##### Osservazioni
- La lista di concetti è definita in fase di progettazione e i concetti devono essere supervisionati. Ci deve essere quindi un train set di dati annotati con il vettore dei concetti, cioè dove l'etichetta non è la classe ma il vettore.
- La spiegazione, supponendo la semplicità del layer lineare, deriva dal vettore dei concetti che viene associato all'input.
##### Esempio
Se ho un'immagine di una mela, vorrei che la CNN mi restituisca un vettore di informazioni legate ad essa: rosso si, tondo si, quadrato no, blu no, e così via. A questo punto la mia spiegazione è il vettore dei concetti.
# Learning
Vediamo come si addestra il modello.
##### Independent
Il concept encoder e il layer lineare $f$ sono addestrati indipendentemente (eventualmente anche in parallelo):
- Si addestra il concept encoder $g$ con i concetti come target. Si tratta di una classificazione multilabel, cioè dove si possono attivare più concetti.
- Si addestra il layer lineare $f$ dandogli in input i concetti veri, cioè un vettore binario. In pratica l'input dell'addestramento di $f$ è il target dell'addestramento di $g$.
##### Sequential
Il concept encoder e il layer lineare $f$ sono addestrati in modo sequenziale:
- Si addestra prima il concept layer $g$. Solo dopo aver finito di addestrare $g$ si passa all'addestramento di $f$.
- Gli intput dell'addestrato del layer lineare $f$ derivano dall'output di $g$.
##### Joint
Si tratta il modello come fosse un singolo layer, incapsulando l'obiettivo nella loss: $L=L_{target}+\lambda(L_{concept})$, dove:
- $L_{target}$ è la classica loss sull'output (i.e. la classificazione finale), cioè $L_{target}(y_i,f(g(x_i)))$.
- $L_{concept}$ è la loss sui concetti, cioè $L_{concept}(c_i,(g(x_i))$, dove $c_i$ sono i concetti.
##### Conseguenze
- Per la versione join se si usa un $\lambda$ piccolo, allora potrei avere più errori sui concetti, cioè sulle spiegazioni; quando $\lambda$ cresce invece potrei avere più errori sulla classificazione finale.
- Solitamente i primi due metodi tendono a imparare meglio i concetti, cioè la spiegazione. Questi portano ad avere un po' di errore sulla classificazione; tale errore diminuisce sempre più quanto il dizionario dei concetti è grande, cioè diminuisce se i concetti legati all'input non semplifica troppo l'input stesso.