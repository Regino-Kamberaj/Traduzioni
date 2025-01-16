# Capitolo 1: Concetti di base

## **1.1 Introduzione**
La sicurezza di un sistema è difficile da definire poiché il termine stesso è soggetto a molte interpretazioni. In generale, le proprietà della sicurezza sono:

- **Confidenzialità**: Assicurarsi che le informazioni non siano accessibili a utenti non autorizzati.
- **Integrità**: Garantire che le informazioni non vengano alterate da utenti non autorizzati senza che ciò venga rilevato.
- **Autenticazione**: Garantire che gli utenti autorizzati siano effettivamente coloro che dichiarano di essere.

Questa classificazione, spesso chiamata CIA (Confidentiality, Integrity, Authentication), è troppo semplice e fuorviante, in quanto esistono molte altre versioni di queste proprietà.

## **1.2 Sicurezza vs. Safety** 
Non bisogna confondere la sicurezza (security) con la safety:
- **Sicurezza**: Rappresenta l'assenza di pericoli o ansie legate al pericolo.
- **Safety**: Indica la protezione da danni fisici, il che è rilevante nei sistemi cibernetici che possono influire sulla sicurezza fisica.

## **1.3 Costi della sicurezza** 
La sicurezza ha costi significativi per tre motivi principali:
- Aumenta la complessità del sistema.
- Richiede tempi di implementazione e manutenzione più lunghi.
- Cambia i flussi di lavoro.

Prima di pianificare, è necessario definire cosa proteggere, perché e contro chi. Se le politiche di sicurezza sono troppo restrittive, gli utenti troveranno il modo di eluderle, rendendole inefficaci (fenomeno noto come **deimplementazione**).

Dunque prima di prendere qualsiasi misura di sicurezza, dobbiamo chiederci:
- Quanto costa?
- Quanto stiamo limitando gli utenti?
- Cosa stiamo proteggendo?
- Perché gli stiamo proteggendo?
- Da cosa gli stiamo proteggendo?
In altre parole, dobbiamo aver chiaro qual'è il contesto operativo nel quale stiamo lavorando. 

## **1.4 Enterprise Architecture Framework**
Un **Enterprise Architecture Framework** (EAF) definisce come creare e usare l'architettura aziendale. Gli EAF includono principi e pratiche per documentare i vari aspetti di un sistema, consentendo di prendere decisioni progettuali a lungo termine.

Esempi di EAF sono
- Framework civili:
	- COBIT: framework for IT Governance and Control;
	- TOGAF: The Open Group Architecture Framework;
- Framework militari:
	- DoDAF: United States Department of Defense Architectural Framework;
	- MODAF: United Kingdom Ministry of Defense Architectural Framework;
	- NAF: NATO Architecture Framework;
- Framework opensource:
	- SABSA: for Enterprise Security Architecture and Service Management;

### **1.4.1 Struttura EAF**
La maggior parte degli EAF utilizza modelli iterativi. Le prime e più importanti fasi sono:
- **Fase Preliminare**: Definisce gli obiettivi dell'azienda.
- **Visione Architetturale**: Definisce il contesto e le aspettative del progetto.
- **Architettura Business**: Definisce come verranno effettuati e utilizzati gli investimenti iniziali.
- **Requisiti**: Una fase ricorrente tra le più importanti, garantisce che ogni di un progetto sia eseguito correttamente e sia conforme a tutti i requisiti che possono esistenti. I requisiti derivano principalmente dall'architettura aziendale e possono essere soddisfatti al 100% o non soddisfatti affatto (non esiste una via di mezzo).
- **Architettura dei sistemi informativi**: definisce i dati necessari per il corretto funzionamento dell'impresa; non specifica le architetture di rete, i programmi necessari o altre risorse software, ma presuppone che i dati siano il bene più prezioso e quello su cui si definiscono i requisiti di sicurezza. Si noti che è della massima importanza non specificare le tecnologie attuali nei requisiti di sicurezza, perché cambiano troppo rapidamente e, anche se in futuro potrebbero diventare vulnerabili, il documento tecnico ne imporrà comunque l'uso. Si dovrebbe includere una nota che indichi che data una certa architettura, gli algoritmi di crittografia e le misure di sicurezza devono essere periodicamente rivisti e aggiornati.

Il resto delle fasi definiscono l'evoluzione aziendale più che i requisiti di sicurezza.
			![[Pasted image 20240927182831.png]]

### **1.4.2 Asset** 
Un **asset** è una risorsa preziosa per l'azienda, e proteggerlo è l'obiettivo principale della sicurezza. Gli asset possono essere **dati**, **componenti software** o **hardware**.

Il livello di sicurezza di un asset deriva dalle sue proprietà; ogni asset ne ha molti, che possono essere fissati da:
- **Legge**: leggi sulla privacy, ecc. (es. GDPR, leggi sulla sicurezza nazionale);
- **Aziende**: qualsiasi cosa l'azienda voglia fare con i suoi beni (es. garantire ai propri utenti
un certo livello di privacy);
- **datore di lavoro**: può essere qualcuno che ha bisogno di una sicurezza supplementare (ad es. il Dipartimento della difesa);
- **contratto**: potrebbe includere accordi di non divulgazione (NDA) o altre politiche simili.

Queste proprietà, tutte elencate nel l'EAF, possono essere **intrinseche** (imposte da un
entità esterna, come la legge) o **estrinseca** (deciso dalla stessa impresa), e devono essere
specificati in termini di must/must not (assets che devono soddisfare al 100% a queste proprietà)

Tutte le proprietà si estendono a tutti i beni che gestiscono altre attività, es. se vi è un requisito sui dati, quindi tutte le applicazioni che lo gestiscono devono soddisfare qualsiasi requisito sui dati. Ciò significa che la sicurezza è forte quanto l'anello più debole della catena. ??

## **1.5 Gestione del rischio** 
La gestione del rischio include:
1. Identificazione del rischio.
2. Valutazione del rischio.
3. Implementazione delle politiche e delle contromisure.
4. Manutenzione delle politiche e delle contromisure.
Senza i primi due punti non è possibile proseguire con il resto.

#### **1.5.1 Valutazione del rischio**
Esistono due metodologie per valutare i rischi:
- **Valutazione qualitativa**: Visione semplice e concisa dei rischi.
- **Valutazione quantitativa**: Valutazione matematica delle perdite attese.

La Valutazione qualitativa utilizza una matrice per rappresentare visivamente quanto è un rischio è importante.
![[Pasted image 20240927183806.png]]
In questo modo diventa facile identificare i possibili rischi e dunque quali dovrebbero essere in qualche modo diminuiti il prima possibile.
Non tutti i rischi devono essere coperti, quelli nella zona centrale sono considerati in qualche modo accettabili, dunque non si fa niente per evitarli.
Quelli invece sulla zona in alto a destra, viene fatto in modo tale da essere riportare nella zona di meno rischio, a seconda dei costi e delle misure più efficaci.
In generale, anche se spostare un rischio direttamente nella parte inferiore sinistra della matrice potrebbe, sembra ideale, facendo questo non è consigliato perché i costi per raggiungerlo sarebbe troppo alto, per cui come detto in precedenza vengono scelti alcuni compromessi.

--- 

La valutazione quantitativa del rischio è un metodo analitico, meno visivo, che può essere calcolato, seguendo le seguenti fasi:
1. Assegnazione del **asset value** (AV): dato un asset, gli attribuiamo un certo valore economico in base alla sua importanza;
2. **Annual Rate of Occurence** (ARO): come il nome implica, valutiamo il numero di volte in cui è probabile che si verifichi un determinato rischio in un anno;
3. Stima del fattore di esposizione (**Exposure Factor** --> EF): soggettiva, percentuale potenziale di perdita se un determinato rischio si realizza;
4. **Single-Loss Expectation** (SLE): SLE = AV * EF ; rappresenta il valore monetario previsto dal verificarsi di un rischio su un'attività;
5. **Annualized-Loss Expectation** (ALE): ALE = SLE * ARO; come la formula implica,
è il prodotto del tasso annuale di occorrenza (ARO) e della singola aspettativa di perdita
(SLE).

_Attenzione alla media_: utilizzarla senza conoscerne la distribuzione di probabilità potrebbe essere dannosa e controproducente. È di solito più sicuro e più informativo considerare minimo e valori massimi di un numero.
### 1.5.2 Risk analysis
Per analizzare correttamente un rischio occorre prendere in considerazione molte fasi e aspetti diversi in considerazione, come illustrati nella figura:
![[Pasted image 20240928175215.png]]

Dato un **asset** e i suoi **dati**, il **livello di sensibilità** indica quanto l'asset è importante per l'attività; più alto è questo valore, maggiore è il livello di protezione necessario per l'asset (e quindi minore è il rischio).

Il **livello di protezione** di un'asset è direttamente correlato al suo livello di sensibilità; esso è attuato attraverso:
1. **Politiche di sicurezza**: attenuano il verificarsi del rischio (ad es. un database potrebbe implementare una lista di controllo degli accessi, in modo che solo gli utenti autorizzati possano accedervi);
2. **Contromisure**: attenuano le conseguenze del rischio dopo che si è verificato (ad es. un sistema di backup periodico).

Il **rischio** dipende quindi da due grandi famiglie di problemi: l'**affidabilità (Reliability)** , che comprende tutti quei fattori determinati dai guasti naturali del sistema, e la **vulnerabilità**, la possibilità che il sistema possa essere attaccato da qualcuno. 
Le vulnerabilità sono innescate dall'esistenza di un bug nei protocolli, nei componenti o nel software utilizzato dall'asset, vale a dire:
- **componenti tecnici** (hardware), generalmente soggetti a problemi di affidabilità;
- **componenti applicativi** (software), generalmente soggetti a problemi di vulnerabilità.

Le vulnerabilità possono essere trovate attraverso **l'analisi delle vulnerabilità** o come
processo di valutazione (**Vulnerability Assessment VA**). È un problema critico, aperto nell'ingegneria del software e della rete, perché anche se alcune vulnerabilità sono conosciute e possono essere corrette o almeno parzialmente coperte, più spesso che non sono conosciute, non possono essere prese contromisure contro di essi né possono essere prese in considerazione nel calcolo dei rischi. 
Quindi, tutte le vulnerabilità rappresentano una minaccia grave che potrebbe essere sfruttata da un **agente di minaccia** - anche se la loro esistenza significa solo che hanno il potenziale per essere sfruttato da un agente maligno, non che questo effettivamente accadrà. In ogni caso, un *modello di minaccia* può essere utilizzato per valutare meglio come un agente maligno potrebbe danneggiare l'asset.

## **1.6 Modello di minaccia**
Il **modello di minaccia** descrive le minacce potenziali. Esso è fondamentale per definire le probabilità di rischio. Dovrebbe contenere informazioni sulle risorse a disposizione del l'attaccante, in termini di **informazioni disponibili**, **capacità di calcolo** (la potenza di calcolo dipende dall'attacco) e **controllo del sistema** (cosa sarebbe in grado di fare l'attaccante, con le sue conoscenze). 
Il modello specifica anche gli obiettivi dell'attaccante e quanto seria sarebbe questa persona nei confronti delle sue azioni.
Il modello di minaccia è necessario per definire la probabilità di rischio, e dipende dall'asset e dagli obiettivi dell'attaccante: più alti sono gli obiettivi, maggiori sono le capacità dell'attaccante. Ovviamente, il modello non tratta solo le minacce fisiche; molti asset sono irrilevanti, come i segreti industriali, e una volta caduti nelle mani di un aggressore possono essere considerati perduti per sempre - anche se l'azienda li possiede ancora.

### **1.6.1 Modello di minaccia di Internet**
Il modello di minaccia generico di Internet assume:
- **Il principio di Kerckhoff**, secondo il quale l'attaccante conosce TUTTO sul sistema.
- L'attaccante ha abbastanza **potenza computazionale**: senza mai limitare ai sistemi off-the-shelf (ovvero sistemi commerciali), in quanto alcuni attaccanti possono usare strumenti altamente specializzati --> anche computer quantistici.
- L'attaccante ha il **controllo del sistema di comunicazione**: l'attaccante potrebbe iniettare dati nella rete. Si noti che l'attaccante potrebbe **non avere il pieno controllo** della rete, e/o potrebbe dover nascondere la sua presenza, in modo da poter inviare solo dati compromessi (attacchi attivi, ciechi o quasi ciechi) o ricevere solo (attacchi passivi);

In altre parole si assume che, anche se i sistemi non sono stati violati, la comunicazione dei sistemi potrebbe essere non sicura.
#### **Esempi di attacchi**

- **Attacchi passivi**: 
	- Violazioni della confidenzialità
	- furto di password
	- attacchi crittografici offline.
- **Attacchi attivi**:
	- Replay di messaggi
	- inserimento, cancellazione o modifica di messaggi.
L' attaccante passivo di solito ha una posizione privilegiata sulla rete, e l'invio di un qualsiasi messaggio farebbe notare la sua presenza. Per questo motivo rimane spesso in silenzio e solamente riceve dati.

### **1.6.2 Topologia di rete** 
La topologia della rete influisce sulla capacità di un attaccante. 
Gli attacchi possono essere:
- **On-path**: L'attaccante è sul percorso naturale dei dati, fra i due *endpoints*.
- **Off-path**: L'attaccante non vede i dati in transito da uno dei due punti, e per non essere visto, deve simulare uno degli endpoint, senza però poter vedere le possibili risposte dell'endpoint simulato verso l'altro endpoint.
- **Link-local**: Il caso peggiore, in quanto l'attaccante si trova esattamente sullo stesso link (in particolare vicinanza) dell'endpoint, nella stessa *subnet* oppure fisicamente attaccato alla stesso *switch/access point*. Questa posizione privilegiata, permette un vasto numero di attacchi.

Possiamo supporre che l'attaccante sia *off-path* se e solo se controlliamo ogni singolo router e collegamento tra i punti A e B, e possiamo essere sicuri che l'attaccante non abbia violato nessuno di questi dispositivi. Si tratta di un obiettivo realmente realizzabile?
La risposta a questa domanda è che dipende dal l'instradamento geografico dei dati, che a sua volta dipende dai grandi collegamenti di comunicazione tra la fonte e la destinazione.

Per esempio, una volta c'era un progetto di posa di un cavo in fibra ottica tra l'America e l'Asia, con uno dei principali punti di interscambio a Hong Kong; gli USA hanno chiesto che questo punto venga rimosso, al fine di evitare il controllo della Cina, poiché avrebbero permesso attacchi on-path. Questa richiesta non è stata soddisfatta e quindi il progetto non è mai stato completato.

Si noti che gli errori nelle tabelle di routing che inviano dati attraverso luoghi che non dovrebbero riceverli (es. San Francisco-Seattle attraverso la Cina) sono all'ordine del giorno, quindi in conclusione, mai, mai presumere che l'attacco è off-path, perché un attaccante può diventare on-path attraverso un attacco secondario al routing.
# Capitolo 4: Internet

L'Internet è un progetto di 60 anni che contiene ancora elementi ereditati dalla sua implementazione originale – un tempo incredibilmente lungo per una rete di telecomunicazioni. È stato costruito lentamente, pezzo per pezzo, inizialmente sviluppato per piccole reti monolitiche (che si sono evolute in base a ciò che volevano i fornitori), risultando molto difficile da usare.

Internet è sopravvissuto e prosperato grazie a molti fattori, tra cui possiamo trovare:

- **Fattori economici**: era (ed è tuttora) quasi gratuito;
- **Fattori tecnologici**: era aperto, quindi chiunque poteva sviluppare i propri protocolli;
- **Facilità d'uso**: era molto più semplice rispetto all'uso di socket grezzi;
- **Utenti finali**: gli stessi sviluppatori erano anche gli utenti finali, quindi potevano modificare ciò che non funzionava come volevano;
- **Fattori politici**: le compagnie di telecomunicazioni hanno guidato tutti gli standard wireless e cablati, anche se per molto tempo hanno creduto che le comunicazioni tradizionali (telefonate, SMS) fossero migliori.

Ciò che ha sempre ostacolato (e probabilmente lo farà ancora) lo sviluppo di Internet è il dover convivere con tutto ciò che è stato già distribuito (come il protocollo TCP/IP), rendendo difficile la diffusione di nuovi e migliori protocolli.

## 4.1 Storia di Internet

Una storia dettagliata di Internet e dei protocolli può essere facilmente trovata su Internet stesso. Fino agli anni '70, Internet ha subito un'evoluzione tecnica di base e sono stati principalmente utilizzati modelli di rete verticali.

Negli anni '80 e '90, Internet è diventato noto al mondo, e i servizi hanno cominciato a essere disponibili per tutti. Da allora è iniziata la competizione tra i fornitori di servizi.

Oggi Internet è onnipresente e offre migliaia di servizi diversi, legali o illegali; per questo motivo, è spesso limitato dalla politica e dall'economia. La neutralità della rete è diventata un principio importante per cui molte persone si battono.

## 4.2 Di cosa è fatto Internet?

Internet non è una singola rete, ma un'interconnessione di reti e una raccolta di **sistemi autonomi.** Si basa su pubblicazioni di **Request for Comments (RFC)** dall'Internet Society (ISOC) e dai suoi organi associati (come l'Internet Engineering Task Force - IETF), il principale organismo tecnico per lo sviluppo e la definizione degli standard per Internet.

Le connessioni fisiche degli host non sono così importanti quanto i protocolli che rendono possibile la comunicazione. Sebbene Internet sia basato su **TCP/IP**, esistono molti altri protocolli, e TCP/IP stesso è molto **flessibile**.
--> vedesi lo standard _RCP 1149_, uno standard di comunicazione dove si sfruttarono i piccioni...

### 4.2.1 Mappatura di Internet

Molte organizzazioni, come il **Center for Applied Internet Data Analysis (CAIDA)**, eseguono la mappatura di Internet, studiando la connettività fisica di Internet.
![[Pasted image 20240928195137.png]]
--> mappa di Diffusione dell'IPv4 nel 2015 e nel 2017
All'interno della mappa ogni punto è un sistema autonomo costituito da router/computer(non un singolo nodo) ed è centrale o periferico a seconda di quanto traffico genera o riceve.
Due punti sono collegati da una linea se si scambiano dati in modo diretto, mentre le linee rosse sono delle _superlinee_ di internet che portano più traffico e di solito differiscono dalle linee degli utenti finali.
### 4.2.2 Alcune definizioni

- **Sistema Autonomo**: Collezione di prefissi di routing (Internet Protocol IP) controllati da uno o più operatori di rete con una politica di routing comune. (Segue uno certo standard --> RFC 1930)
- **Gateway**: Entità di rete che connette reti diverse e definisce i confini di una rete. Come un router, funge da nodo intermedio che richiede un interfaccia IP per ogni subnet alla quale è collegata. Risiede nel terzo e/o settimo strato del protocollo ISO/OSI.
- **Host**: La sorgente e destinazione dei dati, identificato univocamente dal suo indirizzo IP. Riside al terzo strato del protocollo ISO/OSI.
- **Network**: Mezzo al quale possono essere collegati molti nodi, sul quale ogni nodo ha un indirizzo e che permette ai nodi ad esso connessi di trasferire messaggi ad altri nodi collegati, fornendo il contenuto di un messaggio e l'indirizzo del nodo di destinazione, quindi lasciando alla rete  il modo di consegnare il messaggio al nodo di destinazione, eventualmente instradandolo attraverso nodi intermedi.
- **Protocol Stack**: Gruppo di protocolli che lavorano insieme per permettere a software o hardware di svolgere una funzione. Nelle telecomunicazoni il protocollo TCP/IP è un buon esempio.
- **Router**: Dispositivo della rete che connette diverse reti insieme e controlla il traffico dei dati fra questi. Un router come il gateway è un nodo intermedio che richiede un interfaccia IP per ogni subnet connessa, e tramite interne _routing tables_, legge ogni pacchetto dall'indirizzo IP e successivamente decide il percorso più breve per passarlo, dopo aver ipotizzato la subnet di destinazione:
	- Se la destinazione sta su una subnet direttamente connessa al router, il pacchetto viene spedito in modo diretto
	- Altrimenti ricerca il prossimo router e gli trasferisce il pacchetto.
	Ogni router prende decisioni in modo autonomo, l'idea è stata fatta in modo tale che i router possano riassestarsi sempre autonomamente. Come il gateway sta al terzo e/o settimo layer del protocollo ISO/OSI.
- **Tabella di routing**: Una lista di tutti di indirizzi IP a cui un router può connettersi per trasferire i dati.
- **Service Access Point** (SAP):  Etichetta di identificazione per gli endpoint, usati nelle reti ISO/OSI. In sostanza è un luogo concettuale in cui uno strato ISO/OSI può richiedere i servizi di un altro livello ISO/OSI.
- **Subnet**: Segmento di una rete identificato da una coppia {*Network Address* , *Subnet Mask* }; si tratta fondamentalmente di una rete all'interno di una rete. Attraverso le subnet, il traffico di rete può percorrere una distanza più breve senza passare attraverso inutili router per raggiungere la sua destinazione, mentre i router sono utilizzati per comunicare tra diverse subnet.
- **Subnet mask**: Simile a un indirizzo IP, ma solo per uso interno all'interno di una sottorete. Non è indicato all'interno dei pacchetti di dati che attraversano Internet, perché questi pacchetti indicano solo l'indirizzo IP di destinazione.
	

## 4.3 Struttura di Internet

Quanto dovremmo sapere sui protocolli di Internet? La sicurezza di molti protocolli è strettamente legata al modo in cui funzionano. Per trovare vulnerabilità è necessario conoscere molto bene un protocollo.

L'idea dietro il modello **ISO/OSI** è quella di dividere la rete in vari livelli separati, ognuno dei quali offre servizi al livello superiore e riceve servizi da quello inferiore.

			![[Pasted image 20240930162006.png]]

1. **Livello fisico**: Responsabile della trasmissione e ricezione dei dati non strutturati tra un dispositivo e un mezzo di trasmissione fisico.
2. **Livello Data Link**: Fornisce il trasferimento di dati nodo-a-nodo e corregge errori dal livello fisico.
3. **Livello di rete**: Trasferisce pacchetti da un nodo all’altro in diverse reti.
---
- In un protocollo di rete costituito da più livelli, ciascun livello aggiunge i propri dati in un'intestazione (header) e, facoltativamente, un'intestazione di coda (trailer), costruendo una **Unità Dati di Protocollo (PDU)**.
- ![[Pasted image 20240930162544.png]]
- Il principio seguito è quello dell'**incapsulamento**, un metodo di progettazione di protocolli di comunicazione modulari in cui le funzioni logicamente separate nella rete vengono astratte dalle loro strutture sottostanti attraverso l'inclusione o il nascondimento delle informazioni all'interno di oggetti di livello superiore ![[Pasted image 20240930162618.png]]
-> ogni layer include i dati del precedente, senza però poter individuare ogni parte del layer precedente, questo serve a encapsulare le informazioni dei layer precedenti.

- L'incapsulamento è: 
	– **ricorsivo**: ogni livello aggiunge la propria intestazione (e coda, se presente); 
	– **reversibile**: è sempre possibile de-incapsulare correttamente la PDU del livello superiore.
### 4.3.1 Protocollo ISO/OSI

Il modello **ISO/OSI** è un modello concettuale, con lo scopo di standardizzare la comunicazione tra sistemi di telecomunicazione, senza guardare la sua struttura interna o la tecnologia. Il suo obiettivo è l'interoperabilità di diversi sistemi di telecomunicazioni con standard di comunicazione.
Presenta sette livelli di architettura, ovvero 7 layers di comunicazione.![[Pasted image 20240930163645.png]]

- I livelli da **L1 a L3** sono anche chiamati **media layers** (livelli fisici), poiché gestiscono le connessioni da un collegamento all'altro, mentre i livelli da **L4 a L7** sono i **host layers** (livelli host), perché gestiscono connessioni **end-to-end** (da un'estremità all'altra). 

- Questo modello vieta la comunicazione tra i livelli. I due principi chiave del modello sono: 
	– **separazione delle responsabilità**: le funzionalità non devono essere duplicate;
    – **nascondimento delle informazioni**: l'implementazione deve rimanere nascosta e separata dall'interfaccia.

- Non è necessario sviluppare un livello separato per ogni funzione descritta nel modello. Tuttavia, seguendo le linee guida generali, gli sviluppatori possono garantire un certo livello di compatibilità.

**1. Livello Fisico** 
Il livello fisico è responsabile della trasmissione e della ricezione di dati grezzi non strutturati tra un dispositivo e un mezzo di trasmissione fisico. Converte i bit digitali in segnali elettrici, radio o ottici.

**2. Livello Data Link (Collegamento Dati)**
Il livello di collegamento dati fornisce il trasferimento di dati da nodo a nodo, stabilendo un collegamento tra due nodi direttamente connessi. Rileva e, se possibile, corregge gli errori che possono verificarsi nel livello fisico. 
Definisce il protocollo per stabilire e terminare una connessione tra due dispositivi fisicamente collegati.
- L'IEEE 802 divide il livello di collegamento dati in due sotto-livelli: 
	– **Livello di controllo dell'accesso al mezzo (MAC)**: responsabile del controllo di come i dispositivi in una rete accedono al mezzo e ottengono il permesso di trasmettere dati; 
	– **Livello di controllo del collegamento logico (LLC)**: responsabile dell'identificazione e dell'incapsulamento dei protocolli di livello di rete; controlla anche il controllo degli errori e la sincronizzazione dei frame.

**3. Livello di Rete** (Network layer)
l livello di rete fornisce i mezzi funzionali e procedurali per trasferire pacchetti da un nodo a un altro connesso in reti diverse. Se il pacchetto (messaggio) è troppo grande per essere trasmesso da un nodo all'altro tramite il livello di collegamento dati tra quei nodi, la rete può implementare la consegna dei messaggi suddividendolo in più frammenti in un nodo, inviando i frammenti indipendentemente e riassemblandoli in un altro nodo. 
Può, ma non è obbligata, a segnalare errori di consegna.

**4. Livello di Trasporto** 
Il livello di trasporto fornisce i mezzi funzionali e procedurali per trasferire sequenze di dati di lunghezza variabile da un host sorgente a un host di destinazione, mantenendo le funzioni di qualità del servizio. Controlla anche l'affidabilità di un dato collegamento attraverso il controllo del flusso, la segmentazione/desegmentazione e il controllo degli errori.

**5. Livello di Sessione** 
Il livello di sessione controlla le connessioni tra computer. Stabilisce, gestisce (checkpoint, sospende e riavvia) e termina (in modo ordinato) le connessioni tra le applicazioni locali e remote.

**6. Livello di Presentazione** 
Il livello di presentazione stabilisce il contesto tra entità del livello applicativo, in cui tali entità possono utilizzare sintassi e semantiche diverse se il servizio di presentazione fornisce una mappatura tra di esse. Se è disponibile una mappatura, le unità di dati del protocollo di presentazione sono incapsulate nelle unità di dati del protocollo di sessione e passate giù per la pila di protocolli. Questo livello fornisce indipendenza dalla rappresentazione dei dati, traducendo tra i formati dell'applicazione e della rete.

**7. Livello Applicativo** 
Il livello applicativo è il livello ISO/OSI più vicino all'utente finale, il che significa che sia il livello applicativo ISO/OSI che l'utente interagiscono direttamente con l'applicazione software. Questo livello interagisce con applicazioni software che implementano una componente di comunicazione. Tali programmi applicativi sono al di fuori dell'ambito del modello ISO/OSI. Le funzioni del livello applicativo tipicamente includono l'identificazione dei partner di comunicazione, la determinazione della disponibilità delle risorse e la sincronizzazione della comunicazione.
### 4.3.2 Protocollo TCP/IP

Il protocollo **TCP/IP** è il più comunemente usato su Internet. Sebbene violi il principio di separazione delle responsabilità del modello ISO/OSI, è flessibile e consente l'interconnessione tra sistemi.

**TCP**  
Il **Transmission Control Protocol** è una suite di protocolli Internet che suddivide il messaggio in segmenti TCP e li riassembla sul lato ricevente.

**IP**  
Un indirizzo **Internet Protocol**, noto anche come indirizzo IP, è un'etichetta numerica. Viene assegnato a ciascun dispositivo collegato a una rete informatica che utilizza il protocollo IP per la comunicazione. La sua funzione di instradamento consente il funzionamento dell'internet e essenzialmente lo stabilisce.
				![[Pasted image 20241004082402.png]]

La combinazione di IP con TCP permette di sviluppare una connessione virtuale tra una destinazione e una sorgente.

**1. Livello Data Link (L2)**  
Questo livello instrada i dati tra dispositivi sulla stessa rete e gestisce lo scambio di dati tra la rete e altri dispositivi. Lo stack TCP/IP presuppone semplicemente che la rete sottostante faccia del suo meglio per trasferire i pacchetti dalla sorgente alla destinazione; non vengono fatte ulteriori ipotesi, quindi in realtà potremmo utilizzare qualsiasi livello di collegamento dati (anche uccelli come i piccioni, come si vede nella sezione 4.2).

**2. Livello di rete (L3)**  (Network)
A questo livello, il protocollo Internet (IP) utilizza l'indirizzo IP, composto da un identificatore di rete e un identificatore di host, per determinare l'indirizzo del dispositivo con cui sta comunicando.
   
**3. Livello di trasporto (L4)** (Transport)
Questa è la parte dello stack di protocolli dove si trova il Transmission Control Protocol (TCP). Il TCP funziona chiedendo a un altro dispositivo sulla rete se è disposto ad accettare informazioni dal dispositivo locale.
    
**4. Livello applicazione (L7)** (Application)
I protocolli per funzioni specifiche come la posta elettronica (Simple Mail Transfer Protocol, SMTP) e il trasferimento di file (File Transfer Protocol, FTP) risiedono a questo livello.

### 4.3.3 Indirizzi
	1
Gli indirizzi sono importanti perché, se usati in modo scorretto, possono permettere agli attaccanti di fare molte cose dannose: per fingere di essere qualcun altro, hanno bisogno di una sorta di maschera, e un indirizzo è la miglior maschera dietro la quale un attaccante può nascondersi.

**Indirizzo MAC**  
Un indirizzo **Media Access Control (MAC)** (spesso chiamato erroneamente indirizzo fisico) è solitamente un indirizzo fisso il cui formato (e lunghezza) dipende dalla tecnologia utilizzata dalla scheda di rete del dispositivo.  

Ad esempio, i dispositivi Ethernet e WiFi hanno entrambi indirizzi MAC a 48 bit; 
l’IEEE 802.15.4 ha indirizzi MAC a 48 o 64 bit; LTE e altre interfacce wireless hanno indirizzi di lunghezza diversa e di solito con un significato particolare.  

L’unico vero requisito per gli indirizzi MAC non è che siano **unici nell’intera Internet,** ma che non possano esistere due schede di rete diverse con lo stesso indirizzo MAC nella stessa rete locale, poiché il MAC identifica una scheda di rete in quella rete specifica, dunque si può avere parecchia confusione perchè non sappiamo dove mandare i pacchetti.

È importante notare che una scheda può avere più di un indirizzo MAC; dipende dall'hardware. Di solito, la maggior parte delle schede di rete non ci permette di farlo, perché con più indirizzi MAC saremmo visti nella rete come più dispositivi, anche se ne abbiamo solo uno.  

Esistono anche dispositivi hardware che possono essere programmati per filtrare pacchetti basandosi su più di un indirizzo MAC: tecnicamente, tutto è possibile.  

Notoriamente, in una rete esistono anche indirizzi MAC speciali, come l'indirizzo broadcast (che invia pacchetti a tutte le schede di rete in grado di riceverli).  

Per impostazione predefinita, quando una **NIC** (network interface controller, un altro nome per ciò che comunemente è una scheda di rete) riceve un pacchetto, controlla l'intestazione e se non è indirizzato all'indirizzo MAC di quella scheda di rete lo scarta (a meno che sia un pacchetto indirizzato in broadcast o multicast).

In modalità *promiscua* (una modalità speciale disponibile per tutte le NIC), tuttavia, la NIC consente il passaggio di tutti i pacchetti, permettendo così al computer di leggere e rispondere ai pacchetti destinati ad altre macchine o dispositivi di rete.  
La modalità promiscua può essere usata in modo dannoso per catturare dati privati in transito su una rete, quindi potremmo essere interessati a rilevare dispositivi di rete che si trovano in modalità promiscua per individuare potenziali attaccanti. 

Il ruolo dell’indirizzo MAC non è prevenire questa modalità; è stato progettato solo per efficienza: il bus tra la NIC e la CPU è un collo di bottiglia, quindi una scheda di rete che non è in modalità promiscua filtra tutti i pacchetti ricevuti basandosi sulle loro intestazioni e indirizzi MAC per evitare di rallentare il traffico sul bus con pacchetti inutili.

**Indirizzo numerico**  
L’indirizzo numerico è solo un altro nome per l'indirizzo IP, che è necessario per il processo di instradamento. Deve essere conforme alla rete a cui siamo collegati (significa che deve rientrare nell’intervallo di indirizzi gestiti dal router su quella rete) e di solito è assegnato da un amministratore di rete (network manager). Un indirizzo IP ha due funzioni principali: **identificazione dell'host** e **indirizzamento della posizione**, e per questo motivo ==deve essere unico nella rete globale.==  
Ad esempio, **150.217.8.24** è un indirizzo IPv4, un tipo di indirizzo numerico al livello 3 scritto nella sua forma canonica.

Nota che in realtà tutti gli indirizzi sono numeri binari di lunghezza fissa (32 bit per IPv4 e 128 bit per IPv6). Inoltre, è possibile e perfettamente legittimo che un dispositivo abbia più di un indirizzo IP, per varie ragioni (ad esempio, se l'host è collegato a più di una rete).

**Indirizzo alfanumerico**  
Gli indirizzi alfanumerici sono indirizzi speciali che corrispondono agli indirizzi IP. Sono completamente gratuiti e l'unico requisito è che qualcuno (il DNS) li mappi direttamente e inversamente a un indirizzo IP, basandosi su un database.  
Esempio: **daconets.dinfo.unifi.it** è un indirizzo alfanumerico.  

In generale, un host può avere uno o più indirizzi MAC sulla stessa scheda di rete, uno o più indirizzi IP per ciascun indirizzo MAC, e ogni indirizzo IP può avere nessuno, uno o più indirizzi alfanumerici.
D'altra parte, un indirizzo alfanumerico può essere mappato a uno o più indirizzi IP (poiché si tratta di un database). Tuttavia, avere un ==IP mappato su più di un indirizzo MAC non è consigliato==, in quanto possono accadere molte cose negative. 
L'unico caso in cui questa soluzione è una buona idea è quando un esperto ingegnere di rete collega il dispositivo a due reti diverse, oppure quando assegna il nostro indirizzo IP a due NIC, di cui una è inattiva.  
Se un indirizzo alfanumerico è mappato a più di un indirizzo IP, allora è responsabilità dell'host di origine scegliere quale sia il migliore, basandosi o sulla casualità o sulla velocità.

### 4.3.4 Indirizzamento IPv4

Storicamente (anni '80), IPv4 ha suddiviso i suoi 2^32 indirizzi in cinque diversi blocchi, o classi, ciascuno per scopi differenti.
![[Pasted image 20241004162719.png]] L'indirizzo IP era diviso in tre parti: **netID**, **subnetID** e **hostID**, con il **netID** dipendente dalla classe della rete. 

Si osservò presto che questa architettura era troppo complicata e inefficiente (le tabelle di routing sarebbero diventate troppo lunghe), quindi nel 1993 furono sostituite dal **Classless Inter-Domain Routing (CIDR)**.  
La notazione CIDR, che assume la forma **x.x.x.x/y**, elimina la distinzione tra **netID** e **subnetID**, e si costruisce da un indirizzo IP, un carattere slash ('/') e un numero decimale.

Il numero finale è il conteggio dei bit iniziali a 1 (quelli rilevanti per il processo di routing) nella *subnet mask*. Questa notazione consente l'unione di indirizzi che differiscono per il loro bit meno significativo. 
Nota che il numero di bit di una maschera non è necessariamente un multiplo di un byte (questo effettivamente complica le cose se osserviamo l'indirizzo nella sua forma canonica).  
Se vogliamo verificare se due indirizzi sono nella stessa subnet (equivalentemente, se possono essere raggiunti direttamente tramite l'indirizzo MAC), allora controlliamo se le loro parti di rete (quelle specificate dal numero di bit nella maschera) sono identiche.

**Esempio**: Gli indirizzi **150.217.8.0/24** e **150.217.9.0/24** differiscono solo per il loro **Least Significant Bit (LSB)**, quindi sono uniti per formare l'indirizzo **150.217.8.0/23**.  
**Esempio**: **192.168.100.14/24** rappresenta l'indirizzo IPv4 **192.168.100.14** e il suo prefisso di routing associato **192.168.100.0** o, in modo equivalente, la sua subnet mask **255.255.255.0**, che ha 24 bit iniziali a 1.  

Una maschera a 32 bit identifica un singolo host e avrebbe una subnet mask pari a **255.255.255.255**, mentre maschere a 24 bit o meno, come **255.255.255.0**, identificano reti: il blocco **192.168.100.0/22** rappresenta i 1024 indirizzi IPv4 da **192.168.100.0** a **192.168.103.255**. 

**Tabella di routing**  
Una **tabella di routing** è una tabella di dati memorizzata in un router o in un host di rete che elenca le rotte verso destinazioni di rete specifiche e le metriche (distanze) associate a tali rotte.
La tabella di routing contiene informazioni sulla topologia della rete circostante.  
Nella sicurezza di rete è piuttosto importante, poiché uno dei modi più semplici per ingannare gli utenti è controllare e sfruttare la loro tabella di routing.

La tabella di routing contiene almeno i seguenti campi di informazione:
- **destinazione**: l'indirizzo IP di destinazione, che può essere abbinato alla *netmask*;
- **netmask o genmask**: la subnet mask che, quando usata insieme alla destinazione, fornisce l'ID della rete finale, necessario per il routing;
- **gateway**: chiamato anche "next hop" (prossimo salto), è l'indirizzo della prossima stazione a cui inviare il pacchetto sulla strada verso la sua destinazione finale. Questo è l'interfaccia di uscita utilizzata per inviare pacchetti all'esterno. Un asterisco accanto ad esso indica che è direttamente raggiungibile tramite l'interfaccia corrente, il che significa che i pacchetti non devono passare attraverso il router (altrimenti i pacchetti saranno inviati prima al router (gateway));
- **metrica**: la metrica di routing del percorso attraverso il quale il pacchetto deve essere inviato; la rotta andrà nella direzione del gateway con la metrica più bassa.

A seconda dell'applicazione e dell'implementazione, può contenere anche valori aggiuntivi che affinano la selezione del percorso:
- **interfaccia**: identifica la NIC associata all'ID della rete corrispondente (ad esempio, eth0 per la prima scheda Ethernet, eth1 per la seconda scheda Ethernet, ecc.);
- **flags QoS**: qualità del servizio associata alla rotta (ad esempio, il flag "U" indica che una rotta IP è attiva);
- **criteri di filtraggio**: liste di controllo degli accessi associate alla rotta.

La voce **default** è un'entrata unica nella tabella di routing che indica il percorso predefinito (0.0.0.0) e il gateway predefinito (che viene utilizzato quando non esiste una rotta specifica nella tabella per un indirizzo di rete di destinazione).  
Se due destinazioni hanno lo stesso gateway (e la stessa interfaccia), vengono unite, e la netmask viene modificata di conseguenza.

Poiché non possiamo ordinare la tabella di routing in modo logico, per trovare la destinazione di un pacchetto dobbiamo trovare la migliore corrispondenza nella tabella di routing. 

Se l'equazione "destIP && mask_i == destIP_i"  è vera ovvero un AND bit a bit tra l'indirizzo di destinazione e la netmask, che dovrebbe essere uguale alla destinazione alla riga i, allora l'elemento i ha un punteggio pari al numero di bit a 1 di **mask_i**; dopo aver eseguito questa operazione per tutte le voci, scegliamo quella con il punteggio più alto.
![[Pasted image 20241004171632.png]]
**Esempio**: La Figura mostra un estratto da una tipica tabella di routing di un computer. La destinazione **192.168.21.0** e la netmask **255.255.255.0** possono essere scritte come networkID **192.168.21.0/24**. Questa particolare tabella di routing non ha voci per la rete **192.168.16.0**: se riceve pacchetti indirizzati a questa rete, li invierà tramite il gateway predefinito.

In generale, chi ha il numero maggiore di bit corrispondenti vince: supponiamo di voler instradare qualcosa verso **10.8.0.2**. Abbiamo due righe che corrispondono a questo indirizzo nella colonna della destinazione: **10.8.0.2** (fa corrispondenza per 32 bit) e **10.8.0.0** (corrisponde per 24 bit). Il primo di questi indirizzi vince ed è scelto.
### 4.3.5 Interconnessione e trasferimento dati

I dati vengono scambiati tra nodi adiacenti come mostrato nella Figura(qui mostrato secondo il protocollo ISO/OSI); i nodi intermedi non dovrebbero aver bisogno di elaborare informazioni end-to-end (ad eccezione di gateway e proxy).
![[Pasted image 20241005165847.png]]

Per inviare dati, l'host sorgente segue questi passaggi:
1. Crea un pacchetto indirizzato all'host di destinazione.
2. Controlla se l'host di destinazione si trova nella stessa subnet dell'host sorgente guardando l'indirizzo IP (L3) di destinazione:
    - Se è nella stessa subnet, l'host sorgente utilizza i meccanismi specifici della subnet per raggiungerlo;
    - Se non lo è, l'host sorgente invia il pacchetto a un router appropriato nella propria subn (quella dell'host sorgente).
3. La rete sottostante si occupa del resto (la traduzione degli indirizzi avviene qui, poiché questo passaggio richiede un indirizzo MAC (L2)).

Nota che gli indirizzi alfanumerici sono già stati risolti e lavoriamo con gli indirizzi L3 (indirizzi IP) fin dall'inizio.

# Capitolo 5: IPv6

**Internet Protocol versione 6**, abbreviato IPv6, è la versione più recente del Protocollo Internet (IP). È stato sviluppato dall'Internet Engineering Task Force (IETF) per affrontare il problema, a lungo previsto, dell'esaurimento degli indirizzi IPv4 e ha l'obiettivo di sostituire completamente l'IPv4.

## 5.1 Storia dell'IPv6

La storia dell'IPv6 è iniziata quando è diventato evidente che, prima o poi, non sarebbero più stati disponibili indirizzi IPv4. In sintesi, è composta principalmente da persone che hanno riconosciuto che IPv4 era una cattiva idea, numerose previsioni contrastanti su quando si sarebbe esaurito il pool di indirizzi IPv4, e infine altre previsioni sul completo dispiegamento dell'IPv6 (che si sono rivelate così errate che, a questo ritmo, potremmo non vederlo mai completamente implementato durante la nostra vita, o qualcosa del genere). Segue una cronologia semplificata delle tappe più importanti nella vita di questo protocollo.

### 5.1.1 Esaurimento degli indirizzi IPv4

L'esaurimento degli indirizzi IPv4 si riferisce al termine del pool di indirizzi IPv4 non ancora assegnati. Poiché l'architettura originale di Internet disponeva di meno di 4,3 miliardi di indirizzi, l'esaurimento era stato previsto sin dalla fine degli anni '80, quando Internet iniziò a crescere in modo drammatico.  
Non tutti gli indirizzi IPv4 sono effettivamente utilizzati, poiché molti di essi sono stati acquistati da persone o aziende che non li usano realmente. Tuttavia, il loro esaurimento era comunque inevitabile a causa della crescita esplosiva di Internet, non solo per l'alto numero di persone che ora vi accedono, ma anche per i milioni di dispositivi connessi (come smartphone, IoT, ecc.).
![[Pasted image 20241007080924.png]]
Al giorno d'oggi (2020), gli indirizzi IPv4 sono esauriti; tuttavia, sono ancora ampiamente utilizzati, quindi cosa significa questo? Cerchiamo innanzitutto di capire chi sta utilizzando questi indirizzi.  
Per poter usare un indirizzo IP, dobbiamo possederlo, e non solo uno, ma un blocco di essi. Supponiamo di essere un'azienda che, per motivi legittimi, desidera avere i propri indirizzi. Andiamo a un registro regionale e richiediamo degli indirizzi; se ci sono IP disponibili, paghiamo un costo nominale (una piccola tassa per il funzionamento del registro) e otteniamo alcuni indirizzi per noi.  
Fino all'esaurimento, era possibile andare semplicemente a un registro e chiedere un blocco di indirizzi IP; ora, dobbiamo aspettare in coda per settimane o mesi per ottenere un nuovo blocco. Ma aspetta - non erano esauriti tutti gli indirizzi? Sì, ma no: alcune aziende che possedevano blocchi sono fallite, oppure alcune aziende hanno rilasciato vecchi blocchi, quindi possiamo ottenere nuovi indirizzi anche se non ci sono nuovi blocchi disponibili. In alternativa, potremmo anche chiedere a un'azienda sul mercato libero di venderci i loro indirizzi (Ad oggi vendere un blocco di indirizzi IPv4 risulta molto profittevole, visto la loro disponibilità e domanda sul mercato). 
Al contrario, se vogliamo indirizzi IPv6, basta inviare un'email al registro, e otterremo quanti ne vogliamo.

### 5.1.2 IPv6 Timeline

![[Pasted image 20241007081010.png]]

**1993**  
Dopo aver capito che il routing basato su classi era una cattiva idea, il CIDR (Classless Inter-Domain Routing) ritarda l'esaurimento degli indirizzi IPv4 assegnando blocchi più piccoli. Prima del CIDR, non era possibile assegnare più di 254 indirizzi di classe C (nemmeno due blocchi consecutivi di questa classe), quindi le persone che necessitavano di più IP dovevano ottenere un blocco di classe B, molto più grande. Il CIDR contribuisce anche a ridurre (drammaticamente) la dimensione delle tabelle di routing.

**1995**  
IPv6 viene ufficialmente rilasciato con l'RFC 1752. Nota che, ad oggi (2020), è un protocollo che ha 25 anni, quindi non proprio nuovo.

**1997**  
SURFNet, la rete accademica dei Paesi Bassi, passa completamente all'IPv6.

**1999**  
Vengono creati l'IPv6Forum e task force regionali per forzare l'adozione dell'IPv6; falliscono miseramente.

**2000**  
SixXS, uno dei più grandi broker di tunnel, inizia le sue operazioni, consentendo agli utenti di collegare i loro dispositivi alla rete IPv6 tramite esso.

**2003**  
Viene creato 6bone, un banco di prova IPv6 a livello mondiale. Giappone, Cina e Corea del Sud annunciano la loro volontà di diventare leader nell'adozione dell'IPv6, principalmente perché sono molto popolati e connessi a Internet.

**2004**  
La maggior parte dei nodi di rete (router) supporta l'IPv6.

**2005**  
Le cose iniziano a diventare più interessanti: il governo degli Stati Uniti richiede che tutte le agenzie federali migrino all'IPv6 entro il 2008 (e ci riescono). Allo stesso tempo, Sify, il più grande ISP dell'India, inizia a fornire connettività IPv6 agli utenti finali, a causa della sovrappopolazione. Inoltre, Tony Hain, di Cisco Systems, prevede che tra il 2009 e il 2016 diremmo addio all'IPv4 a causa dell'esaurimento degli indirizzi.

**2006**  
L'esperimento 6bone si conclude con successo.

**2008**  
Il DNS root può essere raggiunto anche tramite IPv6. Questo non è molto sorprendente, poiché il DNS non è altro che un database: non importa come inviamo una query, risponderà. Se chiediamo una traduzione di un indirizzo alfanumerico, risponderà con l'elenco degli indirizzi IPv4 e IPv6 corrispondenti a quell'indirizzo. Nello stesso anno, la Commissione Europea fissa un obiettivo: raggiungere il 25% della popolazione tramite IPv6 entro il 2010 (e fallisce miseramente, perché gli ISP non sono stati obbligati a farlo). Nel frattempo, la Cina utilizza IPv6 per coprire i Giochi Olimpici di Pechino; è il più grande utilizzo di IPv6 mai visto, e il passaggio da IPv4 è così indolore che nessuno ha notato nulla di diverso.

**2009**  
La dorsale UniFi passa a IPv6, insieme a un server DNS e a un server web.

**2010**  
Geoff Huston aggiorna le previsioni sull'esaurimento degli indirizzi IPv4, stimando una data tra settembre 2011 e maggio 2012. Che anche la fine del mondo sia prevista per lo stesso anno, secondo il calendario Maya, è solo una coincidenza. (O forse no...)

**2012**  
Il pool di indirizzi IPv4 è finalmente esaurito. Il mondo non finisce.

**2020**  
IPv6 è ancora in fase di implementazione – senza troppi problemi, ma anche senza sufficiente sicurezza (è estremamente problematico). Gli indirizzi IPv4 sono ancora disponibili, ma c'è una lista d'attesa.

## 5.2 IPv6 vs IPv4

Poiché IPv6 è la nuova versione del protocollo IP, i suoi obiettivi di progettazione sono risolvere i punti deboli di IPv4 e migliorare i suoi punti di forza. È molto diverso e, in definitiva, non correlato a IPv4, al punto che possono essere paragonati a due linee parallele che non si incontrano mai. Per questo motivo, possono essere utilizzati insieme senza interferire l'uno con l'altro (ma non saranno in grado di comunicare tra loro). Le principali differenze tra i due protocolli sono:

1. Uno spazio di indirizzi più grande (indirizzi a 128 bit per IPv6 rispetto agli indirizzi a 32 bit di IPv4);
2. I NAT sono scomparsi;
3. Intestazione (L'header) del pacchetto semplificata (drammaticamente più veloce);
4. Autoconfigurazione.

### 5.2.1 Spazio di indirizzi più grande

Supponiamo che il quadrato verde nella figura sottostante rappresenti lo spazio degli indirizzi IPv4; per confronto, lo spazio degli indirizzi IPv6 sarebbe rappresentato dallo spazio bianco attorno al quadrato verde, che, per mantenere le proporzioni, dovremmo estendere all'intero Sistema Solare. 
![[Pasted image 20241007081859.png]]
Un altro esempio: se supponiamo che un indirizzo IP abbia la forma di un granello di sabbia standard, misurando 1 mm x 1 mm x 1 mm, per creare lo spazio degli indirizzi IPv4 avremmo bisogno di quattro e mezzo secchi di sabbia. Per IPv6, avremmo bisogno di una quantità di sabbia sufficiente a coprire sei pianeti Terra (oceani inclusi) con 1 metro di sabbia.

Questa enorme quantità di indirizzi ci permette di fare qualcosa di impensabile in IPv4: sprecarli.

### 5.2.2 NAT

In IPv4, ogni host collegato a Internet deve avere un indirizzo unico per il routing. Se non è dietro un NAT (Network Address Translation), avrà un indirizzo pubblico e globale; altrimenti, un host situato in una subnet dietro un NAT avrà un indirizzo IPv4 che non sarà unico nella rete globale, quindi non sarà in grado di usarlo per il routing – in altre parole, l'host non potrà essere raggiunto direttamente dall'esterno.

Come suggerisce il nome, il NAT è una tecnica di manipolazione degli indirizzi IP (una sorta di riscrittura di un indirizzo IP) utilizzata per consentire a più host di condividere lo stesso indirizzo pubblico. Fondamentalmente, dal punto di vista di qualcuno fuori dalla rete, qualsiasi quantità di host dietro un NAT apparirà come ==un singolo indirizzo IP==.

Il NAT consente a un indirizzo IP privato di accedere a Internet, ma non viceversa – almeno non in modo prevedibile: i NAT non sono deterministici, quindi non è prevedibile se qualcuno da Internet può raggiungere un host dietro uno di essi. È anche possibile aggirare un NAT, anche se attraverso protocolli complessi, difficili, pericolosi o instabili.

**Esempio**: L'applicazione PS Remote Play, che consente a un utente di giocare a distanza sulla propria console PlayStation, utilizza tecniche che le permettono di aggirare il NAT per raggiungere direttamente la console – ciò apre enormi falle di sicurezza, simili a creare un buco nella porta principale di una casa.

Vale la pena notare che potremmo essere dietro un NAT anche se abbiamo un indirizzo IP pubblico, perché a volte gli ISP utilizzano NAT su larga scala (LSN -> Large Scale NAT), macchine molto costose e inaffidabili.

In breve, i NAT sono qualcosa di incredibilmente complesso e in definitiva inutile, poiché non hanno impedito l'esaurimento degli indirizzi IPv4 limitando il numero di dispositivi direttamente connessi a Internet; erano anche dannosi per la sicurezza. È quindi un aspetto molto positivo che non esistano più in IPv6.

### 5.2.3 Intestazione semplificata

È possibile apprendere e dedurre molte informazioni dall'intestazione di un pacchetto. I protocolli consentono la comunicazione tra i livelli; la loro implementazione risiede nell'intestazione: è l'intestazione che trasporta le informazioni, quindi ricordarla significa implicitamente conoscere cosa fa un protocollo e se può o non può fare qualcosa.

![[Pasted image 20241007082712.png]]

Come mostrato nella figura, l'intestazione di IPv6, con i suoi 320 bit (A differenza di IPv4 che sono almeno 160 --> lunghezza variabile), contiene le seguenti informazioni: 
– **Versione** (4 bit): valore costante uguale a 6 (sequenza di bit 0110);
– **Classe di traffico** (6+2 bit): i bit di questo campo contengono due valori che svolgono la stessa funzione del corrispondente campo di IPv4. I primi sei bit contengono il campo DS (Differentiated Services), utilizzato per classificare i pacchetti, mentre i rimanenti due bit sono utilizzati per l'ECN (Explicit Congestion Notification). 
In altre parole, questo campo specifica il tipo di pacchetto, come la sua priorità, se deve essere messo in coda o meno, se deve seguire un certo percorso ecc...
– **Etichetta del flusso (Flow label)** (20 bit): un flusso è un gruppo di pacchetti, ad esempio una sessione TCP o un flusso multimediale; l'etichetta di flusso speciale 0 significa che il pacchetto non appartiene a nessun flusso.
Si noti che mentre le porte TCP consistono in sequenze di 32 bit (16 + 16 bit), questo campo ha solo 20 bit: questo perché tale numero è stato considerato sufficiente per etichettare correttamente i pacchetti. Questo campo è molto efficiente e consente di identificare i pacchetti tramite una semplice operazione XOR; 
– **Lunghezza del payload** (Payload length) (16 bit): dimensione del payload, inclusi eventuali header di estensione; 
– **Header successivo** (Next header) (8 bit): specifica il tipo di header successivo, solitamente il protocollo del livello di trasporto utilizzato dal payload di un pacchetto. Quando nel pacchetto sono presenti header di estensione, questo campo indica quale header di estensione segue.
I valori sono condivisi con quelli utilizzati per il campo protocollo di IPv4, poiché entrambi i campi hanno la stessa funzione;
– **Limite di hop** (Hop limit) (8 bit): sostituisce il campo di durata di vita (time to live) di IPv4. Questo valore viene decrementato di uno in ogni nodo di inoltro e il pacchetto viene scartato se diventa 0. Tuttavia, il nodo di destinazione dovrebbe elaborare il pacchetto normalmente anche se ricevuto con un limite di hop pari a 0;
– **Indirizzo di origine** (Source address) (128 bit): indirizzo IPv6 del nodo di invio; 
– **Indirizzo di destinazione** (Destination address) (128 bit): indirizzo IPv6 del nodo o dei nodi di destinazione.

+Riassumendo le caratteristiche più importanti dell'header IPv6 sono:

– **Lunghezza fissa** (40 byte, o 320 bit); 
– Niente più controllo degli errori (IPv4 aveva un checksum solo per l'header, che doveva essere controllato in ogni nodo, rallentando il routing); 
– Niente più frammentazione (almeno non nell'header stesso); 
– Estensioni dell'header: non è sbagliato dire che IPv6 potrebbe includere anche informazioni di livello 4 (porte) nell'header, rendendo più complessa la traduzione; la differenza rispetto a IPv4, tuttavia, risiede nel fatto che sappiamo esattamente dove trovare queste informazioni, rendendo l'operazione estremamente semplice. Il processo funziona così: dopo aver letto i primi 40 byte di un pacchetto, il router controlla se l'header successivo contiene tutti zeri; se trova qualcosa di diverso da uno zero (un 1), significa che c'è una o più estensioni hop-by-hop che devono essere ulteriormente elaborate;

![[Pasted image 20241007085122.png]]
--> Di solito non sono presenti estensioni di header, ma se richiesto (dai nodi intermedi o dalla destinazione) uno handling speciale, l'host che invia il pacchetto aggiunge uno o più header di estensione. Più header di estensione formano una catena di puntatori fino a che l'ultimo protocollo di rete è definito.

– Migliore supporto per i tag QoS(Quality of Service), grazie all'etichetta di controllo del flusso; 
– **IPSec** nativo: le specifiche IPv6 richiedono che ogni host che utilizza IPv6 implementi anche IPSec (tecniche di encription dei pacchetti), ma in realtà si tratta di un protocollo molto complesso con una gestione delle chiavi altrettanto complessa (in parole povere, un incubo), quindi pochissimi sistemi lo utilizzano effettivamente;
– **IPv6 mobile** notevolmente semplificato, poiché mantiene il vecchio indirizzo IP anche su una nuova rete, il che significa che la connessione non verrà interrotta. Con IPv6 mobile si intende la possibilità per un device di fare lo switch da una rete ad un altra (ad esempio da 3G a 4G) senza perdere la connessione perchè l'indirizzo IP cambia. 
--> in ISO/OSI ciò non potrebbe accadere, siccome indirizzi appartenenti a layer diversi sarebbero logicamente separati, il layer di session avrebbe questo problema.

### 5.2.4 Autoconfigurazione

Questo è il punto di forza di IPv6, che non deve mai essere sottovalutato per motivi di sicurezza, poiché più un sistema è facile da usare, più può essere pericoloso.

L'idea dell'autoconfigurazione di IPv6 è quella di collegare semplicemente il cavo e far funzionare tutto automaticamente (plug & play), senza l'intervento dell'utente. 
Questo comportamento si basa principalmente sull'auto-negoziazione degli indirizzi IP che, a differenza di IPv4, viene eseguita senza l'aiuto di DHCP (anche se può ancora essere utilizzato in IPv6).
--> Il DHCP è un protocollo internet usato sulle reti IP dove un server DHCP assegna in modo automatico un indirizzo IP e altre informazioni (ovvero la subnet mask, il gateway di default, il DNS (domain server name) e altri parametri di configurazione), ad ogni host presente sulla rete in modo tale che possono comunicare in modo efficente con gli altri endpoints. Si riducono così i possibili errori che possono essere causati dall'assegnare indirizzi IP manualmente. Inoltre limita il tempo di quanto un device può tenere un personale indirizzo IP 

## 5.3 Indirizzamento IPv6

Lo spazio degli indirizzi IPv6 è così vasto che è necessario un nuovo schema di indirizzamento. I due RFC che lo definiscono sono:

- **RFC 4291**: definisce lo schema di indirizzamento IPv6;
- **RFC 3587**: definisce il formato degli indirizzi unicast globali IPv6.

Gli indirizzi IPv6 sono scritti utilizzando il formato esadecimale (base 16). 
Una scheda di rete IPv6 ha sempre diversi indirizzi IPv6.

Esistono molti tipi di indirizzi IPv6:
- **unicast**: indirizzo one-to-one, che può essere di uno dei seguenti tipi:
    - **globale**: il suo scope è l'intero Internet ed è unico;
    - **link-local**: è limitato all'ambito del link, il che significa che se due dispositivi si trovano sullo stesso link (ad esempio collegati allo stesso switch) avranno questo tipo di indirizzo, che potrebbe non essere unico. Inoltre, poiché dobbiamo definire il link, potrebbe esserci un indirizzo link-local per ogni interfaccia di rete connessa a un dato dispositivo. In una rete multi-hop, come una rete wireless, l'ambito del link è l'area di copertura radio della rete, quindi l'indirizzo link-local sarà valido solo tra un dispositivo e un altro raggiungibile entro un hop. In generale, se i dispositivi che stiamo considerando operano al livello 2 (ad esempio, hanno più switch), tutti gli host saranno nello stesso link. 
	- **site-local**: deprecato, utilizzato prima di ULA.
	- **unique local** (ULA): utilizzo estremamente limitato e specifico, poiché è simile agli indirizzi privati (ad esempio, viene utilizzato come soluzione temporanea nei casi in cui si sta configurando un indirizzo IPv6 ma non si dispone ancora di un prefisso valido);
	- compatibile con IPv4: deprecato;
	- **mappato su IPv4**: un indirizzo IPv6 che è stato mappato su IPv4; è pensato come una soluzione per la transizione a IPv6, sebbene non sia molto elegante.
	
- **multicast**: one-to-many, un indirizzo che consente a un dispositivo di comunicare con molti altri dispositivi contemporaneamente; viene utilizzato per quasi tutto; (non in IPv4)

- **anycast**: one-to-nearest; funziona in modo molto simile a un indirizzo unicast, tranne per il fatto che i dati vengono inviati all'host più vicino (quindi la destinazione viene decisa dal router). Possono esserci più dispositivi raggiungibili globalmente alla stessa distanza. Anycast è ampiamente utilizzato per i prodotti di Content Delivery Network (CDN, una rete distribuita geograficamente di server proxy e i loro data center) per avvicinare i loro contenuti all'utente finale, poiché è molto più efficiente rispetto a controllare un elenco di indirizzi IPv4 per scoprire quale sia il più vicino. 
 
Non esiste un indirizzo broadcast, perché il multicast è molto più potente.

### 5.3.1 Formato dell'indirizzo IPv6

Il formato preferito per un indirizzo IPv6 globale di 16 byte è mostrato nel seguente esempio (forma estesa e compatta):
![[Pasted image 20241010224505.png]]
La **forma compatta** mostrata sotto quella completa omette tutti gli zeri iniziali, mantenendo solo i due punti per evitare ambiguità nella lunghezza dell'indirizzo.

Esiste anche una **rappresentazione letterale** che utilizza parentesi quadre e può essere utilizzata per inserire l'indirizzo in, ad esempio, un indirizzo HTTP (proprio come possiamo fare con un indirizzo IPv4):  
![[Pasted image 20241010224859.png]]

**Esempio**  
Un uso curioso dei prefissi IPv6, e un buon esempio di come possiamo dire che lo spazio degli indirizzi IPv6 è così grande che possiamo permetterci di sprecare effettivamente degli indirizzi, è il "Debate Prefix" o 2001:DB8::/32. 
Questo è un prefisso di indirizzo utilizzato solo a scopo di documentazione, quindi gli indirizzi che iniziano con questo prefisso non possono essere instradati (i router scartano automaticamente i pacchetti che li contengono come destinazioni). Si noti che ci sono 2^96 indirizzi riservati solo a questo scopo: uno spreco significativo di indirizzi. Nonostante ciò, questo prefisso è necessario per evitare la configurazione errata delle reti (anche a livello di ISP) creata da persone che copiano e incollano esempi senza cambiare gli indirizzi IP. 

### 5.3.2 Prefissi degli indirizzi IPv6

I prefissi attualmente allocati dallo IANA (Internet Assigned Numbers Authority) sono:

- ::/128 (tutti zeri): non specificato (solo per casi speciali);
- ::1/128: loopback (non c'è posto come casa ::1/128);
- 2000::/3: indirizzi unicast globali (RFC 4291); gli indirizzi anycast sono allocati dai prefissi unicast, quindi sono indistinguibili;
- FC00::/7: unicast locale unico, quasi mai utilizzato (al loro posto vengono utilizzati gli indirizzi link-local) (RFC 4193);
- FE80::/10: unicast link-local (RFC 4291);
- FF00::/8: multicast (RFC 4291);
- 64:FF9B::/96: indirizzo IPv4 mappato su IPv6 (RFC 6052).

### 5.3.3 Indirizzi link-local

Per ottenere un indirizzo unicast globale, dobbiamo conoscere alcuni dati sulla rete a cui ci stiamo unendo. Al contrario, l'indirizzo unicast link-local non richiede di conoscere nulla in particolare, poiché viene utilizzato sul link locale: questo tipo di indirizzo viene utilizzato durante l'autoconfigurazione, anche quando non sono presenti router.
![[Pasted image 20241011083142.png]]
Come mostrato in figura, i primi 10 bit di un indirizzo link-local sono sempre FE80, mentre i successivi 54 bit sono riempiti con zeri (potrebbero anche essere uno, sarebbe comunque valido). La seconda parte, composta dai restanti 64 bit, è riempita con l'ID dell'interfaccia, che deve essere univoco (ogni dispositivo deve avere un ID dell'interfaccia diverso).

**ID dell'interfaccia**  
Il modo più semplice per ottenere un ID dell'interfaccia univoco è utilizzare l'indirizzo MAC del dispositivo, poiché sullo stesso link deve essere unico per ogni NIC, e quindi possiamo usarlo per costruire un indirizzo di livello 3.

Tuttavia, l'ID dell'interfaccia può anche essere creato in altri modi. Ad esempio, se abbiamo un indirizzo MAC più corto (come nelle reti Ethernet o WiFi), dovremo espanderlo a 64 bit, creando così un indirizzo EUI-64.

Potremmo anche generare indirizzi utilizzando DHCPv6 (leggermente più complesso di DHCPv4 a causa del modo in cui gli host vengono identificati), configurarli manualmente o generarli con numeri pseudocasuali (in questo caso la probabilità che due host selezionino gli stessi numeri è estremamente bassa).

Possiamo anche generarlo in modo più creativo, come nel caso delle CGA (Cryptographically Generated Address), che sono generate utilizzando i 64 bit della firma crittografica dei nostri pacchetti dati.

Altri metodi includono praticamente qualsiasi cosa che possa essere utilizzata per generare un indirizzo ragionevolmente ==unico==; dobbiamo tuttavia assicurarci di controllare sempre tutto, per sicurezza.

![[Pasted image 20241011083511.png]]
Esempio di come un indirizzo MAC a 48bit venga mappato in quello di IPv6
--> Ad esempio da 00:1F:5B:39:67:3C a **02**1F:5B**FF**:**FE**39:673C
### 5.3.4 Interfacce IPv6

Ogni host (computer) con almeno una scheda di rete (NIC) ha almeno tre indirizzi IPv6:

- **loopback** (::1/128): l'equivalente IPv6 dell'indirizzo localhost in IPv4, assegnato a una scheda di rete virtuale chiamata loopback;
- indirizzo **unicast link-local** (FE80:::::): ogni indirizzo MAC configurato per ogni NIC ha il proprio indirizzo link-local;
- **unicast globali**: assegnati in qualche modo, potrebbe essercene più di uno per dispositivo;
- **multicast all-nodes** (FF02::1): il dispositivo potrebbe rispondere anche a uno o più indirizzi multicast, che sono l'equivalente di un indirizzo broadcast in IPv4;
- **multicast all-routers** (FF02::2): i router hanno anche un indirizzo multicast all-routers;
- indirizzo **multicast solicited-node** (FF02::1:FF00:0000/104): il cuore e la causa dell'autoconfigurazione. Questo indirizzo è un indirizzo multicast IPv6 valido all'interno del link locale ed è utilizzato nel Neighbor Discovery Protocol per ottenere gli indirizzi di livello 2 (livello di collegamento) di altri nodi. Un indirizzo multicast solicited-node viene creato prendendo gli ultimi 24 bit di un indirizzo unicast o anycast e aggiungendoli al prefisso FF02::1:FF00:0/104. Usiamo un gruppo multicast solicited invece del gruppo all-nodes perché il gruppo all-nodes potrebbe essere troppo numeroso e potrebbe essere costantemente interrogato da qualcuno che si unisce alla rete riducendo notevolmente l'efficienza; utilizzando indirizzi multicast di solicited-node, limitiamo il target a un sottoinsieme molto piccolo di nodi.
Nota che, utilizzando indirizzi diversi per specificare le capacità di alto livello di un nodo, trasferiamo in realtà funzioni del livello 7 (applicazione) ai livelli 2 e 3: una violazione del principio di separazione delle occupazioni.

**Esempio**: se vogliamo raggiungere una stampante, utilizziamo un indirizzo multicast di tutte le stampanti, il che è ottimo perché non dobbiamo chiedere a ogni singolo nodo se supporta uno dei (numerosi) protocolli supportati dalle stampanti; invece, inviamo un solo pacchetto e raggiungiamo tutte contemporaneamente. Lo stesso vale per trovare un server DHCP: inviamo un pacchetto a un indirizzo multicast di tutti i DHCP e raggiunge solo i nodi che implementano il DHCP.

**Gruppi multicast IPv6**
Cosa significa unirsi a un gruppo multicast? 
Supponiamo di volerci unire a un gruppo FF02: dobbiamo solo istruire il nostro livello IP affinché i pacchetti che hanno tale indirizzo come destinazione non vengano scartati, ma passati dal livello IP stesso verso i livelli superiori (Gli altri invece sono scartati).
Questo è il motivo per cui gli indirizzi multicast sono più efficienti dei broadcast: i pacchetti verranno scartati prima nello stack, dai nodi che non sono router; qualsiasi nodo può inviare pacchetti a un gruppo multicast, ma quelli che non fanno parte del gruppo scarteranno i pacchetti a livello IP (nel kernel, in modo più veloce). 
In altre parole, IPv6 utilizza l'indirizzo di broadcast a livello 2, quindi se ci uniamo a un ambito link-local, dobbiamo solo ottenere l'indirizzo IPv6 a cui stiamo inviando i dati, dire al livello 2 di trasformarlo in un indirizzo MAC e poi inviarlo. Al contrario, in IPv4 l'indirizzo di broadcast (un indirizzo IP/livello 3) è mappato a un indirizzo di livello 2, il che significa che ogni nodo lo riceverà; uno switch invierà un pacchetto broadcast a tutte le porte e tutte le NIC lo inoltreranno al livello IP.

È chiaro quindi che il nodo non ha bisogno di nulla per unirsi a un gruppo multicast. A seconda del bit 02, potrebbe non dover nemmeno avvisare nessuno: l'indirizzo multicast IPv6 ha un ambito (raggiungibilità) definito da quel bit, il che significa che mentre 01 è locale all'interfaccia (il pacchetto non uscirà nemmeno dalla NIC), 02 ha ambito link-local.
Altri ambiti multicast sono *realm*-, *admin*-, *site*-, e *località dell'organizzazione*; questi non sono su un link, quindi i pacchetti passeranno attraverso i router e, unendosi a uno di questi gruppi, dovremo informare il router che facciamo parte di quel gruppo.
In generale esistono una sacco di tipi di indirizzi multicast, e potremmo definirne anche altri di questi...
### 5.3.5 Autoconfigurazione (ancora)

L'autoconfigurazione è molto semplice e molto vulnerabile. Abbiamo visto come leggere gli indirizzi IPv6 e che ci sono più classi di indirizzi IPv6 (le più importanti sono global, link-local e multicast).
Per comprenderla meglio, vedremo come funziona in pratica.

Per qualsiasi nodo, l'autoconfigurazione può essere riassunta nei seguenti passaggi:
1. Costruire l'ID dell'interfaccia (ID del nodo, con uno dei metodi visti in precedenza);
2. Unirsi al gruppo di indirizzi multicast solicited-node e inviare un messaggio DAD (Duplicate Address Detection); il DAD non viene inviato con l'indirizzo di origine del nodo, poiché non sa ancora se può usarlo, quindi utilizza un indirizzo non specificato (tutti zeri) come sorgente. Il nodo quindi attende una risposta fino alla scadenza di un timeout; chiunque stia già utilizzando quell'indirizzo deve rispondere alla richiesta DAD, mentre se il nodo non riceve nulla, assumerà che l'indirizzo scelto sia sicuro da usare (riconoscimento implicito);
3. Si inizia a utilizzare l'indirizzo link-local per verificare la presenza di Router Advertisements (RA), i messaggi ICMP (Internet Control Message Protocol, ovvero protocollo usato dalle reti di devices per mandare messaggi di errore e di operazione che indicano il successo/fallimento quando si comunica con un altro indirizzo IP) sono periodicamente inviati al gruppo multicast di tutti i nodi dai router (una sorta di funzione "sono ancora attivo");
4. Si costruisce un indirizzo unicast globale: se non c'è DHCP, gli RA contengono un PIO (Prefix Information Object) che indica al nodo quale prefisso può usare per costruire un indirizzo globale; altrimenti, gli RA contengono un flag che indica che il nodo deve fare affidamento sul DHCP per ottenere un indirizzo globale (il che porta a utilizzare un gruppo multicast di tutti i DHCP). Gli RA contengono anche il DNS;
5. Inviare un altro DAD , per controllare la presenza di duplicati (solo se non c'è DHCP, altrimenti il nodo si fida che il DHCP gli abbia dato un indirizzo unico);
6. Impostare automaticamente un router predefinito (in IPv4 o te lo setta il DHCP, oppure lo devi fare manualmente)
7. Iniziare a navigare in Internet.

Il secondo passaggio del processo rappresenta un problema a più livelli, perché potrebbe esserci un nodo che utilizza l'indirizzo scelto ma risponde troppo tardi. Il valore ottimale per il timeout dovrebbe quindi essere un compromesso tra velocità e sicurezza, quindi dipende molto dalla topologia della rete; di solito, per Ethernet e WiFi non importa molto, perché le risposte saranno nell'ordine dei millisecondi, ma per sistemi a lunga distanza/del ritardo è molto importante.

Durante questo passaggio, il nodo assume anche implicitamente che il DAD (che è un pacchetto simile a UDP) sarà ricevuto da ogni nodo e che quindi la rete sia affidabile; in una rete con alta probabilità di perdita di pacchetti, questo sistema non è affidabile.

Ultimo ma non meno importante, il nodo assume anche che non ci siano attaccanti che potrebbero rispondere in modo anomalo. Tuttavia, se c'è effettivamente un attaccante nella rete, potrebbe facilmente impedire a un nodo di unirsi alla rete semplicemente unendosi a tutti i gruppi multicast solicited-node e rispondendo costantemente a chiunque tenti di unirsi che l'indirizzo IPv6 che vorrebbero utilizzare è già stato rivendicato. Se non ci sono malintenzionati in giro, allora il nodo inizierà a utilizzare il proprio indirizzo link-local.

**Esempio**: supponiamo di avere un'interfaccia con l'indirizzo IP FE80::2AA:FF:FE28:9C5A. Poiché un indirizzo multicast solicited-node viene creato prendendo gli ultimi 24 bit di un indirizzo unicast o anycast e aggiungendoli al prefisso FF02::1:FF00:0/104, l'indirizzo multicast solicited-node associato è FF02::1:FF28:9C5A. Nota come, avendo preso 104 bit dall'indirizzo, l'ultimo byte del campo penultimo 00 non viene utilizzato nel prefisso.

È interessante notare che il prefisso dell'indirizzo multicast solicited-node FF02 viene utilizzato anche nell'autoconfigurazione per gli indirizzi multicast globali; un sottoinsieme di 24 bit dell'indirizzo originale è comunque abbastanza grande da avere una probabilità estremamente bassa di ottenere una risposta DAD, anche da qualcuno con un indirizzo molto simile.

Il DNS di solito si ottiene tramite l'RA, ma si può ottenere anche:
- Dallo stack IPv4, se esiste un dual-stack
- Configurato manualmente (cattiva idea)
- Dal DHCPv6
Nota che nelle vecchie macchine o negli stack IP fatti a mano dobbiamo controllare due volte che hanno conoscenza degli RA oppure dei DHCP con DNS, altrimenti i nostri device apparentemente funzionano ma non saranno capaci di risolvere il conflitto di indirizzi. 

**Attacchi all'autoconfigurazione**  
Cosa succede se un attaccante riesce a entrare in questo processo? Totale panico: non c'è modo di evitarlo. Gli attacchi più pericolosi sono quelli sulla stessa rete, dove si presume generalmente che nessun attaccante possa avvicinarsi così tanto alla vittima. Alcune persone hanno proposto di proteggere i messaggi sulla stessa rete con un protocollo crittografico, ma questo andrebbe contro l'autoconfigurazione, poiché richiederebbe che ogni dispositivo che può unirsi alla rete sia già configurato per quella rete (dato un segreto). In breve, o abbiamo l'autoconfigurazione, o ci proteggiamo dagli attaccanti: è una coperta corta.

**IPv6 rispetto a IPv4**  
In generale, dobbiamo dimenticare molti concetti legati a IPv4, perché sono completamente sbagliati in IPv6. Ad esempio, in IPv6 non esiste una netmask, perché l'indirizzo è semplicemente diviso tra una parte di rete (che è sempre lunga 64 bit) e la parte dell'interfaccia di rete (composta dagli altri 64 bit), quindi non possiamo mai avere sottoreti di lunghezze e dimensioni diverse.  
Un altro esempio è la richiesta di vicinato(*neighbour solicitation*): mentre in IPv4 è abilitata quando due host condividono la parte di rete, questo non è sempre vero in IPv6, perché quando un nodo ha un pacchetto unicast da inviare a un vicino ma non conosce il suo link-layer address, esegue la risoluzione dell'indirizzo.  

Si noti che in IPv6 i vicini sono nodi collegati alla stessa rete, che è definita come una struttura o un mezzo di comunicazione attraverso il quale i nodi possono comunicare a livello di collegamento dati, ovvero il livello immediatamente inferiore all'IP. Ciò significa che tutto dipende dalla topologia fisica del livello 2, non da qualcosa che possiamo dedurre dall'indirizzo IP.  

L'unico concetto che rimane valido è "on-link", che non si basa sull'indirizzo IP. Tuttavia, mentre in IPv4 due indirizzi sono nella stessa sottorete se condividono la stessa parte di rete (e quindi sono collegati da uno switch o un altro sistema di livello 2 e non necessitano di un router), in IPv6 non possiamo mai dedurre da due indirizzi IP se sono collegati allo stesso switch, se c'è un router in mezzo e/o se possono comunicare direttamente, anche se si inviano ping a vicenda.
La proprietà "on-link" non è una conseguenza della condivisione dello stesso prefisso.

Esempio  

![[Pasted image 20241011180459.png]]

Consideriamo la rete mostrata nella figura: i dispositivi A e B sono sulla stessa rete ma hanno prefissi di indirizzo IP diversi, mentre A e C sono su reti diverse ma hanno gli stessi prefissi.  
In IPv4, i dispositivi A e B non sarebbero in grado di comunicare, perché i loro indirizzi non hanno lo stesso prefisso. Inoltre, avere A e C con lo stesso prefisso o la stessa parte di rete su due lati diversi (interfacce fisiche) del router creerebbe un conflitto drammatico: il router sarebbe piuttosto infelice; è possibile, ma solo se si hanno ottime competenze e si costruisce la tabella di routing in modo molto specifico, non solo sul router, ma anche su A e C - fondamentalmente, sarebbe una cattiva idea.

In IPv6, viceversa, non solo la rete nella figura è legale, ma tutti i dispositivi potranno anche comunicare tra loro: A e B perché sono sullo stesso link (collegati dallo switch S), mentre A e C perché sanno di essere collegati allo stesso router. È il router che, nel suo Router Advertisement (RA), comunica al link A-B che sono sullo stesso link (collegati dal router stesso), tramite un prefisso e un bit on-link che, se impostato, permette a ogni host di assumere che qualsiasi altro host che condivide lo stesso prefisso sia sullo stesso link (come avviene in IPv4). Se il bit on-link non è impostato, nessun host assumerà mai che una determinata destinazione sia sullo stesso link, a meno che il router non lo comunichi diversamente.

Supponiamo ora che A voglia inviare un pacchetto a C; poiché A non presume che C sia sullo stesso link, lo invierà al router, che lo inoltrerà a C. C farà lo stesso. Se anche A e B seguissero questa procedura, sarebbe subottimale: ogni pacchetto passerebbe attraverso il router, mentre potrebbe semplicemente andare da A a B (e viceversa) direttamente, dato che si trovano sullo stesso link.

Supponiamo ora che ci sia un altro host D, con l'indirizzo IPv6 2001:db8:f00d::6616, sullo stesso lato di C; in questo caso A invierà i suoi pacchetti al router, che li inoltrerà a D, e D farà lo stesso con i pacchetti destinati ad A. Anche questo sarebbe subottimale, poiché i dati dovrebbero passare attraverso il router.
### 5.3.6 ICMP redirect

Abbiamo detto prima che l'autoconfigurazione è un punto molto delicato di IPv6. La verità è che esiste un'altra vulnerabilità fenomenale in questo protocollo, ed è l'ICMP (Internet Control Message Protocol) redirect.

Attraverso ICMP, il router può informare un dispositivo riguardo alla proprietà on-link di una destinazione, reindirizzando efficacemente i pacchetti.

**Esempio**  
Consideriamo di nuovo l'esempio visto prima.
Supponiamo che A invii un pacchetto a B attraverso il router. Il router inoltra il pacchetto a B e invia un messaggio (a B) dicendo che A è on-link, fornendo l'indirizzo MAC di A. Da quel momento in poi, A e B sapranno di essere sullo stesso link e, quindi, A invierà pacchetti direttamente a B, e viceversa.

Ora, supponiamo che B sia un router con un indirizzo leggermente diverso (un altro numero al posto del finale 100). Se A non sa che B è il router giusto, invierà un pacchetto al router principale; il router principale inoltrerà il pacchetto e invierà un messaggio ad A dicendo che il router designato è B, in modo che da quel momento in poi A invierà pacchetti direttamente a B.

L'esempio sopra spiega come funziona l'ICMP redirect; la vulnerabilità risiede nel fatto che se un attaccante si trova su un determinato link e falsifica messaggi di reindirizzamento, può dichiarare di essere il router per un determinato blocco di indirizzi e per qualsiasi host su Internet, bypassando così tutti i router dopo il primo pacchetto (perché gli host lavoreranno a livello di switch).

Il punto è che possiamo avere indirizzi completamente diversi che comunicano direttamente se un router (o qualcuno che si spaccia per esso) dice loro che sono sullo stesso link.

In breve, l'ICMP redirect è un meccanismo estremamente potente, ma anche molto pericoloso. Nonostante ciò, è drammaticamente utile e importante per configurare e mantenere una rete con più router e indirizzi, perché anche se potessimo filtrare (escludere) i suoi messaggi, sarebbe una pessima idea.

**Contromisure**  
Vista la grande vulnerabilità rappresentata dall'ICMP redirect, è necessario avere un piano di sicurezza. Ricorda che la sicurezza non consiste nel rendere le cose sicure, ma piuttosto nel definire cosa significhi sicurezza per noi - e farla diventare realtà.

I passaggi per raggiungere l'obiettivo di sicurezza devono seguire un percorso preciso:
- comprendere l'architettura aziendale e i suoi obiettivi;
- definire gli obiettivi di sicurezza che devono essere applicati (ad esempio, robustezza, operazioni failsafe e percentuali, interruzione ammessa, riservatezza, ecc.);
- analizzare le minacce, la probabilità di occorrenza e le capacità degli attaccanti;
- definire le contromisure;
- misurare l'efficacia.

Nel caso di IPv6, dobbiamo valutare se la rete link-local possa essere fisicamente accessibile da qualcuno che non è affidabile (per esempio, la rete di un'università non è affidabile perché alcune porte si trovano in stanze pubblicamente accessibili, come la porta Ethernet nella stanza delle stampe).

Una contromisura agli attacchi di ICMP redirect potrebbe essere il controllo di ciò che passa attraverso la rete, dal punto di vista fisico. Dovremmo verificare che il cavo di rete sia fisicamente sicuro (ad esempio, inserito in un tubo di ferro), per garantire che sia sempre integro e non possa essere toccato; potrebbero anche essere impiegati controlli elettrici periodici (una soluzione abbastanza comune) per garantire che non sia stato scollegato e ricollegato.

Potremmo anche controllare da dove proviene un pacchetto: contro qualcuno che finge di essere un router potremmo installare un controllo sullo switch per vedere su quale porta si trova il router e consentire messaggi RA solo da quella porta (significando che tutto il resto è un attaccante). Tuttavia, per fare ciò abbiamo bisogno di uno switch in grado di analizzare questo tipo di minaccia.
### 5.3.7 IPv6 Threat Model

Gli attacchi e le vulnerabilità a livello superiore non sono di nostra competenza, ma dovremmo sempre verificare eventuali falle nel software. Gli indirizzi IPv6 (e in particolare quelli mappati su IPv4), invece, possono (e lo faranno) sollevare vulnerabilità a livello di applicazione.

Rispetto a IPv4, IPv6 presenta alcuni attacchi simili, ma anche alcuni nuovi. Esistono molti attacchi IPv4 che non sono più applicabili a IPv6.

Ad esempio, l'attacco di frammentazione, possibile in IPv4, è impossibile in IPv6 - non perché IPv6 non abbia la frammentazione, ma perché in IPv6 l'header di estensione per la destinazione è end-to-end (solo la sorgente può frammentare i pacchetti): se troviamo un pacchetto malformato, possiamo facilmente assumere che o il mittente abbia avuto un problema o che il mittente sia un po' sospetto, quindi lo scartiamo![[Pasted image 20241012111224.png]].

La scansione della rete è praticamente impossibile in IPv6 se l'attaccante non si trova nella stessa rete, a causa delle enormi dimensioni dello spazio degli indirizzi - ciò significa anche che la rete è più difficile da controllare, però.

Un'altra cosa positiva è che i NAT non esistono più; tuttavia, poiché le reti hanno ancora bisogno di essere partizionate, IPv6 utilizza più firewall rispetto a IPv4. 

L'attacco ICMP redirect, viceversa, è un nuovo tipo di attacco che non era possibile in IPv4, mentre l'ARP spoofing è ancora presente, sebbene in una forma leggermente diversa. L'ARP spoofing è la situazione in cui un attaccante è in grado di far credere ad una determinata destinazione che sia qualcun'altro.

Il punto è che IPv6 non è stato creato per essere sicuro, ma solo per essere più facile da usare rispetto a IPv4; il fatto che sia stato progettato per essere più semplice per l'utente significa che è anche più facile da sfruttare per un attaccante. 
Il fatto che qualcosa sia stato certificato come sicuro (con un dato livello di sicurezza) in IPv4 non implica un livello di sicurezza simile in IPv6. Ovviamente, assumere che i sistemi siano simili in termini di sicurezza sia in IPv4 che in IPv6 sarebbe un errore gravissimo. Per questa ragione, poiché IPv4 e IPv6 sono completamente scollegati, per verificare se un software/protocollo è sicuro a livello 3 o - ancora più importante - a livello 7, è necessario effettuare un'analisi delle vulnerabilità, o vulnerability assessment (controllare perdite di memoria e altri problemi che sorgono dal fatto che gli indirizzi IPv6 sono più lunghi) per entrambi.

Ricorda: IPv6 non è più sicuro di IPv4; è semplicemente insicuro in modo diverso (inoltre, non abbiamo nemmeno molta esperienza con gli attacchi IPv6, quindi è più difficile renderlo sicuro).

Esempio: il toolkit di attacco IPv6 di THC include molti strumenti efficaci per attaccare IPv6; è disponibile all'indirizzo [https://github.com/vanhauser-thc/thc-ipv6](https://github.com/vanhauser-thc/thc-ipv6)

# Capitolo 6:  Il lato oscuro dei NAT

La **traduzione degli indirizzi di rete**, o NAT (Network Address Translation), è un metodo di rimappatura di uno spazio di indirizzi IP in un altro, modificando le informazioni di indirizzo di rete nell'header IP dei pacchetti mentre sono in transito attraverso un dispositivo di routing del traffico.
Questa tecnica è stata originariamente utilizzata come mezzo per mitigare l'esaurimento degli indirizzi IPv4, poiché un singolo indirizzo IP Internet di un NAT può essere utilizzato per identificare un'intera rete privata. Per questa caratteristica, il NAT viene spesso utilizzato anche per nascondere la struttura della rete interna, sebbene ciò non costituisca un vantaggio dal punto di vista della sicurezza.

In pratica, un NAT nasconde un intero spazio di indirizzi IP, di solito costituito da indirizzi IP privati, dietro un singolo indirizzo IP in uno spazio di indirizzi pubblici (quello del NAT). Gli indirizzi nascosti vengono modificati in un singolo indirizzo IP pubblico come indirizzo sorgente dei pacchetti IP in uscita, in modo che sembrino provenire non dall'host nascosto ma dal dispositivo di routing stesso.

Per far funzionare il NAT, alcuni indirizzi IPv4 sono stati dichiarati privati  (l'intervallo più utile è la classe C).
![[Pasted image 20241012114454.png]]
--> Spazio di indirizzi privati di IPV4
Essendo privati per definizione, questi indirizzi non possono essere utilizzati per il routing nelle reti pubbliche, poiché potrebbero essere (e di fatto sicuramente lo sono) duplicati.

Si noti che, sebbene il NAT esista sia per IPv4 che per IPv6, nell'IPv6 non è comunemente utilizzato, quindi da ora in poi si sottintenderà che ci si riferisce solo alla versione IPv4.
## 6.1 Classificazione del NAT

Possiamo definire tre tipi di NAT:

- **NAT statico** (mappatura 1:1): un singolo indirizzo nel pool privato viene direttamente tradotto nel pool pubblico, utilizzando una tabella senza stato; sostanzialmente inutile, poiché non risparmia indirizzi: servono tanti indirizzi globali quanti sono i dispositivi nella rete locale;
- **NAT dinamico**: mappa dinamicamente un indirizzo nella rete di area privata su un altro indirizzo dell'area esterna, il che significa che solo i dispositivi effettivamente attivi necessitano di un binding (una traduzione attiva); per questo motivo, necessita di una tabella con stato per tracciare quali dispositivi devono uscire dalla rete (e quali no);
- **NAPT, Network Address and Port Translation**: il sistema non solo cambia il numero IP, ma anche l'indirizzo di livello 4 (la porta TCP o UDP), il che significa che con un singolo indirizzo globale possiamo ospitare e mantenere circa 64.000 connessioni (connessioni, non host). In questo caso il sistema è molto più complesso, poiché deve tracciare le singole connessioni end-to-end (il flusso) tra i dispositivi nella rete privata e quella globale.

## 6.2 NAPT: Network Address and Port Translation

NAPT, Network Address and Port Translation, rappresenta il NAT effettivamente presente nella maggior parte delle reti private. Come brevemente spiegato nella sezione 6.1, è una variante del NAT dinamico che traccia i flussi.
Un flusso è identificato in TCP/IP (sia TCP che UDP) da una cinquina composta dal protocollo, dagli indirizzi IP di destinazione e sorgente e dalle porte di destinazione e sorgente. Possiamo differenziare due flussi in base a una variazione di uno qualsiasi di questi cinque elementi. Il protocollo, l'IP di destinazione e la porta non possono cambiare effettivamente, tranne per l'indirizzo e la porta sorgente che vengono modificati da un NAT.

### 6.2.1 NAT e crittografia

Timete Danaos et dona ferentes(ocho ai regali degli dei): il NAT viola il principio di non modifica di un pacchetto. Poiché cambia gli indirizzi IP e le porte, dovremo ricalcolare l'header e i checksum TCP/UDP, e i dati precedenti che avrebbero potuto consentirci di verificare se un pacchetto è stato manomesso non saranno più utilizzabili.
Per questo motivo, il protocollo IPsec non funziona in ambienti NAT: tutti i pacchetti verrebbero scartati a causa di un fallimento nel controllo di sicurezza.![[Pasted image 20241017195447.png]]
L'unico modo per fare un check dell'integrità del checksum mentre uso un NAT, è quello di farlo o dopo aver passato il NAT, oppure in una rete privata dietro NAT. 
Un alternativa, ma penalizzante in termini di efficenza è l'*IP-over-IP*, tecnica che encapsula un pacchetto IP in un altro pacchetto IP, in modo tale che due possiede due headers; potremmo addirittura fare *IP-over-TCP* ma alla fine ammazza tutte il processo di trasferimento dei dati.
### 6.2.2 Le basi del NAT ![[Pasted image 20241017201026.png]]
Come mostrato nella figura è anche compito del NAT modificare l'intestazione IP dei pacchetti in entrata per consegnarli ai destinatari previsti. L'intero processo è (di solito) completamente trasparente per l'utente e può essere riassunto come segue:
- Un pacchetto arriva nell'**interfaccia interna** del NAT:
    1. Cercare un'associazione (una traduzione); esiste?
	    - Sì: vai al passaggio successivo;
	    - No: creare un'associazione;
    2. Traduci il pacchetto;
    3. Inoltra il pacchetto.
- Un pacchetto arriva nell'**interfaccia esterna** del NAT:
    1. Cercare un'associazione (una traduzione); esiste?
	    - Sì: vai al passaggio successivo;
	    - No: scarta il pacchetto;
    2. Traduci il pacchetto;
    3. Inoltra il pacchetto.

**Bindings**
Un'associazione è una voce nella tabella NAT che lega un protocollo e un IP interni a un protocollo e un IP esterni, specificando sostanzialmente come tradurre tale tupla: 
	{IP, protocollo, porta} (interno) ⇐⇒ {IP, protocollo, porta} (esterno)

Non è facile determinare se un'associazione non è più necessaria, quindi le associazioni hanno un tempo di scadenza; si noti che alcune di esse possono essere eliminate prima che scadano: ad esempio, poiché i flussi TCP possono essere chiusi con grazia, il NAT attende l'ultimo handshake e poi rimuove l'associazione. Il NAT consente 64.000 associazioni simultanee per protocollo.
![[Pasted image 20241017202507.png]]

**Filtri**  
I filtri NAT decidono se un pacchetto debba essere tradotto, anche se esiste già un'associazione per esso.
Rendono il NAT non deterministico (comportamenti multipli, sia buoni che cattivi) e esistono a causa dell'UDP:  
	– **TCP** (connessione uno-a-uno, bidirezionale): invia e riceve pacchetti solo verso e da un singolo endpoint, dopo che una connessione è stata stabilita. I pacchetti broadcast non possono essere ricevuti, quindi ogni pacchetto TCP verrà tradotto da un NAT. Il TCP utilizza timeout, facendo scadere la connessione dopo un certo periodo di tempo dall'ultimo dato ricevuto;  
	– **UDP** (basato sui dati, senza connessione): può ricevere da più mittenti senza una connessione precedente e i messaggi broadcast sono consentiti. Non può essere vincolato perché non c'è un flusso: non è possibile decidere quando eliminare un'associazione e un filtro solo osservando i pacchetti in entrata/uscita. Introduce anche il problema del demultiplexing: il NAT deve capire a quale flusso appartiene ciascun pacchetto, poiché esiste un solo socket (è necessario consultare gli header IP e UDP del pacchetto per verificare indirizzo e porta).

## 6.3 Comportamenti NAT 

È chiaro che il NAT deve avere comportamenti differenti per TCP e UDP - e ciò che è peggio, le applicazioni potrebbero non funzionare (correttamente) se viene scelto il comportamento "sbagliato". Di seguito descriviamo i quattro tipi di comportamento NAT: 
	– NAT **simmetrico**;  
	– NAT **full cone**;  
	– NAT **restricted cone**;  
	– NAT **port restricted cone**.

### 6.3.1 NAT simmetrico  

Un NAT simmetrico  è un tipo di NAT in cui tutte le richieste provenienti dallo stesso indirizzo IP interno e porta, verso un indirizzo IP e una porta di destinazione specifici, vengono mappate allo stesso indirizzo IP e porta esterni. 
![[Pasted image 20241017224628.png]]
Se lo stesso host invia un pacchetto con lo stesso indirizzo e porta sorgente, ma verso una destinazione diversa, viene utilizzata una mappatura differente. Inoltre, solo l'host esterno che riceve un pacchetto può inviare un pacchetto UDP di ritorno all'host interno. Funziona allo stesso modo sia per TCP che per UDP, e questo è in realtà l'unico comportamento NAT utilizzato per TCP.

### 6.3.2 NAT full cone

Un NAT full cone (a cono pieno), il tipo più comune, è quello in cui tutte le richieste provenienti dallo stesso indirizzo IP interno e porta vengono mappate allo stesso indirizzo IP e porta esterni. Inoltre, qualsiasi host esterno può inviare un pacchetto all'host interno inviando un pacchetto all'indirizzo esterno mappato. A seconda del filtro, tutte le altre associazioni possono portare a un NAT full cone.
![[Pasted image 20241017225119.png]]
Il problema di sicurezza con questo tipo di NAT è che chiunque può effettuare una scansione rapida del server NAT e scoprire quali computer hanno qualcosa di aperto: eseguire una scansione di rete dietro la nostra rete diventa un gioco da ragazzi.

### 6.3.3 NAT restricted cone

In un NAT a cono ristretto (restricted cone), tutte le richieste provenienti dallo stesso indirizzo IP interno e porta vengono mappate allo stesso indirizzo IP e porta esterni. A differenza di un NAT a cono pieno, un host esterno (con indirizzo IP X) può inviare un pacchetto all'host interno solo se l'host interno aveva inviato in precedenza un pacchetto all'indirizzo IP X. ![[Pasted image 20241017225446.png]]
Questo tipo di NAT è leggermente migliore di un NAT simmetrico, ma, a fini pratici, è quasi inutile perché il referral and handover, ovvero il processo di trasferire dati di sessione da un canale ad un altro -> ad esempio quando un telefono si sposta da un area ad un altra, coperta da un altra cella(?), la chiamata è trasferita al successivo cella in modo da evitare la fine della chiamata.

### 6.3.4 NAT a cono ristretto per porta (port cone restricted)

Un NAT a cono ristretto per porta è simile a un NAT a cono ristretto, ma la restrizione include i numeri di porta. Nello specifico, un host esterno può inviare un pacchetto, con indirizzo IP sorgente X e porta sorgente P, all'host interno solo se quest'ultimo aveva precedentemente inviato un pacchetto all'indirizzo IP X e alla porta P.  
![[Pasted image 20241017230218.png]]
In questo tipo di NAT è ancora possibile effettuare una scansione di rete se si conosce la porta che deve essere utilizzata come porta sorgente, per inviare pacchetti al NAT e farli tradurre verso il computer interno. Tuttavia, è più probabile che il NAT o il firewall individuino attività sospette. Per questo motivo, l'UDP dovrebbe essere utilizzato solo con questo comportamento NAT.

### 6.3.5 Hairpinning

L'hairpinning  descrive una comunicazione tra due host dietro lo stesso dispositivo NAT utilizzando il loro endpoint mappato dal NAT.
Poiché non tutti i dispositivi NAT supportano questa configurazione di comunicazione, le applicazioni devono esserne consapevoli.  
![[Pasted image 20241017230416.png]]
In altre parole, l'hairpinning è quando una macchina sulla LAN è in grado di accedere a un'altra macchina sulla LAN tramite l'indirizzo IP esterno della LAN/router (con il port forwarding configurato sul router per indirizzare le richieste alla macchina appropriata nella LAN).  
Questa capacità del NAT è rilevante nei casi in cui un host desidera raggiungere un altro host dietro lo stesso NAT, ma conosce solo il suo indirizzo pubblico.

### 6.3.6 STUN

A volte è necessario scoprire che tipo di NAT abbiamo, così da sapere se possiamo utilizzare determinate applicazioni. STUN è proprio lo strumento adatto a questo scopo.
**STUN** è un protocollo *request-reply*: server, da dove proviene questo pacchetto? 
Il server risponde e STUN deduce il tipo di NAT dalla risposta. ![[Pasted image 20241019190746.png]]
Per effettuare una richiesta STUN, abbiamo bisogno di un server STUN ospitato su un computer che disponga di due indirizzi IP globali con due porte aperte per ciascun indirizzo (una capacità totale di quattro connessioni). 
Il client, operando tipicamente all'interno di una rete privata, invia una richiesta di binding (attraverso un pacchetto UDP) a un server STUN su Internet pubblico. Il server STUN risponde con una risposta di successo che contiene l'indirizzo IP e il numero di porta del client, come osservato dalla prospettiva del server.

**Esempio**  
Consideriamo il NAT a cono pieno dell'esempio di prima. Se l'host C può raggiungerci dalla porta 90, l'unica possibilità è che abbiamo un NAT a cono pieno, poiché quella connessione è consentita solo in un cono pieno; se non riceviamo una risposta, allora chiediamo di usare ciò che rimane (un cono ristretto o NAT per porta).
Alla fine, possiamo discriminare tra tutti i tipi di NAT.

STUN non è affidabile. Innanzitutto, poiché l'UDP non fornisce garanzie di trasporto affidabili, un certo livello di affidabilità viene raggiunto attraverso ritrasmissioni controllate dall'applicazione delle richieste STUN. Tuttavia, i NAT sono non deterministici, il che significa che il loro comportamento può cambiare nel tempo; inoltre, un client potrebbe avere più NAT uno dietro l'altro (questo accade molto più spesso di quanto si possa pensare): in questi casi, STUN potrebbe semplicemente fallire del tutto.
## 6.4 Altre Classificazioni NAT

Ora, chiariamo il fatto che, per classificare realmente un NAT, dobbiamo controllare le sue associazioni e filtri. Prendiamo ad esempio il sistema qui mostrato, ![[Pasted image 20241019193541.png]]
Dove il NAT mappa l'host in due cose completamente diverse: che tipo di NAT è questo?

### 6.4.1 Associazione  

Le associazioni NAT possono appartenere a uno dei seguenti quattro tipi:  
	– **Indipendente dall'endpoint**: il NAT riutilizza l'associazione per tutti i pacchetti con lo stesso indirizzo IP/porta di origine. **L'indirizzo IP/porta** di destinazione non viene considerato (NAT a cono pieno);  
	– **Dipendente dall'indirizzo dell'endpoint**: il NAT riutilizza l'associazione per tutti i pacchetti con lo stesso indirizzo IP/porta di origine e indirizzo IP di destinazione. La **porta** di destinazione non viene considerata (NAT a cono ristretto);  
	– **Dipendente dalla porta dell'endpoint**: il NAT riutilizza l'associazione per tutti i pacchetti con lo stesso indirizzo IP/porta di origine e porta di destinazione. **L'indirizzo IP** di destinazione non viene considerato (NAT a cono ristretto per porta);  
	– **Dipendente dall'indirizzo e dalla porta dell'endpoint**: il NAT riutilizza l'associazione per tutti i pacchetti con la stessa quintupla (NAT simmetrico).

### 6.4.2 Associazione di porta  

Le associazioni di porta NAT possono appartenere a uno dei seguenti tre tipi:  
	– **Conservazione della porta**: il NAT cerca di non cambiare il numero di porta. Se due (o più) host utilizzano la stessa porta di origine, tutti tranne il primo vedranno la loro porta modificata;  
	– **Sovraccarico della porta**: come per la conservazione della porta, il secondo host avrà la precedenza e l'associazione del primo verrà scartata (ouch);  
	– **Multiplexing della porta**: il NAT effettua un multiplexing aggressivo, cercando di multiplexare i flussi sulla stessa porta in base all'indirizzo/porta di destinazione. Questo può causare molti problemi se alcuni host tentano di connettersi con lo stesso host di destinazione. Il NAT deve capire quando fare il multiplexing e quando non farlo.  
	
In conclusione, è (quasi) impossibile prevedere cosa farà il NAT. Per questo motivo, i programmi di solito riservano diverse porte (circa 10-15), ma ciò non è né logico, né efficiente o sicuro, poiché ogni associazione aperta consente ai dati di tornare al mittente.

### 6.4.3 Aggiornamento del timer

Un timer NAT può essere aggiornato nei seguenti modi:  
	– **Bidirezionale**: il timer viene aggiornato dai pacchetti in entrata e in uscita;  
	– **In uscita**(outbound): solo i pacchetti in uscita aggiorneranno il timer; a seconda dell'applicazione, potrebbe essere necessario un keep-alive;  
	– **In entrata**(inbound): solo i pacchetti in entrata aggiorneranno il timer; a seconda dell'applicazione, potrebbe essere necessario un keep-alive;  
	– **Stato del protocollo di trasporto**: questo tenta di decodificare il protocollo a livello applicativo e "fare la cosa giusta" – cosa che spesso non avviene.  
	
Si noti che tutti, tranne gli aggiornamenti del timer in uscita, portano ad attacchi DoS. Gli aggiornamenti bidirezionali o in entrata non sono raccomandati perché un attaccante potrebbe intercettare quali flussi sono attivi, quindi continuare a inviare pacchetti alle loro associazioni: forse quei pacchetti verranno scartati, ma nel frattempo le associazioni rimarranno attive. Questo è un ottimo modo per sovraccaricare il NAT fino a farlo crollare (attacchi di panico).  

L'aggiornamento in uscita (outbound) è buono finché lo usiamo per lo streaming, perché dovremo inviare pacchetti keep-alive dal lato che non è il mittente principale (ad esempio, l'host dovrà dire a Netflix che è ancora attivo, altrimenti l'associazione scadrà - anche se è Netflix a inviare un'enorme quantità di pacchetti di dati).
L'UDP è unidirezionale, quindi questo metodo non funzionerà. Per quanto riguarda lo stato del protocollo di trasporto, deve conoscere lo stato di un'applicazione a livello 7: il NAT può farlo e lo farà, ma deve conoscere il protocollo dell'applicazione, e i protocolli a livello 7 non sono sempre open source (alcuni sono standard e pubblici, ma molti altri, come Skype o Webex, sono privati e protetti da copyright, e non possono essere semplicemente reverse-engineered).

### 6.4.4 Filtro esterno

Il filtraggio NAT include le seguenti modalità (le stesse delle associazioni nella sezione 6.4.1):  
	– **Indipendente dall'endpoint**: non fa nulla (NAT a cono pieno);  
	– **Dipendente dall'indirizzo dell'endpoint**: filtra in base all'indirizzo IP di destinazione (NAT a cono ristretto);  
	– **Dipendente dall'indirizzo e dalla porta dell'endpoint**: filtra in base all'indirizzo IP e alla porta di destinazione (NAT simmetrico).  
![[Pasted image 20241019202217.png]]	
Ricorda che filtri e associazioni devono essere abbinati, ma possono comportarsi in modi completamente diversi. Non possiamo controllare a quale categoria appartiene l'associazione o la porta che stiamo utilizzando; tutto dipende dalla quantità di risorse (CPU/memoria) del NAT, che cambiano durante il giorno.

## 6.5 Conclusioni sul NAT

**Applicazioni P2P**  

Il calcolo o il networking peer-to-peer (P2P) è un'architettura di applicazioni distribuite che suddivide compiti o carichi di lavoro tra peer, che sono partecipanti paritetici ed equipotenti nell'applicazione. 
Al giorno d'oggi, ogni dannato dispositivo in una casa che cerca di essere "smart" utilizza questa tecnologia (NAS (Network Attached Storage), smart TV e simili), apre porte sul NAT utilizzando tecniche di traversata del NAT, poiché rendono più facile per l'utente controllare rapidamente questi dispositivi. Tuttavia, questo significa anche che un attaccante può fare lo stesso.  
Fondamentalmente, ogni associazione che viene aperta consente ai pacchetti di tornare all'host; i casi più estremi si verificano quando abbiamo iniziato una comunicazione giorni fa e abbiamo ancora un'associazione attiva a causa di questo comportamento, che la rende molto pericolosa.

**ICMP, crittografia di livello 3 & co.**  

Tutti i pacchetti che non hanno porte specifiche, come nei messaggi del protocollo ICMP (Internet Control Message Protocol), funzionano per magia: invece di aprire una porta, utilizzano un'associazione specifica per quel computer. 
Se siamo dietro un NAT e proviamo a inviare un ping a un altro host dietro un altro NAT, possiamo farlo (un dispositivo alla volta).

**Frammentazione IP**  

Per tradurre i pacchetti dobbiamo controllare l'header di livello 4, ma i frammenti non contengono questo livello (perché appare solo nel primo pacchetto). Per questa ragione, i NAT devono controllare l'ID del frammento o ricostruire il frammento. Entrambi i casi non sono piacevoli: l'ID del frammento richiede una macchina ancora più complessa, e ricomporre il pacchetto all'interno del NAT introduce latenza, maggiori requisiti di memoria e, alla fine, il rischio di esaurimento delle risorse.

**UPnP e IGD**

Un dispositivo compatibile con Universal Plug and Play (UPnP) di qualsiasi fornitore può unirsi dinamicamente a una rete, ottenere un indirizzo IP, annunciare il proprio nome, comunicare le proprie capacità su richiesta e apprendere la presenza e le capacità di altri dispositivi.  
Il problema è evidente: UPnP consente a un programma/host/applicazione di aprire forzatamente un'associazione, il che significa che l'applicazione può chiedere al NAT di assegnarle una porta specifica - il che porta ad avere porte specifiche e ben note (non solo da noi, ma anche dagli attaccanti) permanentemente aperte sul NAT.  
Il protocollo di controllo standardizzato dei dispositivi Internet Gateway Device (IGD) peggiora la situazione poiché consente a un dispositivo UPnP di scoprire l'indirizzo IP esterno utilizzato dal NAT e di creare automaticamente associazioni e filtri.

# Capitolo 2: Introduzione alla crittografia

## 2.1 Sulla sicurezza

Come affermato nel capitolo 1, la sicurezza delle informazioni non è facile da definire. Anche il National Institute for Science and Technology (NIST, il principale istituto americano per gli standard dei sistemi connessi) cambia periodicamente la sua definizione di sicurezza, dimostrando come siamo passati da una sicurezza centrata sui computer a una centrata sulle informazioni:

- **Sicurezza informatica**(1995): la protezione fornita a un sistema informatico automatizzato per raggiungere gli obiettivi applicabili di preservazione dell'integrità, disponibilità e riservatezza delle risorse del sistema informatico (includendo hardware, software, firmware, informazioni/dati e telecomunicazioni).

- **Sicurezza delle informazioni**(2017): la protezione delle informazioni e dei sistemi informatici da accessi non autorizzati, uso, divulgazione, interruzione, modifica o distruzione, al fine di garantire riservatezza, integrità e disponibilità.

L'obiettivo finale, quindi, non è proteggere il computer, ma il bene più importante: i dati. I principali aspetti della sicurezza possono essere riassunti in sei concetti o politiche, tutti strettamente interconnessi: non possiamo garantire la riservatezza senza autenticazione, l'integrità senza controllo degli accessi, ecc.:

1. **controllo degli accessi**;
2. **autenticazione**;
3. **disponibilità**;
4. **riservatezza**;
5. **integrità**;
6. **non ripudio**.

In generale, la sicurezza delle informazioni:

- supporta la missione dell'organizzazione;
- rappresenta un elemento integrante di una gestione sana;
- implementa protezioni commisurate al rischio;
- rende espliciti ruoli e responsabilità;
- spinge le responsabilità dei proprietari dei sistemi oltre la loro organizzazione;
- richiede un approccio completo e integrato;
- è valutata e monitorata regolarmente;
- è vincolata da fattori sociali e culturali.
### 2.1.1 Controllo degli accessi

Il **controllo degli accessi** è la tecnica di sicurezza che regola chi o cosa può visualizzare, utilizzare o accedere a un luogo o ad altre risorse. È strettamente legato all'autenticazione, poiché prima assegna profili agli utenti e poi limita l'accesso ai servizi solo ai profili autorizzati. Questa tecnica consiste in molte regole che non sono facili da definire e richiedono un'attenta considerazione. Come si può immaginare, per eseguire il controllo degli accessi si utilizzano tecniche di rendicontazione.

È interessante notare che, dopo una violazione della sicurezza, il controllo degli accessi è la prima politica ad essere esaminata. Il responsabile della rete è la prima persona sotto indagine: deve dimostrare di non essere responsabile dell'attacco, poiché potrebbe avere conseguenze legali potenzialmente gravi.
### 2.1.2 Autenticazione

L'**autenticazione** è il processo di verifica se qualcuno (o qualcosa) è effettivamente chi (o cosa) ha dichiarato di essere: a volte gli aggressori potrebbero fingere di essere qualcun altro per ottenere informazioni riservate destinate solo a un'altra persona o dispositivo. Per ottenere l'autenticazione si utilizzano funzioni di *firma digitale*.
### 2.1.3 Disponibilità (Availability)

La disponibilità garantisce che il sistema e i dati (l'intero servizio) possano essere accessibili e soddisfare le richieste degli utenti autorizzati, ogni volta e ovunque siano necessari. La disponibilità del servizio è la qualità più difficile da garantire, poiché richiede una pianificazione accurata della rete; ad esempio, non è garantita se è in corso un attacco Denial of Service (DoS) (in questo caso, la nostra missione sarebbe rendere oneroso per un attaccante realizzare un attacco DoS).
Si noti che controllare periodicamente la disponibilità di un sistema non è un metodo efficace per garantire questa politica, poiché un attaccante potrebbe mettere il sistema fuori uso e poi ripristinarlo tra due controlli. (Non basta calcolare la disponibilità media, ma è importante calcolarla nei casi peggiori di attacco )
### 2.1.4 Riservatezza (Confidentiality)

La **riservatezza** è la tecnica di sicurezza che protegge le informazioni dall'essere accessibili a parti non autorizzate. I dati scambiati devono rimanere segreti tra mittente e destinatario. Normalmente, la riservatezza è garantita mediante ==l'uso di algoritmi crittografici==, poiché le reti consentono l'intercettazione dei pacchetti e i dati non criptati potrebbero potenzialmente essere letti da qualcun altro.
### 2.1.5 Integrità

L'**integrità** è la garanzia che l'informazione sia affidabile e accurata. I dati devono quindi raggiungere la destinazione senza essere stati alterati, sia durante la trasmissione che durante la memorizzazione. Di solito, l'integrità dei dati è garantita mediante ==l'uso di funzioni di hash==.
Si noti che i dati criptati non garantiscono l'integrità, poiché a volte i metodi crittografici sono vulnerabili agli attacchi, e i dati criptati possono comunque essere modificati (ad esempio, attraverso un attacco di "bit flipping"). Inoltre, è possibile garantire l'integrità senza la riservatezza.
### 2.1.6 Non Ripudio

Il **non ripudio** è la garanzia che qualcuno non possa negare la validità di qualcosa. È una politica molto importante quando si scambiano documenti ed è generalmente ottenuta mediante l'uso ==di funzioni di firma digitale==. 
Le firme digitali sono molto più forti delle firme tradizionali. Tuttavia, essendo metodi crittografici, saranno valide solo per un certo numero di anni; dopo la scadenza di un determinato termine, non sono più valide, il che significa che chiunque potrebbe sostenere qualsiasi cosa riguardo ai documenti firmati con una firma digitale scaduta.
## 2.2 Principi della Crittografia

La crittografia è la base per ottenere il non ripudio (firme digitali), il controllo degli accessi (perché si basa sull'autenticazione, che a sua volta si basa sulle firme digitali), l'integrità e la riservatezza - praticamente tutto tranne la disponibilità.
La crittografia è antica quanto il mondo; significa "scrivere qualcosa in modo oscuro" e descrive come scambiare informazioni in modo che solo la sorgente e la destinazione possano comprenderle.
In generale, ogni messaggio inviato da una sorgente a una destinazione contiene informazioni che possono essere quantificate. Lo scopo della crittografia è nascondere queste informazioni al punto che un attaccante non possa distinguere tra dati significativi e rumore casuale e non correlato (come il rumore bianco). Questo è chiamato segretezza perfetta. È raggiungibile? Sì, ma in realtà no - e vedremo perché.
Nota: Non dobbiamo mai inventare il nostro algoritmo crittografico, perché falliremmo quasi sicuramente: è un compito matematico molto complesso per il quale reinventare la ruota non funziona (per niente).
### 2.2.1 Funzioni di Hash

Una **funzione di hash** è una funzione matematica che prende un input (nel nostro caso, un messaggio) e produce un *digest*, che è un pezzo di dati più piccolo di dimensione fissa n che possiede alcune proprietà matematiche.![[Pasted image 20241020130056.png]]
In generale, qualsiasi minima modifica all'input effettuata dalla funzione di hash fornirà un risultato completamente diverso nel digest.
Le funzioni di hash sono comunemente utilizzate per garantire l'integrità dei documenti trasmessi; sono realizzate con operazioni elementari come shift e XOR, quindi sono computazionalmente molto veloci.

Una funzione di hash può e deve essere definita in termini di proprietà matematiche, poiché queste sono utili per diversi motivi. Ad esempio, se una persona A (il mittente) invia un messaggio (alcuni dati) e il suo digest a un'altra persona B (il destinatario), B può calcolare il digest del messaggio utilizzando la stessa funzione di hash di A (che è già nota a entrambi) e confrontarlo con quello ricevuto da A.
![[Pasted image 20241020131118.png]]
Se i due digest sono uguali, allora il messaggio ricevuto da A non è stato modificato; altrimenti, qualcuno potrebbe aver intenzionalmente modificato i dati durante la trasmissione, e l'integrità è stata compromessa.

Nota che, diversamente da questo diagramma, nella vita reale non vogliamo mai inviare il messaggio e il suo digest attraverso lo stesso canale, perché un attaccante potrebbe modificare entrambi e ingannare così il destinatario facendogli credere che i dati non siano stati alterati. Costringere un attaccante a violare due canali diversi rappresenta un ulteriore passo in termini di difficoltà e sicurezza.
#### Proprietà delle funzioni di hash

In termini matematici, una funzione di hash è una funzione
- $H : X \rightarrow Y$ che mappa un input $m$ di lunghezza finita arbitraria, a un output  $y = H(m)$ di lunghezza fissa $n$ (**facilità di calcolo**).
Il dominio $X$ contiene tutti i possibili messaggi, mentre il codominio $Y$ tutti i possibili digest; essendo $n$ di lunghezza fissa arbitraria, $Y$ sarà molto più piccolo di $X$: $dim(X) \gg dim(Y)$ (compressione).
Supponiamo che un attaccante conosca il digest di un messaggio, ma non la funzione che lo ha generato. "Non dovremmo" essere in grado di trovare un altro messaggio che abbia lo stesso hash - non perché sia impossibile, ma perché è infattibile. (unfeasible -> nel senso che un task non può eseguire entro un intervallo di tempo ragionevole e con un insieme ragionevole di risorse).
Questa proprietà è chiamata **resistenza della pre-immagine**, e significa fondamentalmente che un attaccante non può fingersi un utente legittimo e inviare un messaggio con un certo hash per poi affermare che il messaggio era diverso (invalidando il messaggio originale).

In breve, le principali proprietà di una funzione di hash sono:

1. **Compressione**: $H : X \rightarrow Y$, con $dim(X) \gg dim(Y)$;
2. **Facilità di calcolo**: dato $H$ e un input $m$, $y = H(m)$ è molto facile da calcolare;
3. **Resistenza alla pre-immagine**: dato un valore di hash $h$, è *computazionalmente infattibile* trovare un qualsiasi messaggio $m$ tale che $H(m) = h$;
4. **Resistenza alla seconda pre-immagine**: dato un messaggio $m$, è computazionalmente infattibile trovare un qualsiasi messaggio $m'$ tale che $H(m') = H(m)$;
5. **Resistenza alle collisioni**: è computazionalmente infattibile trovare due input distinti e arbitrariamente scelti $m$ e $m'$ tali che $H(m') = H(m)$. Questa è la proprietà più difficile da raggiungere in pratica; nota che avere una funzione di hash resistente alle collisioni non significa che sia anche resistente alla pre-immagine e alla seconda pre-immagine.

Se una funzione di hash non rispetta nemmeno una di queste proprietà, non può essere utilizzata per scopi crittografici. Tuttavia, non tutte sono facili da ottenere, né possono essere matematicamente dimostrate per un algoritmo.
### 2.2.2 HMAC

Abbiamo visto che le funzioni di hash sono utili per garantire l'integrità. E per quanto riguarda l'autenticazione? Per questo compito, abbiamo bisogno di un **codice di autenticazione dei messaggi hash**(hash message authentication code), o HMAC, che combina una funzione di hash con una chiave segreta.
L'algoritmo HMAC più utilizzato è quello descritto nell'RFC 2104, che consiste nell'applicazione della funzione di hash $H$ a un messaggio $m$ e a una chiave segreta condivisa $K$ utilizzando l'equazione:
- $HMAC(K, m) = H((K' \oplus opad) \parallel H((K' \oplus ipad) \parallel m))$ per ottenere un digest in output, dove:
	- $H$ è una funzione di hash crittografica;
	- $m$ è il messaggio da autenticare, diviso in blocchi di dimensione $j$ (con $j$ dipendente dalla funzione di hash utilizzata);
	- $K$ è la chiave segreta;
	- $K'$ è una chiave di dimensione del blocco derivata dalla chiave segreta tramite *padding* a destra con zeri fino alla dimensione del blocco, oppure riducendo tramite hash fino a una dimensione inferiore o uguale alla dimensione del blocco e poi eseguendo padding a destra con zeri:
	- ![[Pasted image 20241020143003.png]]
	- $\parallel$ denota la concatenazione;
	- $\oplus$ denota l'operazione di XOR bit a bit.
	- **opad** è il padding esterno di dimensione pari a quella del blocco, costituito da byte con valore "0x5c" ripetuti $j/8$ volte;
	- **ipad** è il padding interno di dimensione pari a quella del blocco, costituito da byte con valore "0x36" ripetuti $j/8$ volte. (valori opad/ipad usati per massimizzare distanza di hamming --> K e K' hanno meno bit in comune)

La chiave segreta viene prima utilizzata per derivare due chiavi: interna ed esterna; il primo passaggio dell'algoritmo produce un hash interno derivato dal messaggio e dalla chiave interna, mentre il secondo passaggio produce il codice HMAC finale derivato dal risultato dell'hash interno e dalla chiave esterna.
È importante notare che il risultato finale dipenderà non solo dal messaggio, ma anche dalla chiave, il che significa che anche se l'attaccante ha il messaggio, potrebbe non essere in grado di decifrarlo. 
$K$ dovrebbe essere sufficientemente lungo e casuale per non contenere bit prevedibili, altrimenti un attaccante potrebbe trovarlo utilizzando un attacco a forza bruta. Se $K$ è più corto di $j$ bit, lo si completa con un padding di 0 e poi lo si utilizza così com'è, oppure lo si sottopone a hash e si aggiunge un numero con massima entropia. (ovvero massimo di bit casuali)
#### HMAC in pratica

Il digest può essere calcolato solo se entrambi i partecipanti conoscono la chiave $K$, quindi sarà necessaria un'autenticazione per garantire che siano realmente chi dichiarano di essere (evitando così di dare la chiave a un potenziale attaccante).

Supponiamo che A invii $m$ e $HMAC(K, m)$ a B nello stesso pacchetto: se un attaccante E intercetta entrambe le informazioni, non può ricalcolare $HMAC(K, m)$ perché non conosce la chiave $K$, ma potrebbe facilmente modificare $m$ in $m'$.

È quindi chiaro che i principali problemi di HMAC sono:
1. trovare un modo sicuro per scambiare  K (e no, Internet non è la risposta);
2. attacchi a forza bruta: E potrebbe intercettare un pacchetto e tentare di prevedere $K$. Questo tipo di attacco è computazionalmente infattibile, ma se la chiave è derivata da una password, E può eseguire un attacco basato su dizionario, poiché generare parole in un dizionario richiede solo pochi minuti. Questo problema è più comune di quanto si possa pensare.
#### Considerazioni finali

HMAC non specifica quale funzione di hash debba essere utilizzata, quindi dobbiamo scegliere quella più appropriata. Dobbiamo essere consapevoli delle vulnerabilità che di tanto in tanto vengono scoperte nelle funzioni di hash e cambiarla eventualmente, poiché più vengono utilizzate, più vengono studiate e più vulnerabilità vengono scoperte. Ad esempio, dovremmo usare ***SHA3*** invece di *SHA2* o *SHA1* (che in realtà sono ancora ampiamente utilizzati nonostante siano gravemente compromessi).
Se utilizziamo una funzione di hash debole, un attaccante potrebbe forgiare un messaggio che verrebbe considerato valido dal destinatario; questo è un caso molto grave, perché l'attaccante non solo potrebbe inviare messaggi falsi, ma potrebbe anche trovare la chiave segreta.

### 2.2.3 Crittografia a chiave simmetrica

Gli algoritmi a chiave simmetrica sono algoritmi di crittografia che utilizzano le stesse chiavi crittografiche sia per la cifratura del testo in chiaro (il messaggio originale) sia per la decifratura del testo cifrato. 
Le chiavi, in pratica, rappresentano un segreto condiviso tra due o più parti che può essere utilizzato per mantenere un collegamento informativo privato. Gli algoritmi utilizzati per la crittografia e la decrittografia possono essere simmetrici o asimmetrici.
![[Pasted image 20241020145743.png]]
#### Limitazioni della crittografia a chiave simmetrica

Il requisito che entrambe le parti abbiano accesso alla chiave segreta è uno dei principali svantaggi della crittografia a chiave simmetrica, rispetto alla crittografia a chiave pubblica (nota anche come crittografia a chiave asimmetrica). 
Tutto funziona se e solo se possiamo garantire che nessuno tranne il mittente e il destinatario conosca le chiavi. Questa affermazione è estremamente debole: non possiamo mai presumere che sia vera, perché il mittente o il destinatario potrebbero essere stati compromessi, o il destinatario potrebbe non essere affidabile, e/o non possiamo scambiare chiavi diverse in tempo reale. In altre parole, la crittografia a chiave simmetrica è cieca: non ci dice nulla sull'identità del mittente, né se il messaggio è stato modificato o meno.
#### Uso con HMAC

Per garantire l'integrità di un messaggio nella crittografia a chiave simmetrica, possiamo usarla combinata con HMAC nel seguente modo:
1. generare un HMAC con una chiave segreta K;
2. crittografare l'intero messaggio (incluso l'HMAC) con un'altra chiave segreta K';
3. confrontando il messaggio e il suo HMAC, il destinatario può stabilire se tutto è corretto (o no).

Usiamo HMAC invece di un semplice hash perché se utilizzassimo un hash e l'attaccante recuperasse la chiave esterna K' (quella utilizzata per la crittografia simmetrica), potrebbe cambiare il messaggio e il suo hash - quindi la chiave K' rappresenta un ulteriore passo in termini di sicurezza. 
Tuttavia, nonostante questo metodo, i problemi legati all'invio privato delle chiavi e all'identificazione del mittente rimangono.
### 2.2.4 Crittografia a chiave asimmetrica

La crittografia a chiave **asimmetrica** non utilizza una chiave condivisa; invece, entrambi i partecipanti (che chiamiamo A e B) possiedono due chiavi:
- una chiave privata $Pri_A$, $Pri_B$ 
- una chiave pubblica $Pub_A$, $Pub_B$ 

Come suggeriscono i loro nomi, le chiavi private devono essere mantenute segrete: solo A conosce $Pri_A$ e solo B conosce $Pri_B$
Le chiavi pubbliche, invece, possono essere diffuse ovunque, poiché non necessitano di protezione; sia A che B le conoscono entrambe, così come eventualmente molte altre persone. Ovviamente, per qualsiasi persona X, deve essere computazionalmente infattibile ottenere$Pri_X$ tramite $Pub_X$ e viceversa.
In uno schema di crittografia a chiave asimmetrica, chiunque può crittografare messaggi utilizzando la chiave pubblica, ma solo il titolare della chiave privata associata può decifrarli. Un attaccante potrebbe recuperare il messaggio che è stato inviato, ma poiché non conosce la chiave privata, non sarà in grado di decifrarlo.
Dunque, la crittografia a chiave asimmetrica funziona come segue:![[Pasted image 20241020150831.png]]
1. il mittente (A) utilizza la chiave pubblica del destinatario (B) $Pub_B$ per crittografare il suo messaggio $m$, ottenendo $m'$;
2. B utilizza la sua chiave privata $Pri_{B}$ per decifrare $m'$.

L'algoritmo per la crittografia e la decrittografia è lo stesso per entrambe le operazioni: se utilizziamo l'algoritmo con una chiave, otteniamo un messaggio che può essere riportato all'originale eseguendo l'algoritmo con la seconda chiave (in altre parole, la seconda chiave decifra i dati crittografati dalla prima).

Le chiavi vengono generalmente generate insieme con programmi specifici, come `ssh-keygen` negli ambienti Linux. Non è necessario concordare in anticipo una chiave comune di crittografia/decrittografia; un numero imprevedibile (tipicamente grande e casuale) viene utilizzato per iniziare la generazione di una coppia di chiavi accettabile e adatta all'uso con un algoritmo a chiave asimmetrica.
#### Crittografia a chiave asimmetrica: pro e contro

La sicurezza complessiva di questo metodo dipende interamente dalla segretezza della chiave privata: se ci fidiamo che la chiave privata sia stata mantenuta segreta da qualcuno o qualcosa, allora, ogni volta che riceviamo un messaggio che può essere decifrato dalla chiave pubblica associata a quella specifica chiave privata, sappiamo con certezza che l'unica entità in grado di crittografare quel messaggio era il vero mittente.
Vale la pena notare che in questo modo garantiamo la **riservatezza** e risolviamo il problema dell'**identità**.
### 2.2.5 Firma Digitale

La firma digitale si basa sulla crittografia a chiave asimmetrica e, infatti, utilizza gli stessi principi, solo che sono invertiti: poiché in questo caso non ci interessa la riservatezza, ma vogliamo solo garantire l'identità (non ripudio) del mittente, utilizziamo la chiave privata di A, per crittografare $m$. In questo modo, tutti saranno in grado di decifrare il messaggio con la chiave pubblica di A, ma garantiremo che il mittente fosse veramente A (il messaggio è stato **firmato** da A).
![[Pasted image 20241020152049.png]]
### 2.2.6 Crittografia a Chiave Mista

Nella vita quotidiana non si utilizza né la crittografia a chiave simmetrica pura né quella a chiave asimmetrica pura, ma piuttosto sono stati ideati algoritmi che combinano questi due metodi in modi creativi per ottenere una migliore sicurezza.
Ad esempio:
![[Pasted image 20241020152315.png]]

Il modo più comune per farlo è crittografare una chiave simmetrica con una chiave asimmetrica. Utilizziamo la crittografia asimmetrica per impostare la comunicazione, ovvero per negoziare una *chiave di sessione* (session key) segreta che sarà utilizzata durante quella sessione. A questo punto, il segreto è conosciuto solo dal mittente e dal destinatario e può essere utilizzato in modo sicuro per scambiare messaggi privati tra loro, garantendo riservatezza, integrità e identificazione.
Come suggerisce il nome, una chiave di sessione è valida solo durante la comunicazione per la quale è stata creata; nuove sessioni dovranno generare nuove chiavi segrete.
#### Mittenti/Destinatari Multipli

In casi come le chat di gruppo, dove esistono più (n) mittenti/destinatari, dobbiamo utilizzare una chiave segreta condivisa per evitare algoritmi di comunicazione computazionalmente inefficienti o addirittura infattibili. 
Tuttavia, questo è un problema completamente diverso che non discutiamo qui; è complicato da molti fattori aggiuntivi, come garantire che qualcuno escluso dalla chat non possa tornare finché non viene ri-autenticato, mantenendo attiva la comunicazione per tutti gli altri.

# Capitolo 3: Algoritmi di crittografia
## 3.1 Definizioni Matematiche (Saltate per ora)

TBD
## 3.2 Algoritmo RSA

L'algoritmo RSA (chiamato così dagli inventori Rivest, Shamir e Adleman, che lo descrissero pubblicamente nel 1977) è un algoritmo di crittografia a chiave pubblica ampiamente usato per la trasmissione sicura dei dati. RSA è un algoritmo relativamente lento, perciò non viene usato spesso per crittografare direttamente i dati utente; viene invece impiegato per trasmettere chiavi condivise per la crittografia a chiave simmetrica, che poi vengono utilizzate per la cifratura e decifratura in blocco.

La sicurezza di RSA si basa sulla difficoltà pratica di fattorizzare il prodotto di due numeri primi di grandi dimensioni, noto come "problema della fattorizzazione". Decifrare l'algoritmo RSA è chiamato "problema RSA". Anche se non è dimostrato che il problema RSA sia altrettanto difficile quanto il problema della fattorizzazione, non esistono metodi pubblicati per violare il sistema se viene utilizzata una chiave sufficientemente lunga.

Dati:
- p,q numeri primi (privati)
- n = p x q (pubblici)
- e, d con d inverso moltiplicativo di e, con e phi(n) coprimi per assicurare di avere inverso moltiplicativo
	- $e \cdot d = 1 (\text{mod} \phi(n)) = k \cdot \phi(n)+1$ (privato)
- Quindi usando la funzione toziente ottengo:
![[Pasted image 20241101185202.png]]

Se dunque scelto e,d tale che $d = (k \cdot \phi(n)+1) / e$, allora avremmo che $m = m^{d*e}(\text{mod}\space n)$, e quindi detto $c = m^{e}(\text{mod}\space n)$ il testo cifrato per riottenere il messaggio basterà:
- $c^d \text{mod} \space n = m^{ed} \text{mod} \space n = m^{e(k \cdot \phi(n)+1) / e}\text{mod} \space n = m$ 

L'RSA è un algoritmo interessante poiché, anche se un attaccante conoscesse n ed e, calcolare uno degli altri numeri (come $φ(n)$ o d) risulta computazionalmente infattibile: pur non essendo impossibile, richiederebbe migliaia di anni anche utilizzando il miglior hardware disponibile, a causa della complessità del calcolo del logaritmo discreto e, in ultima analisi, della fattorizzazione, che è un problema NP-completo.

È importante notare, tuttavia, che tra il 1994 e il 1996 è stato scoperto un nuovo algoritmo che ha ridotto la complessità computazionale della fattorizzazione di circa il 20%. Inoltre, i computer quantistici potrebbero calcolare logaritmi discreti in tempo polinomiale.

## 3.3 Algoritmo Diffie-Hellman-Merkle

L'algoritmo di scambio di chiavi Diffie-Hellman-Merkle (DHM) è un metodo per scambiare chiavi crittografiche in modo sicuro su un canale pubblico (non sicuro), ed è stato uno dei primi protocolli a chiave pubblica, come concepito da Ralph Merkle, Whitfield Diffie e Martin Hellman.

Pubblicato nel 1976 da Diffie e Hellman, rappresenta il primo lavoro pubblicato che propone l'idea di una chiave privata e di una chiave pubblica corrispondente. Anche se è un po' datato, rimane un metodo interessante e dibattuto.

Dati: 
- $p$ un numero primo molto grande
- $\alpha$ una radice primitiva (ovvero un numero tale che $\alpha (\text{mod} \space p)$ ha ordine moltiplicativo $p-1$ ovvero tutte le sue potenze $\alpha^i \text{mod} \space p$ sono diverse per $\forall i \in [1,p-1]$ 

L'algoritmo prosegue come segue:
1. A e B scelgono un numero segreto, rispettivamente $X_a$ e  $X_b$;
2. A invia a B $Y_a = \alpha^{X_a} \,(\text{mod}\, p)$;
3. B invia ad A $Y_b = \alpha^{X_b} \,(\text{mod}\, p)$;
4. A calcola $K_a = Y_b^{X_a} \,(\text{mod}\, p) = (\alpha^{X_b})^{X_a} \,(\text{mod}\, p)$;
5. B calcola $K_b = Y_a^{X_b} \,(\text{mod}\, p) = (\alpha^{X_a})^{X_b} \,(\text{mod}\, p)$.

Alla fine, $K \equiv K_a \equiv K_b$ è la chiave segreta che solo A e B conoscono. È evidente che il DHM è simile all'RSA, poiché entrambi utilizzano una funzione esponenziale del tipo $c = m^e$  e necessitano di un logaritmo (logaritmo discreto) come funzione inversa.

Questo algoritmo deve essere combinato con un meccanismo di verifica dell'identità, poiché un attaccante in grado di posizionarsi nel percorso di comunicazione potrebbe facilmente modificare $Y_a$ e $Y_b$. Non possiamo risolvere DHM in tempo lineare, a meno di possedere una tabella di tutte le radici primitive (dato che l'unico modo per calcolare un logaritmo è utilizzare tabelle o approssimazioni successive) - motivo per cui è necessario che $p$ sia molto grande: è possibile creare una tabella inversa per la funzione logaritmica, ma se $p$ è sufficientemente grande richiederebbe troppo spazio, rendendo il calcolo impraticabile.

## 3.4 Algoritmo One-Time Pad

Il one-time pad (OTP) è una tecnica di cifratura che non può essere decifrata, ma richiede l'uso di una chiave precondivisa ==utilizzabile una sola volta==, lunga almeno quanto il messaggio che si desidera inviare. 
In questa tecnica, un testo in chiaro $m$ viene abbinato a una chiave segreta casuale $k$ (nota anche come one-time pad), e ogni bit o carattere del testo in chiaro viene cifrato combinandolo con il corrispondente bit o carattere della chiave tramite addizione modulare, ovvero lo XOR, (una funzione invertibile): il testo cifrato sarà $c = m \oplus k$ , mentre la decifrazione sarà $m = c \oplus k$ .

Il testo cifrato risultante sarà impossibile da decifrare o violare se vengono soddisfatte le seguenti quattro condizioni per la chiave $k$:
1. $k$ deve essere **veramente casuale**; (ogni singolo bit ha il 50% di possibilità di essere 0/1)
2. $k$ deve essere **lungo almeno quanto il testo** in chiaro;
3. $k$  non deve **mai essere riutilizzato**, neanche parzialmente;
4. $k$ deve essere mantenuto **completamente segreto**.

Il one-time pad ha una proprietà nota come **segretezza perfetta**: il testo cifrato $c$ non fornisce assolutamente alcuna informazione aggiuntiva sul testo in chiaro. Questo perché, data una chiave veramente casuale usata una sola volta, un testo cifrato può essere interpretato come qualsiasi testo in chiaro della stessa lunghezza, e tutti sono ugualmente probabili. Pertanto, la probabilità a priori di un messaggio in chiaro $m$ è uguale alla probabilità a posteriori dello stesso messaggio $m$ dato il corrispondente testo cifrato.
### Limitazioni dell'OTP

Il problema principale con questo algoritmo è ottenere una chiave $k$ perfettamente casuale. Inoltre, avere una chiave lunga quanto il messaggio può risultare praticamente impossibile.
Una soluzione potrebbe essere quella di generare la chiave con un generatore di numeri pseudo-casuali e scambiare solo il seme del generatore.
Questa potrebbe sembrare un’ottima idea, ma il generatore di numeri pseudo-casuali deve essere davvero in grado di generare numeri casuali - perciò, in pratica, non funziona davvero, perché avrà sempre qualche problema (come correlazioni tra bit, ripetizioni di numeri, ecc.). Inoltre, essendo pseudo-casuale, si tratta di un algoritmo, il che significa che, conoscendo il seme, si conosce anche il numero generato. Più un generatore pseudo-casuale è affidabile, più lento sarà il suo funzionamento; tuttavia, tutti i generatori hanno almeno un problema: la loro casualità dipende interamente dai semi, che devono avere certe proprietà per essere efficaci.

## 3.5 Confusione e diffusione

Nella crittografia, **confusione** e **diffusione** sono due proprietà del funzionamento di un cifrario sicuro identificate da Claude Shannon nel suo rapporto riservato del 1945, *A Mathematical Theory of Cryptography*. Queste proprietà, quando presenti, confondono l'applicazione delle statistiche e di altri metodi di crittoanalisi. 

Questi concetti sono importanti per la progettazione di funzioni hash robuste e generatori di numeri pseudo-casuali, dove la *decorrelazione* dei valori generati è di fondamentale importanza; in pratica, dovrebbero essere applicati negli algoritmi per prevenire la ***crittoanalisi* statistica**. Tuttavia, queste proprietà non sono obbligatorie per garantire la sicurezza di un algoritmo. Ad esempio, l'algoritmo del cifrario monouso (one-time pad), che genera un testo cifrato statisticamente indipendente dal testo in chiaro, non si basa né sulla confusione né sulla diffusione (quest'ultima, poiché ogni bit del testo in chiaro dipende da un singolo bit della chiave).
Questo vale per tutti i cifrari a flusso, poiché per definizione sono immuni alla crittoanalisi statistica. Si potrebbe sostenere che l'OTP faccia uso della confusione poiché il segreto non è veramente la chiave $k$ , che ha la stessa lunghezza di $m$ e $c$, ma il seme che lo ha generato, assumendo che $k$ sia stato creato utilizzando un generatore di numeri pseudo-casuali.
### Confusione

La confusione significa che ogni cifra binaria (bit) del testo cifrato dovrebbe dipendere da diverse parti della chiave, oscurando le connessioni tra i due. Questa proprietà nasconde la relazione tra il testo cifrato e la chiave. 
La confusione rende anche difficile trovare la chiave dal testo cifrato e, se un singolo bit della chiave viene modificato, anche il calcolo dei valori della maggior parte o di tutti i bit del testo cifrato verrà influenzato; in sostanza, aumenta l’**ambiguità** del testo cifrato.

### Diffusione

La diffusione significa che, se cambiamo un singolo bit del testo in chiaro, allora (statisticamente) metà dei bit nel testo cifrato dovrebbero cambiare, e, similmente, se cambiamo un bit del testo cifrato, allora circa metà dei bit del testo in chiaro dovrebbero cambiare. Dato che un bit può avere solo due stati, quando tutti vengono rivalutati e cambiati da una posizione apparentemente casuale all'altra, metà dei bit cambieranno stato. In altre parole, l'idea della diffusione è di nascondere la ==relazione tra il testo cifrato e il testo in chiaro==.

## 3.6 Algoritmi di sostituzione

Gli algoritmi di sostituzione fanno parte delle cosiddette *reti di sostituzione-permutazione* (SPN), proposte da Shannon per la creazione di cifrari robusti e pratici, come il cifrario di Feistel. Anche il one-time pad è un caso speciale di algoritmo di sostituzione. 
Consideriamo il caso di cifrari a blocchi (algoritmi operanti su una lunghezza fissa di bit, detti blocchi) su $n$ bit. Nel caso più generale, per una chiave fissa $k$, tale cifrario consiste semplicemente in una funzione iniettiva $f$  che mappa i blocchi di $n$  bit su altri blocchi di $n$ bit, o, in altre parole, una mappa (statica) che cambia i bit di un messaggio: 
$f : \{0, 1\} \to \{0, 1\}^n$

**Esempio** Consideriamo la seguente funzione per  n = 2  (mappa a 2 bit), dove $f$ è una permutazione di $\{0, 1\}^2$:
	00 → 01  
	01 → 11  
	10 → 00  
	11 → 10  

Nel caso più generale, il numero di possibili trasformazioni è uguale alle possibili permutazioni dei $2^n$ blocchi, o $n^{n!}$. Se usiamo piccoli blocchi, ad esempio con $n = 4$ o $n = 5$, otteniamo un classico cifrario a sostituzione monoalfabetica( sostituisco ogni lettera del testo da cifrare in una qualsiasi altra lettera dello stesso insieme)
Chiaramente, questi cifrari sono suscettibili agli attacchi di crittoanalisi statistica, poiché non hanno diffusione. Per mitigare questo rischio potremmo utilizzare mappe più grandi, ma non è pratico perché le chiavi avrebbero troppi bit per essere effettivamente usate.

**Esempio** Dato una mappa a 64 bit (n = 64), che è ragionevolmente sicura, la chiave sarebbe rappresentata dalla permutazione stessa, codificata come $n \cdot 2^n = 64 \cdot 2^{64} \approx 10^{21}$. Questo è un numero di bit impossibile da gestire per un computer.

## 3.7 Cifrario di Feistel

Un cifrario di Feistel è una struttura simmetrica utilizzata nella costruzione di cifrari a blocchi, intitolata a Horst Feistel che ha condotto ricerche pionieristiche mentre lavorava per IBM.

In un cifrario di Feistel, la crittografia e la decrittografia sono operazioni molto simili, e entrambe consistono nell'esecuzione iterativa di una funzione chiamata *funzione di round*, fatta agire un numero fissi di volte.
La funzione che prende due input, il blocco di dati e una sottochiave, e ritorna un valore di dimensione pari al blocco di partenza. 
L'algoritmo opera quindi in questo modo:
1. il testo in chiaro viene diviso in due parti $L_0$ e $R_0$, ciascuna di $w$ bit;
2. $L_0$ e $R_0$ attraversano $n$ round che hanno la stessa struttura (il testo in chiaro è modificato da una funzione $F$ che esegue la diffusione) ma utilizzano $n$ sottochiavi $K_1, \dots, K_n$ generate dalla chiave principale $K$ tali che $K_i \neq K_j \ \forall i, j \in [1, n], i \neq j$, e $K_i \neq K \ \forall \in [1, n]$;
3. le due parti del testo in chiaro escono dall'ultimo round come $L_n$ e $R_n$ e passano attraverso un ultimo passaggio che le scambia (creando $L_{n+1}$ e $R_{n+1}$) per eseguire la confusione.

La funzione $F$ è una funzione di permutazione pseudo-casuale crittograficamente sicura, dove $K_i$ è il seme.
Questo schema è (più o meno) utilizzato da tutti gli algoritmi di crittografia simmetrica. Un importante vantaggio dei cifrari di Feistel è che l'intera operazione è garantita essere invertibile, anche la funzione di round non lo è.
La funzione di round può essere resa arbitrariamente complessa, poiché non è necessario progettarla per essere invertibile. Inoltre, le operazioni di cifratura e decifratura sono molto simili, e in alcuni casi addirittura identiche; pertanto, la dimensione del codice o del circuito necessario per implementare un tale cifrario si riduce quasi della metà, rendendo questo cifrario facilmente traducibile in hardware.![[Pasted image 20241107192402.png]]

## 3.8 Crittografia a curve ellittiche (Non fatto)

La **crittografia a curve ellittiche** (ECC) è uno dei tipi di crittografia più potenti ma meno compresi in uso oggi. Un numero crescente di siti web utilizza ampiamente l’ECC per proteggere vari aspetti, dalle connessioni HTTPS dei clienti al modo in cui i dati vengono scambiati tra data center. Ha vantaggi e svantaggi straordinari, ma poiché non sappiamo ancora se e quando esisterà un modo per invertirla, non dovremmo utilizzarla per cifrare dati di grande importanza.

Dopo l'introduzione degli algoritmi RSA e Diffie-Hellman, i ricercatori esplorarono soluzioni crittografiche basate su ulteriori matematiche alla ricerca di algoritmi oltre al fattorizzazione che potessero funzionare come buone funzioni di "trapdoor". 
Nel 1985, furono proposti algoritmi crittografici basati su un ramo della matematica chiamato curve ellittiche. Una curva ellittica è una funzione matematica della forma $y^2 = x^3 + ax + b$
	![[Pasted image 20241107192753.png]]

Ha due proprietà interessanti:
- è simmetrica rispetto all'asse $x$;
- ogni linea non verticale interseca la curva in al massimo tre punti.

Immaginiamo questa curva come un tavolo da biliardo particolare. Prendiamo due punti qualsiasi sulla curva e tracciamo una linea attraverso di essi; la linea intersecherà la curva esattamente in un altro punto. 
In questo gioco di biliardo, prendiamo una pallina al punto $A$ e la lanciamo verso il punto $B$. Quando colpisce la curva, la pallina rimbalza o verso l'alto (se si trova sotto l'asse $x$) o verso il basso (se si trova sopra l'asse $x$) verso l'altro lato della curva.

Possiamo chiamare questo movimento di biliardo su due punti una funzione di "dot". Qualsiasi coppia di punti su una curva può essere combinata tramite "dot" per ottenere un nuovo punto:
$$
A \cdot B = C \space(3.4)
$$

Possiamo anche concatenare mosse per combinare un punto con sé stesso più volte:
$$
A \cdot A = B \quad \text{(questa è la tangente alla curva ellittica)}
$$
$$
A \cdot B = C \quad \text{(inoltre, } A \cdot B = B \cdot A\text{)}
$$
$$
A \cdot C = D
$$

In sostanza, se abbiamo due punti e un punto iniziale combinato con sé stesso $n$ volte per arrivare a un punto finale, risalire a $n$ conoscendo solo il punto finale e quello iniziale è difficile. Per continuare il nostro esempio di biliardo, immagina che una persona giochi da sola in una stanza per un periodo di tempo casuale. Per lui o lei è facile colpire la pallina più e più volte seguendo le regole sopra descritte. Se qualcun altro entra nella stanza in un secondo momento e vede dove si trova la pallina, anche conoscendo tutte le regole del gioco e il punto di partenza della pallina, non può determinare il numero di volte che è stata colpita senza ripercorrere tutto il gioco fino a raggiungere lo stesso punto. Facile da fare, difficile da invertire: questa è la base per una funzione di trapdoor molto efficace.

Ogni coppia di punti $A$ e $B$ ha un risultato $C$, poiché la curva ellittica è definita da un punto chiamato punto nullo e si estende fino a infinito, quindi sull'asse $x$, dal punto nullo (negativo) a infinito (positivo), abbiamo coperto ogni valore di $x$.

Limitiamoci a numeri in un intervallo fisso come in RSA, il che significa che, invece di permettere qualsiasi valore per i punti sulla curva, ci limitiamo a numeri interi in un intervallo fisso. Calcolando la formula per la curva ellittica $y^2 = x^3 + ax + b$, usiamo lo stesso trucco di "rollover" quando raggiungiamo il valore massimo. Se scegliamo come massimo un numero primo, la curva ellittica è chiamata curva "prime" e possiede eccellenti proprietà crittografiche.![[Pasted image 20241107205232.png]]La figura 3.4 appare meno come una curva nel senso tradizionale, ma lo è. È come se la curva originale fosse avvolta intorno ai bordi, e solo le parti della curva che toccano coordinate a numero intero sono colorate, mostrando ancora la simmetria orizzontale.

Possiamo ancora giocare al gioco del biliardo su questa curva e combinare i punti. L'equazione di una linea sulla curva mantiene le stesse proprietà. Inoltre, l'operazione di combinazione (dot) può essere calcolata in modo efficiente: possiamo visualizzare la linea tra due punti come una linea che si avvolge ai bordi finché non incontra un punto. È come nel nostro gioco di biliardo, quando una pallina colpisce il bordo (il massimo), viene magicamente trasportata dall'altro lato del tavolo e continua il suo percorso fino a raggiungere un punto.

Con questa nuova rappresentazione della curva, possiamo prendere messaggi e rappresentarli come punti sulla curva. Possiamo immaginare di prendere un messaggio e impostarlo come coordinata $x$ e risolvere per $y$ per ottenere un punto sulla curva. In pratica è leggermente più complicato di così, ma questo è il concetto generale. Un sistema crittografico a curve ellittiche può essere definito scegliendo un numero primo come massimo, un'equazione della curva e un punto pubblico sulla curva. Una chiave privata è un numero $priv$, e una chiave pubblica è il punto pubblico combinato con sé stesso $priv$ volte. Il calcolo della chiave privata dalla chiave pubblica in questo tipo di sistema crittografico è chiamato funzione del logaritmo discreto su curve ellittiche.

Questo risulta essere la funzione di trapdoor che stavamo cercando.

Fondamentalmente, dato un punto iniziale $A$, calcoliamo $A \cdot A$ $n$ volte: $A \cdot A$ interseca un altro punto $B$. Se lo facciamo ancora otteniamo un altro punto, e così via. Il punto è che, se conosciamo il punto iniziale e quante volte abbiamo combinato $A$ con sé stesso, calcolare il punto finale è molto semplice, ma se conosciamo solo il punto di partenza e il punto finale, calcolare quante volte abbiamo fatto l'operazione "dot" diventa estremamente difficile (in sostanza dovremmo provare a farlo $n$ volte).

**Vantaggi delle funzioni ellittiche**

La curva ellittica è stata proposta da due matematici che lavoravano per la NSA. È stato dimostrato che è estremamente difficile da ingegnerizzare al contrario e che la sicurezza viene raggiunta con meno byte nella chiave rispetto agli algoritmi normali. Di solito, una chiave più corta implica un algoritmo più debole; tuttavia, per le curve ellittiche è stato dimostrato che sono forti quanto altri algoritmi con una chiave più corta, il che è una proprietà estremamente vantaggiosa: possiamo risparmiare bit e byte negli scambi di protocollo e, a seconda dell'algoritmo, essere anche più veloci.

**Contro delle funzioni ellittiche**  

Un problema emerso quasi immediatamente nelle funzioni a curve ellittiche è che non esiste una dimostrazione matematica che il problema di invertire una curva ellittica non sia trattabile. Non sappiamo se esista un modo per invertire la funzione; i creatori potrebbero conoscerlo ma non averlo divulgato. Inoltre, se scegliamo male i punti $A$ e $B$, potrebbe esserci un modo ingegnoso per invertire l'algoritmo. 

In generale, dobbiamo sempre assicurarci di utilizzare algoritmi di prim'ordine; non dobbiamo mai utilizzare quelli nuovi, che potrebbero non essere stati testati a fondo e potrebbero presentare vulnerabilità sconosciute. Piuttosto, è meglio utilizzare quelli più vecchi e consolidati, di cui conosciamo molte proprietà.

## 3.9 Attacchi a canale laterale

Un attacco a canale laterale, o semplicemente **attacco laterale**, è un attacco basato sulle informazioni ottenute dall'implementazione di un sistema informatico, piuttosto che sulle debolezze dell'algoritmo implementato stesso (ad esempio, crittoanalisi e bug software).

Le principali categorie di attacchi laterali includono:
- **Attacchi temporali**: l'attaccante cerca di compromettere un sistema crittografico analizzando il tempo necessario per eseguire gli algoritmi crittografici. Poiché ogni operazione logica in un computer richiede un tempo di esecuzione, e questo tempo può variare in base all'input, misurando con precisione il tempo di ogni operazione, un attaccante può risalire all'input.
  
- **Attacchi di monitoraggio del calore e del consumo di energia**: l'attaccante studia la generazione di calore e/o il consumo di energia di un dispositivo crittografico. Misurando queste proprietà fisiche di un sistema, è possibile ottenere una piccola quantità di informazioni sui dati in elaborazione.

- **Attacchi al generatore di numeri casuali**: l'attaccante compromette o sfrutta le debolezze del processo di generazione di numeri casuali. Dal punto di vista hardware, questo può essere fatto cercando di captare emissioni radiofrequenze dal computer (ad esempio, ottenendo i tempi di interruzione del disco rigido dal rumore del motore) o alimentando segnali controllati in una fonte che dovrebbe essere casuale (come un segnale forte e noto in una scheda audio).

In tutti i casi, il principio sottostante è che gli effetti fisici causati dall'operazione di un sistema crittografico (laterale) possono fornire informazioni utili sui segreti nel sistema, come la chiave crittografica, informazioni di stato parziali, testo in chiaro completo o parziale, ecc.
Il punto fondamentale è assicurarsi che l'algoritmo funzioni allo stesso modo per ogni input o in modo casuale per ogni input.

# Capitolo 7: Attacchi e vulnerabilità

Questo capitolo esamina le principali fonti di vulnerabilità e attacchi, dal principio di Kerckhoffs agli attacchi di hacker.
## 7.1 I principi di Kerckhoffs  

**Auguste Kerckhoffs**, un crittografo nato nei Paesi Bassi, scrisse nel suo saggio del 1883 *La Cryptographie Militaire* sei principi per la progettazione pratica dei cifrari:

1. Il sistema dovrebbe essere, se non teoricamente inviolabile, inviolabile nella pratica.
2. ==Il design di un sistema non dovrebbe richiedere segretezza, e la compromissione del sistema non dovrebbe mettere in difficoltà i corrispondenti.==
3. La chiave dovrebbe essere memorizzabile senza appunti e facilmente modificabile.
4. I crittogrammi dovrebbero essere trasmissibili tramite telegrafo.
5. L'apparato o i documenti dovrebbero essere portatili e utilizzabili da una sola persona.
6. Il sistema dovrebbe essere semplice, senza richiedere conoscenze di una lunga lista di regole né causare affaticamento mentale.

Nonostante abbiano più di 130 anni, alcuni di questi principi sono ancora validi.

### Primo principio

Un evergreen. È accettabile che il nostro sistema crittografico non sia perfetto; la perfezione è difficile da raggiungere, e gli attacchi a forza bruta sono sempre possibili. Tuttavia, qualsiasi attacco fattibile dovrebbe richiedere troppo tempo per essere eseguito, rendendo così le informazioni eventualmente ottenute inutili.

### Secondo principio

Come già menzionato nella sezione 1.6.1, il più importante tra questi sei principi, noto semplicemente come principio di Kerckhoffs, è il secondo, che afferma che la sicurezza basata sull'oscurità è una pessima idea.  
Non dovremmo mai utilizzare un sistema inutilmente complicato, poiché non dobbiamo fare affidamento sul fatto che un attaccante non sappia come funziona il sistema (potrebbe essere un tirocinante), e quando le informazioni sulla struttura del sistema trapelano, esso passa da sicuro a completamente insicuro. Inoltre, poiché la sicurezza risiede nel design, non possiamo nemmeno cambiarlo molto spesso.

*Esempio*  
Durante la Seconda Guerra Mondiale i tedeschi utilizzavano l'Enigma, una macchina estremamente complessa, per proteggere le loro comunicazioni. Quando i britannici trovarono una di queste macchine - nemmeno una versione completa, ma una ridotta - la decodificarono e riuscirono a violare l'intero sistema crittografico.

*Esempio*  
Ci sono aziende che condividono solo alcune parti delle schede tecniche dei loro dispositivi, rilasciando documentazione con pagine mancanti. Queste pagine, che solitamente contengono algoritmi crittografici o altre informazioni sensibili, vengono fornite ai clienti solo dopo la firma di un accordo di non divulgazione. Tuttavia, queste pagine possono spesso essere trovate su siti web russi. 
I sistemi industriali possono ancora basarsi sulla sicurezza tramite oscurità poiché dispongono di eserciti di avvocati: se qualcuno viola un tale sistema, questi si presenteranno alla sua porta molto rapidamente – e gli avvocati sono molto più temibili delle forze dell’ordine, specialmente quando chi ha violato il sistema è una persona comune e non una grande organizzazione.

### Terzo principio + Quarto/Quinto e Sesto
La sicurezza di un sistema risiede nella sua chiave. Questo era un buon principio 130 anni fa, ma oggi è meno rilevante poiché le operazioni sono svolte dai computer, che non hanno problemi a memorizzare chiavi lunghe.  
Va sottolineato che l’obiettivo di rubare le password degli account è creare database per poterli poi utilizzare in attacchi a forza bruta. Avere numeri, lettere e caratteri speciali nelle password non è più una garanzia di sicurezza; non è nemmeno la lunghezza della password a renderla forte. La forza della password risiede nella sua casualità e nel fatto che non dovrebbe essere collegata a nulla di già presente nel dizionario comune (e, inoltre, è sconsigliabile usare la stessa password su tutti i siti).

**Quarto principio**  
Irrilevante nel 2020.

**Quinto principio**  
Irrilevante nel 2020.

**Sesto principio**  
La crittografia non dovrebbe essere complessa dal punto di vista dell’utente.
## 7.2 Outsourcing 

L’*outsourcing* è un accordo in cui un’azienda assume un’altra azienda per occuparsi di un'attività pianificata o esistente che potrebbe essere svolta internamente, e a volte implica il trasferimento di dipendenti e risorse da una società all’altra.  
Oggi affidiamo costantemente servizi in *outsourcing* (ad esempio, sistemi cloud); molti sistemi e/o servizi (come una rete, lo storage, o un servizio) coinvolgono almeno tre entità: un cliente del servizio, un fornitore di servizi (che potrebbe anche esternalizzare a qualcun altro) e un operatore di rete.

- **Fornitore di servizi**: gestisce il servizio e i suoi componenti, che utilizzano l'infrastruttura di rete per raggiungere il cliente.
- **Cliente del servizio**: può personalizzare il servizio e i suoi componenti in base al contratto con il fornitore di servizi (solitamente solo nei limiti del framework fornito). ==Utilizza il servizio e non è interessato a come funziona la rete.==
- **Operatore di rete**: costruisce, mantiene e gestisce l'infrastruttura di rete, che deve rispettare la Qualità del Servizio (QoS) richiesta da ciascun servizio. Non dovrebbe essere coinvolto nel servizio.
### 7.2.1 Service Level Agreement  

Il *Service Level Agreement* (**SLA**) è un contratto scritto che stabilisce gli obiettivi di un servizio, le penalità per il mancato rispetto degli stessi e i limiti. In altre parole, definisce ciò che possiamo aspettarci da un servizio; pertanto, come analisti della sicurezza, dobbiamo verificare se sono presenti clausole su violazioni dei dati, sicurezza, crittografia e, naturalmente, privacy.  
L'SLA è firmato dall’utente (ad esempio **EULA**, *End-User License Agreement*) e può essere trovato tra l’utente e il fornitore di servizi. Tuttavia, non è raro avere un SLA anche tra il fornitore di servizi e l’operatore di rete, poiché se quest'ultimo non è coinvolto nell’accordo la sicurezza del sistema non può essere pienamente garantita.
#### Servizi verticali

È molto più semplice se il fornitore di servizi comunica con l'operatore di rete per specificare il tipo di QoS o protezione necessaria; ciò rende il servizio verticale.  
Un servizio verticale è dannoso per la concorrenza (e quindi un'idea poco valida, specialmente a lungo termine), poiché un fornitore che ha stretto un accordo con l’operatore di rete avrà un vantaggio sui concorrenti.

**Esempio**  
Non possiamo guardare Sky su una rete che non sia fornita da Fastweb.

![[Pasted image 20241107220842.png]]

#### Servizi orizzontali

Quando non c'è un SLA tra il fornitore di servizi e l'operatore di rete, si ottiene uno schema tipico dei servizi orizzontali, simile a quello che si potrebbe ottenere modificando la figura, come quelli costruiti su Internet. In questo caso, il cliente può utilizzare una varietà di servizi senza conoscere chi sia il proprio operatore di rete.

**Esempio**  
Se vogliamo guardare Hulu, Netflix, Sky, ecc., non dobbiamo preoccuparci di sapere chi sia il nostro operatore di rete; ci basta accedere a Internet e utilizzarli. Se usiamo Outlook Mail ma vogliamo passare a Gmail, possiamo semplicemente cambiare.

Questo schema favorisce la concorrenza, ma poiché nei servizi orizzontali l'operatore di rete non è coinvolto con il fornitore di servizi, dobbiamo avere un accordo solido con l'operatore di rete per ottenere la migliore qualità del servizio.

**Esempio**  
Supponiamo che normalmente navighiamo in Internet per leggere le e-mail, ma guardiamo anche la TV su Internet dalle 6 AM alle 2 AM. Possiamo informare il fornitore di servizi su ciò che stiamo facendo, ma non c'è modo di chiedere all'operatore di rete una maggiore larghezza di banda per i film (così da adattarsi al servizio che stiamo utilizzando in quel momento). L'operatore di rete non sa quali servizi stiamo utilizzando; potrebbe saperlo, ma non è suo compito e non è interessato. Purtroppo, dobbiamo negoziare con loro per ottenere buoni SLA per i nostri servizi.

In casi in cui è necessario un sistema estremamente sicuro, la regola generale è di non puntare su servizi completamente verticali, ma di firmare comunque un SLA tra l'operatore di rete e il fornitore di servizi. Questo perché, nonostante la sicurezza di un data center, il vero problema risiede nel sistema di trasporto, nella rete: un attaccante raramente si trova vicino alla fonte o alla destinazione, ma piuttosto da qualche parte nel mezzo.

### 7.2.2 Hacker

*Un hacker informatico è un qualsiasi esperto di computer che utilizza le sue conoscenze tecniche per superare un problema. Sebbene "hacker" possa riferirsi a qualsiasi programmatore esperto, il termine è associato nella cultura popolare con un "hacker di sicurezza", cioè qualcuno che sfrutta bug o exploit per accedere a sistemi informatici.*

L’uso del termine "hacker" risale agli anni ’60 ed è datato; indica qualcuno che è in grado di prendere un sistema, aprirlo (fisicamente), smontarlo e rimontarlo. Oggi questo termine non dovrebbe più essere usato, poiché è troppo generico per fini di sicurezza. Se qualcuno dice di essere stato attaccato da hacker, probabilmente non ha subito un attacco o non sa cosa significa.

Per comprendere meglio il nostro attaccante, ci riferiamo al "colore del cappello," che dà una buona caratterizzazione dello scopo di un attacco.

**Classi di hacker:**
- **White hat**: Non hanno intenzione di causare danni; sono le persone che smontano il sistema e ci dicono cosa non va.
- **Black hat**: Hanno l’intento di causare danni, possibilmente senza lasciare tracce.
- **Grey hat**: Attaccanti che a volte agiscono in modo etico (white hat) e altre volte in modo dannoso (black hat).
- **Blue hat**: Tirocinanti di un’azienda che lavorano contro un team rosso per testare la sicurezza dei sistemi.
- **Script kiddies**: Gli attaccanti meno esperti e pericolosi perché non sanno cosa stanno facendo.

Gli attacchi di **script kiddies** sono i più comuni e anche i più pericolosi, poiché sfruttano vulnerabilità note che spesso vengono dimenticate o trascurate negli aggiornamenti di sicurezza. Sebbene non siano generalmente pericolosi, sono molto fastidiosi per via della loro numerosità e possono accidentalmente causare danni significativi.

**Hacktivisti**  
Questi attaccanti sono estremamente pericolosi: hanno un obiettivo o un messaggio da trasmettere e spesso non considerano le reali conseguenze delle loro azioni.

**Esempi di hacktivismo:**
- Persone contrarie all'industria delle pellicce che liberano animali allevati per questo scopo, causando involontariamente danni all'ecosistema liberando specie non autoctone.
- Un gruppo noto di hacktivisti, Anonymous, ha condotto una campagna contro i pedofili, interrompendo i siti web di pedofilia. La polizia internazionale, a un certo punto, ha chiesto di interrompere queste azioni, poiché avevano distrutto anni di indagini mirate all’arresto di queste persone.

Gli hacktivisti possiedono mezzi e obiettivi, ma possono causare effetti collaterali significativi o, in alcuni casi, agire contro gli interessi di altre persone o istituzioni.

**Nazioni unite**

Organizzazioni governative come NSA, i servizi segreti israeliani, cinesi, russi e italiani dispongono di strumenti che sono al di fuori della nostra portata. Sebbene difendersi da uno di questi attori sia teoricamente possibile, nella pratica risulta inefficace: se vogliono accedere a un sistema, lo faranno. Esistono anche numerosi gruppi di hacking sponsorizzati da stati nazionali. I loro attacchi sono potenti, ben congegnati e difficili da contrastare. In un'analisi dei rischi per un sistema industriale, sarebbe necessario considerarli come una minaccia; tuttavia, spesso è più pratico ignorarli per motivi di costo e complessità, sperando di non doversi mai confrontare con loro.
### 7.2.3 Vulnerabilità

L'unico sistema privo di vulnerabilità è un computer spento, smontato e con ogni componente chiuso in una cassaforte in luoghi differenti. Anche così, però, non sarebbe completamente sicuro. Non esistono sistemi senza vulnerabilità e qualsiasi sistema davvero sicuro sarebbe inutilizzabile (poiché non esiste). Ogni applicazione contiene almeno un bug o un'istruzione superflua; per induzione, tutti i programmi potrebbero essere ridotti a una singola istruzione errata.

Le vulnerabilità nascono per vari motivi:
- per **progettazione**;
- per **cattiva progettazione**;
- per **cattiva implementazione**;
- per **errato deployment**;
- per **aggiornamenti di librerie/sistema operativo**.

#### Vulnerabilità per progettazione

Una vulnerabilità per progettazione deriva dal modo in cui il sistema è stato pensato. Questa vulnerabilità è nota e accettata; solitamente è giustificata da motivi di semplicità, compatibilità o altre ragioni simili. Eliminare questa vulnerabilità significherebbe spesso compromettere il funzionamento del sistema.

**Esempi di vulnerabilità per progettazione:**
- protocolli di scoperta delle risorse;
- ARP/NDP;
- NAT.

#### Vulnerabilità per cattiva progettazione

Una vulnerabilità per cattiva progettazione nasce da un errore o da una svista nel design del software. Spesso è il risultato di una cattiva implementazione di uno standard. Anche se il programmatore presta attenzione ad ogni singola riga di codice, la vulnerabilità può derivare da un’interpretazione incompleta o ambigua dello standard stesso, che potrebbe essere stato volutamente poco chiaro per avvantaggiare certi attori.

**Esempi di vulnerabilità per cattiva progettazione:**
- SAMBA (condivisione file di Windows);
- attacchi su esecuzioni speculative nelle CPU; (task eseguiti senza necessità per tecniche di ottimizzazione di un computer)
- errori nella sequenza di gestione delle eccezioni.

#### Vulnerabilità per cattiva implementazione

Queste vulnerabilità derivano dal fatto che i programmatori sono spesso sottopagati e i cicli di rilascio del software sono troppo rapidi. Una corretta implementazione richiederebbe più risorse e controlli accurati, ma le aziende non sono disposte a pagare il prezzo di un software robusto.

**Esempi di vulnerabilità per cattiva implementazione:**
- clausole if/then/else incomplete;
- copie di memoria non controllate;
- input non verificati.

Per mitigare questo tipo di vulnerabilità, si consiglia di scrivere test e documentazione adeguati, e di fornire ai programmatori risorse e tempo sufficienti per svolgere un buon lavoro.

#### Vulnerabilità per cattivo deployment

Un cattivo deployment si verifica quando chi implementa il sistema non ha considerato alcuni eventi previsti nel design, spesso per non aver letto la documentazione con attenzione. La contromisura principale è leggere attentamente il manuale.

#### Vulnerabilità dovute ad aggiornamenti di librerie/sistema operativo

Queste vulnerabilità non si trovano nell'applicazione stessa, ma nelle librerie o nel sistema operativo utilizzato. Sono più comuni di quanto si possa pensare.

**Esempi di vulnerabilità nelle librerie:**
- uso di funzioni deprecate o obsolete;
- numeri casuali che non sono realmente casuali.

Contromisure includono l'uso di container e la virtualizzazione, che isolano il sistema.

**Esempio**  
Durante lo sviluppo di un'applicazione in Python, è possibile utilizzare un ambiente virtuale per installare nuovi pacchetti senza compromettere quelli esistenti, garantendo che nulla possa interferire con il sistema sottostante se non esplicitamente voluto.

#### Altro sulle vulnerabilità

Una classificazione alternativa delle vulnerabilità è in base alla loro conoscenza:
- "Lo so già"
- "Accidenti, non lo sapevo".

Poiché le vulnerabilità sono estremamente importanti, esistono programmi che pagano le persone per trovarle (bug bounty, caccia alle vulnerabilità, ecc.). Trovare nuove vulnerabilità, tuttavia, non è semplice: richiede test approfonditi in un ambiente controllato per identificare i problemi e le vulnerabilità che ne derivano. Il compenso per la scoperta di una vulnerabilità può variare notevolmente, dal costo di una pizza a decine di migliaia di dollari.

Esistono database di vulnerabilità note, tra cui il più importante è il **CVE (Common Vulnerabilities and Exposures**). Il CVE è uno strumento per i sysadmin per verificare se il proprio sistema è vulnerabile e trovare le contromisure. (é sempre meglio avere un problema che conosciamo, e quindi sappiamo come evitare piuttosto che un sistema che non ha nessun problema ma che potrebbe avere problemi che non siamo a conoscenza)

# Capitolo 8: Chi è chi? Il problema dell'identità

**L'identità** è una componente fondamentale della sicurezza; non possiamo pensare di realizzare un sistema sicuro se non consideriamo questa problematica, poiché dobbiamo sapere chi è chi. L'idea di base della sicurezza è permettere alle persone autorizzate di svolgere le loro attività e impedire a tutti gli altri di fare le stesse cose, e questo richiede **identificazione**.

**Riepilogo**

Abbiamo visto nel capitolo 2 molti modi diversi per proteggere una comunicazione tra due (o più) persone o dispositivi:

- **HASH**: utile solo quando si usano canali differenti;
- **HMAC**: più sicuro dell'HASH, ma richiede una chiave segreta;
- **Crittografia simmetrica**: buona, ma richiede una chiave segreta e, soprattutto, non permette di identificare chi è chi (non possiamo fidarci di entrambe le estremità);
- **Crittografia asimmetrica**: buona, ma richiede ancora di identificare le parti coinvolte; inoltre, è più lenta della crittografia simmetrica.

Notare che avere una chiave segreta non significa che possiamo identificare persone o dispositivi; la chiave non dice nulla su chi siamo: chiunque la possieda può fingere di essere noi.
## **8.1 La questione dell'identità**

La **questione dell'identità** si riduce al problema principale di garantire che l'identità di una persona o di un dispositivo sia corretta e non contraffatta. In sostanza, vogliamo e abbiamo bisogno di sapere che, se qualcuno afferma di essere qualcun altro, ciò corrisponda a verità.

Il trucco per fare ciò è legare **qualcosa** all'identità di una persona, come una carta d'identità contenente una foto della persona stessa, che può essere successivamente utilizzata per identificarla.

**La questione dell'identità negli esseri umani**

Questo è un problema molto antico, legato a questioni amministrative. Chi ci assicura che il nostro amico sia la persona che dichiara di essere? Nessuno, in realtà. Ci fidiamo del fatto che sia chi dice di essere perché si è presentato in quel modo, e tutti gli altri lo chiamano con il nome con cui si è presentato.

Come esseri umani, siamo sempre identificati da qualcun altro: chi ci identifica dai nostri documenti abbina il nostro aspetto alla foto sulla nostra carta d'identità, confidando che il documento contenga informazioni corrette (supponendo che sia stato stampato correttamente, che abbia tutti i timbri necessari e che qualcuno presso l'ufficio municipale abbia verificato che tutto fosse in ordine). In ultima analisi, è sempre una questione di **fiducia**.

Durante un accesso al sistema, l'identificazione varia a seconda che siamo esseri umani o computer; gli esseri umani normalmente hanno più possibilità, tra cui le famigerate **tre** (a volte due) **modalità di autenticazione**:

1. Qualcosa che **sappiamo** (una password);
2. Qualcosa che **possediamo** (una smart card, un telefono, ecc.);
3. Qualcosa che **siamo** (un'impronta digitale o un altro metodo biometrico).

#### La questione dell'identità nei computer

Per quanto riguarda i computer, il modo migliore per identificarli è usare qualcosa che conoscono (una chiave segreta), perché è difficile chiedere loro qualcosa che possiedono (avrebbero bisogno di una periferica fisicamente collegata per farlo). È importante notare che le chiavi non sono una vera prova di identità, ma piuttosto un modo per discriminare tra dispositivi diversi; ci affidiamo alle chiavi perché generare due chiavi identiche è estremamente improbabile, ma il fatto che possiamo distinguere tra due o più dispositivi non significa che siano realmente chi affermano di essere.

Nei computer dobbiamo basarci su alcune ipotesi. Ad esempio, supponiamo che dal punto di vista amministrativo qualcuno garantisca che una chiave privata sia privata, e quindi che l'amministratore non abbia installato l'identità di qualcun altro e che la nostra identità sia stata installata solo sul nostro computer. Ma come possiamo essere sicuri che una certa chiave privata appartenga a un certo proprietario? Un modo per farlo è utilizzare le **impronte digitali**, una meta-informazione che va oltre la chiave e ci dice qualcosa sull'entità stessa (dispositivo, programma, ecc.).
Nelle telecomunicazioni, le **impronte digitali** sono parte di una chiave crittografica; non sono destinate a decriptare nulla, ma funzionano come un hash. La differenza principale tra un'impronta digitale e un hash è che, mentre l'hash prende in input un messaggio e restituisce un altro messaggio codificato, un'impronta digitale è semplicemente una parte della chiave segreta di qualcuno.
Le impronte digitali sono sempre contenute nelle **chiavi pubbliche**, in modo che il proprietario possa distribuirle a quanti più utenti possibile, permettendo così a persone e dispositivi di identificare il proprietario stesso e rendendo difficile per gli attaccanti interferire con esse. Un attaccante potrebbe modificarne alcune, ma non tutte le impronte digitali esistenti. Naturalmente, questo metodo è affidabile solo finché il destinatario verifica attivamente l'impronta digitale; altrimenti, potrebbe riceverne una manomessa senza accorgersene.
In pratica: hashiamo la chiave insieme ad altri dati (come la lunghezza della chiave, il metodo di cifratura, ecc.) e usiamo il risultato come impronta digitale. Questo metodo è migliore rispetto all'uso diretto della chiave perché è **molto più breve**: mentre una chiave privata è solitamente lunga 256 byte, un'impronta digitale SHA1 è lunga solo 20 byte.
## **8.2 Rete di fiducia**

Un modo per gestire l'identità nei sistemi informatici è creare una "rete di fiducia" (**Web of Trust**). Questa struttura non è un’entità centralizzata, bensì un sistema decentralizzato in cui le persone o i dispositivi certificano reciprocamente la loro identità.
Ogni utente crea una coppia di chiavi **pubblica/privata** e utilizza la chiave privata per firmare digitalmente documenti, messaggi o altre chiavi pubbliche. L'identità è quindi garantita dalla fiducia che gli altri utenti hanno nei confronti della chiave pubblica e della firma di un utente.

In una **rete di fiducia**:
- Le persone garantiscono l'autenticità delle chiavi altrui.
- Gli utenti possono decidere in chi o cosa riporre fiducia in base alle firme ricevute.

![[Pasted image 20241124161717.png]]

Il problema con le reti di fiducia è che un **gruppo sufficientemente** grande può sovvertirle, cioè può introdurre nel sistema elementi che saranno considerati autentici da altre persone. In sostanza, confidiamo nel fatto che altre persone non abbiano firmato un documento falsificato (è una fiducia condivisa), ma quando un numero sufficiente di persone crede a un documento falsificato, perché in qualche modo sono state ingannate, anche altri che si fidano di loro saranno ingannati, perché stanno riponendo fiducia nelle persone sbagliate. In questi casi, non c'è nessuno da incolpare se riceviamo informazioni errate: non si tratta di un problema tecnico, ma di una questione amministrativa.
## **8.3 Certificati**

Un **certificato** non è firmato da pari, ma da un'Autorità di Certificazione (**CA**, Certification Authority). Invece di avere chiavi private e pubbliche, un certificato contiene alcune informazioni (scritte nel formato **X.509** --> formato di standard di networking) firmate da un'entità superiore, considerata affidabile da tutti (e che può essere ritenuta responsabile in caso di errore), la quale è stata delegata a verificare l'autenticità di un documento. Per questo motivo, i certificati hanno una singola firma (invece di più firme, come nelle reti di fiducia) - non perché sia più forte, ma perché l'entità superiore è considerata più affidabile rispetto ai nostri pari.
Vediamo com’è fatto un certificato; anche se la sua struttura non è fondamentale, può aiutarci a capire meglio come funziona. La figura mostra un tipico certificato; le parti in giallo sono comuni a tutte le versioni, quelle in blu sono disponibili solo nella seconda versione dello standard, mentre le estensioni sono supportate solo dalla terza versione. 

![[Pasted image 20241124162810.png]]

Esistono tre versioni di certificati, tutte retrocompatibili (le versioni più vecchie ignorano semplicemente le parti che non comprendono). Analizziamo nel dettaglio ogni componente di un certificato:
- **Versione**: la versione utilizzata per il certificato (prima, seconda o terza);
- **Numero di serie**: il numero del certificato; non è univoco a livello globale, ma solo tra i certificati emessi da quella specifica autorità;
- **ID dell'algoritmo di firma**;
- **Nome X.500 dell'emittente**: il nome della CA (ad esempio, Poste Italiane, VeriSign, ecc.), nel formato **X.500**;
- **Periodo di validità**: i certificati hanno una data di scadenza, dopo la quale non sono più validi;
- **Nome X.500 del subject**: questo è il motivo principale dell'esistenza di un certificato: associa la chiave pubblica del soggetto con il suo nome (un esempio potrebbe essere il seguente: il nome del soggetto è _[www.dinfo.unifi.it](http://www.dinfo.unifi.it/)_, la sua chiave pubblica è "public key" , e il nome X.500 del subject è "public key info");
- **Informazioni sulla chiave pubblica del soggetto**: include informazioni sulla chiave pubblica del soggetto (algoritmo utilizzato, dimensione della chiave, uso della chiave e la chiave pubblica stessa);
- **ID univoco dell'emittente**: necessario per evitare ambiguità tra gli emittenti;
- **ID univoco del soggetto**: necessario per evitare ambiguità tra i soggetti;
- **Estensioni**: estensioni al certificato che contengono informazioni aggiuntive;
- **Firma digitale della CA**: proprio come nelle reti di fiducia, questa firma è considerata autentica perché la CA ha generato un hash del certificato stesso, lo ha cifrato con la sua chiave privata e lo ha inserito in questo campo.

Il **periodo di validità** è molto importante, perché implica che, trascorso un certo tempo, il certificato non può più essere considerato affidabile. Questo è necessario poiché la chiave pubblica di un certificato, data una sufficiente quantità di tempo, potrebbe essere violata da un attaccante; invalidare il certificato dopo un certo periodo garantisce che gli attaccanti non abbiano avuto abbastanza tempo per trovare una chiave privata corrispondente a quella pubblica.

### **8.3.1 Uso dei certificati**

I certificati sono semplici: l'utente genera una chiave asimmetrica, quindi la chiave e l'identità dell'utente vengono firmate dalla CA. Invece di inviare solo una chiave pubblica, inviamo un certificato che, oltre alla chiave pubblica, contiene ulteriori informazioni sulla nostra identità, consentendo una migliore identificazione. Ovviamente, se possediamo la chiave privata corrispondente, abbiamo una vera identità.

**Come verificare se il certificato è valido?**  
Possiamo ricalcolare la firma digitale della CA e verificare se l'hash è corretto. Se il certificato è stato creato con la chiave privata della CA, possiamo utilizzare la chiave pubblica della CA per decifrarlo e vedere se tutto corrisponde. Ma a questo punto, come possiamo assicurarci che la chiave pubblica fornita dalla CA sia affidabile? Sembra proprio una situazione simile a un cane che si morde la coda.
**La soluzione a questo problema** è che noi possediamo già la chiave pubblica della CA, preinstallata nel nostro computer dal sistema operativo.
È ovvio che il sistema operativo debba essere affidabile (ovvero non compromesso in alcun modo), perché se riceviamo la chiave di una CA fasulla, automaticamente ci fideremo di qualsiasi certificato firmato da quella CA, rendendo molto felice un attaccante. Per questo motivo, dovremmo sempre installare gli aggiornamenti di sicurezza, che spesso **contengono nuove chiavi di CA** per sostituire quelle vecchie o scadute.
Dal punto di vista tecnico, i certificati non sono migliori delle reti di fiducia, ma consentono comunque di avere qualcuno da incolpare quando le cose vanno storte.
### **8.3.2 Revoca**

I certificati possono essere eliminati per molte ragioni: la CA ha cessato le operazioni, il loro sito è stato disattivato, ecc., e quindi dobbiamo invalidare un certificato. Il problema è che chiunque abbia ancora quel certificato può trasmetterlo nuovamente, e non possiamo semplicemente dire a tutti di smettere di usarlo (ci sarebbero troppe persone coinvolte e non sapremmo nemmeno chi lo sta utilizzando). Il certificato deve quindi essere revocato attraverso una **Certification Revocation List (CRL)** ospitata dalla CA, verificando ogni volta se il certificato che stiamo usando è presente in quella lista.
Dovremmo sempre chiedere alla CA se un certificato è valido; tuttavia, ciò comporta alcuni svantaggi:
- Invece di avere una comunicazione diretta tra A e B, coinvolgiamo anche la CA, il che significa una connessione più lenta.
- Aumenta il traffico verso la CA.
- Comporta una perdita di privacy. Ad esempio, se chiediamo alla CA se il certificato della nostra banca è valido, la CA saprebbe quante persone stanno utilizzando una certa banca. Questa è un'informazione preziosa e potrebbe anche essere utilizzata per raccogliere dati simili a quelli dei DNS o dei browser web, che sono in grado di tracciare la nostra cronologia di navigazione a livello di dominio.
### **8.3.3 CA compromesse**

Una **Autorità di Certificazione (CA) compromessa** (cioè, la chiave privata della CA è finita nelle mani sbagliate) rappresenta un enorme problema, perché chiunque possieda questa chiave può creare certificati per chiunque e qualsiasi cosa (letteralmente qualsiasi cosa). Questo significa che la CA deve garantire che le sue chiavi private rimangano segrete e che non vengano mai utilizzate per generare certificati falsi (cosa che è già successa molte volte).
Se una CA compie azioni discutibili, rischia un **ban pubblico** su Internet. Ad esempio, i browser web potrebbero smettere di accettare i certificati emessi da quella CA oppure potrebbero essere rimossi dai sistemi operativi.
### **8.3.4 Uso dei certificati nei browser**

I certificati vengono utilizzati principalmente nei browser, nel protocollo **HTTPS** (**Hypertext Transfer Protocol Secure**). HTTPS è un'estensione del protocollo Hypertext Transfer Protocol (**HTTP**) utilizzata per comunicazioni sicure su una rete ed è ampiamente utilizzata su Internet. In pratica, il protocollo di comunicazione viene cifrato utilizzando il **Transport Layer Security (TLS)** (o, precedentemente, il **Secure Sockets Layer, SSL**), ed è quindi anche noto come HTTP su TLS (o HTTP su SSL).
In pratica, invece di creare un socket TCP per comunicare end-to-end, si crea un socket TLS, che si trova tra il livello applicativo (livello 7) e il protocollo TCP. **TLS è un protocollo enorme**: svolge molte funzioni e, tra le altre cose, crea un canale sicuro (non necessariamente cifrato).
Tutte le versioni di TLS utilizzano i certificati. I socket TLS, tuttavia, funzionano esattamente come un socket TCP (eccetto per l'inizializzazione, dove dobbiamo specificare cose come la versione di TLS che vogliamo utilizzare, se vogliamo fidarci solo del certificato che ci viene inviato o se entrambe le parti devono presentare certificati, se dobbiamo identificare chi ha inviato il certificato, ecc.).
È possibile utilizzare TLS non solo nei browser web, ma anche per protocolli come **e-mail, IMAP, SMTP**, e così via. I certificati, quindi, non sono limitati solo ai browser.

# Capitolo 11: Metodi di autenticazione

I metodi impiegati dal protocollo Wi-Fi non sono autentiche forme di autenticazione, anche se vengono chiamati così. Si basano semplicemente sul fatto che un determinato utente conosca un segreto, ma non autenticano realmente nessuno perché non verificano l'identità di un utente (il "qualcosa che sanno" non è un'informazione privata dell'utente, ma una conoscenza condivisa da un gruppo).

Abbiamo già esaminato alcuni metodi di autenticazione e abbiamo sottolineato che le idee di base rientrano in tre ampie categorie di conoscenza:

1. **Qualcosa che sappiamo:** di gran lunga il modo più semplice e comune di autenticazione, ma anche il più debole.
    - **Esempi:** nome utente e password, chiavi pubbliche e private.
2. **Qualcosa che siamo:** intuitivamente molto robusto, ma in realtà piuttosto complesso e dipendente dalla soluzione scelta; è anche costoso.
    - **Esempi:** autenticazione biometrica (sensori di impronte digitali, lettori oculari).
3. **Qualcosa che possediamo:** un'altra buona soluzione, ma per definizione potrebbe essere smarrita.
    - **Esempi:** penne USB.

In sicurezza, dobbiamo sempre ricordare quali sono i nostri **obiettivi**. L'obiettivo dell'autenticazione non è di per sé uno scopo finale: è semplicemente un mezzo per ottenere l'autorizzazione. Per questa ragione, i protocolli di autenticazione sono chiamati protocolli **AAA**: **autenticazione, autorizzazione e accounting**. Autentichiamo un utente perché abbiamo bisogno di decidere se ha i diritti per utilizzare una risorsa.
## **11.1 Storia**

- **1969: Telnet**
    - Autenticazione per utente, nessuna crittografia (tutti erano considerati amici e gli ingegneri facevano le cose nel modo più semplice e diretto possibile).
- **1988: SNMP v1**
    - Autenticazione per gruppo, nessuna crittografia (ritenuta non necessaria).
- **1993: SNMP v2c**
    - Autenticazione per gruppo, crittografia debole (iniziava a sentirsi la necessità di una maggiore protezione).
- **1995: SSH v1**
    - Autenticazione per utente, crittografata (gli ingegneri si resero conto che potevano esserci persone malintenzionate nei loro canali).
- **1997: WEP**
    - Autenticazione per gruppo, crittografata (anche se sappiamo quanto male fosse implementata).
- **2002: SNMP v3**
    - Autenticazione per utente/per gruppo, crittografata.
- **2003: WPA**
    - Autenticazione per utente/per gruppo, crittografata.

I primi sistemi, più semplici (Telnet, SNMP v1), sono buoni esempi di ciò che non dovremmo più usare oggi: Telnet inviava password e nomi utente in chiaro sul canale (canali insicuri), mentre SNMP v1 utilizzava anche l'autenticazione per gruppo.

L'autenticazione per gruppo è un segreto condiviso da tutto il gruppo, ed è quindi un'idea pessima per definizione. Per passare a un'autenticazione per utente, possiamo assegnare a ciascun utente un ID e una password, anche se tecnicamente non è sufficiente, poiché l'autenticazione dovrebbe essere bidirezionale e identificare entrambe le parti coinvolte (l'utente e il server/fornitore del servizio).

Fortunatamente, questi protocolli sono stati presto abbandonati per introdurre almeno un po' di crittografia, in modo da non inviare informazioni sensibili su un canale insicuro senza prima cifrarle; SSH è un buon esempio. Anche se proteggere un canale prima dell'autenticazione non è banale, è possibile farlo negoziando una **chiave temporanea** (come nel caso dell'algoritmo Diffie-Hellman) o implementando un **meccanismo di sfida** a cui l'utente deve rispondere con una combinazione del proprio nome utente e password. Lo stesso può essere fatto utilizzando chiavi pubbliche e private o persino certificati.

**Nota:** la prima volta che ci connettiamo a un server, non possiamo sapere con certezza se è quello giusto o no; se abbiamo installato noi stessi il server, possiamo verificare l'impronta digitale (**fingerprint**); a volte è possibile consultarla altrove su Internet. Tuttavia, si tratta di un'impronta digitale e non di un certificato, quindi deve essere verificata manualmente da un essere umano: non è possibile farlo su vasta scala né automatizzarlo.

**Esempio:**  
La prima volta che qualcuno stabilisce una connessione SSH, il terminale comunica all'utente la chiave segreta del computer su cui sta operando, mostrando una grande quantità di byte: questa è l'impronta digitale della chiave pubblica del server a cui l'utente si sta connettendo. Tale impronta dovrebbe essere memorizzata in modo sicuro per poterla verificare successivamente e prevenire situazioni in cui, se un altro computer rubasse l'indirizzo IP del server, l'utente invierebbe dati a una macchina diversa.

L'idea di autenticazione e autorizzazione degli utenti è antica quanto i computer, ma, soprattutto nei primi giorni di Internet, non era considerata una questione urgente. Al contrario, è sempre stata una questione estremamente importante e urgente nelle reti domestiche (le classiche reti telefoniche), perché le telecomunicazioni dovevano sapere chi fosse chi per implementare una fatturazione efficace per i loro clienti. Per lungo tempo, le telecomunicazioni hanno fatturato in modo poco trasparente; il telefono è stato (e in realtà lo è ancora, insieme a Internet) uno dei pochi servizi in cui gli utenti devono fidarsi del loro provider per la fatturazione, non avendo alcuna possibilità di verificare cosa venisse loro addebitato (non esistono contatori fisici accessibili agli utenti).

Su Internet, gli ingegneri erano più interessati a far funzionare le cose che a garantire un'operatività corretta e sicura, quindi persino protocolli come Telnet implementavano l'autenticazione per utente solo come conseguenza del fatto che, essendo un accesso remoto, i computer che accedevano ne erano già dotati.

Quando doveva essere inventato qualcosa da zero, come in SNMP, la parte di autenticazione è stata completamente ignorata a favore di un metodo di autorizzazione.

Per funzionare, il requisito principale di SNMP non è dichiarare chi siamo, ma se siamo abilitati a fare qualcosa (ad esempio, se siamo un utente che può solo visualizzare i dati o un amministratore che può modificare la configurazione). **Nota:** questo non è una forma di autenticazione, ma di autorizzazione: stiamo semplicemente affermando di far parte di un gruppo con un certo tipo di autorizzazione (l'autenticazione di gruppo in realtà non esiste).  
La vera autenticazione identifica un singolo utente o dispositivo, e la necessità di questo tipo di autenticazione è emersa meno di 20 anni fa (non molto tempo per gli standard Internet), quando si è scoperto che gli attacchi erano più comuni di quanto si pensasse. Mentre ci difendevamo da questi attacchi, abbiamo anche dovuto proteggerci da attacchi interni, e quindi l'autenticazione è diventata diffusa, poiché consente di riconoscere efficacemente chi sta facendo cosa.
## **11.2 Requisiti di un sistema di autenticazione**

In generale, dobbiamo sempre verificare attentamente i **requisiti aziendali**, poiché non tutte le politiche sono valide ovunque, e alcuni requisiti dell'architettura aziendale possono richiedere meno lavoro del previsto.

**Esempio**  
Supponiamo di gestire un Internet café e vogliamo fornire Internet a tutti; poiché non siamo vincolati da leggi o altri requisiti, siamo liberi di fare ciò che vogliamo. Possiamo quindi offrire una connessione Internet/Wi-Fi aperta senza password, perché non ci interessa l'autenticazione. Tuttavia, le leggi locali potrebbero richiedere che siamo in grado di tracciare l'attività degli utenti, e quindi dovremmo implementare account per utente.

In breve, vogliamo un’autenticazione per utente che possa autenticare esseri umani, dispositivi o persino processi (poiché una persona può avere più di un dispositivo, e i dispositivi possono eseguire più processi contemporaneamente).

**L’autorizzazione deve sempre essere separata dall’autenticazione**. Questo è un concetto molto importante, anche se queste due nozioni vengono spesso confuse. Il fatto che il sistema riconosca un utente non significa che abbia i diritti per fare ciò che altri utenti possono fare.

- **Autenticazione**: distingue le persone o i dispositivi.
- **Autorizzazione**: determina chi può fare cosa.

**Esempio**  
Gli studenti che accedono alla rete Wi-Fi di un’università dovrebbero avere diritti diversi rispetto a un ospite autenticato o a un professore, poiché i loro ruoli sono diversi: questa è una questione di autorizzazione.

Un altro requisito fondamentale è che aggiungere utenti **dovrebbe essere semplice**; nella pratica, spesso non lo è, ma non dovrebbe nemmeno essere un processo drammaticamente complesso. Rimuovere un utente (ad esempio revocare la sua autorizzazione) dovrebbe essere ancora più facile e senza richiedere l'interazione dell'utente.
Ad esempio non possiamo escludere qualcuno da una casa se gli diamo una chiave fisica, perché poi dovremmo richiedergli di restituirla e assicurarci che non ne abbia duplicati.

La crittografia deve essere completamente separata dal materiale di autenticazione e autorizzazione. Quello che usiamo per autenticarci potrebbe essere un segreto, ma non deve avere nulla a che fare con le chiavi utilizzate per cifrare il sistema. Ricorda che questa distinzione è drammatica rispetto a WEP, dove la chiave utilizzata per autenticare un gruppo era parte del sistema di crittografia - una soluzione alquanto folle, e sappiamo come è finita.
Questo requisito è necessario perché un dispositivo compromesso non dovrebbe essere in grado di danneggiare l'intero sistema, ma solo il dispositivo stesso o i processi in esecuzione su di esso.

**Esempio**  
Se salviamo le password Wi-Fi sul nostro telefono e qualcuno le accede, la perdita danneggia tutti gli altri utenti nel sistema, poiché anche loro dovranno cambiare le password Wi-Fi.

L’autenticazione dovrebbe sempre essere bidirezionale, per evitare che utenti legittimi vengano ingannati da attaccanti che si spacciano per qualcun altro.
### **11.2.1 Riepilogo della progettazione di un sistema di autenticazione**

1. **L'autenticazione dovrebbe essere centralizzata:**  
    Dobbiamo poter fare affidamento sul fatto che un server (non necessariamente un singolo computer, ma un punto unico di servizio) sia in grado di dirci se un utente è conosciuto (**autenticazione**) e se può fare qualcosa (**autorizzazione**).
    
2. **Autenticazione e autorizzazione sono diverse:**  
    L'autenticazione viene per prima, mentre l'autorizzazione si basa sul fatto che l'autenticazione non sia fallita.
    
3. **Autenticazione e autorizzazione non sono semplici:**  
    Il sistema sarà difficile da implementare, anche se, una volta messo in funzione, funzionerà senza troppe complicazioni successive.
    
4. **Revocare un'autorizzazione** significa che sappiamo ancora chi è l'utente, ma non gli permettiamo più di fare determinate cose. **Revocare un'autenticazione**significa che non sappiamo più chi sia l'utente. Tuttavia, l'effetto netto è lo stesso.

5. La crittografia deve utilizzare **chiavi generate dinamicamente** e **chiavi temporanee.**
    
6. **L'autenticazione dovrebbe essere sempre reciproca.**

Tutto ciò è complesso. Come sempre, dobbiamo valutare attentamente se queste misure di sicurezza siano necessarie e utili per un'organizzazione.  
Lo implementeremmo per la **rete domestica** Probabilmente no.  
Sarebbe necessario per una grande **azienda IT**? Assolutamente sì.

## **11.3 IEEE 802.1X: l'architettura definitiva**

**IEEE 802.1X** è uno standard IEEE parte del gruppo di protocolli di rete **IEEE 802.11** e fornisce un meccanismo di **autenticazione** per i dispositivi che desiderano connettersi a una LAN o WLAN. È il sistema di autenticazione e autorizzazione più utilizzato, complesso e testato.

**Nota:** 802.1X non è un protocollo. È invece un **framework** (un'architettura), e come ogni altro framework si basa su più protocolli ed entità, sebbene lo standard stesso sia architetturale: definisce solo gli elementi e gli scambi di dati tra di essi. Per questo motivo, i punti più importanti sono le ipotesi fatte su questi elementi: dobbiamo leggere attentamente le parti dettagliate dello standard, altrimenti potremmo finire con qualcosa che formalmente segue lo standard, ma praticamente è completamente sbagliato.

Un altro equivoco comune: **802.1X non è Wi-Fi**. Non è stato creato per esso. 1X è stato concepito prima del Wi-Fi ed è stato successivamente adottato con la revisione **11i** nel 2004, la stessa che ha introdotto WPA e WPA2 (in pratica, quando siamo passati da WEP a WPA abbiamo anche avuto la possibilità di utilizzare 1X sul Wi-Fi, ma 1X esisteva già all'epoca).
1X funziona altrettanto bene per autenticare sia dispositivi che esseri umani e, in generale, copre un ampio spettro di utilizzi.

### **11.3.1 Astratto e terminologia**

*Questo prodotto degli standard IEEE fa parte della famiglia **802** per LAN/MAN.
Il controllo dell'accesso alla rete basato sulle porte utilizza le caratteristiche di accesso fisico delle infrastrutture **LAN IEEE 802** per fornire un mezzo di autenticazione e autorizzazione dei dispositivi connessi a una porta LAN con caratteristiche di connessione punto-punto, e per impedire l'accesso a tale porta nel caso in cui il processo di autenticazione e autorizzazione fallisca.*

Questa architettura utilizza almeno tre attori (**elementi attivi**; si noti che la terminologia è fondamentale):

- **Supplicant (richiedente):**  
    Entità a un'estremità di un segmento LAN punto-punto che cerca di essere autenticata da un autenticatore collegato all'altra estremità di quel collegamento; da notare che tra il supplicant e l'altra estremità c'è un mezzo unico, indiviso e non condiviso (802.1X su mezzi condivisi richiede ulteriori sviluppi).
    
- **Authenticator (autenticatore):**  
    Entità che facilita (ma non esegue) l'autenticazione di altre entità collegate alla stessa LAN.
    
- **Authentication server (server di autenticazione):**  
    Entità che fornisce un servizio di autenticazione a un autenticatore. Questo servizio determina, a partire dalle credenziali fornite dal supplicant, se quest'ultimo è autorizzato ad accedere ai servizi forniti dal sistema in cui risiede l'autenticatore.

**Esempio**  
Nel Wi-Fi, l'autenticatore è il punto di accesso (**access point**), mentre il servizio fornito dal sistema in cui risiede l'autenticatore è la rete Wi-Fi. Si noti che nella terminologia 802.1X, un **punto di accesso** designa qualsiasi punto di ingresso alla rete.

**Nota:**  
Lo standard parla di servizi generici, senza specificare chiaramente quali siano, in quanto questi dipendono dal tipo di autorizzazione di ciascun utente.
### **13.3.2 802.1X in pratica**

I **supplicant** utilizzano il protocollo **EAP** (framework di autenticazione per l'uso e il transporto dei parametri generati dai metodi EAP) per scambiare dati con il server di autenticazione tramite l'autenticatore stesso. EAP viene incapsulato in altri protocolli; quando questa comunicazione termina, l'autenticatore sarà in grado di sapere cosa il supplicant è autorizzato a fare (ad esempio, accedere a Internet o a determinati dispositivi/servizi nella LAN). L'obiettivo principale è infatti determinare se l'utente è autorizzato (o meno) a utilizzare le risorse disponibili.

![[Pasted image 20241127081636.png]]

Anche se potrebbero esserci più autenticatori, i supplicant comunicano con uno solo alla volta. Lo stesso vale per il server di autenticazione, che rappresenta un punto su cui l'autenticatore può fare affidamento per il servizio di autenticazione, ma potrebbe essere costituito da una federazione di server o qualcosa di simile (questo non è rilevante per lo standard).

Il canale di comunicazione tra autenticatore e server è sicuro, il che significa che l'identità del server di autenticazione e dell'autenticatore, tra loro, è ben nota in anticipo: nessun attaccante potrebbe intercettare o iniettare dati in questo canale. Da notare che questo livello di sicurezza può essere raggiunto con qualsiasi mezzo, poiché la sua implementazione non fa parte dello standard.  
**Praticamente parlando**, potremmo avere una VPN, un canale TLS, o persino un dispositivo/rete fisicamente sicuro, come un cavo Ethernet protetto da un cubo di ferro, squali, laser, coccodrilli, o qualsiasi altra cosa. Se il canale attraversa aree insicure, allora deve essere protetto con altri mezzi.

Il canale tra supplicant e autenticatore è privato dopo l'autenticazione; anche se potrebbe non essere già sicuro, non è comunque condiviso, perché i dati che vi transitano (l'identità del supplicant e il modo in cui sta effettuando l'autenticazione) sono critici e non protetti. Poiché non possiamo stabilire un canale sicuro e autenticato prima dell'autenticazione, ciò significa che il canale tra supplicant e autenticatore deve essere protetto tramite un metodo generico (anche un'autenticazione precondivisa o simulata) per garantire un minimo di riservatezza durante il processo di autenticazione.

**Esempio:**  
Un canale Wi-Fi è condiviso fino a quando non vengono effettuate autenticazione e autorizzazione. Al contrario, cercare di autenticarsi su uno switch Internet non richiede questa prima fase, perché c'è una connessione fisica tra le parti (dipende comunque dal contesto; tuttavia, le probabilità che un attaccante possa intercettare dati su un cavo Ethernet integro e ben funzionante sono praticamente nulle).
### **11.3.3 Protocolli 802.1X**

I protocolli che fanno parte dello standard 802.1X sono due:

- **EAP (Extensible Authentication Protocol):**  
    Definisce come il **supplicant** e il server di autenticazione scambiano i dati necessari per autenticarsi reciprocamente. Essendo un protocollo estendibile, non definisce un **unico** metodo di autenticazione, ma un'intera classe di metodi di autenticazione.  
    Di per sé, EAP definisce solo gli scambi di dati, mentre i protocolli effettivamente utilizzati per chiarire l'identità del supplicant o del server dipendono da ulteriori specifiche (esistono diverse varianti di EAP, alcune più robuste di altre).
    
- **EAPOL (EAP over LAN):**  
    È il metodo utilizzato da EAP per proteggere gli autenticatori interni quando si trovano in un mezzo condiviso. EAPOL può essere evitato se siamo sicuri che non ci siano attaccanti all'interno del mezzo.

In realtà esiste un terzo protocollo, **RADIUS/Diameter**, che però potrebbe essere sostituito da qualsiasi protocollo **AAA** in grado di scambiare i dati EAP tra autenticatore e server. Questo terzo protocollo è necessario perché EAP definisce solo come vengono generate e scambiate le credenziali, ma non specifica come queste vengano trasmesse dall'autenticatore al server.  
Da un'altra prospettiva, EAP ci dice cosa sono i dati, mentre RADIUS/Diameter si occupa di trasmettere i pacchetti.

**Storia dei principali protocolli AAA:**

- **TACACS:**  
    Ormai obsoleto, non merita nemmeno di essere menzionato.
    
- **RADIUS:**  
    Il più utilizzato al giorno d'oggi; è stato in uso per lungo tempo e ha dimostrato di avere alcune vulnerabilità dovute a un design non perfetto (anche se esistono mitigazioni).
    
- **Diameter:**  
    La seconda e migliore versione di RADIUS. È molto più complesso, rendendo la sua accettazione controversa e ostacolata. A differenza di RADIUS, supporta nativamente federazioni di server di autenticazione.
### **Note finali**

Dopo che l'autenticazione e l'autorizzazione sono state eseguite, c'è una fase in cui lo standard **802.1X** prevede che, a seconda dell'applicazione specifica, il server di autenticazione scambi con il supplicant e l'autenticatore alcuni materiali crittografici che consentiranno loro di continuare senza il server stesso. Durante tutto questo processo, l'autenticatore non vuole e non sa (in realtà non lo saprà mai) chi è il supplicant, ma solo cosa è autorizzato a fare.

**Esempio**  
Prendiamo un sistema Wi-Fi: il server di autenticazione terminerà la fase di autenticazione fornendo al client (il supplicant) le informazioni necessarie per consentirgli di negoziare con l'autenticatore alcune chiavi crittografiche senza trasmetterle in chiaro sul canale, e invierà lo stesso materiale all'autenticatore. In questo modo, autenticatore e supplicant potranno procedere autonomamente.

Un altro punto che spesso viene dimenticato è che il server comunicherà all'autenticatore cosa il client può fare. Non si tratta solo di dire: "Ho trovato l'utente, ecco alcuni dati per creare un canale sicuro", ma piuttosto di: "Ho trovato l'utente, ecco cosa può fare sul sistema ed ecco i dati necessari".  
Questo significa che il server di autenticazione è in grado di dire all'autenticatore, tramite **RADIUS** o **Diameter**, quali sono le configurazioni dell'utente in termini di:

- configurazioni del firewall;
- reti disponibili;
- priorità dei pacchetti;
- utilizzo di determinati protocolli;
- larghezza di banda massima che può usare, ecc.

Tutto ciò è legale ed è l'uso previsto dallo standard **802.1X**: informare l'autenticatore sui permessi dell'utente. Se non facciamo questo, stiamo usando solo una parte del protocollo (l'autenticazione), ignorando l'autorizzazione, il che equivale a "usare un cannone per uccidere una zanzara".  
**Ironia della sorte**, praticamente tutto ciò che implementa **802.1X** fa esattamente questo: utilizza solo la parte di autenticazione.

La morale è che dovremmo sempre conoscere tutte le funzionalità dei nostri strumenti e usarle di conseguenza.

# Capitolo 9: I Firewalls

Un **firewall** è un dispositivo, hardware o software, situato tra due aree di una rete con diversi livelli di fiducia. Non è soltanto qualcosa che si interpone tra una rete e Internet, ma rappresenta una componente fondamentale per la sicurezza di una rete, specialmente nelle reti IPv6 (a causa dell’autoconfigurazione).

I firewall dispongono di un'interfaccia semplice che specifica quale tipo di traffico può o non può attraversarli. Tuttavia, costituiscono un singolo punto di vulnerabilità, poiché ogni singolo pacchetto di traffico deve passarvi attraverso. Di conseguenza, se qualcuno riesce ad aggirarli, diventano completamente inutili. Per questa ragione, è essenziale che un firewall sia estremamente **resistente** a qualsiasi tipo di attacco, il che significa che deve essere ridondante e assolutamente affidabile; la configurazione di un firewall è complessa e non dovrebbe mai essere effettuata da persone non esperte.

I firewall più semplici separano una rete locale (con un alto livello di fiducia) da Internet (con un livello minimo di fiducia). Tuttavia, è possibile che vengano utilizzati anche tra due aree della stessa rete, come un’area amministrativa e un’area tecnica, che hanno un firewall a separarli. In generale, potremmo aver bisogno di più firewall di quanto inizialmente si possa pensare.
## 9.1 **Tipi di firewall**

Esistono tre tipi di firewall:

- **Packet filter firewall**: il firewall più semplice, ispeziona ogni pacchetto e decide, in base a determinate regole, se può passare o meno (è una macchina priva di memoria; completamente obsoleto).
- **Stateful firewall**: molto più complesso, è una macchina con stato (possiede memoria) e può decidere se un pacchetto può passare o meno in base a ciò che è accaduto in precedenza nei **livelli 3 e 4** (IP e TCP; l’unico firewall accettabile da utilizzare).
- **Application layer firewall**: una macchina ancora più complessa, che verifica i pacchetti fino al **livello 7**, ossia il livello dell’applicazione, ispezionando i dati trasmessi a questo livello (viola la privacy per definizione e non dovrebbe essere utilizzato).

Per funzionare, i firewall a livello applicativo devono conoscere il protocollo del livello applicativo utilizzato. Questo significa che devono comprendere non solo i protocolli pubblici/standard, ma anche quelli proprietari (poiché devono decodificarli e ispezionare i dati). Quando viene creato un nuovo protocollo o quando un protocollo esistente subisce anche solo lievi modifiche, i firewall a livello applicativo devono essere aggiornati, altrimenti diventano obsoleti. Questo crea un problema evidente: l’aggiornamento non è banale, e più complesso è il sistema, maggiore è la probabilità di introdurre bug (vulnerabilità) nel sistema. E quale componente di un sistema non dovrebbe mai avere vulnerabilità? Esatto.

I firewall a livello applicativo sono estremamente efficaci, ma rappresentano un esempio in cui occorre decidere se la cura è peggiore della malattia: il peggior danno che un attaccante potrebbe fare hackerando un firewall stateful è far passare del traffico non autorizzato, mentre hackerare un Application layer firewall permetterebbe di ispezionare ogni singolo bit che transita, trasformandolo di fatto in un attacco man-in-the-middle.

**Firewall hardware vs. software**

I firewall possono essere hardware o software. I firewall hardware sono costituiti da FPGA o altri tipi di microcontrollori, mentre i firewall software – i più comuni – consistono in un’applicazione software che gira su un sistema operativo su un dispositivo di piccole dimensioni, come un Raspberry Pi o un Arduino.

È importante notare che, sebbene i firewall hardware non abbiano un sistema operativo sottostante, implementano comunque del software, ma si tratta di un’**unica applicazione** che si ripete in loop sul chip.

La principale differenza tra firewall hardware e software è che quest’ultimi devono garantire anche che il sistema operativo e i relativi processi siano privi di bug. La cosa più importante è evitare di mescolare funzionalità: il dispositivo del firewall dovrebbe eseguire solo il firewall stesso, mentre tutti gli altri servizi (come i server web) dovrebbero essere eseguiti su un altro dispositivo. In caso contrario, un attacco a uno degli altri processi potrebbe compromettere anche il firewall.
## 9.2 **Posizionamento del firewall**

A questo punto dovrebbe essere chiaro che un firewall è indispensabile. Tutti hanno un firewall integrato nel router, anche se quasi nessuno lo configura correttamente. Ma dove dovrebbe essere posizionato un firewall?

Come già accennato, in ogni rete esistono almeno due aree di sicurezza:

- **Area interna**: una rete interna che contiene tutti i dispositivi degli utenti, i server interni e i database (essenzialmente la parte che necessita della maggiore protezione).
- **Zona demilitarizzata (DMZ)**: l’area che contiene i server web, e-mail e DNS, insieme a tutti gli altri servizi che devono essere direttamente accessibili dall’esterno.

![[Pasted image 20241128092231.png]]

I servizi della DMZ possono essere accessibili sia dall’area interna sia dall’esterno (Internet); tuttavia, mentre questi servizi possono a loro volta comunicare verso l’esterno, è loro proibito **accedere direttamente** alla rete interna.

La zona demilitarizzata è **sacrificabile**: è il luogo in cui vengono collocati i servizi che devono essere raggiungibili da Internet, ma che non causano grandi problemi se compromessi (basterà ripristinarli senza drammi, o almeno senza esagerare). Questo è anche il punto in cui le contromisure sono cruciali, poiché permette traffico diretto proveniente da Internet, rendendolo vulnerabile agli attacchi. La rete interna, al contrario, ==ha requisiti di sicurezza completamente differenti.==

Ma un solo firewall è sufficiente?
Sì; un singolo firewall può avere tre **interfacce**, che dovrebbero essere il più possibile separate, anche fisicamente (usando connessioni Ethernet differenti – nota che non possono condividere lo stesso switch).

Se il budget lo consente, è possibile installare **due firewall**. La loro configurazione sarebbe sostanzialmente identica, ma ciascun firewall avrebbe solo due interfacce. Tuttavia, le regole diventerebbero molto più complesse, poiché dovrebbero essere applicate da entrambi i firewall.

![[Pasted image 20241128182233.png]]

Lo scopo di avere due firewall è che, se un attaccante riesce a bypassare il primo, dovrebbe poi superare anche il secondo, rendendo l’attacco più lungo e complesso. Naturalmente, questa strategia è valida solo se i due firewall sono completamente diversi (per tipo, marca, sistema operativo e hardware).

Questo requisito fondamentale, tuttavia, rende questa configurazione complicata non solo per l’attaccante, ma anche per l’amministratore di sistema. Inoltre, aumenta le probabilità di commettere errori nella configurazione (che a loro volta porterebbero a vulnerabilità). È un’idea valida, ma che può facilmente ritorcersi contro.
Per questa ragione, nella maggior parte dei casi è meglio utilizzare un singolo firewall che si sappia configurare perfettamente.
## 9.3 **Netfilter**

**Netfilter** (iptables) è un framework fornito dal kernel Linux che permette di implementare varie operazioni relative alla rete. In particolare, offre diverse funzioni e operazioni per il filtraggio dei pacchetti, la traduzione degli indirizzi di rete (NAT) e la traduzione delle porte, che forniscono la funzionalità necessaria per instradare i pacchetti attraverso una rete e impedire che raggiungano posizioni sensibili al suo interno. Netfilter rappresenta il firewall di Linux (macOS ne usa un altro di nome PacketFilter) e, essendo molto accessibile, costituisce un caso di studio interessante per diversi motivi.

È importante notare che quando si accede al firewall di Linux, in realtà si interagisce con due componenti software:

1. **iptables**: un programma user-space che consente all’amministratore di sistema di configurare le regole per il filtraggio dei pacchetti IP (fondamentalmente l’interfaccia visibile sullo schermo).
2. **Firewall kernel-space**: il vero firewall che opera all’interno del kernel.

Questo sistema fornisce un controllo potente e granulare sulle operazioni di rete, rendendo Netfilter uno strumento versatile e ampiamente utilizzato nel mondo Linux.

## 9.4 **Filtraggio**

Un firewall deve generalmente controllare ogni pacchetto che attraversa la rete, essere privo di bug e rappresentare il software più piccolo e veloce del sistema. **iptables** funge da scudo contro eventuali errori dell'utente (l'utente non dovrebbe mai interagire direttamente con Netfilter). Altri sistemi operativi implementano filtri di pacchetti ancora più avanzati: ad esempio, il *Cisco IOS* (Internetworking Operating System) consente di apportare modifiche alle regole in tempo reale senza perdere i pacchetti in entrata o in uscita durante il processo.

Ad esempio una regola di iptables potrebbe essere:

```bash
iptables -t filter -D INPUT –dport 80 -j ACCEPT
```

Questa regola può essere interpretata come: "accetta tutti i pacchetti in ingresso alla porta 80". I parametri significano:

- `-t filter`: tabella;
- `-D INPUT`: catena;
- `–dport 80`: regola di corrispondenza;
- `-j ACCEPT`: azione (target).

**Altro Esempio**

Un firewall può essere visto come un **host** con almeno **due interfacce di rete** (NIC 1 e NIC 2), che collega due reti distinte, **rete A** e **rete B**. I pacchetti arrivano su una delle interfacce, vengono filtrati e quindi inoltrati verso l'altra interfaccia.

![[Pasted image 20241128184244.png]]

Per semplificare, supponiamo che i pacchetti possano fluire solo da **rete A** a **rete B**. Questo flusso può essere rappresentato come un diagramma di flusso, in cui:

- I pacchetti possono provenire da **rete A** o dal **localhost** (il firewall stesso).
- I pacchetti possono essere destinati a **rete B** o al **localhost**.

![[Pasted image 20241128184624.png]]

Poiché il **localhost** (il firewall) è in grado di inviare dati autonomamente, può inviare direttamente pacchetti alla rete **B** senza passare attraverso la tabella di routing. Tuttavia, i pacchetti provenienti da **rete A** devono passare attraverso la tabella di routing prima di raggiungere **rete B**.
Se si consente al **localhost** di comunicare con se stesso (localhost-to-localhost) senza passare dalla tabella di routing, si otterrebbe un layout leggermente diverso.

La configurazione dipende dal sistema operativo in uso:

- Nei sistemi **Linux/BSD**, il **localhost** è considerato, dal punto di vista del kernel, come un **socket TCP**.
- Tuttavia, tecnicamente il localhost è implementato come un'interfaccia virtuale chiamata **loh** (localhost/127.0.0.1).

Se si apre un socket su localhost della rete **B** e si vuole inviare dati a localhost della rete **A**, i dati non passeranno attraverso il punto di routing (il software che controlla le tabelle di routing), perché il kernel sa già chi sta inviando i dati.
Questo comportamento è specifico del design delle interfacce virtuali nel kernel e influisce sul modo in cui i firewall e le reti locali interagiscono all'interno di un singolo host.
### **9.4.1 Catene e tabelle**

Ad un alto livello, iptables contiene **tabelle** che a loro volta contengono **catene**, che possono essere built-in o definite dall'utente e ciascuna delle quali può avere regole specifiche per i pacchetti. Le **catene** identificano i punti nel kernel in cui viene effettuato il filtraggio, mentre le **tabelle** associano una funzione a ciascuna regola.
Possiamo fare diverse cose nelle catene, come **accettere** o **scartare** pacchetti, modificarli e avere un **log dei messaggi**.

Le catene principali di Netfilter includono:

- **prerouting**: un controllo preliminare per ispezionare i pacchetti prima di verificare la loro destinazione;
- **postrouting**: controllo ridondante dopo l'instradamento;
- **output**: allo stesso modo del prerouting, per pacchetti da una socket locale;
- **input**: per pacchetti in arrivo verso il dispositivo locale, che sono poi analizzati;
- **forward**: lo stesso dell'input, ma per pacchetti diretti verso altre reti (ad esempio Internet).

	 ![[Pasted image 20241129182954.png]]

Stiamo, tuttavia, trascurando qualcosa: il diagramma nella figura non mostra come funziona un firewall, ma come funziona qualsiasi programma che invia dati. Se scriviamo un nostro codice, i pacchetti dal nostro computer alle porte Internet non passano attraverso il router. Questo è vero ma anche falso, nel senso che l'instradamento nella figura è responsabile dell'inoltro dei pacchetti da una porta all'altra. La cosa che non è rappresentata qui è un altro pezzo di software che decide quale porta di uscita deve essere utilizzata per un determinato socket (decisione sulla porta).

Per distinguere facilmente tra gruppi di flussi di ispezione dati simili, **iptables** include quattro tabelle predefinite che raggruppano regole con la stessa funzione:
- **Filter table**: utilizzata per il filtraggio generale dei pacchetti (firewalling).
- **NAT table**: utilizzata per la traduzione degli indirizzi di rete.
- **Mangle table**: utilizzata per la modifica specializzata dei pacchetti.
- **Raw table**: utilizzata per configurare eccezioni, ad esempio evitando operazioni di tracciamento delle connessioni (conntrack).
Ogni tabella contiene catene di regole che possono anche essere richiamate da altre tabelle.
 
1. **Filter Table**  
    È la tabella predefinita per il ==filtraggio generale dei pacchetti==. I target possibili includono:
    - `drop`: il pacchetto viene scartato senza notifiche;
    - `reject`: il pacchetto viene scartato con notifica al mittente;
    - `accept`: il pacchetto prosegue verso la destinazione;
    - `log`: registra il pacchetto nei log (da usare con cautela per evitare di riempire il disco).
    Un numero di attacchi possono essere effettuati usando la *rejection*, quindi non dovremmo usarla se possibile, anche il *logging* dovrebbe essere evitata perchè potrebbe facilmente riempire l'hard disk.
     
2. **NAT Table**  
    Qui è dove ci chiediamo perchè un firewall modifica i pacchetti come fa il NAT. La risposta è che tutto quello che il NAT fa è applicabile anche per il firewall (ad esempio condividono la feature per tracciare i pacchetti).
    I target principali includono:
    - **DNAT**(Destination Address Translation): modifica l’indirizzo IP di destinazione dei pacchetti prima dell’instradamento, verso qualcosa che corrisponda il routing sul server locale (utile per redistribuire il traffico su una rete con più server);
    - **SNAT**(Source Address Translation): modifica l’indirizzo IP di origine dopo l’instradamento (utile per comunicazioni in uscita).
	In altre parole DNAT e SNAT sono usati per far vedere come se una data macchina (come un webserver) si trovi ad una certa locazione, anche se in realtà è all'interno di una rete locale dietro un NAT

3. **Mangle Table**  
    Serve per modifiche specializzate ai pacchetti dopo il monitoraggio delle connessioni (**conntrack**) ma prima di altre operazioni come NAT o filtraggio.
    

4. **Raw Table**  
    Consente di applicare eccezioni alle configurazioni, evitando operazioni ad alto consumo di memoria come il monitoraggio delle connessioni.
    
###  **9.4.2 Conntrack**

Netfilter/iptables è uno strumento **stateful**, in grado di monitorare tutte le connessioni logiche o sessioni di rete e di gestire i pacchetti correlati. **Conntrack** è una funzionalità che assegna un’etichetta a ogni pacchetto, in modo che le fasi successive del processo di instradamento possano sempre sapere a quale connessione appartiene un pacchetto. Sostanzialmente il conntrack individua:
	- Frammenti che appartengono allo stesso pacchetto IP (solo nel caso IPv4, in IPv6 non necessario)
	- Pacchetti che appartengono alla stessa connessione
	- Pacchetti lascamente correlati fra di loro (che appartengono a connessioni distinte ma legate come nel File Transfer Protocol (FTP))

Per alcuni protocolli il firewall può ispezionare anche i dati dell'application layer e identificare i pacchetti che appartengono alla stessa connessione anche se non condividono le stesse porti, definendo 4 stati: 
- **new**: il kernel vede il pacchetto per la prima volta;
- **established**: il pacchetto appartiene a una connessione già nota;
- **related**: il pacchetto è correlato a una connessione esistente (ad esempio, connessioni di trasferimento dati legate a connessioni di comando come in FTP);
- **invalid**: pacchetti che non appartengono a nessuno stato valido (usualmente un errore).

 **Esempio**

Un'applicazione come **Cisco Webex Meetings** potrebbe avere più flussi di dati (es. video, audio e presentazioni). Il flusso video/audio sarebbe `established`, mentre quello delle slide potrebbe essere `related` se usa porte TCP diverse.

Un firewall non blocca realmente i pacchetti, ma i flussi che iniziano dall'esterno verso l'interno. Questo consente di mantenere funzionalità essenziali, come risposte ai pacchetti generati dall’interno della rete. Se abbiamo un nuovo protocollo possiamo sempre modificare il conntrack in modo tale da capirlo e dare le giuste etichette ai pacchetti.

## 9.5 **Tolleranza ai guasti e bilanciamento del carico**

**La tolleranza ai guasti e il bilanciamento del carico** nei firewall sono argomenti estremamente importanti. Se un firewall si guasta, il miglior scenario possibile è la disconnessione della rete, mentre il peggiore è rimanere connessi ma completamente esposti.

Essendo un punto di ingresso/uscita naturale in una rete, il firewall, se non gestito correttamente, può facilmente diventare un **collo di bottiglia**. Per questo motivo, e specialmente in reti ad alto traffico, è fondamentale dividere il carico tra due o più firewall per migliorare le prestazioni e implementare soluzioni di backup, rendendo il sistema tollerante ai guasti e resistente a ogni condizione di rete.

**Esempio**
In una rete Ethernet gigabit, il firewall deve essere in grado di elaborare un gigabit di dati al secondo, una quantità considerevole.

### **9.5.1 Configurazione primaria di backup**

Il problema della tolleranza ai guasti può essere risolto facilmente installando un firewall di backup, quindi utilizzando due firewall anziché uno. Tuttavia, il bilanciamento del carico non viene affrontato in questa configurazione.

![[Pasted image 20241130155909.png]]

Il firewall secondario non può essere completamente spento, poiché deve essere pronto per l'attivazione tramite una configurazione automatica chiamata **heartbeat**. L'heartbeat è un monitor di basso livello che verifica lo stato della macchina inviando un segnale positivo se funziona correttamente. Se la CPU della macchina primaria si blocca o supera valori nominali, il monitor rileva il guasto e avvia il dispositivo secondario. Per fare questo avremmo bisogno di installare switches per dirigere il traffico dall'intefaccia del firewall guasto al secondo.

Questa configurazione è più o meno efficiente a seconda dello stato di backup del firewall:
1. **Spento (cold swap backup)**:
    - La CPU è priva di alimentazione.
    - Il tempo di avvio richiede alcuni secondi, durante i quali la rete è inattiva.
2. **Modalità sleep (hot swap backup)**:
    - Il tempo di avvio è ridotto, ma il consumo energetico è maggiore per mantenere attiva la memoria.
3. **Attivo**:
    - Il firewall di backup è già operativo e deve solo assumere il controllo del traffico.
    - Consumo energetico più elevato rispetto alla modalità sleep.

#### **Contro della configurazione primaria di backup**

La configurazione primaria di backup presenta alcune problematiche:
- **Affidabilità al riavvio**: La maggior parte dei problemi hardware s==i verifica durante l'accensione.== Gli spike elettrici generati dall'alimentazione possono danneggiare i componenti elettronici. Per questo motivo, è generalmente preferibile utilizzare una configurazione di hot swap backup.
- **Affidabilità delle memorie secondarie**:
    - Gli HDD (hard disk drives) hanno una maggiore resistenza rispetto agli SSD (solid state drives), il cui tempo medio tra i guasti (MTBF) è proporzionale al numero di scritture effettuate.
- **Costo**: Un firewall di backup inattivo è un investimento poco efficiente, paragonabile all'acquisto di un'auto di riserva che rimane inutilizzata.
### **9.5.2 Cluster di firewall multi-primary e multi-path**

Una soluzione migliore è far lavorare anche il secondo firewall. In questa configurazione si implementa un **bilanciamento del carico**, in cui l'intero cluster di firewall opera come un unico firewall.
#### **Vantaggi**

1. Il traffico è gestito da **n firewall più piccoli**, con la capacità totale distribuita.
2. In caso di guasto di un firewall, il **bilanciatore di carico** ridistribuisce il traffico tra gli altri firewall,(occhio che load balancers sono colli di bottiglia)
3. È possibile eseguire la manutenzione di un firewall senza interrompere il servizio.

#### **Considerazioni**

Il bilanciamento del carico è una strategia **win-win**, che migliora sia l’efficienza economica sia la configurazione rispetto alla semplice ridondanza. Tuttavia, è importante ricordare che il bilanciatore stesso potrebbe diventare un collo di bottiglia, quindi va progettato con attenzione per evitare nuovi punti di vulnerabilità.

### **9.5.3 Cluster di firewall multi-primary hash-based con stato condiviso**

Questa configurazione, la più utile, elimina la necessità di un bilanciatore di carico. Ogni firewall riceve un **ID numerico** da 0 a n−1 (per n firewall). Il traffico in ingresso viene distribuito tra i firewall utilizzando una funzione hash basata su una tupla $T=(IP_s,IP_d,port_s,port_d,protocol)$, dove per ogni tupla T, il firewall verifica se $\text{hash}(T) \% n == ID$. Se la condizione è soddisfatta, il firewall gestisce la connessione; altrimenti, la ignora. In questo modo, i firewall distribuiscono il carico autonomamente senza bisogno di un bilanciatore di carico esterno.

![[Pasted image 20241130163504.png]]

Un **heartbeat** è necessario per gestire correttamente i guasti.
#### **Replica dello stato Conntrack**

In questa configurazione, quando un firewall si guasta, i flussi gestiti da quel firewall vengono persi. Questo avviene perché il **conntrack** (lo stato delle connessioni tracciato da ogni firewall) è separato per ogni firewall, e gli altri firewall non comprendono i flussi provenienti da quello guasto, causando il probabile scarto dei pacchetti.

Per risolvere questo problema, è necessario replicare lo stato del conntrack tra i firewall. Esistono tre approcci principali per la replica:

- **1. Replica continua**
	- Ogni firewall aggiorna continuamente il proprio conntrack e invia le modifiche agli altri firewall.
	- Pro: garantisce la sincronizzazione in tempo reale.
	- Contro: può diventare rapidamente onerosa, soprattutto in reti con traffico elevato o con molti firewall, a causa del sovraccarico di comunicazione.

- **2. Replica periodica**
	- Gli aggiornamenti vengono inviati periodicamente (ad esempio ogni 5, 10 o 60 secondi).
	- Gli amministratori possono scegliere l’intervallo di tempo per evitare collisioni sui canali di comunicazione.
	- Pro: riduce il carico rispetto alla replica continua.
	- Contro: se un firewall si guasta tra due aggiornamenti, si perdono i flussi modificati dall’ultimo aggiornamento al momento del guasto.

- **3. Replica basata su polling**
	- Lo stato del conntrack viene aggiornato secondo una politica basata su polling, anziché su eventi.
	- La frequenza del polling può essere regolata: da frequenze simili alla replica continua a intervalli molto ampi (vicini all’assenza di replica).
	- Pro: offre flessibilità nella frequenza degli aggiornamenti.
	- Contro: genera traffico di polling anche in assenza di modifiche, con un costo aggiuntivo rispetto ai metodi basati su eventi.

Indipendentemente dal metodo scelto, la replica dello stato richiede di creare copie dei dati su HDD o SSD in configurazione **RAID**, per garantire la disponibilità e la sicurezza delle informazioni.
## 9.6 **Filtraggio al livello 7**

Un amministratore di sistema potrebbe voler filtrare il traffico di livello 7 per diversi motivi, come il registro (log) e l'analisi del traffico (ad esempio, per configurare meglio l'intero sistema), il traffic shaping (ad esempio, per la priorità dei flussi) o il blocco dei protocolli. Questo tipo di firewall è necessario ogni volta che i numeri di porta sorgente e destinazione non sono sufficienti per capire che tipo di traffico si sta analizzando.

Esistono molti firewall a livello applicativo (livello 7); sono estremamente esigenti e difficili da mantenere, principalmente perché un gestore di protocollo deve essere sviluppato all'interno del firewall stesso, e ogni applicazione (anche quelle proprietarie) ne richiede uno specifico.

In generale, è meglio utilizzare firewall che facciano solo il necessario (quindi non firewall di livello 7 e 4). Anche se dobbiamo bloccare determinati tipi di traffico (ad esempio, per impedire agli utenti di giocare o di accedere ai social media dai loro uffici), la soluzione migliore è non bloccarli, ma semplicemente controllare cosa fanno i nostri utenti, perché altrimenti disabiliteranno sicuramente le nostre misure di sicurezza.
### 9.6.1 **Filtraggio al livello 7: livello amministrativo di sicurezza**

Il gestore del protocollo in un firewall di livello 7 è un punto critico: ci sono stati molti casi di malware e vulnerabilità (a causa di cattiva implementazione) in questi decodificatori.

**Esempio: Wireshark**  
Un caso notevole è stato quello di Wireshark, che presentava perdite di memoria nelle sue librerie che permettevano l'esecuzione arbitraria di codice o portavano a blocchi del sistema – problemi particolarmente seri nei firewall e dispositivi simili.

**Esempio: Snort RPC Preprocessing Vulnerability** (sistema di intrusion-detection compagno del firewall)
Ricercatori dell’ISS hanno scoperto un buffer overflow remotamente sfruttabile nel modulo preprocessor stream4 di Snort, che permetteva ad attaccanti remoti di eseguire codice arbitrario su un sensore Snort. È come convincere una guardia di sicurezza – una delle persone di cui ci fidiamo di più – a fare cose malevole.

**Esempio: Trend Micro InterScan VirusWall Remote Overflow**  
Un difetto di implementazione in un gateway permetteva a un attaccante remoto di eseguire codice con privilegi da demone (cioè quasi completi).

**Esempio: Microsoft ISA Server 2000 H.323 Filter**  
Un attaccante potrebbe usare un flusso H.323 malevolo malformato per eseguire un buffer overflow remoto, consentendogli di fatto di diventare un superutente – la cosa peggiore che potrebbe accadere in un sistema.

**Esempio: Cisco SIP Fixup Denial of Service (DoS)**  
Un attaccante potrebbe abbattere il firewall semplicemente inviando un messaggio.
### 9.6.2 **Filtraggio al livello 7: neutralità**

Un firewall deve essere considerato esclusivamente come uno strumento di applicazione di politiche di sicurezza. Come amministratori di rete, il nostro obiettivo è la sicurezza di un sistema, guidata dall'analisi dei rischi. Se troviamo una vulnerabilità che può essere sfruttata in qualche modo, la isolo e lasciamo eventualmente il dispositivo vulnerabile nella parte sicura della rete, posizionando un firewall nel mezzo.

Nessuno dovrebbe mai iniziare felicemente a bloccare tutto ciò che per qualche ragione è indesiderato o inaspettato, perché questo non è lo scopo di un firewall.

Sfortunatamente, però, il firewalling può essere utilizzato anche per scopi negativi, ossia per applicare regole non legate all'analisi del rischio, ma a politiche rilevanti per altri scopi (come impedire l'accesso ai social media durante l'orario di lavoro).

**Esempio**
La rete UniFi è limitata dal **GARR** (Gruppo per l'Armonizzazione delle Reti della Ricerca), la rete nazionale italiana per le università e la ricerca. L'obiettivo principale del GARR è progettare e gestire un'infrastruttura di rete ad alte prestazioni che fornisca servizi avanzati alla comunità accademica e scientifica italiana. Questo significa anche che ogni singolo traffico su questa rete deve essere legato al lavoro universitario: se usiamo la nostra e-mail istituzionale per inviare un messaggio a un familiare o a un amico, o per leggere e scrivere messaggi su WhatsApp, stiamo facendo qualcosa di vietato – non per ragioni di sicurezza, ma per motivi amministrativi (regole non legate alla sicurezza).

Dobbiamo sempre distinguere tra le regole che implementiamo per motivi di sicurezza e quelle per politiche aziendali, perché sono due cose diverse e, talvolta, possono anche entrare in conflitto.

Abbiamo nelle nostre mani la chiave per **la privacy, la libertà, la neutralità della rete e l'equità della rete**.

Ad esempio
- Se un provider di servizi Internet (**ISP**) blocca o rallenta tutto il traffico verso un servizio concorrente, si tratta di una forma di concorrenza sleale.
- A livello aziendale, se il blocco viene fatto per impedire ai dipendenti di accedere a pagine web dei sindacati, si pone un problema legato alla libertà dei lavoratori.
- A livello nazionale, se lo stesso approccio viene adottato per qualunque motivo, può portare alla censura.

Bloccando un protocollo, un firewall può operare facilmente. Tuttavia, bloccare un sito specifico è più complesso, poiché i siti web cambiano frequentemente indirizzo IP, rendendo difficile il blocco. Per impedire agli utenti di accedere a siti specifici, i firewall devono lavorare a livello DNS, bloccando le richieste DNS. Tuttavia, gli utenti possono utilizzare DNS alternativi, quindi, sebbene queste misure siano efficaci per la maggior parte degli utenti, non lo sono per chi ha maggiore competenza tecnologica.

Detto questo, per bloccare davvero qualcuno da fare qualcosa, dovremmo impedire loro di connettersi a Internet.

#### **Caso di studio: il firewall iraniano**

Un esempio significativo (seppur negativo per gli utenti) di strumento di censura a livello nazionale è il **firewall dell'Iran**, uno dei paesi maggiormente associati alla censura su Internet.

![[Pasted image 20241201175519.png]]

Questo firewall è stato attivato durante le controverse elezioni presidenziali iraniane del 2009, quando la popolazione insorse contro presunte manipolazioni del voto e brogli elettorali. Non solo queste rivolte furono represse violentemente dai militari, ma anche tutto l'accesso a Internet fu bloccato per impedire alle persone di condividere in tempo reale notizie sulle rivolte e di comunicare tra loro per organizzarsi.

![[Pasted image 20241201175638.png]]

Anche se questo è un caso estremo di censura, firewall nazionali si trovano non solo in paesi come la Cina (il Grande Firewall della Cina), la Russia e l'Egitto, ma anche in paesi apparentemente insospettabili.
In altre parole, il firewalling a livello nazionale è una realtà sempre presente.

![[Pasted image 20241201180059.png]]
### 9.6.3 **Firewall domestici**

I firewall come Windows Defender sono molto simili alle mascherine facciali. Durante la pandemia di COVID-19, molte persone indossavano una mascherina, uscivano, incontravano amici, stringevano mani, si baciavano... tutto questo perché indossavano una mascherina. Queste persone sono idiote. Le mascherine davano loro una sensazione di protezione, ma in realtà ==non lo erano==. I firewall personali sono simili: sono utili e ci danno una sensazione di sicurezza, ma potrebbe essere un’illusione. Avere un firewall è comunque meglio di non averne uno, ma non bisogna riporre troppa fiducia in esso per il solito vecchio motivo: per configurarlo correttamente bisogna sapere esattamente come farlo.

Inoltre, per semplificare l’interfaccia, molti firewall personali tendono a nascondere opzioni che un utente avanzato troverebbe fondamentali per una configurazione corretta.

Un vero firewall domestico costa circa 100 dollari e non è più grande di un pacchetto di sigarette. Non può gestire troppo traffico, quindi dovrebbe essere utilizzato solo in ambito domestico o in piccole attività (SOHO --> Small office Home office)

Ricorda che il conntrack per IPv4 è diverso dal suo equivalente IPv6, e i due stack sono in gran parte indipendenti. Pertanto, è fondamentale scrivere le stesse regole per entrambi. Attualmente, il tuo firewall probabilmente non contiene alcuna regola perché non è stato configurato:
- Per IPv4, ciò significa che non ci sono misure di sicurezza.
- Per IPv6, significa che i tuoi dispositivi domestici hanno un indirizzo pubblico globale, senza firewall, e sono accessibili da tutto il mondo.

Quindi sì, dovresti almeno provare a configurare il tuo firewall **adesso**. Ricorda che le regole vengono applicate nell’ordine in cui sono scritte: invertire due righe non produce lo stesso risultato e potrebbe anche influire sull’efficienza del firewall.
#### **Suggerimenti per la configurazione**

- **Non copiare-incollare configurazioni trovate online**:
    - Spesso contengono errori o regole che potrebbero compromettere la sicurezza del tuo sistema.
    - Se devi copiare qualcosa, scegli configurazioni semplici e studiale attentamente prima di applicarle.

- **Usa configuratori di alto livello**:
    - Iptables è solo un’interfaccia tra l’applicazione Netfilter e l’utente. È meglio utilizzare strumenti come **Shorewall**, che offrono un’interfaccia più chiara e riducono il rischio di errori.

- **Sperimenta in ambienti sicuri**:
    - Configura **macchine virtuali** e posiziona firewall tra di esse per imparare senza rischiare di danneggiare nulla.

#### **pfSense**

Un esempio di firewall domestico è **pfSense**, un firewall open-source basato sul tool di filtro dei pacchetti di OpenBSD (**pf** --> packet filter tool).

Tra iptables e pfSense, il prof. Pecorella consiglia vivamente pfSense, perché offre nativamente supporto per:
- Ridondanza;
- Replica dello stato;
- Clustering.

Le funzionalità di iptables in Linux non si applicano a pfSense. Sebbene il concetto generale sia simile, l’approccio richiede un apprendimento ex novo.

# Capitolo 10: Wi-Fi

Il **Wi-Fi** è una famiglia di protocolli di rete wireless, basati sugli standard IEEE 802.11 (di cui costituisce un sottoinsieme), comunemente usati per reti locali e l'accesso a Internet. Wi-Fi è un marchio registrato della non-profit **Wi-Fi Alliance**, che limita l'uso del termine "Wi-Fi Certified" ai prodotti che superano i test di certificazione per l'interoperabilità. La Wi-Fi Alliance non fa parte dell'IEEE, ma è un'alleanza di fornitori commerciali (aziende) che si sono riuniti per promuovere questo standard.
## 10.1 **Sugli standard**

Per realizzare il proprio standard, la Wi-Fi Alliance ha sostanzialmente preso parti degli standard 802.11 e le ha dichiarate obbligatorie o facoltative. Ciò che vediamo in 802.11b, 802.11g o 802.11n è stato effettivamente tradotto dalla Wi-Fi Alliance in un insieme di regole che ci dicono quali parti dello standard devono essere implementate per essere conformi alla versione Wi-Fi (b/g/n e così via). Lo standard effettivo di ogni versione contiene tutto, ed è diverso dalle altre versioni solo per quanto riguarda le specifiche delle parti obbligatorie e facoltative. Nello standard potremmo trovare anche cose che non fanno parte di una normale implementazione Wi-Fi.

Segue un elenco degli standard Wi-Fi (fino all'autunno 2020; le lettere mancanti non sono effettivamente mancanti, ma sono state omesse perché l'elenco sarebbe stato troppo lungo):

![[Pasted image 20241202144738.png]]

Ogni lettera è un addendum allo standard; a volte i compendi contengono tutto ciò che è stato precedentemente rilasciato come addendum.

**Esempio**: 802.11r ci permette di passare tra punti di accesso federati senza dover riautenticarsi. Questa funzionalità non fa parte di "n", ma potrebbe essere parte di "c" (sebbene non sia obbligatoria). 11i è sostanzialmente la versione "n" contenente questa funzionalità (ma ancora in modo opzionale). È chiaro che dobbiamo controllare esattamente cosa implementa il nostro **punto di accesso**, perché non è molto ovvio.

Un'altra cosa importante da capire sugli standard è che lo standard emette un documento. L'entità responsabile della verifica della compatibilità e conformità di un dispositivo allo standard è la Wi-Fi Alliance. Un test di conformità mira a verificare che il sistema superi alcuni test in un ambiente di test (in altre parole, controlliamo che il sistema reagisca nel modo previsto a determinati input). ==Tale test non è un test di vulnerabilità, ma un test positivo(superato/non superato)==. Non dice nulla sul dispositivo o sul comportamento contro input imprevisti, quindi possiamo sempre avere un dispositivo che supera tutti i test ma si comporta terribilmente in un test di vulnerabilità.

## 10.2  **Modalità di connettività di base**

Esistono due principali topologie e modalità di connessione al Wi-Fi:

1. **Modalità infrastrutturata**:
    - Topologia a stella, che richiede un ==**punto di accesso== (Access Point, AP)** incaricato del coordinamento della rete.
    - Ogni comunicazione tra due dispositivi deve passare attraverso l’AP, che funge da ripetitore intelligente del segnale.
2. **Peer-to-peer**:
    - Permette una comunicazione diretta tra dispositivi.
    - Esiste comunque un **gruppo proprietario** responsabile della gestione delle funzioni di base della rete, che può essere riassegnato.

Esiste una terza modalità progettata per dispositivi a basso consumo energetico, ma non verrà considerata qui.
## 10.3 **Segnale Wi-Fi**

L'equazione per calcolare la potenza ricevuta $P_{RX}$ è la seguente:

- $P_{RX} = P_{TX} + G_{TX} - L_{TX} - L_{FS} - L_{M} + G_{RX} - L_{RX}$

Questa formula semplice, derivata dalla trasmissione fisica, descrive approssimativamente quanta **potenza riceve il ricevitore**. Sebbene possa essere complicata da vari fattori, mostra come parte della potenza inviata dal trasmettitore venga persa per diversi motivi:
- $L_{TX}$: perdita del trasmettitore (cavi coassiali, connettori, ecc.) (dB);
- $L_{RX}$: perdita del ricevitore (cavi coassiali, connettori, ecc.) (dB);
- $L_{FS}$: perdita di percorso (solitamente perdita nello spazio libero) (dB);
- $L_{M}$: perdite varie (margine di fading, perdita del corpo (schermiamo il wifi facendoli perdere potenza, disallineamento di polarizzazione, ecc.) (dB).

La perdita di percorso è causata dal fatto che trasmettiamo attraverso l'aria, anziché attraverso un vuoto perfetto. Ostacoli come muri, pavimenti o alberi possono aumentare significativamente $L_{FS}$. Ad esempio:
- Un muro spesso è spesso un ottimo scudo con alto $L_{FS}$.
- Un pavimento o un soffitto ha un $L_{FS}$ più basso.
- Un albero aumenta molto la perdita, specialmente a causa delle foglie.

Anche il tempo atmosferico e le condizioni stagionali influiscono:
- La nebbia (o l'umidità in generale) aumenta $L_{FS}$.
- Gli alberi in inverno, senza foglie, causano meno perdite rispetto all'estate.

Altri parametri della formula sono:
- $G_{TX}$: guadagno dell'antenna trasmittente (dBi).
- $G_{RX}$: guadagno dell'antenna ricevente (dBi).
- $P_{TX}$: potenza di uscita del trasmettitore (dBm).
- $P_{RX}$: potenza ricevuta (dBm).

Le quantità positive in questa equazione non aumentano la potenza del segnale ma combatte contro le perdite, ricorda che non riceveremo mai un segnale più forte rispetto a quello che è stato mandato.

Il guadagno delle antenne (sia in trasmissione che ricezione) può essere negativo, il che comporta una perdita. Tuttavia, dipende dalla qualità delle antenne:
- **Antenne corte**: hanno un basso guadagno (-16 dB).
- **Antenne più lunghe**: possono migliorare il guadagno fino a -9 dB.

Le antenne **planari o paraboliche** hanno un guadagno eccellente (circa +3 dB), ma sono **direzionali** e funzionano bene solo in linea di vista, perdendo molto guadagno ai lati. Sono ideali per comunicazioni a lunga distanza.

Le antenne **omnidirezionali** hanno lo stesso guadagno in tutte le direzioni, quindi sono più adatte per spazi aperti.

![[Pasted image 20241202153543.png]]

Molti tutorial consigliano di aumentare la potenza massima dell'AP per migliorare le prestazioni. Tuttavia:
1. In UE, la potenza massima dell’AP è limitata a **100 mW** per legge.
2. Anche se aumentassimo la potenza del segnale ricevuto dall’AP, il segnale trasmesso dai dispositivi non migliorerebbe, causando uno squilibrio del canale.

Quanto può viaggiare il segnale Wi-Fi prima che sia indistinguibile dal rumore termico? Più di quanto immaginiamo.

Ogni antenna riceve un rumore termico dovuto al rumore elettromagnetico, generato da altri dispositivi o dalla temperatura ambiente. Sebbene con attrezzature normali possiamo pensare che il segnale Wi-Fi non possa essere ricevuto all’esterno, un attaccante con attrezzature migliori (basse perdite del ricevitore e antenne ad alto guadagno, come paraboliche o planari) può facilmente decodificare il segnale.

**Esempio:**  
Con attrezzature comuni, è possibile decodificare il segnale Wi-Fi dell'ospedale Careggi di Firenze dagli uffici UniFi Santa Marta.

**Conclusione:**  
La posizione dei dispositivi Wi-Fi è fondamentale, poiché il segnale si propaga molto più di quanto si pensi. Ignorare questa realtà può esporre il segnale a potenziali attacchi.

## 10.4 **Jamming**

Il **jamming radio** è l'atto deliberato di bloccare o interferire con comunicazioni wireless autorizzate. I jammer funzionano trasmettendo segnali radio che disturbano le comunicazioni riducendo il rapporto segnale-rumore. Questo concetto può essere utilizzato nelle reti dati wireless per interrompere il flusso di informazioni ed è una forma comune di censura nei paesi totalitari, per impedire alle stazioni radio straniere di raggiungere aree di confine.

Il jamming si distingue solitamente dall'interferenza accidentale, che può verificarsi a causa di malfunzionamenti o circostanze non intenzionali. Dispositivi che causano interferenze non intenzionali sono regolati diversamente.

Il jamming unintenzionale:
- Può verificarsi quando un operatore trasmette su una frequenza occupata senza controllare prima se è in uso, o quando non riesce a sentire altre stazioni che usano quella frequenza.
- Può anche accadere quando un'attrezzatura emette accidentalmente un segnale, come un impianto di televisione via cavo che interferisce con una frequenza di emergenza aeronautica.

Tecnicamente, il jamming non diminuisce la potenza del segnale ricevuto, ma aumenta il **rumore ricevuto dall'antenna** (le perdite varie, $L_M$). Sotto una certa soglia del rapporto segnale-rumore, il sistema non sarà in grado di decodificare il segnale, quindi un jammer deve iniettare abbastanza rumore per sovrastare il segnale desiderato.

Il jamming può essere:
1. **Stupido**:
    - Il jammer inietta continuamente rumore nel canale.
    - Questo tipo di jamming può facilmente far capire al ricevitore che è in corso un attacco.

2. **Intelligente**:
    - Il jammer aspetta l'arrivo di determinati pacchetti e inietta rumore solo quando questi arrivano.
    - Questo tipo di jamming è molto più difficile da rilevare.

Un attaccante, in generale, non ha bisogno di disturbare tutto il segnale; basta interferire quanto basta per renderlo inutilizzabile. Ad esempio, in pacchetti da 2000 byte, è sufficiente alterare 10 byte per interrompere i dati.
#### **Contromisure**

Il jamming è un attacco che funziona su qualsiasi tipo di trasmissione wireless, aumentando $L_M$ È sempre possibile e non può essere contrastato se non intervenendo fisicamente contro il jammer.

Ecco alcune strategie per attenuarne gli effetti:

1. **Allargare lo spettro del ricevitore**:
    - Utilizzando, ad esempio, tecniche come il **CDMA (Code Division Multiple Access)**, un attaccante avrà difficoltà a coprire tutto lo spettro. Tuttavia, l'efficacia dipende dall'hardware dell'attaccante, e oggi persino il CDMA può essere disturbato.
    
1. **Cambio frequente della base di trasmissione**:
    - Cambiare frequentemente la frequenza di base può evitare disturbi sia intenzionali che accidentali.

**Esempio:**  
Questa tecnica è implementata nel protocollo **Bluetooth**, che utilizza il **channel hopping**. Per disturbare una connessione Bluetooth, un attaccante deve coprire tutti i canali contemporaneamente (jamming stupido) o seguire i salti e i pacchetti – un compito molto più difficile, specialmente se non conosce come avviene il salto di canale.
## 10.5 **Il ruolo del livello MAC**
	
Sopra il livello fisico si trova il livello di controllo dell'accesso al mezzo (**MAC**), che riveste un ruolo molto importante. Nelle reti cablate, questo livello svolge compiti molto semplici.

**Esempio:**  
Nei protocolli come **Aloha** o **Ethernet**, il livello MAC (insieme al livello di controllo del collegamento logico) deve semplicemente:
- ascoltare il canale;
- verificare se qualcuno sta trasmettendo;
- decidere quando trasmettere;
- controllare se ci sono collisioni;
- pianificare le trasmissioni e simili.

Questi compiti sono relativamente semplici rispetto a quelli richiesti nel Wi-Fi.

Nel Wi-Fi (e in molti altri sistemi wireless), il livello MAC è stato arricchito con altre funzioni, tra cui:
- **Controllo dell'accesso**: decidere non solo chi sta trasmettendo (e quando), ma anche chi può e chi non può trasmettere.
- **Crittografia**: un compito inaspettato per questo livello.

Per queste ragioni, il livello MAC è estremamente importante per la sicurezza dei sistemi Wi-Fi.
## 10.6 **Perché il Wi-Fi è così popolare?**

Questa è una buona domanda, poiché il Wi-Fi non è uno standard eccellente, ma al massimo decente.

**Problemi principali del Wi-Fi:**
- Non utilizza i canali in modo efficiente.
- Non è efficiente dal punto di vista energetico (è come un camion mostruoso rispetto a un'auto elettrica; consuma molta energia).
- La sua sicurezza è scarsa.
- La copertura radio è compromessa da ostacoli come muri e acqua.
- Le interferenze riducono ulteriormente le prestazioni.
- Non garantisce né prestazioni né disponibilità, nemmeno a basse velocità.

Inoltre, sotto il marchio Wi-Fi sono stati sviluppati molteplici varianti che condividono poco con lo standard originario. Un esempio è lo standard **802.11ax**, che utilizza una banda da 6 GHz.

**Ragioni della popolarità del Wi-Fi nonostante i problemi:**
1. **È wireless**: le persone odiano i cavi e amano liberarsene.
2. **Hardware economico**: aggiungere il Wi-Fi a un dispositivo oggi è quasi gratuito grazie alla produzione di massa.
3. **È ovunque**: essendo economico, il Wi-Fi si trova anche dove non lo si vorrebbe.
4. **È veloce (più o meno)**: funziona abbastanza bene per utenti che si preoccupano solo della velocità di connessione.
5. **È facile**: i dispositivi Wi-Fi sono semplicissimi da installare e configurare, perfetti per l’utente medio.

**Nota:** Mai utilizzare il Wi-Fi per sistemi mission-critical, perché potrebbe fallire in qualsiasi momento.

## 10.7 **Regolamentazioni**

Il Wi-Fi è regolamentato dalla **Wi-Fi Alliance**, ma segue anche regolamentazioni locali e regionali, che differiscono principalmente per le frequenze utilizzate. Queste rientrano nella banda **ISM** (Industrial, Scientific, and Medical), porzioni dello spettro non soggette a licenze.

Le regolamentazioni definiscono:
- quali bande possono essere utilizzate;
- la potenza massima di trasmissione;
- per quanto tempo possono essere utilizzate.

Solitamente, i dispositivi devono rispettare un rapporto tra trasmissione e silenzio per consentire ad altri sistemi di utilizzare lo stesso canale.

**Bande ISM più utilizzate:**
- **868 MHz – 868,6 MHz** (UE).
- **902 MHz – 928 MHz** (USA).
- **2,4 GHz – 2,5 GHz**.
- **5,725 GHz – 5,875 GHz**.

Il Wi-Fi non utilizza praticamente mai le prime due bande. Nota che, a parità di potenza trasmessa, frequenze più basse garantiscono una migliore penetrazione del segnale attraverso i muri.

## 10.8 **Pacchetti**

I pacchetti Wi-Fi si suddividono in tre categorie:
- **Gestione**: tutto ciò che permette di scoprire una rete Wi-Fi vicina e di connettersi ad essa ((de)autenticazione, (de)associazione, beacon, ecc.);
- **Controllo**: ciò che ci si aspetta da un sistema MAC (RTS/CTS, ACK, ecc.), ovvero ciò che consente di trasmettere sul canale senza collisioni e di sapere se il nostro pacchetto è stato ricevuto;
- **Dati**: semplicemente i dati (cosa ti aspettavi?).

I primi due tipi sono obbligatori e fondamentali, ma non trasportano dati. Nota che l’unica parte crittografata è il payload dei pacchetti di dati; gli header non sono crittografati. Questo è un punto importante, poiché consente una serie di attacchi.

La mancanza di crittografia è una vulnerabilità intrinseca (di progettazione, non cattiva progettazione), che verrà discussa in dettaglio più avanti.

## 10.9 **RTS/CTS**

In breve, il Wi-Fi non crittografa tutto ciò che viene trasmesso perché alcuni frame di gestione (pacchetti a livello MAC) non possono essere codificati o decodificati se un dispositivo ==non fa ancora parte della rete==, a causa della mancanza della chiave. Avere una chiave pre-negoziata renderebbe inutile l’intero scopo del Wi-Fi.

I frame di controllo, invece, potrebbero essere crittografati, poiché a livello di controllo un dispositivo è già parte della rete. Tuttavia, si è deciso di non crittografarli per motivi di compatibilità: quando reti diverse coesistono nelle stesse bande ISM, è utile dichiarare pubblicamente cosa stanno facendo, in modo che possano decodificare ciò che viene inviato e agire di conseguenza.

**Esempio:** L’uso di pacchetti di controllo non crittografati e degli header dei pacchetti di dati consente a reti Wi-Fi diverse di decodificarsi a vicenda e di evitare collisioni. Lo stesso vale per diverse versioni di Wi-Fi e anche per standard differenti (come LTE non licenziato). Nota che la situazione opposta è valida per GSM, LTE e 5G, dove gestione, controllo, dati e tutto il resto sono crittografati perché gli utenti possiedono fisicamente una SIM card.

RTS/CTS (**Request To Send/Clear To Send**) è un meccanismo (opzionale) utilizzato dal protocollo Wi-Fi per ridurre le collisioni dei frame introdotte dal problema del nodo nascosto. Per risolvere questo problema, i pacchetti di controllo vengono inviati per informare C che c’è un altro dispositivo (A) nell’area di B e che quindi dovrebbe rimanere in silenzio per consentire ad A di inviare pacchetti a B.

![[Pasted image 20241202203822.png]]

Quando invia dati, il terminale A non invia un pacchetto direttamente a B; prima invia un breve pacchetto di controllo, la richiesta di invio (RTS). Tutti possono riceverlo e chiunque riceva tale messaggio sa che qualcuno sta tentando di accedere al canale e rimarrà in silenzio.

A questo punto, B invierà un pacchetto **CTS (Clear To Send)**, che verrà ricevuto da tutti gli altri terminali, inclusi quelli che non hanno visto l’RTS. C capirà quindi che qualcuno ha riservato il canale e attenderà andando in modalità sleep.

Entrambi questi pacchetti contengono la **durata** del pacchetto da trasmettere, ovvero il tempo per cui il canale è riservato da un terminale. Questo meccanismo è incredibilmente potente e utile per nodi nascosti, anche in reti/protocolli diversi.
### **10.9.1 - Attacchi RTS/CTS**

Come si potrebbe sospettare, un attaccante può sfruttare il meccanismo RTS/CTS per realizzare attacchi molto efficaci.

#### **Tipi di attacchi RTS/CTS**

1. **RTS falsi con durate estremamente lunghe**:
    - L'attaccante invia richieste RTS false, bloccando il canale per lunghi periodi.

2. **CTS falsi**:
    - L'attaccante simula che il punto di accesso stia concedendo l'accesso al canale a un dispositivo inesistente.
    - Con una potenza molto bassa, è possibile generare CTS falsi diretti solo a un singolo dispositivo, creando un attacco molto selettivo simile al **jamming** a livello MAC.

Non esistono contromisure contro i CTS falsi, poiché non sono crittografati e non è possibile distinguerli da quelli autentici. Tuttavia, in caso di attacco RTS/CTS, è ragionevole rilevare un numero anomalo di tali messaggi nella rete e segnalare un possibile problema – anche se ciò potrebbe indicare solo un comportamento insolito (ad esempio una PlayStation che comunica con un controller) e non necessariamente un attacco.

Fortunatamente, il protocollo Wi-Fi utilizza raramente RTS/CTS, poiché inviare questi messaggi richiede troppo tempo. Con le velocità di trasmissione attuali, i pacchetti di dati sono molto più brevi delle sequenze RTS/CTS, rendendole ingombranti. L'uso di RTS/CTS è giustificato solo quando la probabilità di collisioni è abbastanza alta da richiederlo; altrimenti, possiamo evitarlo sperando che non si verifichino collisioni.
#### **Problema del MTU (Unità Massima Trasmissibile)**

Il **MTU del Wi-Fi** è di 2000 byte, mentre per il protocollo Ethernet è di 1500 byte. Come è possibile trasmettere pacchetti da Wi-Fi su Ethernet?
La risposta è che l'MTU viene definito dall'Ethernet. Pertanto, in pratica, il Wi-Fi utilizza pacchetti molto più piccoli di quanto potrebbe e usa pacchetti più lunghi solo quando due stazioni Wi-Fi comunicano direttamente.
Il Wi-Fi implementa anche l'**aggregazione dei pacchetti**, quindi si potrebbero vedere pacchetti molto grandi passare attraverso la rete.

Non è corretto ignorare completamente i messaggi RTS/CTS, anche se vengono usati raramente. La Wi-Fi Alliance specifica chiaramente che i dispositivi devono essere sempre pronti a gestirli, anche se non vengono utilizzati frequentemente.

## 10.10 **WEP**

**Wired Equivalent Privacy**, abbreviato in WEP, è un algoritmo di sicurezza per le reti wireless IEEE 802.11. Introdotto come parte dello standard originale 802.11 ratificato nel 1997, aveva l'obiettivo di fornire una confidenzialità dei dati paragonabile a quella di una rete cablata tradizionale: nomen omen.

Non appena il Wi-Fi è stato creato, è stato immediatamente chiaro che inviare dati in chiaro non era una buona idea – non perché fosse desiderata una forte crittografia per la privacy, ma a causa della coesistenza dei canali. In pratica, gli sviluppatori non volevano che tutti potessero ascoltare ciò che trasmettevano gli altri. Il WEP è stato introdotto per questa ragione e, come implica il nome, offriva lo stesso livello di privacy di un cavo: tutti sullo stesso cavo potevano ascoltare ciò che trasmettevano gli altri. Lo scopo non era introdurre la privacy tra i nostri dispositivi e l’AP, ma solo tra reti diverse.

### 10.10.1 **Autenticazione e associazione**

Poiché il WEP ha introdotto la crittografia nelle reti Wi-Fi, doveva includere un metodo per unirsi e lasciare la rete. Nel Wi-Fi, questo richiede due passaggi: **autenticazione** e **associazione**.

Questi due passaggi sono diversi, e non si può dare per scontato che si possa autenticare e associare automaticamente a una rete. L’autenticazione funziona solo se un dispositivo è stato in grado di accedere alla rete, mentre l’associazione ci dice se il dispositivo è effettivamente nella rete.

Il motivo dell'esistenza del meccanismo di associazione risiede nel fatto che, all'epoca, i punti di accesso erano macchine piuttosto semplici, molto costose e con gravi limitazioni hardware. Potevano gestire solo un numero limitato di dispositivi alla volta, quindi, per gestire reti con centinaia di dispositivi, era necessario il meccanismo di associazione per consentire la comunicazione solo a determinati dispositivi (quelli associati), mantenendo gli altri parzialmente pronti a trasmettere (quelli solo autenticati).

![[Pasted image 20241205083644.png]]

I passaggi che un dispositivo deve eseguire per connettersi a una rete Wi-Fi sono illustrati in figura. Questo processo avrebbe potuto essere gestito diversamente, ad esempio con due soli stati (il primo e l'ultimo) e un codice di ritorno che indicava al dispositivo il motivo per cui non poteva unirsi alla rete in un determinato momento. Tuttavia, avere tre stati consente uno switch più rapido tra di essi: è più efficiente rimuovere un dispositivo dall’elenco di associazione e riammetterlo piuttosto che espellerlo completamente dalla rete.

Questi passaggi vengono effettuati tramite frame di gestione, che non sono crittografati, quindi un attaccante potrebbe facilmente utilizzare pacchetti falsificati per impedire a qualcuno di associarsi a una rete. In realtà, è così facile che gli attaccanti potrebbero annoiarsi rapidamente.

(Come al solito) È importante capire che autenticazione e associazione sono due concetti saparati: 
- Uno dice *conosco chi sei*
- L'altro *puoi fare questo o quello*
Un device non può comunicare con entrambi senza aver completato con successo entrambe le fasi, i pacchetti mandati in una delle due fasi intermedie saranno scartati dall'access point

L’autenticazione dimostra che conosciamo qualcosa. È eseguita in tre passaggi:
1. Il dispositivo che vuole unirsi alla rete invia una richiesta di autenticazione.
2. Il punto di accesso risponde con una **sfida**.
3. Il dispositivo risponde con una **sfida crittografata** (usando il segreto della rete, ovvero la password, che solo gli utenti legittimati dovrebbero conoscere)
L' associazione a questo punto non è altro che una semplice two-way richiesta-risposta, necessaria solo per essere sicuri che l'AP ha abbastanza risorse disponibili, come indirizzi IP e spazi nella tabella di routing

**Dove sta il problema?**
La sfida in pratica non è altro che un piccolo insieme di bytes, e cosi è anche la sfida crittografata, (la chiave viene usata come una chiave simmetrica) il processo non autentica realmente un dispositivo specifico. Tutto ciò che facciamo è dimostrare di conoscere qualcosa (un segreto, che in realtà non è nemmeno così tanto privato). Un AP non saprà mai realmente chi sei, anche guardando gli indirizzi MAC.
Inoltre, il problema reale è che con questo meccanismo di sfida l’attaccante vede sia il testo in chiaro che la sua forma crittografata, che è un esempio drammatico di **leakage di informazioni**, consentendo facilmente attacchi brute force per recuperare la password.

#### **Altro su attacchi di autenticazione e associazione**

Andremo a vedere alcuni modi creativi per eseguire un attacco (DoS) su una rete Wi-Fi (non solo quelle con la WEP encryption)

- **De-associazione**: Un attaccante può fingere di essere l’AP e de-associare i dispositivi. Il risultato è che il dispositivo non solo non può comunicare, ma potrebbe anche sovraccaricare l’AP inviando richieste ripetute, nonostante questo sia già stato associato. È possibile eseguire lo stesso attacco anche nella seconda fase, anche se difficile da eseguire poichè i device stanno in questa fase solo un breve periodo

- **De-autenticazione IP**: La vittima è costretta a ripetere il processo di autenticazione, fornendo un nuovo set di informazioni testo **chiaro-crittografato** all’attaccante. Accumulando questi dati, l’attaccante può recuperare la password, aumentando la possibilità di indovinarla.

Non esistono difese solide contro questi attacchi poiché i frame di gestione non sono crittografati, l'attaccante infatti non deve nemmeno essere connesso alla rete, ma gli basta creare un pacchetto con il giusto sorgente di indirizzo MAC, e la gestione dei messaggi in modo tale da sembrare un AP. In entrambi gli attacchi, non si riesce a notare la presenza di un attaccante, facendoci pensare che la rete semplicemente non funzioni (queste vulnerabiltà di design, possono essere sfruttate anche per futuri attacchi man-in-the-middle)

L’unica soluzione possibile è cambiare frequentemente il SSID(il nome della rete) e la password, ma questo introduce disagi per gli utenti, che potrebbero salvare le informazioni su carta o in luoghi non sicuri.

## 10.11 Wi-Fi frame 

![[Pasted image 20241205230717.png]]

L'intero **MAC header** non è mai crittografato nel Wi-Fi, nemmeno nei messaggi di dati. I messaggi di gestione e controllo non crittografano nemmeno il corpo del frame (e, naturalmente, l'autenticazione e l'associazione sono frame di gestione). Questi frame, specialmente i frame di dati, vengono trasmessi utilizzando modulazioni e codifiche che potrebbero differire da ciò che ci aspettiamo. Per questa ragione, quando abbiamo dispositivi con standard Wi-Fi diversi nella stessa rete (come 802.11b e 802.11n), l'header MAC viene trasmesso al tasso della modulazione più bassa, il che significa che più lungo è l'header, maggiore sarà il tempo necessario per trasmettere anche il payload.

**Esempio:**  
Supponiamo di utilizzare una codifica di modulazione molto alta, mentre l'AP utilizza 802.11b, che per standard ha una codifica di modulazione più bassa: l'AP non comprenderà la maggior parte dei nostri header, quindi dovremo trasmetterli a una modulazione più bassa. Questo è anche il motivo per cui non possiamo fidarci della velocità apparente della nostra rete, perché ciò che conosciamo è probabilmente il tasso massimo, mentre in realtà potrebbe essere molto più basso. In ogni caso, dobbiamo sempre essere consapevoli della versione esatta di Wi-Fi che stiamo utilizzando.

## 10.12 **Crittografia WEP**

Dal punto di vista dei metodi di autenticazione, probabilmente sappiamo già che esistono **WEP** e **WPA (Wi-Fi Protected Access)**, che non dovrebbero mai essere utilizzati, e poi **WPA2**, quello affidabile. Esiste anche **WPA3**, ma è meglio fare finta che non esista.

Un **stream cipher** è un cifrario simmetrico in cui i bit del plaintext vengono combinati con un flusso pseudocasuale di bit del cifrario (un **keystream**). Ogni bit del plaintext viene crittografato uno alla volta con il corrispondente bit del keystream, risultando in un bit del flusso di ciphertext. In pratica, l'operazione di combinazione è una XOR esclusiva. Lo stream cipher è utilizzato per crittografare sia gli scambi di autenticazione sia i pacchetti di dati (solo il payload) nei metodi di autenticazione WPA.

In generale, il problema con la crittografia dei dati (dati reali) è che dobbiamo crittografare un numero finito di byte, non un flusso continuo reale, e spesso dobbiamo anche ritrasmetterli (a causa di errori, pacchetti persi, ecc.). Inoltre, i pacchetti non sono ordinati: è perfettamente legittimo, dal punto di vista del trasmettitore, inviare un pacchetto mentre un altro è stato perso, poiché il livello 2 non si preoccupa delle ricevute (a differenza di **TCP**, che opera tuttavia al livello 4). Questo rende l'uso di stream cipher su singoli pacchetti (anziché sull'intero flusso di dati) sub-ottimale, poiché somiglia più a un **block cipher** (dove tutti i blocchi poichè sono indipendenti stessa confusione e diffusione facendo diventare questo metodo di cifratura meno efficiente)

OTP (One-Time Pad), invece, richiede un flusso di crittografia lungo quanto il messaggio; in pratica, invece di dividere il messaggio in blocchi, lo crittografa interamente. Tuttavia, potremmo crittografare il messaggio un byte alla volta mantenendo lo stato del byte precedente.

### 10.12.1 **OTP ripensato**

Il **cifratore a flusso Wi-Fi** (stream cipher) è molto simile a OTP. In OTP abbiamo bisogno di un messaggio e di una chiave generata casualmente (un segreto) K, lunga quanto il messaggio:  
- $C = M \oplus K$  Dove C è il ciphertext e M il messaggio.

Nel Wi-Fi, il segreto condiviso con il punto di accesso non è lo stesso K dell’equazione precedente; viene invece utilizzato come input per un **PRNG (Pseudo-Random Number Generator)**, una "scatola nera" che, dato un input, genera un flusso di bit o byte casuali.

Un PRNG genererà lo stesso numero casuale (a questo punto non così casuale) se viene inizializzato con lo stesso stato (il **seed**). Perciò, serve un seed crittograficamente forte, senza correlazioni tra i bit di output, sia a livello di bit singoli sia di coppie, triplette o multipli. Ogni bit, indipendentemente dalla sua posizione nel byte generato, deve avere esattamente il 50% di probabilità di essere 0 o 1 (indipendenza statistica).

I PRNG non sono altro che algoritmi e hanno stati interni; a un certo punto il loro stato ritornerà a quello iniziale, e i segreti si ripeteranno: questo si chiama **lunghezza del ciclo**, e per un buon PRNG deve essere il più lungo possibile. In pratica, il ciclo minimo deve essere più lungo del massimo pacchetto trasmissibile (64.000 bit nel Wi-Fi).

Alcuni PRNG sono sensibili a determinati numeri (ad esempio pari o dispari), il che significa che gli output generati da seed sensibili conterranno correlazioni significative. Per questa ragione, dobbiamo conoscere bene come funziona il nostro PRNG e potremmo dover escludere alcuni input. In generale, inizializzarlo con l’orario o con numeri molto grandi non è molto efficace.

Se abbiamo un buon PRNG e possiamo avere una chiave (un seed casuale) che può essere facilmente fornita al sistema e non è la stessa per ogni pacchetto, come facciamo a cambiare il seed per ogni pacchetto?

#### **Crittografia del payload**

![[Pasted image 20241205235320.png]]

Per crittografare i payload dei pacchetti di dati, il WEP usa la password Wi-Fi per ottenere la chiave segreta, che è un semplice hash della password stessa (altrimenti non sarebbe abbastanza casuale, poiché probabilmente userebbe lettere prevedibili a causa dei codici ASCII). La procedura di crittografia per il WEP è la seguente:

1. Esegui l’hash della password della rete Wi-Fi per ottenere il segreto (chiave).
2. Concatenare la chiave con l’IV (**Initialization Vector**, un input a dimensione fissa richiesto per essere casuale o pseudo-casuale) per ottenere il seed del PRNG.
3. Usare il PRNG per generare un flusso casuale di byte.
4. Concatenare il plaintext con l’**ICV (Integrity Check Value)**, un hash del plaintext.
5. Applicare XOR ai bit del punto 4 con il flusso casuale generato al punto 3.
6. Aggiungere l’IV all’inizio del messaggio cifrato.

**Problemi del WEP**

1. **Chiave segreta troppo corta:** La chiave è lunga solo 40 bit, che sono troppo pochi. Non importa quanto complessa sia la password, il WEP la codifica sempre in un hash di 5 byte, rendendolo vulnerabile alle collisioni.
2. **IV troppo corto:** Con 24 bit, l’IV si ripete dopo 2242^{24} pacchetti (circa 16 milioni). In una rete moderna, questo limite può essere raggiunto in circa 5 ore.
3. **Debolezza del PRNG RC4:** L’RC4, utilizzato come PRNG, ha correlazioni tra la chiave e il seed, rendendo possibile derivare la chiave dalla sequenza generata.
4. **ICV (CRC32) debole:** L’ICV è solo un controllo di integrità, non un hash sicuro. Non ha né confusione né diffusione, rendendolo facile da indovinare per un attaccante.

L' RCV è anche un lui uno stream cipher, usato per la sua semplicità e velocità nel software.
Mentre per CRC (Cyclic redundancy check) si intende un algoritmo di error detection, usato principalmente nelle rete digitali per evidenziare i cambiamenti accidentali ai dati. Il 32 indica che la lunghezza dei bit è di 32 byte.

La **WEP decryption** è molto simile all'encryption: avendo la chiave segreta e l'IV (ottenuti dal pacchetto), rigeneriamo il seme, ottiena la sequenza della chiave, decifriamo il testo cifrato a quel punto controlliamo l'ICV.

![[Pasted image 20241206084610.png]]

### 10.12.2 **Attacchi alla cieca**

Si potrebbe pensare di essere al sicuro poiché l’attaccante vede solo il testo cifrato e non ha accesso al plaintext. Tuttavia, durante l’autenticazione, trasmettiamo sia il testo in chiaro che la sua versione cifrata. Un attaccante può semplicemente de-autenticare un dispositivo, permettergli di ri-autenticarsi e ottenere entrambi i dati. Questo consente all'attaccante di rivelare le correlazioni nell'RC4 e recuperare la chiave.

Il **CRC32** è ancora peggio del previsto, perché il suo codice è pubblico. È veloce, ma anche **lineare** e facilmente invertibile. In pratica, non è altro che un'operazione di XOR e shift.

Normalmente, per modificare un messaggio, dobbiamo decodificarlo e poi ricodificarlo dopo averlo modificato. In un attacco a occhi chiusi (**blind attack**), non è necessario decodificare tutto: dobbiamo solo **flippare** alcuni bit. Ad esempio, per cambiare "sì" in "no", basta flippare i bit che contengono la parte "sì". Nei protocolli binari conosciamo la posizione e il significato dei bit, quindi possiamo cambiare qualsiasi valore in un altro.

Ma come flippiamo un messaggio?
Se conosciamo il testo in chiaro, prendiamo il messaggio e applichiamo una XOR con "1" nei punti in cui vogliamo effettuare il bitflipping, lasciando "0" nelle altre parti.

Possiamo fare lo stesso con un messaggio cifrato se la crittografia è stata effettuata con una semplice XOR (come nel caso dello stream cipher del WEP). Il CRC potrebbe teoricamente impedirlo, ma essendo il CRC basato sul messaggio, che a sua volta è composto dall'**IV** concatenato ai dati reali da inviare ($M_p$), possiamo suddividere la chiave $K$ in due parti di pari lunghezza ($K_p$ e $K_c$), come mostrato nell'equazione:
- $C = K \oplus M$ 
- $= (K_p \| K_c) \oplus (M_p \| CRC(M_p))$
- $= (K_p \oplus M_p) \| (K_c \oplus CRC(M_p))$
- $= C_p \| C_c$

Dove:
- $M_p$: messaggio,
- $CRC(M_p)$: checksum,
- $C$: messaggio cifrato.

Grazie alla linearità del CRC, possiamo calcolare $M_p' = M_p \oplus d$, dove $d$ è un messaggio lungo come $M_p$, composto da zeri e con "1" nelle posizioni in cui vogliamo flippare i bit.

L'equazione si evolve così:
- $C' = K \oplus (M_p' \| CRC(M_p'))$
- $= (K_p \oplus M_p \oplus d) \| (K_c \oplus CRC(M_p) \oplus CRC(d))$ 
- $= (C_p \oplus d) \| (C_c \oplus CRC(d))$

Anche senza conoscere $M_p$ o $CRC(M_p')$, possiamo manipolare i bit grazie alle proprietà di linearità. Questo ci consente di flippare i bit di un messaggio senza doverlo decrittare, semplicemente ipotizzando il tipo di pacchetto inviato.

### 10.12.3 **L'attacco "chop-chop" di KoreK**

**Abbiamo davvero bisogno della chiave segreta per decrittare un messaggio? Spoiler: no.**

Il WEP utilizza un IV di 24 bit, con oltre 16 milioni di possibilità. Supponendo di raccogliere tutti i pacchetti in una rete Wi-Fi, possiamo eliminare quelli con IV duplicati e salvare solo quelli con IV unici. Dopo un po', avremo una mappatura completa degli IV con i relativi keystream, permettendoci di decodificare la rete senza conoscere la chiave segreta. Tipicamente infatti un messagio Wi-Fi (un pachetto) contiene solo 2300 bytes, per cui 40 GB di dati potrebbe bastare per memorizzare ogni possibile keystream
#### **Metodi per estrarre il keystream:**

1. **Attacco di de-autenticazione**: otteniamo un piccolo frammento di keystream, da ampliare successivamente.
2. **Attacco "chop-chop"**: sfruttiamo pacchetti di lunghezza fissa (tipici degli ambienti DHCP) per ottenere **frammenti** del keystream. Dovremmo quindi essere in grado di ricostruirci quello che non sappiamo tramite l'attacco chop chop.

Ecco come funziona l’attacco "chop-chop" (assumiamo di non conoscere niente del pacchetto):
- **Esempio**: Supponiamo di sniffare un pacchetto cifrato (D0...D5, con CRC J3...J0), che risulta nel ciphertext S1...S9. Costruiamo un pacchetto più corto (D0...D4, con CRC I3...I0) e trasmettiamolo con lo stesso keystream. Il risultato è un pacchetto crittografato che va da S1 e S9 (sappiamo solo questo e non altro)

	![[Pasted image 20241206142517.png]]

- Ripetiamo il processo, tagliando progressivamente il messaggio (un byte in meno alla volta) e ricostruendo un byte alla volta il keystream completo. Il punto critico è che l’AP ci confermerà con un ACK quando avremo trovato il keystream corretto.

	![[Pasted image 20241206142538.png]]

	Notare che avremmo un altro CRC rispetto al pacchetto precedente, anche se supponiamo di crittografare il pacchetto con lo stesso keystream, da K0 a K9 in quanto sarà solo più corto di un byte (uccideremo solo K9). 
	Alcuni parti del nuovo pacchetto saranno identici al precedente, ovvero S0-S4 mentre S6-S9 e R5-R8 non hanno niente in comune, anche se in realtà con un po' di matematica scopriamo che esiste una relazione fra S6-S9 e R5-R8, dipende da un numero fra 0 e 255.
	Quindi in pratica potremmo ottenere un secondo pacchetto solo provando a indovinare il valore di questo numero. Facciamo questo fino ad ottenere i byte da R5 a R8. In realtà la relazione fra questi byte può essere espressa in termini di D5. 
	Quando dunque troviamo il giusto numero D5, ci possiamo ricavare anche K5, ovvero un byte del keystream. E così via, ricaviamo D4 e ottienamo K4 e successivamente anche K3, K2, K1 e K0, ottenendo tutto il Keystream.

Sarà effettivamente il numero giusto? 
Beh l'access point ce lo dirà! Basterà mandare i pacchetti all'AP e se ci risponde con un ACK vuol dire che i pacchetti sono stati ricevuti correttamente. Non importa che questi pacchetti abbiano senso per l'IP layer, abbiamo bisogno solo della conferma del keystream.
Se quindi con 128 tentativi otteniamo un byte... potremmo costruire il keystream abbastanza velocemente!

Esiste un altra drammatica conseguenza di questo, perchè una volta chiuso il keystream, non dobbiamo rifare tutto per ogni altro keystream. Ci basta fare il ping all'AP, infatti una volta ottenuto il primo keystream, mandiamo un messaggio di ping con questo. Il Ping è un ICMP echo, che ci ritorna un ICMP reply crittografato con un altro IV. Quest'ultimo è identico a ciò che mando eccetto un bit, che sappiamo esattamente dove calcolare, dunque calcolarsi qualsiasi altro keystream è un gioco

### 10.12.4 **L'attacco di Fluhrer, Mantin e Shamir** 

Nel 2001, Fluhrer, Mantin e Shamir hanno dimostrato che l'RC4 non era un buon generatore di numeri pseudo-casuali, consentendo di decifrare la chiave Wi-Fi con un numero sufficiente di pacchetti sniffati.

A differenza dell'attacco di KoreK, che è attivo, l’attacco contro RC4 è **passivo** e sfrutta le limitazioni intrinseche del PRNG.
#### **Evoluzione dell'attacco:**
- **2005**: Klein scopre ulteriori correlazioni nell’RC4.
- **2007**: Tews, Pychkine e Weinmann migliorano l’attacco, riducendo il numero di pacchetti necessari a 85.000 per una chiave di 104 bit.

#### **Possibili soluzioni:**
1. **Usare IV più lunghi**: rende l’attacco chop-chop più difficile ma non risolve i problemi di RC4.
2. **Abbandonare RC4**: è chiaramente insicuro.
## 10.13 **WPA**

Con il tempo, siamo finalmente passati al **WPA (Wi-Fi Protected Access)**, poiché il WEP aveva troppi problemi. WPA esiste in tre versioni: **WPA**, **WPA2** e **WPA3**, ma condividono tutte la stessa architettura di base.

Dalla figura possiamo notare immediatamente che WPA è molto più complicato rispetto al WEP, sebbene contenga ancora qualcosa di poco gradito: **RC4**.

![[Pasted image 20241206173857.png]]
### 10.13.1 **RC4 in WPA**

Perché RC4? Beh, era obbligatorio: le schede di rete erano costose e ingombranti all'epoca, e RC4 era integrato nell'hardware. Dire ai produttori di buttare via i loro prodotti non sarebbe stato ben accolto.

La questione era come **riutilizzare** l'hardware esistente in un sistema migliore. La soluzione fu creare un metodo che nella maggior parte dei casi potesse essere applicato come aggiornamento firmware, rendendolo allo stesso tempo più complesso per mitigare i bug dell'RC4.

Cosa cambia in WPA è che il seed del PRNG non è solo composto dall'**IV** e dal segreto, ma consiste in una chiave (ora lunga 128 bit) e altri dati aggiuntivi (**TSC0**, **TSC1**, **TSC2**, **TSC4**, **TSC5**, un indirizzo di trasmissione **TA** e una chiave temporanea **TK**). Questo nuovo protocollo di sicurezza si chiama **TKIP (Temporal Key Integrity Protocol)**.

- **TSC0-5**: contatori semplici.
- **TA (Transmit Address)**: indirizzo del trasmettitore.
- La chiave temporanea e l'indirizzo TA sono combinati in due fasi per generare l'input dell'RC4. (vedi figura)
- L’algoritmo di controllo dell'integrità è stato aggiornato al **MIC (Message Integrity Check)**, che garantisce solo l'integrità (come CRC) ma viene crittografato con una chiave separata prima della trasmissione.

WPA2 ha sostituito TKIP con **CCMP** e **AES (Advanced Encryption Standard)**, modificando le parti di crittografia e di controllo dell'integrità. Ciò ha permesso un sistema più semplice e leggermente più veloce rispetto a WPA.
### 10.13.2 **Sicurezza del WPA**

Prima del 2018, erano già stati trovati attacchi contro WPA e WPA2, come una variante dell'attacco **chop-chop**, che permetteva di costruire un dizionario di keystream. Tuttavia, l'attacco richiedeva una quantità di dati molto grande, rendendolo poco pratico.

Nel 2018 è stato scoperto **KRACK**, un attacco che sfruttava il **4-way handshake** di autenticazione per scoprire la chiave temporanea.

- In WPA/WPA2, la chiave temporanea è privata per ogni utente ed è negoziata durante le fasi di autenticazione e autorizzazione.
- A differenza del WEP, in cui ogni utente poteva decodificare i pacchetti di ogni altro utente, in WPA questo non è possibile senza conoscere la chiave temporanea dell'utente specifico.
- **KRACK** consentiva di decodificare i pacchetti di un utente specifico trovandone la chiave temporanea, sfruttando una vulnerabilità di progettazione intrinseca nel 4-way handshake. Vulnerablità di cattivo design che non può essere risolta...
#### **WPA3**

Quando è stato scoperto KRACK, la Wi-Fi Alliance ha creato in fretta e furia una nuova versione, **WPA3**, con un metodo di handshake chiamato **Dragonfly**, che nessuno aveva mai sentito prima.

Appena rilasciato, è stato trovato un attacco, **Dragonblood**, che lo ha reso persino peggiore di WPA2.

**Problemi principali di WPA3:**

- **Implementazione complessa**: i produttori devono aggiornare il firmware per supportarlo.
- **Sicurezza non migliorata**: presenta problemi simili ai predecessori.
- **Progettazione poco trasparente**: la Wi-Fi Alliance ha preso decisioni senza coinvolgere matematici o esperti di sicurezza per testare il design.

La storia ci insegna che gli standard progettati a porte chiuse spesso falliscono. Gli errori di progettazione devono essere evitati e gli standard devono essere pubblicamente discussi e **testati** nel tempo.

# Capitolo 12: Attacchi - cosa aspettarsi 

Non esamineremo tutti gli attacchi possibili, ma solo alcuni esempi che mostrano il tipo di situazioni che potremmo incontrare in una rete e le loro conseguenze.

Gli attacchi vengono sempre eseguiti contro una **vulnerabilità**: trova una vulnerabilità, trova un attacco. Paradossalmente, se non sappiamo di avere una vulnerabilità, gli attaccanti possono fare tutto ciò che vogliono. Di solito, se siamo certi di non utilizzare un determinato protocollo/software/applicazione (con vulnerabilità note), possiamo semplicemente ignorare gli attacchi relativi a quel particolare software.

## 12.1 **Classificazione**

Gli attacchi possono essere classificati in base alla vulnerabilità o al livello che sfruttano, come segue:

- livello applicativo;
- ...
- livello di trasporto;
- livello di rete;
- livello di collegamento dati;
- livello fisico.

#### **Perché i puntini sotto il livello applicativo?**

Quell'area rappresenta Internet, e il TCP/IP non fa parte del modello ISO/OSI. Normalmente, dopo il livello di trasporto e di rete non ci sono altri livelli su Internet, anche se ci sono esempi che dimostrano che non è sempre così.

**Esempio:**  
**QUIC** è un protocollo inventato da Google e successivamente sottoposto a standardizzazione, dove è stato pesantemente modificato. Viene utilizzato in **HTTP/3**, una leggera modifica di HTTP/2 che usa QUIC invece di TCP e TLS. QUIC funziona sopra UDP e fornisce tutte le funzionalità di sessione. In pratica, ha reimplementato TCP sopra UDP. Questo è un esempio di un livello situato dove si trovano i puntini nella lista precedente.

## 12.2 **Attacchi al livello fisico**

Non c'è molto da dire su questo tipo di attacchi, tranne che sono ==estremamente efficaci== perché interrompono il mezzo fisico. Vanno dal **jamming** (il più ovvio) alla distruzione fisica della rete.

Gli attacchi al livello fisico non devono mai essere sottovalutati. Ad esempio, il jamming è molto efficace, e l'unico modo per fermarlo è una triangolazione costosa del segnale (cioè trovare l'antenna che emette, andare lì e affrontare fisicamente l'attaccante).

Anche nelle reti cablate, gli attacchi al livello fisico sono pericolosi, poiché le probabilità che si verifichino non sono così basse come si potrebbe pensare:

- **2015**: qualcuno ha tagliato i cavi in fibra ottica nell'area della Baia di San Francisco (California).
- **2020**: torri per la telefonia mobile sono state attaccate da idioti che sostenevano che il 5G diffondesse il COVID-19.

Gli attacchi fisici hanno il vantaggio aggiuntivo di essere praticamente gratuiti, poiché l'unica cosa necessaria è sapere dove si trovano i cavi. Per il proprietario della rete, il costo consiste nel dover sostituire un cavo lungo, lasciando nel frattempo un'enorme area senza copertura (inclusi bancomat, telecamere di sorveglianza, reti bancarie, ecc.).

Per prevenire attacchi al livello fisico, si può utilizzare la **ridondanza**: non bisogna fare affidamento su un singolo elemento fisico se la rete richiede un alto livello di affidabilità.

**Esempio:**  
I cavi sottomarini in fibra ottica sono molto spessi, anche se proteggono un cavo sottile come un dito, perché devono essere protetti dagli squali che li mordono. Seriamente.

## 12.3 **Attacchi al livello di collegamento dati**

Gli **attacchi al livello di collegamento dati** sono più sofisticati e dipendono dal protocollo del livello dati, quindi gli attacchi al Wi-Fi non funzionano su WiMAX, **802.15.4** o Ethernet.

Esempi di attacchi:

- **Wi-Fi RTS/CTS**: vedi sezione 10.9.1.
- **Inondazione di pacchetti**: consiste nel sovraccaricare la rete inviando troppi pacchetti; può essere eseguito su quasi tutte le reti.
- **Collisione di datagrammi**: molto efficaci e semplici, specialmente se c'è una qualche forma di coordinamento nella rete (ad esempio, in una topologia ad anello con token, un attaccante potrebbe semplicemente generare un token per disturbare l'intero sistema).
- **Modifiche ai tempi MAC**: in Ethernet, se un router è occupato mentre un dispositivo tenta di inviare un pacchetto, cosa succede se dieci dispositivi usano una politica e un altro dispositivo ne usa una diversa? Probabilmente, quello in disaccordo funzionerà male o funzionerà eccezionalmente bene, interrompendo la rete per gli altri utenti.
- **Attacchi ai dispositivi di livello 2**: questi attacchi, anche se difficili, sono numerosi (come l'overflow del buffer di uno switch, descritto di seguito). Più è complicato il sistema, più creativo sarà l'attacco.

**Esempio - Overflow del buffer di uno switch:**  
Gli attacchi ai dispositivi di livello 2 sfruttano il fatto che anche se un sistema è semplice e non ha un sistema operativo (come uno switch normale), ha comunque elettronica e logica per decodificare i pacchetti e instradarli.

Cosa succede se due dispositivi inviano pacchetti contemporaneamente allo stesso destinatario?

- Uno switch economico simulerà una collisione e scarterà entrambi i pacchetti.
- Uno switch migliore tratterrà uno dei pacchetti per inviarlo successivamente.

La tabella di associazione MAC-porta fisica in uno switch non ha lo stesso numero di voci delle porte fisiche, ma molte di più (ad esempio, potremmo avere altri switch collegati a ciascuna porta, che moltiplicano il numero di ingressi). Se uno switch non ha una voce in tabella, non esegue una scoperta dei dispositivi; invia invece il pacchetto in broadcast a tutte le porte, diventando di fatto un hub. Ciò riduce drasticamente le prestazioni dell'intero sistema.

Un utente normale noterà una perdita di prestazioni improvvisa, ma non capirà il motivo, che potrebbe essere un attacco. 

## 12.4 **Attacchi al livello 2.5**

Gli attacchi al **livello 2.5** sono un caso particolare, in quanto non mirano realmente al livello 2.5 (che in realtà non esiste), ma prendono di mira le API tra L2 e L3 (i protocolli necessari per collegare questi due livelli, in particolare il protocollo di scoperta dei vicini, Neighbor Discovery Protocol). A volte vengono classificati come attacchi a livello MAC, altre volte come attacchi a livello 3.

Gli attacchi al livello 2.5 esistono perché, in protocolli come TCP/IP, dove il livello di collegamento dati può essere qualsiasi cosa, non possiamo fare alcuna assunzione su di esso. Pertanto, dobbiamo usare alcuni protocolli in grado di svolgere funzioni che L3 potrebbe non considerare garantite. Questi protocolli sono **ARP (Address Resolution Protocol)** per IPv4 e **NDP (Network Discovery Protocol)** per IPv6, e vengono utilizzati per scoprire l'indirizzo del livello di collegamento, come un indirizzo MAC, associato a un determinato indirizzo del livello Internet.

**ARP e NDP sono obbligatori**, poiché non esiste altro modo per collegare un indirizzo IP a un indirizzo MAC. A volte vengono utilizzate alternative per NDP a causa del suo alto costo computazionale, ma supponiamo di utilizzare solo ARP e NDP. Per funzionare correttamente, essi richiedono:

- tradurre un indirizzo IP in un indirizzo MAC;
- essere plug & play (non richiedere configurazione), motivo per cui non c'è sicurezza o chiave crittografica associata ad ARP e NDP;
- essere veloci (protocolli pesanti sarebbero inutili, poiché i pacchetti dovrebbero richiedere solo pochi millisecondi per essere trasmessi tra dispositivi);
- supportare reti contenenti macchine con indirizzi IP variabili rispetto ai loro indirizzi MAC;
- supportare reti abilitate a broadcast/multicast;
- essere in grado di sovrascrivere rapidamente un'associazione esistente (es. quando si cambia un cavo Ethernet da una porta a un'altra, il dispositivo dovrebbe mantenere il proprio indirizzo IP originale).
### 12.4.1 **ARP e NDP in breve**

**ARP** e **NDP** funzionano nello stesso modo.

Le nostre macchine hanno **buffer**. Quando si invia un pacchetto tramite IP (dopo aver già attraversato TCP o UDP), esiste una tabella di cache ARP (IPv4) o di scoperta dei vicini (IPv6).

Ogni porta ha un buffer contenente gli indirizzi IP e MAC di tutti gli altri dispositivi collegati alla stessa rete e il loro stato (indicando se le voci sono aggiornate). Quando si invia un pacchetto, il livello IP verifica se l'indirizzo IP è presente nella tabella:

- Se è presente ed è sufficientemente aggiornato, il pacchetto viene inviato immediatamente utilizzando l'indirizzo MAC associato a quell'indirizzo IP.
- Le voci vengono generate e aggiornate utilizzando messaggi di livello 4 o ARP/NDP.

**Differenze principali tra ARP e NDP:**

- **NDP** non ha un indirizzo di broadcast (usa l'indirizzo multicast del nodo sollecitato).
- **ARP** non utilizza IP, poiché gli indirizzi sono incapsulati direttamente nel frame Ethernet, mentre NDP usa ICMP, che è sopra IP.

Questo significa che ARP deve mantenere molte più informazioni extra, mentre NDP le ottiene direttamente dagli header ICMP e IP.

#### **Formato del frame ARP**

![[Pasted image 20241208153812.png]]

Il frame ARP è molto semplice. Alcuni campi dimostrano che ARP è stato progettato per trasportare informazioni di qualsiasi supporto e protocollo (non solo Ethernet/Wi-Fi e IP):

- **HTYPE** (hardware type): uguale a 1 per Ethernet;
- **PTYPE** (protocol type): 0x0800 per IPv4;
- **HLEN** (hardware length): lunghezza dell'indirizzo hardware in byte (= 6);
- **PLEN** (protocol length): lunghezza dell'indirizzo IP in byte (= 4);
- **Operazione ARP**: richiesta (= 1) o risposta (= 2);
- **SHA** (sender hardware address): di solito l'indirizzo MAC sorgente;
- **SPA** (sender protocol address): di solito l'indirizzo IP sorgente;
- **THA** (target hardware address): di solito l'indirizzo MAC di destinazione;
- **TPA** (target protocol address): di solito l'indirizzo IP di destinazione.

La richiesta può essere inviata in broadcast o unicast. Di solito il broadcast viene usato quando non si conosce il destinatario, mentre l’unicast viene usato quando si ha almeno un’idea di dove si trovi il destinatario.

La risposta può essere sia unicast che broadcast. La risposta unicast è piuttosto ovvia: inviamo una richiesta in broadcast, e chiunque voglia rispondere lo fa inviandoci una risposta direttamente. La risposta in broadcast è chiamata gratuitous ARP, e non è solo inutile, ma rappresenta il vero problema dell'intero protocollo.

Nota che manca qualcosa nel frame, in particolare il numero di sequenza (non c'è modo di associare una richiesta a una risposta, soprattutto perché ARP non si preoccupa di chi sta inviando una risposta e per quale motivo) e la firma del mittente (nessuna protezione contro errori o indirizzi falsificati).
#### **Formato del frame NDP**

![[Pasted image 20241208162312.png]]

Il frame NDP è leggermente diverso perché utilizza IP per i suoi pacchetti (i messaggi ICMP sono incapsulati in frame IP).

Per questa ragione, NDP non ha bisogno dell'indirizzo IPv6 del mittente, dato che lo ricava dall'header IP. Lo stesso vale per l'indirizzo MAC sorgente, che è trasportato dal frame MAC (questo vale anche per ARP, dove questo indirizzo è ridondante). Tuttavia, se necessario, l'indirizzo MAC sorgente può essere incluso nel campo SLLAO (Source Link-Layer Address Option): di fatto, possiamo inviare richieste e risposte NDP contemporaneamente dallo stesso indirizzo MAC in modo legale. I campi rimanenti sono simili a quelli del frame ARP.

La risposta NDP non è identica a una richiesta, come invece accade con ARP, ma viene inviata all'indirizzo unicast del mittente, e alcuni bit sono indefiniti, il che la rende leggermente più corta. Il campo SLLAO contiene l'indirizzo MAC del richiedente (nella richiesta) e del risponditore (nella risposta).

NDP è quindi un meccanismo di richiesta-risposta, dove la richiesta viene inviata all'indirizzo multicast del nodo sollecitato e la risposta all'indirizzo unicast (che non ha bisogno di essere tradotto in un indirizzo MAC come accade in ARP, poiché lo è già e viene automaticamente tradotto direttamente in un indirizzo Internet a livello IP). Solitamente, riceviamo una richiesta, leggiamo l'indirizzo del livello di collegamento sorgente, creiamo una voce temporanea e inviamo una risposta; se il mittente invia un'altra risposta, la voce passa da temporanea a valida. La risposta è inviata all'indirizzo unicast.

**Esempio**  
Supponiamo di avere due schede Ethernet con indirizzi MAC diversi, gestite come un set gemellato; avere due indirizzi MAC distinti è necessario perché, anche se avessimo una configurazione perfetta e riuscissimo a mantenere una delle NIC completamente silenziosa, lo switch non avrebbe tabelle adeguate, quindi se spegniamo una scheda e ne attiviamo un'altra, il dispositivo sarebbe confuso perché vedrebbe le trasmissioni provenire da un cavo e poi dall'altro. In questo caso, che non è raro nei sistemi a livello enterprise, vogliamo mappare istantaneamente (o quasi) un indirizzo IP da un indirizzo MAC a un altro.

Il problema qui è che dobbiamo informare chiunque stia comunicando con noi che la sua cache ARP o NDP deve essere aggiornata immediatamente, perché se non lo facciamo ci sarà un breve periodo, ma comunque inaccettabile in molti casi, durante il quale i pacchetti andrebbero persi.

Ad esempio, supponiamo che Alice stia parlando con noi, Bob; se cambiamo la nostra mappatura IP, passerà del tempo prima che Alice si accorga di stare parlando al vento, poiché supporrà che i pacchetti vengano scartati dalla rete per qualche motivo casuale. Solo quando la voce ARP nella cache di Alice passerà da valida a non valida, lei invierà una richiesta ARP unicast, e, vedendola fallire, probabilmente userà un broadcast, a cui Bob infine risponderà.

Nel peggior (ma normale) caso, il passaggio da una voce valida a una non valida o obsoleta richiede 30 secondi (timeout), durante i quali Alice invia dati ma non riceve alcuna risposta. L'unico modo per informarla che qualcosa è cambiato è dirglielo proattivamente, inviando un annuncio del vicino non sollecitato (gratuitous ARP).

#### **ARP spoofing**

La **vulnerabilità di design** dei gratuitous ARP permette attacchi di spoofing ARP (o ARP poisoning).

**Esempio:**  
Supponiamo di avere tre persone: Alice, Bob ed Eve, dove Eve è un attaccante sconosciuto agli altri due.

- Eve invia un gratuitous ARP unicast ad Alice, sostenendo che l'indirizzo IP di Bob è raggiungibile al suo indirizzo MAC.
- Eve fa lo stesso con Bob.

Finché Eve invia regolarmente questi pacchetti (ogni 30 secondi), Alice e Bob stabiliscono una connessione a livello di trasporto che fluisce attraverso Eve, che diventa un **man-in-the-middle**.

---

#### **Contromisure per ARP spoofing**

1. **Modificare il protocollo ARP/NDP**: una soluzione efficace ma che inevitabilmente perde alcune caratteristiche fondamentali del protocollo.
2. **Rilevare spoofing**: molti sistemi moderni segnalano gratuitous ARP sospetti, ma ciò non è sempre efficace se i messaggi sono inviati in unicast e lo switch non li inoltra a noi.
3. **Monitorare la rete**: implementato nello switch, blocca ARP gratuiti sospetti e consente failover da cavi Ethernet specifici.
4. **Evitare attaccanti sulla rete locale**: utilizzando lo standard **802.1X AAA**, che autorizza solo dispositivi specifici con certificati validi.
### Traduzione letterale:

---

### **12.5 - Attacchi al livello di rete**

Non entreremo nei dettagli sugli attacchi a questo livello, poiché discuteremmo di attacchi al livello IP, che esistono ma non sono particolarmente rilevanti. Infatti, anche se il livello IP fa molte cose, di per sé è un meccanismo semplice con funzionalità e obiettivi essenziali. Può essere sfruttato solo per **spoofing di indirizzi** e **attacchi di routing**, ma viene principalmente utilizzato come base per attacchi su altri protocolli specifici, che non mirano direttamente al livello IP stesso.

---

### **12.5.1 - Attacchi di frammentazione**

Il primo attacco che discuteremo non mira direttamente al livello IP (rete), ma sfrutta il modo in cui IPv4 gestisce l’**MTU** (Maximum Transmittable Unit) per eseguire un attacco di frammentazione.

L'MTU è un requisito fondamentale del livello di collegamento dati, poiché specifica la dimensione massima che il payload di un datagramma può avere in un determinato segmento di rete.  
È importante distinguere tra **MTU** e **PMTU** (Path MTU):

- L'MTU è quella vista da un host sulla rete a cui è connesso (quindi l'host conosce sempre questo valore).
- Il PMTU è valido lungo l'intero percorso del pacchetto, dalla sorgente alla destinazione.

Determinare il PMTU non è un compito semplice, poiché non può essere noto in anticipo; il percorso deve essere testato, poiché per calcolare questo valore l'host deve conoscere l'MTU di ogni rete tra la sorgente e la destinazione. Peggio ancora, il routing non è fisso, quindi il PMTU può cambiare durante la trasmissione di un pacchetto.

La frammentazione si verifica perché il livello applicativo del nodo sorgente ha fornito al livello di trasporto un blocco di dati troppo grande per quella rete. Questo può accadere per diversi motivi:

- TCP gestisce da solo il numero di byte che trasmette.
- **UDP**, invece, tenta di includere tutti i dati in un unico datagramma, quindi potrebbe inviare al livello IP un pacchetto troppo grande, costringendo IP a frammentarlo.

Un pacchetto che supera l'MTU può essere:

1. **Spezzato** tra i livelli IP e MAC e frammentato sotto il livello IP (un approccio non comune, ma utilizzato da protocolli come 6LoWPAN).
2. **Scartato**: viene inviato un messaggio agli strati superiori per notificare l'evento, sperando che i dati vengano suddivisi prima di essere ritrasmessi (metodo di IPv6).
3. **Frammentato** da qualsiasi router/host/dispositivo lungo il percorso (metodo di IPv4).

---

#### **IPv4 vs IPv6 nella frammentazione**

- **IPv6** richiede che il nodo sorgente conosca l'MTU; un nodo intermedio che riceve un pacchetto troppo grande semplicemente lo scarta e invia un messaggio alla sorgente per notificare l'accaduto. La frammentazione è responsabilità del nodo sorgente e viene utilizzata solo in casi estremi.
    
- **IPv4**, al contrario, consente a qualsiasi router lungo il percorso di frammentare un pacchetto che supera l'MTU della rete successiva. Questo processo è supportato direttamente dall'header IP, che contiene un campo **fragment offset** per accoppiare i frammenti dello stesso pacchetto. La responsabilità di riassemblare i pacchetti frammentati spetta alla destinazione finale.
    

Questo approccio presenta diversi problemi, in gran parte legati al modo in cui è strutturato l'header TCP.

---

#### **Attacchi di frammentazione con IPv4**

L'**offset di frammentazione** è misurato in unità di blocchi da 8 byte. Questo significa che il frammento minimo può contenere solo i campi **porta sorgente**, **porta di destinazione** e **numero di sequenza**. Le informazioni come i flag TCP (es. **SYN**) saranno nel secondo frammento.

Un firewall configurato per bloccare pacchetti con flag **SYN** consentirebbe il passaggio del primo frammento, che non contiene tali flag. Il secondo frammento, contenente il flag SYN, potrebbe passare perché non ha un header TCP completo, consentendo così di bypassare completamente il firewall.

Inoltre, possiamo inviare un primo frammento con un header TCP completo e un payload, e un secondo frammento che sovrascrive parte dell'header TCP stesso. Questo non è illegale in IPv4, poiché i pacchetti duplicati o frammentati lungo percorsi diversi possono essere riassemblati con frammenti sovrapposti, senza verificare se le parti sovrapposte siano identiche.

Questo permette l'**attacco di frammentazione IP**, che è tecnicamente un attacco TCP, sfruttando una vulnerabilità di design del livello IP.

---

#### **Contromisure**

La soluzione più semplice ed efficace per prevenire gli attacchi di frammentazione è ricostruire i pacchetti all'interno del firewall, evitando così che venga bypassato. Tuttavia, questo richiede risorse aggiuntive e lascia il firewall vulnerabile a **attacchi di flooding** di frammenti infiniti che ne esauriscono la memoria, causandone il crash.

---

### **12.5.2 - Attacchi DNS**

Gli attacchi DNS non riguardano interamente il livello IP, poiché il DNS è un servizio a livello applicativo.

Il **Domain Name System (DNS)** è il meccanismo che trasforma stringhe alfanumeriche in indirizzi IP. Fondamentalmente, è un grande database ridondante. Il suo compito è ricevere una richiesta (l'indirizzo IP associato a un indirizzo alfanumerico) e fornire una risposta (gli IP corrispondenti all'indirizzo richiesto).

**Obiettivo dell'attacco:** fornire all'utente una risposta sbagliata, possibilmente l'indirizzo di un sito simile a quello richiesto. Se l'utente non si accorge dell'errore, potrebbe inserire dati sensibili, portando a una fuga di informazioni.

---

#### **Elementi del DNS**

Il DNS è composto da tre elementi principali:

1. **Server DNS locale**
2. **Server DNS root**
3. **Server DNS autorevole**

Quando si effettua una richiesta DNS:

- La richiesta passa dal server DNS locale, che raggiunge il server autorevole grazie alla gerarchia ad albero dei server DNS.
- La risposta torna indietro lungo lo stesso percorso, fino al server DNS locale, che fornisce la risposta all'host.

Per velocizzare il processo si usa la **cache**, valida per un certo periodo.

---

#### **Attacco di avvelenamento DNS**

L'attaccante tenta di indurre il DNS a fornire una risposta errata. Poiché il DNS utilizza UDP, l'attacco consiste nel:

1. **Indovinare** la porta UDP di destinazione e l'ID del pacchetto.
2. **Inviare** una risposta falsa prima che arrivi quella corretta.

Un attaccante può anche sfruttare un complice per generare richieste controllate, aumentando le probabilità di successo.

**Contromisure:**

- Utilizzare porte casuali per le richieste DNS.
- Limitare le richieste DNS alla rete fidata.
- Implementare **DNSSEC** per comunicazioni DNS crittografate e firmate.
Ecco la traduzione letterale del testo fornito:

---

### **12.6 - Attacchi al livello di trasporto**

#### **12.6.1 - SYN Spoofing**

Peccato, peccato, a tutti piace peccare. Tipo, apriamo letteralmente connessioni ogni pochi minuti.  
O era SYN? Comunque, avete capito.  
Quando un computer riceve un SYN, si prepara per un flusso in arrivo riservando una certa quantità di memoria per i buffer TCP.  
Una connessione avviata con un SYN è una sorta di connessione semi-aperta durante la procedura di handshake a tre vie, ma consuma comunque risorse. Quindi, cosa succede se inviamo un SYN ma non rispondiamo ai successivi SYN-ACK?  
La risposta semplice è che il server elimina il SYN dopo che è scaduto un determinato timeout. La risposta complessa è che il timeout è critico, poiché è proporzionale al tempo di andata e ritorno (roundtrip time), ovvero il tempo necessario affinché un pacchetto vada e torni tra i due dispositivi che eseguono l'handshake. Questo tempo non può essere misurato perché il ricevente del SYN non sa quanto tempo ci è voluto per ricevere il SYN. Per determinare il timeout, deve essere fatta un'assunzione sul roundtrip time, e questa assunzione risulta essere piuttosto lunga, portando alla riserva di diversi megabyte di risorse.

Questo attacco è chiamato **SYN Spoofing** e consiste in un **SYN flooding**: l'attaccante invia carichi di pacchetti SYN a un server, ma non risponde ai relativi SYN-ACK.  
La parte interessante è che l'attaccante non ha nemmeno bisogno di usare il proprio indirizzo IP, poiché è sufficiente uno falsificato, e i SYN-ACK andranno altrove (lasciando libera la larghezza di banda dell'attaccante).  
Una volta che l'attaccante ha occupato tutte le risorse del server con i propri SYN, il server non sarà in grado di aprire nuove connessioni fino a quando quelle semi-aperte non saranno chiuse.

Come contromisura possiamo utilizzare i **SYN cookies**, una variazione che memorizza piccoli frammenti di informazioni per associare un SYN a una possibile connessione in arrivo, ma che alloca le risorse solo quando riceve l'ultimo ACK. L'attacco SYN rimane fattibile, ma estremamente improbabile.

---

#### **12.6.2 - TCP Reset Guess**

Un attacco completamente diverso al livello di trasporto è il **TCP Reset Guess**, una vulnerabilità di progettazione davvero pessima che parte da una semplice domanda: come si termina una connessione TCP?

Le connessioni TCP possono essere terminate in due modi: in modo non elegante o inviando un flag di reset.  
Il TCP è una macchina a stati "soft", il che significa che necessita di un flusso costante di dati per mantenere la connessione; se non vengono ricevute risposte in un determinato periodo di tempo, la connessione verrà chiusa in modo non elegante.  
Un **reset flag**, invece, indica all'altra parte che la connessione sarà chiusa dopo averlo ricevuto. E questo tipo di pacchetto può essere falsificato su una connessione in corso senza nemmeno guardare agli altri pacchetti di quel flusso.

Come al solito, un attaccante deve sapere:

- gli indirizzi IP sorgente e destinazione;
- le porte TCP sorgente e destinazione;
- il numero di sequenza corretto (nel flusso).

Le porte TCP possono essere indovinate, mentre il numero di sequenza deve solo essere ragionevolmente corretto: anche se il TCP è un protocollo basato su flussi, i pacchetti a livello basso arrivano in ordine casuale a causa dell'IP, quindi il TCP considera corretto tutto ciò che rientra nel suo buffer di ricezione. Quanto è grande questo buffer?

Il numero di sequenza è lungo 32 bit, quindi ci vorrebbero circa **284 giorni** per indovinare il numero corretto (bisognerebbe fare 2³² tentativi). Tuttavia, il TCP richiede che il numero di sequenza di un pacchetto di reset rientri in una finestra lunga 16 bit (che consiste nei numeri di sequenza mantenuti attivi dalla macchina).

Il risultato è che ci vogliono solo **6 minuti** per indovinare il numero corretto con un modem a 16k (che, per inciso, è molto lento), mentre con una normale connessione a 45 Mb/s sono necessari solo **13,6 secondi** o **11 minuti** nello scenario peggiore (dove non si sa nulla delle porte).  
Oggi il TCP utilizza moltiplicatori che spostano la finestra da 2¹⁶ a 2³² bit. Tuttavia, anche se la finestra TCP è di 2³² bit, bastano **4 tentativi** con una connessione veloce per indovinare il numero corretto.  
Praticamente, possiamo facilmente utilizzare questo attacco per impedire al nostro vicino di guardare Netflix o per buttare fuori dalla rete nostra sorella/collega/amico.

Il numero di sequenza avrebbe dovuto essere almeno a 64 o 128 bit, perché, anche se la finestra TCP è stata aumentata con il moltiplicatore, questo numero è ancora vincolato nell'header TCP, che non può essere modificato. Per questo motivo, non esiste un modo per prevenire questo tipo di attacco, nemmeno crittografando la connessione (poiché l'unica cosa che necessiterebbe di crittografia è proprio l'header TCP).

---

Se desideri continuare con la sezione **12.7 - Attacchi al livello applicativo**, fammi sapere!
### **12.7 - Attacchi al livello applicativo**

Passiamo ora al livello applicativo, sopra TCP. Tutti gli attacchi presentati in questa sezione sono solo alcuni esempi di quanto danno si possa fare con implementazioni o progettazioni errate, perché il numero effettivo di attacchi possibili a questo livello è molto più ampio.

Questi attacchi sono estremamente pericolosi perché colpiscono ciò che usiamo ogni giorno, ossia (e soprattutto) i browser web. Sono leggermente meno drammatici rispetto a quelli che interessano i livelli dal TCP in giù, perché è sempre possibile (anche se meno doloroso) cambiare i livelli superiori, e quindi possono essere mitigati aggiornandoli.

---

#### **12.7.1 - Attacchi di validazione dell'input**

Cominciamo mostrando quanto danno possa essere causato semplicemente sviluppando con il cervello spento.

---

**SQL è amore, SQL è vita**

Poiché vedremo quanto sia facile non pensare correttamente alle conseguenze di ciò che stiamo facendo, iniziamo con un esempio estremamente semplice di form HTML per username e password:

```html
<html>
<form action=retrieve.php method="get">
User: <input type="text" name="user">
<br>
Password: <input type="text" name="pass">
<input type="submit" value="Login">
</form>
</html>
```

Lo script PHP corrispondente è il seguente:

```php
<?php
$link = mysql_connect(’localhost’, ’test’);
mysql_select_db(’sql_inject’);
$user = $_GET[’user’];
$password = $_GET[’pass’];
$result = mysql_query("SELECT secret FROM userdb WHERE user = ’$user’
AND password = ’$password’");
$row = mysql_fetch_assoc($result);
echo $user."\’Secret is: ". $row[’secret’]. "\n";
?>
```

Ricorda che PHP, generalmente parlando, è davvero una pessima idea, e nessuno lo usa più al giorno d’oggi (si spera); tuttavia, rimane un buon esempio di ciò che si può fare. Nota che in questo form la password è oscurata per l'utente, ma se non utilizziamo HTTP con crittografia sarà trasmessa in chiaro - ma ignoreremo questa questione per il momento, poiché non è la cosa più pericolosa qui. Inoltre, l’uso di PHP è puramente ipotetico in questo esempio, perché ciò di cui ci occupiamo realmente è MySQL.

MySQL è un sistema di gestione di database relazionali (RDBMS) open-source, o nel nostro caso il modo più semplice per gestire una lista di coppie username-password (sebbene qualsiasi altro tipo di database SQL andrebbe bene).

La funzione di SQL in questo script è eseguire una query sul database e vedere se l’username e la password inseriti sono presenti (si spera non archiviati in chiaro). Se vengono trovati, il server mostrerà all’utente alcuni dati privati.

---

**Questo processo sembra privo di bug, giusto? Sbagliato.**

In realtà è altamente fallace e rappresenta un eccellente esempio di vulnerabilità dovuta a una cattiva implementazione (che si può trovare in una miriade di siti web in circolazione).

Un attaccante che non conosce né l’username né la password non sarà in grado di ottenere il segreto. Come regola generale, non dovremmo mai dire a un utente quale parte della query ha fallito in caso di informazioni errate (es. non specificare "utente non trovato" o "password errata"), perché potrebbe fornire all’attaccante dettagli aggiuntivi che potrebbero aiutarlo a perfezionare il suo attacco.

La riga incriminata nello script PHP è la query SQL:

```sql
SELECT secret FROM userdb WHERE user = ’$user’ AND password = ’$password’
```

Il motore SQL la interpreta esattamente così com’è, poiché lo script PHP (o Python, Ruby, ecc.) sostituisce semplicemente "password" con qualsiasi cosa l’utente abbia scritto. Praticamente, se inseriamo `'Alice'` come username e come password utilizziamo un carattere speciale come l’apostrofo (`'`), la query restituirà un errore, poiché la query effettiva sarà:

```sql
SELECT secret FROM userdb WHERE user = ’Alice’ AND password = ’‘’
```

Chiaramente, se questo errore trapela all’utente, lui o lei saprà che lo sviluppatore è stupido come un cumulo di sassi. A questo punto, possiamo semplicemente modificare l’inserimento e, invece di utilizzare un apostrofo, essere più creativi e sfruttare questa vulnerabilità per ottenere il segreto di un utente senza conoscere la sua password, ad esempio con:

```sql
SELECT secret FROM userdb WHERE user = ’Alice’ AND password = ’’ OR user = ’Alice’
```

Peggio ancora, in SQL ci sono molti altri caratteri speciali, come il meno (`-`), che indica l’inizio di un commento e può essere utilizzato per ottenere intere righe di una tabella fino al punto di scaricare l’intero database senza nemmeno conoscerne la struttura.

---

**La lezione appresa da questa vulnerabilità, tuttavia, non sta nell’iniezione SQL di per sé, ma nella ragione per cui è effettivamente possibile.**

In PHP 5 e versioni successive, le contromisure sono chiamate **magic quotes** e consistono in virgolette precedute da backslash che impediscono a un utente di inserirle in un campo e farle passare così come sono al backend. Tuttavia, il vero problema risiede nel fatto che lo sviluppatore non ha verificato l’input.

Infatti, l'iniezione SQL rientra nella categoria degli **attacchi di validazione dell'input**.

**Validare l'input è dannatamente doloroso**, ma dobbiamo sempre farlo, non solo quando l’utente inserisce del testo, ma su ogni singola funzione che scriviamo.

---

Se vuoi continuare con le sezioni successive, fammi sapere!