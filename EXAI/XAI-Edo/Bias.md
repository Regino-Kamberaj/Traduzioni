Un bias è definito come un errore sistematico nel processo decisionale che porta a un risultato [unfair](regio/Fairness.md).
Nel mondo del ML la previsione del modello viene presa basandosi sui dati del train set; se questi dati contengono dei bias allora l'outcome sarà unfair.
- Un esempio è che se passiamo una foto di un matrimonio occidentale allora ci dice che è un matrimonio, ma la foto è di un matrimonio orientale allora ci dice che sono persone.
- Un altro esempio è che se i dati esprimono (e succede davvero) che le donne hanno uno stipendio più basso, allora i modelli di raccomandazione propongono alle donne dei lavori con stipendio più basso.
- Se un dataset contiene foto di lupi dove nella maggior parte i lupi sono sulla neve, allora se chiediamo di classificare un Husky sulla neve ci darà che è un lupo.
# Bias nei dati
Vediamo alcuni tipi di bias nei dati.
- Sampling
	È detto bias di campionamento è succede quando il train set non è ottenuto in modo casuale dalla distribuzione della popolazione, ma ci sono alcune categorie di individui che hanno più probabilità di essere campionate.
	È quindi un problema di come sono raccolti i dati.
- Representation
	Avviene quando ci sono delle sotto popolazioni che sono rappresentate meno. È un concetto molto simile al sampling, ma qua l'attenzione è sulle sotto popolazioni e non sul campionamento in generale
- Artefatti
	Si presenta quando c'è una correlazione tra artefatti (e.g. patch in una foto) e classe di appartenenza del sample.
	In pratica il modello usa l'artefatto per classificare i futuri samples.
# Bias negli algoritmi
Vediamo alcuni tipi di bias negli algorimi.
- Algoritmico
	Non ci sono bias nei dati, ma è l'algoritmo che introduce dei bias per come è costruito.
- D'interazione
	Quando il bias proviene dall'interazione dell'algoritmo verso alcune categorie di utenti.
- Di conferma
	Se chi ha progettato l'algoritmo ha introddo un bias perché il suo pensiero è affetto da bias.
- Generativo
	Se i dati hanno dei bias e un modello generativo genera risposte affetti da questi bias. È strettamente legato ai modelli generativi.