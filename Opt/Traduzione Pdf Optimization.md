 ### Dipartimento di Ingegneria dell’Informazione

**Università degli Studi di Firenze**

**Optimization Methods - Optimization Techniques for Machine Learning: Lecture Notes**

**Matteo Lapucci**

---

#### Contenuti:

1. **Preliminari**
2. **Introduzione ai Problemi di Ottimizzazione**
3. **Caratterizzazione delle Soluzioni di Problemi di Ottimizzazione**
    - 3.1 Esistenza di Soluzioni Ottimali
    - 3.2 Condizioni di Ottimalità
    - 3.3 Il Caso Non Vincolato
    - 3.4 Il Caso Vincolato
4. **Algoritmi di Ottimizzazione Non Vincolata**
    - 4.1 Metodi Iterativi di Ottimizzazione
        - 4.1.1 Esistenza di Punti di Accumulazione
        - 4.1.2 Convergenza alla Stazionarietà
        - 4.1.3 Efficienza dei Solver di Ottimizzazione
    - 4.2 Metodi di Discesa Basati su Line Search
        - 4.2.1 Line Search
        - 4.2.2 Direzioni legate al gradiente
        - 4.2.3 Risultati di Convergenza
    - 4.3 Metodo di Discesa del Gradiente
    - 4.4 Metodi del Gradiente con Momentum
        - 4.4.1 Metodo Heavy-Ball
        - 4.4.2 Metodi del Gradiente Coniugato
    - 4.5 Metodo di Newton
    - 4.6 Metodi Quasi-Newton
        - 4.6.1 Metodo BFGS
        - 4.6.2 Metodo L-BFGS
    - 4.7 Tecniche di Decomposizione
        - 4.7.1 Metodi di Decomposizione con Blocchi Sovrapposti
    - 4.8 Metodo del Gradiente Stocastico per Problemi con Somma Finita
        - 4.8.1 Analisi Teorica di SGD
5. **Algoritmi di Ottimizzazione Vincolata**
6. **Problemi di Ottimizzazione nel Machine Learning**
    - 6.1 Introduzione
    - 6.2 Regressione Lineare
        - 6.2.1 Caso senza Regolarizzazione
    - 6.3 Classificatori Lineari e Regressione Logistica
7. **Support Vector Machines**
    - 7.1 Il Problema Duale
    - 7.2 Soluzione del Problema Duale
        - 7.2.1 Sequential Minimal Optimization
        - 7.2.2 Proprietà di Convergenza di SMO con Regole di Selezione di Primo Ordine
        - 7.2.3 Selezione del Working Set usando Informazioni di Secondo Ordine
    - 7.3 Algoritmi per SVM Lineari
8. **Ottimizzazione su Larga Scala per Modelli Profondi**
    - 8.1 Miglioramenti di SGD per l’Addestramento di Reti Profonde
        - 8.1.1 Accelerazione
        - 8.1.2 Stepsizes Adattivi
    - 8.2 Differenziazione Automatica e Algoritmo di Backpropagation

---

## 1. Preliminari

In questa sezione riportiamo alcuni concetti preliminari, definizioni e proprietà che verranno usati ricorrentemente in queste note.

**Notazione:**

- Indichiamo con $e \in \mathbb{R}^n$ il vettore di tutti uno nello spazio euclideo $n$-dimensionale.
- Con $e_i \in \mathbb{R}^n$ indichiamo l’$i$-esimo elemento della base canonica, ovvero il vettore con tutte le componenti a zero eccetto la $i$-esima pari a 1.
- Dati due vettori $u, v \in \mathbb{R}^n$, la notazione $u^T v$ rappresenta il prodotto scalare tra $u$ e $v$, ovvero $u^T v = \sum_{i=1}^n u_i v_i$.
- Indichiamo con $| \cdot |$ la funzione norma; se non specificato altrimenti, assumiamo implicitamente che sia considerata la norma euclidea (in tal caso $|x|_2 = x^T x$).
- Denotiamo con $\mathcal{S}_n \subset \mathbb{R}^{n \times n}$ l’insieme delle matrici quadrate simmetriche di dimensione $n \times n$.
- Data una matrice $A \in \mathcal{S}_n$ (di cui sappiamo che gli autovalori sono numeri reali), denotiamo con $\lambda_{\text{min}}(A)$ e $\lambda_{\text{max}}(A)$ rispettivamente il più piccolo e il più grande autovalore di $A$.

**Definizione 1.1:** Una matrice $A \in \mathcal{S}_n$ è:

- Semidefinita positiva, denotata $A \succeq 0$, se $x^T A x \geq 0$ per ogni $x \in \mathbb{R}^n$;
- Definita positiva, denotata $A \succ 0$, se $x^T A x > 0$ per ogni $x \in \mathbb{R}^n, x \neq 0$.

**Proposizione 1.1:** Una matrice $A \in \mathcal{S}_n$ è semidefinita positiva se e solo se tutti gli autovalori di $A$ sono non negativi, cioè $\lambda_{\text{min}}(A) \geq 0$. Analogamente, $A$ è definita positiva se e solo se tutti gli autovalori di $A$ sono strettamente positivi, cioè $\lambda_{\text{min}}(A) > 0$.

**Proposizione 1.2:** Data $A \in \mathcal{S}_n, A \succeq 0$, per ogni $x \in \mathbb{R}^n$ abbiamo:

- $\lambda_{\text{min}}(A) |x|_2^2 \leq x^T A x \leq \lambda_{\text{max}}(A) |x|_2^2$;
- $\lambda_{\text{min}}(A) |x| \leq |A x| \leq \lambda_{\text{max}}(A) |x|$.

**Definizione 1.2:** Una funzione continua $f : \mathbb{R}^n \to \mathbb{R}$ si dice coerciva se $\lim_{k \to \infty} f(x_k) = +\infty$ per ogni sequenza ${x_k} \subseteq \mathbb{R}^n$ tale che $\lim_{k \to \infty} |x_k| = +\infty$.

**Proposizione 1.3:** Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione continua. Allora, $f$ è coerciva se e solo se tutti i suoi insiemi di livello sono compatti.

---

## 2. Introduzione ai Problemi di Ottimizzazione

L’Operations Research (OR) è un campo della matematica che si concentra sulla modellazione e sulla risoluzione di problemi reali attraverso strumenti matematici. In particolare, l’OR mira a descrivere compiti decisionali del mondo reale come problemi di ottimizzazione matematica e a risolverli mediante procedure numeriche.

L’Ottimizzazione Matematica (o Programmazione Matematica) è quindi un sottoinsieme dell’OR focalizzato sull’analisi formale dei problemi di ottimizzazione e sullo studio di procedure algoritmiche adatte a risolverli correttamente. Il workflow dell’approccio OR e l’oggetto della programmazione matematica sono riassunti nel diagramma della Figura 1.
![[Pasted image 20250108170907.png]]
L’obiettivo di queste note e del corso da cui originano è fornire agli studenti una panoramica completa di alcuni argomenti fondamentali nella programmazione matematica. L’oggetto principale attorno a cui ruota tutta la discussione che segue è dunque il problema di ottimizzazione matematica. Formalmente, un problema di ottimizzazione è definito come:
![[Pasted image 20250108171128.png]]
dove:

- $x$ è un vettore di variabili in uno spazio $n$-dimensionale; le variabili rappresentano le quantità che possiamo controllare nel compito reale e di cui dobbiamo decidere i valori da assegnare;
    
- $S$ è un sottoinsieme dello spazio delle variabili e viene chiamato insieme ammissibile, definito dai vincoli. Questo insieme identifica le scelte di valori per le variabili che sono considerate ammissibili da utilizzare nella pratica. Una scelta di valori delle variabili al di fuori dell’insieme ammissibile è quindi proibita;
    
- $f$ è una funzione obiettivo che, data una soluzione, ne misura numericamente la qualità. Senza perdere di generalità, assumiamo che lavori più piccoli di $f$ sono associati a migliori soluzioni, vogliamo quindi _minimizzare_ la funzione. Questo non è restrittivo: se vogliamo massimizzare $f(x)$ potremmo ugualmente minimizzare $g(x) = -f(x)$
    
**Esempio 2.1 (Problema di Selezione di Portafoglio Ottimale):**  
Uno dei problemi di ottimizzazione più famosi è quello di selezionare in modo ottimale come allocare risorse finanziarie. Indicativamente, supponiamo che esistano $n$ asset di mercato nei quali possiamo investire un'unità di capitale. Ogni asset $i$ è associato a un rendimento atteso $\mu_i$, ossia il guadagno previsto per unità di investimento. Inoltre, per ogni coppia di asset $i$ e $j$, esiste un coefficiente di covarianza $\sigma_{ij}$, che è alto se i rendimenti dei due asset sono positivamente correlati, negativo se sono negativamente correlati, e nullo se i rendimenti sono indipendenti. La quantità $\sigma_{ii}$ indica la varianza del rendimento dell’asset $i$.

Il problema di selezione degli investimenti può essere modellato come un problema di ottimizzazione:

1. Definiamo un vettore di variabili $x \in \mathbb{R}^n$; il valore di ogni variabile $x_i$ rappresenta la quantità di capitale investita nell’asset $i$.
2. L’insieme ammissibile è definito dai seguenti vincoli:
    - Gli investimenti devono essere non negativi (non possiamo vendere quote di asset):  
	        $x_i \geq 0 \quad \forall i$ 
    - Il capitale totale investito deve essere pari a 1, ossia la somma delle quantità investite in tutti gli asset deve risultare 1:  
        $\sum_{i=1}^n x_i = 1 \quad (e^T x = 1)$
3. La funzione obiettivo più comune è quella di bilanciare il rendimento totale atteso dell’investimento e il rischio associato. Il rendimento atteso totale è dato dalla somma dei rendimenti attesi degli asset moltiplicati per il capitale investito in ciascun asset:  
    $\sum_{i=1}^n \mu_i x_i \quad (\mu^T x)$  
    
    Il rischio è definito come segue:  
    $\sum_{i=1}^n \sum_{j=1}^n \sigma_{ij} x_i x_j \quad (x^T \Sigma x, \sum_{ij}=)$ 
    dove $\Sigma_{ij}$ (matrice delle covarianze) con:  $\sum_{ij} = \begin{cases} \frac{1}{2}\sigma_{ij}, & \text{se } i \neq j \\\\ \sigma_{ii}, & \text{se } i = j \end{cases}$​
**Razionale della definizione del rischio:** Interpretiamo il rischio come l’investimento in un asset con alta varianza, dato che ci sono alte probabilità di ottenere un ritorno molto inferiore rispetto a quello atteso. Se $\sigma_{ii}$ è elevato e $x_i^2$ è grande, stiamo assumendo un rischio significativo. Inoltre, se due asset sono positivamente correlati ($\sigma_{ij} > 0$), investire in entrambi comporta un rischio, dato che c’è una grande probabilità che l’asset $i$ performi peggio del previsto se anche l’asset $j$ lo fa. Al contrario, si vuole promuovere l’investimento in asset negativamente correlati, poiché una perdita di un asset potrebbe essere compensata dall’aumento dell’altro.

**Scopo:** Minimizzare il rischio e massimizzare il rendimento. Nel contesto di un problema di minimizzazione, possiamo definire una funzione obiettivo che è una combinazione pesata del rischio e del negativo del rendimento atteso:

$- \mu^T x + \lambda x^T \Sigma x$

dove $\lambda$ è un parametro che bilancia il compromesso tra rischio e rendimento.

**Problema finale (in forma vettoriale):**

$\min_{x \in \mathbb{R}^n} -\mu^T x + \lambda x^T \Sigma x \quad$ 
$\text{s.t. } e^T x = 1$
$x \geq 0$

In queste note saremmo interessati negli aspetti della programmazione matematica della ricerca operativa. Ci focalizzeremo sulla caratterizzazione dei problemi, e sulle procedure algoritmiche per determinare le soluzioni a tali problemi.

![[Pasted image 20250108174217.png]]

Qui ci occuperemo di problemi non lineari e continui di ottimizzazione, sia con che senza vincoli, avendo accesso alle informazioni delle derivate.

## 3. Problemi di ottimizzazione: caratterizzazione delle soluzioni

TBD

## 4. Algoritmi di Ottimizzazione Non Vincolata

### 4.1 Metodi Iterativi di Ottimizzazione

#### Introduzione

Quando affrontiamo problemi di ottimizzazione non vincolata e non lineare della forma:
	$\min_{x \in \mathbb{R}^n} f(x)$

dove $f : \mathbb{R}^n \to \mathbb{R}$ è una funzione continuamente differenziabile, nella pratica si cerca di trovare soluzioni candidate ottimali che soddisfano la condizione di stazionarietà $\nabla f(x) = 0$. In rari e fortunati casi, gli zeri dei gradienti possono essere trovati analiticamente, risolvendo il problema in forma chiusa.

In generale, tuttavia, non avremo accesso a formule esatte per risolvere il problema. Dobbiamo quindi affidarci ad algoritmi che costruiscono una soluzione attraverso un processo iterativo, cioè metodi che producono una sequenza di soluzioni ${x_k}$ che si avvicinano progressivamente a un punto stazionario. Gli algoritmi di ottimizzazione iterativa sono generalmente caratterizzati da una regola di aggiornamento della forma:
	$\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$

cioè il nuovo punto viene ottenuto partendo dalla soluzione corrente e spostandosi di un vettore di aggiornamento $\mathbf{s}_k$. L'algoritmo si arresta non appena la condizione di stazionarietà viene soddisfatta in una delle iterazioni $\mathbf{x}_k$. Esistono diverse classi di algoritmi, ma le tre più rilevanti sono le seguenti (vedi Figura 3):
![[Pasted image 20250113220602.png]]
1. **Algoritmi basati sulla ricerca in direzione**: il vettore di aggiornamento è strutturato come $\mathbf{s}_k = \alpha_k \mathbf{d}_k$, dove $\mathbf{d}_k \in \mathbb{R}^n$ è una direzione nello spazio euclideo e $\alpha_k \in \mathbb{R}^+$ è uno scalare denominato passo (stepsize). In questi algoritmi, viene prima identificata una direzione di ricerca $\mathbf{d}_k$, e successivamente scelto un passo appropriato per stabilire la grandezza dello spostamento lungo quella direzione.
    
2. **Algoritmi basati sulla regione di fiducia**: il vettore di aggiornamento è definito come il miglior aggiornamento possibile per un'approssimazione (modello) della funzione obiettivo in una vicinanza della soluzione corrente:
		
		$\mathbf{s}_k \in \arg\min_{x \in \Delta_k} m_k(x), \quad m_k(x) \approx f(x) \; \forall x \in \Delta_k, \; m_k(\mathbf{x}_k) = f(\mathbf{x}_k).$

	L'accettazione dell'aggiornamento e la variazione del raggio $\rho_k$ della regione di fiducia $\Delta_k$ dipendono dal miglioramento della funzione obiettivo reale:

	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) \ll 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$, e $\rho_{k+1} > \rho_k$.
	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) < 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$, e $\rho_{k+1} = \rho_k$.
	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) \geq 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k$, e $\rho_{k+1} < \rho_k$.

3. **Algoritmi di ricerca per schemi (pattern search)**: il vettore di aggiornamento è il migliore tra un insieme predefinito di soluzioni da verificare:

	$\mathbf{s}_k \in \arg\min_{\mathbf{s}_{i,k}, i=1,\dots,N_k} f(\mathbf{x}_k + \mathbf{s}_{i,k})$

I metodi di ricerca per schemi vengono spesso considerati quando non si ha accesso alle derivate della funzione obiettivo. In questi casi, si parla di metodi senza derivata (o di ordine zero). Al contrario, i metodi di ricerca in direzione e quelli basati sulla regione di fiducia utilizzano solitamente informazioni di primo ordine (gradienti, $\nabla f$) e secondo ordine (hessiane, $\nabla^2 f$), e in questa prospettiva si parla rispettivamente di metodi di primo ordine e di secondo ordine.
Entreremo successivamente nei dettagli dei metodi basati su line search, nel mentre discuteremo le proprietà che vorremmo che la sequenza $\{x_k\}$ e le sequenze corrispondenti $\{f(x_k)\}$  e $\{\nabla f(x_k)\}$ abbiano, senza guardare il tipo di aggiornamento.
In uno scenario ideale, un algoritmo finisce in un punto stazionari dopo un numero finito di iterazioni, in altre parole per qualche $k^*$ tale che $\nabla f(x^{k^*}) = 0$ e la procedura finisce. Quando un metodo è garantito che si comporta in questo modo, diremo che possiede proprietà di convergenza finita. Sfortunatamente, questa proprietà è ottenuta solo per pochi algoritmi di alcune classi di problemi. Le sequenze in generale sono infinite. Siamo quindi interessati a proprietà di convergenza su sequenze infinite. 

#### 4.1.1 Esistenza di Punti di Accumulazione

La prima proprietà fondamentale che un algoritmo deve garantire è che la sequenza che produce, o almeno una parte di essa, abbia una direzione precisa. In altre parole, **non** vorremmo che la sequenza $\{x_k\}$ divergesse completamente, ovvero che $\|x_k\| \to \infty$. Infatti, siamo interessati a ottenere una soluzione con valori finiti e definiti, da utilizzare in un sistema reale.

Questo requisito si traduce formalmente nella presenza di punti di accumulazione per la sequenza. Ricordiamo che un punto di accumulazione di una sequenza è un punto limite di una sottosequenza, cioè $\bar{x}$ è un punto di accumulazione per $\{x_k\}$ se esiste una sottosequenza $K \subseteq \{0, 1, \dots\}$ tale che $x_k \to \bar{x}$ per $k \in K, \, k \to \infty$.

Garantire l’esistenza di almeno un punto di accumulazione è piuttosto semplice dal punto di vista algoritmico, con ipotesi molto deboli sul problema considerato, come affermato nella seguente proposizione.

**Proposizione 4.1.**  
Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione continua. Sia $x_0 \in \mathbb{R}^n$ e sia il sottoinsieme di livello $L_0 = \{x \in \mathbb{R}^n \, | \, f(x) \leq f(x_0)\}$ compatto. Supponiamo che la sequenza $\{x_k\}$, iniziando da $x_0$, sia tale che, per ogni $k, f(x_{k+1}) \leq f(x_k)$. Allora, la sequenza $\{x_k\}$ ammette punti di accumulazione, ognuno appartenente a $L_0$, e la sequenza $\{f(x_k)\}$ converge a un valore $\bar{f}$.

**Dimostrazione.**  
In base alle ipotesi, $f(x_{k+1}) \leq f(x_k)$ per ogni $k$. Per induzione, abbiamo che $f(x_k) \leq f(x_0)$ per ogni $k = 0, 1, \dots,$ il che implica che l’intera sequenza $\{x_k\}$ è contenuta nel sottoinsieme di livello $L_0$. Dalla compattezza di $L_0$, segue che $\{x_k\}$ ha punti di accumulazione, tutti appartenenti a $L_0$.

Inoltre, la sequenza $\{f(x_k)\}$ è monotona decrescente e quindi ammette un limite $\bar{f}$. Grazie alla limitatezza di $\{x_k\} \subseteq L_0$ e alla continuità di $f$, il valore di $\bar{f}$ è finito.

La condizione di compattezza sul sottoinsieme di livello iniziale è soddisfatta, ad esempio, se la funzione obiettivo è coerciva. D’altra parte, imporre la monotonicità della sequenza dei valori della funzione obiettivo è relativamente semplice dal punto di vista algoritmico: ci concentreremo su questo aspetto nelle sezioni successive.

Un risultato interessante della proposizione è che la sequenza dei valori di $f$ converge completamente; di conseguenza, abbiamo $f(\bar{x}) = \bar{f}$ ​ per qualsiasi punto di accumulazione $\bar{x}$ (cioè, tutti i punti di accumulazione sono equivalenti in termini di valore della funzione obiettivo). In realtà, questa proprietà si verifica immediatamente ogni volta che garantiamo un comportamento monotono con una funzione limitata inferiormente.

Tuttavia, mentre l’esistenza di punti di accumulazione è un requisito minimo essenziale, non abbiamo garanzie che uno qualsiasi di questi punti sia effettivamente significativo per il problema che stiamo cercando di risolvere. Questo è l’aspetto su cui ci concentreremo nella prossima sezione.
#### 4.1.2 Convergenza verso la stazionarietà

Ragionevolmente, vorremmo che le (sotto)sequenze convergenti discusse nella sezione precedente raggiungano asintoticamente la condizione di stazionarietà. Sebbene questo aspetto sia concettualmente semplice, la sua caratterizzazione formale richiede attenzione. In particolare, la proprietà di stazionarietà può essere raggiunta in modi diversi, elencati e descritti di seguito in ordine decrescente di forza:

1. $\lim_{k \to \infty} x_k = \bar{x}$  con $\nabla f(\bar{x}) = 0$: l'intera sequenza converge a un punto limite che è un punto stazionario.
2. $\lim_{k \to \infty} \|\nabla f(x_k)\| = 0$ : l'**intera** sequenza dei gradienti tende a zero; per continuità della norma e di $\nabla f$, tutti i punti di accumulazione della sequenza $\{x_k\}$ sono punti stazionari.
3. $\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$ : i gradienti tendono a zero almeno **lungo una sottosequenza**; se $\{x_k\}$ non ha sottosequenze divergenti, **almeno un punto di accumulazione è stazionario**.

Il significato di queste tre situazioni può essere meglio compreso attraverso il seguente esempio.

**Esempio 4.1.**  
Consideriamo la funzione di una variabile $f(x)$ con derivata (gradiente) data da:
$\nabla f(x) = (x - 1)(x - 2)$

1. **Caso 1:** La sequenza dei valori
	    $\{x_k\} = \{0.9, 0.99, 0.999, 0.9999, 0.99999, \dots\}$
    
    converge all’unico limite $\bar{x} = 1$, che è un punto stazionario per $f$.
    
2. **Caso 2:** La sequenza dei valori
	    $\{x_k\} = \{0.9, 2.1, 0.99, 2.01, 0.999, 2.001, 0.9999, 2.0001, 0.99999, 2.00001, \dots\}$
    
    corrisponde alla sequenza dei gradienti:
	    $\{\nabla f(x_k)\} = \{0.11, 0.11, 0.0101, 0.0101, 0.001001,$
	     $0.001001, 0.00010001, 0.00010001, 0.0000100001, 0.0000100001, \dots\}$
    
    che chiaramente converge a zero. I due punti di accumulazione di $\{x_k\}$, 1 e 2, sono entrambi punti stazionari.
    
3. **Caso 3:** La sequenza dei valori
    
    $\{x_k\} = \{0.9, 3.1, 0.99, 3.01, 0.999, 3.001, 0.9999, 3.0001, 0.99999, 3.00001, \dots\}$
    
	che corrisponde alla sequenza dei gradienti: $\{\nabla f(x_k)\} = \{0.11, 2.31, 0.0101, 2.0301, 0.001001,$
	$2.003001, 0.00010001, 2.00030001, 0.0000100001, 2.0000300001, \dots\}$

In questo caso, la sequenza $\{|\nabla f(x_k)|\}$ presenta due sottosequenze convergenti: una con limite 0 e l'altra con limite 2. Il limite inferiore della norma del gradiente è dunque 0, e esiste una sottosequenza di $\{x_k\}$ (quella che converge a 1) che tende a un punto stazionario.

Nella pratica, garantire la terza condizione $\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$) è sufficiente per scopi computazionali. Infatti, grazie alla continuità del gradiente, sappiamo che se $\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$, allora, per ogni $\epsilon > 0$, esiste un $k$ sufficientemente grande tale che $\|\nabla f(x_k)\| \leq \epsilon$. Questo è importante perché garantisce che, se utilizziamo una condizione di arresto basata su una soglia per la norma del gradiente, l'algoritmo si fermerà certamente in tempo finito, fornendoci una soluzione con il livello di accuratezza desiderato.

Garantire questo tipo di convergenza per la sequenza di soluzioni non è affatto banale; ad esempio, la semplice decrescita della funzione obiettivo non è sufficiente per garantire la convergenza ai punti stazionari, nemmeno nel caso convesso, come dimostra il seguente esempio.

**Esempio 4.2.** Consideriamo il problema:

	$\min_{x \in \mathbb{R}} f(x) = \frac{1}{2}x^2$

dove la funzione obiettivo è continua e strettamente convessa, raggiungendo il valore minimo $f^\star = 0$ nell'unico ottimizzatore globale $x^\star = 0$.

Supponiamo ora di considerare il processo iterativo che parte da $x^0 = 2$ e segue la regola di aggiornamento:
	$x^{k+1} = x^k - \alpha_k f'(x^k) = x^k - \alpha_k x^k$

dove il passo $\alpha_k$ è definito come:
	$\alpha_k = \frac{x^k - 1}{2x^k}$​.

In tal caso, la regola di aggiornamento diventa:
	$x^{k+1} = \frac{x^k + 1}{2}$

Osserviamo che, per ogni $x^k \in (1, 2]$, abbiamo:
	$2 \geq \frac{x^k + 1}{2} \geq \frac{1 + 1}{2} = 1$,

cioè $x^{k+1}$ appartiene all'intervallo $(1, 2]$, e inoltre:
	$x^{k+1} = \frac{x^k + 1}{2} < x^k$,

Ricordando che $x^0 = 2$, per induzione abbiamo che $x^{k+1} < x_k$​ vale per l'intera sequenza $\{x_k\}$.

Pertanto, possiamo osservare che:
	$f(x^{k+1}) = \frac{1}{2}(x^{k+1})^2 < \frac{1}{2}(x^k)^2 = f(x^k)$

Abbiamo così definito una sequenza strettamente decrescente su una funzione fortemente convessa; tuttavia, l'intera sequenza è contenuta nell'intervallo $(1, 2]$ e quindi non può convergere all'unico punto stazionario 0: in realtà, converge a 1.

Concludiamo questa discussione evidenziando un'importante distinzione riguardo il tipo di proprietà di convergenza che possono essere associate a un algoritmo:

- **Convergenza Globale:** Si dice che le proprietà di convergenza di un algoritmo siano **globali** se valgono indipendentemente dalla soluzione iniziale scelta per il processo iterativo.
- **Convergenza Locale:** Si dice che le proprietà di convergenza siano **locali** se valgono solo quando il punto di partenza è sufficientemente vicino a una delle soluzioni desiderate.

Le proprietà di convergenza di tipo globale sono ovviamente preferibili. Questo è particolarmente vero poiché, nella pratica, non sappiamo quanto grande sia il "vicinato di convergenza" né dove si trovi, quando le proprietà di convergenza sono solo locali. Tuttavia, i risultati di convergenza locale sono talvolta di interesse, poiché possono essere dimostrate proprietà migliori per certi metodi quando si trovano **vicini** a una soluzione.

#### 4.1.3 Efficienza dei Solver di Ottimizzazione

Nello studio degli algoritmi di ottimizzazione, l'interesse principale risiede nell'analisi delle proprietà di convergenza locale e globale verso i punti stazionari: è fondamentale garantire che producano effettivamente soluzioni candidate ottimali. Tuttavia, anche l'efficienza degli algoritmi è cruciale, specialmente nei contesti su larga scala, dove i tempi di calcolo possono essere molto lunghi.

L'efficienza degli algoritmi di ottimizzazione è solitamente studiata in termini di due concetti principali: **tasso di convergenza** e **complessità**.
##### Tasso di convergenza

Il **tasso di convergenza** indica intuitivamente con quale rapidità la sequenza dei valori della funzione obiettivo $\{f(x_k)\}$ (o, equivalentemente, la sequenza degli iterati $\{x_k\}$ o dei gradienti $\{\|\nabla f(x_k)\|\}$ si avvicina al punto limite. Formalmente, possiamo distinguere i seguenti casi:

**Definizione 4.1.** Sia $\{f(x_k)\}$ la sequenza di valori obiettivo generata da un algoritmo iterativo, con $f(x_k) \to f^\star$. Allora, il tasso di convergenza è:

- **Sublineare** se:

	$\lim_{k \to \infty} \frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star} = 1$

- **Lineare** se, per un $\rho \in (0, 1)$:
	$\lim_{k \to \infty} \frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star} = \rho$

- **Superlineare** se:

	$\lim_{k \to \infty} \frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star} = 0$.

Per comprendere meglio queste definizioni, consideriamo il rapporto che viene calcolato nel limite:

	$\frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star}$

- Al numeratore, abbiamo il divario residuo da colmare per raggiungere il valore limite **dopo** l'aggiornamento all'iterazione k.
- Al denominatore, abbiamo il divario all'**inizio** dell'iterazione.
- Il rapporto indica quindi quanto è piccolo il ==divario residuo dopo l'iterazione rispetto a quello iniziale.==

Il tasso di convergenza misura come si comporta questo rapporto nel limite.

Andando a interpretare i casi:
- **Sublineare:** Un tasso di convergenza sublineare è inefficiente: più l'algoritmo procede, meno progresso viene fatto (la riduzione del divario diventa progressivamente irrilevante).
- **Lineare:** Un tasso lineare è accettabile: a ogni iterazione, viene coperta una percentuale fissa della distanza residua dal valore finale.
- **Superlineare:** Un tasso di convergenza superlineare è eccellente: per k grande, una singola iterazione è sufficiente per ridurre l'errore di ordini di grandezza.
##### Complessità

Un altro approccio molto popolare per misurare l'efficienza degli algoritmi di ottimizzazione si basa sulla **complessità**. Tuttavia, anche se gli algoritmi hanno tassi di convergenza asintotici eccellenti, la loro complessità computazionale deve essere considerata per valutarne l'**efficacia** nei contesti pratici.
Quante iterazioni (e possibilmente quante valutazioni della funzione e del gradiente) sono necessarie per raggiungere un determinato livello di accuratezza $\epsilon$?

Partiamo prima dalla definizione di **Notazione O**
**Definizione 4.2.** Date due funzioni $\phi$ e $g$, diciamo che $\phi(n) = O(g(n))$ se esistono una costante c > 0 e un indice $\bar{n}$ tali che:
	$\phi(n) \leq c \, g(n), \quad \forall n \geq n̄$

Focalizzandoci sul numero di iterazioni come metrica di costo, possiamo definire quanto segue.

**Definizione 4.3.** Sia $\{x^k\}$ la sequenza generata da un metodo iterativo, con $f(x^k) \to f^\star$ Diciamo che l'algoritmo ha un **errore di iterazione** di $O(h(k))$ se:

	$f(x^k) - f^\star = O(h(k))$

equivalentemente, dato un livello di accuratezza $\epsilon$, l'algoritmo ha una **complessità di iterazione** di $O(q(\epsilon))$ se:

	$\min \{k \, | \, f(x^k) - f^\star \leq \epsilon\} = O(q(\epsilon))$

Invece di considerare il divario $f(x^k) - f^\star$, possiamo utilizzare la quantità $\|\nabla f(x^k)\|$, cioè la **distanza dalla stazionarietà**. Questa scelta è particolarmente utile per analizzare algoritmi in contesti non convessi, dove il gradiente viene spesso utilizzato come criterio di arresto.

Il caso peggiore sull'errore di iterazione ci fornisce una misura della dimensione dell'**errore** che possiamo aspettarci dopo ==un dato numero di iterazioni.== D'altro canto, il bound sulla complessità di iterazione ci offre **una stima del tempo necessario** affinché l'algoritmo produca ==una soluzione accettabile== nel caso peggiore.

Esiste una corrispondenza fra errore di iterazione e complessità d'iterazione: se un algoritmo ha un **errore di iterazione** $O(\frac{1}{k})$ e vogliamo ottenere una soluzione accurata entro $\epsilon$, cioè $f(x_k) - f^\star \leq \epsilon$, nel caso peggiore abbiamo:

	$f(x_k) - f^\star \leq \frac{C}{k}$.

Quindi, $\frac{C}{k} \leq \epsilon$, garantiamo che la soluzione è accettabile per ogni $k \geq \frac{C}{\epsilon}$. Concludiamo che il primo $k$ tale che $f(x_k) - f^\star \leq \epsilon$ è $O(\frac{1}{\epsilon})$, cioè la **complessità di iterazione** è:	$O\left(\frac{1}{\epsilon}\right)$.

In modo analogo, se l'errore di iterazione è $O(\frac{1}{k^2})$, la complessità di iterazione diventa $O\left(\frac{1}{\sqrt{\epsilon}}\right)$.

Nota che una complessità $O\left(\frac{1}{\epsilon}\right)$ non è favorevole. Consideriamo il significato pratico:

- Possiamo interpretare $\log\left(\frac{1}{\epsilon}\right)$ come il **numero di cifre decimali di accuratezza desiderate**.
- Con una complessità $O\left(\frac{1}{\epsilon}\right)$, se servono 10 iterazioni per una cifra di accuratezza, potrebbero essere necessarie:
    - 100 iterazioni per 2 cifre,
    - 1000 iterazioni per 3 cifre,
    - e così via (il costo aumenta esponenzialmente).

Questo può essere messo in relazione con la velocità di convergenza:
- Per una complessità di iterazione di $O(\frac{1}{\epsilon})$ corrisponde un **Errore di Iterazione** $O(\frac{1}{k})$ che equivale a un tasso di convergenza **sublineare**, come mostrato:

	$\lim_{k \to \infty} \frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star} = \lim_{k \to \infty} O ( \frac{k}{k+1}) = 1$.

- **Errore di Iterazione** $O(\rho^k)$ con $\rho < 1$: Questo porta a un **tasso di convergenza lineare** e una complessità di iterazione di $O(\log\left(\frac{1}{\epsilon}\right))$. In questo caso, il costo per aggiungere una nuova cifra di accuratezza cresce in modo **polinomiale**, risultando molto più favorevole rispetto al caso sublineare.

- Un errore del tipo $O(\rho^2)$, con $\rho < 1,$ porta a un tasso di convergenza **superlineare** e a una complessità di iterazione di $O(\log(\log(\frac{1}{\epsilon})))$. In questo caso, il costo per aggiungere una nuova cifra di accuratezza è **costante**, il che rappresenta una proprietà altamente desiderabile.

**Tabella 1: Esempi di Tipi di Complessità**

| **ϵ**      | $O(\frac{1}{\epsilon^2})$ | $O(\frac{1}{\epsilon})$ | $O(\frac{1}{\epsilon^{1/2}})$ | $O(\log(\frac{1}{\epsilon}))$ | $O(\log(\log(\frac{1}{\epsilon})))$ |
| ---------- | ------------------------- | ----------------------- | ----------------------------- | ----------------------------- | ----------------------------------- |
| 1          | 1                         | 1                       | 1                             | 0                             | −-                                  |
| 0.1        | 100                       | 10                      | $\sqrt{10}$                   | 1                             | 0                                   |
| 0.01       | $10^4$                    | 100                     | 10                            | 2                             | $\log(2)$                           |
| $10^{-3}$  | $10^6$                    | 1000                    | $\sqrt{10^{3}}$               | 3                             | $\log(3)$                           |
| $10^{-10}$ | $10^{20}$                 | $10^{10}$               | $10^5$                        | 10                            | 1                                   |

**Tabella 2: Esempi di Tipi di Errore Iterativo**

| **k** | $O(\frac{1}{\sqrt{k}})$ | $O(\frac{1}{k})$ | $$O(\frac{1}{k^2})$ | $O((\frac{1}{2})^k)$ | $O((\frac{1}{2})^{2^k})$ |
| ----- | ----------------------- | ---------------- | ------------------- | -------------------- | ------------------------ |
| 1     | 1                       | 1                | 1                   | 0.5                  | 0.25                     |
| 2     | 0.7                     | 0.5              | 0.25                | 0.25                 | 0.06                     |
| 3     | 0.57                    | 0.33             | 0.11                | 0.12                 | 0.004                    |
| 4     | 0.5                     | 0.25             | 0.06                | 0.06                 | $10^{-5}$                |
| 10    | 0.31                    | 0.1              | 0.01                | $10^{-3}$            | $10^{-308}$              |
| 100   | 0.1                     | 0.01             | $10^{-4}$           | $10^{-5}$            | 0                        |
| 1000  | 0.03                    | $10^{-3}$        | $10^{-6}$           | $10^{-300}$          | 0                        |

### 4.2 Metodi di Discesa Basati su Line Search

#### Introduzione

La classe principale di algoritmi di interesse è quella dei metodi basati su **line search**. Gli aggiornamenti negli approcci iterativi di questa famiglia sono della forma:

	$x^{k+1} = x^k + \alpha_k d_k$,

dove:

- $d_k$ è una **direzione di ricerca** (in particolare, una **direzione di discesa** che soddisfa $\nabla f(x_k)^T d_k < 0$),
- $\alpha_k$ è uno scalare positivo, detto **passo** (_stepsize_).

Per algoritmi di questo tipo, è fondamentale scegliere con attenzione sia la direzione $d_k$ che il passo $\alpha_k$ per garantire le proprietà di convergenza.

Consideriamo ancora l'Esempio 4.2. In quel caso specifico, la sequenza $\{x^k\}$ è definita secondo una regola della forma: $x^{k+1} = x^k - \alpha_k \nabla f(x_k)$, dove la direzione di ricerca, $-\nabla f(x^k)$, è l'unica direzione di discesa in $x^k$. Il fallimento della convergenza è quindi attribuibile a una scelta errata del passo $\alpha_k$.

Vediamo ora un esempio in cui i problemi di convergenza sono chiaramente legati alla scelta della direzione.

**Esempio 4.3.** Consideriamo il seguente problema di ottimizzazione:

$\min f(x, y, z) = \frac{1}{2}x^2 + \frac{1}{2}y^2 - xy + \frac{1}{2}z^2$

partendo dal punto iniziale (x0,y0,z0)=(1,1,1). Supponiamo che le direzioni di ricerca $d_k$ siano definite come segue:

$d_k = \begin{cases} (-\nabla_x f(x_k, y_k, z_k), 0, 0)^T = (-x_k + \frac{1}{2}y_k, 0, 0)^T & \text{se } k \text{ è pari}, \\ (0, -\nabla_y f(x_k, y_k, z_k), 0)^T = (0, -y_k + \frac{1}{2}x_k, 0)^T & \text{se } k \text{ è dispari}. \end{cases}$

A ogni iterazione, si ottiene uno dei seguenti aggiornamenti:

- Per iterazioni pari:

	$\begin{pmatrix} x_{k+1} \\ y_{k+1} \\ z_{k+1} \end{pmatrix} = \begin{pmatrix} x_k - \alpha_k x_k + \frac{1}{2}\alpha_k y_k \\ y_k \\ z_k \end{pmatrix}$

- Per iterazioni dispari:
	$\begin{pmatrix} x_{k+1} \\ y_{k+1} \\ z_{k+1} \end{pmatrix} = \begin{pmatrix} x_k \\ y_k - \alpha_k y_k + \frac{1}{2}\alpha_k x_k \\ z_k \end{pmatrix}$


Supponiamo che, a ogni iterazione, il passo $\alpha_k$ sia scelto come $\alpha_k = 1$. Mostriamo che questa è la scelta ottimale per ogni iterazione.
Per esempio, in un'iterazione pari, consideriamo **l'obiettivo come funzione del passo:**
	$\phi(\alpha) = f(x_k - \alpha x_k + \alpha \frac{1}{2}y_k, y_k, z_k) =$ $\frac{1}{2}(x_k - \alpha x_k + \alpha \frac{1}{2}y_k)^2 + \frac{1}{2}y_k^2 - y_k(x_k - \alpha x_k + \alpha \frac{1}{2}y_k) + \frac{1}{2}z_k^2$

che è una funzione **convessa** (infatti il coefficiente al quadrato è non negativo). Per minimizzare $\phi(\alpha)$, calcoliamo la derivata prima e la poniamo uguale a zero:

	$\phi'(\alpha) = \left(-x_k + \frac{1}{2}y_k\right)\left(x_k - \alpha x_k + \alpha \frac{1}{2}y_k\right) - y_k\left(-x_k + \frac{1}{2}y_k\right) = 0$

Risolvendo, otteniamo $\alpha = 1$ Un'analisi analoga vale per le iterazioni dispari.

Con $\alpha_k = 1$, le regole di aggiornamento diventano:

- Iterazioni pari:

	$\begin{pmatrix} x_{k+1} \\ y_{k+1} \\ z_{k+1} \end{pmatrix} = \begin{pmatrix} \frac{1}{2}y_k \\ y_k \\ z_k \end{pmatrix}$

- Iterazioni dispari:

	$\begin{pmatrix} x_{k+1} \\ y_{k+1} \\ z_{k+1} \end{pmatrix} = \begin{pmatrix} x_k \\ \frac{1}{2}x_k \\ z_k \end{pmatrix}$

Per le iterazioni pari, la direzione $d_k$ è sicuramente una direzione di discesa se $x_k \neq \frac{1}{2}y_k$:

	$\nabla f(x_k, y_k, z_k)^T d_k = \begin{pmatrix} x_k - \frac{1}{2}y_k, y_k - x_k, 2z_k \end{pmatrix} \cdot \begin{pmatrix} -x_k + \frac{1}{2}y_k \\ 0 \\ 0 \end{pmatrix} = - (x_k - \frac{1}{2}y_k)^2 < 0$

Analogamente, per le iterazioni dispari, $d_k$ è una direzione di discesa se $y_k \neq \frac{1}{2}x_k$

Consideriamo infine la sequenza delle soluzioni prodotte dall'algoritmo:

1. Iterazione iniziale:
    
	    $(x_0, y_0, z_0) = (1, 1, 1)$
1. Iterazione dispari:
    
	    $(x_1, y_1, z_1) = (\frac{y_0}{2}, y_0, z_0) = \left(\frac{1}{2}, 1, 1\right)$
1. Iterazione pari:
    
	    $(x_2, y_2, z_2) = (x_1, \frac{x_1}{2}, z_1) = \left(\frac{1}{2}, \frac{1}{4}, 1\right)$
1. Iterazione dispari:
    
	    $(x_3, y_3, z_3) = (\frac{y_2}{2}, y_2, z_2)= \left(\frac{1}{8}, \frac{1}{4}, 1\right)$
1. Iterazione pari:
    
	    $(x_4, y_4, z_4) = (x_3, \frac{x_3}{2}, z_2)= \left(\frac{1}{8}, \frac{1}{16}, 1\right)$
	    
e così via. La sequenza converge lentamente verso (0, 0, 1).

La sequenza è costruita utilizzando una direzione di discesa e il miglior passo possibile a ogni iterazione, ed è chiaro che converge a (0, 0, 1). Tuttavia, il punto limite **non è un punto stazionario** per il problema, poiché: $\nabla f(0, 0, 1) = (0, 0, 2) \neq 0$

Questo esempio evidenzia che è fondamentale progettare con attenzione le regole di aggiornamento della forma: $x_{k+1} = x_k + \alpha_k d_k$, per i metodi di discesa. Nelle sezioni successive discuteremo questo problema in dettaglio.

#### 4.2.1 Line Search

Data una direzione di discesa $d_k$, ovvero una direzione che soddisfa:	$\nabla f(x_k)^T d_k < 0$

il nostro obiettivo è trovare un **passo** $\alpha_k$ lungo questa direzione da utilizzare nella regola di aggiornamento: $x_{k+1} = x_k + \alpha_k d_k$, in modo tale che la funzione obiettivo decresca in modo appropriato.

##### Line search esatta

Un'idea potrebbe essere quella di scegliere il **miglior passo possibile** lungo la direzione, cioè quello che ==porta al minimo valore== di f (sempre lungo la direzione scelta). In questo caso, stiamo eseguendo una **line search esatta** lungo $d_k$, formalmente caratterizzata come segue:

	$\alpha_k \in \arg\min_{\alpha > 0} \phi(\alpha) = f(x_k + \alpha d_k)$

dove la funzione $\phi$ della variabile scalare $\alpha$ descrive l'evoluzione della funzione obiettivo lungo la direzione di ricerca. Questa operazione è stata eseguita, ad esempio, nell'Esempio 4.3 ed è rappresentata nella Figura 4a.

![[Pasted image 20250116184353.png]]

Questa strategia è **generalmente** fattibile per problemi di ottimizzazione quadratica strettamente convessi della forma: $\min_x f(x) = \frac{1}{2}x^T Qx + c^T x, \quad Q \succ 0$.

Utilizzando lo sviluppo di Taylor di secondo ordine per $f(x_k + \alpha d_k)$ (che è esatto per funzioni quadratiche) e ricordando che $\nabla^2 f(x_k) = Q$, otteniamo:

	$\phi(\alpha) = f(x_k + \alpha d_k) = f(x_k) + \alpha \nabla f(x_k)^T d_k + \frac{\alpha^2}{2} d_k^T Q d_k$.

Questa è una parabola convessa (il coefficiente quadratico $d_k^T Q d_k$ è positivo grazie alla definitezza positiva di Q). 

Il passo ottimale può essere calcolato annullando la derivata prima:

	$0 = \phi'(\alpha) = \nabla f(x_k)^T d_k + \alpha d_k^T Q d_k$

che si risolve con: $\alpha_k = -\frac{\nabla f(x_k)^T d_k}{d_k^T Q d_k}$.

Tuttavia, eccetto per casi molto particolari come questo, le line search esatte devono essere evitate per due motivi principali:

1. **Costo computazionale:** Per una funzione generica f, il minimizzatore di $\phi(\alpha)$ potrebbe non essere disponibile in forma chiusa, e trovarlo potrebbe richiedere l'uso di un risolutore, con un costo computazionale non trascurabile. Inoltre, la direzione $d_k$ potrebbe non essere sufficientemente buona da giustificare un'esplorazione così precisa.
    
2. **Caso non convesso:** Nel caso non convesso, non possiamo nemmeno verificare se un passo sia globalmente ottimale per la direzione di ricerca.
    
##### Line Search Approssimata

Queste considerazioni motivano l'interesse per le tecniche di **line search approssimate**. Questa classe di metodi per la selezione del passo si pone l'obiettivo di identificare un valore $\alpha_k$ che garantisca una ==diminuzione della funzione obiettivo==, ovvero un decremento significativo rispetto allo stato attuale della soluzione: $f(x_k + \alpha_k d_k) < f(x_k)$

La condizione di decremento sufficiente più utilizzata è la **Condizione di Armijo**, che richiede:

	$f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, \space \text{con} \space \gamma \in (0, 1)$

In pratica, questa condizione chiede di selezionare un passo $\alpha_k$ in modo che la funzione obiettivo decresca almeno quanto un modello lineare con una pendenza più "dolce" rispetto al modello tangente (vedi Figura 4b).

Analizzando i termini:
- Il termine a sinistra $\phi(\alpha)$ rappresenta ==la funzione obiettivo lungo la direzione di ricerca== $d_k$.
- Il termine $f(x_k) = \phi(0)$ è il valore corrente della funzione obiettivo.
- Il termine $\nabla f(x_k)^T d_k$, se guardiamo bene è la derivata di $\phi(\alpha)$, per $\alpha = 0$, per la regola della catena abbiamo $\phi'(\alpha) = \nabla f(x_k + \alpha d_k)^T d_k, \phi'(0) = \nabla f(x_k)^Td_k$  

Dunque, per $\gamma = 1$, la parte destra rappresenta la retta tangente al grafico di $\phi(\alpha)$ in $\alpha = 0$ Più in generale possiamo scrivere la condizione come: $\phi(\alpha) \leq \phi(0) + \gamma \phi'(0)\alpha$, che per direzioni di discesa, la condizione rappresenta una linea con un trend iniziale di discesa.

Per valori di $\gamma \in (0, 1)$, otteniamo rette che passano per $(0, \phi(0))$ con una pendenza più dolce rispetto alla tangente. Quindi la condizione di Armijo ci chiede di trovare un passo tale che la funzione $\phi(\alpha)$ si trovi sotto la linea risultante (vedi figura 4b)

###### Ricerca del Passo mediante Backtracking

Per identificare **operativamente** un passo che soddisfi la condizione di decremento sufficiente, utilizziamo un algoritmo basato sul concetto di **backtracking**. 

L'idea è intuitiva:
1. Si assume un valore iniziale per il passo $\alpha_k$.
2. Si verifica se questo valore soddisfa la Condizione di Armijo: 
	 $f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k$.
3. Se la condizione è soddisfatta, il passo viene accettato.
4. Altrimenti, si riduce il valore del passo moltiplicandolo per un fattore $\delta \in (0, 1)$ (passo di backtrack) e si ripete il controllo.

Andiamo a vedere quindi l'algoritmo:

**Input:**
- $x_k \in \mathbb{R}^n, d_k \in \mathbb{R}^n \space \text{tc} \space \nabla f(x_k)^T d_k < 0$,
- $\Delta_0 > 0, \gamma \in (0, 1), \delta \in (0, 1)$.

**Procedura:**
1. Imposta $\alpha = \Delta_0$.
2. **While** $f(x_k + \alpha d_k) > f(x_k) + \gamma \alpha \nabla f(x_k)^T d_k$:
    - Aggiorna $\alpha = \delta \alpha$.
3. Imposta $\alpha_k = \alpha$.
4. **Restituisci** $\alpha_k$.

Algoritmo riassumibile dalla seguente formula: 
	$\alpha_k = max_{j=0,1,...} \{\delta^j\Delta_0 \space | \space \phi(\delta^j\Delta_0) \leq \phi(0) + \gamma \delta^j\Delta_0\phi'(0)\}$ con $\delta \in (0,1)$ e $\Delta_0 > 0$ 

Algoritmo che gode di alcune proprietà teoriche:

**Proposizione 4.2.**  
Sia $f: \mathbb{R}^n \to \mathbb{R}$ una funzione continuamente differenziabile. Siano $x_k \in \mathbb{R}^n, d_k \in \mathbb{R}^n \space \text{con} \space \nabla f(x_k)^T d_k < 0,\gamma \in (0, 1), \delta \in (0, 1), \Delta_0 > 0$. Allora, l'algoritmo **Armijo Line Search** termina in ==un numero finito di iterazioni==, fornendo un passo $\alpha_k$ che soddisfa la condizione di Armijo. Inoltre, valgono le seguenti proprietà:

-  $\alpha_k = \Delta_0$, se il primo tentativo soddisfa la condizione di Armijo;  
-  $\alpha_k \leq \delta \Delta_0$ e $f(x^k + \frac{\alpha_k}{\delta}d_k) > f(x^k + \gamma \frac{\alpha_k}{\delta}\nabla f(x^k)^Td_k$ 

Assumiamo per assurdo che l'algoritmo non termini mai, cioè che la condizione di arresto non venga mai soddisfatta per alcun passo $\delta^j \Delta_0$, con j=0,1,…
Questo implica che: $f(x_k + \delta^j \Delta_0 d_k) > f(x_k) + \gamma \delta^j \Delta_0 \nabla f(x_k)^T d_k$.

Dividendo entrambi i membri per $\delta^j \Delta_0$, otteniamo:

	$\frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} > \gamma \nabla f(x_k)^T d_k$.

Poiché $\delta \in (0, 1)$, quando $j \to \infty$ (al limite), abbiamo $\delta^j \Delta_0 \to 0$, e il termine a sinistra tende alla derivata direzionale di $f$ lungo $d_k$:

	$\lim_{j \to \infty} \frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} = \nabla f(x_k)^T d_k$

Otteniamo quindi:

	$\nabla f(x_k)^T d_k \geq \gamma \nabla f(x_k)^T d_k, => (1-\gamma)\nabla f(x^k)^Td_k \geq 0$ 
 
Poiché $(1 - \gamma)$ è positivo e $\nabla f(x_k)^T d_k < 0$ per ipotesi, questa relazione è contraddittoria. Quindi, l'algoritmo deve terminare in un numero finito di iterazioni.

La seconda proprietà deriva direttamente dalla struttura dell'algoritmo: se il passo iniziale $\Delta_0$ non è accettabile, almeno un backtracking viene eseguito, e il passo accettato $\alpha_k$ sarà il primo che soddisfa la condizione, mentre il secondo ultimo step tentato sarà $\frac{\alpha_k}{\delta}$ che non soddisfa la condizione di Armijo.

La logica della prima proprietà è che, riducendo ripetutamente il passo della stessa frazione, nel caso peggiore ad un certo punto arriveremo nell'intervallo iniziale dello stepsize che soddisfa la condizione, cosicchè la linesearch si ferma in tempo finito.
La seconda proprietà ci dice banalmente che, se non accettiamo il primo passo, otteniamo un passo riducendo il passo più grande che non soddisfa la condizione di Armijo.

#### 4.2.2 Direzioni gradient related

Come abbiamo visto nell'Esempio 4.3, e forse contrariamente all'intuizione, scegliere una direzione di discesa a ogni iterazione non è sufficiente per garantire la convergenza verso un punto stazionario. Nell'esempio, si osserva che il punto limite non stazionario viene avvicinato asintoticamente utilizzando direzioni che diventano sempre meno di discesa, tendendo a essere ortogonali al gradiente del punto limite.

Per evitare questo tipo di comportamento, richiediamo che la direzione di ricerca sia in qualche modo legata al vettore gradiente. Formalizziamo questa idea con la seguente definizione.

---
 **Definizione 4.4: Direzioni Correlate al Gradiente**

Sia {xk,dk}\{x_k, d_k\} la sequenza generata da un algoritmo iterativo della forma:

xk+1=xk+αkdk.x_{k+1} = x_k + \alpha_k d_k.

Diciamo che la sequenza {dk}\{d_k\} delle direzioni è correlata al gradiente rispetto a {xk}\{x_k\} se esistono due costanti c1,c2>0c_1, c_2 > 0 tali che, per ogni k=0,1,…k = 0, 1, \dots, valgano le seguenti condizioni:

1. ∥dk∥≤c1∥∇f(xk)∥\|d_k\| \leq c_1 \|\nabla f(x_k)\|,
2. ∇f(xk)Tdk≤−c2∥∇f(xk)∥2\nabla f(x_k)^T d_k \leq -c_2 \|\nabla f(x_k)\|^2.

---

 Interpretazione delle Condizioni

- **Prima condizione:** La grandezza della direzione di ricerca può essere molto grande, purché non sia infinitamente maggiore rispetto alla grandezza del gradiente. Inoltre, la direzione deve ridursi a zero quando il gradiente tende a zero.
- **Seconda condizione:** Richiede che la direzione di discesa selezionata abbia una derivata direzionale non trascurabile rispetto alla derivata direzionale lungo il gradiente, e che si riduca a zero solo quando ci si avvicina a un punto stazionario.

---

 Relazione tra Direzione di Ricerca e Gradiente

Denotiamo con θ(v1,v2)\theta(v_1, v_2) l'angolo tra due vettori v1v_1 e v2v_2. Combinando le due condizioni della Definizione 4.4, otteniamo:

cos⁡θ(dk,−∇f(xk))=−∇f(xk)Tdk∥dk∥∥∇f(xk)∥≥c2c1>0.\cos \theta(d_k, -\nabla f(x_k)) = \frac{-\nabla f(x_k)^T d_k}{\|d_k\| \|\nabla f(x_k)\|} \geq \frac{c_2}{c_1} > 0.

Questa relazione garantisce che l'angolo tra la direzione di ricerca e il gradiente negativo rimanga inferiore o uguale a 90∘90^\circ e sia sempre maggiore di zero. In questo modo, evitiamo che le due direzioni diventino asintoticamente ortogonali, come osservato nell'Esempio 4.3.

---

 Classi di Direzioni di Ricerca Correlate al Gradiente

Un esempio ovvio di direzione correlata al gradiente è il gradiente negativo stesso, −∇f(xk)-\nabla f(x_k), che soddisfa le due condizioni con c1=c2=1c_1 = c_2 = 1.

Un'altra classe di direzioni correlate al gradiente è data da:

dk=−Hk∇f(xk),d_k = -H_k \nabla f(x_k),

dove HkH_k è una matrice simmetrica con opportune proprietà. In particolare, dkd_k è certamente una direzione di discesa se HkH_k è definita positiva, poiché:

∇f(xk)Tdk=−∇f(xk)THk∇f(xk)<0.\nabla f(x_k)^T d_k = -\nabla f(x_k)^T H_k \nabla f(x_k) < 0.

---

 Proprietà degli Autovalori della Matrice HkH_k

Tuttavia, la sola definitezza positiva di HkH_k non è sufficiente a garantire la correlazione al gradiente. La proprietà può essere assicurata se imponiamo che la sequenza {Hk}\{H_k\} soddisfi la condizione di autovalori limitati, cioè esistano costanti c1,c2c_1, c_2 con 0<c2<c1<∞0 < c_2 < c_1 < \infty tali che, per ogni k=0,1,…k = 0, 1, \dots:

c2≤λmin(Hk)≤λmax(Hk)≤c1.c_2 \leq \lambda_{\text{min}}(H_k) \leq \lambda_{\text{max}}(H_k) \leq c_1.

Sotto questa assunzione, possiamo dimostrare che per ogni kk:

1. ∥dk∥=∥Hk∇f(xk)∥≤λmax(Hk)∥∇f(xk)∥≤c1∥∇f(xk)∥,\|d_k\| = \|H_k \nabla f(x_k)\| \leq \lambda_{\text{max}}(H_k) \|\nabla f(x_k)\| \leq c_1 \|\nabla f(x_k)\|,
2. ∇f(xk)Tdk=−∇f(xk)THk∇f(xk)≤−λmin(Hk)∥∇f(xk)∥2≤−c2∥∇f(xk)∥2.\nabla f(x_k)^T d_k = -\nabla f(x_k)^T H_k \nabla f(x_k) \leq -\lambda_{\text{min}}(H_k) \|\nabla f(x_k)\|^2 \leq -c_2 \|\nabla f(x_k)\|^2.

---

 Conclusione

Questa condizione sarà particolarmente utile nella discussione di alcune classi importanti di algoritmi, dove la correlazione tra direzione e gradiente è fondamentale per garantire proprietà di convergenza e stabilità.


#### 4.2.3 Risultati di Convergenza

In questa sezione forniamo i risultati generali di convergenza per i metodi di discesa basati su **line search**. Cominciamo con il risultato di convergenza globale.

---

#### **Proposizione 4.3: Convergenza Globale**

Sia ff una funzione continuamente differenziabile, e sia {xk,dk}\{x_k, d_k\} la sequenza generata da un algoritmo iterativo della forma:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

supponendo che il passo αk\alpha_k sia ottenuto tramite l'algoritmo di Armijo (Algoritmo 1) per ogni kk, e che la sequenza delle direzioni {dk}\{d_k\} sia correlata al gradiente rispetto a {xk}\{x_k\}. Inoltre, supponiamo che l'insieme di livello:

L0={x∈Rn ∣ f(x)≤f(x0)}L_0 = \{x \in \mathbb{R}^n \, | \, f(x) \leq f(x_0)\}

sia compatto. Allora, la sequenza {xk}\{x_k\} ammette punti di accumulazione, e ogni punto di accumulazione xˉ\bar{x} è un punto stazionario, cioè:

∇f(xˉ)=0.\nabla f(\bar{x}) = 0.

---

#### **Dimostrazione**

Per ogni k=0,1,…k = 0, 1, \dots, poiché la condizione di Armijo è soddisfatta e ricordando la condizione di correlazione al gradiente, abbiamo:

f(xk+1)=f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk≤f(xk)−γc2αk∥∇f(xk)∥2<f(xk).(5)f(x_{k+1}) = f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k \leq f(x_k) - \gamma c_2 \alpha_k \|\nabla f(x_k)\|^2 < f(x_k). \tag{5}

La sequenza {f(xk)}\{f(x_k)\} è quindi monotona decrescente e, grazie alla compattezza di L0L_0 e alla Proposizione 4.1, la sequenza {xk}\{x_k\} ammette punti limite, tutti appartenenti a L0L_0. Inoltre, {f(xk)}\{f(x_k)\} converge a un valore finito f∗f^*, e abbiamo:

lim⁡k→∞(f(xk+1)−f(xk))=0.(6)\lim_{k \to \infty} \left(f(x_{k+1}) - f(x_k)\right) = 0. \tag{6}

Sia xˉ\bar{x} uno di questi punti limite, cioè esiste K⊆{0,1,… }K \subseteq \{0, 1, \dots\} tale che:

lim⁡k∈K, k→∞xk=xˉ.\lim_{k \in K, \, k \to \infty} x_k = \bar{x}.

Supponiamo per assurdo che xˉ\bar{x} non sia un punto stazionario, cioè che ∥∇f(xˉ)∥=ν>0\|\nabla f(\bar{x})\| = \nu > 0. Riscrivendo l'equazione (5), otteniamo:

f(xk+1)−f(xk)≤γαk∇f(xk)Tdk≤0.f(x_{k+1}) - f(x_k) \leq \gamma \alpha_k \nabla f(x_k)^T d_k \leq 0.

Prendendo il limite per k∈K, k→∞k \in K, \, k \to \infty e ricordando (6), abbiamo:

0≤lim⁡k∈K, k→∞γαk∇f(xk)Tdk≤0,0 \leq \lim_{k \in K, \, k \to \infty} \gamma \alpha_k \nabla f(x_k)^T d_k \leq 0,

quindi:

lim⁡k∈K, k→∞αk∇f(xk)Tdk=0.\lim_{k \in K, \, k \to \infty} \alpha_k \nabla f(x_k)^T d_k = 0.

Dalla condizione di correlazione al gradiente, sappiamo che:

∇f(xk)Tdk≤−c2∥∇f(xk)∥2,\nabla f(x_k)^T d_k \leq -c_2 \|\nabla f(x_k)\|^2,

e quindi:

0=lim⁡k∈K, k→∞αk∇f(xk)Tdk≤lim⁡k∈K, k→∞−c2αk∥∇f(xk)∥2.0 = \lim_{k \in K, \, k \to \infty} \alpha_k \nabla f(x_k)^T d_k \leq \lim_{k \in K, \, k \to \infty} -c_2 \alpha_k \|\nabla f(x_k)\|^2.

Questo implica:

lim⁡k∈K, k→∞αk∥∇f(xk)∥2=0.(7)\lim_{k \in K, \, k \to \infty} \alpha_k \|\nabla f(x_k)\|^2 = 0. \tag{7}

---

Grazie alla continuità di ∇f(x)\nabla f(x), abbiamo che, per k∈K, k→∞k \in K, \, k \to \infty, vale:

∥∇f(xk)∥2→∥∇f(xˉ)∥2=ν2>0.\|\nabla f(x_k)\|^2 \to \|\nabla f(\bar{x})\|^2 = \nu^2 > 0.

Pertanto, deve necessariamente valere:

lim⁡k∈K, k→∞αk=0.\lim_{k \in K, \, k \to \infty} \alpha_k = 0.

---

Ora, αk→0\alpha_k \to 0 lungo la sottosequenza KK implica che esiste un kˉ∈Kk̄ \in K tale che:

αk<Δ0,∀k∈K, k≥kˉ.\alpha_k < \Delta_0, \quad \forall k \in K, \, k \geq k̄.

Secondo la Proposizione 4.2, abbiamo:

f(xk+αkdk)>f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) > f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k,

il che contraddice il fatto che la condizione di Armijo sia soddisfatta. Quindi, ∥∇f(xˉ)∥=0\|\nabla f(\bar{x})\| = 0, e xˉ\bar{x} è un punto stazionario. Questo conclude la dimostrazione.
### Continuazione della Dimostrazione della Proposizione 4.3

Riprendendo il discorso dalla relazione derivata dal **teorema del valor medio**, per ogni kk abbiamo:

f(xk+αkδdk)=f(xk)+αkδ∇f(xk+θkαkδdk)Tdk,f\left(x_k + \frac{\alpha_k}{\delta} d_k\right) = f(x_k) + \frac{\alpha_k}{\delta} \nabla f\left(x_k + \theta_k \frac{\alpha_k}{\delta} d_k\right)^T d_k,

con θk∈(0,1)\theta_k \in (0, 1). Combinando questa espressione con l'equazione (7), otteniamo per ogni k∈Kk \in K:

αkδ∇f(xk+θkαkδdk)Tdk>γ∇f(xk)Tdk.\frac{\alpha_k}{\delta} \nabla f\left(x_k + \theta_k \frac{\alpha_k}{\delta} d_k\right)^T d_k > \gamma \nabla f(x_k)^T d_k.

Denotiamo questa relazione con l'etichetta:

αkδ∇f(xk+θkαkδdk)Tdk>γ∇f(xk)Tdk.(8)\frac{\alpha_k}{\delta} \nabla f\left(x_k + \theta_k \frac{\alpha_k}{\delta} d_k\right)^T d_k > \gamma \nabla f(x_k)^T d_k. \tag{8}

---

#### Limiti e Sequenza delle Direzioni

Grazie alla continuità di ∇f(x)\nabla f(x), sappiamo che la sequenza {∇f(xk)}K\{\nabla f(x_k)\}_K converge a ∇f(xˉ)\nabla f(\bar{x}) ed è quindi limitata. Esiste una costante M>0M > 0 tale che:

∥∇f(xk)∥≤M,∀k∈K.\|\nabla f(x_k)\| \leq M, \quad \forall k \in K.

Grazie alla condizione di correlazione al gradiente, segue che:

∥dk∥≤c1∥∇f(xk)∥≤c1M,∀k∈K.\|d_k\| \leq c_1 \|\nabla f(x_k)\| \leq c_1 M, \quad \forall k \in K.

Pertanto, la sequenza {dk}K\{d_k\}_K è limitata e ammette una sottosequenza {dk}K2⊆{dk}K\{d_k\}_{K_2} \subseteq \{d_k\}_K tale che:

lim⁡k∈K2,k→∞dk=dˉ.\lim_{k \in K_2, k \to \infty} d_k = \bar{d}.

---

#### Limiti nell'Equazione (8)

Prendendo i limiti nell'equazione (8) per k∈K2,k→∞k \in K_2, k \to \infty, e ricordando che θk∈(0,1)\theta_k \in (0, 1) e αk→0\alpha_k \to 0, otteniamo:

dˉT∇f(xˉ)≥γdˉT∇f(xˉ),\bar{d}^T \nabla f(\bar{x}) \geq \gamma \bar{d}^T \nabla f(\bar{x}),

che implica:

(1−γ)dˉT∇f(xˉ)≥0,(1 - \gamma) \bar{d}^T \nabla f(\bar{x}) \geq 0,

cioè:

dˉT∇f(xˉ)≥0.\bar{d}^T \nabla f(\bar{x}) \geq 0.

Tuttavia, dalla condizione di correlazione al gradiente e dall'assunzione che xˉ\bar{x} non sia stazionario, sappiamo che:

dˉT∇f(xˉ)=lim⁡k∈K2,k→∞dkT∇f(xk)≤lim⁡k∈K2,k→∞−c2∥∇f(xk)∥2=−ν2<0.\bar{d}^T \nabla f(\bar{x}) = \lim_{k \in K_2, k \to \infty} d_k^T \nabla f(x_k) \leq \lim_{k \in K_2, k \to \infty} -c_2 \|\nabla f(x_k)\|^2 = -\nu^2 < 0.

Questa è una contraddizione, completando la dimostrazione della Proposizione 4.3.

---

### Proposizione 4.4: Intervallo dei Passi Sufficientemente Piccoli

Sia f:Rn→Rf : \mathbb{R}^n \to \mathbb{R} una funzione LL-liscia. Sia {xk}\{x_k\} la sequenza generata da un algoritmo iterativo della forma:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

supponendo che la sequenza delle direzioni di ricerca {dk}\{d_k\} sia correlata al gradiente. Allora, per ogni kk, la condizione di Armijo (4) è soddisfatta per ogni passo α∈[0,Δlow]\alpha \in [0, \Delta_{\text{low}}], con:

Δlow=2c2(1−γ)Lc12.\Delta_{\text{low}} = \frac{2 c_2 (1 - \gamma)}{L c_1^2}.

---

#### Dimostrazione della Proposizione 4.4

Supponiamo che un passo α\alpha non soddisfi la condizione di Armijo, cioè:

f(xk+αdk)>f(xk)+γα∇f(xk)Tdk.f(x_k + \alpha d_k) > f(x_k) + \gamma \alpha \nabla f(x_k)^T d_k.

Dalla LL-liscezza di ff, sappiamo anche che:

f(xk+αdk)≤f(xk)+α∇f(xk)Tdk+Lα22∥dk∥2.f(x_k + \alpha d_k) \leq f(x_k) + \alpha \nabla f(x_k)^T d_k + \frac{L \alpha^2}{2} \|d_k\|^2.

Combinando le due disuguaglianze, otteniamo:

γα∇f(xk)Tdk<α∇f(xk)Tdk+Lα22∥dk∥2.\gamma \alpha \nabla f(x_k)^T d_k < \alpha \nabla f(x_k)^T d_k + \frac{L \alpha^2}{2} \|d_k\|^2.

Riordinando i termini:

(1−γ)α∣∇f(xk)Tdk∣<Lα22∥dk∥2.(1 - \gamma) \alpha |\nabla f(x_k)^T d_k| < \frac{L \alpha^2}{2} \|d_k\|^2.

Dividendo entrambi i membri per α>0\alpha > 0:

(1−γ)∣∇f(xk)Tdk∣<Lα2∥dk∥2.(1 - \gamma) |\nabla f(x_k)^T d_k| < \frac{L \alpha}{2} \|d_k\|^2.

Sfruttando la condizione di correlazione al gradiente, abbiamo:

∣∇f(xk)Tdk∣≥c2∥∇f(xk)∥2,∥dk∥2≤c12∥∇f(xk)∥2.|\nabla f(x_k)^T d_k| \geq c_2 \|\nabla f(x_k)\|^2, \quad \|d_k\|^2 \leq c_1^2 \|\nabla f(x_k)\|^2.

Sostituendo, otteniamo:

(1−γ)c2∥∇f(xk)∥2<Lα2c12∥∇f(xk)∥2.(1 - \gamma) c_2 \|\nabla f(x_k)\|^2 < \frac{L \alpha}{2} c_1^2 \|\nabla f(x_k)\|^2.

Semplificando ∥∇f(xk)∥2\|\nabla f(x_k)\|^2, ricaviamo il limite superiore per α\alpha:

α<2c2(1−γ)Lc12.\alpha < \frac{2 c_2 (1 - \gamma)}{L c_1^2}.

Questo conclude la dimostrazione.
### Completamento della Dimostrazione e Risultati Derivati

#### Proposizione 4.4: Conclusione della Dimostrazione

Abbiamo dimostrato che un passo α\alpha non soddisfa la condizione di Armijo se:

α(1−γ)∇f(xk)Tdk+α2L2∥dk∥2>0.\alpha(1 - \gamma)\nabla f(x_k)^T d_k + \frac{\alpha^2 L}{2} \|d_k\|^2 > 0.

Utilizzando le ipotesi di correlazione al gradiente, possiamo limitare i termini ∇f(xk)Tdk\nabla f(x_k)^T d_k e ∥dk∥\|d_k\| come segue:

∇f(xk)Tdk≤−c2∥∇f(xk)∥2,∥dk∥≤c1∥∇f(xk)∥.\nabla f(x_k)^T d_k \leq -c_2 \|\nabla f(x_k)\|^2, \quad \|d_k\| \leq c_1 \|\nabla f(x_k)\|.

Sostituendo nella disuguaglianza:

−c2α(1−γ)∥∇f(xk)∥2+c12α2L2∥∇f(xk)∥2>0.-c_2 \alpha(1 - \gamma)\|\nabla f(x_k)\|^2 + \frac{c_1^2 \alpha^2 L}{2} \|\nabla f(x_k)\|^2 > 0.

Dividendo entrambi i membri per α∥∇f(xk)∥2\alpha \|\nabla f(x_k)\|^2 e riordinando i termini:

α>2c2(1−γ)c12L=Δlow.\alpha > \frac{2c_2(1 - \gamma)}{c_1^2 L} = \Delta_{\text{low}}.

Questo conclude la dimostrazione della Proposizione 4.4.

---

#### Proposizione 4.5: Numero Massimo di Backtrack

**Enunciato:** Sotto le stesse ipotesi della Proposizione 4.4, supponiamo inoltre che, per ogni kk, il passo αk\alpha_k venga ottenuto utilizzando l'algoritmo di Armijo con un passo iniziale Δ0>0\Delta_0 > 0. Allora, a ogni iterazione kk, il numero di passi di backtracking jkj_k è limitato superiormente da:

jk≤j∗=max⁡(0,log⁡1/δΔ0Δlow),j_k \leq j^* = \max\left(0, \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}}\right),

dove Δlow=2c2(1−γ)Lc12\Delta_{\text{low}} = \frac{2c_2(1 - \gamma)}{L c_1^2}. Inoltre, il passo αk\alpha_k è limitato inferiormente da:

αk≥min⁡{Δ0,δΔlow}.\alpha_k \geq \min\{\Delta_0, \delta \Delta_{\text{low}}\}.

---

#### Dimostrazione della Proposizione 4.5

Sia j∗j^* il più piccolo intero positivo tale che:

δj∗Δ0≤Δlow.\delta^{j^*} \Delta_0 \leq \Delta_{\text{low}}.

Secondo la Proposizione 4.4, il passo δj∗Δ0\delta^{j^*} \Delta_0 soddisfa la condizione di Armijo per ogni kk. Quindi, dall'algoritmo di Armijo, abbiamo:

jk≤j∗.j_k \leq j^*.

Per la definizione di j∗j^*, vale anche:

δj∗−1Δ0>Δlow,\delta^{j^* - 1} \Delta_0 > \Delta_{\text{low}},

e prendendo il logaritmo in base 1/δ1/\delta:

j∗−1<log⁡1/δΔ0Δlow,j^* - 1 < \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}},

quindi:

j∗=max⁡(0,⌈log⁡1/δΔ0Δlow⌉).j^* = \max\left(0, \lceil \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}} \rceil \right).

---

#### Limiti Inferiori su αk\alpha_k

Consideriamo i due casi:

1. Se Δ0≤Δlow\Delta_0 \leq \Delta_{\text{low}}, non è necessario effettuare backtracking (jk=0j_k = 0), e abbiamo:

αk=Δ0.\alpha_k = \Delta_0.

2. Se Δ0>Δlow\Delta_0 > \Delta_{\text{low}}, il backtracking fornisce:

αk=δjkΔ0,\alpha_k = \delta^{j_k} \Delta_0,

e quindi, dal limite inferiore sul numero di iterazioni jkj_k:

αk≥δΔlow.\alpha_k \geq \delta \Delta_{\text{low}}.

---

### Risultato Finale

Concludiamo che il passo αk\alpha_k è limitato inferiormente da:

αk≥min⁡{Δ0,δΔlow}.\alpha_k \geq \min\{\Delta_0, \delta \Delta_{\text{low}}\}.

Inoltre, il numero massimo di passi di backtracking necessari è dato da:

jk≤max⁡(0,log⁡1/δΔ0Δlow).j_k \leq \max\left(0, \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}}\right).
### Considerazioni sul Passo Costante e Risultati di Complessità

#### Conseguenze del Risultato su Δlow\Delta_{\text{low}}

Un'interessante conseguenza dei risultati precedenti è che, se conoscessimo le quantità LL, c1c_1, e c2c_2, e quindi Δlow\Delta_{\text{low}}, potremmo impostare direttamente il passo αk=Δlow\alpha_k = \Delta_{\text{low}}. Questo garantirebbe sempre la soddisfazione della condizione di Armijo, oltre alla convergenza globale descritta nella Proposizione 4.3, senza necessità di effettuare backtracking. Inoltre, il risultato di complessità successivo sarebbe anch'esso garantito.

Questo giustifica il fatto che talvolta gli algoritmi di discesa utilizzano un passo costante: se il valore scelto è inferiore a Δlow\Delta_{\text{low}}, si ottiene convergenza globale. Tuttavia, passi troppo piccoli riducono l'efficienza pratica degli algoritmi, rendendo le line search più convenienti, poiché consentono di provare passi più aggressivi senza compromettere le garanzie di convergenza.

---

### Proposizione 4.6: Complessità nel Caso Non Convesso

**Enunciato:**  
Sia f:Rn→Rf : \mathbb{R}^n \to \mathbb{R} una funzione LL-liscia. Sia {xk}\{x_k\} la sequenza generata da un algoritmo iterativo della forma:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

supponendo che la sequenza delle direzioni di ricerca {dk}\{d_k\} sia correlata al gradiente e che il passo αk\alpha_k venga calcolato tramite l'algoritmo di Armijo con un passo iniziale Δ0>δΔlow\Delta_0 > \delta \Delta_{\text{low}}. Inoltre, supponiamo che ff sia limitata inferiormente da un valore f∗f^*. Allora, per ogni ϵ>0\epsilon > 0, sono necessarie al massimo kmaxk_{\text{max}} iterazioni per produrre un iterato xkx_k tale che:

∥∇f(xk)∥≤ϵ,\|\nabla f(x_k)\| \leq \epsilon,

dove:

kmax≤f(x0)−f∗γc2δΔlowϵ2=O(ϵ−2).k_{\text{max}} \leq \frac{f(x_0) - f^*}{\gamma c_2 \delta \Delta_{\text{low}} \epsilon^2} = O(\epsilon^{-2}).

Lo stesso limite di complessità O(ϵ−2)O(\epsilon^{-2}) vale anche per il numero di valutazioni di funzione e gradiente.

---

#### Dimostrazione della Proposizione 4.6

Poiché la condizione di Armijo è soddisfatta a ogni iterazione e grazie alla condizione di correlazione al gradiente, abbiamo per ogni kk:

f(xk+1)−f(xk)=f(xk+αkdk)−f(xk)≤γαk∇f(xk)Tdk≤−γc2αk∥∇f(xk)∥2≤−γc2δΔlow∥∇f(xk)∥2.f(x_{k+1}) - f(x_k) = f(x_k + \alpha_k d_k) - f(x_k) \leq \gamma \alpha_k \nabla f(x_k)^T d_k \leq -\gamma c_2 \alpha_k \|\nabla f(x_k)\|^2 \leq -\gamma c_2 \delta \Delta_{\text{low}} \|\nabla f(x_k)\|^2.

L'ultima disuguaglianza deriva dalla Proposizione 4.5. Supponiamo ora che, per le prime kϵk_\epsilon iterazioni, valga ∥∇f(xk)∥>ϵ\|\nabla f(x_k)\| > \epsilon. Poiché ff è limitata inferiormente da f∗f^*, possiamo scrivere:

f∗−f(x0)≤f(xkϵ)−f(x0)=∑k=0kϵ−1(f(xk+1)−f(xk))≤∑k=0kϵ−1−γc2δΔlow∥∇f(xk)∥2.f^* - f(x_0) \leq f(x_{k_\epsilon}) - f(x_0) = \sum_{k=0}^{k_\epsilon - 1} \big(f(x_{k+1}) - f(x_k)\big) \leq \sum_{k=0}^{k_\epsilon - 1} -\gamma c_2 \delta \Delta_{\text{low}} \|\nabla f(x_k)\|^2.

Sostituendo il limite inferiore ∥∇f(xk)∥2>ϵ2\|\nabla f(x_k)\|^2 > \epsilon^2:

f∗−f(x0)≤−kϵγc2δΔlowϵ2.f^* - f(x_0) \leq -k_\epsilon \gamma c_2 \delta \Delta_{\text{low}} \epsilon^2.

Riordinando i termini, otteniamo:

kϵ≤f(x0)−f∗γc2δΔlowϵ2.k_\epsilon \leq \frac{f(x_0) - f^*}{\gamma c_2 \delta \Delta_{\text{low}} \epsilon^2}.

---

#### Complessità di Valutazione della Funzione e del Gradiente

Dato che il gradiente viene valutato una volta per iterazione e che, dalla Proposizione 4.5, il numero massimo di backtracking è costante a ogni iterazione, lo stesso limite O(ϵ−2)O(\epsilon^{-2}) si applica al numero di valutazioni della funzione e del gradiente.

---

### Conclusione

Nel caso non convesso, il limite di complessità O(ϵ−2)O(\epsilon^{-2}) stabilisce il numero massimo di iterazioni (e valutazioni di funzione/gradiente) necessario per raggiungere un gradiente con norma inferiore a ϵ\epsilon. Sebbene questo risultato rappresenti il caso peggiore, dimostra che i metodi di discesa basati su line search sono praticabili anche per problemi complessi e non convessi.

### Complessità e Metodo di Discesa del Gradiente

#### Complessità nei Metodi di Primo Ordine

Abbiamo dimostrato che i metodi di discesa basati su line search di tipo Armijo e direzioni correlate al gradiente hanno, per funzioni LL-lisce e non convesse, una complessità iterativa nel caso peggiore di:

O(1ϵ2),O\left(\frac{1}{\epsilon^2}\right),

equivalentemente descritta come:

O(1k).O\left(\frac{1}{\sqrt{k}}\right).

Questo risultato è significativo poiché il limite è noto per essere **ottimale** per i metodi di primo ordine.

---

#### Proposizione 4.7: Limite per Metodi di Primo Ordine

**Enunciato:** Nessun algoritmo di primo ordine può essere progettato con una complessità migliore di O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right) per trovare un punto stazionario approssimato ϵ\epsilon-accurato di una funzione LL-liscia.

**Osservazione:** Complessità migliori possono essere ottenute solo con ipotesi più forti, ad esempio quando la funzione obiettivo è convessa o, ancor meglio, strettamente convessa. Per questi casi particolari, le dimostrazioni devono sfruttare la definizione specifica delle regole di aggiornamento dell'algoritmo. Tali casi verranno analizzati in seguito.

---

### 4.3 Metodo di Discesa del Gradiente

È ora semplice introdurre l'algoritmo archetipo per l'ottimizzazione non lineare: il **metodo di discesa del gradiente**. Questo famoso algoritmo è un metodo basato su line search della forma:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

dove:

1. **Direzione di ricerca:** La direzione è il gradiente negativo: dk=−∇f(xk),d_k = -\nabla f(x_k), che è, ovviamente, una direzione correlata al gradiente con c1=c2=1c_1 = c_2 = 1.
2. **Scelta del passo:** Il passo αk\alpha_k è selezionato tramite la regola di Armijo.

---

#### Algoritmo 2: Metodo di Discesa del Gradiente

**Input:** x0∈Rnx_0 \in \mathbb{R}^n.

1. Inizializza k=0k = 0.
2. **Mentre** ∥∇f(xk)∥≠0\|\nabla f(x_k)\| \neq 0:  
    a. Imposta dk=−∇f(xk)d_k = -\nabla f(x_k).  
    b. Calcola αk\alpha_k lungo dkd_k usando la line search di Armijo (Algoritmo 1).  
    c. Aggiorna xk+1=xk+αkdkx_{k+1} = x_k + \alpha_k d_k.  
    d. Incrementa k=k+1k = k + 1.

---

#### Risultati di Convergenza nel Caso Non Convesso

Poiché l'algoritmo soddisfa tutti i criteri analizzati nelle sezioni 4.2.1 e 4.2.2, possiamo applicare direttamente le Proposizioni 4.3 e 4.6 per affermare:

- **Convergenza globale:** L'algoritmo converge verso un punto stazionario in contesti non convessi.
- **Complessità iterativa:** La complessità iterativa nel caso peggiore è O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right), ottimale per i metodi di primo ordine.
- **Valutazioni del gradiente e della funzione:** Poiché ogni iterazione richiede una sola valutazione del gradiente e il numero di passi di backtracking è limitato da una quantità costante (Proposizione 4.5), la complessità per le valutazioni della funzione è anch'essa O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right).

---

#### Caso Convesso con Passo Costante

Analizziamo ora il caso convesso assumendo un passo costante αk=1L\alpha_k = \frac{1}{L} a ogni iterazione. Sappiamo, dalla Proposizione 4.4 (con γ=0.5\gamma = 0.5), che questo passo soddisfa sempre la condizione di Armijo e conduce a risultati di convergenza globale.

**Proposizione 4.8: Convergenza nel Caso Convesso**

**Enunciato:** Sia ff una funzione LL-liscia e convessa, e sia {xk}\{x_k\} la sequenza generata dall'algoritmo di discesa del gradiente con passo costante αk=1L\alpha_k = \frac{1}{L}. Supponiamo che f∗f^* sia il valore ottimale di ff e che x∗x^* sia un minimizzatore di ff, cioè f(x∗)=f∗f(x^*) = f^*. Allora:

f(xk)−f∗≤L∥x0−x∗∥22k.f(x_k) - f^* \leq \frac{L \|x_0 - x^*\|^2}{2k}.

---

#### Interpretazione della Proposizione 4.8

Il risultato implica che:

1. **Errore iterativo:** L'errore iterativo è O(1k)O\left(\frac{1}{k}\right).
2. **Complessità iterativa:** La complessità iterativa è O(1ϵ)O\left(\frac{1}{\epsilon}\right).

Questo rappresenta un miglioramento significativo rispetto al caso non convesso, dove la complessità è O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right). La dipendenza lineare da kk o 1ϵ\frac{1}{\epsilon} è una caratteristica fondamentale dei metodi di primo ordine applicati a funzioni convesse lisce.

### Dimostrazione della Proposizione 4.8

#### Passo 1: Continuità Lipschitziana di ∇f(x)\nabla f(x)

Dalla continuità Lipschitziana del gradiente ∇f(x)\nabla f(x) e considerando xk+1=xk+αkdkx_{k+1} = x_k + \alpha_k d_k, abbiamo che:

f(xk+1)≤f(xk)+αk∇f(xk)Tdk+αk2L2∥dk∥2.f(x_{k+1}) \leq f(x_k) + \alpha_k \nabla f(x_k)^T d_k + \frac{\alpha_k^2 L}{2} \|d_k\|^2.

Sostituendo dk=−∇f(xk)d_k = -\nabla f(x_k) e αk=1L\alpha_k = \frac{1}{L}:

f(xk+1)≤f(xk)−1L∥∇f(xk)∥2+12L2L∥∇f(xk)∥2.f(x_{k+1}) \leq f(x_k) - \frac{1}{L} \|\nabla f(x_k)\|^2 + \frac{1}{2L^2} L \|\nabla f(x_k)\|^2.

Semplificando:

f(xk+1)≤f(xk)−12L∥∇f(xk)∥2.(9)f(x_{k+1}) \leq f(x_k) - \frac{1}{2L} \|\nabla f(x_k)\|^2. \tag{9}

---

#### Passo 2: Convessità della Funzione ff

Dalla convessità di ff, possiamo scrivere:

f(x∗)≥f(xk)+∇f(xk)T(x∗−xk).f(x^*) \geq f(x_k) + \nabla f(x_k)^T (x^* - x_k).

Riordinando:

f(xk)≤f(x∗)+∇f(xk)T(xk−x∗).f(x_k) \leq f(x^*) + \nabla f(x_k)^T (x_k - x^*).

---

#### Passo 3: Combinazione dei Risultati

Combinando la relazione sopra con l'equazione (9):

f(xk+1)≤f(x∗)+∇f(xk)T(xk−x∗)−12L∥∇f(xk)∥2.f(x_{k+1}) \leq f(x^*) + \nabla f(x_k)^T (x_k - x^*) - \frac{1}{2L} \|\nabla f(x_k)\|^2.

Da questa, possiamo ottenere:

f(xk+1)−f(x∗)≤∇f(xk)T(xk−x∗)−12L∥∇f(xk)∥2.f(x_{k+1}) - f(x^*) \leq \nabla f(x_k)^T (x_k - x^*) - \frac{1}{2L} \|\nabla f(x_k)\|^2.

Utilizziamo l'identità vettoriale ∥a∥2+∥b∥2−2aTb=∥a−b∥2\|a\|^2 + \|b\|^2 - 2a^T b = \|a - b\|^2, per riscrivere:

∥∇f(xk)∥2−2∇f(xk)T(xk−x∗)+∥xk−x∗∥2=∥xk−x∗−∇f(xk)∥2.\|\nabla f(x_k)\|^2 - 2 \nabla f(x_k)^T (x_k - x^*) + \|x_k - x^*\|^2 = \|x_k - x^* - \nabla f(x_k)\|^2.

Pertanto, abbiamo:

f(xk+1)−f(x∗)≤−L2∥xk+1−x∗∥2+L2∥xk−x∗∥2.f(x_{k+1}) - f(x^*) \leq -\frac{L}{2} \|x_{k+1} - x^*\|^2 + \frac{L}{2} \|x_k - x^*\|^2.

---

#### Passo 4: Somma su kk

Sommiamo entrambi i membri su t=0,…,kt = 0, \dots, k:

∑t=0k(f(xt+1)−f(x∗))≤L2(∥x0−x∗∥2−∥xk+1−x∗∥2).\sum_{t=0}^k \big(f(x_{t+1}) - f(x^*)\big) \leq \frac{L}{2} \big(\|x_0 - x^*\|^2 - \|x_{k+1} - x^*\|^2\big).

Poiché f(xt)f(x_t) è decrescente, vale f(xt+1)≥f(xk+1)f(x_{t+1}) \geq f(x_{k+1}) per ogni t=0,…,kt = 0, \dots, k, e quindi:

(k+1)(f(xk+1)−f(x∗))≤L2∥x0−x∗∥2.(k+1) \big(f(x_{k+1}) - f(x^*)\big) \leq \frac{L}{2} \|x_0 - x^*\|^2.

Dividendo per (k+1)(k+1), otteniamo:

f(xk+1)−f(x∗)≤L2(k+1)∥x0−x∗∥2.f(x_{k+1}) - f(x^*) \leq \frac{L}{2(k+1)} \|x_0 - x^*\|^2.

---

#### Conclusione

L'errore iterativo del metodo di discesa del gradiente è quindi:

f(xk+1)−f(x∗)≤L2k∥x0−x∗∥2,f(x_{k+1}) - f(x^*) \leq \frac{L}{2k} \|x_0 - x^*\|^2,

il che implica che l'algoritmo ha:

1. **Errore iterativo:** O(1k)O\left(\frac{1}{k}\right),
2. **Complessità iterativa:** O(1ϵ)O\left(\frac{1}{\epsilon}\right).

### 4.4 Metodi del Gradiente con Momento

Il semplice metodo di discesa del gradiente non è particolarmente efficiente in teoria e, in pratica, risulta spesso poco performante. Per questo motivo, si studiano approcci che mirano a migliorare la velocità del metodo di discesa del gradiente. Iniziamo con metodi di primo ordine che sfruttano informazioni dalle iterazioni precedenti per determinare la direzione di ricerca e il passo nell'iterazione corrente.

Questi metodi, noti come **metodi del gradiente con momento**, sono descritti dalla seguente regola di aggiornamento generica:

xk+1=xk−αk∇f(xk)+βk(xk−xk−1),x_{k+1} = x_k - \alpha_k \nabla f(x_k) + \beta_k (x_k - x_{k-1}),

dove:

- αk>0\alpha_k > 0 è il passo,
- βk>0\beta_k > 0 è il peso del momento.

L'idea alla base di questo aggiornamento è che la direzione dell'ultima iterazione sia probabilmente una buona direzione di ricerca anche per quella corrente. Ripetere parzialmente il passo precedente ha l'effetto di controllare le oscillazioni e fornire accelerazione nelle regioni di bassa curvatura. Questa strategia sfrutta solo informazioni già disponibili, senza richiedere ulteriori valutazioni della funzione, rendendola particolarmente attraente per problemi su larga scala.

I metodi del gradiente con momento più noti e importanti sono:

- **Metodo della palla pesante (Heavy-ball method);**
- **Metodi del gradiente coniugato (Conjugate gradient methods).**

---

### 4.4.1 Metodo della Palla Pesante (Heavy-ball Method)

Il **metodo della palla pesante** è descritto direttamente dalla regola di aggiornamento (10) ed è specificato dalla seguente regola in due passi:

yk=xk−αk∇f(xk),xk+1=yk+βk(xk−xk−1),\begin{aligned} &y_k = x_k - \alpha_k \nabla f(x_k), \\ &x_{k+1} = y_k + \beta_k (x_k - x_{k-1}), \end{aligned}

dove:

- αk\alpha_k e βk\beta_k sono tipicamente fissati a valori positivi.

In linea di principio, i valori dei parametri dovrebbero essere scelti in base alle proprietà della funzione obiettivo (ad esempio, utilizzando la costante di Lipschitz del gradiente o la costante di forte convessità). Tuttavia, nella pratica queste informazioni non sono spesso accessibili, quindi:

- αk\alpha_k può essere scelto tramite una **line search**,
- βk\beta_k viene spesso impostato a un valore "ragionevole" predefinito.

---

#### Risultati di Convergenza Locale

Per il metodo della palla pesante, i risultati di **convergenza locale** sono stati dimostrati nel caso convesso. In particolare:

- Nel caso di **funzioni quadratiche strettamente convesse**, i valori ottimali dei parametri αk\alpha_k e βk\beta_k possono essere calcolati in forma chiusa.
- Con questa scelta ottimale dei parametri, si ottiene un **tasso di convergenza lineare locale** con costanti migliori rispetto al metodo di discesa del gradiente standard.### Metodo della Palla Pesante: Limiti e Analogia Fisica

Sebbene il **metodo della palla pesante** abbia dimostrato buone proprietà di accelerazione in diversi contesti, è stato mostrato che il metodo potrebbe non convergere anche sotto forti assunzioni di regolarità. La convergenza del metodo nel caso non convesso rimane un problema aperto, in parte perché la struttura dell'algoritmo non rientra nel quadro analizzato nella Sezione 4.2.2.

---

#### Analogia Fisica

Il metodo della palla pesante è spesso spiegato tramite un'analogia fisica, sebbene non completamente accurata:
- Il **vettore delle variabili** può essere visto come una particella che si muove nello spazio euclideo.
- La particella tende naturalmente a preservare la sua traiettoria corrente ma viene deviata dall'accelerazione (il gradiente) prodotta da una forza.

In questo contesto, l'aggiornamento del momento può essere definito dalla seguente coppia di equazioni:

\[
v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k),
\]
\[
x_{k+1} = x_k + v_{k+1}.
\]

Qui:
- \(v_k\) rappresenta un termine di velocità, calcolato come una media decrescente esponenziale dei gradienti negativi passati.
- I gradienti modificano la velocità della particella, piuttosto che direttamente la sua posizione.
- Il movimento è quindi effettuato in base alla velocità calcolata nella posizione corrente.

---

### Metodo del Gradiente Accelerato di Nesterov

Il **metodo di Nesterov Accelerated Gradient (NAG)** può essere visto come una variante del metodo della palla pesante. La regola di aggiornamento dell'algoritmo di Nesterov è data da:

\[
v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k + \beta_k v_k),
\]
\[
x_{k+1} = x_k + v_{k+1}.
\]

---

#### Differenze rispetto alla Palla Pesante

L'unica differenza rispetto al metodo della palla pesante risiede nel fatto che:
- Il gradiente è calcolato nel punto che sarebbe ottenuto ripetendo l'ultimo movimento (\(x_k + \beta_k v_k\)) piuttosto che nel punto corrente (\(x_k\)).

Le iterazioni sono essenzialmente composte da due fasi:
1. **Passo puro di momento** (senza influenza del gradiente).
2. **Passo puro di discesa del gradiente**.

La regola di aggiornamento può essere riscritta in forma equivalente come:

\[
y_k = x_k - \alpha_k \nabla f(x_k),
\]
\[
x_{k+1} = y_k + \beta_k (y_k - y_{k-1}). \tag{11}
\]

---

#### Calcolo dei Parametri

- Il passo \(\alpha_k\) può essere calcolato tramite una **line search di Armijo**.
- Il parametro del momento \(\beta_k\) segue uno schema definito a priori.

---

#### Visualizzazione e Confronto

Un confronto visivo delle iterazioni dei metodi della palla pesante e di Nesterov è mostrato nella **Figura 5**:
- **(a)** Metodo della Palla Pesante.
- **(b)** Metodo di Nesterov Accelerated Gradient.

---

#### Importanza del Metodo di Nesterov

Il seguente risultato è particolarmente rilevante nell'ottimizzazione convessa.

---

### Proposizione per il Metodo di Nesterov

Sia \(f\) una funzione \(L\)-liscia e convessa. Con il metodo di Nesterov, usando valori appropriati di \(\alpha_k\) e \(\beta_k\), possiamo ottenere risultati di accelerazione significativi, inclusa una convergenza che migliora rispetto al metodo della palla pesante. Questi risultati saranno discussi in dettaglio nelle sezioni successive.

---

#### Generalizzazioni

I risultati sopra citati possono essere generalizzati sotto le seguenti ipotesi:

1. Differenziabilità due volte continua della funzione obiettivo;
2. Gradiente Lipschitz-continuo;
3. Forte convessità.

Queste ipotesi consentono al metodo della palla pesante di ottenere prestazioni superiori rispetto al gradiente standard, specialmente su problemi ben condizionati, grazie alla combinazione di accelerazione e controllo delle oscillazioni.

### Metodo della Palla Pesante: Limiti e Analogia Fisica

Sebbene il **metodo della palla pesante** abbia dimostrato buone proprietà di accelerazione in diversi contesti, è stato mostrato che il metodo potrebbe non convergere anche sotto forti assunzioni di regolarità. La convergenza del metodo nel caso non convesso rimane un problema aperto, in parte perché la struttura dell'algoritmo non rientra nel quadro analizzato nella Sezione 4.2.2.

---

#### Analogia Fisica

Il metodo della palla pesante è spesso spiegato tramite un'analogia fisica, sebbene non completamente accurata:

- Il **vettore delle variabili** può essere visto come una particella che si muove nello spazio euclideo.
- La particella tende naturalmente a preservare la sua traiettoria corrente ma viene deviata dall'accelerazione (il gradiente) prodotta da una forza.

In questo contesto, l'aggiornamento del momento può essere definito dalla seguente coppia di equazioni:

vk+1=βkvk−αk∇f(xk),v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k), xk+1=xk+vk+1.x_{k+1} = x_k + v_{k+1}.

Qui:

- vkv_k rappresenta un termine di velocità, calcolato come una media decrescente esponenziale dei gradienti negativi passati.
- I gradienti modificano la velocità della particella, piuttosto che direttamente la sua posizione.
- Il movimento è quindi effettuato in base alla velocità calcolata nella posizione corrente.

---

### Metodo del Gradiente Accelerato di Nesterov

Il **metodo di Nesterov Accelerated Gradient (NAG)** può essere visto come una variante del metodo della palla pesante. La regola di aggiornamento dell'algoritmo di Nesterov è data da:

vk+1=βkvk−αk∇f(xk+βkvk),v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k + \beta_k v_k), xk+1=xk+vk+1.x_{k+1} = x_k + v_{k+1}.

---

#### Differenze rispetto alla Palla Pesante

L'unica differenza rispetto al metodo della palla pesante risiede nel fatto che:

- Il gradiente è calcolato nel punto che sarebbe ottenuto ripetendo l'ultimo movimento (xk+βkvkx_k + \beta_k v_k) piuttosto che nel punto corrente (xkx_k).

Le iterazioni sono essenzialmente composte da due fasi:

1. **Passo puro di momento** (senza influenza del gradiente).
2. **Passo puro di discesa del gradiente**.

La regola di aggiornamento può essere riscritta in forma equivalente come:

yk=xk−αk∇f(xk),y_k = x_k - \alpha_k \nabla f(x_k), xk+1=yk+βk(yk−yk−1).(11)x_{k+1} = y_k + \beta_k (y_k - y_{k-1}). \tag{11}

---

#### Calcolo dei Parametri

- Il passo αk\alpha_k può essere calcolato tramite una **line search di Armijo**.
- Il parametro del momento βk\beta_k segue uno schema definito a priori.

---

#### Visualizzazione e Confronto

Un confronto visivo delle iterazioni dei metodi della palla pesante e di Nesterov è mostrato nella **Figura 5**:

- **(a)** Metodo della Palla Pesante.
- **(b)** Metodo di Nesterov Accelerated Gradient.

---

#### Importanza del Metodo di Nesterov

Il seguente risultato è particolarmente rilevante nell'ottimizzazione convessa.

---

### Proposizione per il Metodo di Nesterov

Sia ff una funzione LL-liscia e convessa. Con il metodo di Nesterov, usando valori appropriati di αk\alpha_k e βk\beta_k, possiamo ottenere risultati di accelerazione significativi, inclusa una convergenza che migliora rispetto al metodo della palla pesante. Questi risultati saranno discussi in dettaglio nelle sezioni successive.

### Proposizione 4.10: Complessità del Metodo di Nesterov

**Enunciato:**  
Sia ff una funzione LL-liscia e convessa, e sia {xk}\{x_k\} la sequenza prodotta dal **metodo del gradiente accelerato di Nesterov**. Supponiamo che f∗f^* sia il valore ottimale di ff. Allora:

f(xk)−f∗=O(1k2),f(x_k) - f^* = O\left(\frac{1}{k^2}\right),

ovvero, l'algoritmo ha un **errore iterativo** di O(1k2)O\left(\frac{1}{k^2}\right) e una **complessità iterativa** di O(1ϵ)O\left(\frac{1}{\sqrt{\epsilon}}\right).

---

#### Significato del Risultato

- Questo risultato è significativo poiché il limite di complessità O(1ϵ)O\left(\frac{1}{\sqrt{\epsilon}}\right) è stato dimostrato essere **ottimale** per i metodi di primo ordine: utilizzando solo informazioni sui gradienti, non è possibile ottenere complessità migliori.
- Tuttavia, il tasso di convergenza rimane **sublineare**, anche se significativamente più veloce rispetto al metodo di discesa del gradiente standard.

---

#### Caso Fortemente Convesso

Nel caso di funzioni **fortemente convesse**, il metodo del gradiente accelerato ottiene:

- La stessa complessità iterativa e tasso di convergenza del metodo di discesa del gradiente, cioè O(ρk)O(\rho^k).
- Tuttavia, il valore di ρ\rho è più piccolo rispetto a quello della discesa del gradiente, indicando un tasso di **convergenza lineare più rapido**.

---

### 4.4.2 Metodi del Gradiente Coniugato

I **metodi del gradiente coniugato** sono descritti dalle seguenti regole di aggiornamento:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k, dk+1=−∇f(xk+1)+βk+1dk,d_{k+1} = -\nabla f(x_{k+1}) + \beta_{k+1} d_k,

dove:

- αk\alpha_k è calcolato tramite una **line search**,
- βk\beta_k è ottenuto secondo una delle seguenti regole:

1. **Fletcher-Reeves**:
    
    βk+1=∥∇f(xk+1)∥2∥∇f(xk)∥2.\beta_{k+1} = \frac{\|\nabla f(x_{k+1})\|^2}{\|\nabla f(x_k)\|^2}.
2. **Polak-Ribiére**:
    
    βk+1=∇f(xk+1)T(∇f(xk+1)−∇f(xk))∥∇f(xk)∥2.\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{\|\nabla f(x_k)\|^2}.
3. **Hestenes-Stiefel**:
    
    βk+1=∇f(xk+1)T(∇f(xk+1)−∇f(xk))dkT(∇f(xk+1)−∇f(xk)).\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{d_k^T (\nabla f(x_{k+1}) - \nabla f(x_k))}.
4. **Liu-Storey**:
    
    βk+1=∥∇f(xk+1)∥2−dkT∇f(xk).\beta_{k+1} = \frac{\|\nabla f(x_{k+1})\|^2}{-d_k^T \nabla f(x_k)}.
5. **Dai-Yuan**:
    
    βk+1=∇f(xk+1)T(∇f(xk+1)−∇f(xk))−dkT∇f(xk).\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{-d_k^T \nabla f(x_k)}.

---

#### Costo Computazionale

Tutte le regole sopra elencate richiedono calcoli semplici basati su quantità già calcolate nel metodo di discesa del gradiente di base. Pertanto, il costo aggiuntivo per la costruzione della direzione dk+1d_{k+1} è trascurabile nella pratica.

---

#### Interpretazione come Metodo con Momento

L'aggiornamento nei metodi del gradiente coniugato può essere riscritto come:

xk+1=xk+αk(−∇f(xk)+βkdk−1),x_{k+1} = x_k + \alpha_k (-\nabla f(x_k) + \beta_k d_{k-1}),

che equivale a:

xk+1=xk−αk∇f(xk)+βkxk−xk−1αk−1.x_{k+1} = x_k - \alpha_k \nabla f(x_k) + \beta_k \frac{x_k - x_{k-1}}{\alpha_{k-1}}.

Questo è esattamente un **metodo del gradiente con momento**, secondo la definizione:

xk+1=xk−αk∇f(xk)+βk(xk−xk−1).x_{k+1} = x_k - \alpha_k \nabla f(x_k) + \beta_k (x_k - x_{k-1}).

---

#### Risultati di Convergenza

- I metodi del gradiente coniugato sono particolarmente efficaci per problemi quadratici strettamente convessi, dove convergono in un numero finito di iterazioni pari alla dimensione dello spazio del problema.
- In generale, offrono prestazioni superiori rispetto alla discesa del gradiente nei problemi ben condizionati, mantenendo costi computazionali simili.

### Metodi del Gradiente Coniugato: Problemi di Convergenza e Soluzioni

#### Assenza di Garanzie di Convergenza

Sebbene il metodo del gradiente coniugato segua la regola di aggiornamento:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

dove αk\alpha_k è calcolato tramite una **line search** lungo la direzione dkd_k, non possiamo garantire in generale che dkd_k sia:

- una **direzione di discesa** (∇f(xk)Tdk<0\nabla f(x_k)^T d_k < 0),
- né una **direzione correlata al gradiente**.

Di conseguenza, i risultati di convergenza descritti nella Sezione 4.2.2 non sono immediatamente applicabili.

---

#### Strategia di Salvaguardia per Garantire la Convergenza

Per recuperare le garanzie di convergenza, una strategia semplice consiste nell'introduzione di una salvaguardia all'interno del metodo:

1. **Verifica delle condizioni correlate al gradiente:** Se la direzione dkd_k soddisfa le condizioni correlate al gradiente, il metodo del gradiente coniugato può procedere normalmente con una **line search di Armijo**.
2. **Restart:** In caso contrario, l'algoritmo viene "riavviato" utilizzando una pura iterazione di discesa del gradiente.

Questa modifica permette di applicare immediatamente i risultati di convergenza e complessità delle Proposizioni 4.3 e 4.6.

---

#### Line Search di Wolfe per Garantire Direzioni di Discesa

Un'alternativa alla strategia di salvaguardia è l'uso di una **line search più forte**, come la **line search di Wolfe**, per garantire che dkd_k sia una direzione di discesa.

---

#### Condizioni di Wolfe

La line search di Wolfe mira a trovare un passo αk\alpha_k che soddisfi:

1. **Condizioni di Wolfe deboli:**
    
    f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, ∇f(xk+αkdk)Tdk≥σ∇f(xk)Tdk.\nabla f(x_k + \alpha_k d_k)^T d_k \geq \sigma \nabla f(x_k)^T d_k.
2. **Condizioni di Wolfe forti:**
    
    f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, ∣∇f(xk+αkdk)Tdk∣≤∣σ∇f(xk)Tdk∣.|\nabla f(x_k + \alpha_k d_k)^T d_k| \leq |\sigma \nabla f(x_k)^T d_k|.

Dove:

- γ∈(0,1)\gamma \in (0, 1),
- σ∈(γ,1)\sigma \in (\gamma, 1).

---

#### Significato delle Condizioni di Wolfe

- Le condizioni richiedono che la **condizione di Armijo** sia soddisfatta (riduzione sufficiente della funzione obiettivo).
- Richiedono inoltre che la derivata direzionale corrente sia significativamente ridotta al passo successivo, assicurando che la direzione corrente sia stata sfruttata al massimo.
- Questo restringe l'intervallo dei passi αk\alpha_k a valori che sono **approssimativamente stazionari** per ϕ(α)\phi(\alpha), garantendo che il prossimo passo non necessiti di muoversi nella stessa direzione.

---

#### Garanzie di Convergenza con Wolfe

Per garantire che la direzione dk+1=−∇f(xk+1)+βk+1dkd_{k+1} = -\nabla f(x_{k+1}) + \beta_{k+1} d_k sia una direzione di discesa, deve essere verificata la seguente condizione:

dk+1T∇f(xk+1)=−∥∇f(xk+1)∥2+βk+1dkT∇f(xk+1)<0.d_{k+1}^T \nabla f(x_{k+1}) = -\|\nabla f(x_{k+1})\|^2 + \beta_{k+1} d_k^T \nabla f(x_{k+1}) < 0.

- Qui, ∇f(xk+1)=∇f(xk+αkdk)\nabla f(x_{k+1}) = \nabla f(x_k + \alpha_k d_k) e, ad esempio, nel metodo di **Fletcher-Reeves**, βk+1\beta_{k+1} dipende da ∥∇f(xk)∥2\|\nabla f(x_k)\|^2.
- Poiché sia ∇f(xk+1)\nabla f(x_{k+1}) che βk+1\beta_{k+1} sono funzioni di αk\alpha_k, il loro comportamento può essere controllato tramite la line search di Wolfe.

---

#### Rappresentazione Grafica

Le condizioni di Wolfe, sia deboli che forti, possono essere illustrate graficamente (vedi Figura 6):

- Mostrano come le direzioni vengano selezionate in modo da ottimizzare il passo corrente e garantire che la direzione successiva mantenga le proprietà di discesa.

### Condizioni di Wolfe: Deboli e Forti

Le **condizioni di Wolfe** (deboli e forti) sono utilizzate per garantire che il passo αk\alpha_k scelto in una line search soddisfi sia la **condizione di Armijo** sia ulteriori restrizioni sulla derivata direzionale. Esse si esprimono come segue:

1. **Condizioni di Wolfe Deboli:**
    
    f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, ∇f(xk+αkdk)Tdk≥σ∇f(xk)Tdk.\nabla f(x_k + \alpha_k d_k)^T d_k \geq \sigma \nabla f(x_k)^T d_k.
2. **Condizioni di Wolfe Forti:**
    
    f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, ∣∇f(xk+αkdk)Tdk∣≤∣σ∇f(xk)Tdk∣.|\nabla f(x_k + \alpha_k d_k)^T d_k| \leq |\sigma \nabla f(x_k)^T d_k|.

Dove:

- γ∈(0,1)\gamma \in (0, 1) controlla la riduzione sufficiente della funzione,
- σ∈(γ,1)\sigma \in (\gamma, 1) garantisce che la derivata direzionale diminuisca adeguatamente.

---

### Visualizzazione Grafica (Figura 6)

La Figura 6 mostra come la **condizione di Armijo** e le **condizioni di Wolfe** limitino il passo αk\alpha_k. I passi accettabili si trovano nell'intervallo in cui:

- La funzione obiettivo si riduce sufficientemente (condizione di Armijo).
- La derivata direzionale soddisfa le restrizioni aggiuntive delle condizioni di Wolfe.

---

### Implicazioni Computazionali

- **Costi aggiuntivi:** L'uso della line search di Wolfe richiede il calcolo sia della funzione obiettivo sia del gradiente per ogni passo di prova, aumentando il costo computazionale rispetto alla sola condizione di Armijo.
- **Vantaggi:** Nel metodo del gradiente coniugato (ad esempio, con la regola di Fletcher-Reeves), l'uso della line search di Wolfe garantisce che la direzione successiva dk+1d_{k+1} sia una direzione di discesa: ∇f(xk+αkdk)Tdk+1<0.\nabla f(x_k + \alpha_k d_k)^T d_{k+1} < 0. Questo assicura proprietà di convergenza globale, rendendo i metodi del gradiente coniugato efficaci sia nei casi convessi sia non convessi, anche se i risultati di complessità non sono ancora ben definiti.

---

### Caso Quadratico e Metodi delle Direzioni Coniugate

I metodi del gradiente coniugato sono particolarmente efficaci per problemi di ottimizzazione **quadratici strettamente convessi** con funzioni obiettivo della forma:

f(x)=12xTQx+cTx,f(x) = \frac{1}{2} x^T Q x + c^T x,

dove QQ è una matrice simmetrica e definita positiva. In questi casi:

1. **Definizione delle Direzioni Coniugate:** Un insieme di direzioni d0,d1,…,dm−1∈Rnd_0, d_1, \dots, d_{m-1} \in \mathbb{R}^n è detto **mutuamente coniugato** rispetto a QQ se:
    
    diTQdj=0,∀i≠j.d_i^T Q d_j = 0, \quad \forall i \neq j.
    
    Questa proprietà è più forte della linearità indipendente.
    
2. **Proposizione 4.11: Convergenza Finita** Se d0,…,dn−1d_0, \dots, d_{n-1} sono mutuamente coniugate rispetto a QQ, allora:
    
    xm+1=x∗,x_{m+1} = x^*,
    
    con m≤n−1m \leq n - 1, dove x∗x^* è il minimizzatore globale che soddisfa Qx∗+c=0Qx^* + c = 0.
    
    **Significato:** Per problemi quadratici, con una ricerca esatta lungo direzioni mutuamente coniugate, il metodo converge esattamente al minimo globale in un numero finito di passi.
    

---

### Metodo del Gradiente Coniugato per Problemi Quadratici

L'algoritmo specifico per problemi quadratici è descritto come segue:

1. Inizializza: g0=∇f(x0)g_0 = \nabla f(x_0), d0=−g0d_0 = -g_0.
2. Per k=0,1,…k = 0, 1, \dots: αk=−gkTdkdkTQdk,\alpha_k = \frac{-g_k^T d_k}{d_k^T Q d_k}, xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k, gk+1=∇f(xk+1),g_{k+1} = \nabla f(x_{k+1}), βk+1=∥gk+1∥2∥gk∥2,\beta_{k+1} = \frac{\|g_{k+1}\|^2}{\|g_k\|^2}, dk+1=−gk+1+βk+1dk.d_{k+1} = -g_{k+1} + \beta_{k+1} d_k.

---

### Osservazioni Finali

- **Convergenza Finita:** Per problemi quadratici, il metodo è esatto e raggiunge il minimo globale in nn iterazioni.
- **Pratica:** In casi ad alta dimensione, si introduce un criterio di arresto basato su ∥gk∥≤ϵ\|g_k\| \leq \epsilon, rendendo il metodo iterativo. Soluzioni altamente accurate vengono spesso ottenute in poche iterazioni.

### Metodo del Gradiente Coniugato per Problemi Quadratici: Algoritmo e Analisi

#### Algoritmo 3: Metodo del Gradiente Coniugato per Problemi Quadratici

1. **Input:** x0∈Rnx_0 \in \mathbb{R}^n, d0=−g0d_0 = -g_0 (con g0=∇f(x0)g_0 = \nabla f(x_0)).
2. **Inizializzazione:** k=0k = 0.
3. **Iterazione:**
    - Calcola: αk=∥gk∥2dkTQdk.\alpha_k = \frac{\|g_k\|^2}{d_k^T Q d_k}.
    - Aggiorna: xk+1=xk+αkdk.x_{k+1} = x_k + \alpha_k d_k. gk+1=gk+αkQdk.g_{k+1} = g_k + \alpha_k Q d_k. βk+1=∥gk+1∥2∥gk∥2.\beta_{k+1} = \frac{\|g_{k+1}\|^2}{\|g_k\|^2}. dk+1=−gk+1+βk+1dk.d_{k+1} = -g_{k+1} + \beta_{k+1} d_k.
    - Incrementa k=k+1k = k + 1.
4. **Output:** xkx_k quando ∥gk∥≤ϵ\|g_k\| \leq \epsilon.

---

### Metodo di Newton: Introduzione

Il **metodo di Newton** è un algoritmo di ottimizzazione di secondo ordine che utilizza informazioni derivate dalla **matrice hessiana** ∇2f(x)\nabla^2 f(x) per accelerare la convergenza. La regola di aggiornamento è:

xk+1=xk−[∇2f(xk)]−1∇f(xk).x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k).

Questo metodo si basa sull'approssimazione quadratica della funzione obiettivo, costruita tramite l'espansione di Taylor di secondo ordine:

mk(x)=f(xk)+∇f(xk)T(x−xk)+12(x−xk)T∇2f(xk)(x−xk).m_k(x) = f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{1}{2} (x - x_k)^T \nabla^2 f(x_k) (x - x_k).

Il minimizzatore globale di mk(x)m_k(x) si ottiene annullandone il gradiente:

∇mk(x)=∇f(xk)+∇2f(xk)(x−xk)=0,x=xk−[∇2f(xk)]−1∇f(xk).\begin{aligned} \nabla m_k(x) &= \nabla f(x_k) + \nabla^2 f(x_k)(x - x_k) = 0, \\ x &= x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k). \end{aligned}

---

### Esempio 4.4: Iterazioni del Metodo di Newton

**Problema:**  
Minimizzare f(x)=1+x2f(x) = \sqrt{1 + x^2}, con:

f′(x)=x1+x2,f′′(x)=1(1+x2)3/2.f'(x) = \frac{x}{\sqrt{1 + x^2}}, \quad f''(x) = \frac{1}{(1 + x^2)^{3/2}}.

**Iterazioni:**

xk+1=xk−f′(xk)f′′(xk)=xk−xk(1+xk2).x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)} = x_k - x_k(1 + x_k^2).

- Se x0=±1x_0 = \pm 1, la sequenza oscilla tra 1 e -1, senza convergenza.
- Se ∣x0∣>1|x_0| > 1, la sequenza diverge.
- Se ∣x0∣<1|x_0| < 1 (es. x0=0.5x_0 = 0.5), la sequenza converge rapidamente a 0.

**Conclusione:**  
Il metodo di Newton non garantisce convergenza globale, ma se converge, lo fa **superlinearmente**.

---

### Proposizione 4.12: Proprietà del Metodo di Newton

Sia f:Rn→Rf : \mathbb{R}^n \to \mathbb{R} una funzione due volte continuamente differenziabile. Sia x∗x^* un punto tale che:

- ∇f(x∗)=0\nabla f(x^*) = 0,
- ∇2f(x∗)\nabla^2 f(x^*) è non singolare.

Allora esiste ϵ>0\epsilon > 0 tale che, per x0∈B(x∗,ϵ)x_0 \in B(x^*, \epsilon):

1. La sequenza {xk}\{x_k\} è ben definita e rimane in B(x∗,ϵ)B(x^*, \epsilon).
2. lim⁡k→∞xk=x∗\lim_{k \to \infty} x_k = x^*.
3. Il tasso di convergenza è **superlineare**.

---

#### Dimostrazione

**Continuità dell'Hessiana:** ∇2f(x)\nabla^2 f(x) è continua e non singolare in x∗x^*. Esistono ϵ1>0\epsilon_1 > 0 e μ>0\mu > 0 tali che:

∥[∇2f(x)]−1∥≤μ,∀x∈B(x∗,ϵ1).\|[\nabla^2 f(x)]^{-1}\| \leq \mu, \quad \forall x \in B(x^*, \epsilon_1).

**Induzione:**

- Base: x0∈B(x∗,ϵ)x_0 \in B(x^*, \epsilon).
- Passo: Assumiamo xk∈B(x∗,ϵ)x_k \in B(x^*, \epsilon). Per la regola di aggiornamento di Newton:

xk+1−x∗=−[∇2f(xk)]−1(∇f(xk)−∇2f(xk)(xk−x∗)).x_{k+1} - x^* = -[\nabla^2 f(x_k)]^{-1} (\nabla f(x_k) - \nabla^2 f(x_k)(x_k - x^*)).

Usando il teorema di Taylor e la continuità di ∇2f(x)\nabla^2 f(x), si dimostra che la sequenza converge a x∗x^* con tasso superlineare.

---

### Osservazioni Finali

- **Convergenza Globale:** Non garantita; dipende dalla scelta della soluzione iniziale.
- **Convergenza Locale:** Rapida, tipicamente superlineare.
- **Implicazioni:** Il metodo di Newton è estremamente efficace vicino al minimo, ma richiede attenzione per evitare divergenza o oscillazioni lontano da esso.

### Metodo di Newton e Convergenza Superlineare

#### Proprietà del Metodo di Newton

**Aggiornamento Iterativo:** Il metodo di Newton utilizza l'aggiornamento:

xk+1=xk−[∇2f(xk)]−1∇f(xk),x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k),

dove:

- ∇2f(xk)\nabla^2 f(x_k) è la matrice hessiana.
- ∇f(xk)\nabla f(x_k) è il gradiente della funzione obiettivo.

**Conclusione Principale:** Il metodo di Newton gode di **garanzie di convergenza locale superlineare** in prossimità di un punto stazionario x∗x^* che soddisfa le seguenti condizioni:

1. ∇f(x∗)=0\nabla f(x^*) = 0,
2. ∇2f(x∗)\nabla^2 f(x^*) è non singolare.

---

#### Analisi della Convergenza

1. **Integrazione della Hessiana:** Usando il **teorema del valore medio**, possiamo esprimere:
    
    ∇f(xk)−∇f(x∗)=∫01∇2f(x∗+t(xk−x∗))(xk−x∗) dt.\nabla f(x_k) - \nabla f(x^*) = \int_0^1 \nabla^2 f(x^* + t(x_k - x^*))(x_k - x^*) \, dt.
2. **Stima della Distanza:** Sostituendo nella relazione di aggiornamento, otteniamo:
    
    ∥xk+1−x∗∥≤μ∫01∥∇2f(x∗+t(xk−x∗))−∇2f(xk)∥∥xk−x∗∥ dt.\|x_{k+1} - x^*\| \leq \mu \int_0^1 \|\nabla^2 f(x^* + t(x_k - x^*)) - \nabla^2 f(x_k)\| \|x_k - x^*\| \, dt.
3. **Continuità della Hessiana:** Poiché xk→x∗x_k \to x^* e ∇2f(x)\nabla^2 f(x) è continua, la differenza ∥∇2f(x∗+t(xk−x∗))−∇2f(xk)∥\|\nabla^2 f(x^* + t(x_k - x^*)) - \nabla^2 f(x_k)\| tende a 0. Questo porta a:
    
    ∥xk+1−x∗∥≤σ∥xk−x∗∥,\|x_{k+1} - x^*\| \leq \sigma \|x_k - x^*\|,
    
    con σ∈(0,1)\sigma \in (0, 1), garantendo convergenza.
    
4. **Tasso di Convergenza:** Iterando, abbiamo:
    
    ∥xk−x∗∥≤σk∥x0−x∗∥,\|x_k - x^*\| \leq \sigma^k \|x_0 - x^*\|,
    
    mostrando che la convergenza è **superlineare**.
    

---

#### Problemi del Metodo di Newton

1. **Costo Computazionale Elevato:**
    
    - Calcolare ∇2f(xk)\nabla^2 f(x_k) richiede O(n2)O(n^2).
    - Risolvere il sistema lineare [∇2f(xk)]dk=−∇f(xk)[ \nabla^2 f(x_k) ] d_k = -\nabla f(x_k) richiede O(n3)O(n^3).
    - Questo rende il metodo meno pratico in problemi su larga scala.
2. **Assenza di Garanzie di Convergenza Globale:**
    
    - Se ∇2f(xk)\nabla^2 f(x_k) non è definita positiva, il metodo potrebbe fallire.
    - In funzioni non convesse, la direzione calcolata potrebbe essere di salita invece che di discesa.
3. **Dipendenza dalla Soluzione Iniziale:**
    
    - Se il punto iniziale x0x_0 è lontano da x∗x^*, il metodo potrebbe non convergere.

---

#### Strategia di Globalizzazione

Per risolvere i problemi sopra menzionati, si introducono le seguenti modifiche:

1. **Modifica della Hessiana:**
    
    - Se alcuni autovalori di ∇2f(xk)\nabla^2 f(x_k) sono fuori dall'intervallo [c2,c1][c_2, c_1] con 0<c2<c1<∞0 < c_2 < c_1 < \infty, si modifica la matrice per garantire che sia definita positiva.
2. **Ricerca Lineare di Armijo:**
    
    - Si esegue una ricerca di Armijo lungo la direzione calcolata, iniziando con un passo iniziale α=1\alpha = 1.
3. **Comportamento Localizzato:**
    
    - Una volta che il metodo entra in una regione vicina al punto stazionario x∗x^*, le modifiche alla Hessiana e la ricerca lineare diventano superflue, permettendo al metodo di recuperare la velocità di convergenza locale.

**Conclusione:**  
Queste strategie portano al **metodo di Newton globalmente convergente**, che combina garanzie di convergenza globale con tassi di convergenza locale superlineari.

---

### Considerazioni Finali

Il metodo di Newton rappresenta uno strumento potente per l'ottimizzazione non lineare, ma il suo utilizzo richiede attenzione:

- **Localmente:** È estremamente efficace, con una velocità di convergenza superlineare.
- **Globalmente:** Deve essere modificato per garantire la convergenza.

Nonostante il costo computazionale elevato, il metodo è ideale per problemi in cui il numero di iterazioni è più critico del costo per iterazione.

### Metodi Quasi-Newton

I metodi Quasi-Newton nascono dall'esigenza di mantenere la velocità di convergenza dei metodi di Newton, riducendo però i costi computazionali per iterazione. Invece di calcolare esattamente la matrice hessiana, questi metodi utilizzano un'approssimazione costruita tramite informazioni di primo ordine e iterazioni precedenti.

#### Formula Generale

I metodi Quasi-Newton seguono la regola di aggiornamento:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

dove la direzione dkd_k è calcolata come:

dk=−Hk∇f(xk),d_k = -H_k \nabla f(x_k),

con Hk≈[∇2f(xk)]−1H_k \approx [\nabla^2 f(x_k)]^{-1}. Alternativamente, possiamo utilizzare un'approssimazione diretta della Hessiana:

dk=−Bk−1∇f(xk),d_k = -B_k^{-1} \nabla f(x_k),

con Bk≈∇2f(xk)B_k \approx \nabla^2 f(x_k).

---

#### Equazione Quasi-Newton

Per funzioni quadratiche f(x)=12xTQx+cTxf(x) = \frac{1}{2}x^T Qx + c^T x, con Q≻0Q \succ 0, si ha:

Δ∇f=∇f(xk+1)−∇f(xk)=Q(xk+1−xk).\Delta \nabla f = \nabla f(x_{k+1}) - \nabla f(x_k) = Q(x_{k+1} - x_k).

Generalizzando, imponiamo che le matrici approssimate soddisfino una relazione simile:

Bk+1sk=yk,B_{k+1}s_k = y_k,

oppure:

Hk+1yk=sk,H_{k+1}y_k = s_k,

dove:

- sk=xk+1−xks_k = x_{k+1} - x_k,
- yk=∇f(xk+1)−∇f(xk)y_k = \nabla f(x_{k+1}) - \nabla f(x_k).

---

#### Schema Generale

Lo schema algoritmico per un metodo Quasi-Newton è riportato di seguito:

**Algoritmo 4: Metodo Quasi-Newton con Aggiornamenti Inversi**

1. **Input:** x0∈Rnx_0 \in \mathbb{R}^n, H0∈SnH_0 \in S^n, H0≻0H_0 \succ 0.
2. **Inizializzazione:** k=0k = 0.
3. **Ciclo:**
    - Calcolare dk=−Hk∇f(xk)d_k = -H_k \nabla f(x_k).
    - Determinare αk\alpha_k tramite una ricerca lineare.
    - Aggiornare xk+1=xk+αkdkx_{k+1} = x_k + \alpha_k d_k.
    - Calcolare ΔHk\Delta H_k affinché Hk+1yk=skH_{k+1} y_k = s_k.
    - Aggiornare Hk+1=Hk+ΔHkH_{k+1} = H_k + \Delta H_k.
4. **Fermarsi quando ∥∇f(xk)∥≈0\|\nabla f(x_k)\| \approx 0.

---

#### Regole di Aggiornamento

##### **Aggiornamenti di rango-1**

La forma generale è:

ΔHk=ρkukvkT,\Delta H_k = \rho_k u_k v_k^T,

dove ρk∈R+\rho_k \in \mathbb{R}^+, uk,vk∈Rnu_k, v_k \in \mathbb{R}^n. Un esempio noto è la **regola di Broyden**:

Bk+1=Bk+(yk−Bksk)skTskTsk.B_{k+1} = B_k + \frac{(y_k - B_k s_k)s_k^T}{s_k^T s_k}.

**Svantaggi:** La simmetria e la definita positività di Bk+1B_{k+1} non sono garantite.

##### **Aggiornamenti di rango-2**

La forma generale è:

ΔHk=akukukT+bkvkvkT,\Delta H_k = a_k u_k u_k^T + b_k v_k v_k^T,

dove ak,bk∈R+a_k, b_k \in \mathbb{R}^+. Questi aggiornamenti garantiscono stabilità e proprietà desiderate per HkH_k.

---

### Algoritmo BFGS

Il **BFGS (Broyden-Fletcher-Goldfarb-Shanno)** è uno dei metodi Quasi-Newton più popolari, basato su aggiornamenti di rango-2. Le formule sono:

**Aggiornamento Diretto (Hessiana):**

Bk+1=Bk+ykykTykTsk−BkskskTBkskTBksk.B_{k+1} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}.

**Aggiornamento Inverso (Hessiana inversa):**

Hk+1=Hk+(1+ykTHkykskTyk)skskTskTyk−HkykskT+skykTHkskTyk.H_{k+1} = H_k + \left(1 + \frac{y_k^T H_k y_k}{s_k^T y_k}\right)\frac{s_k s_k^T}{s_k^T y_k} - \frac{H_k y_k s_k^T + s_k y_k^T H_k}{s_k^T y_k}.

---

### Vantaggi dei Metodi Quasi-Newton

1. **Efficienza Computazionale:**
    
    - Evitano il calcolo diretto di ∇2f(xk)\nabla^2 f(x_k).
    - Risolvono O(n2)\mathcal{O}(n^2) operazioni per aggiornare HkH_k rispetto alle O(n3)\mathcal{O}(n^3) del metodo di Newton.
2. **Convergenza Globale:**
    
    - Combinando una ricerca di Armijo e un controllo sugli autovalori, si garantisce la convergenza globale con complessità O(1ϵ2)\mathcal{O}(\frac{1}{\epsilon^2}).
3. **Applicabilità su Scala Larga:**
    
    - Ideali per problemi ad alta dimensionalità.

---

### Conclusione

I metodi Quasi-Newton bilanciano efficienza computazionale e velocità di convergenza, rendendoli strumenti versatili per l'ottimizzazione non lineare, in particolare in contesti su larga scala.

### Nota che queste regole di aggiornamento soddisfano effettivamente la proprietà di quasi-Newton; infatti:

Bk+1sk=Bksk+ykykTykTsksk−BkskskTBkskTBksksk=Bksk+ykykTskykTsk−Bksk=Bksk+yk−Bksk=yk.B_{k+1}s_k = B_k s_k + \frac{y_k y_k^T}{y_k^T s_k}s_k - B_k \frac{s_k s_k^T B_k}{s_k^T B_k s_k}s_k = B_k s_k + y_k \frac{y_k^T s_k}{y_k^T s_k} - B_k s_k = B_k s_k + y_k - B_k s_k = y_k.

Calcoli simili possono essere eseguiti per la regola di aggiornamento inversa.

---

### Preservazione della definitezza positiva nell'algoritmo BFGS

**Proposizione 4.13.** Sia HkH_k definito positivo e Hk+1H_{k+1} calcolato tramite la regola di aggiornamento BFGS. Allora Hk+1H_{k+1} è definito positivo se e solo se skTyk>0s_k^T y_k > 0.

Questa proposizione garantisce che, se H0H_0 è definito positivo e ad ogni iterazione skTyk>0s_k^T y_k > 0, la condizione di definitezza positiva sarà mantenuta in ogni passo.

La condizione skTyk>0s_k^T y_k > 0 può essere imposta scegliendo adeguatamente il passo αk\alpha_k. Infatti:

skTyk=(∇f(xk+1)−∇f(xk))T(xk+1−xk)>0,s_k^T y_k = (\nabla f(x_{k+1}) - \nabla f(x_k))^T (x_{k+1} - x_k) > 0,

che equivale a:

(∇f(xk+1)−∇f(xk))Tdk>0,(\nabla f(x_{k+1}) - \nabla f(x_k))^T d_k > 0,

oppure:

∇f(xk+1)Tdk>∇f(xk)Tdk.\nabla f(x_{k+1})^T d_k > \nabla f(x_k)^T d_k.

Questa condizione può essere soddisfatta utilizzando una ricerca lineare del tipo Wolfe per determinare αk\alpha_k nell'algoritmo 4.

---

### Algoritmo BFGS

L'algoritmo BFGS, senza ulteriori accorgimenti, offre risultati di convergenza globale sotto ipotesi di convessità sulla funzione obiettivo ff. Inoltre, se ff è fortemente convessa e due volte differenziabile, l'algoritmo può essere dimostrato convergere superlinearmente al minimizzatore globale, accettando sempre il passo unitario per grandi kk.

Pertanto, l'algoritmo BFGS riesce a raggiungere una velocità di convergenza locale rapida, simile al metodo di Newton, senza utilizzare informazioni di secondo ordine.

---

### Metodo L-BFGS

Il metodo **L-BFGS** è una variante del BFGS progettata specificamente per problemi di grande scala (da cui il nome _Limited Memory_). Questo metodo mostra un'ottima performance pratica ed è considerato una delle scelte preferite per risolvere problemi di ottimizzazione non vincolati.

#### Idea Chiave

In problemi ad alta dimensionalità, la memorizzazione della matrice HkH_k e il calcolo di dk=−Hk∇f(xk)d_k = -H_k \nabla f(x_k) possono diventare proibitivi. Per affrontare questa difficoltà, L-BFGS utilizza una regola ricorsiva che richiede solo i vettori yky_k e sks_k per calcolare:

Hk+1=VkTHkVk+ρkskskT,H_{k+1} = V_k^T H_k V_k + \rho_k s_k s_k^T,

dove:

ρk=1ykTsk,Vk=I−ρkykskT.\rho_k = \frac{1}{y_k^T s_k}, \quad V_k = I - \rho_k y_k s_k^T.

In L-BFGS, l'approssimazione Hk+1H_{k+1} viene interrotta dopo mm passi, utilizzando solo le ultime mm coppie (yk,sk)(y_k, s_k), insieme a una stima iniziale Hk−m≈γIH_{k-m} \approx \gamma I, facilmente memorizzabile.

---

### Prestazioni e Limiti del Metodo L-BFGS

Esperimenti mostrano che valori relativamente piccoli di mm (tra 2 e 20) sono sufficienti per ottenere approssimazioni soddisfacenti. Inoltre, la procedura ricorsiva HG consente di calcolare dkd_k con soli 4mn4mn moltiplicazioni, riducendo significativamente i costi computazionali.

Tuttavia:

- Le proprietà teoriche di convergenza globale non sono forti come per il BFGS.
- La convergenza globale può essere garantita solo con strategie di salvaguardia standard.
- In caso di forte convessità, è possibile dimostrare la convergenza lineare sotto ipotesi specifiche su HkH_k.

Un'estensione chiamata **L-BFGS-B** è stata progettata per affrontare problemi di ottimizzazione con vincoli di tipo _bound constrained_.

### Metodi di Decomposizione e Metodi Stocastici

#### **Metodi di Decomposizione**

I metodi di decomposizione mirano a suddividere i problemi complessi in sottoproblemi più semplici, lavorando su blocchi di variabili. Tali approcci possono essere classificati in due categorie principali: **metodi sequenziali** e **metodi paralleli**.

---

#### **Metodi di Decomposizione Sequenziale**

Nei metodi sequenziali, i sottoproblemi vengono risolti uno alla volta, aggiornando le variabili di ciascun blocco ad ogni passo. Un esempio classico è l'**algoritmo di Gauss-Seidel**, definito dalla seguente regola di aggiornamento:

xik+1=arg⁡min⁡ξi∈Xif(x1k+1,…,xi−1k+1,ξi,xi+1k,…,xmk).x_{i}^{k+1} = \arg\min_{\xi_i \in X_i} f(x_{1}^{k+1}, \dots, x_{i-1}^{k+1}, \xi_i, x_{i+1}^k, \dots, x_m^k).

L'algoritmo risolve ciclicamente i sottoproblemi ottenuti fissando il valore di tutte le variabili, tranne quelle di un blocco. La soluzione trovata per il sottoproblema viene immediatamente utilizzata per aggiornare il valore delle variabili del blocco corrente.

**Garanzie di convergenza:**

- **Convessità di ff:** il metodo converge ai punti stazionari.
- **Convessità stretta per blocchi:** il metodo garantisce la convergenza anche in casi non globalmente convessi.
- **Due blocchi di variabili (m=2m = 2):** la convessità globale non è necessaria.

---

#### **Metodi di Decomposizione Parallela**

Nei metodi paralleli, i sottoproblemi associati ai diversi blocchi vengono risolti in modo indipendente e simultaneo. Successivamente, la soluzione migliore tra questi sottoproblemi viene utilizzata per aggiornare le variabili, ovvero ad ogni iterazione si aggiorna un solo blocco.

Un esempio è l'**algoritmo di Jacobi**, descritto dalle seguenti regole di aggiornamento:

x^ik+1∈arg⁡min⁡xif(x1k,…,xi,…,xmk),\hat{x}_{i}^{k+1} \in \arg\min_{x_i} f(x_1^k, \dots, x_i, \dots, x_m^k), xk+1∈arg⁡min⁡f(x1k,…,x^ik+1,…,xmk).x^{k+1} \in \arg\min f(x_1^k, \dots, \hat{x}_{i}^{k+1}, \dots, x_m^k).

---

#### **Metodi di Decomposizione con Sovrapposizione dei Blocchi**

Un'estensione più flessibile permette di lavorare con insiemi variabili di blocchi, chiamati **insiemi di lavoro** (WkW_k). Il sottoproblema considerato in ogni iterazione diventa:

min⁡xWkf(xWk,xWkc),\min_{x_{W_k}} f(x_{W_k}, x_{W_k^c}),

dove WkcW_k^c è il complemento di WkW_k. La regola di aggiornamento è:

xik+1={xi⋆se i∈Wk,xikaltrimenti.x_i^{k+1} = \begin{cases} x_i^\star & \text{se } i \in W_k, \\ x_i^k & \text{altrimenti.} \end{cases}

---

#### **Metodi Stocastici**

I problemi di **somma finita**, tipici in apprendimento automatico, sono rappresentati come:

min⁡x∈Rnf(x)=1N∑i=1Nfi(x).\min_{x \in \mathbb{R}^n} f(x) = \frac{1}{N} \sum_{i=1}^N f_i(x).

Quando NN è molto grande, calcolare il gradiente completo ∇f(x)\nabla f(x) diventa oneroso. L'**algoritmo di discesa del gradiente stocastico (SGD)** fornisce una soluzione computazionalmente più leggera, aggiornando le variabili con passi stocastici basati su un gradiente approssimato:

xk+1=xk−αk∇fik(xk),x^{k+1} = x^k - \alpha_k \nabla f_{i_k}(x^k),

dove iki_k è un indice scelto casualmente tra {1,…,N}\{1, \dots, N\}.

---

#### **Proprietà e Varianti di SGD**

1. **Stima del gradiente:** L'approccio è stocastico ma garantisce che il gradiente approssimato ∇fik(xk)\nabla f_{i_k}(x^k) sia un **stimatore non distorto** del gradiente reale:

E[∇fik(xk)]=∇f(xk).\mathbb{E}[\nabla f_{i_k}(x^k)] = \nabla f(x^k).

2. **Mini-batch SGD:** Per ridurre la varianza, si calcola il gradiente su un sottoinsieme (mini-batch) di MM termini della somma:

dk=−1M∑i∈Bk∇fi(xk).d_k = -\frac{1}{M} \sum_{i \in B_k} \nabla f_i(x^k).

3. **Strategia di riordinamento casuale:** Gli indici vengono rimescolati ad ogni epoca, garantendo che ogni termine sia usato una volta per epoca.

---

#### **Analisi Teorica di SGD**

Sotto opportune assunzioni di smoothness e scelta del passo αk\alpha_k, l'algoritmo garantisce che:

lim⁡k→∞E[∥∇f(zk)∥2]=0.\lim_{k \to \infty} \mathbb{E}\left[\|\nabla f(z^k)\|^2\right] = 0.

Questa proprietà assicura che l'algoritmo converge a punti stazionari, anche in presenza di rumore stocastico.

### Traduzione in Italiano

#### Aggiornamenti nell'SGD

L'algoritmo **Stochastic Gradient Descent (SGD)** utilizza aggiornamenti della forma:

xk+1=xk−αk∇fik(xk),x^{k+1} = x^k - \alpha_k \nabla f_{i_k}(x^k),

dove il passo αk\alpha_k è spesso impostato a un valore costante o segue una sequenza predefinita. Le tradizionali ricerche di linee (line searches) non sono generalmente adatte in questo caso, poiché la funzione obiettivo cambia a ogni iterazione. Questo porta a due problematiche principali:

1. Non si può garantire una diminuzione sufficiente della funzione obiettivo reale.
2. Forzare una diminuzione sufficiente sull'approssimazione corrente potrebbe non portare benefici.

---

#### **Razionalità della direzione di ricerca stocastica**

La scelta stocastica della direzione di discesa si basa sul fatto che, se consideriamo il valore atteso della quantità ∇fik(xk)\nabla f_{i_k}(x^k), e assumendo una distribuzione uniforme sui valori {1,…,N}\{1, \ldots, N\}, otteniamo:

E[∇fi(xk)]=∑i=1Npi∇fi(xk)=∑i=1N1N∇fi(xk)=1N∑i=1N∇fi(xk)=∇f(xk).E[\nabla f_i(x^k)] = \sum_{i=1}^N p_i \nabla f_i(x^k) = \sum_{i=1}^N \frac{1}{N} \nabla f_i(x^k) = \frac{1}{N} \sum_{i=1}^N \nabla f_i(x^k) = \nabla f(x^k).

In altre parole, in media ci si aspetta di ottenere il gradiente reale. Formalmente, diciamo che una direzione dkd_k è uno **stimatore non distorto** del vero gradiente ∇f(xk)\nabla f(x^k) se soddisfa E[dk]=−∇f(xk)E[d_k] = -\nabla f(x^k).

---

#### **Strategie per ridurre la varianza**

Ridurre la varianza del gradiente stocastico è fondamentale per diminuire gli errori nella stima della direzione di discesa. Strategie di riduzione della varianza sono state proposte per migliorare il tasso di convergenza teorico di SGD. Tuttavia, queste strategie richiedono:

- **Elevati requisiti di memoria**, oppure
- **Calcolo del gradiente reale** in alcune iterazioni.

Per questo motivo, tali strategie sono applicabili solo in problemi particolarmente strutturati.

Un approccio pratico per ottenere un effetto di riduzione della varianza è basare il calcolo del gradiente non su un singolo termine della somma, ma su un sottoinsieme di termini Bk⊂{1,…,N}B_k \subset \{1, \ldots, N\}, con ∣Bk∣=M≪N|B_k| = M \ll N:

dk=−1∣Bk∣∑i∈Bk∇fi(xk).d_k = -\frac{1}{|B_k|} \sum_{i \in B_k} \nabla f_i(x^k).

---

#### **Remark 4.1**

Nel contesto del **machine learning** e dell'apprendimento statistico:

- Ogni termine fif_i corrisponde alla **perdita associata a un campione**.
- Un sottoinsieme BkB_k di esempi è detto **mini-batch**, in contrasto con il **full batch**, che include l'intero dataset.

Nel contesto del **deep learning**, il passo αk\alpha_k è comunemente noto come **learning rate**.

---

#### **Mini-Batching e Random Reshuffling**

Le tecniche di mini-batching e le strategie stocastiche sono spesso combinate con un rimescolamento casuale. Invece di scegliere gli indici in BkB_k completamente a caso a ogni iterazione:

- Si effettuano **macro-iterazioni** (chiamate epoche), in cui tutti i termini della somma sono usati esattamente una volta.

La struttura di un algoritmo di **mini-batch SGD con random reshuffling** è mostrata in _Algorithm 5_.

---

#### **Analisi Teorica del SGD**

Per studiare rigorosamente l'SGD, si introducono alcune ipotesi aggiuntive:

1. ff è **limitata inferiormente**.
2. Il modulo dei campioni di gradiente è limitato da una costante G>0G > 0: ∥∇fi(x)∥≤G,∀x∈Rn.\|\nabla f_i(x)\| \leq G, \quad \forall x \in \mathbb{R}^n.
3. La funzione obiettivo è LL-lipschitziana (L-smooth).

---

#### **Proposizione 4.14**

Sia {xk}\{x^k\} la sequenza generata dall'algoritmo SGD con una sequenza di passi {αk}\{\alpha_k\} tale che:

- ∑k=0∞αk=∞\sum_{k=0}^\infty \alpha_k = \infty,
- ∑k=0∞αk2<∞\sum_{k=0}^\infty \alpha_k^2 < \infty.

Assumendo che, a ogni iterazione kk, l'algoritmo selezioni casualmente un τ∈{0,…,k−1}\tau \in \{0, \ldots, k-1\} con probabilità:

P(τ=t)=αt∑i=0k−1αi,P(\tau = t) = \frac{\alpha_t}{\sum_{i=0}^{k-1} \alpha_i},

allora:

lim⁡k→∞E[∥∇f(zk)∥2]=0.\lim_{k \to \infty} E\left[\|\nabla f(z^k)\|^2\right] = 0.

---

#### **Dimostrazione (Schizzo)**

Dalla proprietà di smoothness e l'ipotesi sui campioni del gradiente, si ottiene che:

f(xk+1)≤f(xk)−αk∇fik(xk)T∇f(xk)+αk2LG22.f(x^{k+1}) \leq f(x^k) - \alpha_k \nabla f_{i_k}(x^k)^T \nabla f(x^k) + \frac{\alpha_k^2 L G^2}{2}.

Sotto aspettazione e applicando le ipotesi di αk\alpha_k, si dimostra che la successione converge in media a un punto stazionario, soddisfacendo:

lim⁡k→∞E[∥∇f(zk)∥2]=0.\lim_{k \to \infty} E[\|\nabla f(z^k)\|^2] = 0.

### Traduzione in Italiano

#### **Valore atteso del gradiente stocastico**

Il valore atteso di ∇fik(xk)\nabla f_{i_k}(x^k), dato xkx^k, può essere calcolato come:

E[∇fik(xk) ∣ xk]=∑i=1n∇fi(xk)⋅P(ik=i ∣ xk)=∑i=1n∇fi(xk)⋅1n=∇f(xk).E\left[\nabla f_{i_k}(x^k) \,|\, x^k\right] = \sum_{i=1}^n \nabla f_i(x^k) \cdot P(i_k = i \,|\, x^k) = \sum_{i=1}^n \nabla f_i(x^k) \cdot \frac{1}{n} = \nabla f(x^k).

Quindi, in media, il gradiente stocastico corrisponde al vero gradiente ∇f(xk)\nabla f(x^k).

---

#### **Dimostrazione dell'ineguaglianza ricorsiva**

Dalla proprietà di Lipschitz-continuity della funzione ff e dall'assunzione sui campioni del gradiente, abbiamo:

E[f(xk+1)]≤E[f(xk)]−αkE[∥∇f(xk)∥2]+αk2LG22.E\left[f(x^{k+1})\right] \leq E\left[f(x^k)\right] - \alpha_k E\left[\|\nabla f(x^k)\|^2\right] + \frac{\alpha_k^2 L G^2}{2}.

Applicando ricorsivamente questa disuguaglianza e osservando che E[f(x0)]=f(x0)E[f(x^0)] = f(x^0), otteniamo:

E[f(xk+1)]−f(x0)≤−∑t=0kαtE[∥∇f(xt)∥2]+LG22∑t=0kαt2.E\left[f(x^{k+1})\right] - f(x^0) \leq - \sum_{t=0}^k \alpha_t E\left[\|\nabla f(x^t)\|^2\right] + \frac{L G^2}{2} \sum_{t=0}^k \alpha_t^2.

Da cui si deduce:

∑t=0kαtE[∥∇f(xt)∥2]≤f(x0)−E[f(xk+1)]+LG22∑t=0kαt2.\sum_{t=0}^k \alpha_t E\left[\|\nabla f(x^t)\|^2\right] \leq f(x^0) - E\left[f(x^{k+1})\right] + \frac{L G^2}{2} \sum_{t=0}^k \alpha_t^2.

Poiché f(xk+1)≥f⋆f(x^{k+1}) \geq f^\star, il valore ottimale minimo, possiamo riscrivere:

∑t=0kαtE[∥∇f(xt)∥2]≤f(x0)−f⋆+LG22∑t=0kαt2.\sum_{t=0}^k \alpha_t E\left[\|\nabla f(x^t)\|^2\right] \leq f(x^0) - f^\star + \frac{L G^2}{2} \sum_{t=0}^k \alpha_t^2.

---

#### **Soluzione "output" zk+1z^{k+1}**

Consideriamo ora il valore atteso del gradiente in zk+1z^{k+1}, definito come una combinazione pesata degli iterati {xt}\{x^t\}:

E[∥∇f(zk+1)∥2]=∑t=0kE[∥∇f(xt)∥2]⋅P(zk+1=xt).E\left[\|\nabla f(z^{k+1})\|^2\right] = \sum_{t=0}^k E\left[\|\nabla f(x^t)\|^2\right] \cdot P(z^{k+1} = x^t).

Dato che P(zk+1=xt)=αt∑i=0kαiP(z^{k+1} = x^t) = \frac{\alpha_t}{\sum_{i=0}^k \alpha_i}, otteniamo:

E[∥∇f(zk+1)∥2]=1∑i=0kαi∑t=0kαtE[∥∇f(xt)∥2].E\left[\|\nabla f(z^{k+1})\|^2\right] = \frac{1}{\sum_{i=0}^k \alpha_i} \sum_{t=0}^k \alpha_t E\left[\|\nabla f(x^t)\|^2\right].

Sostituendo il limite superiore derivato in precedenza, otteniamo:

E[∥∇f(zk+1)∥2]≤1∑i=0kαi(f(x0)−f⋆+LG22∑t=0kαt2).E\left[\|\nabla f(z^{k+1})\|^2\right] \leq \frac{1}{\sum_{i=0}^k \alpha_i} \left(f(x^0) - f^\star + \frac{L G^2}{2} \sum_{t=0}^k \alpha_t^2\right).

---

#### **Limite per k→∞k \to \infty**

Poiché:

1. ∑t=0∞αt=∞\sum_{t=0}^\infty \alpha_t = \infty,
2. ∑t=0∞αt2<∞\sum_{t=0}^\infty \alpha_t^2 < \infty,

prendendo il limite per k→∞k \to \infty, si ottiene:

lim⁡k→∞E[∥∇f(zk+1)∥2]=0.\lim_{k \to \infty} E\left[\|\nabla f(z^{k+1})\|^2\right] = 0.

---

#### **Proposizione 4.15**

Sia {xk}\{x^k\} la sequenza generata dall'algoritmo SGD con una sequenza di passi {αk}\{\alpha_k\} tale che:

- ∑k=0∞αk=∞\sum_{k=0}^\infty \alpha_k = \infty,
- ∑k=0∞αk2<∞\sum_{k=0}^\infty \alpha_k^2 < \infty.

Allora:

lim inf⁡k→∞∥∇f(xk)∥=0.\liminf_{k \to \infty} \|\nabla f(x^k)\| = 0.

### Traduzione in Italiano

#### **Risultato della Proposizione 4.15**

La proposizione sopra afferma che, se la regola sui passi {αk}\{\alpha_k\} richiesta dalla Proposizione 4.14 è soddisfatta, possiamo ottenere un risultato di convergenza in stazionarietà, in valore atteso, per la sequenza {xk}\{x_k\}. Una regola sui passi che garantisce la convergenza in valore atteso ai punti stazionari per l'algoritmo SGD è, ad esempio:

αk=α0k+1.\alpha_k = \frac{\alpha_0}{k + 1}.

In pratica, i passi devono tendere a zero per garantire la convergenza, ma devono farlo "abbastanza lentamente" da consentire all'algoritmo di raggiungere un punto stazionario.

---

#### **Complessità dell'algoritmo**

La velocità di convergenza dell'SGD è inferiore rispetto a quella dei metodi a batch completo (GD), come osservabile nella **Tabella 3**. Il limite di complessità nel caso peggiore è peggiore per l'SGD rispetto al GD nei casi non convessi, convessi e fortemente convessi. In particolare, nel caso fortemente convesso, i tassi di convergenza sono **lineari** per GD contro **sottolineari** per SGD.

|**Caso**|**GD**|**SGD**|
|---|---|---|
|Non convesso (ff)|O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right)|O(1ϵ4)O\left(\frac{1}{\epsilon^4}\right)|
|Convesso (ff)|O(1ϵ)O\left(\frac{1}{\epsilon}\right)|O(1ϵ2)O\left(\frac{1}{\epsilon^2}\right)|
|Fortemente convesso (ff)|O(log⁡(1ϵ))O\left(\log\left(\frac{1}{\epsilon}\right)\right)|O(1ϵ)O\left(\frac{1}{\epsilon}\right)|

**Tabella 3:** Esempi di complessità per GD e SGD.

I valori nella tabella aiutano a visualizzare i trend; tuttavia, ricordiamo che i limiti sono validi asintoticamente, ovvero sono più accurati per piccoli valori di ϵ\epsilon.

---

#### **Osservazioni sul comportamento**

- **Accelerazione:** L'accelerazione non migliora il tasso di convergenza per SGD.
- **Costo per iterazione:** A differenza del batch GD, l'SGD non nasconde nei costanti della complessità temporale il numero NN dei termini sommati nella funzione obiettivo. Il costo per iterazione è quindi molto più basso rispetto al GD batch.

L'**efficienza del GD rispetto all'SGD** si osserva solo per valori molto piccoli di ϵ\epsilon, cioè quando è richiesta un'elevata accuratezza nella soluzione (vedi Figura 9). Questo è uno dei motivi principali per cui il **minibatch GD** (1<∣B∣=M≪N1 < |B| = M \ll N), rappresentando una via di mezzo tra batch e stochastic GD, è nella pratica l'approccio più efficace nelle applicazioni.
