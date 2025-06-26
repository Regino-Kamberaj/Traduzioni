Un problema che il campo dell'AI vuole risolvere è cercare di utilizzare la stessa struttura e modi di fare del nostro cervello. In merito a questo ci sono due tipi di approcci, quello simbolico e quello connessionista (sub-simbolico). Queste due tecniche hanno sia differenze filosofiche che tecniche: non ce ne c'è una meglio o peggio, ma dipende dal caso d'uso.
# Simbolici
Il ragionamento avviene tramite la manipolazione di simboli rappresentati tramite qualche formalismo.
Si basa sulla [logica](XAI/ILP/Programmazione%20logica.md) e si vuole quindi sfruttare una background knowledge.
##### Conseguenze
- È molto interpretabile, come abbiamo visto per gli [ILP system](XAI/ILP/ILP%20system.md).
- Ha bisogno di features discrete (valori finiti ed enumerabili). Diventa complesso, ma fattibile, il reasoning con valori numerici.
- Non è un buon approccio quando abbiamo grandi quantità di dati. Come abbiamo visto per [Aleph system](XAI/ILP/ILP%20system.md#Aleph%20system) si deve costruire i predicati grounded (quelli con tutte le clausole) e questo porta a poca efficienza se abbiamo molti dati.
- Sono metodi soggetti al rumore. Se una regola vale ma non per tutti gli esempi, allora il modello imparerà quella regole e anche un'altra, in modo da coprire tutti gli esempi.
# Connessionisti
Il ragionamento avviene tramite l'elaborazione del segnale tra unità fondamentali interconnesse. Vogliamo in questo modo replicare il ragionamento che avviene nel nostro cervello.
Si basa sulle reti neurali.
##### Conseguenze
- Utile quando non abbiamo una grande conoscenza di base. I modelli scoprono infatti dei pattern in questi in modo non supervisionato, lo svantaggio sta che imparano anche i [bias](XAI/Bias.md) resenti nei dati.
- Non si devono codificare i dati in qualche modo, ma il modello apprende da dati raw.
- Servono una grande quantità di dati.
- Non si ha una grande perdita di prestazioni se in dati viene introdotto del rumore. Le prestazioni decadono in modo lineare rispetto al rumore.
# Unione
Supponiamo di avere tre ingredienti: i metodi simbolici, quelli connessionisti e quello probabilistici. A seconda di come li uniamo otteniamo tecniche diverse.
Oggi questi mondi si incontrano sempre di più.
##### Machine/deep learning
Si ricava dall'unione degli approcci probabilistici e neurali. Ci sono solo features e variabili aleatorie, ma non simboli.
Ci sono soluzione che permettono anche un po' di reasoning, come i LLM.
##### StarAI
È la Statistical Relational AI e unisce metodi probabilistici e simbolici.
Un esempio è una [Markov Logic Networks](regio/Approcci%20neuro-simbolici/Markov%20Logic%20Networks.md).
##### Neural Symbolic Computation (NeSy)
Unisce metodi neurali e simbolici.
- [KBANNs](regio/Approcci%20neuro-simbolici/KBANNs.md)