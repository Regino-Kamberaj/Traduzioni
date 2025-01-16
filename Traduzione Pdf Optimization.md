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

Data una direzione di discesa dkd_k, ovvero una direzione che soddisfa:

∇f(xk)Tdk<0,\nabla f(x_k)^T d_k < 0,

il nostro obiettivo è trovare un passo αk\alpha_k lungo questa direzione da utilizzare nella regola di aggiornamento:

xk+1=xk+αkdk,x_{k+1} = x_k + \alpha_k d_k,

in modo tale che la funzione obiettivo decresca in modo appropriato.

#### Line Search Esatta

Un'idea potrebbe essere quella di scegliere il miglior passo possibile lungo la direzione, cioè quello che porta al minimo valore di ff. In questo caso, stiamo eseguendo una **line search esatta** lungo dkd_k, formalmente caratterizzata come segue:

αk∈arg⁡min⁡α>0ϕ(α)=f(xk+αdk),\alpha_k \in \arg\min_{\alpha > 0} \phi(\alpha) = f(x_k + \alpha d_k),

dove la funzione ϕ\phi della variabile scalare α\alpha descrive l'evoluzione della funzione obiettivo lungo la direzione di ricerca. Questa operazione è stata eseguita, ad esempio, nell'Esempio 4.3 ed è rappresentata nella Figura 4a.

#### Applicazione ai Problemi Quadratici Convessi

Questa strategia è generalmente fattibile per problemi di ottimizzazione quadratica strettamente convessi della forma:

min⁡xf(x)=12xTQx+cTx,Q≻0.\min_x f(x) = \frac{1}{2}x^T Qx + c^T x, \quad Q \succ 0.

Utilizzando lo sviluppo di Taylor di secondo ordine per f(xk+αdk)f(x_k + \alpha d_k) (che è esatto per funzioni quadratiche) e ricordando che ∇2f(xk)=Q\nabla^2 f(x_k) = Q, otteniamo:

ϕ(α)=f(xk+αdk)=f(xk)+α∇f(xk)Tdk+α22dkTQdk.\phi(\alpha) = f(x_k + \alpha d_k) = f(x_k) + \alpha \nabla f(x_k)^T d_k + \frac{\alpha^2}{2} d_k^T Q d_k.

Questa è una parabola convessa (il coefficiente quadratico dkTQdkd_k^T Q d_k è positivo grazie alla definitezza positiva di QQ). Il passo ottimale può essere calcolato annullando la derivata prima:

0=ϕ′(α)=∇f(xk)Tdk+αdkTQdk,0 = \phi'(\alpha) = \nabla f(x_k)^T d_k + \alpha d_k^T Q d_k,

che si risolve con:

αk=−∇f(xk)TdkdkTQdk.\alpha_k = -\frac{\nabla f(x_k)^T d_k}{d_k^T Q d_k}.

#### Limiti della Line Search Esatta

Tuttavia, eccetto per casi molto particolari come questo, le line search esatte devono essere evitate per due motivi principali:

1. **Costo computazionale:** Per una funzione generica ff, il minimizzatore di ϕ(α)\phi(\alpha) potrebbe non essere disponibile in forma chiusa, e trovarlo potrebbe richiedere l'uso di un risolutore, con un costo computazionale non trascurabile. Inoltre, la direzione dkd_k potrebbe non essere sufficientemente buona da giustificare un'esplorazione così precisa.
    
2. **Caso non convesso:** Nel caso non convesso, non possiamo nemmeno verificare se un passo sia globalmente ottimale per la direzione di ricerca.
    

---

### Line Search Approssimata

Queste considerazioni motivano l'interesse per le tecniche di **line search approssimate**. Questa classe di metodi per la selezione del passo si pone l'obiettivo di identificare un valore αk\alpha_k che garantisca una diminuzione della funzione obiettivo, ovvero:

f(xk+αkdk)<f(xk).f(x_k + \alpha_k d_k) < f(x_k).

Inoltre, come abbiamo visto nell'esempio precedente, è cruciale che il passo scelto soddisfi certe condizioni per garantire la convergenza e migliorare l'efficienza algoritmica. Nelle sezioni successive, esploreremo queste condizioni in dettaglio.
### Sufficiente Decremento e Condizione di Armijo

Nell'Esempio 4.2, la semplice decrescita della funzione obiettivo non è sufficiente a garantire la convergenza di un algoritmo di discesa. Gli approcci basati su **line search** mirano a identificare un passo αk\alpha_k che fornisca un **decremento sufficiente** della funzione obiettivo, ovvero un decremento significativo rispetto allo stato attuale della soluzione.

La condizione di decremento sufficiente più utilizzata è la **Condizione di Armijo**, che richiede:

f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk,f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k,

dove γ∈(0,1)\gamma \in (0, 1). In pratica, questa condizione chiede di selezionare un passo αk\alpha_k in modo che la funzione obiettivo decresca almeno quanto un modello lineare con una pendenza più dolce rispetto al modello tangente (vedi Figura 4b).

---

#### Analisi della Condizione di Armijo

- Il termine a sinistra ϕ(α)\phi(\alpha) rappresenta la funzione obiettivo lungo la direzione di ricerca dkd_k.
- Il termine f(xk)=ϕ(0)f(x_k) = \phi(0) è il valore corrente della funzione obiettivo.
- Per γ=1\gamma = 1, la parte destra rappresenta la retta tangente al grafico di ϕ(α)\phi(\alpha) in α=0\alpha = 0.
- Per valori di γ∈(0,1)\gamma \in (0, 1), otteniamo rette che passano per (0,ϕ(0))(0, \phi(0)) con una pendenza più dolce rispetto alla tangente.

Dato che dkd_k è una direzione di discesa (∇f(xk)Tdk<0\nabla f(x_k)^T d_k < 0), ϕ(α)\phi(\alpha) e la retta ϕ(0)+γα∇f(xk)Tdk\phi(0) + \gamma \alpha \nabla f(x_k)^T d_k avranno una tendenza discendente iniziale. Pertanto, per un dato valore di γ∈(0,1)\gamma \in (0, 1), la Condizione di Armijo richiede che il valore della funzione ϕ(α)\phi(\alpha) si trovi al di sotto della retta corrispondente.

---

### Ricerca del Passo mediante Backtracking

Per identificare operativamente un passo che soddisfi la condizione di decremento sufficiente, utilizziamo un algoritmo basato sul concetto di **backtracking**. L'idea è intuitiva:

1. Si assume un valore iniziale per il passo αk\alpha_k.
2. Si verifica se questo valore soddisfa la Condizione di Armijo: f(xk+αkdk)≤f(xk)+γαk∇f(xk)Tdk.f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k.
3. Se la condizione è soddisfatta, il passo viene accettato.
4. Altrimenti, si riduce il valore del passo moltiplicandolo per un fattore δ∈(0,1)\delta \in (0, 1) e si ripete il controllo.

---

### Algoritmo 1: Armijo Line Search

**Input:**

- xk∈Rnx_k \in \mathbb{R}^n, dk∈Rnd_k \in \mathbb{R}^n con ∇f(xk)Tdk<0\nabla f(x_k)^T d_k < 0,
- Δ0>0\Delta_0 > 0, γ∈(0,1)\gamma \in (0, 1), δ∈(0,1)\delta \in (0, 1).

**Procedura:**

1. Imposta α=Δ0\alpha = \Delta_0.
2. **Mentre** f(xk+αdk)>f(xk)+γα∇f(xk)Tdkf(x_k + \alpha d_k) > f(x_k) + \gamma \alpha \nabla f(x_k)^T d_k:
    - Aggiorna α=δα\alpha = \delta \alpha.
3. Imposta αk=α\alpha_k = \alpha.
4. **Restituisci** αk\alpha_k.

---

### Proprietà Teoriche dell'Algoritmo

**Proposizione 4.2.**  
Sia f:Rn→Rf : \mathbb{R}^n \to \mathbb{R} una funzione continuamente differenziabile. Siano xk∈Rnx_k \in \mathbb{R}^n, dk∈Rnd_k \in \mathbb{R}^n con ∇f(xk)Tdk<0\nabla f(x_k)^T d_k < 0, e γ∈(0,1)\gamma \in (0, 1), δ∈(0,1)\delta \in (0, 1), Δ0>0\Delta_0 > 0. Allora, l'algoritmo **Armijo Line Search** termina in un numero finito di iterazioni, fornendo un passo αk\alpha_k che soddisfa la condizione di Armijo. Inoltre, valgono le seguenti proprietà:

(a) αk=Δ0\alpha_k = \Delta_0, se il primo tentativo soddisfa la condizione di Armijo;  
(b) αk≤δΔ0\alpha_k \leq \delta \Delta_0 e il passo precedente αk/δ\alpha_k / \delta non soddisfa la condizione.

---

### Dimostrazione della Terminazione Finita

Assumiamo per assurdo che l'algoritmo non termini mai, cioè che la condizione di arresto non venga mai soddisfatta per alcun passo δjΔ0\delta^j \Delta_0, con j=0,1,…j = 0, 1, \dots. Questo implica che:

f(xk+δjΔ0dk)>f(xk)+γδjΔ0∇f(xk)Tdk.f(x_k + \delta^j \Delta_0 d_k) > f(x_k) + \gamma \delta^j \Delta_0 \nabla f(x_k)^T d_k.

Dividendo entrambi i membri per δjΔ0\delta^j \Delta_0, otteniamo:

f(xk+δjΔ0dk)−f(xk)δjΔ0>γ∇f(xk)Tdk.\frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} > \gamma \nabla f(x_k)^T d_k.

Poiché δ∈(0,1)\delta \in (0, 1), quando j→∞j \to \infty, abbiamo δjΔ0→0\delta^j \Delta_0 \to 0, e il termine a sinistra tende alla derivata direzionale di ff lungo dkd_k:

lim⁡j→∞f(xk+δjΔ0dk)−f(xk)δjΔ0=∇f(xk)Tdk.\lim_{j \to \infty} \frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} = \nabla f(x_k)^T d_k.

Otteniamo quindi:

∇f(xk)Tdk≥γ∇f(xk)Tdk.\nabla f(x_k)^T d_k \geq \gamma \nabla f(x_k)^T d_k.

Poiché (1−γ)(1 - \gamma) è positivo e ∇f(xk)Tdk<0\nabla f(x_k)^T d_k < 0, questa relazione è contraddittoria. Quindi, l'algoritmo deve terminare in un numero finito di iterazioni.

La seconda proprietà deriva direttamente dalla struttura dell'algoritmo: se il passo iniziale Δ0\Delta_0 non è accettabile, almeno un backtracking viene eseguito, e il passo accettato αk\alpha_k sarà il primo che soddisfa la condizione.