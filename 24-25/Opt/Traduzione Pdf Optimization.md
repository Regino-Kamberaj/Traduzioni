Dipartimento di Ingegneria dell’Informazione

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
    - 4.7 Metodi di Decomposizione
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

### Notazione:

- Indichiamo con $e \in \mathbb{R}^n$ il vettore di tutti uno nello spazio euclideo $n$-dimensionale.
- Con $e_i \in \mathbb{R}^n$ indichiamo l’$i$-esimo elemento della base canonica, ovvero il vettore con tutte le componenti a zero eccetto la $i$-esima pari a 1.
- Dati due vettori $u, v \in \mathbb{R}^n$, la notazione $u^T v$ rappresenta il prodotto scalare tra $u$ e $v$, ovvero $u^T v = \sum_{i=1}^n u_i v_i$.
- Indichiamo con $| \cdot |$ la funzione norma; se non specificato altrimenti, assumiamo implicitamente che sia considerata la norma euclidea (in tal caso $|x|_2 = x^T x$).
- Denotiamo con $\mathcal{S}_n \subset \mathbb{R}^{n \times n}$ l’insieme delle matrici quadrate simmetriche di dimensione $n \times n$.
- Data una matrice $A \in \mathcal{S}_n$ (di cui sappiamo che gli autovalori sono numeri reali), denotiamo con $\lambda_{\text{min}}(A)$ e $\lambda_{\text{max}}(A)$ rispettivamente il più piccolo e il più grande autovalore di $A$.

### Matrice definita/semidefinita positiva

**Definizione 1.1:** Una matrice $A \in \mathcal{S}_n$ è:

- *Semidefinita positiva*, denotata $A \succeq 0$, se $x^T A x \geq 0$ per ogni $x \in \mathbb{R}^n$;
- *Definita positiva*, denotata $A \succ 0$, se $x^T A x > 0$ per ogni $x \in \mathbb{R}^n, x \neq 0$.

**Proposizione 1.1:** Una matrice $A \in \mathcal{S}_n$ è *semidefinita positiva* se e solo se:
- Tutti gli autovalori di $A$ sono **non negativi**, cioè $\lambda_{\text{min}}(A) \geq 0$. 
Analogamente, $A$ è *definita positiva* se e solo se:
- Tutti gli autovalori di $A$ sono **strettamente positivi**, cioè $\lambda_{\text{min}}(A) > 0$.

**Proposizione 1.2:** Data $A \in \mathcal{S}_n, A \succeq 0$, per ogni $x \in \mathbb{R}^n$ abbiamo:

- $\lambda_{\text{min}}(A) |x|_2^2 \leq x^T A x \leq \lambda_{\text{max}}(A) |x|_2^2$;
- $\lambda_{\text{min}}(A) |x| \leq |A x| \leq \lambda_{\text{max}}(A) |x|$.

### Coercività della funzione

**Definizione 1.2:** Una funzione continua $f : \mathbb{R}^n \to \mathbb{R}$ si dice coerciva se $\lim_{k \to \infty} f(x_k) = +\infty$ per ogni sequenza $\{x_k\} \subseteq \mathbb{R}^n$ tale che $\lim_{k \to \infty} \|x_k\| = +\infty$.

**Proposizione 1.3:** Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione continua. Allora, $f$ è coerciva se e solo se tutti i suoi insiemi di livello sono compatti.

### Riepilogo derivate 

**Definizione 1.3. (Derivata Direzionale)** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che una funzione ha *derivata direzionale* $Df(x, d)$ in un punto $x \in \mathbb{R}^n$ lungo la direzione $d \in \mathbb{R}^n$ se:
- il limite $\lim_{t \to 0^+} \frac{f(x + td) - f(x)}{t} = Df(x, d)$ **esiste ed è finito**.

**Definizione 1.4. (Derivata Parziale)** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che una funzione ha *derivata parziale* $\frac{\partial f}{\partial x_j}(x)$ in un punto $x \in \mathbb{R}^n$ rispetto alla variabile $x_j$ se:
- $f$ ha una derivata direzionale lungo $e_j$ e  $Df(x, e_j) = \frac{\partial f (x)}{\partial x_j}$

**Definizione 1.5. (Gradiente)** Sia $f : \mathbb{R}^n \to \mathbb{R}$ e si supponga che $f$ ammetta in un punto $x$ la derivata parziale rispetto a ciascuna variabile $x_i$, con $i = 1, \dots, n$.
- Definiamo il *gradiente* $\nabla f(x)$ di $f$ in $x$ come il vettore dato da:
	$\nabla f(x) = \begin{pmatrix} \frac{\partial f (x)}{\partial x_1} \\ \vdots \\ \frac{\partial f (x)}{\partial x_n}\end{pmatrix}$

**Definizione 1.6. (Funzione continuamente differenziabile)** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che $f$ è *continuamente differenziabile* su $\mathbb{R}^n$, e lo denotiamo con $f \in C^1(\mathbb{R}^n)$, se:
- Il gradiente $\nabla f(x)$ **esiste** per ogni $x \in \mathbb{R}^n$
- E la funzione $\nabla f : \mathbb{R}^n \to \mathbb{R}^n$ è continua su $\mathbb{R}^n$

**Proposizione 1.4.** Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione continuamente differenziabile. Allora, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, si ha:

	$Df(x, d) = \nabla f(x)^T d$

**Definizione 1.7. (Matrice Jacobiana)** Sia $F : \mathbb{R}^n \to \mathbb{R}^m$ una funzione vettoriale **continua**. Diciamo che $F$ è **continuamente differenziabile** se ogni componente $F_i : \mathbb{R}^n \to \mathbb{R}$ è **continuamente differenziabile** e definiamo la *matrice Jacobiana* $J_F : \mathbb{R}^n \to \mathbb{R}^{m \times n}$ come

	$J_F(x) =\begin{pmatrix}\nabla F_1(x)^T \\\vdots \\\nabla F_m(x)^T\end{pmatrix}$

**Definizione 1.8. (Matrice Hessiana)** Sia $f : \mathbb{R}^n \to \mathbb{R}$, con $f \in C^1(\mathbb{R}^n)$. 
Supponiamo che, in un punto $x \in \mathbb{R}^n$, ogni componente $\nabla f(x)_i$ del gradiente **ammetta la derivata parziale** ==rispetto a ciascuna variabile== $x_j$, con $j = 1, \dots, n$.
Definiamo la *matrice Hessiana* $\nabla^2 f(x)$ di $f$ in $x$ come la matrice (simmetrica) data dalle **derivate seconde** di $f$, ossia:

	$\nabla^2 f(x) = \begin{pmatrix} \frac{\partial^2 f (x)}{\partial x_1^2} & \dots & \frac{\partial^2 f (x)}{\partial x_1 \partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial^2 f (x)}{\partial x_n \partial x_1} & \dots & \frac{\partial^2 f (x)}{\partial x_n^2} \end{pmatrix}$


**Definizione 1.11.** Sia $f : \mathbb{R}^n \to \mathbb{R}$.
Diciamo che $f$ è **due volte continuamente differenziabile** su $\mathbb{R}^n$, e lo denotiamo con $f \in C^2(\mathbb{R}^n)$, se:
- La matrice Hessiana $\nabla^2 f(x)$ **esiste per ogni** $x \in \mathbb{R}^n$
- La funzione $\nabla^2 f : \mathbb{R}^n \to \mathbb{R}^{n \times n}$ è **continua** su $\mathbb{R}^n$

Si noti che l'Hessiano può essere visto come la matrice Jacobiana del gradiente $\nabla f(x)$, ossia:	$\nabla^2 f(x) = J_{\nabla f}(x)$

**Proposizione 1.5.** Sia $f (x) = \frac{1}{2} x^T Qx + c^T x$, con $Q \in S^n$ e $x \in \mathbb{R}^n$. Allora si ha:
- $\nabla f (x) = Qx + c$;
- $\nabla^2 f (x) = Q$
##### Lipschitz-continuità e L-smoothness

**Definizione 1.9.** Sia $F : \mathbb{R}^n \to \mathbb{R}^m$. Diciamo che $f$ è *Lipschitz-continua* con costante $L$ se:
- Per ogni $x, y \in \mathbb{R}^n$, si ha: $\|F(x) - F(y)\| \leq L\|x - y\|$

**Definizione 1.10.** Sia $f : \mathbb{R}^n \to \mathbb{R}$, con $f \in C^1(\mathbb{R}^n)$. Diciamo che $f$ è *L-liscia* se:
- Il gradiente $\nabla f$ è una funzione **Lipschitz-continua** con costante di Lipschitz $L$, ossia se
	$\|\nabla f(x) - \nabla f(y)\| \leq L\|x - y\|$ per ogni $x, y \in \mathbb{R}^n$.

**Proposizione 1.8** (**Lemma di discesa**). Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione **L-liscia**. Allora, per ogni $x \in \mathbb{R}^n$ e per ogni $d \in \mathbb{R}^n$, si ha

	$f (x + d) \leq f (x) + \nabla f (x)^T d + \frac{L}{2} \|d\|^2$

##### Teorema del valor medio e Taylor

**Proposizione 1.6.** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Allora:
- (**Teorema del valor medio**) Se $f \in C^1 (\mathbb{R}^n)$, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, esiste $t \in (0,1)$ tale che $\xi = x + td$ allora:
	- $f (x + d) = f (x) + \nabla f (\xi)^T d$
	- inoltre $f (x + d) = f (x) + \nabla f (x)^T d + \beta (x, d)$  dove $\lim_{\|d\| \to 0} \frac{\beta (x, d)}{\|d\|} = 0$

- (**Taylor**) Se $f \in C^2 (\mathbb{R}^n)$, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, esiste $t \in (0,1)$ tale che $\xi = x + td$ e
	- $f (x + d) = f (x) + \nabla f (x)^T d + \frac{1}{2} d^T \nabla^2 f (\xi) d$
	- inoltre, $f (x + d) = f (x) + \nabla f (x)^T d + \frac{1}{2} d^T \nabla^2 f (x) d + \beta (x, d)$ dove $\lim_{\|d\| \to 0} \frac{\beta (x, d)}{\|d\|^2} = 0$

**Proposizione 1.7** (**Teorema del valor medio per gli integrali**). Sia $F : \mathbb{R}^n \to \mathbb{R}^m$ una funzione **continuamente differenziabile**. Allora, per ogni $x, y \in \mathbb{R}^n$, si ha

	$F (x) = F (y) + \int_0^1 J_F (y + t (x - y)) (x - y) dt$

### Convessità

**Definizione 1.12.** Diciamo che una funzione $f : \mathbb{R}^n \to \mathbb{R}$ è:
- **convessa** se, per ogni $x, y \in \mathbb{R}^n$ e $\lambda \in [0,1]$, si ha:

	  $f (\lambda x + (1 - \lambda) y) \leq \lambda f (x) + (1 - \lambda) f (y)$ (funzione sta sotto)

- **strettamente convessa** se, per ogni $x, y \in \mathbb{R}^n$ e $\lambda \in (0,1)$, si ha:
  
	$f (\lambda x + (1 - \lambda) y) < \lambda f (x) + (1 - \lambda) f (y)$

- **fortemente convessa** se esiste $\mu > 0$ tale che $f (x) - \mu \|x\|^2$ è una **funzione convessa**, ovvero $f (x) = g (x) + \mu \|x\|^2$ con $g$ funzione convessa.

**Proposizione 1.9.** Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione *fortemente convessa*. Allora $f$ è **coerciva** e **strettamente convessa**.

**Proposizione 1.10.** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Le seguenti proprietà valgono:
- Se  $f \in C^1 (\mathbb{R}^n)$, allora $f$ è **convessa** se e solo se:
	
	$f (y) \geq f (x) + \nabla f (x)^T (y - x) \quad \forall x, y \in \mathbb{R}^n$ (funzione sta sopra)
	
- Se $f \in C^2 (\mathbb{R}^n)$, allora $f$ è **convessa** se e solo se

	  $\nabla^2 f (x) \succeq 0 \quad \forall x \in \mathbb{R}^n$ (Hessiana semidefinita positiva)

  Inoltre, se $\nabla^2 f (x) \succ 0$ per ogni $x \in \mathbb{R}^n$, allora $f$ è **strettamente convessa**.

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

TBD (Per ora vedi Pdf notes_palchetti_2023)

## 4. Algoritmi di Ottimizzazione Non Vincolata

### 4.1 Metodi Iterativi di Ottimizzazione

#### Introduzione

Quando affrontiamo problemi di ottimizzazione non vincolata e non lineare della forma:
	$\min_{x \in \mathbb{R}^n} f(x)$

dove $f : \mathbb{R}^n \to \mathbb{R}$ è una funzione continuamente differenziabile, nella pratica si cerca di trovare soluzioni candidate ottimali che soddisfano la condizione di stazionarietà $\nabla f(x) = 0$. In **rari e fortunati casi**, gli zeri dei gradienti possono essere trovati analiticamente, ==risolvendo il problema in forma chiusa==.

In generale, tuttavia, non avremo accesso a formule esatte per risolvere il problema. Dobbiamo quindi affidarci ad algoritmi che costruiscono una soluzione attraverso un processo iterativo, cioè metodi che producono una sequenza di soluzioni ${x_k}$ che si avvicinano progressivamente a un punto stazionario.

Gli algoritmi di ottimizzazione iterativa sono generalmente caratterizzati da una regola di aggiornamento della forma:	$\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$, cioè il **nuovo punto** viene ottenuto ==partendo dalla soluzione corrente e spostandosi di un vettore di aggiornamento== $\mathbf{s}_k$.

L'algoritmo si arresta non appena ==la condizione di stazionarietà viene soddisfatta== in una delle iterazioni $\mathbf{x}_k$. Esistono diverse classi di algoritmi, ma le tre più rilevanti sono le seguenti (vedi Figura 3):

![[Pasted image 20250122224259.png]]

1. **Algoritmi basati sulla ricerca in direzione** (_Line search_): il vettore di aggiornamento è strutturato come $\mathbf{s}_k = \alpha_k \mathbf{d}_k$, dove $\mathbf{d}_k \in \mathbb{R}^n$ è una direzione nello spazio euclideo e $\alpha_k \in \mathbb{R}^+$ è uno scalare denominato passo (*stepsize*). In questi algoritmi, viene prima identificata una direzione di ricerca $\mathbf{d}_k$, e successivamente scelto un passo appropriato per stabilire la grandezza dello spostamento **lungo quella direzione**.
    
2. **Algoritmi basati sulla regione di fiducia**: il vettore di aggiornamento è definito come ==il miglior aggiornamento possibile== per un'approssimazione (modello) della funzione obiettivo **in una vicinanza della soluzione corrente**:
		
		$\mathbf{s}_k \in \arg\min_{x \in \Delta_k} m_k(x), \quad m_k(x) \approx f(x) \; \forall x \in \Delta_k, \; m_k(\mathbf{x}_k) = f(\mathbf{x}_k).$

	L'accettazione dell'aggiornamento e la variazione del raggio $\rho_k$ della regione di fiducia $\Delta_k$ dipendono dal **miglioramento della funzione obiettivo reale**:

	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) \ll 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$, e $\rho_{k+1} > \rho_k$.
	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) < 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{s}_k$, e $\rho_{k+1} = \rho_k$.
	- Se $f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k) \geq 0$, allora $\mathbf{x}_{k+1} = \mathbf{x}_k$, e $\rho_{k+1} < \rho_k$.

3. **Algoritmi di ricerca per schemi (pattern search)**: il vettore di aggiornamento ==è il migliore tra un insieme predefinito di soluzioni da verificare==:

	$\mathbf{s}_k \in \arg\min_{\mathbf{s}_{i,k}, i=1,\dots,N_k} f(\mathbf{x}_k + \mathbf{s}_{i,k})$

I metodi di ricerca per schemi vengono spesso considerati quando non si ha accesso **alle derivate** della funzione obiettivo. In questi casi, si parla di **metodi senza derivata** (o di ordine zero). Al contrario, i metodi di ricerca in direzione e quelli basati sulla regione di fiducia utilizzano solitamente ==informazioni di primo ordine (gradienti, $\nabla f$) e secondo ordine (Hessiane==, $\nabla^2 f$), e in questa prospettiva si parla rispettivamente di metodi **di primo ordine e di secondo ordine**.

Entreremo successivamente nei dettagli dei metodi basati su line search, nel mentre discuteremo le proprietà che vorremmo che la sequenza $\{x_k\}$ e le sequenze corrispondenti $\{f(x_k)\}$  e $\{\nabla f(x_k)\}$ abbiano, senza guardare il tipo di aggiornamento.

**In uno scenario ideale,** un algoritmo finisce in un punto stazionario dopo un numero finito di iterazioni, in altre parole per qualche $k^*$ tale che $\nabla f(x^{k^*}) = 0$ e la procedura finisce.
Quando un metodo è garantito che si comporta in questo modo, diremo che possiede **proprietà di convergenza finita**. Sfortunatamente, questa proprietà è ottenuta solo per pochi algoritmi di alcune classi di problemi. Le sequenze in generale **sono infinite**. Siamo quindi interessati a proprietà di convergenza su sequenze infinite. 

#### 4.1.1 Esistenza di Punti di Accumulazione

La prima proprietà fondamentale che un algoritmo deve garantire è che la sequenza che produce, o **almeno una parte di essa**, abbia una direzione precisa. In altre parole, **non** vorremmo che la sequenza $\{x_k\}$ divergesse completamente, ovvero che $\|x_k\| \to \infty$. Infatti, siamo interessati a ottenere una soluzione con valori finiti e definiti, da utilizzare in un sistema reale.

Questo requisito si traduce formalmente ==nella presenza di punti di accumulazione per la sequenza==. Ricordiamo che un punto di accumulazione di una sequenza è un punto limite di una *sotto-sequenza*, cioè $\bar{x}$ è un punto di accumulazione per $\{x_k\}$ se esiste una sotto-sequenza $K \subseteq \{0, 1, \dots\}$ tale che $x_k \to \bar{x}$ per $k \in K, \, k \to \infty$.

Garantire l’esistenza di **almeno** un punto di accumulazione è piuttosto semplice dal punto di vista algoritmico, con ipotesi molto deboli sul problema considerato, come affermato nella seguente proposizione.

---

**Proposizione 4.1.**  
Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione continua. Sia $x_0 \in \mathbb{R}^n$ e sia il sottoinsieme di livello $L_0 = \{x \in \mathbb{R}^n \, | \, f(x) \leq f(x_0)\}$ **compatto**. 
Supponiamo che la sequenza $\{x_k\}$, iniziando da $x_0$, sia tale che $\forall k, f(x_{k+1}) \leq f(x_k)$. 
Allora, la sequenza $\{x_k\}$ ammette punti di accumulazione, ognuno appartenente a $L_0$, e la sequenza $\{f(x_k)\}$ converge a un valore $\bar{f}$.

----

**Dimostrazione.**  
In base alle ipotesi, $f(x_{k+1}) \leq f(x_k)$ per ogni $k$. Per induzione, abbiamo che $f(x_k) \leq f(x_0)$ per ogni $k = 0, 1, \dots,$ il che implica che l’intera sequenza $\{x_k\}$ è contenuta nel sottoinsieme di livello $L_0$. Dalla **compattezza** di $L_0$, segue che $\{x_k\}$ ha punti di accumulazione, **tutti appartenenti** a $L_0$.

Inoltre, la sequenza $\{f(x_k)\}$ è *monotona decrescente* e quindi **ammette un limite** $\bar{f}$. Grazie alla limitatezza di $\{x_k\} \subseteq L_0$ e alla continuità di $f$, il valore di $\bar{f}$ è finito.

---

La condizione di compattezza sul sottoinsieme di livello iniziale è soddisfatta, ad esempio, se la funzione obiettivo è *coerciva*. D’altra parte, imporre la monotonicità della sequenza dei valori della funzione obiettivo è relativamente semplice dal punto di vista algoritmico: ci concentreremo su questo aspetto nelle sezioni successive.

Un risultato interessante della proposizione è che ==la sequenza dei valori di $f$ converge completamente==; di conseguenza, abbiamo $f(\bar{x}) = \bar{f}$ ​ **per qualsiasi punto di accumulazione** $\bar{x}$ (cioè, tutti i punti di accumulazione sono equivalenti in termini di valore della funzione obiettivo). In realtà, questa proprietà si verifica immediatamente ogni volta che garantiamo un comportamento monotono con una funzione limitata inferiormente.

Tuttavia, mentre l’esistenza di punti di accumulazione è un requisito minimo essenziale, non abbiamo garanzie che uno qualsiasi di questi punti **sia effettivamente significativo** per il problema che stiamo cercando di risolvere. Questo è l’aspetto su cui ci concentreremo nella prossima sezione.
#### 4.1.2 Convergenza verso la stazionarietà

Ragionevolmente, vorremmo che le (sotto)sequenze convergenti discusse nella sezione precedente raggiungano asintoticamente **la condizione di stazionarietà**. Sebbene questo aspetto sia concettualmente semplice, la sua caratterizzazione formale richiede attenzione. In particolare, la proprietà di stazionarietà può essere raggiunta in modi diversi, elencati e descritti di seguito in ordine decrescente di forza:

1. $\lim_{k \to \infty} x_k = \bar{x}$  con $\nabla f(\bar{x}) = 0$: **l'intera sequenza** converge a un punto limite che **è un punto stazionario**.
2. $\lim_{k \to \infty} \|\nabla f(x_k)\| = 0$ : l'**intera** sequenza dei gradienti tende a zero; per continuità della norma e di $\nabla f$, **tutti i punti di accumulazione** della sequenza $\{x_k\}$ **sono punti stazionari**.
3. $\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$ : i gradienti **tendono a zero** almeno **lungo una sottosequenza**; se $\{x_k\}$ non ha sottosequenze divergenti, ==almeno un punto di accumulazione è stazionario.==

Il significato di queste tre situazioni può essere meglio compreso attraverso il seguente esempio.

---
**Esempio 4.1.**  
Consideriamo la funzione di una variabile $f(x)$ con derivata (gradiente) data da:
$\nabla f(x) = (x - 1)(x - 2)$

4. **Caso 1:** La sequenza dei valori
	    $\{x_k\} = \{0.9, 0.99, 0.999, 0.9999, 0.99999, \dots\}$
    
    converge a l’unico limite $\bar{x} = 1$, che è un punto stazionario per $f$.
    
5. **Caso 2:** La sequenza dei valori
	    $\{x_k\} = \{0.9, 2.1, 0.99, 2.01, 0.999, 2.001, 0.9999, 2.0001, 0.99999, 2.00001, \dots\}$
    
    corrisponde alla sequenza dei gradienti:
	    $\{\nabla f(x_k)\} = \{0.11, 0.11, 0.0101, 0.0101, 0.001001,$
	     $0.001001, 0.00010001, 0.00010001, 0.0000100001, 0.0000100001, \dots\}$
    
    che chiaramente converge a zero. I due punti di accumulazione di $\{x_k\}$, 1 e 2, sono entrambi punti stazionari.
    
6. **Caso 3:** La sequenza dei valori
    
	    $\{x_k\} = \{0.9, 3.1, 0.99, 3.01, 0.999, 3.001, 0.9999, 3.0001, 0.99999, 3.00001, \dots\}$
    
	che corrisponde alla sequenza dei gradienti: 
		$\{\nabla f(x_k)\} = \{0.11, 2.31, 0.0101, 2.0301, 0.001001,$
		$2.003001, 0.00010001, 2.00030001, 0.0000100001, 2.0000300001, \dots\}$

	In questo caso, la sequenza $\{|\nabla f(x_k)|\}$ presenta due sotto-sequenze convergenti: una con limite 0 e l'altra con limite 2. Il limite inferiore della norma del gradiente è dunque 0, e esiste una sotto-sequenza di $\{x_k\}$ (quella che converge a 1) che tende a un punto stazionario.

---

Nella pratica, garantire la terza condizione  ($\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$) è sufficiente per scopi computazionali. Infatti, grazie alla continuità del gradiente, sappiamo che se $\lim \inf_{k \to \infty} \|\nabla f(x_k)\| = 0$, allora, per ogni $\epsilon > 0$, esiste un $k$ sufficientemente grande tale che $\|\nabla f(x_k)\| \leq \epsilon$. Questo è importante perché garantisce che, se utilizziamo una condizione di arresto basata su una soglia per la norma del gradiente, l'algoritmo si fermerà certamente in tempo finito, fornendoci una soluzione con il livello di accuratezza desiderato.

Garantire questo tipo di convergenza per la sequenza di soluzioni non è affatto banale; ad esempio, ==la semplice decrescita della funzione obiettivo non è sufficiente per garantire la convergenza ai punti stazionari==, nemmeno nel caso convesso, come dimostra il seguente esempio.

---

**Esempio 4.2.** Consideriamo il problema:

	$\min_{x \in \mathbb{R}} f(x) = \frac{1}{2}x^2$

dove la funzione obiettivo è continua e strettamente convessa, raggiungendo il valore minimo $f^\star = 0$ nell'unico ottimizzatore globale $x^\star = 0$.

Supponiamo ora di considerare il processo iterativo che parte da $x^0 = 2$ e segue la regola di aggiornamento:	$x^{k+1} = x^k - \alpha_k f'(x^k) = x^k - \alpha_k x^k$

dove il passo $\alpha_k$ è definito come: $\alpha_k = \frac{x^k - 1}{2x^k}$​.

In tal caso, la regola di aggiornamento diventa:	$x^{k+1} = \frac{x^k + 1}{2}$

Osserviamo che, per ogni $x^k \in (1, 2]$, abbiamo:

	$2 \geq \frac{x^k + 1}{2} \geq \frac{1 + 1}{2} = 1$,

cioè $x^{k+1}$ appartiene all'intervallo $(1, 2]$, e inoltre:

	$x^{k+1} = \frac{x^k + 1}{2} < x^k$,

Ricordando che $x^0 = 2$, per induzione abbiamo che $x^{k+1} < x_k$​ vale per l'intera sequenza $\{x_k\}$.

Pertanto, possiamo osservare che:

	$f(x^{k+1}) = \frac{1}{2}(x^{k+1})^2 < \frac{1}{2}(x^k)^2 = f(x^k)$

Abbiamo così definito una sequenza **strettamente decrescente** su una funzione fortemente convessa; tuttavia, l'intera sequenza è contenuta nell'intervallo $(1, 2]$ e quindi **non può convergere** all'unico punto stazionario 0: in realtà, converge a 1.

---

Concludiamo questa discussione evidenziando un'importante distinzione riguardo il tipo di proprietà di convergenza che possono essere associate a un algoritmo:

- **Convergenza Globale:** Si dice che le proprietà di convergenza di un algoritmo siano **globali** se valgono ==indipendentemente dalla soluzione iniziale scelta== per il processo iterativo.
- **Convergenza Locale:** Si dice che le proprietà di convergenza siano **locali** se valgono solo quando ==il punto di partenza è sufficientemente vicino a una delle soluzioni desiderate==.

Le proprietà di convergenza di tipo globale sono ovviamente preferibili. Questo è particolarmente vero poiché, nella pratica, non sappiamo **quanto grande** sia il "vicinato di convergenza" **né dove si trovi**, quando le proprietà di convergenza sono solo locali. Tuttavia, i risultati di convergenza locale sono talvolta di interesse, poiché possono essere dimostrate **proprietà migliori** per certi metodi ==quando si trovano **vicini** a una soluzione==.

#### 4.1.3 Efficienza dei Solver di Ottimizzazione

Nello studio degli algoritmi di ottimizzazione, l'interesse principale risiede nell'analisi delle proprietà di convergenza locale e globale verso i punti stazionari: è fondamentale garantire che producano effettivamente soluzioni candidate ottimali. Tuttavia, anche ==l'efficienza degli algoritmi è cruciale==, specialmente nei contesti su larga scala, dove i tempi di calcolo possono essere molto lunghi.

L'efficienza degli algoritmi di ottimizzazione è solitamente studiata in termini di due concetti principali: **tasso di convergenza** e **complessità**.
##### Tasso di convergenza

Il **tasso di convergenza** indica intuitivamente con quale rapidità la sequenza dei valori della funzione obiettivo $\{f(x_k)\}$ (o, equivalentemente, la sequenza degli iterati $\{x_k\}$ o dei gradienti $\{\|\nabla f(x_k)\|\}$) si avvicina al punto limite. Formalmente, possiamo distinguere i seguenti casi:

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
- **Sub-lineare:** Un tasso di convergenza sub-lineare è inefficiente: più l'algoritmo procede, meno progresso viene fatto, ovvero ==la riduzione del divario diventa progressivamente irrilevante==.
- **Lineare:** Un tasso lineare è accettabile: **a ogni iterazione**, viene coperta una percentuale fissa della distanza residua dal valore finale.
- **Superlineare:** Un tasso di convergenza superlineare è eccellente: per k grande, una singola iterazione è sufficiente **per ridurre l'errore di ordini di grandezza**.
##### Complessità

Un altro approccio molto popolare per misurare l'efficienza degli algoritmi di ottimizzazione si basa sulla **complessità**. Tuttavia, anche se gli algoritmi hanno tassi di convergenza asintotici eccellenti, la loro complessità computazionale deve essere considerata per valutarne l'**efficacia** nei contesti pratici.
**Quante iterazioni** (e possibilmente quante valutazioni della funzione e del gradiente) **sono necessarie per raggiungere un determinato livello di accuratezza** $\epsilon$?

---
Partiamo prima dalla definizione di **Notazione O**

**Definizione 4.2.** Date due funzioni $\phi$ e $g$, diciamo che $\phi(n) = O(g(n))$ se esistono una costante c > 0 e un indice $\bar{n}$ tali che:
	$\phi(n) \leq c \, g(n), \quad \forall n \geq n̄$

Da un certo punto in poi la funzione starà sotto una certa funzione.

---

Focalizzandoci sul numero di iterazioni come metrica di costo, possiamo definire quanto segue.

**Definizione 4.3.** Sia $\{x^k\}$ la sequenza generata da un metodo iterativo, con $f(x^k) \to f^\star$ Diciamo che l'algoritmo ha un *errore di iterazione* di $O(h(k))$ se:

	$f(x^k) - f^\star = O(h(k))$

equivalentemente, dato un livello di accuratezza $\epsilon$, l'algoritmo ha una *complessità di iterazione* di $O(q(\epsilon))$ se:

	$\min \{k \, | \, f(x^k) - f^\star \leq \epsilon\} = O(q(\epsilon))$

---

Invece di considerare il divario $f(x^k) - f^\star$, possiamo utilizzare la quantità $\|\nabla f(x^k)\|$, cioè la **distanza dalla stazionarietà**. Questa scelta è particolarmente utile per analizzare algoritmi in contesti non convessi, dove il gradiente viene spesso utilizzato come criterio di arresto.

**Il caso peggiore** sull'errore di iterazione ci fornisce una misura della dimensione dell'**errore** che possiamo aspettarci dopo ==un dato numero di iterazioni.== D'altro canto, il bound sulla complessità di iterazione ci offre **una stima del tempo necessario** affinché l'algoritmo produca ==una soluzione accettabile== nel caso peggiore.

Esiste una corrispondenza fra errore di iterazione e complessità d'iterazione: se un algoritmo ha un **errore di iterazione** $O(\frac{1}{k})$ e vogliamo ottenere una soluzione accurata **entro** $\epsilon$, cioè $f(x_k) - f^\star \leq \epsilon$, nel caso peggiore abbiamo:

	$f(x_k) - f^\star \leq \frac{C}{k}$.

Quindi, $\frac{C}{k} \leq \epsilon$, garantiamo che la soluzione è accettabile per ogni $k \geq \frac{C}{\epsilon}$. Concludiamo che il primo $k$ tale che $f(x_k) - f^\star \leq \epsilon$ è $O(\frac{1}{\epsilon})$, cioè la **complessità di iterazione** è: $O\left(\frac{1}{\epsilon}\right)$.

In modo analogo, se l'errore di iterazione è $O(\frac{1}{k^2})$, la complessità di iterazione diventa $O\left(\frac{1}{\sqrt{\epsilon}}\right)$.

---

Notare che una complessità $O\left(\frac{1}{\epsilon}\right)$ non è favorevole.
Consideriamo il significato pratico:
- Possiamo interpretare $\log\left(\frac{1}{\epsilon}\right)$ come il **numero di cifre decimali di accuratezza desiderate** Con una complessità $O\left(\frac{1}{\epsilon}\right)$, se servono **10 iterazioni** (da 1/0,1) per **una** cifra di accuratezza, potrebbero essere necessarie:
    - 100 iterazioni per 2 cifre,
    - 1000 iterazioni per 3 cifre,
    - e così via (il costo aumenta esponenzialmente).

Questo può essere messo in relazione con la velocità di convergenza:
- Per una complessità di iterazione di $O(\frac{1}{\epsilon})$ corrisponde un **Errore di Iterazione** $O(\frac{1}{k})$ che equivale a un tasso di convergenza **sublineare** (prendo i due errori di iterazione prima e dopo), come mostrato:

	$\lim_{k \to \infty} \frac{f(x_{k+1}) - f^\star}{f(x_k) - f^\star} = \lim_{k \to \infty} O ( \frac{k}{k+1}) = 1$.

- **Errore di Iterazione** $O(\rho^k)$ con $\rho < 1$: Questo porta a un **tasso di convergenza lineare** e una complessità di iterazione di $O(\log\left(\frac{1}{\epsilon}\right))$. In questo caso, il costo per aggiungere una nuova cifra di accuratezza cresce in modo **polinomiale**, risultando molto più favorevole rispetto al caso sublineare.

- Un errore del tipo $O(\rho^2)$, con $\rho < 1,$ porta a un tasso di convergenza **superlineare** e a una complessità di iterazione di $O(\log(\log(\frac{1}{\epsilon})))$. In questo caso, ==il costo per aggiungere una nuova cifra di accuratezza è **costante**==, il che rappresenta una proprietà altamente desiderabile.

**Tabella 1: Esempi di Tipi di Complessità d'iterazione**

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

Per algoritmi di questo tipo, ==è fondamentale scegliere con attenzione sia la direzione $d_k$ che il passo $\alpha_k$== per garantire le proprietà di convergenza.

Consideriamo ancora l'Esempio 4.2. In quel caso specifico, la sequenza $\{x^k\}$ è definita secondo una regola della forma: $x^{k+1} = x^k - \alpha_k \nabla f(x_k)$, dove la direzione di ricerca, $-\nabla f(x^k)$, è l'unica direzione di discesa in $x^k$. Il fallimento della convergenza è quindi attribuibile a una scelta errata del passo $\alpha_k$.

Vediamo ora un esempio in cui i problemi di convergenza sono chiaramente legati alla scelta della direzione.

---

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
2. Iterazione dispari:
	    $(x_1, y_1, z_1) = (\frac{y_0}{2}, y_0, z_0) = \left(\frac{1}{2}, 1, 1\right)$
3. Iterazione pari:
	    $(x_2, y_2, z_2) = (x_1, \frac{x_1}{2}, z_1) = \left(\frac{1}{2}, \frac{1}{4}, 1\right)$
4. Iterazione dispari:
	    $(x_3, y_3, z_3) = (\frac{y_2}{2}, y_2, z_2)= \left(\frac{1}{8}, \frac{1}{4}, 1\right)$
5. Iterazione pari:
	    $(x_4, y_4, z_4) = (x_3, \frac{x_3}{2}, z_2)= \left(\frac{1}{8}, \frac{1}{16}, 1\right)$
	    
e così via. La sequenza converge lentamente verso **(0, 0, 1)**.

La sequenza è costruita utilizzando una direzione di discesa e il miglior passo possibile a ogni iterazione, ed è chiaro che converge a (0, 0, 1). Tuttavia, il punto limite **non è un punto stazionario** per il problema, poiché: $\nabla f(0, 0, 1) = (0, 0, 2) \neq 0$

---

Questo esempio evidenzia che è fondamentale progettare con attenzione le regole di aggiornamento della forma: $x_{k+1} = x_k + \alpha_k d_k$, per i metodi di discesa. Nelle sezioni successive discuteremo questo problema in dettaglio.

#### 4.2.1 Line Search

Data una direzione di discesa $d_k$, ovvero una direzione che soddisfa:	$\nabla f(x_k)^T d_k < 0$ 
Il nostro obiettivo è trovare un **passo** $\alpha_k$ lungo questa direzione da utilizzare nella regola di aggiornamento: $x_{k+1} = x_k + \alpha_k d_k$, in modo tale ==che la funzione obiettivo decresca in modo appropriato.==

##### Line search esatta

Un'idea potrebbe essere quella di scegliere il **miglior passo possibile** lungo la direzione, cioè quello che ==porta al minimo valore== di f (sempre lungo la direzione scelta). In questo caso, stiamo eseguendo una **line search esatta** lungo $d_k$, formalmente caratterizzata come segue:

	$\alpha_k \in \arg\min_{\alpha > 0} \phi(\alpha) = f(x_k + \alpha d_k)$

dove la funzione $\phi$ della variabile scalare $\alpha$ descrive l'evoluzione della funzione obiettivo lungo la direzione di ricerca. Questa operazione è stata eseguita, ad esempio, nell'Esempio 4.3 ed è rappresentata nella Figura 4a.

![[Pasted image 20250209161303.png]]

Questa strategia è "generalmente fattibile" per problemi di **ottimizzazione quadratica** strettamente convessi della forma: $\min_x f(x) = \frac{1}{2}x^T Qx + c^T x, \quad Q \succ 0$.

Utilizzando lo sviluppo di Taylor di secondo ordine per $f(x_k + \alpha d_k)$ (che è esatto per funzioni quadratiche) e ricordando che $\nabla^2 f(x_k) = Q$, otteniamo:

	$\phi(\alpha) = f(x_k + \alpha d_k) = f(x_k) + \alpha \nabla f(x_k)^T d_k + \frac{\alpha^2}{2} d_k^T Q d_k$.

Questa è una parabola convessa (il coefficiente quadratico $d_k^T Q d_k$ è positivo grazie alla definitezza positiva di Q). 

Il passo ottimale può essere calcolato **annullando la derivata prima**:

	$0 = \phi'(\alpha) = \nabla f(x_k)^T d_k + \alpha d_k^T Q d_k$

che si risolve con: $\alpha_k = -\frac{\nabla f(x_k)^T d_k}{d_k^T Q d_k}$.

Tuttavia, eccetto per casi molto particolari come questo, le line search esatte devono essere evitate per due motivi principali:

1. **Costo computazionale:** Per una funzione generica f, il minimizzatore di $\phi(\alpha)$ potrebbe non essere disponibile in forma chiusa, e trovarlo potrebbe richiedere l'uso di un risolutore, ==con un costo computazionale non trascurabile==. Inoltre, la direzione $d_k$ potrebbe **non essere sufficientemente buona** da giustificare un'esplorazione così precisa.
    
2. **Caso non convesso:** Nel caso non convesso, non possiamo nemmeno verificare se un passo sia globalmente ottimale per la direzione di ricerca. (In quanto non sappiamo nemmeno se il passo ottenuto sia il migliore globalmente )
    
##### Line Search Approssimata

Queste considerazioni motivano l'interesse per le tecniche di **line search approssimate**. Questa classe di metodi per la selezione del passo si pone l'obiettivo di identificare un valore $\alpha_k$ che garantisca una ==diminuzione della funzione obiettivo==, ovvero un decremento significativo **rispetto allo stato attuale** della soluzione: $f(x_k + \alpha_k d_k) < f(x_k)$

La condizione di sufficiente decremento più utilizzata è la **Condizione di *Armijo***, che richiede:

	$f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, \space \text{con} \space \gamma \in (0, 1)$

In pratica, questa condizione chiede di selezionare un passo $\alpha_k$ in modo che la funzione obiettivo decresca ==almeno quanto un modello lineare== con una pendenza più "dolce" rispetto al modello tangente (vedi Figura 4b).

Analizzando i termini:
- Il termine a sinistra $\phi(\alpha)$ rappresenta ==la funzione obiettivo lungo la direzione di ricerca== $d_k$.
- Il termine $f(x_k) = \phi(0)$ è il valore corrente della funzione obiettivo.
- Il termine $\nabla f(x_k)^T d_k$, se guardiamo bene è la derivata di $\phi(\alpha)$, per $\alpha = 0$, per la regola della catena abbiamo $\phi'(\alpha) = \nabla f(x_k + \alpha d_k)^T d_k, \space \phi'(0) = \nabla f(x_k)^Td_k$  

Dunque, per $\gamma = 1$, la parte destra rappresenta **la retta tangente al grafico** di $\phi(\alpha)$ in $\alpha = 0$ Più in generale possiamo scrivere la condizione come: $\phi(\alpha) \leq \phi(0) + \gamma \phi'(0)\alpha$, che, per direzioni di discesa, rappresenta una ==linea con un trend iniziale di discesa==.

Per valori di $\gamma \in (0, 1)$, otteniamo rette che passano per $(0, \phi(0))$ con una pendenza più dolce rispetto alla tangente. Quindi la condizione di Armijo ci chiede di trovare **un passo** tale che la funzione $\phi(\alpha)$ ==si trovi sotto la linea risultante== (vedi figura 4b)

###### Ricerca del Passo mediante Backtracking

Per identificare **operativamente** un passo che soddisfi la condizione di decremento sufficiente, utilizziamo un algoritmo basato sul concetto di **backtracking**. 

L'idea è intuitiva:
1. Si assume un valore iniziale $\Delta_0$ per il passo $\alpha_k$.
2. Si verifica se questo valore soddisfa la Condizione di Armijo: 
	 $f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k$.
3. Se la condizione è soddisfatta, il passo viene accettato.
4. Altrimenti, si riduce il valore del passo moltiplicandolo per un fattore $\delta \in (0, 1)$ (*passo di backtrack*) e si ripete il controllo.

Andiamo a vedere quindi l'algoritmo:

---
**Algoritmo 1: Line search di Armijo:**

**Input:**
- $x_k \in \mathbb{R}^n, d_k \in \mathbb{R}^n \space \text{tc} \space \nabla f(x_k)^T d_k < 0$,
- $\Delta_0 > 0, \gamma \in (0, 1), \delta \in (0, 1)$.

**Procedura:**
5. Imposta $\alpha = \Delta_0$.
6. **While** $f(x_k + \alpha d_k) > f(x_k) + \gamma \alpha \nabla f(x_k)^T d_k$:
    - Aggiorna $\alpha = \delta \alpha$.
7. Imposta $\alpha_k = \alpha$.
8. **Restituisci** $\alpha_k$.

---

Algoritmo riassumibile dalla seguente formula: 
	$\alpha_k = max_{j=0,1,...} \{\delta^j\Delta_0 \space | \space \phi(\delta^j\Delta_0) \leq \phi(0) + \gamma \delta^j\Delta_0\phi'(0)\}$ con $\delta \in (0,1)$ e $\Delta_0 > 0$ 

---

Algoritmo che gode di alcune proprietà teoriche:

---

**Proposizione 4.2.**  
Sia $f: \mathbb{R}^n \to \mathbb{R}$ una funzione continuamente differenziabile. Siano $x_k \in \mathbb{R}^n, d_k \in \mathbb{R}^n \space \text{con} \space \nabla f(x_k)^T d_k < 0,\gamma \in (0, 1), \delta \in (0, 1), \Delta_0 > 0$. Allora, l'algoritmo **Line Search di Armijo** termina in ==un numero finito di iterazioni==, fornendo un passo $\alpha_k$ che soddisfa la condizione di Armijo. Inoltre, valgono le seguenti proprietà:

-  $\alpha_k = \Delta_0$, se il primo tentativo soddisfa la condizione di Armijo;  
-  $\alpha_k \leq \delta \Delta_0$ e $f(x^k + \frac{\alpha_k}{\delta}d_k) > f(x^k) + \gamma \frac{\alpha_k}{\delta}\nabla f(x^k)^Td_k$ 

---

**Dimostrazione.**
Assumiamo per assurdo che l'algoritmo non termini mai, cioè che la condizione di arresto non venga mai soddisfatta per alcun passo $\delta^j \Delta_0$, con j=0,1,…
Questo implica che: $f(x_k + \delta^j \Delta_0 d_k) > f(x_k) + \gamma \delta^j \Delta_0 \nabla f(x_k)^T d_k$.

Dividendo entrambi i membri per $\delta^j \Delta_0$, otteniamo:

	$\frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} > \gamma \nabla f(x_k)^T d_k$.

Poiché $\delta \in (0, 1)$, quando $j \to \infty$ (al limite), abbiamo $\delta^j \Delta_0 \to 0$, e il termine a sinistra tende alla derivata direzionale di $f$ lungo $d_k$:

	$\lim_{j \to \infty} \frac{f(x_k + \delta^j \Delta_0 d_k) - f(x_k)}{\delta^j \Delta_0} = \nabla f(x_k)^T d_k$

Otteniamo quindi:

	$\nabla f(x_k)^T d_k \geq \gamma \nabla f(x_k)^T d_k, => (1-\gamma)\nabla f(x^k)^Td_k \geq 0$ 
 
Poiché $(1 - \gamma)$ è positivo e $\nabla f(x_k)^T d_k < 0$ per ipotesi, questa relazione è contraddittoria. 

---

La seconda proprietà deriva direttamente dalla **struttura dell'algoritmo**: se il passo iniziale $\Delta_0$ non è accettabile, almeno un *backtracking* viene eseguito, e il passo accettato $\alpha_k$ ==sarà il primo che soddisfa la condizione==, mentre il secondo ultimo step tentato sarà $\frac{\alpha_k}{\delta}$ che **non soddisfa la condizione di Armijo**.

---

La logica della prima proprietà è che, riducendo ripetutamente il passo della stessa frazione, nel caso peggiore ad un certo punto arriveremo nell'intervallo iniziale dello stepsize che soddisfa la condizione, cosicchè la line search si ferma in tempo finito.
La seconda proprietà ci dice banalmente che, se non accettiamo il primo passo, otteniamo un passo riducendo il passo più grande che non soddisfa la condizione di Armijo.

#### 4.2.2 Direzioni gradient related

Come abbiamo visto nell'Esempio 4.3, e forse contrariamente all'intuizione, scegliere una direzione di discesa a ogni iterazione non è sufficiente per garantire la convergenza verso un punto stazionario. Nell'esempio, si osserva che il punto limite non stazionario viene avvicinato asintoticamente utilizzando direzioni che diventano **sempre meno di discesa**, tendendo a essere ortogonali al gradiente del punto limite.

Per evitare questo tipo di comportamento, richiediamo che la direzione di ricerca sia in qualche modo **legata al vettore gradiente**. Formalizziamo questa idea con la seguente definizione.

---
**Definizione 4.4: Direzioni Correlate al Gradiente**

Sia $\{x_k, d_k\}$ la sequenza generata da un algoritmo iterativo della forma:	$x_{k+1} = x_k + \alpha_k d_k$

Diciamo che la sequenza $\{d_k\}$ delle direzioni è **correlata al gradiente** rispetto a $\{x_k\}$ se esistono due costanti $c_1, c_2 > 0$ tali che, per ogni k=0,1,… valgano le seguenti condizioni:

1. $\|d_k\| \leq c_1 \|\nabla f(x_k)\|$
2. $\nabla f(x_k)^T d_k \leq -c_2 \|\nabla f(x_k)\|^2$

---

Interpretazione ora le due condizioni:
- **Prima condizione:** La grandezza della direzione di ricerca può essere molto grande, purché non sia infinitamente maggiore rispetto alla grandezza del gradiente. ==Inoltre, la direzione deve ridursi a zero quando il gradiente tende a zero.==
- **Seconda condizione:** Richiede che la **direzione di discesa selezionata** abbia una derivata direzionale non trascurabile rispetto alla derivata direzionale lungo il gradiente, e che ==si riduca a zero solo quando ci si avvicina a un punto stazionario==.

---

Denotiamo con $\theta(v_1, v_2)$ l'angolo tra due vettori $v_1$ e $v_2$. Combinando le due condizioni della Definizione 4.4, otteniamo:

	$\cos \theta(d_k, -\nabla f(x_k)) = \frac{-\nabla f(x_k)^T d_k}{\|d_k\| \|\nabla f(x_k)\|} \geq \frac{c_2 \|\nabla f(x^k)\|^2}{c_1 \|\nabla f(x_k)\|\|\nabla f(x_k)\|} = \frac{c_2}{c_1} > 0$

Questa relazione garantisce che l'angolo tra la **direzione di ricerca e il gradiente negativo** rimanga inferiore o uguale a $90^\circ$ e sia sempre maggiore di zero. In questo modo, evitiamo che ==le due direzioni diventino asintoticamente ortogonali==, come osservato nell'Esempio 4.3.

Quali sono quindi le direzioni gradient related?
Un esempio ovvio di direzione correlata al gradiente è il gradiente negativo stesso, $-\nabla f(x_k)$ che soddisfa le due condizioni con $c_1 = c_2 = 1$.

Un'altra _classe_ di direzioni correlate al gradiente è data da: $d_k = -H_k \nabla f(x_k)$,
dove $H_k$ è una **matrice simmetrica** con opportune proprietà. In particolare, $d_k$ è certamente una direzione di discesa se $H_k$ è **definita positiva**, poiché:
	
	$\nabla f(x_k)^T d_k = -\nabla f(x_k)^T H_k \nabla f(x_k) < 0$.

Tuttavia, la sola definitezza positiva di $H_k$ non è sufficiente a garantire la correlazione al gradiente. La proprietà può essere assicurata se imponiamo che la sequenza $\{H_k\}$ soddisfi la condizione di **autovalori limitati**, cioè esistano costanti $c_1, c_2$ con $0 < c_2 < c_1 < \infty$ tali che, per ogni $k = 0, 1, \dots$ : 	$c_2 \leq \lambda_{\text{min}}(H_k) \leq \lambda_{\text{max}}(H_k) \leq c_1.$

Sotto questa assunzione, possiamo dimostrare che per ogni k (Ricorda Prop 1.2 ):

1. $\|d_k\| = \|H_k \nabla f(x_k)\| \leq \lambda_{\text{max}}(H_k) \|\nabla f(x_k)\| \leq c_1 \|\nabla f(x_k)\|$, 
2. $\nabla f(x_k)^T d_k = -\nabla f(x_k)^T H_k \nabla f(x_k) \leq -\lambda_{\text{min}}(H_k) \|\nabla f(x_k)\|^2 \leq -c_2 \|\nabla f(x_k)\|^2$.

---

Questa condizione sarà particolarmente utile nella discussione di alcune classi importanti di algoritmi, dove la correlazione tra direzione e gradiente è fondamentale per garantire proprietà di convergenza e stabilità.
#### 4.2.3 Risultati di Convergenza

In questa sezione forniamo i risultati generali di convergenza per i metodi di discesa basati su **line search**. Cominciamo con il risultato di convergenza globale.

---
##### **Proposizione 4.3: Convergenza Globale**

Sia $f$ una funzione **continuamente differenziabile**, e sia $\{x_k, d_k\}$ la sequenza generata da un algoritmo iterativo della forma: $x_{k+1} = x_k + \alpha_k d_k$, supponendo che:
- il passo $\alpha_k$ sia ottenuto tramite **l'algoritmo di Armijo** (Algoritmo 1) per ogni $k$,
- la sequenza delle direzioni $\{d_k\}$ sia **correlata al gradiente** rispetto a $\{x_k\}$. 
- Inoltre, supponiamo che l'insieme di livello: $L_0 = \{x \in \mathbb{R}^n \, | \, f(x) \leq f(x_0)\}$ sia **compatto**. 

Allora, la sequenza $\{x_k\}$ ammette **punti di accumulazione**, e ==ogni punto di accumulazione $\bar{x}$ è un punto stazionario==, cioè: $\nabla f(\bar{x}) = 0$.

---

**Dimostrazione**
Per ogni $k = 0, 1, \dots$, poiché la condizione di Armijo è soddisfatta e ricordando la condizione di correlazione al gradiente, abbiamo:

	$f(x_{k+1}) = f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k \leq f(x_k) - \gamma c_2 \alpha_k \|\nabla f(x_k)\|^2 < f(x_k). \tag{5}$ (5)

La sequenza $\{f(x_k)\}$ è quindi **monotona decrescente** (tolgo infatti una quantità positiva) e, grazie alla compattezza di $L_0$ e alla Proposizione 4.1, la sequenza $\{x_k\}$ ammette punti limite, tutti appartenenti a $L_0$. Inoltre, $\{f(x_k)\}$ converge a un valore finito $f^*$, e abbiamo:

	$\lim_{k \to \infty} f(x_{k+1}) - f(x_k) = 0. \tag{6}$ (6)

Sia $\bar{x}$ uno di questi punti limite, cioè esiste $K \subseteq \{0, 1, \dots\}$ tale che:

	$\lim_{k \in K, \, k \to \infty} x_k = \bar{x}$

**Supponiamo per assurdo** che $\bar{x}$ non sia un punto stazionario, cioè che $\|\nabla f(\bar{x})\| = \nu > 0$. Riscrivendo l'equazione (5), otteniamo:

	$f(x_{k+1}) - f(x_k) \leq \gamma \alpha_k \nabla f(x_k)^T d_k \leq 0$

Prendendo il limite per $k \in K, \, k \to \infty$ e ricordando (6), abbiamo:

	$0 \leq \lim_{k \in K, \, k \to \infty} \gamma \alpha_k \nabla f(x_k)^T d_k \leq 0$

quindi (per i carabinieri):

	$\lim_{k \in K, \, k \to \infty} \alpha_k \nabla f(x_k)^T d_k = 0$

Dalla condizione di correlazione al gradiente, sappiamo che:

	$\nabla f(x_k)^T d_k \leq -c_2 \|\nabla f(x_k)\|^2$,

e quindi:

	$0 = \lim_{k \in K, \, k \to \infty} \alpha_k \nabla f(x_k)^T d_k \leq \lim_{k \in K, \, k \to \infty} -c_2 \alpha_k \|\nabla f(x_k)\|^2.$

Questo implica:

	$\lim_{k \in K, \, k \to \infty} \alpha_k \|\nabla f(x_k)\|^2 = 0. \tag{7}$ 

Grazie alla continuità di ∇f(x), abbiamo che, per $k \in K, \, k \to \infty$, vale:

	$\|\nabla f(x_k)\|^2 \to \|\nabla f(\bar{x})\|^2 = \nu^2 > 0$ 

Pertanto, deve necessariamente valere:

	$\lim_{k \in K, \, k \to \infty} \alpha_k = 0$

Ora, $\alpha_k \to 0$ **lungo la sottosequenza K** implica che esiste un $k̄ \in K$ tale che:

	$\alpha_k < \Delta_0, \quad \forall k \in K, \, k \geq k̄$ 

Secondo la Proposizione 4.2, abbiamo: 

	$f(x_k + \frac{\alpha_k}{\delta} d_k) > f(x_k) + \gamma \frac{\alpha_k}{\delta} \nabla f(x_k)^T d_k$ (7)

 per ogni $k \in K, k \geq \bar{k}$. 
 Riprendendo il discorso dal **teorema del valor medio**, per ogni k abbiamo:
	
	$f\left(x_k + \frac{\alpha_k}{\delta} d_k\right) = f(x_k) + \frac{\alpha_k}{\delta} \nabla f\left(x_k + \theta_k \frac{\alpha_k}{\delta} d_k\right)^T d_k \space \text{con} \space \theta_k \in (0, 1)$. 

Combinando questa espressione con l'equazione (7) (con un po' di semplificazioni), otteniamo per ogni $k \in K$:

	$\nabla f\left(x_k + \theta_k \frac{\alpha_k}{\delta} d_k\right)^T d_k > \gamma \nabla f(x_k)^T d_k$ (8)

Grazie alla continuità di ∇f(x), sappiamo che la sequenza $\{\nabla f(x_k)\}_K$ converge a $\nabla f(\bar{x})$ ed è quindi limitata. Esiste una costante $M>0$ tale che:

	$\|\nabla f(x_k)\| \leq M, \quad \forall k \in K$

Grazie alla condizione di correlazione al gradiente, segue che:

	$\|d_k\| \leq c_1 \|\nabla f(x_k)\| \leq c_1 M, \quad \forall k \in K$

Pertanto, la sequenza $\{d_k\}_K$ è limitata e ammette una sottosequenza $K_2 \subseteq K$ tale che:

	$\lim_{k \in K_2, k \to \infty} d_k = \bar{d}$.

Prendendo i limiti nell'equazione (8) per $k \in K_2, k \to \infty$, e ricordando che $\theta_k \in (0, 1)$ e $\alpha_k \to 0$, otteniamo:

	$\nabla f(\bar{x})^T \bar{d} \geq \gamma  \nabla f(\bar{x})^T \bar{d}$,

che implica:

	$(1 - \gamma)  \nabla f(\bar{x})^T \bar{d} \geq 0$

cioè:

	$\nabla f(\bar{x})^T \bar{d}\geq 0$

Tuttavia, dalla condizione di correlazione al gradiente e dall'assunzione che $\bar{x}$ non sia stazionario, sappiamo che:

$\nabla f(\bar{x})^T\bar{d} = \lim_{k \in K_2, k \to \infty} \nabla f(x_k)^T  d_k \leq \lim_{k \in K_2, k \to \infty} -c_2 \|\nabla f(x_k)\|^2 = -\nu^2 < 0.$

Questa è una contraddizione, completando la dimostrazione.

---
##### **Proposizione 4.4: Intervallo dei Passi Sufficientemente Piccoli**

Successivamente, forniamo ulteriori informazioni sulla condizione di Armijo e sull'algoritmo di ricerca della linea di backtracking, nel caso speciale in cui viene utilizzato in combinazione con le direzioni relative al gradiente e la funzione obiettivo ha gradienti continui di Lipschitz. Il primo risultato identifica un intervallo completo di stepsize sufficientemente piccolo che ==soddisfano la condizione di Armijo **in tutte le iterazioni**==

---

**Enunciato**
Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione _L-smooth_. Sia $\{x_k\}$ la sequenza generata da un algoritmo iterativo della forma: $x_{k+1} = x_k + \alpha_k d_k$, supponendo che la sequenza delle direzioni di ricerca $\{d_k\}$ sia _gradient related_. Allora, per ogni $k$, la condizione di Armijo  è soddisfatta per ogni passo $\alpha \in [0, \Delta_{\text{low}}]$, con: $\Delta_{\text{low}} = \frac{2 c_2 (1 - \gamma)}{L c_1^2}$.

---

Supponiamo che un passo $\alpha$ non soddisfi la condizione di Armijo, cioè:

	$f(x_k + \alpha d_k) > f(x_k) + \gamma \alpha \nabla f(x_k)^T d_k$

Dalla _L-smoothness_ di $f$, sappiamo anche che:
	
	$f(x_k + \alpha d_k) \leq f(x_k) + \alpha \nabla f(x_k)^T d_k + \frac{L \alpha^2}{2} \|d_k\|^2$

Combinando le due disuguaglianze, otteniamo:

	$\gamma \alpha \nabla f(x_k)^T d_k < \alpha \nabla f(x_k)^T d_k + \frac{L \alpha^2}{2} \|d_k\|^2$

Riordinando i termini:

	$(1 - \gamma) \alpha |\nabla f(x_k)^T d_k| < \frac{L \alpha^2}{2} \|d_k\|^2$

Dividendo entrambi i membri per $\alpha > 0$:

	$(1 - \gamma) |\nabla f(x_k)^T d_k| < \frac{L \alpha}{2} \|d_k\|^2$

Sfruttando la condizione di correlazione al gradiente, abbiamo:

	$|\nabla f(x_k)^T d_k| \geq c_2 \|\nabla f(x_k)\|^2, \quad \|d_k\|^2 \leq c_1^2 \|\nabla f(x_k)\|^2$

Sostituendo (stando attenti ai segni), otteniamo:

	$(1 - \gamma) c_2 \|\nabla f(x_k)\|^2 < \frac{L \alpha}{2} c_1^2 \|\nabla f(x_k)\|^2$

Semplificando $\|\nabla f(x_k)\|^2$, ricaviamo il limite superiore per $\alpha$:

	$\alpha < \frac{2 c_2 (1 - \gamma)}{L c_1^2}= \Delta_{\text{low}}$.

Questo conclude la dimostrazione.

---
##### **Proposizione 4.5: Numero Massimo di Backtrack**

Possiamo ora sfruttare il risultato di sopra per settare un bound sul numero di passi di backtrack necessari ad ogni iterazione per ottenere uno stepsize corretto.

---

**Enunciato:** Sotto le stesse ipotesi della Proposizione 4.4, supponiamo inoltre che, per ogni $k$, il passo $\alpha_k$ venga ottenuto utilizzando l'algoritmo di Armijo con un passo iniziale $\Delta_0 > 0$. Allora, a ogni iterazione $k$, il numero di **passi di backtracking** $j_k$ è limitato superiormente da:

	$j_k \leq j^* = \max\left(0, \lceil \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}}\right \rceil) \space \text{dove} \space \Delta_{\text{low}} = \frac{2c_2(1 - \gamma)}{L c_1^2}$
	
 Inoltre, il passo $\alpha_k$ è limitato da:

	$\alpha_k \geq \min\{\Delta_0, \delta \Delta_{\text{low}}\}$.

---

Dimostrazione. (**saltabile**)
Sia $j^*$ il più piccolo intero positivo tale che:

	$\delta^{j^*} \Delta_0 \leq \Delta_{\text{low}}$.

Secondo la Proposizione 4.4, il passo $\delta^{j^*}\Delta_0$ soddisfa la condizione di Armijo per ogni $k$. Quindi, dall'algoritmo di Armijo, abbiamo 	$j^∗.j_k \leq j^*$.  Per la definizione di $j^*$, vale anche:

	$\delta^{j^*} \leq  \frac{\Delta_{\text{low}}}{\Delta_0 }$,

e prendendo il logaritmo (in base $\delta$):

	$j^* \geq \log_{\delta} \frac{\Delta_{\text{low}}}{\Delta_0} = \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}}$,

quindi, essendo $j^*$ **il più piccolo intero** che soddisfa la disequazione di sopra vale:

	$j^* = \max\left(0, \lceil \log_{1/\delta} \frac{\Delta_0}{\Delta_{\text{low}}} \rceil \right)$

Ora consideriamo i due casi:

1. Se $\Delta_0 < \Delta_{\text{low}}$, non è necessario effettuare backtracking ($j_k = 0$), e abbiamo:
		$\alpha_k = \Delta_0$.

2. Altrimenti se $\Delta_0 > \Delta_{\text{low}}$, abbiamo: $j_k \leq j^* = \lceil \log_{1/\delta} \frac{\Delta_0}{\Delta{\text{low}}} \rceil \leq  \log_{1/\delta} \frac{\Delta_0}{\Delta{\text{low}}} +1$ e quindi: $\frac{1}{\delta^{j_k - 1}} \leq \frac{\Delta_0}{\Delta_{\text{low}}}$, cioè $\delta^{j_k-1} \geq \frac{\Delta_{\text{low}}}{\Delta_0}$ e finalmente $\Delta_{\text{low}} \leq \delta^{j_k}\Delta_0 = \alpha_k$ 

---

Un'interessante conseguenza dei risultati precedenti è che, se conoscessimo le quantità $L$, $c_1$, e $c_2$, e quindi $\Delta_{\text{low}}$, potremmo impostare direttamente il passo $\alpha_k = \Delta_{\text{low}}$. Questo garantirebbe sempre la soddisfazione della condizione di Armijo, oltre alla convergenza globale descritta nella Proposizione 4.3, **senza necessità di effettuare backtracking**. Inoltre, il risultato di complessità successivo sarebbe anch'esso garantito.

Questo giustifica il fatto che ==talvolta gli algoritmi di discesa utilizzano un passo costante==: se il valore scelto è inferiore a $\Delta_{\text{low}}$, si ottiene convergenza globale. Tuttavia, passi troppo piccoli riducono l'efficienza pratica degli algoritmi, dunque usare le line search è in pratica più conveniente, poiché consentono di provare passi più aggressivi senza compromettere le garanzie di convergenza.

##### **Proposizione 4.6: Complessità nel Caso Non Convesso**

Siamo pronti a dare l'ultimo risultato di questa sezione, osservando il bound di complessità peggiore nel caso non convesso.

---

**Enunciato** 
Sia $f: \mathbb{R}^n \to \mathbb{R}$ una funzione $L-smooth$. Sia $\{x_k\}$ la sequenza generata da un algoritmo iterativo della forma: 	$x_{k+1} = x_k + \alpha_k d_k$, supponendo che la sequenza delle direzioni di ricerca $\{d_k\}$ sia _gradient related_ e che il passo $\alpha_k$ venga calcolato tramite l'algoritmo di Armijo con un passo iniziale $\Delta_0 > \delta \Delta_{\text{low}}$. Inoltre, supponiamo che $f$ sia limitata inferiormente da un valore $f^*$. Allora, per ogni $\epsilon > 0$, sono necessarie al **massimo $k_{\text{max}}$ iterazioni** per produrre un iterata $x_k$ tale che: $\|\nabla f(x_k)\| \leq \epsilon$, dove:

	$k_{\text{max}} \leq \frac{f(x_0) - f^*}{\gamma c_2 \delta \Delta_{\text{low}} \epsilon^2} = O(\epsilon^{-2})$

Lo stesso limite di complessità $O(\epsilon^{-2})$ ==vale anche per il numero di valutazioni di funzione e gradiente==.

---

**Dimostrazione**
Poiché la condizione di Armijo è soddisfatta a ogni iterazione e grazie alla condizione di gradient related, abbiamo per ogni $k$:

	$f(x_{k+1}) - f(x_k) = f(x_k + \alpha_k d_k) - f(x_k)$
				$\leq \gamma \alpha_k \nabla f(x_k)^T d_k$
				$\leq -\gamma c_2 \alpha_k \|\nabla f(x_k)\|^2$
				$\leq -\gamma c_2 \delta \Delta_{\text{low}} \|\nabla f(x_k)\|^2$

L'ultima disuguaglianza deriva dalla Proposizione 4.5.
Supponiamo ora che, per le prime $k_\epsilon$ iterazioni, valga $\|\nabla f(x_k)\| > \epsilon$. Poiché $f$ è limitata inferiormente da $f^*$, possiamo scrivere:

	$f^* - f(x_0) \leq f(x_{k_\epsilon}) - f(x_0) = \sum_{k=0}^{k_\epsilon - 1} \big(f(x_{k+1}) - f(x_k)\big) \leq \sum_{k=0}^{k_\epsilon - 1} -\gamma c_2 \delta \Delta_{\text{low}} \|\nabla f(x_k)\|^2$.

Sostituendo il limite inferiore $\|\nabla f(x_k)\|^2 > \epsilon^2$:

	$f^* - f(x_0) \leq -k_\epsilon \gamma c_2 \delta \Delta_{\text{low}} \epsilon^2$

Riordinando i termini, otteniamo:

	$k_\epsilon \leq \frac{f(x_0) - f^*}{\gamma c_2 \delta \Delta_{\text{low}} \epsilon^2}$

Dato che ==il gradiente viene valutato **una volta per iterazione**== e che, dalla Proposizione 4.5, il numero massimo di backtracking è **costante** a ogni iterazione, lo stesso limite $O(\epsilon^{-2})$ ==si applica al numero di valutazioni della funzione e del gradiente.==

---

Conclundendo i metodi di discesa basati su line search con Armijo e direzioni gradient-related hanno nel caso non convesso e funzioni L-smooth, hanno nel caso peggiore un *iteration complexity* di $O(\frac{1}{\epsilon^2})$ (o equivalentemente un iteration error di $O(\frac{1}{\sqrt{k}})$). Sebbene questo risultato rappresenti il caso peggiore, dimostra che i metodi di discesa basati su line search sono praticabili anche per problemi complessi e non convessi.

##### **Proposizione 4.7: Limite per Metodi di Primo Ordine**

Questo risultato è significativo poiché il limite è noto per essere **ottimale** ==per i metodi di primo ordine.==

---

**Enunciato:** Nessun algoritmo di primo ordine può essere progettato con una complessità migliore di $O\left(\frac{1}{\epsilon^2}\right)$ per trovare un punto stazionario approssimato $\epsilon$-accurato di una funzione _L-smooth_.

---

Complessità migliori possono essere ottenute solo con ipotesi più forti, ad esempio quando la funzione obiettivo è **convessa** o, ancor meglio, **strettamente convessa**. Per questi casi particolari, le dimostrazioni devono sfruttare la definizione specifica delle regole di aggiornamento e i meccanismi dell'algoritmo. Tali casi verranno analizzati successivamente.

### 4.3 Metodo di Discesa del Gradiente

È ora semplice introdurre l'algoritmo archetipo per l'ottimizzazione non lineare: il **metodo di discesa del gradiente**. Questo famoso algoritmo è un metodo basato su line search della forma: $x_{k+1} = x_k + \alpha_k d_k$, dove:

1. **Direzione di ricerca:** La direzione è il **gradiente negativo**: $d_k = -\nabla f(x_k)$, che è, ovviamente, ==una direzione correlata al gradiente== con $c_1 = c_2 = 1$.
2. **Scelta del passo:** Il passo $\alpha_k$ è selezionato tramite la regola di Armijo.

---
##### **Algoritmo 2: Metodo di Discesa del Gradiente**

1. **Input:** $x_0 \in \mathbb{R}^n$
2. Inizializza $k = 0$.
3. **Mentre** $\|\nabla f(x_k)\| \neq 0$:  
    a. Imposta $d_k= -\nabla f(x_k)$.  
    b. Calcola $\alpha_k$ lungo $d_k$ usando la line search di Armijo (Algoritmo 1).  
    c. Aggiorna $x_{k+1} = x_k + \alpha_k d_k$.  
    d. Incrementa $k = k + 1$.

---

Poiché l'algoritmo soddisfa tutti i criteri analizzati nelle sezioni 4.2.1 e 4.2.2, possiamo applicare direttamente le proposizioni appena viste per affermare:
- **Convergenza globale:** L'algoritmo converge verso un punto stazionario in contesti non convessi. (Proposizione 4.3)
- **Complessità iterativa:** La complessità iterativa nel caso peggiore è $O\left(\frac{1}{\epsilon^2}\right)$, ==ottimale per i metodi di primo ordine==.(Proposizione 4.6)
- **Valutazioni del gradiente e della funzione:** Poiché ogni iterazione richiede ==una sola valutazione del gradiente== e il numero di passi di backtracking è ==limitato da una quantità costante== (Proposizione 4.5), la complessità (nel caso peggiore) per le **valutazioni della funzione** è anch'essa $O\left(\frac{1}{\epsilon^2}\right)$.

##### **Proposizione 4.8: Convergenza nel Caso Convesso**

Analizziamo ora il **caso convesso** assumendo un passo costante $\alpha_k = \frac{1}{L}$ a ogni iterazione. Sappiamo, dalla Proposizione 4.4 (con $\gamma = 0.5$), che questo passo ==soddisfa sempre la condizione di Armijo== e sempre per Armijo conduce a risultati di convergenza globale.

---

**Enunciato:** Sia $f$ una funzione _L-smooth_ e **convessa**, e sia $\{x_k\}$ la sequenza generata dall'algoritmo di discesa del gradiente con passo costante $\alpha_k = \frac{1}{L}$.
Supponiamo che $f^*$ sia il valore ottimale di $f$ e che $x^*$ sia un minimizzatore di $f$, cioè $f(x^*) = f^*$. Allora:

	$f(x_k) - f^* \leq \frac{L \|x_0 - x^*\|^2}{2k}$

Ovvero, l'algoritmo ha un **errore d'iterazione** di $O(\frac{1}{k})$ e una **complessità di iterazione** di $O(\frac{1}{\epsilon})$ 

---

**Dimostrazione.**

Dalla **_continuità Lipschitziana_** (Proposizione 1.8) del gradiente $\nabla f(x)$ e considerando $x_{k+1} = x_k + \alpha_k d_k$, abbiamo che:

	$f(x_{k+1}) \leq f(x_k) + \alpha_k \nabla f(x_k)^T d_k + \frac{\alpha_k^2 L}{2} \|d_k\|^2$.

Sostituendo $d_k = -\nabla f(x_k)$ e $\alpha_k = \frac{1}{L}$:

	$f(x_{k+1}) \leq f(x_k) - \frac{1}{L} \|\nabla f(x_k)\|^2 + \frac{1}{2L^2} L \|\nabla f(x_k)\|^2$

Semplificando:

	$f(x_{k+1}) \leq f(x_k) - \frac{1}{2L} \|\nabla f(x_k)\|^2. \tag{9}$ (9)

Dalla **convessità** di $f$ (Proposizione 1.10), possiamo scrivere:

	$f(x^*) \geq f(x_k) + \nabla f(x_k)^T (x^* - x_k)$

Riordinando:

	$f(x_k) \leq f(x^*) + \nabla f(x_k)^T (x_k - x^*)$.

Combinando la relazione sopra con l'equazione (9):

	$f(x_{k+1}) \leq f(x^*) + \nabla f(x_k)^T (x_k - x^*) - \frac{1}{2L} \|\nabla f(x_k)\|^2$

Da questa, possiamo ottenere:

	$f(x_{k+1}) - f(x^*) \leq \frac{L}{2} (\frac{2}{L} \nabla f(x_k)^T (x_k - x^*) - \frac{1}{L^2} \|\nabla f(x_k)\|^2)$
				$= \frac{L}{2} (\frac{2}{L} \nabla f(x_k)^T (x_k - x^*) - \frac{1}{L^2} \|\nabla f(x_k)\|^2 + \|(x_k - x^*)\|^2 - \|(x_k - x^*)\|^2)$

Utilizziamo **l'identità vettoriale** $\|a\|^2 + \|b\|^2 - 2a^T b = \|a - b\|^2$, per riscrivere:

	$\frac{1}{L^2} \|\nabla f(x_k)\|^2 - \frac{2}{L} \nabla f(x_k)^T (x_k - x^*) + \|x_k - x^*\|^2 = \|x_k - x^* - \frac{1}{L}\nabla f(x_k)\|^2$

Pertanto, abbiamo:

	$f(x_{k+1}) - f(x^*) \leq \frac{L}{2}( - \|x_{k} - x^* - \frac{1}{L}\nabla f(x_k) \|^2 + \|x_k - x^*\|^2)$
				$= \frac{L}{2}( - \|x_{k+1} - x^*\|^2 + \|x_k - x^*\|^2)$

**Sommiamo entrambi i membri su** $t = 0, \dots, k$ (e con un po' di passaggi risulta):

	$\sum_{t=0}^k \big(f(x_{t+1}) - f(x^*)\big) \leq \frac{L}{2} \big(\|x_0 - x^*\|^2 - \|x_{k+1} - x^*\|^2\big) \leq \frac{L}{2} \|x^0-x^*\|^2$

Poiché $\{f(x_k)\}$ è decrescente (tolgo una quantità negativa), vale $f(x_{t+1}) \geq f(x_{k+1})$ per ogni $t = 0, \dots, k$, e quindi:

	$(k+1) \big(f(x_{k+1}) - f(x^*)\big) \leq \frac{L}{2} \|x_0 - x^*\|^2$.

Dividendo per $(k+1)$, otteniamo:

	$f(x_{k+1}) - f(x^*) \leq \frac{L}{2(k+1)} \|x_0 - x^*\|^2$.

Questo rappresenta un miglioramento significativo rispetto al caso non convesso, dove la complessità è $O\left(\frac{1}{\epsilon^2}\right)$. La dipendenza lineare da $k$ o $\frac{1}{\epsilon}$ è una caratteristica fondamentale dei metodi di primo ordine applicati a funzioni **convesse** *lisce*. Anche se questo rate ==non è ottimale==, infatti sublineare, per i metodi del primo ordine nel caso convesso. Discuteremo questo aspetto successivamente.

##### **Proposizione 4.9: Convergenza nel caso fortemente convesso**

---

**Enunciato:** Sia $f$ una funzione _L-smooth_ e **_fortemente convessa_**. Per ogni $x^0 \in \mathbb{R}^n$, l'intera sequenza $\{x^k\}$ prodotta dal metodo **di discesa del gradiente** con $\alpha_k = \frac{1}{L}$ per ogni $k$, converge al'**unico punto di minimo globale** $x^*$ di $f$ con un ==tasso di convergenza lineare==. 
(complessità di $O(log{\frac{1}{\epsilon}})$ a cui corrisponde una *iteration error* di $O(\frac{1}{2})^k)$)

---

Possiamo vedere che c'è una differenza significativa di performance quando andiamo verso problemi fortemente convessi, come qui il tasso di convergenza è totalmente superiore.

### 4.4 Metodi del Gradiente con Momento

Il semplice metodo di discesa del gradiente non è particolarmente efficiente in teoria (tasso di convergenza comunque sublineare) e, in pratica, risulta spesso poco performante. Per questo motivo, si studiano approcci che mirano a migliorare la velocità del metodo di discesa del gradiente.

Iniziamo con metodi di primo ordine che sfruttano ==informazioni dalle iterazioni precedenti== per determinare la **direzione di ricerca** $d_k$ e **il passo** $\alpha_k$ nell'iterazione corrente.

Questi metodi, noti come **metodi del gradiente con momento**, sono descritti dalla seguente regola di aggiornamento generica:

	$x_{k+1} = x_k - \alpha_k \nabla f(x_k) + \beta_k (x_k - x_{k-1})$ (10)

dove: 
- $\alpha_k > 0$ è il **passo**,
- $\beta_k > 0$ è il *peso del momento*.

L'idea alla base di questo aggiornamento è che ==la direzione dell'ultima iterazione sia probabilmente una buona direzione di ricerca anche per quella corrente==. Ripetere parzialmente il **passo precedente** ha l'effetto di **controllare le oscillazioni** e **fornire accelerazione** nelle regioni **di bassa curvatura**. Questa strategia sfrutta solo informazioni già disponibili, ==senza richiedere ulteriori valutazioni della funzione==, rendendola particolarmente attraente per problemi su larga scala.

I metodi del gradiente con momento più noti e importanti sono:
- **Metodo della palla pesante (Heavy-ball method);**
- **Metodi del gradiente coniugato (Conjugate gradient methods).**

#### 4.4.1 Metodo della Palla Pesante (Heavy-ball Method)

Il **metodo della palla pesante** è descritto direttamente dalla regola di aggiornamento (10) ed è specificato dalla seguente regola in due passi:

	$\begin{cases} &y_k = x_k - \alpha_k \nabla f(x_k), \\ &x_{k+1} = y_k + \beta_k (x_k - x_{k-1}), \end{cases}$

dove:
- $\alpha_k$ e $\beta_k$ sono tipicamente fissati a valori positivi.

In linea di principio, i valori dei parametri dovrebbero essere scelti in base alle proprietà della funzione obiettivo (ad esempio, utilizzando la costante di *Lipschitz* del gradiente o la costante di forte convessità). Tuttavia, nella pratica ==queste informazioni non sono spesso accessibili==, quindi:
- $\alpha_k$ può essere scelto tramite una **line search**,
- $\beta_k$ viene spesso impostato a un valore "ragionevole" predefinito.

Per il metodo della palla pesante, i risultati di **convergenza locale** sono stati dimostrati **nel caso convesso**. In particolare, nel caso di **funzioni quadratiche strettamente convesse**, i valori ottimali dei parametri $\alpha_k$ e $\beta_k$ possono essere calcolati in forma chiusa.
Con questa scelta ottimale dei parametri, si ottiene un **tasso di convergenza lineare locale** ==con costanti migliori rispetto al metodo di discesa del gradiente standard== (occhio però è locale!!). Questo risultato può essere generalizzato sotto ipotesi di doppia continuità e differenziabilità, gradiente _lipschitz-continuo_ e convessità forte.

Sebbene il **metodo della palla pesante** abbia dimostrato buone proprietà di accelerazione in diversi contesti, è stato mostrato con diversi esempi che il metodo ==potrebbe non convergere anche sotto forti assunzioni di regolarità==. Inoltre la convergenza del metodo nel caso non convesso rimane un problema aperto, in parte perché la struttura dell'algoritmo non rientra nel quadro analizzato nella Sezione 4.2.2 (ovvero $d_k$ **non è una direzione gradient-related**).

Il metodo della palla pesante è spesso spiegato tramite un'analogia fisica, sebbene non completamente accurata:
- Il **vettore delle variabili** può essere visto come una particella che si muove nello spazio euclideo.
- La particella tende naturalmente a **preservare la sua traiettoria** corrente ma viene **deviata dall'accelerazione** (il gradiente) prodotta da una forza.

In questo contesto, l'aggiornamento del momento può essere definito dalla seguente coppia di equazioni:

	$\begin{cases} v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k),\\ x_{k+1} = x_k + v_{k+1} \\ v_k = x_k - x_{k-1} \end{cases}$

Qui:
- Il vettore di aggiornamento $v_k$ rappresenta un **termine di velocità**, calcolato come una media decrescente esponenziale dei gradienti negativi passati.
- I gradienti modificano la **velocità della particella**, piuttosto che direttamente la sua posizione.
- Il movimento è quindi effettuato in base alla **velocità calcolata nella posizione corrente**.
##### Metodo del Gradiente Accelerato di Nesterov

Il **metodo di Nesterov Accelerated Gradient (NAG)** può essere visto come una variante del metodo della palla pesante. La regola di aggiornamento dell'algoritmo di Nesterov è data da:

	$\begin{cases}v_{k+1} = \beta_k v_k - \alpha_k \nabla f(x_k + \beta_k v_k), \\ x_{k+1} = x_k + v_{k+1} \end{cases}$

L'unica differenza rispetto al metodo della palla pesante risiede nel fatto che:
- Il **gradiente** è calcolato nel punto che sarebbe ottenuto ==ripetendo l'ultimo movimento== ($x_k + \beta_k v_k$), piuttosto che nel punto corrente $x_k$.

Le iterazioni sono essenzialmente composte da due fasi (in successione):
1. **Passo puro di momento** (senza influenza del gradiente).
2. **Passo puro di discesa del gradiente** (calcolato nel punto ottenuto con il passo di momento).

La regola di aggiornamento può essere riscritta in forma equivalente come:

	$\begin{cases}y_k = x_k - \alpha_k \nabla f(x_k), \\ x_{k+1} = y_k + \beta_k (y_k - y_{k-1}). \end{cases}$

- Il passo $\alpha_k$ può essere calcolato tramite una **line search di Armijo**.
- Il parametro del momento $\beta_k$ segue uno schema definito a priori.

![[Pasted image 20250210215505.png]]

---

**Proposizione 4.10**
Sia $f$ una funzione _L-smooth_ e convessa e sia $\{x_k\}$ la sequenza prodotta con il **metodo del gradiente accelerato di Nesterov**. Supponiamo che $f^*$ sia il valore ottimale di $f$. Allora:

	$f(x_k) - f^* = O\left(\frac{1}{k^2}\right)$,

ovvero, l'algoritmo ha un **errore iterativo** di $O\left(\frac{1}{k^2}\right)$ e una **complessità iterativa** di $O\left(\frac{1}{\sqrt{\epsilon}}\right)$ Questi bound sono stretti per il caso di metodi del primo ordine su funzioni convesse.

---

Questo risultato è significativo poiché il limite di complessità $O\left(\frac{1}{\sqrt{\epsilon}}\right)$ è stato dimostrato essere **ottimale** per i metodi di primo ordine: ==utilizzando solo informazioni sui gradienti, non è possibile ottenere complessità migliori==.
Tuttavia, il tasso di convergenza rimane **sub-lineare**, anche se significativamente più veloce rispetto al metodo di discesa del gradiente standard.

Nel caso di funzioni **fortemente convesse**, il metodo del gradiente accelerato ottiene la stessa complessità iterativa e tasso di convergenza del metodo di discesa del gradiente, cioè $O(\rho^k)$. Tuttavia, il valore di $\rho$ è **più piccolo** rispetto a quello della discesa del gradiente, indicando un tasso di **convergenza lineare più rapido**.

#### 4.4.2 Metodi del Gradiente Coniugato

I **metodi del gradiente coniugato** sono descritti dalle seguenti regole di aggiornamento:

	$x_{k+1} = x_k + \alpha_k d_k, \space\space   d_{k+1} = -\nabla f(x_{k+1}) + \beta_{k+1} d_k$ (12)

dove:
- $\alpha_k$ è calcolato tramite una **line search**,
- $\beta_k$ è ottenuto secondo una delle seguenti regole:
	- **Fletcher-Reeves**:
	    $\beta_{k+1} = \frac{\|\nabla f(x_{k+1})\|^2}{\|\nabla f(x_k)\|^2}$

	- **Polak-Ribiére**:
        $\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{\|\nabla f(x_k)\|^2}$
        
	-  **Hestenes-Stiefel**:    
		$\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{d_k^T (\nabla f(x_{k+1}) - \nabla f(x_k))}$
		
	- **Dai-Yuan**:
		$\beta_{k+1} = \frac{\|\nabla f(x_{k+1})\|^2}{-d_k^T \nabla f(x_k)}$
		
	-  **Liu-Storey**: 
	    $\beta_{k+1} = \frac{\nabla f(x_{k+1})^T (\nabla f(x_{k+1}) - \nabla f(x_k))}{-d_k^T \nabla f(x_k)}$

---

Tutte le regole sopra elencate richiedono calcoli semplici basati su quantità già calcolate nel metodo di discesa del gradiente di base. Pertanto, il costo aggiuntivo per la costruzione della direzione $d_{k+1}$ è trascurabile nella pratica.

L'aggiornamento nei metodi del gradiente coniugato può essere riscritto come:

	$x_{k+1} = x_k + \alpha_k (-\nabla f(x_k) + \beta_k d_{k-1})$

che equivale a:

	$x_{k+1} = x_k - \alpha_k( \nabla f(x_k) + \beta_k \frac{x_k - x_{k-1}}{\alpha_{k-1}})$

Questo è esattamente un **metodo del gradiente con momento**, secondo la definizione:

	$x_{k+1} = x_k - \alpha_k \nabla f(x_k) + \beta_k^* (x_k - x_{k-1})$

dove: $\beta_k^* = \frac{\alpha_k}{\alpha_{k-1}}\beta_k$ 

Quindi può essere visto come un metodo del gradiente con momentum secondo la definizione (10).
Sebbene, diversamente da heavy-ball,, il metodo del gradiente coniugato segua la regola di aggiornamento di line search $x_{k+1} = x_k + \alpha_k d_k$, dove $\alpha_k$ è calcolato tramite una **line search** lungo la direzione $d_k$, non possiamo garantire in generale che $d_k$ sia nè una **direzione di discesa**, né una **direzione correlata al gradiente**.
Di conseguenza, i risultati di convergenza descritti nella Sezione 4.2.2 **non sono immediatamente applicabili.**

Per recuperare le garanzie di convergenza, una strategia semplice consiste nell'introduzione di una **salvaguardia** all'interno del metodo:

1. **Verifica delle condizioni correlate al gradiente (ad ogni iterazione):** Date le due costanti $c_1$ e $c_2$ se la direzione $d_k$ soddisfa le condizioni correlate al gradiente, il metodo del gradiente coniugato può procedere normalmente con una **line search di Armijo**.
2. **Restart:** In caso contrario, l'algoritmo viene "riavviato" utilizzando una pura iterazione di discesa del gradiente.

Questa modifica permette di applicare immediatamente i risultati di convergenza e complessità delle Proposizioni 4.3 e 4.6 (ovvero convergenza globale a punti stazionari e complessità di $\epsilon^{-2}$)

##### Line Search di Wolfe per Garantire Direzioni di Discesa

Un'alternativa alla strategia di salvaguardia è l'uso di una **line search più forte** di quella di Armijo, come la **line search di Wolfe**, ==per garantire che $d_k$ sia una direzione di discesa.==
Per assicurarsi che la direzione $d_{k+1} = - \nabla f(x_{k+1}) + \beta_{k+1}\nabla f(x_k)$ sia di discesa, la condizione:
	
	$d_{k+1}^T \nabla f(x_{k+1}) = - \|\nabla f(x_{x+1})\|^2 + \beta_{k+1} d_k^T \nabla f(x_{k+1}) < 0$

deve essere soddisfatta.  

Notare che sia $\nabla f(x_{k+1}) = \nabla f(x_k + \alpha_k d_k)$ che, (ad esempio, nel metodo di **Fletcher-Reeves**), $\beta_{k+1} = \frac{\|\nabla f(x_k+\alpha_kd_k)\|^2}{\|\nabla f(x_k)\|^2}$ sono funzioni di $\alpha_k$ e dunque possono essere controllate tramite una line search.

La line search di Wolfe quindi punta a trovare un passo che soddisfa:

1. **Condizioni di Wolfe Deboli:**
    
	  $f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, \space \nabla f(x_k + \alpha_k d_k)^T d_k \geq \sigma \nabla f(x_k)^T d_k.$
	  
2. **Condizioni di Wolfe Forti:**
	  
	  $f(x_k + \alpha_k d_k) \leq f(x_k) + \gamma \alpha_k \nabla f(x_k)^T d_k, \space \nabla f(x_k + \alpha_k d_k)^T d_k \leq |\sigma \nabla f(x_k)^T d_k|$.

Dove:

- $\gamma \in (0, 1)$ controlla la riduzione sufficiente della funzione,
- $\sigma \in (\gamma, 1)$ garantisce che la derivata direzionale diminuisca adeguatamente.

 Entrambe le condizioni richiedono che la **condizione di Armijo** sia soddisfatta (riduzione sufficiente della funzione obiettivo). 
 Richiedono inoltre ==che la derivata direzionale corrente sia significativamente ridotta al **passo successivo==**, assicurando che la **direzione corrente** sia stata ==sfruttata al massimo==, così che non sia necessario fare un secondo passo di discesa su una direzione sostanzialmente inalterata. Questo restringe l'intervallo dei passi $\alpha_k$ a valori che sono **approssimativamente stazionari** per $\phi(\alpha)$.

![[Pasted image 20250123161650.png]]

La Figura 6 mostra come la **condizione di Armijo** e le **condizioni di Wolfe** limitino il passo $\alpha_k$.

I passi accettabili si trovano nell'intervallo in cui:
- La funzione obiettivo si riduce sufficientemente (condizione di Armijo).
- La derivata direzionale soddisfa le restrizioni aggiuntive delle condizioni di Wolfe.

Un passo che soddisfa le condizioni deboli o forti di Wolfe, può essere trovato con strategie simile a quelle di Armijo (eccetto che i passi di prova possono essere aumentati se c'è bisogno).
Dal punto di vista computazionale l'uso della line search di Wolfe richiede il calcolo **sia della funzione obiettivo** sia del **gradiente** per ogni passo di prova, ==aumentando il costo computazionale rispetto alla sola condizione di Armijo.==

Nel metodo del gradiente coniugato (ad esempio, con la regola di Fletcher-Reeves), l'uso della line search di Wolfe garantisce che la **direzione successiva** $d_{k+1}$ sia una direzione di discesa: $\nabla f(x_k + \alpha_k d_k)^T d_{k+1} < 0$. Questo assicura proprietà di **convergenza globale**, rendendo i metodi del gradiente coniugato efficaci sia nei casi convessi **sia non convessi**, anche se i risultati di complessità **non sono ancora ben definiti**.
La riduzione delle iterazioni in generale compensa l'aumento delle valutazioni del gradiente, fino a che i parametri della line search sono fissati in modo corretto e il passo di prova è frequentemente accettato dalla line search.

Riassumendo... vuoi convergenza globale per gradiente coniugato usi condizioni di wolfe, arrivi globalmente allo soluzione ma ci spendi ancora più tempo!
###### **Il caso quadratico**

Infine i metodi del gradiente coniugato sono particolarmente efficaci per problemi di ottimizzazione **quadratici strettamente convessi** (o equivalentemente sistemi di equazione lineare). In questo caso tutte le regole definite per $\beta_k$ collassano alla stessa quantità, per qui parleremo di **un solo metodo del gradiente con gradiente coniugato**.

Il nome di *gradiente coniugato* deriva da **una proprietà delle direzioni** nei problemi quadratici della forma $\frac{1}{2} x^TQx+c^Tx$ con $Q > 0$ (matrice simmetrica definita positiva)

---

**Definizione 4.5:** Un insieme di direzioni $d_0, d_1, \dots, d_{m-1} \in \mathbb{R}^n$ è detto *mutuamente coniugato* rispetto a $Q$ matrice simmetrica definita positiva se: 	$d_i^T Q d_j = 0, \quad \forall i, j= 0,..., m-1, i \neq j$

---

Essere **mutuamente coniugati** può essere dimostrato essere più forte della condizione di indipendenza lineare; dal punto di vista dell'ottimizzazione, vorremmo avere un insieme di n direzioni coniugate rispetto a Q, come detto nella seguente Proposizione:

---

**Proposizione 4.11: Convergenza Finita del metodo del gradiente coniugato nel caso Quadratico**: Se $d_0, \dots, d_{n-1}$ sono **mutuamente coniugate** rispetto a $Q$, allora sia $x_0 \in \mathbb{R}^n$ e $x_{k+1} = x_k + \alpha_k d_k$, con $\alpha_k = \frac{-\nabla f{x_k}^Td_k}{d_k^TQd_k}$. Allora esiste $m < n -1$ tale che $x^{m+1} = x^*$  tale che $Qx^* + c = 0$ ovvero $x^*$ è il **minimo globale**.

---

Per problemi quadratici, con una ricerca **esatta lungo direzioni mutuamente coniugate**, il **metodo converge** **esattamente** al minimo globale ==in un numero finito di passi!==

Ora, il problema dell'algoritmo con il **metodo di direzioni coniugate** è appunto trovare l'insieme di direzioni. Ci dà una mano il metodo del gradiente coniugato, sia $g_k = \nabla f(x^k)$; sia $d_0 = -g_0$ allora: $\alpha_k = \frac{-g_k^T d_k}{d_k^TQd_k} = \frac{\|g_k\|^2}{d_k^TQd_k}, \space \beta_{k+1} = \frac{\|g_{k+1}\|^2}{\|g_k\|^2}, \space d_{k+1} = -g_{k+1} + \beta_{k+1}d_k$ .
Può essere mostrato che, ad ogni iterazione la nuova iterazione $d_{k+1}$ è mutualmente coniugata rispetto a $d_0, ... , d_k$ 

---

**Algoritmo 3: Metodo del Gradiente Coniugato per Problemi Quadratici**

3. **Input:** $x_0 \in \mathbb{R}^n, d_0 = -g_0 (\text{con} \space g_0 = \nabla f(x_0))$.
4. **Inizializzazione:** $k = 0$.
5. **Iterazione**  (finché $\|g_k\| \neq 0$):
    - Calcola: $\alpha_k = \frac{\|g_k\|^2}{d_k^T Q d_k}$.
    - Aggiorna:
	    - $x_{k+1} = x_k + \alpha_k d_k$
	    - $g_{k+1} = g_k + \alpha_k Q d_k$.
	    - $\beta_{k+1} = \frac{\|g_{k+1}\|^2}{\|g_k\|^2}$
	    - $d_{k+1} = -g_{k+1} + \beta_{k+1} d_k$
	- Incrementa $k = k + 1$.
6. **Output:** $x_k$

---

Per problemi quadratici, il metodo è ==esatto e raggiunge il minimo globale in $n$ iterazioni==.
**In casi ad alta dimensione**, si introduce un criterio di arresto basato su $\|g_k\| \leq \epsilon$, rendendo il metodo iterativo. Soluzioni altamente accurate vengono spesso ottenute in **poche iterazioni**.

### 4.5 Metodo di Newton

Abbiamo visto che con i metodi di discesa del gradiente e algoritmi del primo ordine in generale ci sono dei limiti che speriamo di ottenere di migliorare in termini di velocità di convergenza nei casi non convesso, convesso e fortemente convesso.

Siamo quindi curioso di osservare, quando la funzione obiettivo lo permette, l'informazione di secondo ordine, e guardiamo se possiamo ottenere qualcosa di meglio.
Assumiamo di avere $f \in C^2(\mathbb{R}^n)$ e ora usiamo l'informazione fornita da $\nabla^2 f(x)$ per costruire un metodo del secondo ordine. Assumiano che siamo ad una qualche soluzione $x^k$ e sia anche $\nabla^2 f(x^k)$ una matrice definita positiva. Possiamo quindi costruire l'espansione di _Taylor_ di $f$ al secondo ordine ottenendo

	$m_k(x) = f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{1}{2} (x - x_k)^T \nabla^2 f(x_k) (x - x_k)$

L'approssimazione ottenuta della funzione obiettivo è una funzione quadratica strettamente convessa (nel caso in cui l'_Hessiana_ sia definita positiva ), possiamo quindi trovare il minimizzatore globale di $m_k(x)$ annullandone il gradiente:

	$\begin{aligned} \nabla m_k(x) &= \nabla f(x_k) + \nabla^2 f(x_k)(x - x_k) = 0, \\ x &= x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k). \end{aligned}$

L'idea del _Metodo di Newton_, è quella di definire uno schema iterativo dove la nuova iterata è ottenuta prendendo il minimo del modello quadratico costruito intorno alla soluzione corrente, ovvero usando la formula di aggiornamento:

	$x^{k+1} = x^k - [\nabla^2 f(x^k)]^{-1} \nabla f(x^k)$ 

Questo tipo di regola di aggiornamento, può essere intesa, come la regola di aggiornamento del metodo di discesa della forma $x^{k+1} = x^k + \alpha_k d_k$ dove $d_k = - [\nabla^2 f(x^k)]^{-1} \nabla f(x^k)$ e $\alpha_k$ è posto costantemente a 1 per l'intero processo.

Osserviamo nel prossimo esempio che può succedere adottando questo tipo di schema su un semplice problema ad una variabile.

**Esempio 4.4: Iterazioni del Metodo di Newton**

**Problema:**  Minimizzare $min_{x \in \mathbb{R}} f(x) = \sqrt{1 + x^2}$, che ha una funzione obiettivo abbastanza regolare: è infatti strettamente convessa, coerciva, doppiamente continua e differenziabile con:

	$f'(x) = \frac{x}{\sqrt{1 + x^2}}, \quad f''(x) = \frac{1}{(1 + x^2)^{3/2}}$

**Iterazioni:**

	$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)} = x_k - \frac{x_k}{(1 + x_k^2)^{\frac{1}{2}}}(1 + x_k^2)^{\frac{3}{2}} = x_k - x_k(1+x_k^2) = -x_k^3$

- Se $x_0 = \pm 1$, la sequenza oscilla tra 1 e -1, senza convergenza.
- Se $|x_0| > 1$, la sequenza diverge.
- Se $|x_0| < 1$ (es. $x_0 = 0.5$), la sequenza converge rapidamente a 0.
	x0 = 1/2 = 0.5, x1 = - 1/2^3 = −0.125, x2 = 1/2^9=0.00195, x3 ≈ −0.000000007, . . .

Che vediamo converge a 0, unico punto di minimo abbastanza velocemente, la distanza dall'ottimo ad ogni iterazione è molto minore di quanto era alla precedente iterazione, sembra un tasso **superlineare**.
Possiamo comunque vedere che osservando il metodo di Newton non converge globalmente al punto di minimo, in quanto la convergenza dipende dal punto di partenza, ma sembra essere veloce quando converge!

L'esempio ci dice tutta la storia sul metodo di Newton nella sua forma pura: non siamo sicuri che converga, ma se lo fa, lo fa molto velocemente. In termini formali, l'algoritmo non possiede garanzie di convergenza globali (peggio addirittura dei metodi del primo ordine), ma ha una garanzia su una velocità di convergenza locale.

Nella prossima proposizione sono descritte queste proprietà.

---

#### Proposizione 4.12: Proprietà del Metodo di Newton

Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione due volte continuamente differenziabile. Sia $x^*$ un punto tale che:

- $\nabla f(x^*) = 0$,
- $\nabla^2 f(x^*) \text{è non singolare}$.

Allora esiste $\epsilon > 0$ tale che, per ogni $x_0 \in B(x^*, \epsilon)$:

7. La sequenza $\{x_k\}$ è ben definita e rimane in $B(x^*, \epsilon)$.
8. $\lim_{k \to \infty} x_k = x^*$.
9. Il tasso di convergenza è **superlineare**.

---

**Dimostrazione**.

Per **continuità dell'Hessiana:** $\nabla^2 f(x)$ è continua e non singolare in $x^*$. Esistono $\epsilon_1 > 0$ e $\mu > 0$ tali che:

	$\|[\nabla^2 f(x)]^{-1}\| \leq \mu, \quad \forall x \in B(x^*, \epsilon_1)$

Successivamente per ogni $\sigma \in (0,1)$, e sempre per la continuità di $\nabla^2f$ è sempre possibile trovare un $\epsilon \leq \epsilon_1$ tale che:

	$\|\nabla^2 f(x) - \nabla^2 f(y) \| \leq \frac{\sigma}{\mu} \quad \forall x,y \in B(x^*, \epsilon)$ (13)
	
Procediamo ora per **induzione:**

- Base: $x_0 \in B(x^*, \epsilon)$.
- Passo: Assumiamo per un arbitrario $k, x_k \in B(x^*, \epsilon)$. ovvero $\|x^k-x^*\| \leq \epsilon$. Per la regola di aggiornamento di Newton:

	$x_{k+1} - x^* = x^k -[\nabla^2 f(x_k)]^{-1}\nabla f(x_k) - x^*$ 
		   $= - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k) + [\nabla^2 f(x_k)]^{-1} \nabla^2 f(x_k) (x_k - x^*)$
		   $=- [\nabla^2 f(x_k)]^{-1} (\nabla f(x_k) - \nabla^2 f(x_k)(x_k - x^*))$
		   $=- [\nabla^2 f(x_k)]^{-1} (\nabla f(x_k) - \nabla f(x^*) - \nabla^2 f(x_k)(x_k - x^*))$
		
Dove si è sfruttato il fatto che $[\nabla^2 f(x_k)]^{-1} \nabla^2 f(x_k) = I, \quad \nabla f(x^*) = 0$. 
Andando avanti abbiamo:

	$\|x^{k+1} - x^*\| =\|[\nabla^2 f(x_k)]^{-1} (\nabla f(x_k) - \nabla f(x^*) - \nabla^2 f(x_k)(x_k - x^*))\|$
			$\leq \|[\nabla^2 f(x_k)]^{-1}\| \|(\nabla f(x_k) - \nabla f(x^*) - \nabla^2 f(x_k)(x_k - x^*))\|$
			$\leq \mu \|(\nabla f(x_k) - \nabla f(x^*) - \nabla^2 f(x_k)(x_k - x^*))\|$

Sfruttiamo ora il teorema della media per gli integrali (Proposizione 1.7):

	$\nabla f(x_k) - \nabla f(x^*) = \int_0^1 \nabla^2f(x^*+t(x^k-x^*))(x^k-x^*)dt$

Per ottenere:

	$\|x_{k+1}-x^*\| = \mu \|\int_0^1 \nabla^2f(x^* + t(x^k-x^*))(x^k - x^*) dt - \nabla^2f(x_k)(x_k-x^*)\|$
			$= \mu \|\int_0^1 (\nabla^2f(x^* + t(x^k-x^*) - \nabla^2f(x_k))(x^k - x^*) dt \|$
			$\leq \mu \int_0^1\| (\nabla^2f(x^* + t(x^k-x^*)) - \nabla^2f(x_k))(x^k - x^*)\|dt$
			$\leq \mu \int_0^1\| \nabla^2f(x^* + t(x^k-x^*)) - \nabla^2f(x_k)\|\|(x^k - x^*)\|dt$ (14)
		
Notiamo quindi che $B(x^*,\epsilon)$ è un insieme convesso e che entrambi $x^*$ e $x^k$ appartengono a $B(x^*,\epsilon)$.
Allora, il punto $x(t) = x^*+ t(x^k+x^*) = (1-t)x^*+tx^k$ appartiene anche lui a $B(x^*,\epsilon)$ per $t \in [0,1]$, anche tutti i valori all'interno dell'integrale. Dunque ricordando (13), avremo $\|\nabla^2 f(x(t)) - \nabla^2 f(x^k)\| \leq \frac{\sigma}{\mu}$ per qualsiasi $t \in [0,1]$. 

Possiamo quindi scrivere:

	$\|x_{k+1}-x^*\| \leq \mu \|\int_0^1 \frac{\sigma}{\mu} \|x^k - x^*\|dt = \sigma \|x^k - x^*\| \leq \|x^k - x^*\| \leq \epsilon$ 

Per $\sigma \in (0,1)$ e $x^k \in B(x^*,\epsilon)$.
Abbiamo fatto vedere quindi che anche $x^{k+1} \in B(x^*,\epsilon)$ se $x^k \in B(x^*,\epsilon)$. Ma allora per induzione l'intera sequenza $\{x^k\}$ sta in $B(x^*,\epsilon)$.

Ora, tornando alle disuguaglianze precedenti si nota che:

	$0 \leq \|x^{k+1}-x^*\|  \leq \sigma \|x^k - x^*\| \leq \sigma^2 \|x^{k-1} - x^* \leq \dots \leq \sigma^{k+1}\|x^0-x^*|$

Dunque prendendo il limite per $k \to \infty$ e ricordando che $\sigma \in (0,1)$ otteniamo che: 
	$0 \leq \lim_{k \to \infty}\|x_{k}-x^*\|  \leq  \lim_{k \to \infty} \sigma^{k}\|x^0-x^*| = 0$

ovvero che:  $\lim_{k \to \infty} x^k = x^*$ (per i carabinieri) 

Infine tornando a (14), divido entrambe le parti per $\|x^k - x^*\|$ e ottengo:

	$0 \leq \frac{\|x^{k+1} - x^*\|}{\|x^k - x^*\|} \leq \mu \int_0^1\| \nabla^2f(x^* + t(x^k-x^*)) - \nabla^2f(x_k)\|dt$

E prendendo i limiti per $k \to \infty$, ricordando che $x^k \to x^*$ allora otteniamo:

	$0 \leq \lim_{k \to \infty} \frac{\|x^{k+1} - x^*\|}{\|x^k - x^*\|} \leq \lim_{k \to \infty} \mu \int_0^1\| \nabla^2f(x^* + t(x^k-x^*)) - \nabla^2f(x_k)\|dt$
				$=\mu \int_0^1\| \nabla^2f(x^*) - \nabla^2f(x^*)\|dt = 0$ 

Ovvero il tasso di convergenza è **superlineare**.

---

Abbiamo quindi dimostrato che il metodo puro di Newton gode di convergenza locale superlineare. Questo risultato ci incoraggia verso l'uso di informazioni del secondo ordine in algoritmi di ottimizazzione non lineari, ma dobbiamo comunque considerare che il costo della computazione della matrice Hessiana è comunque un operazione costosa (circa n volte più costoso di calcolare il gradiente e $n^2$ volte più costoso di $f$). Per calcolare la direzione $d_k = -[\nabla^2f(x^k)]^-1 \nabla f(x^k)$, o invertiamo la matrice $n\space x\space n$ e quindi eseguiamo un prodotto matrice per vettore, oppure risolviamo il sistema lineare (meno costoso e numericamente più robusto): in entrambi i modi il costo dell'operazione è di $O(n^3)$. Dunque, mentre il tasso di convergenza locale in termini di iterazione è molto buono, l'incremento significativo del costo è nascosto dietro il risultato. Dunque, non è sempre il caso in cui la riduzione del numero di iterazioni è specchiato da una discesa nel costo totale dell'algoritmo.

Abbiamo da affrontare alcuni problemi:

- Presentando il metodo di Newton, noi sistematicamente facciamo l'assunzione sul fatto che $\nabla^2f(x^k)$ sia definita positiva, ma in pratica non è sempre il caso:
	- Se la funzione obiettivo è convessa ma non fortemente, potremmo finire, potremmo finire in un punto $x^k$ tale che l'Hessiana sia non invertibile e l'algoritmo quindi non sia ben definito. 
	- Con funzioni generali non convesse, l'Hessiana non solo può non essere invertibile come nel punto sopra, ma può avere anche autovalori negativi e quindi la direzione potrebbe essere di salita.

- L'assenza di garanzie di convergenza globale è una debolezza di relativa importanza del metodo. 

Per risolvere i problemi sopra menzionati, si introducono _strategie di globalizzazione_, ovvero le seguenti modifiche:

10. **Modifica della Hessiana:** se alcuni autovalori di $\nabla^2 f(x_k)$ sono fuori dall'intervallo $[c_2, c_1]$ con $0 < c_2 < c_1 < \infty$, si modifica la matrice di Newton per garantire che la condizione di autovalori limitati valga e quindi la matrice sia definita positiva.
11. **Ricerca Lineare di Armijo:** Si esegue una ricerca di Armijo lungo la direzione calcolata, iniziando con un passo iniziale $\alpha = 1$.

Con queste strategie otteniamo un metodo di discesa usando la line search di Armijo lungo una direzione gradient-related, dunque ottenendo garanzie di convergenza globale.
Sotto ragionevoli assunzioni, può essere dimostrato che quando il metodo di Newton globalizzato entra nell'intorno di un punto stazionario (soddisfacendo l'ipotesi della propozione 4.12), allora non c'è più bisogno di nè modificare l'Hessiana che di fare cattivi passi di backtrack: il metodo puro di Newton è portato da qui in avanti e quindi ottenendo i risultati di convergenza locale veloce.
Quando un metodo ha questo tipo di comportamento è detto _Metodo di Newton globalmente convergente_

---

### 4.6 Metodi Quasi-Newton

Abbiamo visto che i metodi di Newton posseggono delle proprietà di convergenza veloce molto interessanti, ma abbiamo fatto vedere come i costi per iterazione possono diventare comunque molto alti al crescere delle variabili, al punto in cui i vantaggi in termini di iterazione sono sopraffati dal peso richiesto dalle operazioni e l'algoritmo diventa sostanzialmente impraticabile. Ci chiediamo quindi se sia possibile arrivare a qualcosa di simile al metodo di Newton ma evitando i calcoli della matrice Hessiana, usando solo informazioni del primo ordine, e senza bisogno di invertire una matrice $n \space x \space n$ (o risolvere un analogo sistema lineare).

I metodi Quasi-Newton sono stati proposti seguendo precisamente quest'idea: Invece di calcolare esattamente la matrice hessiana, questi metodi utilizzano un'approssimazione costruita tramite informazioni di primo ordine e iterazioni precedenti.
La forma generale dei metodi Quasi-Newton seguono la regola di aggiornamento:

	$x_{k+1} = x_k + \alpha_k d_k \quad \text{con} \quad d_k = -B_k^{-1} \nabla f(x_k)$

Dove $B_k$ ==approssima la vera matrice Hessiana per$x_k$==. Una direzione definita in questo modo sarà sicuramente una direzione di discesa se $B_k$ definita positivamente. 
Ora, il problema principale è come calcolare $B_k$ e quali proprietà questa approssimazione della matrice possiede. Per rispondere a questa domanda riprendiamo il caso quadratico.

Per funzioni quadratiche $f(x) = \frac{1}{2}x^T Qx + c^T x$, con $Q \succ 0$, si ha:

Per qualsiasi $x,z \in \mathbb{R}^n$: $\nabla f(x) - \nabla f(z) = Qx+c - Qz - c = Q(x-z)$ 

Dunque se inseriamo due iterate successive $x_k$ e $x_{k+1}$ e definiamo $y_k = \nabla f(x_{k+1}) - \nabla f(x)$ e $s_k = x_{k+1}- x_k$, allora otteniamo:
	
	$y_k = \nabla f(x_{k+1}) - \nabla f(x_k) = Q(x_{k+1} - x_k) = \nabla^2 f(x^{k+1})s_k$

Uguaglianza che vale nel caso di vera Hessiana nel caso quadratico è chiamata _equazione di Quasi-Newton_. Eventualmente possiamo scrivere:

	$[\nabla^2f(x^{k+1})]^{-1} y_k = s_k$

Possiamo dunque pensare di traslare questa proprietà al caso generale non lineare, dove impiegheremo un approssimazione della matrice Hessiana che soddisa l'equazione di Quasi-Newton, ovvero soddisfa una proprietà tipica delle vere Hessiane per funzioni obiettivo quadratiche.

Gli schemi generali per gli approcci Quasi-Newton sono descritti con aggiornamenti del tipo _diretto_ o _inverso_:
- $x_{k+1} = x_k - \alpha_k B_k^{-1}\nabla f(x_k) \quad B \approx \nabla^2f(x_k) \quad B_{k+1}s_k = y_k \quad \text{update diretto}$
- $x_{k+1} = x_k - \alpha_k H_k^\nabla f(x_k) \quad H \approx [\nabla^2f(x_k)]^{-1} \quad H_{k+1}y_k = s_k \quad \text{update inverso}$

Update inversi sono spesso più convenienti da un punto di vista computazionale: siccome approssimiamo l'inversa dell'Hessiana, non abbiamo poi il dovere di invertire una grande matrice o risolvere un sistema lineare per calcolare la direzione di ricerca.

Non abbiamo ancora visto come ottenere queste matrici di approssimazioni che soddisfano la proprietà di Quasi-Newton. L'idea è data l'approssimazione corrente $B_k$ (o $H_k$), aggiorneremo le matrici seconda una regola della forma:

	$B_{k+1} = B_k + \Delta B_k H_{k+1} = H_k + \Delta H_k$ 

Segue lo schema Generale per un metodo Quasi-Newton (nel caso inverso):

---

<a id="algoritmo-4"></a>
**Algoritmo-4: Metodo Quasi-Newton con Aggiornamenti Inversi**

12. **Input:** $x_0 \in \mathbb{R}^n$, $H_0 \in S^n$, $H_0 \succ 0$.
13. **Inizializzazione:** $k = 0$.
14. **Ciclo:** (Finche $\|g_k\| \neq 0$)
    - Calcolo $d_k = -H_k \nabla f(x_k)$.
    - Determino $\alpha_k$ tramite una ricerca lineare lungo $d_k$.
    - Aggiorno $x_{k+1} = x_k + \alpha_k d_k$.
    - Calcolo $\Delta H_k$ affinché $H_{k+1} y_k = s_k$. 
	    - Ovvero $(H_k + \Delta H_k)(\nabla f(x_{k+1}) - \nabla f(x_k)) = x_{k+1} - x_k$
    - Aggiornare $H_{k+1} = H_k + \Delta H_k$.
    - $k=k+1$ 
15. Restituisco $\{H_k\}$ e $x_k$

---
L'algoritmo 4 è uno schema generale, la realizzazione di questo schema sono caratterizzate da due elementi, il tipo di line search eseguito e la regola di update scelta per definire $\Delta H_k$. 
Si nota subito che se sfruttiamo una line Search di Armijo e aggiungo una salvaguardia di garanzia affichè $H_k$ soddisfi la condizione di bound sugli autovalori, allora immediatamente riotteniamo la convergenza globale e bound sulla complessità di $O(\frac{1}{\epsilon^2})$.

Regole di aggiornamento per la matrice Hessiana sono di solito basate su **aggiornamenti di rango-1 o rango-2** della matrice corrente:

- **Aggiornamenti di rango-1**:

	$\Delta B_k = \rho_k u_k v_k^T \quad \text{oppure} \quad \Delta H_k = \rho_k u_k v_k^T$,

dove $\rho_k \in \mathbb{R}_+$, $u_k, v_k \in \mathbb{R}^n$: La matrice ottenuta in questo modo è una matrice di rango-1, nella quale l'efficienza degli aggiornamenti dipendono sulla scelta specifica di $\rho_k,u_k, v_k$. 
Un esempio noto è la **regola di Broyden**:

	$B_{k+1} = B_k + \frac{(y_k - B_k s_k)s_k^T}{s_k^T s_k}$

La simmetria e la definita positività negli aggiornamenti di $B_{k+1}$ non sono garantite ( a meno di giuste correzzioni)

- **Aggiornamenti di rango-2**

	$\Delta B_k = a_k u_k u_k^T + b_k v_k v_k^T \quad \text{oppure} \quad \Delta H_k = a_k u_k u_k^T + b_k v_k v_k^T$

dove $a_k, b_k \in \mathbb{R}_+$ e  $u_k, v_k \in \mathbb{R}^n$. Di nuovo, l'efficacia degli aggiornamenti dipende dalla scelta specifica degli scalari e dei vettori che definiscono l'aggiornamento. Questi aggiornamenti garantiscono più stabilità di rango-1 in quanto riescono a mantenere proprietà di simmetria e positività per la matrice.

#### 4.6.1 Algoritmo BFGS

Il **BFGS (Broyden-Fletcher-Goldfarb-Shanno)** è uno dei metodi Quasi-Newton più popolari, basato su aggiornamenti di rango-2. 

Le formule per gli aggiornamenti sono:
- **Caso Diretto:**

	$B_{k+1} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$

- **Caso Inverso:**

	$H_{k+1} = H_k + \left(1 + \frac{y_k^T H_k y_k}{s_k^T y_k}\right)\frac{s_k s_k^T}{s_k^T y_k} - \frac{H_k y_k s_k^T + s_k y_k^T H_k}{s_k^T y_k}$

Notare che queste regole di aggiornamento soddisfano le proprietà di Quasi-Newton, infatti:

	$B_{k+1}s_k = B_ks_k + \frac{y_k y_k^T}{y_k^T s_k}s_k - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}s_k$
		$= B_k s_k + y_k\frac{y_k^T s_k}{y_k^Ts_k} -  B_k s_k\frac{ s_k^T B_ks_k}{s_k^T B_k s_k}$
		$= B_k s_k + y_k -  B_k s_k = y_k$

Calcoli simili possono essere eseguiti per la regola di aggiornamento inversa.

Possiamo fare vedere anche come la regola di update di BFGS può rafforzare la preservazione della definitezza positiva.

---

**Proposizione 4.13.** Sia $H_k$ definito positivo e $H_{k+1}$ calcolato tramite la regola di aggiornamento BFGS. Allora $H_{k+1}$ è definito positivo se e solo se $s_k^T y_k > 0$.

Questa proposizione garantisce che, se $H_0$ è definito positivo e ad ogni iterazione $s_k^T y_k > 0$, la condizione di definitezza positiva sarà mantenuta in ogni passo.
La condizione $s_k^T y_k > 0$ può essere imposta scegliendo adeguatamente il passo $\alpha_k$. 

Infatti:

	$s_k^T y_k = (\nabla f(x_{k+1}) - \nabla f(x_k))^T (x_{k+1} - x_k) > 0$

che equivale a:

	$s_k^T y_k =  (x_{k+1} - x_k)^T (\nabla f(x_{k+1}) - \nabla f(x_k))$
		$= (x_k - \alpha_kd_k - x_k)^T (\nabla f(x_{k+1}) - \nabla f(x_k))$
		$= \alpha_kd_k^T (\nabla f(x_{k+1}) - \nabla f(x_k))$

ovvero siccome $\alpha_k > 0$, necessariamente:

	$(\nabla f(x_{k+1}) - \nabla f(x_k))^T d_k > 0$

oppure:

	$\nabla f(x_{k+1})^T d_k > \nabla f(x_k)^T d_k$

Questa condizione può essere soddisfatta utilizzando ==una ricerca lineare del tipo Wolfe== per determinare $\alpha_k$ nell'[algoritmo 4](#algoritmo-4-metodo-quasi-newton-con-aggiornamenti-inversi).

Per BFGS puro, senza salvaguardie, esistono risultati di convergenza globale sotto ipotesi di convessità sulla funzione obiettivo, inoltre se si assumono forte convessità e doppia differenziabilità si può dimostrare che il metodo converge in modo superlineare al minimo globale, accettando sempre il passo unitario per $k$ grande.
Dunque l'algoritmo BGFS è in grado di avere sia la convergenza veloce di Newton senza dover impiegare informazioni del secondo ordine.

---

#### 4.6.2 Metodo L-BFGS

Il metodo **L-BFGS** è una variante del BFGS progettata specificamente per problemi di grande scala (da cui il nome _Limited Memory_). Questo metodo mostra un'ottima performance pratica ed è considerato una delle scelte preferite per risolvere problemi di ottimizzazione non vincolati.

L'idea di base è che in problemi ad alta dimensionalità, la memorizzazione della matrice $H_k$ e il calcolo di $d_k = -H_k \nabla f(x_k)$ possono diventare proibitivi. Per affrontare questa difficoltà, L-BFGS utilizza una regola ricorsiva che richiede solo i vettori $y_k$ e $s_k$ per calcolare:

	$H_{k+1} = V_k^T H_k V_k + \rho_k s_k s_k^T$

dove: $\rho_k = \frac{1}{y_k^T s_k}, \quad V_k = I - \rho_k y_k s_k^T$.

In L-BFGS, l'approssimazione $H_{k+1}$ viene interrotta dopo $m$ passi, utilizzando solo le ultime $m$ coppie $(y_k, s_k)$, insieme a una stima iniziale $H_{k-m} \approx \gamma I$ (di solito si usa questa), facilmente memorizzabile. Esperimenti mostrano che valori relativamente piccoli di $m$ (tra 2 e 20) sono sufficienti per ottenere approssimazioni soddisfacenti. La formula può quindi essere sfruttato per il calcolo di $H_k \nabla f(x^k)$.
Inoltre, la procedura ricorsiva chiamata HG consente di calcolare $d_k$ con soli $4mn$ moltiplicazioni, tramite la sola conoscenza di $(y_{k-i}, s_{k-i}), i = 0, ..., m$ e l'approssimazione di $H_{k-m}$, riducendo significativamente i costi computazionali.

Come precedentemente discusso L-BFGS è veramente efficiente nella pratica nel risolvere problemi di ottimizzazione non vincolata.
Tuttavia:
- Le **proprietà teoriche** di convergenza globale non sono forti come per il BFGS: risultati di convergenza globale verso punti stazionari sono ancora sconosciuti, anche sotto assunzioni di convessità.
- Si può garantire convergenza solo tramite strategie di salvaguardia.
- La convergenza globale può essere garantita solo con strategie di salvaguardia standard.
- In caso di forte convessità, è possibile dimostrare la **convergenza lineare** sotto ipotesi specifiche sulla sequenza $\{H_k\}$.

Un'estensione chiamata **L-BFGS-B** è stata progettata per affrontare problemi di ottimizzazione con vincoli di tipo _bound constrained_.

### 4.7 Metodi di Decomposizione

Esistono varie situazioni dove i problemi di ottimizzazione sono molto complicati e difficili da affrontare interamente. In alcuni di questi casi è possibile affrontare efficacemente il problema dividendolo in parti più piccole o semplici. 
I casi dove i *metodi di decomposizione* sono utili includono quelle situazioni dove uno o più dei seguenti aspetti ricorrono:
- Il numero $n$ di variabili è grande ( $∼ 10^4$)  e le informazioni sulle variabili oppure sulla funzione obiettivo non possono essere interamente memorizzate.
- Fissato il valore per alcune variabili, otteniamo un sottoproblema che può essere diviso in parti indipendenti risolte con metodi di computazione parallela.
- Fissato il valore per alcune variabili, il sottoproblema rimanente è facile da risolvere o possiede proprietà di regolarità superiori rispetto all'originale.

---

**Esempio 4.5**
Di seguito, elenchiamo alcuni esempi di problemi in cui le strategie di decomposizione 
possono essere utili:

- $f (x) = g(x_1 ) + \sum_{i=2}^{n} h_i (x_1 )s_i (x_i )$
  La funzione sopra diventa più semplice da gestire se il valore della variabile $x_1$ 
  è fissato, poiché in tal caso rimangono $n - 1$ termini separabili, ognuno dipendente solo da una singola variabile $x_i$, che possono essere minimizzati in parallelo. Possiamo quindi alternare tra un passo di ottimizzazione univariata su $x_1$ e un'ottimizzazione parallela di tutte le altre variabili.

- $f (x, y) = \| \Phi(y)x - b \|^2$
  Il problema di minimi quadrati non lineare sopra diventa un semplice problema 
  di minimi quadrati lineari se il valore delle variabili $y$ è fissato.

- $f (x, y) = x^2 y^2 + 10xy + x^2 + y^2$
  La funzione sopra è non convessa; tuttavia, è una parabola convessa rispetto a $x$ 
  per ogni valore di $y$, e lo stesso vale rispetto a $y$ per ogni valore di $x$. Pertanto, minimizzare rispetto a una sola delle due variabili alla volta equivale a risolvere un problema di ottimizzazione convessa più semplice, che può essere risolto fino a ottenere l'ottimo globale.

---

Supponiamo ora di avere un problema generico della forma:

	$\min_{x \in X} f (x)$

dove $f : \mathbb{R}^n \to \mathbb{R}$ e $X \subseteq \mathbb{R}^n$  
Il problema può essere riscritto in una forma decomposta come:

	$\min_{x_1 \in X_1 ,...,x_m \in X_m} f (x_1 , \dots , x_m )$

dove $f : \mathbb{R}^{n_1} \times \dots \times \mathbb{R}^{n_m} \to \mathbb{R}, X_1 \subseteq \mathbb{R}^{n_1} , \dots , X_m \subseteq \mathbb{R}^{n_m}$ e $\sum_{i=1}^{m} n_i = n$.  

In altre parole, il vettore delle variabili è stato **suddiviso in blocchi separati** 
di variabili che possono essere gestiti in modo indipendente.

Esistono diversi metodi per identificare un modo di dividere le variabili in blocchi e sfruttare questa suddivisione tramite algoritmi. Tali approcci possono essere classificati in due categorie principali: **metodi sequenziali** e **metodi paralleli**. In entrambi i casi i sottoproblemi sono definiti rispetto ai singoli blocchi di variabili, tenendo il valore delle variabili negli altri blocchi fermo.

---
##### **Metodi di Decomposizione Sequenziale**

Nei metodi sequenziali, i sottoproblemi vengono ==risolti uno alla volta==, aggiornando le variabili di ciascun blocco ad ogni passo.

![[Pasted image 20250203083017.png]]

Un esempio classico è l'**algoritmo di Gauss-Seidel**, definito dalla seguente *regola di aggiornamento*:

	$x_{i}^{k+1} = \arg\min_{\xi_i \in X_i} f(x_{1}^{k+1}, \dots, x_{i-1}^{k+1}, \xi_i, x_{i+1}^k, \dots, x_m^k)$.

L'algoritmo risolve ciclicamente i sottoproblemi ottenuti fissando il valore di tutte le variabili, tranne quelle di un blocco. La soluzione trovata per il sottoproblema viene immediatamente utilizzata per aggiornare il valore delle variabili del blocco corrente.

Notare che l'algoritmo richiede di calcolare un ottimizzatore **globale** per ogni sottoproblema: questo è una richiesta forte, che può essere soddisfatta solo se i sottoproblemi sono abbastanza semplici.

La convergenza globale verso punti stazionari può essere garantita per il metodo di Gauss-Seidel sotto assunzioni di compattezza sull'insieme di livello e in aggiunte le seguenti condizioni:

-  f è convessità.
- f è strettamente convessa per blocchi ovvero la funzione obiettivo di tutti i sottoproblemi è sempre strettamente convessa.
- $m=2$ con solo due blocchi di variabili la convessità della funzione obiettivo non è necessaria.

---
##### **Metodi di Decomposizione Parallela**

Nei metodi paralleli, i sottoproblemi associati ai diversi blocchi vengono risolti **in modo indipendente e simultaneo**. Successivamente, la soluzione migliore tra questi sottoproblemi viene utilizzata per aggiornare le variabili, ovvero ==ad ogni iterazione si aggiorna un solo blocco==.

![[Pasted image 20250203091825.png]]

Un esempio è l'**algoritmo di *Jacobi***, descritto dalle seguenti *regole di aggiornamento*:
	
	$\hat{x}_{i}^{k+1} \in \arg\min_{x_i} f(x_1^k, \dots, x_i, \dots, x_m^k)$,

	$x^{k+1} \in \arg\min_{(x_1^k, \dots, \hat{x}_{i}^{k+1}, \dots, x_m^k)} f(x_1^k, \dots, \hat{x}_{i}^{k+1}, \dots, x_m^k)$

---

#### 4.7.1 Metodi di Decomposizione con Sovrapposizione dei Blocchi

Fino a questo punto, abbiamo considerato approcci di decomposizione dove $x \in \mathbb{R}^n$ è diviso in $m$ blocchi che non cambiano con l'iterazione $x^k=(x_1^k, ..., x_m^k)$

Un'estensione più flessibile permette di lavorare con ==insiemi variabili di blocchi==, chiamati **insiemi di lavoro** ($W_k ⊂ \{1, ..., n\}$).Il sottoproblema considerato in ogni iterazione diventa:

	$\min_{x_{W_k}} f(x_{W_k}, x_{\overline{W}^k})$

dove $\overline{W}^k$ è il **complemento** di $W_k$. La regola di aggiornamento è:

	$x_i^{k+1} = \begin{cases} x_i^\star & \text{se } i \in W_k, \\ x_i^k & \text{altrimenti.} \end{cases}$

La convergenza globale di questo schema dipende dal _working set selection rule_ ovvero la scelta delle variabili per ogni iterazione.
Possibili regole di scelta che assicurano convergenza a punti stazionari includono:
- *Regola ciclica*: $\exists M > 0 \space \text{t.c.} \space \forall i \in \{1,..., n\}, \forall k \space \exists \ell(k) \leq M  \space \text{t.c.} \space  i \in W^{k+\ell(k)}$ . Questa regola richiede che ogni variabile appare nel set di lavoro almeno ogni $M$ iterazioni; in questo modo, si previene che variabili importanti da ottimizzare vengano dimenticate.
- *Regola di Gauss-Southwell*: $\forall k, i(k) \in W_k \space \text{if} \space | \nabla_{i(k)} f(x^k)| \geq | \nabla_i f(x^k)| \space \forall i \in \{1, ... , n\}$. Questa regola richiede di includere nella selezione delle variabili ad ogni iterazione, la variabile più "promettente" (che è quella associata alla derivata più grande). Questa strategia permette al limite, di portare a zero la più grande derivata parziale, ovvero portare a zero l'intero gradiente.

---

### 4.8 Metodo del Gradiente Stocastico per Problemi con Somma Finita

I problemi di **somma finita**, tipici in apprendimento automatico, sono rappresentati come:

	$\min_{x \in \mathbb{R}^n} f(x) = \frac{1}{N} \sum_{i=1}^N f_i(x)$

Quando $N$ è molto grande, calcolare il gradiente completo $\nabla f(x)$ diventa oneroso. Affrontare l'intera funzione obiettivo $f$ da sola potrebbe diventare costoso in termini di memoria e tempi di computazione.

L'**algoritmo di discesa del gradiente stocastico (SGD)** fornisce una soluzione computazionalmente più leggera, aggiornando le variabili ad ogni iterazione con passi stocastici basati su un gradiente approssimato:	$x^{k+1} = x^k - \alpha_k \nabla f_{i_k}(x^k)$ (19), dove $i_k$ è un indice **scelto casualmente** tra $\{1, \dots, N\}$ all'iterazione K.
L'approssimazione allevia la pesantezza del calcolo delle derivata, in quanto dobbiamo calcolare solo un gradiente $\nabla f_i$ , ad ogni iterazione rispetto agli $N$ termini necessari per calcolare la vera $\nabla f$ 

Il passo $\alpha_k$ è spesso impostato a un valore costante o segue una sequenza predefinita. Le tradizionali ricerche di linee (line searches) non sono generalmente adatte in questo caso, poiché la funzione obiettivo cambia a ogni iterazione. Questo porta a due problematiche principali:
16. Non si può garantire una diminuzione sufficiente della funzione obiettivo reale.
17. Forzare una diminuzione sufficiente sull'approssimazione corrente potrebbe non portare benefici.

La scelta stocastica della direzione di discesa si basa sul fatto che, se consideriamo il **valore atteso** della quantità $\nabla f_{i_k}(x^k)$, e assumendo una distribuzione uniforme sui valori $\{1, \ldots, N\}$, otteniamo (con $p_i = \frac{1}{N}$):

$E[\nabla f_i(x^k)] = \sum_{i=1}^N p_i \nabla f_i(x^k) = \sum_{i=1}^N \frac{1}{N} \nabla f_i(x^k) = \frac{1}{N} \sum_{i=1}^N \nabla f_i(x^k)$
$= \nabla f(x^k)$

In altre parole, ==in media ci si aspetta di ottenere il gradiente reale==. 

Formalmente, diciamo che una direzione $d_k$ tale che $E[d_k]=-\nabla f(x^k)$ è uno **stimatore non distorto** (_unbiased_) del vero gradiente $\nabla f(x^k)$. In principio, vorremmo usare una direzione di ricerca fra i diversi stimatori unbiased di $-\nabla f(x^k)$, che abbia piccola varianza. In quanto riducendo questa, implicherebbe una minore probabilità di fare grossi errori nella stima della direzione del gradiente.

Strategie di riduzione della varianza sono state proposte per migliorare il tasso di convergenza teorico di SGD. 
Tuttavia, queste strategie richiedono o elevati requisiti di memoria, oppure calcolo del gradiente reale in alcune iterazioni.
Per questo motivo, tali strategie sono applicabili solo in problemi particolarmente strutturati.

Un approccio pratico per ottenere un effetto di riduzione della varianza è basare il calcolo del gradiente non su un singolo termine della somma, ma su un sottoinsieme di termini $B_k \subset \{1, \ldots, N\}$, con $|B_k| = M \ll N$:

	$d_k = -\frac{1}{|B_k|} \sum_{i \in B_k} \nabla f_i(x^k)$.

**Remark 4.1.** Nel contesto del **machine learning** e dell'apprendimento statistico:

- Ogni termine $f_i$ corrisponde alla **perdita associata a un campione**.
- Un sottoinsieme $B_k$ di esempi è detto _mini-batch_, in contrasto con il *full batch*, che include l'intero dataset.

Nel contesto del **deep learning**, il passo $\alpha_k$ è comunemente noto come **learning rate**.

Le tecniche di mini-batching e le strategie stocastiche sono spesso combinate con un *rimescolamento casuale*: Invece di scegliere gli indici in $B_k$ completamente a caso a ogni iterazione, si effettuano **macro-iterazioni** (chiamate *epoche*), in cui ==tutti i termini della somma sono usati esattamente una volta==.

La struttura di un algoritmo di **mini-batch SGD con random reshuffling** è mostrata in _Algorithm 5_.
Praticamente entro ogni epoca (indicizzata da $k$), sono eseguite $\frac{N}{M}$ iterazioni (indicizzate da $t$) del minibatch GD, successivamente un diverso minibatch della funzione viene considerato, in modo tale che non ci sia overlap e dentro ogni epoca ogni termine viene considerato una ed una sola volta. Nota che che il random split in minibatches è diverso per ogni epoca.

#### 4.8.1 Analisi Teorica del SGD

In questa sezione, riportiamo l'analisi di convergenza per l'analisi di un metodo SGD base, dove un singolo e randomico sample è scelto per approssimare il gradiente ad ogni iterazione; seguendo  i passi della forma (19).

---
**Algoritmo 5: Mini-batch Discesa del Gradiente con Rimescolamento randomico**

18. Input: $f_1, ... , f_n, \space x^0, \space \{\alpha_k\}$
19. $k=0$
20. **while** un criterio di arresto non è soddisfato fai
	- Dividi randomicamente l'insieme di indici {1,...,N} in $\frac{N}{M}$ mini-batches $B_0^k, B_{\frac{N}{M} -1}$ di dimensione M
	- $x_0^k = x_k$
	- **for** $t = 0, ..., \frac{N}{M}$ fai
		- $x_{t+1}^k = x_t^k - \alpha \frac{1}{M} \sum_{i \in B_{t^k}} \nabla f_i(x_t^k)$ 
	- $x^{k+1} = x_{\frac{N}{M}}^k$
21. Output: $x^k$

---

Diversamente dall'algoritmo di discesa del gradiente, SGD non necessariamente abbassa il valore della funzione obiettivo ad ogni passo. 

Per studiare rigorosamente l'SGD, si introducono alcune ipotesi aggiuntive che caratterizzano quanto lontano i campioni del gradiente possono distare da questo:

22. $f$ è **limitata inferiormente**.
23. Il modulo dei campioni di gradiente è limitato da una costante $G > 0: \|\nabla f_i(x)\| \leq G, \quad \forall x \in \mathbb{R}^n$.
24. La funzione obiettivo è _L-lipschitziana_ (L-smooth).

---
**Proposizione 4.14**

Sia $\{x^k\}$ la sequenza generata dall'algoritmo SGD con una sequenza di passi $\{\alpha_k\}$ tale che:

- $\sum_{k=0}^\infty \alpha_k = \infty$,
- $\sum_{k=0}^\infty \alpha_k^2 < \infty$.

Assumendo che, a ogni iterazione $k$, l'algoritmo selezioni casualmente un $\tau \in \{0, \ldots, k-1\}$ con probabilità:

	$P(\tau = t) = \frac{\alpha_t}{\sum_{i=0}^{k-1} \alpha_i}$,

allora:
	$\lim_{k \to \infty} E\left[\|\nabla f(z^k)\|^2\right] = 0$.

---

**Dimostrazione (Schizzo male)**

Dalla proprietà di smoothness e l'ipotesi sui campioni del gradiente, si ottiene che:

	$f(x^{k+1}) \leq f(x^k) - \alpha_k \nabla f_{i_k}(x^k)^T \nabla f(x^k) + \frac{\alpha_k^2 L G^2}{2}$.

Sotto aspettazione (?) e applicando le ipotesi di $\alpha_k$, si dimostra che la successione converge in media a un punto stazionario, soddisfacendo:

	$\lim_{k \to \infty} E[\|\nabla f(z^k)\|^2] = 0$

---

**Proposizione 4.15**

Sia $\{x^k\}$ la sequenza generata dall'algoritmo SGD con una sequenza di passi $\{\alpha_k\}$ tale che:

- $\sum_{k=0}^\infty \alpha_k = \infty$,
- $\sum_{k=0}^\infty \alpha_k^2 < \infty$.

Allora:
	$\liminf_{k \to \infty} \|\nabla f(x^k)\| = 0$.

---

La proposizione sopra afferma che, se la regola sui passi $\{\alpha_k\}$ richiesta dalla Proposizione 4.14 è soddisfatta, possiamo ottenere un risultato di convergenza in stazionarietà, in valore atteso, per la sequenza $\{x_k\}$. 

Una regola sui passi che garantisce la convergenza in valore atteso ai punti stazionari per l'algoritmo SGD è, ad esempio: $\alpha_k = \frac{\alpha_0}{k + 1}$.

In pratica, i passi ==devono tendere a zero per garantire la convergenza, ma devono farlo "abbastanza lentamente"== da consentire all'algoritmo di raggiungere un punto stazionario.

Per la complessità dell'algoritmo, la **velocità di convergenza** dell'SGD è inferiore rispetto a quella dei metodi a batch completo (GD), come osservabile nella tabella successiva. Il limite di complessità nel caso peggiore è peggiore per l'SGD rispetto al GD nei casi non convessi, convessi e fortemente convessi. In particolare, nel caso fortemente convesso, i tassi di convergenza sono **lineari** per GD contro **sottolineari** per SGD.

| **Caso**                | **GD**                                              | **SGD**                              |
| ----------------------- | --------------------------------------------------- | ------------------------------------ |
| Non convesso $f$        | $O\left(\frac{1}{\epsilon^2}\right)$                | $O\left(\frac{1}{\epsilon^4}\right)$ |
| Convesso $f$            | $O\left(\frac{1}{\epsilon}\right)$                  | $O\left(\frac{1}{\epsilon^2}\right)$ |
| Fortemente convesso $f$ | $O\left(\log\left(\frac{1}{\epsilon}\right)\right)$ | $O\left(\frac{1}{\epsilon}\right)$   |

**Tabella 3:** Esempi di complessità per GD e SGD.

I valori nella tabella aiutano a visualizzare i trend; tuttavia, ricordiamo che i limiti sono validi asintoticamente, ovvero sono più accurati per piccoli valori di $\epsilon$

---

**Osservazioni sul comportamento**
- L'accelerazione non migliora il tasso di convergenza per SGD.
- Però a differenza del batch GD, l'SGD non nasconde nelle costanti della complessità temporale il numero N dei termini sommati nella funzione obiettivo (ovvero il costo per-iterazione è molto più piccolo di quello del batch GD).

L'**efficienza del GD rispetto all'SGD** si osserva solo per valori molto piccoli di $\epsilon$, cioè ==quando è richiesta un'elevata accuratezza nella soluzione== (vedi Figura sotto). Questo è uno dei motivi principali per cui il **minibatch GD** ($1 < |B| = M \ll N$), rappresentando una via di mezzo tra batch e stochastic GD, è nella pratica l'approccio più efficace nelle applicazioni.

![[Pasted image 20250204183712.png]]

## 5. Algoritmi di ottimizzazione vincolata

TBD (Per ora vedi Pdf notes_palchetti_2023/ notes_senoner_2024)

## 6. Problemi di Ottimizzazione nel Machine Learning: Concetti di Base

### 6.1 Introduzione

Il machine learning non è **ottimizzazione**. Il machine learning è un ramo dell’intelligenza artificiale che si è dimostrato estremamente efficace in numerosi compiti negli ultimi anni; il suo successo è probabilmente attribuibile alle forti proprietà statistiche possedute dai modelli di apprendimento, che permettono di sfruttare correttamente la grande quantità di dati oggi disponibile; inoltre, l’enorme progresso in corso degli strumenti hardware e software ha giocato un ruolo cruciale nel rendere i sistemi di apprendimento effettivamente impiegabili.

Tuttavia, l’*ottimizzazione matematica* è un elemento centrale per questa tecnologia: spesso si utilizza la metafora del "motore". Infatti, il processo di addestramento di un sistema di apprendimento consiste, per la stragrande maggioranza dei modelli, nella risoluzione di un problema di ottimizzazione. Molte librerie di machine learning sono diventate popolari e ampiamente utilizzate negli ultimi anni; in ciascuna di esse, premere il "pulsante di esecuzione" non fa altro che ==avviare un algoritmo di ottimizzazione.==

Per questa ragione, è estremamente importante per gli esperti e gli ingegneri di machine learning conoscere in dettaglio i meccanismi di questi processi; questo è particolarmente vero per essere in grado di interpretare comportamenti anomali e correggere i problemi che frequentemente si verificano nella progettazione e implementazione dei sistemi di apprendimento.

Nel corso di questo capitolo, ci concentreremo sugli algoritmi di ottimizzazione più rilevanti impiegati nei compiti di apprendimento supervisionato. 
Consideriamo quindi un dataset:

	$D = \left\{ (x^{(i)}, y^{(i)}) \mid x^{(i)} \in X, y^{(i)} \in Y, i = 1, \dots, n \right\}$

dove $X \subseteq \mathbb{R}^p$ ed $Y = \mathbb{R}$ (compiti di regressione) oppure $Y = \{0,1\}$ (compiti di classificazione binaria). Il dataset rappresenta un **campionamento** da una qualche distribuzione, dove esiste una relazione $f$ tra le coppie $(x, y)$, tale che $f(x) = y$.

L’obiettivo del machine learning è costruire, basandosi sulle coppie in $D$, una funzione $\hat{f}$ che catturi *l’essenza* di $f$, essendo in grado di fornire "accuratamente" valori di $\hat{y} = \hat{f}(x)$ per punti $x$ che **non sono presenti** nel set di addestramento $D$.

L’addestramento è tipicamente modellato come un problema di ottimizzazione (**minimizzazione del rischio empirico**), dove una *funzione di perdita* deve essere minimizzata rispetto ai parametri $w$ del modello $f$.

La forma usuale dei problemi di ottimizzazione per l’addestramento è:

	$\min_{w} L(w) = \frac{1}{n} \sum_{i=1}^{n} \ell(f(x^{(i)};w), y^{(i)})$ (20)

cioè, vogliamo **minimizzare** la somma finita di termini **che possono avere forme diverse**, a seconda della specifica funzione di perdita impiegata; alcuni esempi di funzioni di perdita sono:

- **Loss quadratica:** $\ell(u, v) = (u - v)^2$ (regressione);
- **Loss $\ell_1$:** $\ell(u, v) = |u - v|$ (regressione);
- **Loss logaritmica:** $\ell(u, v) = -(u \log(v) + (1 - u) \log(1 - v))$ (classificazione binaria);
- **Loss 0-1:** $\ell(u, v) = 1 - \mathbb{1}\{u = v\}$ (classificazione binaria);
- **Hinge loss:** $\ell(u, v) = \max\{0, 1 - uv\}$ (classificazione binaria).

Ora, essere in grado di risolvere efficacemente il problema di ottimizzazione (20) non è sufficiente per garantire che il modello risultante funzioni bene su dati fuori campione; si verificano spesso due situazioni sfortunate:

- Se la qualità dei dati è **scarsa**, o se il modello è **troppo semplice** rispetto alla distribuzione dei dati, non è possibile identificare una buona approssimazione della “vera” $f$, anche se il problema di ottimizzazione è risolto accuratamente; questo problema è noto come ***underfitting*** e non può essere affrontato con i soli strumenti di ottimizzazione matematica.
- Il secondo problema è in qualche modo l’opposto del primo e si verifica quando il problema di ottimizzazione è risolto “troppo bene”; infatti, nel problema (20) viene utilizzata una funzione obiettivo "surrogata": si minimizza l’errore sul set di addestramento, mentre si vorrebbe minimizzare l’errore ==su tutta la distribuzione dei dati==, inclusi quelli non visti. Se il modello di apprendimento è sufficientemente espressivo (come spesso accade con i modelli parametrici di grandi dimensioni), si potrebbe ottenere una funzione di previsione molto complessa, perfettamente adattata ai dati in $D$, ma assolutamente scorretta per i dati non visti. Questo problema è noto come ***overfitting***.

Per mitigare parzialmente questo problema, solitamente si introduce un termine di **regolarizzazione** nel problema di addestramento per migliorare ==la capacità di generalizzazione== del modello di apprendimento. 
Il problema di ottimizzazione risultante è:

	$\min_{w} L(w) + \Omega(w)$,

dove il termine di regolarizzazione $\Omega(w)$ è solitamente scelto tra:

- $\Omega(w) = \|w\|_2^2$ (regolarizzazione quadratica);
- $\Omega(w) = \|w\|_1$ (regolarizzazione $\ell_1$);
- $\Omega(w) = \|w\|_0$ (regolarizzazione $\ell_0$, con $\|w\|_0 = |\{i : w_i \neq 0\}|$).

La **regolarizzazione quadratica** è la più utilizzata per la sua semplicità e le sue proprietà di regolarità. I regolarizzatori $\ell_1$ e $\ell_0$ inducono **sparsità**, con il primo che ha proprietà di regolarità molto più forti rispetto al secondo. La **sparsità** è spesso una caratteristica desiderabile nei modelli predittivi.

D’ora in avanti, non ci concentreremo sugli aspetti statistici dei modelli di apprendimento, ma considereremo solo il punto di vista della pura ottimizzazione matematica.

Infatti, si noti che l’aggiunta di un termine di regolarizzazione quadratico nel problema di ottimizzazione non solo ha un valore statistico, migliorando le proprietà di generalizzazione del modello addestrato, ma trasforma anche funzioni obiettivo convesse in funzioni **fortemente convesse**. Tenendo conto della discussione sulla complessità computazionale degli algoritmi di ottimizzazione nella Sezione 4.2.3, possiamo sottolineare che la regolarizzazione dovrebbe anche **accelerare significativamente** il processo di ottimizzazione. Inoltre, il termine di regolarizzazione rende qualsiasi funzione di perdita limitata **coerciva** (anche in assenza di proprietà di convessità), ==garantendo l’esistenza di soluzioni== per il problema di ottimizzazione sottostante.

---

### 6.2 Regressione Lineare

Il modello più semplice per i tasks di regressione è la **regressione lineare**. I regressori lineari sono solitamente ottenuti risolvendo un problema di minimi quadrati **regolarizzato**:
	
	$\min_{w \in \mathbb{R}^p} \|Aw - b\|^2 + \lambda\|w\|^2$ (22)

dove $A \in \mathbb{R}^{n \times p}$ e $b \in \mathbb{R}^{n}$. Il problema è **convesso** e può essere risolto trovando una soluzione con **gradiente nullo**.
Definendo:

	$f(w) = \|Aw - b\|^2 + \lambda\|w\|^2 = w^T A^T A w - 2w^T A^T b + \|b\|^2 + \lambda w^T w$

e calcolando il gradiente:

	$\nabla f(w) = 2A^T A w - 2A^T b + 2\lambda w$

il problema si riduce alla risoluzione del seguente sistema lineare, noto come **equazione normale**:

	$(A^T A + \lambda I)w = A^T b$ (23)

**Proposizione 6.1** Il Problema 22 ammette soluzione ottimale unica.
Dimostrazione.
La funzione obiettivo è coerciva:

	$\lim_{\|w\| \to \infty} \|Aw - b\|^2 + \lambda\|w\|^2 \geq \lim_{\|w\| \to \infty} \lambda\|w\|^2 = +\infty$ 

Per cui, dal teorema di Weierstrass.

La matrice Hessiana della funzione obiettivo è data da:

	$\nabla^2 f(w) = 2A^T A + 2\lambda I$

che è definita positiva, infatti per ogni $w \neq 0$ abbiamo:

	$2w^TA^T A w + 2w^T(\lambda I)w = 2\|Aw\|^2 + 2\lambda \|w\|^2 \geq \lambda \|w\|^2 > 0$

Dunque $f(w)$ è strettamente convessa è il minimo (globale) è unico.

---
Il sistema di equazioni (23) ha soluzione unica, che può essere calcolata:
- In forma chiusa, tramite una matrice inversa $w^* = (A^TA + \lambda I)^{-1}A^Tb$. Questo approccio può essere usato se $p$ è relativamente piccolo (il costo della matrice inversa è $O(p^3)$) e se A non è mal condizionata
- Usando un metodo iterativo, come il metodo di discesa del gradiente o quello di Newton; nei fatti il metodo del *gradiente coniugato* è spesso usato nei sistemi lineari.

#### 6.2.1 Casi senza Regolarizzatore

Il problema:

	$min_{w \in \mathbb{R}^p}\|Aw-b\|^2$ (24)

Ha proprietà simili alla sua controparte regolarizzata $\ell_2$  e può essere risolto similmente, ma far vedere che la soluzione del problema sempre esiste è un po' più complicato; inoltre la soluzione non sempre è unica, se il rango della matrice non è il massimo, la matrice Hessiana $A^TA$ non è strettamente definita positiva e $f$ non è necessariamente coerciva nè strettamente convessa.

**Proposizione 6.2** Il problema (24) ammette sempre soluzione.
Dimostrazione.
Consideriamo il problema:
	
	$min_z \frac{1}{2}\|b-z\|^2 \quad \text{t.c.} \quad A^Tz=0$

La  funzione obiettiva del problema è coerciva e l'insieme raggiungibile(?) è chiuso, dunque il problema ammette una soluzione.
Siccome inoltre la funzione obiettivo è quadratica e i vincoli sono lineari, le KKT sono condizioni necessarie e sufficienti per l'ottimalità: $\exists \mu^* \in \mathbb{R}^p$ tale che:

	$\nabla_z L(z^*,\mu^*) = -(b-z^*) + A\mu^* = 0 \quad \text{con} \quad A^Tz^* = 0$

Dunque, $b = z^* + A\mu^*$, con $z^* \space : \space A^Tz^*=0 \quad e \quad \mu^*\in \mathbb{R}^p$ Abbiamo ottenuto un risultato base della geometria: $b = b_R+b_N$ tale che:

	$b_R = A\mu^* \in Im(A) \quad (\exists:Ay =b_R), b_N = z^* \in Ker(A^T) \quad (A^Tb_N = 0)$

Ora, possiamo osservare che:

	$A^Tb = (A^Tz^*+A^TA\mu^*) = A^TA\mu^*$

ovvero $b_R = A\mu^*$ è la soluzione dell'equazione normale.

### 6.3 Classificatori Lineari e Regressione Logistica

In questa sezione affrontiamo il problema dell'addestramento di un modello di **regressione logistica**. 
Il problema di ottimizzazione per questo modello ha la seguente forma:

	$\min_{w \in \mathbb{R}^p} L(w) + \lambda \Omega(w)$

dove $L(w)$ è la funzione di **log-verosimiglianza negativa** del modello logistico, che è una funzione convessa, e $\Omega(w)$ è un regolarizzatore convesso. Si noti che questa impostazione è concettualmente equivalente ad altri problemi di addestramento con funzioni di perdita convesse, come la **regressione softmax** o il fitting di modelli **ARMA** nelle serie temporali.

Per risolvere problemi di questa forma, è necessario un algoritmo iterativo di ottimizzazione; metodi come **discesa del gradiente** o **metodo di Newton** sono opzioni valide. Tuttavia, l'algoritmo **L-BFGS** è generalmente considerato il metodo più efficiente per l'ottimizzazione non vincolata, sia nel caso convesso che in quello non convesso (quando non è richiesta l'ottimalità globale), anche per problemi di dimensioni considerevoli. Per dataset di grandi dimensioni, può essere considerato anche un metodo di tipo **SGD**.
#### Regressione logistica 

Mostriamo ora come calcolare il **gradiente** e la **matrice Hessiana** per il problema della regressione logistica. Consideriamo una classificazione binaria con \(Y = \{-1,1\}\).
La funzione di perdita ha la forma:

	$L(w; X, y) = \sum_{i=1}^{n} \log(1 + \exp(-y^{(i)} w^T x^{(i)}))$
##### Calcolo Gradiente ed Hessiana (da saltare senza problemi)

Se definiamo $z = Xw$ (cioè $z_i = w^T x^{(i)}$ per ogni $i$), possiamo riscrivere la funzione di perdita come:

	$L(w; X, y) = \varphi(z; y) = \sum_{i=1}^{n} \log(1 + \exp(-y^{(i)} z_i))$
	
Vogliamo ora calcolare $\nabla_w L(w; X, y)$; applicando la *regola della catena multivariata*, otteniamo:

	$\nabla_w L(w; X, y)^T = \nabla_z \varphi(Xw; y)^T \frac{\partial}{\partial w} (Xw)$

Osserviamo inoltre che:

	$\frac{\partial}{\partial z_i} \varphi(z; y) = \frac{\partial}{\partial z_i} \left( \log(1 + \exp(-y^{(i)} z_i)) \right)$

Svolgendo il calcolo della derivata:

	$\frac{1}{1 + \exp(-y^{(i)} z_i)} \cdot \exp(-y^{(i)} z_i) \cdot (-y^{(i)}) = -y^{(i)} \frac{1}{1 + \exp(y^{(i)} z_i)} = -y^{(i)} \sigma(-y^{(i)} z_i)$

dove $\sigma(\cdot)$ è la **funzione sigmoide**. Quindi, possiamo scrivere:

	$\nabla_z \varphi(z; y) = (-y^{(1)} \sigma(-y^{(1)} z_1), \dots, -y^{(n)} \sigma(-y^{(n)} z_n))^T$

D'altra parte, abbiamo:

	$\frac{\partial}{\partial w} (Xw) = X$

quindi otteniamo il gradiente della funzione di perdita:

	$\nabla_w L(w; X, y) = (r^T X)^T = X^T r$

dove $r \in \mathbb{R}^n$ è definito come:

	$r_i = -y^{(i)} \sigma(-y^{(i)} w^T x^{(i)}) \quad \text{per ogni } i = 1, \dots, n$

Con calcoli analoghi, possiamo ottenere la matrice Hessiana:

	$\nabla^2 L(w; X, y) = X^T D X$

dove \(D\) è una matrice diagonale con elementi:

	$d_{ii} = \sigma(y^{(i)} w^T x^{(i)}) \cdot \sigma(-y^{(i)} w^T x^{(i)})$

## 7. Support Vector Machines

Un modello di **Support Vector Machine (SVM)** lineare è, in breve, un modello di classificazione ottenuto risolvendo il problema di minimizzazione del ==rischio empirico con la **hinge loss** e il regolarizzatore $\ell_2$==, ossia:

	$\min_{w,b} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^{n} \max\{0, 1 - y^{(i)} (w^T x^{(i)} + b)\}$

Si può notare che le soluzioni ottimali di questo problema di ottimizzazione **non liscio e non vincolato** sono anche soluzioni del seguente problema **liscio con vincoli lineari**:

	$\min_{w,b,\xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^{n} \xi^{(i)}$
										(26)
	$\text{t.c} \quad y^{(i)} (w^T x^{(i)} + b) \geq 1 - \xi^{(i)}, \quad \xi^{(i)} \geq 0$ 

Si può dimostrare che, quando $C = \infty$, il problema corrisponde a trovare, tra gli ==iperpiani che separano **perfettamente** i dati di addestramento==, quello che **massimizza la distanza** dal punto più vicino di entrambe le classi (vedi Figure 10 e 11). 

![[Pasted image 20250201164438.png]]
Figura 10: Classificazione tramite Iperpiani. Tutti gli iperpiani soddisfano correttamente il problema dell'addestramento dei dati. SVM sceglie fra questi quello che è equidistante fra le due classi(in verde).

![[Pasted image 20250201164501.png]]
Figura 11: Iperpiani di massimo margine. I punti cerchiati, che definiscono i margini di separazione sono chiamati _support vectors_.

Tuttavia, se i dati non sono **linearmente separabili**, il problema non ha soluzioni ammissibili (Figura 12).

![[Pasted image 20250201163933.png]]
Figura 12: Esempio di un dataset non separabile.

Pertanto, con una scelta finita di $C$, si accetta di ==**pagare un costo** per tutti i punti classificati **erroneamente**,== nonché per quelli classificati **correttamente ma con una confidenza insufficiente** (Figura 13). Questo non solo garantisce l'esistenza di una soluzione, ma aiuta anche ad **evitare problemi di overfitting**.

![[Pasted image 20250201164411.png]]
Figura 13: Classificatori SVM ottenuti lasciando liberi _slacks_ non nulli.

Il problema (26) è **quadratico convesso con vincoli lineari**, quindi è in teoria risolvibile tramite solutori standard per problemi vincolati, come l'**algoritmo di Frank-Wolfe**. Tuttavia, il numero di vincoli è **proporzionale al numero di punti di addestramento** e può crescere rapidamente. 

Per questa ragione (e per altre che vedremo in seguito), si segue una strategia differente: l'analisi del **problema duale**.
### 7.1 Il Problema Duale

Come accennato, il problema (26) è **convesso e quadratico con vincoli lineari**. Questo implica che le **condizioni di Karush-Kuhn-Tucker (KKT)** sono **necessarie e sufficienti** per l'ottimalità. 

Senza entrare nei dettagli di un argomento vasto e complesso, introduciamo un risultato dalla **teoria della dualità** per problemi convessi vincolati, che permetterà di riformulare il problema primale in una forma più trattabile.

---
#### Proposizione 7.1 

Consideriamo il seguente problema di ottimizzazione:

	$\min_{x} f(x) \quad \text{soggetto a} \quad g(x) \leq 0$

dove $f$ e $g$ sono funzioni continuamente differenziabili e convesse.  

Sia $x^\star$ una soluzione ottimale del problema e supponiamo che esista un vettore di moltiplicatori $\mu^\star$ tale che $(x^\star, \mu^\star)$ soddisfi le **condizioni KKT**.  
Allora, la coppia $(x^\star, \mu^\star)$ è una **soluzione ottimale** del **problema duale di Wolfe**:

	$\max_{x, \mu} L(x, \mu) = f(x) + \mu^T g(x)$

	$\text{t.c.} \quad \nabla_x L(x, \mu) = 0, \quad \mu \geq 0$

---
**Dimostrazione**.  
La coppia $(x^\star, \mu^\star)$ soddisfa le condizioni KKT, ossia:

- $\nabla_x L(x^\star, \mu^\star) = 0$ (i),
- $\quad \mu^\star \geq 0$ (ii), 
- $\quad g(x^\star) \leq 0$ (iii),
- $\quad \mu^\star_i g_i(x^\star) = 0 \quad \forall i$ (iv)

Di conseguenza, $(x^\star, \mu^\star)$ soddisfa i vincoli del problema duale di Wolfe (grazie a (i) e (ii)). 

Inoltre, per la condizione di complementarità (iv), abbiamo:
	
	$L(x^\star, \mu^\star) = f(x^\star) + \sum_i \mu^\star_i g_i(x^\star) = f(x^\star)$

Ora, per una qualunque soluzione ammissibile $(x, \mu)$ del problema duale, poiché $\mu \geq 0$  e $g(x^\star) \leq 0$, si ha:

	$L(x^\star, \mu^\star) = f(x^\star) \geq f(x^\star) + \sum_i \mu_i g_i(x^\star) = L(x^\star, \mu)$

Dalla convessità di $L(x, \mu)$ rispetto a $x$ (essendo combinazione lineare positiva delle funzioni convesse $f, \space g_1, \dots, g_m$), possiamo scrivere:

	$L(x^\star, \mu) \geq L(x, \mu) + \nabla_x L(x, \mu)^T (x^\star - x)$

Unendo tutti i passaggi precedenti e ricordando che $\nabla_x L(x, \mu) = 0$ per $(x, \mu)$ ammissibile nel problema duale, otteniamo:

	$L(x^\star, \mu^\star) \geq L(x^\star, \mu) \geq L(x, \mu)$

Essendo $(x, \mu)$ una soluzione qualsiasi ammissibile del problema duale, si ottiene la tesi(richiediamo infatti che sia un max).

---

Torniamo ora al problema SVM (26).  
Poiché le condizioni KKT sono **necessarie e sufficienti** per l'ottimalità globale, allora per una soluzione ottimale $(w^\star, b^\star, \xi^\star)$  devono esistere moltiplicatori  $(\alpha^\star, \mu^\star)$ tali che la **coppia** $(w^\star, b^\star, \xi^\star, \alpha^\star, \mu^\star)$ sia un punto KKT e, per la proposizione sopra, sia soluzione del **problema duale**:

	$\max_{w, b, \xi, \alpha, \mu} L(w, b, \xi, \alpha, \mu) = f(x) + \mu^Tg(x)$
			  $= \frac{1}{2} \|w\|^2 + C \sum_i \xi_i + \sum_i -\mu_i \xi_i + \sum_i \alpha_i (1 - y^{(i)} (w^T x^{(i)} + b) - \xi_i)$

	$\text{t.c} \quad \alpha \geq 0, \quad \mu \geq 0$,

	$\nabla_w L(w, b, \xi, \alpha, \mu) = 0, \quad \nabla_b L(w, b, \xi, \alpha, \mu) = 0, \quad \nabla_\xi L(w, b, \xi, \alpha, \mu) = 0$

Osserviamo ora che dai vincoli sopra si ottengono le seguenti relazioni:

	$0 = \nabla_w L(w, b, \xi, \alpha, \mu) = w - \sum_i \alpha_i y^{(i)} x^{(i)}, \quad \text{cioè} \quad w = \sum_i \alpha_i y^{(i)} x^{(i)}$

	$0 = \nabla_b L(w, b, \xi, \alpha, \mu) = -\sum_i \alpha_i y^{(i)}, \quad \text{cioè} \quad \alpha^T y = 0$
	
	$0 = \nabla_\xi L(w, b, \xi, \alpha, \mu) = C e - \sum_i \mu_i e_i - \sum_i \alpha_i e_i, \quad \text{cioè} \quad \alpha_i = C - \mu_i \leq C \quad \forall i$
	
Manipolando la funzione obiettivo, possiamo prima ottenere:

	$\frac{1}{2} w^T w + C \sum_{i} \xi_i + \sum_{i} -\mu_i \xi_i + \sum_{i} \alpha_i - \sum_{i} \alpha_i y^{(i)} w^T x^{(i)} - b \sum_{i} \alpha_i y^{(i)} - \sum_{i} \alpha_i \xi_i$

Ora, ricordiamo che $\sum_{i} \alpha_i y^{(i)} = 0$ per la seconda condizione vista sopra. Inoltre, usando la terza condizione possiamo scrivere:

	$C \sum_{i} \xi_i - \sum_{i} \mu_i \xi_i = \sum_{i} \xi_i (C - \mu_i) = \sum_{i} \xi_i \alpha_i$

Otteniamo quindi:

	$\frac{1}{2} w^T w + \sum_{i} \alpha_i \xi_i + \sum_{i} \alpha_i - \sum_{i} \alpha_i y^{(i)} w^T x^{(i)} - \sum_{i} \alpha_i \xi_i$

ossia:

	$w^T \left(\frac{1}{2} w - \sum_{i} \alpha_i y^{(i)} x^{(i)}\right) + \sum_{i} \alpha_i$

Ora possiamo sostituire $w = \sum_{i} \alpha_i y^{(i)} x^{(i)}$ per ottenere:

	$L(w, b, \xi, \alpha, \mu) = -\frac{1}{2} \sum_{i} \sum_{j} \alpha_i \alpha_j y^{(i)} y^{(j)} x^{(i)T} x^{(j)} + \sum_{i} \alpha_i$

Quindi, la funzione obiettivo dipende **solo dai moltiplicatori $\alpha$**, che sono vincolati da $y^T \alpha = 0$, $\alpha \geq 0$ e $\alpha \leq C$. Scambiando i segni e passando alla notazione matriciale, definiamo la matrice $Q$ tale che: $Q_{ij} = y^{(i)} y^{(j)} x^{(i)T} x^{(j)}$, ottenendo il problema duale (27):

	$\min_{\alpha} \frac{1}{2} \alpha^T Q \alpha - e^T \alpha$
	$\text{t.c.} \quad \alpha^T y = 0, \quad 0 \leq \alpha_i \leq C \quad \forall i$

(Notare si passa facilmente al min cambiando il segno della funzione obiettivo)

---

Dopo aver risolto il problema duale (27), possiamo ottenere la soluzione $\alpha^\star$ e recuperare le altre variabili:
- $w^\star = \sum_{i} \alpha^\star_i y^{(i)} x^{(i)}$,
- $\mu^\star_i = C - \alpha^\star_i \quad \forall i$,
- $b^\star = \frac{1}{y^{(i)}} - w^{\star T} x^{(i)} \quad \text{per ogni } i \text{ tale che } \alpha^\star_i \in (0, C)$,
- $\xi^\star_i = \max\{0, 1 - y^{(i)} (w^{\star T} x^{(i)} + b^\star)\}$

La terza equazione (per $b^\star$) segue dall'imposizione delle condizioni di complementarità delle KKT. (ovvero imponendo $\xi_i^* = 0 \space e \space \alpha_i^* \neq 0$ necessariamente avrò $1- y^{(i)}(w^{*T}x^{(i)}) + b^*=0$ dalla condizione $\mu^Tg_i(x) \leq 0$, anzi vedi sotto... )

---
##### Interpretazione Geometrica: Support Vectors

Dalle condizioni di complementarità segue che:

	$\alpha^\star_i (1 - y^{(i)} (w^{\star T} x^{(i)} + b^\star) - \xi^\star_i) = 0, \quad 0 = \mu^\star_i \xi^\star_i = (C - \alpha^\star_i) \xi^\star_i$

- Se $\alpha^\star_i \in (0, C)$, allora $\xi^\star_i = 0$  e il punto soddisfa esattamente  $y^{(i)} (w^{\star T} x^{(i)} + b^\star) = 1$, ovvero si trova **sul margine di separazione**.
- Se $\alpha^\star_i = C$, allora $\xi^\star_i > 0$, (negativo non può essere per i vincoli del problema), indicando che il punto è un errore di classificazione(in quanto ha uno _slack_ non nullo).

Tutti i punti associati a **moltiplicatori non nulli** $\alpha^\star_i$ sono chiamati **support vectors**, poiché:

	$w^\star = \sum_{i} \alpha^\star_i y^{(i)} x^{(i)}$

ovvero classificatore risultante dipende esclusivamente dai **support vectors**.

Per classificare un nuovo punto $x$, calcoliamo:

	$w^{\star T} x = \sum_{i} \alpha_i y^{(i)} x^T x^{(i)}$

In altre parole, il risultato della funzione decisionale è una ==somma pesata sui dati di addestramento==, dove solo i **support vector** (ovvero quelli con moltiplicatore non nullo) vengono effettivamente considerati. 
Per ciascun support vector, viene calcolato il **prodotto scalare** con il punto da classificare: ==più alto è il prodotto scalare, maggiore è la somiglianza== tra $x^{(i)}$ e $x$, più grande sarà il contributo di quel support vector nell'assegnare la classe $y^{(i)}$ al nuovo punto dati.

Tuttavia, il prodotto scalare **non è l'unica misura di somiglianza** disponibile per confrontare due punti dati. Infatti, possiamo pensare di sostituire i termini $x^T x^{(i)}$ nella funzione decisionale con **funzioni di kernel**:  $k(\cdot, \cdot) : \mathbb{R}^p \times \mathbb{R}^p \to \mathbb{R}$. 

![[Pasted image 20250202130559.png]]

In questo caso, gli elementi della matrice $Q$ nel problema duale (27) diventano:

	$Q_{ij} = y^{(i)} y^{(j)} k(x^{(i)}, x^{(j)})$

Senza addentrarci nella teoria dei kernel, ricordiamo che una funzione $k$ può essere usata come kernel se e solo se:
- La matrice $Q$ è **semidefinita positiva** per ogni possibile dataset $D$ (garantendo che il problema duale sia convesso).
- La funzione kernel rappresenta un **prodotto scalare** tra i punti dati mappati in uno spazio di dimensione potenzialmente maggiore.

In questi casi, la funzione decisionale assume la forma:

	$h(x) = \sum_{i} \alpha^\star_i y^{(i)} k(x, x^{(i)})$

che in generale **non è più una funzione lineare.** 

Da un lato, non è più possibile esprimere il classificatore in termini di pesi $w$; 
dall'altro, il classificatore diventa **non lineare**, consentendo di costruire modelli **più espressivi** e potenti.

![[Pasted image 20250202130901.png]]

Per riassumere, le due principali ragioni per considerare il **problema duale** della SVM sono:
1. **Kernel trick:** consente di ottenere **classificatori non lineari** senza esplicitamente trasformare i dati in uno spazio di dimensione più elevata.
2. **Forma del problema:** il problema rimane **quadratico convesso con vincoli lineari**, come nella formulazione primale, ma con vincoli più semplici (l'unico vincolo complesso è $\alpha^T y = 0$, il resto sono vincoli di box).

### 7.2 Risolvendo il problema duale

Prima di riprendere il problema duale riguardare tecniche di decomposizione (capitolo 4.7)

In questa sezione mostriamo come il problema duale per l'addestramento di un SVM **non lineare** può essere risolto in modo efficiente. Richiamiamo prima la formulazione con alcune modifiche nella notazione per renderla più chiara dal punto di vista dell'ottimizzazione (28):

	$\min \frac{1}{2} x^T Q x - e^T x$

	$\text{t.c} \quad a^T x = 0, \quad 0 \leq x \leq C$

dove $Q \in \mathbb{R}^{n \times n}$ è una matrice semi-definita positiva ($n$ è la dimensione del set di addestramento) e $e = (1, \dots, 1)^T$. Tipicamente, $n$ è grande e $Q$ è densa, fattori che contribuiscono alla difficoltà del problema. Un'ulteriore fonte di complessità è il vincolo lineare $a^T x = 0$. I vincoli box sono invece più facili da trattare, poiché sono **separabili per componente.**

Questo problema è risolto in modo efficiente attraverso una strategia di decomposizione: a ogni iterazione 
viene selezionato un **working set** $W \subset \{1, \dots, n\}$, con complemento $\overline{W} = \{1, \dots, n\} \setminus W$.

Il sottoproblema risultante (29) è quindi:

	$\min_{x_W} f (x_W , x_{\overline{W}^k}) = \frac{1}{2} x_W^T Q_{W W} x_W - (e_W - Q_{W \overline{W}} x_{\overline{W}^k})^T x_W$

	$\text{t.c.} \quad a_W^T x_W = -a_{\overline{W}}^T x_{\overline{W}^k}, \quad 0 \leq x_W \leq C$

la cui soluzione è $x_W^\star$. Di conseguenza, le variabili vengono aggiornate come segue:

	$x_i^{k+1} = \begin{cases} x_i^\star, & \text{se } i \in W, \\ x_i^k, & \text{se } i \notin W\end{cases}$

A questo punto sorgono due domande.
La prima riguarda la cardinalità minima di $W$: deve valere $|W| \geq 2$. Se fosse $W = \{i\}$, allora si avrebbe sempre $x^{k+1} = x^k$, poiché entrambi soddisfano il vincolo $a_W^T x_W = -a_{W^c}^T x_W^k$. (In particolare se prendessimo la cardinalità pari a 1, avremmo un valore sempre costante come soluzione che non ci permette alcuna condizione di discesa)

Gli **algoritmi di decomposizione** si classificano in base alla cardinalità del working set:
- Se $|W| = 2$, si parla di **Sequential Minimal Optimization (SMO)**, che non richiede l'uso di un solutore per il sottoproblema.
- Se $|W| > 2$, l'algoritmo necessita di un solutore per trovare la soluzione di (29).

La seconda questione riguarda la selezione di $W$, che approfondiremo nella prossima sezione.
#### 7.2.1 Sequential Minimal Optimization (SMO)

Nel caso $|W| = 2$, il sottoproblema (29) diventa:

	$\min_{x_i, x_j} \frac{1}{2}\begin{bmatrix} x_i \\ x_j \end{bmatrix}^T\begin{bmatrix} q_{ii} & q_{ij} \\ q_{ij} & q_{jj} \end{bmatrix}\begin{bmatrix} x_i \\ x_j \end{bmatrix}- x_i -x_j + p_{\overline{W}^T} \begin{bmatrix} x_i \\ x_j \end{bmatrix}$

	$\text{t.c.} \quad a_i x_i + a_j x_j = b, \quad 0 \leq x_i, x_j \leq C$

Si tratta di un problema di programmazione **quadratica convessa in due variabili**, la cui soluzione può essere calcolata analiticamente.  
Il principale vantaggio degli **algoritmi SMO** è proprio quello di non dover impiegare alcun solutore.

Ora ci concentriamo sulla strategia di selezione delle variabili nel sottoproblema. Vogliamo ottenere un aggiornamento della forma:

	$x^{k+1} = (x_1^k, \dots, x_i^{k+1}, \dots, x_j^{k+1}, \dots, x_n^k)$

tale che sia **fattibile** e soddisfi: $f(x^{k+1}) < f(x^k)$

Per raggiungere questi obiettivi, dobbiamo identificare, a ogni passo, una direzione di discesa ammissibile ==che abbia esattamente due componenti non nulle==.

---

**Proposizione 7.2**
L'insieme delle direzioni ammissibili per il Problema (28) nel punto $\bar{x}$ è dato da:
	$D(\bar{x}) = \{ d \in \mathbb{R}^n \mid a^T d = 0, \ d_i \geq 0 \ \forall i \in L(\bar{x}), \ d_i \leq 0 \ \forall i \in U(\bar{x}) \}$

dove:

	$L(\bar{x}) = \{ i \in \{1, \dots, n\} \mid \bar{x}_i = 0 \}$

	$U(\bar{x}) = \{ i \in \{1, \dots, n\} \mid \bar{x}_i = C \}$

---

**Dimostrazione**.
Indichiamo con $S$ l'insieme ammissibile:

	$S = \{ x \in \mathbb{R}^n \mid a^T x = 0, \ 0 \leq x \leq C \}$

Sia $\bar{x} \in S$ e sia $D(\bar{x})$ l'insieme delle direzioni ammissibili in $\bar{x}$; se $d \in D(\bar{x})$, allora deve valere(Per definizione di direzione ammissibile):

	$\bar{x} + t d \in S, \quad \forall t \in [0, \bar{t}]$

per $\bar{t}$ sufficientemente piccolo. Da ciò segue:

	$a^T (\bar{x} + t d) = 0 \Rightarrow a^T \bar{x} + t a^T d = 0$

da cui otteniamo (Guarda l'insieme ammissibile):	$a^T d = 0$ (31)

Inoltre, deve valere: $0 \leq \bar{x} + t d \leq C$,

il che implica:

	$\begin{cases}d_i \leq 0 \text{ se } \bar{x}_i = C \quad(32) \\ d_i \geq 0 \text{ se } \bar{x}_i = 0\end{cases}$

Combinando le condizioni precedenti otteniamo la tesi.

---

Stiamo cercando direzioni in $D(\bar{x})$ con due sole componenti non nulle tali che:

	$d_{i,j}^T = (0, \dots, d_i, \dots, d_j, \dots, 0)$ (33)

Poiché $a^T d_{i,j} = 0$, abbiamo: $a_i d_i + a_j d_j = 0$.

Possiamo quindi scegliere: $d_i = \frac{1}{a_i}, \quad d_j = -\frac{1}{a_j}$ (34)

Se $i \in L(\bar{x})$, cioè $\bar{x}_i = 0$, allora $d_i \geq 0$, quindi possiamo considerare solo variabili con $a_i > 0$.  
Viceversa, se $i \in U(\bar{x})$, allora $d_i \leq 0$ e possiamo considerare l'$i$-esima componente solo se $a_i < 0$.

Analogamente, se $j \in L(\bar{x})$ si deve avere $a_j < 0$, mentre se $j \in U(\bar{x})$ deve valere $a_j > 0$.  

| Indice $i, j$    | $i \in L(\bar{x})$ | $i \in U(\bar{x})$ | $j \in L(\bar{x})$ | $j \in U(\bar{x})$ |
| ---------------- | ------------------ | ------------------ | ------------------ | ------------------ |
| Valore variabile | $\bar{x}_i = 0$    | $\bar{x}_i = C$    | $\bar{x}_j = 0$    | $\bar{x}_j = C$    |
| Direzione amm.   | $d_i \geq 0$       | $d_i \leq 0$       | $d_j \geq 0$       | $d_j \leq 0$       |
| Coeff. vincolo   | $a_i > 0$          | $a_i < 0$          | $a_j < 0$          | $a_j > 0$          |

Osserviamo che se $0 < \bar{x}_i < C$ non vi è alcun vincolo sul segno di $a_i$, e lo stesso vale per $a_j$.  
Possiamo quindi suddividere gli insiemi $L$ e $U$ come segue:

	$L(\bar{x}) = L^+ (\bar{x}) \cup L^- (\bar{x}), \quad U(\bar{x}) = U^+ (\bar{x}) \cup U^- (\bar{x})$,

dove:

	$L^- (\bar{x}) = \{ h \in L(\bar{x}) \mid a_h < 0 \}, \quad L^+ (\bar{x}) = \{ h \in L(\bar{x}) \mid a_h > 0 \}$

	$U^- (\bar{x}) = \{ h \in U(\bar{x}) \mid a_h < 0 \}, \quad U^+ (\bar{x}) = \{ h \in U(\bar{x}) \mid a_h > 0 \}.$

Infine, definiamo gli insiemi:

	$R(\bar{x}) = L^+ (\bar{x}) \cup U^- (\bar{x}) \cup \{ i \mid 0 < \bar{x}_i < C \}$ (direzioni pos)

	$S(\bar{x}) = L^- (\bar{x}) \cup U^+ (\bar{x}) \cup \{ i \mid 0 < \bar{x}_i < C \}$ (direzioni neg)

---

**Proposizione 7.3**
La direzione $d_{i,j}$ definita come in (33)-(34) è ammissibile in $\bar{x}$ per il Problema (28) se e solo se $i \in R(\bar{x})$ e $j \in S(\bar{x})$.

**Dimostrazione**
Sia $d_{i,j}$ una direzione ammissibile e supponiamo per assurdo che $j \notin S(\bar{x})$. Allora si ha che $j \in L^+(\bar{x})$ oppure $j \in U^-(\bar{x})$. Tuttavia, nel primo caso:

	$d_j = -\frac{1}{a_j} < 0$

mentre nel secondo caso:

	$d_j = -\frac{1}{a_j} > 0$

Entrambi i casi violano **l’ammissibilità** della direzione $d_{i,j}$.  
Un ragionamento analogo vale per $i \notin R(\bar{x})$, il che completa la dimostrazione.

D'altra parte, se $i \in R(\bar{x})$ e $j \in S(\bar{x})$, supponiamo in particolare $i \in U^-(\bar{x})$ e $j \in U^+(\bar{x})$.  
Allora, vale la relazione:

	$a^T d_{i,j} = a_i \frac{1}{a_i} - a_j \frac{1}{a_j} = 0$

Inoltre, poiché $i \in U^-(\bar{x})$, segue che $a_i < 0$ e quindi:

	$d_i = \frac{1}{a_i} < 0$

Analogamente, $j \in U^+(\bar{x})$ implica $a_j > 0$ e quindi:

	$d_j = -\frac{1}{a_j} < 0$

Questo conclude la dimostrazione.

---

**Proposizione 7.4**
La direzione $d_{i,j}$ definita come in (33)-(34) è una direzione di discesa per il Problema (28) se e solo se:

	$\frac{\nabla_j f (\bar{x})}{a_j} < \frac{\nabla_i f (\bar{x})}{a_i}$

**Dimostrazione**
Poiché $f$ è una funzione quadratica convessa, l==a direzione $d$ è una direzione di discesa in $\bar{x}$ se e solo se:==

	$\nabla f (\bar{x})^T d_{i,j} < 0$

Esplicitando il prodotto scalare otteniamo:

$\frac{1}{a_i} \nabla_i f (\bar{x}) - \frac{1}{a_j} \nabla_j f (\bar{x}) < 0$

da cui segue la condizione: $\frac{\nabla_j f (\bar{x})}{a_j} < \frac{\nabla_i f (\bar{x})}{a_i}$

---
##### **Algoritmo 6: Sequential Minimal Optimization (SMO)**
Di seguito riportiamo il procedimento generale dell’algoritmo SMO.

---

1. **Input**: $Q$, $a$ (vettore dei coefficienti), $C$  
2. $x^0 = 0$;  
3. $k = 0$;  
4. $\nabla f (x^0) = -e$.
5. **Ciclo fino al soddisfacimento del criterio di arresto**:
   - Selezionare $i \in R(x^k)$,  $j \in S(x^k)$ tali che:
		 $\frac{\nabla_j f (x^k)}{a_j} < \frac{\nabla_i f (x^k)}{a_i}$

   - Definire il working set: $W = \{i, j\}$.

   - Risolvere analiticamente il problema:
     $\min_{x_W} f (x_W, x^k_{\overline{W}}) \quad \text{s.t.} \quad a_W^T x_W = -a_{\overline{W}}^T x^k_{\overline{W}}, \quad 0 \leq x_W \leq C$

   - Sia $x^*_W$ la soluzione trovata al passo precedente.
	   - Aggiornare le variabili:
	     $x^{k+1}_h = \begin{cases} x^*_j & \text{se } h = j, \\ x^*_i & \text{se } h = i, \\x^k_h & \text{altrimenti}     \end{cases}$

   - Aggiornare il gradiente:
	$\nabla f (x^{k+1}) = \nabla f (x^k) + Q_i (x^{k+1}_i - x^k_i) + Q_j (x^{k+1}_j - x^k_j)$
   - Incrementare $k$

6. **Output**:  Restituire $x^k$

---

La selezione degli indici $i, j$ garantisce che $x^{k+1}$ rimanga ammissibile e che $f(x)$ diminuisca. L'aggiornamento del gradiente segue la formula:

  $\nabla f (x^{k+1}) = Q x^{k+1} - e = Q (x^{k+1} - x^k) + Q x^k - e$

e, poiché $Q x^{k+1}$ e $Q x^k$ differiscono solo nelle componenti $i$ e $j$, possiamo scrivere:

 $\nabla f (x^{k+1}) = \nabla f (x^k) + Q_i (x^{k+1}_i - x^k_i) + Q_j (x^{k+1}_j - x^k_j)$

Questo permette di aggiornare il gradiente ==usando solo due colonne della matrice== $Q$, con un notevole risparmio computazionale. Poiché $x^0 = 0$, si ha $\nabla f (x^0) = -e$, eliminando la necessità di calcolare il gradiente iniziale. La matrice $Q$ non è quindi mai necessaria interamente per il calcolo del gradiente, un vantaggio in termini in termini di I/O.
Ammissibilità e discesa stretta sono sufficienti a garantire convergenza globale.
#### 7.2.2 Proprietà di Convergenza di SMO con Regola di Selezione del Primo Ordine

La scelta del working set $W = \{i, j\}$ è la chiave per ottenere proprietà di convergenza per SMO.

---

**Proposizione 7.5**
Un punto $x^\star$ è un minimizzatore globale per il problema (28) se e solo se:

	$\max_{h \in R(x^\star)} \left( -\frac{\nabla_h f (x^\star)}{a_h} \right) \leq \min_{h \in S(x^\star)} \left( -\frac{\nabla_h f (x^\star)}{a_h} \right)$ (36)

**Dimostrazione**
Poiché il problema (28) è convesso con vincoli lineari, le condizioni di ottimalità KKT sono necessarie e sufficienti:

$\nabla_i L(x, \lambda, \xi, \hat{\xi}) = \nabla_i f (x) + \lambda a_i - \xi_i + \hat{\xi}_i = 0, \quad \forall i = 1, \dots, n$

	$\xi_i x_i = 0, \quad \hat{\xi}_i (x_i - C) = 0, \quad \xi, \hat{\xi} \geq 0, \quad \forall i = 1, \dots, n$

Pertanto, per $x^\star, \lambda^\star, \xi^\star, \hat{\xi}^\star$ ottimali, abbiamo:

	$\nabla_i f(x^*)+\lambda^*a_i \begin{cases}\geq 0, & \text{se } i \in L(x^\star), \\\leq 0, & \text{se } i \in U(x^\star), \\= 0, & \text{se } 0 < x^\star_i < C.\end{cases}$

e quindi:

	$\frac{\nabla_i f(x^*)}{a_i} +\lambda^*\begin{cases}\geq 0, & \text{se } i \in L^+(x^\star) \cup U^-(x^\star) , \\\leq 0, & \text{se } i \in L^-(x^\star) \cup U^+(x^\star), \\= 0, & \text{altrimenti} \end{cases}$

Segue che:

	$\begin{cases}\lambda^\star \geq -\frac{\nabla_i f (x^\star)}{a_i}, & \forall i \in L^+ (x^\star) \cup U^- (x^\star)\\ \lambda^\star \leq -\frac{\nabla_i f (x^\star)}{a_i}, & \forall i \in L^- (x^\star) \cup U^+ (x^\star),  \\\lambda^\star = -\frac{\nabla_i f (x^\star)}{a_i}, & \forall i : 0 < x^\star_i < C.\end{cases}$


Ricordando la definizione di:

	$R(x^\star) = L^+ (x^\star) \cup U^- (x^\star) \cup \{i | 0 < x^\star_i < C\}$
	
	$S(x^\star) = L^- (x^\star) \cup U^+ (x^\star) \cup \{i | 0 < x^\star_i < C\}$

otteniamo la disuguaglianza (36), completando la dimostrazione.

---

**Corollario 7.6**

Sia $x^k$ la soluzione attuale (ammissibile) e supponiamo che non sia ottimale.  
Allora esistono $i \in R(x^k)$ e $j \in S(x^k)$ tali che:

	$-\frac{\nabla_j f (x^k)}{a_j} > -\frac{\nabla_i f (x^k)}{a_i}$

**Dimostrazione**
Questo corollario è una conseguenza diretta della Proposizione 7.5.

---

**Definizione 7.1**
La **coppia più violante** (_most violating pair_) alla soluzione ammissibile e non ottimale $x^k$ del problema (28) è la coppia di indici $(i^\star, j^\star)$ definita come:

	$i^\star \in \arg \max_{h \in R(x^k)} \left( -\frac{\nabla_h f (x^k)}{a_h} \right), \quad j^\star \in \arg \min_{h \in S(x^k)} \left( -\frac{\nabla_h f (x^k)}{a_h} \right)$

---

Nel metodo SMO, possiamo selezionare la **Most Violating Pair**, ovvero la coppia di indici che viola maggiormente la condizione di ottimalità (36).

Questa strategia porta all'algoritmo **SVMlight** (Algoritmo 7), un algoritmo di decomposizione basato su SMO (Sequential Minimal Optimization) con proprietà di convergenza, storicamente impiegato nelle librerie software per la risoluzione del problema di addestramento degli SVM non lineari.

---

 **Algoritmo 7: SVMlight**
```plaintext
1  Input: Q, a, C.
2  x^0 = 0;
3  k = 0;
4  ∇f (x^0 ) = −e;
5  finchè criterio di stop non soddisfato fai
6      identifica la most violating pair (i⋆ , j⋆);
7      W = {i⋆ , j⋆};
8      risolvi analytically
		min f (xW , xkW )
		- s.t. aTW xW = −aTW xkW , 0 ≤ xW ≤ C;
9      sia x⋆W la solutione trovata allo step precedente;
10     imposta:
11         xk+1_h = x⋆h if h ∈ W,
12         xk+1_h = xkh otherwise;

13     ∇f (xk+1 ) = ∇f (xk ) + Qi⋆ (xk+1_i⋆ − xki⋆ ) 
			+ Qj⋆ (xk+1_j⋆ − xkj⋆ );
14     k = k + 1;
15  Output: xk.
````

---

**Proposizione 7.7**

La sequenza $\{x^k\}$ generata dall'algoritmo **SVMlight** ha punti limite, ognuno dei quali è una soluzione del problema (28).

---

 Discutiamo infine un possibile **Criterio di Arresto**. La condizione di ottimalità è data dalla disuguaglianza:

	$\max_{h \in R(x)} \left( -\frac{\nabla_h f (x)}{a_h} \right) \leq \min_{h \in S(x)} \left( -\frac{\nabla_h f (x)}{a_h} \right).$

Possiamo definire due quantità:

	$m(x) = \max_{h \in R(x)} \left( -\frac{\nabla_h f (x)}{a_h} \right),M(x) = \min_{h \in S(x)} \left( -\frac{\nabla_h f (x)}{a_h} \right)$

Dalla **Proposizione 7.5**, sappiamo che $x^\star$ è una soluzione ottimale se e solo se:	$m(x^\star) \leq M(x^\star)$
Dunque la seguente proposizione ci può dare un idea sul possibile criterio di arresto.

---

**Proposizione 7.8**

Siano m(x) e M(x) definiti come in (38). Allora, per ogni $\epsilon > 0$, l'algoritmo **SVMlight** produce una soluzione $x^k$ tale che:

	$m(x^k) \leq M(x^k) + \epsilon$

entro un numero finito di iterazioni.

La dimostrazione di questa proprietà richiede un ragionamento complesso, principalmente a causa della discontinuità delle funzioni m(x) e M(x).

#### 7.2.3 Working Set Selection usando informazioni del secondo ordine

Non fatte quindi non le studio :D

### 7.3 Algoritmi per SVM lineari

Uguale a 7.2.3 :D

## 8. Ottimizzazioni su larga scala per Deep Models

Prima leggere capitolo 4.8

Uno dei problemi di ottimizzazione più rilevanti oggi è l'**addestramento delle reti neurali artificiali (ANNs)**. Le ANNs rappresentano un potente modello di **apprendimento automatico** (machine learning), utilizzato con risultati impressionanti in numerose applicazioni.

L'**ottimizzazione del rischio empirico** di una rete con pesi $w \in \mathbb{R}^n$, dato un dataset $(X, Y)$ di $N$ campioni, assume la forma del problema (21), ma presenta diverse caratteristiche peculiari rispetto ai classici problemi di ottimizzazione non vincolata. In particolare:

7. **Obiettivo dell'ottimizzazione e generalizzazione**  
   Come in altri problemi di machine learning, non si cerca **realmente** di minimizzare il **rischio empirico** (che è solo una funzione obiettivo surrogata), ma piuttosto di trovare un modello **efficace in termini di generalizzazione**.  
   Il problema di addestramento, altamente **non convesso**, presenta numerosi **punti stazionari subottimali**, molti dei quali con un valore di perdita molto vicino all’ottimo globale. Tuttavia, la **prestazione fuori campione** di queste soluzioni può variare drasticamente.  
   **Non ha quindi senso cercare l’ottimo globale**, ma piuttosto individuare soluzioni locali che garantiscano una buona generalizzazione, anche se raggiunte con solver a **bassa precisione**.

8. **Efficienza del calcolo del gradiente tramite backpropagation**  
   Grazie all’**algoritmo di backpropagation**, i **gradienti della funzione di perdita** $\nabla L(w)$  possono essere calcolati in modo **estremamente efficiente**.  
   Il **costo computazionale** del calcolo dei gradienti è **soltanto il doppio** di quello della valutazione della funzione di perdita stessa.  
   Maggiori dettagli su backpropagation e differenziazione automatica sono riportati nella **Sezione 8.2**.

9. **Costo computazionale elevato della valutazione della funzione obiettivo**  
   Il calcolo del valore di **$L(w)$** è **computazionalmente oneroso**, poiché richiede l'uso dell'intero dataset per determinare tutti gli elementi della somma che definisce la funzione.

L’**ottimizzazione stocastica**, e in particolare il **SGD (Stochastic Gradient Descent)**, è particolarmente adatta per l’addestramento delle ANNs per diversi motivi, che riassumiamo di seguito:

10. **I dati sono spesso ridondanti**, quindi usare **tutte** le informazioni disponibili ad ogni iterazione risulta **inefficiente**.

11. L'esperienza computazionale accumulata dalla comunità del **machine learning** dimostra che, se si seleziona correttamente un **passo $\alpha$**, i metodi **stocastici** sono **molto più veloci** di quelli batch, **soprattutto nelle fasi iniziali** del processo di ottimizzazione.

12. **Il tasso di convergenza** di **SGD** verso una soluzione **$\epsilon$-ottimale** è **più lento** rispetto a quello del metodo **Gradient Descent** batch (cfr. **Tabella 3** in cap 4.8), ma **non dipende** dalla **dimensione del dataset di training**, che è solitamente **molto grande** nelle applicazioni pratiche.  
   Questo implica che il **costo asintotico inferiore** di **GD** rispetto a **SGD** diventa evidente **solo per valori molto bassi di $\epsilon$**.  
   Inoltre, recenti studi hanno mostrato che, in molti problemi di **deep learning**, la funzione di perdita soddisfa due proprietà fondamentali:
   - **Proprietà di interpolazione**:  
     Un **ottimizzatore globale** $w^* \in \arg\min_w L(w)$ della funzione di perdita totale è anche ottimale per **ciascun termine individuale** nella somma, ovvero:  
		 $w^* \in \arg\min_w \ell_i(w) \quad \forall i = 1, \dots, N$
     Questo significa che il modello è **sufficientemente espressivo** da poter **adattarsi perfettamente** a tutti i dati nel dataset.

   - **Condizione di Polyak-Łojasiewicz (PL-condition)**:  
     Se la funzione obiettivo soddisfa la seguente disuguaglianza  
		 $L(w) - L^* \leq \frac{1}{2\mu} \|\nabla L(w)\|^2 \quad \forall w \in \mathbb{R}^n$
     allora **ogni punto stazionario è un ottimizzatore globale** del problema.  
     **Sotto queste due ipotesi, è possibile dimostrare che SGD possiede un tasso di convergenza lineare, esattamente come il batch Gradient Descent.**

13. **SGD evita i minimi locali "stretti"** (**sharp minima**) grazie alla natura **stocastica** dei suoi passi di discesa.  
   - I **minimi stretti** si trovano in **valli molto profonde** con una **curvatura molto alta**, rendendo il modello molto sensibile a piccoli cambiamenti nei dati di input.
   - **SGD**, a causa della sua natura rumorosa, tende a **sfuggire** da questi minimi stretti e a trovare invece **minimi più "piatti"** (**flat minimizers**), che generalizzano meglio ai dati non visti. Questo effetto comporta **un'operazione di regolarizzazione intrinseca**, migliorando la capacità del modello di generalizzare. **(Figura 15 fornisce un’intuizione visiva di questo comportamento).**

![[Pasted image 20250204223801.png]]
Figura 15: Facendo un confronto fra le due loss, i punti di minimo più stretti sono molto più sensibili rispetto a punti di minimo più piatti.

Tuttavia, i metodi **batch** possiedono alcuni **vantaggi intrinseci**, in particolare:

- **Uso completo delle informazioni sul gradiente**  
  Poiché ogni iterazione utilizza l'intero gradiente, i metodi batch permettono di sfruttare appieno numerose **tecniche deterministiche di ottimizzazione** basate sul gradiente.

- **Parallelizzazione**  
  A differenza di **SGD**, i metodi batch possono sfruttare il parallelismo in modo più efficace, dato che la computazione principale riguarda **la valutazione della funzione obiettivo e dei gradienti**, operazioni facilmente parallelizzabili.

- **Migliore performance sul lungo termine**  
  Se consideriamo **un numero elevato di epoche**, il metodo batch **supera** SGD in termini di **errore di training**, garantendo una soluzione più accurata.

Queste osservazioni, sia **teoriche** che **empiriche**, suggeriscono che il metodo **minibatch SGD** (con **1 < M ≪ N**) rappresenta **un buon compromesso** tra le caratteristiche positive dei metodi **stocastici** e quelli **batch**.

---

### 8.1 Miglioramenti a SGD per l’Addestramento delle Reti Neurali Profonde

Negli ultimi anni, diverse modifiche all'algoritmo **SGD** si sono dimostrate **praticamente efficaci** per migliorare l'ottimizzazione delle **reti neurali profonde**.

#### 8.1.1 Accelerazione

I termini di **Momentum** o **Nesterov Acceleration**, discussi in **Sezione 4.4**, sono particolarmente efficaci nell'ottimizzazione **stocastica** delle reti neurali per due motivi principali:

14. **Filtraggio delle oscillazioni casuali**  
   - Il **momentum** accumula informazioni dai passi precedenti, attenuando le forti **oscillazioni stocastiche** delle direzioni di discesa.
   - Ciò riduce il tipico **comportamento a zigzag** di **SGD**, rendendo l'ottimizzazione più **stabile** ed efficace.

15. **Computazione efficiente**  
   - Il calcolo della funzione obiettivo e del suo gradiente è **computazionalmente costoso** nelle reti profonde.
   - Tuttavia, i termini $(x^k - x^{k-1})$ necessari per l'accelerazione sono **facilmente ottenibili**, permettendo di **migliorare l'efficacia di ogni iterazione senza costi aggiuntivi significativi**.

---

#### 8.1.2 Adattamento del passo di apprendimento (Learning Rate)

Oltre a migliorare la **direzione di discesa**, un'altra strategia vincente per l'ottimizzazione **stocastica** è **adattare il learning rate** in base al **progresso dell’addestramento**.  
Poiché i gradienti **si comportano in modo diverso a seconda del layer**, ogni variabile del modello può avere un **passo di apprendimento individuale**.

Negli ultimi anni, sono stati proposti diversi metodi per aggiornare il learning rate in modo **adattivo**.  
Di seguito analizziamo le tecniche più rilevanti, utilizzando una **notazione batch** per semplicità, sebbene si tratti di **metodi stocastici**.

---
##### **AdaGrad (Adaptive Gradient)**

Uno dei primi algoritmi a introdurre un **learning rate adattivo** è **AdaGrad**.  
L'idea alla base di **AdaGrad** è **accumulare l’informazione sui gradienti passati**, in modo da **scalare** il passo di aggiornamento in base alla geometria della funzione obiettivo.

Il metodo prevede di memorizzare la **somma cumulativa** dei **quadrati** delle derivate direzionali:

	$s^{k+1}_i = s^k_i + (\nabla_i f(x^k))^2$

Questa quantità viene utilizzata per **normalizzare il gradiente**, ottenendo il seguente **aggiornamento**:

	$x^{k+1} = x^k - \alpha (\text{diag}(s^{k+1}) + \epsilon I)^{-1/2} \nabla f(x^k)$

Dove:

- $\epsilon$ è un piccolo termine di **smorzamento** per evitare divisioni per zero.
- L'aggiornamento può essere riscritto in **forma componente-wise** più intuitiva:

	$x^{k+1}_i = x^k_i - \frac{\alpha}{\sqrt{s^{k+1}_i} + \epsilon} \nabla_i f(x^k)$

**Caratteristiche principali di AdaGrad**:
- **Pro:**  
  - Effettua passi **più grandi** per parametri con gradienti **piccoli**  
  - Effettua passi **più piccoli** per parametri con gradienti **grandi**  
  - Ideale per problemi **sparsi**, dove alcuni parametri aggiornano più lentamente di altri.  
- **Contro:**  
  - L'aggiornamento **accumula i gradienti quadrati**, causando un **decadimento eccessivo del learning rate**, che può portare a convergenza **troppo lenta**.

Un aspetto critico di **AdaGrad** è che i componenti di $s^k$ **crescono continuamente** con le iterazioni. Sebbene la teoria dell'**SGD** suggerisca di **diminuire** il learning rate nel tempo (scalandolo con $O(1/k)$ ), in pratica il comportamento di **AdaGrad** è spesso **troppo aggressivo**. Per questo motivo, sono state proposte alcune **varianti** che hanno avuto un grande impatto nel campo del **deep learning**.

---
##### **RMSprop (Root Mean Square Propagation)**

**RMSprop** è una variante di AdaGrad che cerca di risolverne le limitazioni, sostituendo la **somma cumulativa** con una **media esponenzialmente pesata** dei gradienti passati:

	$s^{k+1}_i = \rho s^k_i + (1 - \rho)(\nabla_i f(x^k))^2$

Dove:
- $\rho$ determina il peso assegnato ai gradienti passati.
- I parametri vengono aggiornati **esattamente come in AdaGrad**, utilizzando:

	$x^{k+1} = x^k - \frac{\alpha}{\sqrt{s^{k+1}_i} + \epsilon} \nabla_i f(x^k)$

**Vantaggi di RMSprop**:
- I **gradienti più recenti** hanno un impatto maggiore sull'aggiornamento.
- $s^k$ **non cresce all'infinito**, migliorando la **stabilità numerica** rispetto ad AdaGrad.

---

##### **AdaDelta**

**AdaDelta** è un'altra variante di AdaGrad che cerca di **ridurre l'aggressività della riduzione del learning rate**.  
Sebbene sviluppato **indipendentemente** da **RMSprop**, può essere considerato un'estensione di quest'ultimo.

L'algoritmo introduce una **media esponenziale dei quadrati degli spostamenti** ($r^k$):

	$r^{k+1} = \gamma r^k + (1 - \gamma)(x^k - x^{k-1})^2$

**Regola di aggiornamento**:

	$x^{k+1}_i = x^k_i - \frac{\sqrt{r^{k+1}_i} + \epsilon}{\sqrt{s^{k+1}_i} + \epsilon} \nabla_i f(x^k)$

**Vantaggi di AdaDelta**:
- **Elimina la necessità di scegliere manualmente** un learning rate ($\alpha$).
- Evita la **riduzione eccessiva** del learning rate osservata in AdaGrad.

---

##### **Adam (Adaptive Moment Estimation)**

L'**Adam** (**Adaptive Moment Estimation**) è oggi **l’algoritmo più utilizzato** per l'ottimizzazione delle reti neurali profonde.  
Può essere visto come un'evoluzione di **RMSprop** e **AdaDelta**, combinando i **benefici del Momentum** con l'adattamento del learning rate.

Adam mantiene due statistiche esponenzialmente pesate:
16. **Media dei gradienti** (simile a Momentum):

	$m^{k+1}_i = \beta_1 m^k_i + (1 - \beta_1) \nabla_i f(x^k)$

17. **Varianza dei gradienti** (simile a RMSprop):

    $v^{k+1}_i = \beta_2 v^k_i + (1 - \beta_2)(\nabla_i f(x^k))^2$

Questi vettori sono inizializzati a zero che è molto importante per le iterazioni iniziali dove i tassi di decadimento sono piccoli:
![[Pasted image 20250204231614.png]]

L'algoritmo **Adam** presenta un bias iniziale dovuto alla modalità con cui vengono calcolate le stime dei momenti primo ($m^k$) e secondo ($v^k$).  
Per correggere questo bias, si introducono le seguenti **stime corrette del bias**:

	$\hat{m}^k = \frac{m^k}{1 - (\beta_1)^k}, \space \hat{v}^k = \frac{v^k}{1 - (\beta_2)^k}$

Il nuovo aggiornamento delle variabili segue quindi la formula:

	$x^{k+1}_i = x^k_i - \frac{\alpha \hat{m}^k_i}{\sqrt{\hat{v}^k_i} + \epsilon}$

---

Negli ultimi anni sono state proposte alcune **varianti** dell'algoritmo **Adam** per migliorarne stabilità ed efficienza:
18. **AdaMax**  
   - Proposto insieme ad Adam.  
   - Sostituisce la stima del secondo momento con una **norma infinita stabilizzata**:
   
	$u^{k+1} = \max\{\beta_2 u^k, |\nabla f(x^k)|\}$
  
   - Questa modifica evita la necessità di correggere il bias iniziale e offre **migliore stabilità empirica**.

19. **Nadam (Nesterov-accelerated Adam)**  
   - Integra l’**accelerazione di Nesterov** nell’algoritmo Adam.  
   - Mira a **migliorare la velocità di convergenza** nei problemi di ottimizzazione profonda.

---

### 8.2 Differenziazione Automatica e Algoritmo di Backpropagation

Uno dei problemi fondamentali nell’**addestramento delle reti neurali** è il **calcolo dei gradienti della funzione di perdita**.  
L'ottimizzazione di una rete neurale comporta la **somma di funzioni di milioni di variabili**, ciascuna ottenuta dalla **composizione di operazioni elementari**.

**Problemi delle tecniche di derivazione numerica**:
- **Costo computazionale elevato**: richiedono molte valutazioni della funzione per ottenere un'approssimazione del gradiente.
- **Errori di approssimazione significativi**: la differenziazione numerica tramite differenze finite introduce errori significativi.

**Alternative alla derivazione numerica**
20. **Derivazione simbolica**  
   - Utilizza strumenti software per manipolare espressioni matematiche ed estrarre le derivate.  
   - Tuttavia, genera **formule enormi** e **calcoli eccessivamente costosi**.

21. **Differenziazione Automatica (AD - Automatic Differentiation)**  
   - Sfrutta **intelligentemente** la **regola della catena** per ottenere le derivate in modo **efficiente e preciso**:

		$\frac{\partial f}{\partial x_j} = \sum_i \frac{\partial f}{\partial g_i} \frac{\partial g_i}{\partial x_j}$
	
   - Qualsiasi funzione matematica può essere decomposta in **operazioni elementari** (es: exp, log, sin, cos, etc.).  
   - Applicando la regola della catena a ciascuna operazione, è possibile ottenere automaticamente le derivate **senza espandere simbolicamente l’intera funzione**.

---

Nel contesto del **deep learning**, l'algoritmo più utilizzato per l’AD è il **backpropagation**.  
Tecnicamente, il backpropagation è **un'implementazione della differenziazione automatica in modalità inversa** (**reverse mode AD**).

Il concetto chiave è:
- **Propagazione avanti (forward pass):** calcola l'output della rete.
- **Propagazione all'indietro (backward pass):** calcola i gradienti utilizzando la regola della catena.

L’algoritmo di backpropagation consente il calcolo **efficiente dei gradienti** ed è il cuore di tutti i moderni algoritmi di addestramento delle **reti neurali profonde**.

---

**Esempio Semplice di Backpropagation**

![[Pasted image 20250204232818.png]]

![[Pasted image 20250204232851.png]]![[Pasted image 20250204232851 1.png]

Prima, tutte le operazioni elementari vengono mappate in un Computation Graph (Figura 16a), che è una struttura che permette di collegare quantità che dipendono l'una dall'altra. 
In questo modo, le quantità calcolate che saranno necessarie per calcolare altri termini possono essere memorizzate in memoria, evitando calcoli duplicati.

Il calcolo effettivo procede prima alimentando gli input alla funzione e calcolando i prodotti 
intermedi fino all'output della funzione; poi, il grafo viene attraversato all'indietro, 
per calcolare tutte le derivate parziali. 
Si deve notare che, per calcolare i gradienti, otteniamo come prodotto intermedio il valore della funzione; quindi, in un'iterazione di discesa del gradiente, possiamo ottenere il valore della funzione nel punto attuale, effettuando un passaggio in avanti attraverso il grafo di calcolo, e poi i gradienti, dopo un passaggio all'indietro attraverso il grafo.

Come accennato in precedenza, alcuni termini appaiono più volte durante il calcolo; 
per evitare calcoli duplicati, possiamo memorizzare questi valori per riutilizzarli quando necessario; ovviamente, non sarà difficile immaginare che nelle reti profonde e complesse i termini si ripetano in modo molto più massiccio rispetto al semplice esempio in questione.
