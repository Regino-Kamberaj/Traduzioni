L'explainable AI (XAI) produce e integra modelli di intelligenza artificiale per rendere interpretabile la logica interna e il risultato degli algoritmi, rendendo il processo comprensibile agli esseri umani. Se un modello non fa parte di questa categoria si parla di black-box model.
Nel processo decisionale dovremmo tendere a favore dei modelli black-box solo se le prestazioni motivano questa scelta. Non ci sono infatti motivi per non andare verso un modello XAI se non per le prestazioni: siccome con i modelli XAI lavoriamo maggiormente sui dati, durante la costruzione del modello si può capire se il dataset è affetto da bias, se abbiamo formulato male il problema.
##### Paradosso di Hans
Un uomo aveva un cavallo che reputava molto intelligente a livello scientifico: se gli veniva posta una domanda di tipo matematico allora rispondeva, battendo lo zoccolo per contare, bene; se però l'interlocutore si allontanava e non lo poteva vedere, ma lo poteva solo sentire, allora rispondeva male. La verità è che non aveva un'intelligenza matematica ma osservava molto bene il comportamento dell'interlocutore per rispondere bene.
Il risultato è che si parla di paradosso di Hans quando un agente da un risultato giusto ma per il motivo sbagliato.
# Motivazioni
Le motivazioni principali per cui ci servono motivi spiegabili sono:
- Capire le decisioni
	Ci interessa capire perché un modello ha preso una decisione e non ne ha presa un'altra.
- Migliorare
	Si parla di "human in the loop" quando dopo che il modello ha preso una decisione, l'uomo da il proprio feedback, che finisce nei dati di addestramento. In questo modo di possono produrre modelli personalizzati per una situazione, cioè si possono integrare informazioni che a priori non erano rappresentabili.
- Fiducia
	Se un modello è spiegabile allora possiamo riporre un certo grado di fiducia.
	Questo non vuol dire che se un modello è spiegabile allora è degno di fiducia, ma possiamo capire anche quando non fidarsi.
# Problemi
- Costruzione dei dati
	Un esempio è quello in cui un sistema predice il rischio di un paziente affetto da polmonite. Dai risultati del sistema si osserva che se una persona è asmatica allora ha un basso rischio (basso rischio si intende che poi sta male); questo sarebbe contro intuitivo per ogni dottore.
	Il motivo di questo è che se una persona asmatica ha una polmonite viene curato subito e ha un trattamento privilegiato e quindi alla fine non sta male.
	Tutto questo succede perché nei dati c'è la relazione per cui le persone con asma non stanno male nel lungo periodo, ma questo avviene perché vengono visitate tempestivamente e perché hanno in realtà un rischio alto.
- Blackbox ingannati
	I modelli blackbox possono essere ingannati.
	Un esempio sono gli esempi avversari: abbiamo un immagine $x$ a cui viene applicato un rumore $\epsilon$; il modello predice $x$ con una certa probabilità, ma se valuta $x+\epsilon$ allora predice altro con una probabilità molto più alta.
- [Bias](regio/Bias.md)
# AI Act
L'AI Act definisce 4 livelli di rischio nell'utilizzo dei modelli: si va dal livello più basso in cui sono contenuti gli scenari deve gli uomini non sono coinvolti (es: industria e giochi), fino al livello più alto in cui le persone sono centrali (es: riconoscimento facciale).
L'articolo 13 dell'AI Act afferma che "i sistemi di intelligenza artificiale ad alto rischio devono essere progettati e sviluppati in modo tale da garantire che il loro funzionamento sia abbastanza trasparente per consentire agli sviluppatoti di interpretare l'output di un sistema e utilizzarlo in modo appropriato".
# Interpretability/Explainability
Quando si parla di [explainability](regio/Explainability/Explainability.md) si intende la spiegazione delle decisioni prese dai modelli. Alcuni modelli sono spiegabili per costruzione (by design); in questo caso si parla di [interpretability](regio/Interpretability/Interpretability.md).