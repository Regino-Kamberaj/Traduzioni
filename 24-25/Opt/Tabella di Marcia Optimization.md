# Tabella

- ## ==24-25 September==

	~~**Lecture 01 (2hrs):**~~
    
    Introduction to the course, bureaucracy. Definition of a mathematical optimization problem: objective function, decision variables, feasibile set; Example: optimal portfolio selection problem; Classification of optimization problems [GS 1.1]. Optimation problem example: mathematical models estimation; the case of supervised learning - empirical risk minimization problem [GS 1.5, LN 6.1].
    
    ~~**Lecture 02 (2hrs):**~~
    
    Fundamental concepts: global optimizer; Existence of an optimal solution: definition and conditions; Weierstrass Theorem (w/ prf.); Definition of compact sets and the case of the Euclidean space [GS A.3]; Compact level sets, sufficient conditions of existence of a solution (w/ prf.) [GS 1.4].
    
- ## ==1-2 October==
    
    ~~**Lecture 03 (2hrs):**~~
    
    Coercivity, examples of coercive functions: norms, quadratic forms (w/ prf.) [GS 1.4]; Local minimizers; convexity [GS C.1,C.2,C.3].
    
    ~~**Lecture 04 (2hrs):**~~
    
    Optimal solutions in the convex case (w/ prf.), strict convexity, uniqueness of solution in strictly convex case [GS 1.2]. Strong convexity [LN X.XX].  Optimality conditions: overview [GS 2.1]; Preliminaries: differentiable functions [GS Appendix B].
    
- ## ==8-9 October==
    
    ~~**Lecture 05 (2hrs):**~~
    
    Convex differentiable functions [GS Appendix C.5]. Descent directions; first order descent condition, necessary condition of local optimality; first order  necessary condition of optimality (w/ prf.).
    
    ~~**Lecture 06 (2hrs):**~~ 
    
    Descent condition for convex functions (w/ prf.); necessary and sufficient condition of optimality in the convex case (w/ prf.) [GS 2.3]. Negative curvature directions, second order descent condition (w/ prf.) [GS 2.2]. Second order necessary condition of optimality (w/ prf.); second order sufficient conditions of optimality; the case of quadratic functions (w/ prf.)  [GS 2.3].
    
- ## ==15-16 October==
    
    ~~**Lecture 07 (2hrs):**~~ 
    
    Regularized linear regression problems: existence and uniqueness of the solution [LN 6.2]. Optimization algorithms for unconstrained optimization: general scheme of iterative algorithm; sequences of solutions [GS 3.1, LN 4.1]. Baisc principles of line search,  trust region and direct search methods [LN 4.1].  
    Sufficient condition of existence of accumulation points (w\ prf.) [LN 4.1.1]. Infinite convergence towards stationary points [LN 4.1.2]. 
    
    ~~**Lecture 08 (2hrs):**~~ 
    
    Assumptions for convergence towards stationarity: counterexample [LN 4.1.2]. Convergence speed and complexity bounds [LN 4.1.3]. Global and local convergence properties.
    
    Line-search type methods: general scheme; crucial elements for convergence: choice of the direction and the stepsize; counterexample [LN 4.2]. 
    
- ## ==22-23 October==
    
    ~~**Lecture 09 (2hrs):**~~ 
    
    Line searches: general concepts; exact line searches, the quadratic case; inexact line searches, sufficient decrease, Armijo condition; Armijo line search, finite termination properties (w/ prf.) [LN 4.2.1]. 
    
    ~~**Lecture 10 (2hrs):**~~
    
    Gradient-related directions: definition and interpretation; bounded eigenvalues condition [LN 4.2.2]. Global convergence of line search based methods (w/ prf.) [LN 4.2.3]
    
- ## ==29-30 October==
    
    ~~**Lecture 11 (2hrs):**~~ 
    
    L-smoothness, descent lemma; Armijo line search along gradient related directions: interval of surely acceptable stepsizes (w/ prf.); upper bound on backtracks/lower bound on stepsize (w/o prf.); complexity of the algorithmic framework under L-smoothness assumptions (w/ prf.), optimal complexity of first-order methods (w/o prf.).  [LN 4.2.3]. Gradient descent method: algorithmic scheme, convergence properites [GS 6.1-6.2, LN 4.3].  
      
    
    ~~**Lecture 12 (2hrs):**~~ 
    
    Gradient descent with constant stepsize; complexity under convexity assumptions (w/ prf.); convergence rate in the strongly convex case (w/o prf.) [LN 4.3], impact of l2 regularization in machine learning problems [LN 6.1]. Algorithms with momentum terms [LN 4.4], Heavy-ball method [LN 4.4.1].
    
- ## ==5-6 November==
    
    ~~**Lecture 13 (2hrs):**~~ 
    
    Accelerated gradient method [LN 4.4.2]. Nonlinear conjugate direction methods, restarting strategies, Wolfe line search [LN 4.4.3]. 
    
    ~~**Lecture 14 (2hrs):**~~ 
    
    Conjugate gradient method for quadratic problems, finite termination (w/o prf.) [LN 4.4.3]. 
    
    Second order methods, Netwon method as iterative optimization of second order Taylor approximation;  Newton's method does not have global convergence properties: counterexample; Local convergence properties (w/ prf.) [LN 4.5].
    
- ## ==12-13 November==
    
    ~~**Lecture 15 (2hrs):**~~ 
    
    Local convergence properties of Newton's method (continued) [LN X.XX]. Globalization of Newton's method [LN 4.5]. 
    
    Hessian approximation, Quasi-Newton equation, direct and inverse update rules [LN 4.6].
    
    ~~**Lecture 16 (2hrs):~~  
    
    Rank-1 and rank-2 update rules [LN 4.6]; BFGS method [LN 4.6.1]; large scale problems, L-BFGS algorithm [LN 4.6.2].
    
    Constrained optimization problems: feasible directions, necessary optimality conditions [GS 17.2.1].
    
- ## ==19-20 November==
    
    ~~**Lecture 17 (2hrs):**~~ 
    
    Problems with convex constraints: feasible directions (w/ prf.), optimality conditions (w/ prf.) [GS 17.2.2]. Problems with linear constraints, feasible directions (w/o prf.), optimality conditions with box constraints (w/ prf.) [GS 17.2.3]. Projection onto a convex set: definition, equivalent characterization (w/o prf.), continuity (w/o prf.), stationarity condition basedon projection (w/ prf.) [GS 17.2.4].
    
    ~~**Lecture 18 (2hrs):**~~ 
    
    Projection onto box constraints and ball constraints [GS 17.2.4]. Constrained Armijo type line-search, convergence properties (w/o prf.) [GS 17.3]. Projected gradient method: algorithmic scheme and convergence properties (w/ prf.) [GS 17.5]. Frank-Wolfe method: algorithmic scheme and convergence properties (w/ prf.) [GS 17.4].
    
- ## ==26-27 November==
    
    ~~**Lecture 19 (2hrs):**~~ 
    
    Optimization problems with analytical constraints [GS D]; Fritz-John conditions [GS D.1]; constraints qualifications, KKT conditions [GS D.2]; LCQ, LICQ (w/ prf.), SCQ; particular case of convex problems with linear constraints [GS D.5].
    
    ~~**Lecture 20 (2hrs):**~~ 
    
    Simplex constraints, optimality condition (w/ prf.) [GS D.5]. Binary classification problems; Support Vector Machines as minimizers of L2-regularized hinge loss minimization, geometrical interpretation [LN 7]; properties of Wolfe dual problem (w/ prf.), derivation of SVM dual formulation (w/ prf.) [LN 7.1].
    
- ## 3-4 December
    
    ~~**Lecture 21 (2hrs):**~~
    
    Derivation of dual problem (continued), geometrical interpretation of the solution [LN.1]. Kernel SVM [LN 7.1]. Decomposition Techniques [LN 4.7, GS 16].
    
    **Lecture 22 (2hrs):** 
    
    Solving SVM dual by decomposition [LN 7.2]; Sequential Minimal Optimization: two-variables update, feasible directions, descent directions, SMO algorithmic scheme, gradients update  [LN 7.2.1]. SVM dual: optimality conditions (w/o prf.), Most Violating Pairs, convergence results for SMO algorithm [LN 7.2.2].
    
- ## 10-11 December
    
    **Lecture 23 (2hrs):**
    
    Finite-sum problems, Stochastic Gradient Descent method [LN 4.8]. Convergence of SGD (w/o prf.), complexity results, Minibatch SGD [LN 4.8.1]; Overview on Deep Networks training: problem characteristics and motivations for minibatch SGD [LN 8].
    
    **Lecture 24 (2hrs):** 
    
    SGD in DL scenario: addition of acceleration terms [LN 8.1.1], adaptive learning rate [LN 8.1.2]. Automatic differentiation and backpropagation [LN 8.2].

# ✅ CHECKLIST DI STUDIO - OTTIMIZZAZIONE (Primo Registro)
## Piano intensivo per 2 settimane (24 lezioni → 14 giorni)

**Istruzioni:** Segui l'ordine delle lezioni. Spunta ogni argomento man mano che lo studi e lo padroneggi. Ogni blocco corrisponde a circa 1 giorno di studio intensivo.

---

## 📚 **SETTIMANA 1: FONDAMENTI TEORICI & OTTIMALITÀ**

### **Giorno 1: Introduzione & Esistenza dei Minimi (Lec 01-02)**
**Riferimenti:** [GS 1.1, 1.4, 1.5, A.3], [LN 6.1]
- [x] Definire un problema di ottimizzazione (funzione obiettivo, variabili, insieme ammissibile)
- [x] Classificare problemi (lineari, convessi, non lineari, vincolati/non vincolati)
- [x] Conoscere l'esempio di **Portfolio Selection** e di **Empirical Risk Minimization**
- [x] Definizione di **minimizzatore globale**
- [x] **Teorema di Weierstrass:** enunciato, ipotesi (continuità + compattezza), idea della dimostrazione
- [x] Sapere cosa sono gli insiemi **compatti** in ℝⁿ (chiusi e limitati)
- [x] Concetto di **insiemi di livello compatti** come condizione sufficiente per l'esistenza del minimo

### **Giorno 2: Strumenti per l'Esistenza & Convessità Base (Lec 03)**
**Riferimenti:** [GS 1.4, C.1-C.3]
- [x] Definizione di **coercività** di una funzione
- [x] Dimostrare/sapere perché le **norme** e le **forme quadratiche definite positive** sono coercive
- [x] **Implicazione chiave:** funzione continua + coerciva → insieme di livello compatto → minimo esiste (via Weierstrass)
- [x] Definizione di **minimizzatore locale**
- [x] Definizioni di base: **insieme convesso**, **funzione convessa**
- [x] Proprietà fondamentali delle funzioni convesse

### **Giorno 3: Convessità & Ottimalità - Primi Strumenti (Lec 04)**
**Riferimenti:** [GS 1.2, App. B], [LN X.XX]
- [x] **Teorema fondamentale:** Per funzioni convesse, ogni minimo locale è globale
- [x] Convessità **stretta** → unicità del minimo
- [x] Concetto di **convessità forte** (strong convexity) [dalle note]
- [x] Panoramica sulle **condizioni di ottimalità** (cosa studieremo)
- [x] Richiami su **funzioni differenziabili** (gradiente, derivate parziali, matrice jacobiana)

### **Giorno 4: Condizioni di Ottimalità del Primo Ordine (Lec 05)**
**Riferimenti:** [GS App. C.5, 2.1-2.3]
- [x] Proprietà delle **funzioni convesse e differenziabili** (derivata prima e convessità)
- [x] Concetto di **direzione di discesa**
- [x] **Condizione di discesa del primo ordine** (se ∇f(x)ᵀd < 0, allora d è direzione di discesa)
- [x] **Condizione necessaria del primo ordine (FONC)** per ottimo locale: ∇f(x*) = 0
- [x] **Per funzioni convesse:** FONC diventa anche **condizione sufficiente** per ottimo globale

### **Giorno 5: Condizioni di Ottimalità del Secondo Ordine (Lec 06)**
**Riferimenti:** [GS 2.2, 2.3]
- [x] **Condizione di discesa per funzioni convesse** (dimostrazione)
- [x] **Condizione necessaria e sufficiente per ottimo** nel caso convesso
- [x] Concetto di **direzione di curvatura negativa**
- [x] **Condizione di discesa del secondo ordine**
- [x] **Condizione necessaria del secondo ordine (SONC):** ∇f(x*)=0 e Hessiana H(x*) è semidefinita positiva
- [x] **Condizione sufficiente del secondo ordine (SOSC):** ∇f(x*)=0 e H(x*) è definita positiva → x* è minimo locale stretto
- [x] Caso particolare: **funzioni quadratiche** (applicazione delle condizioni)

### **Giorno 6: Modelli & Introduzione agli Algoritmi (Lec 07)**
**Riferimenti:** [LN 6.2, 4.1], [GS 3.1]
- [x] **Regressione Lineare Regolarizzata (L2):** problema, perché la convessità forte garantisce esistenza e unicità della soluzione
- [x] Schema generale di un **algoritmo iterativo** per ottimizzazione non vincolata
- [x] Concetto di **successione di punti** generata da un algoritmo
- [x] Panoramica sui tipi di algoritmi: **line search**, **trust region**, **direct search**
- [x] **Condizione sufficiente per l'esistenza di punti di accumulazione** per una successione
- [x] Convergenza di una sottosuccessione verso un **punto stazionario** (∇f(x)=0)

### **Giorno 7: Convergenza degli Algoritmi & Line Search (Lec 08-09)**
**Riferimenti:** [LN 4.1.2, 4.1.3, 4.2, 4.2.1]
- [x] Controesempi alla convergenza (cosa succede se non si scelgono bene direzione e passo?)
- [x] Concetti di **convergenza globale vs. locale**, **velocità di convergenza**, **limiti di complessità**
- [x] Schema generale dei metodi di **line search**: `x_{k+1} = x_k + α_k d_k`
- [x] Due scelte cruciali: **direzione d_k** e **passo α_k**
- [x] **Ricerca di linea esatta vs. inesatta**
- [x] **Condizione di sufficiente decrescita (Armijo):** `f(x_k + αd_k) ≤ f(x_k) + γα∇f(x_k)ᵀd_k`
- [x] Proprietà di **terminazione finita** della line search di Armijo (con backtracking)

---

## ⚙️ **SETTIMANA 2: ALGORITMI & APPLICAZIONI AVANZATE**

### **Giorno 8: Convergenza Globale dei Metodi di Line Search (Lec 10-11 Parte 1)**
**Riferimenti:** [LN 4.2.2, 4.2.3]
- [x] Definizione di **direzioni legate al gradiente (gradient-related)**
- [x] Condizione degli **autovalori limitati** per le direzioni
- [x] **Teorema di convergenza globale** per metodi di line search con direzioni legate al gradiente e passo di Armijo
- [x] Concetto di **L-smoothness** (gradiente Lipschitziano) e **Descent Lemma**
- [x] Per funzioni L-smooth, esiste un **intervallo di passi accettabili** per Armijo
- [x] Limitazione superiore al numero di backtrack / limitazione inferiore al passo α

### **Giorno 9: Complessità & Gradient Descent (Lec 11 Parte 2 - 12 Parte 1)**
**Riferimenti:** [LN 4.2.3, 4.3], [GS 6.1-6.2]
- [x] **Complessità** (numero di iterazioni) del framework generale sotto ipotesi di L-smoothness
- [x] Limite ottimale per metodi del primo ordine (cenni)
- [x] **Algoritmo del Gradient Descent (GD)**: `x_{k+1} = x_k - α∇f(x_k)`
- [x] Proprietà di convergenza del GD
- [x] GD con **passo costante**: condizioni su α per la convergenza (α < 2/L)
- [x] Complessità del GD per funzioni **convesse** e L-smooth
- [x] Velocità di convergenza per funzioni **fortemente convesse**

### **Giorno 10: Algoritmi Avanzati del 1° Ordine (Lec 12 Parte 2 - 14 Parte 1)**
**Riferimenti:** [LN 4.3, 4.4, 4.4.1-4.4.3]
- [x] Impatto della **regolarizzazione L2** nei problemi di ML (rende il problema fortemente convesso)
- [x] Idea degli **algoritmi con momento (momentum)**
- [x] **Metodo della Palla Pesante (Heavy-ball)**
- [x] **Metodo del Gradiente Accelerato (es. Nesterov)**
- [x] Metodi a **direzioni coniugate non lineari**, strategie di **restart**
- [x] **Condizioni di Wolfe** per la line search (condizioni più forti di Armijo)
- [x] **Metodo del Gradiente Coniugato per problemi quadratici**: idea e proprietà di terminazione finita

### **Giorno 11: Metodi del Secondo Ordine & Quasi-Newton (Lec 14 Parte 2 - 16 Parte 1)**
**Riferimenti:** [LN 4.5, 4.6]
- [x] **Metodo di Newton**: direzione `d_k = -[H(x_k)]⁻¹∇f(x_k)` (minimizza l'approssimazione quadratica)
- [x] **Mancanza di convergenza globale**: controesempio
- [x] **Convergenza locale quadratica** (con dimostrazione delle ipotesi)
- [x] Strategie di **globalizzazione** di Newton (es. Newton + Armijo)
- [x] Approssimazione dell'Hessiana: **equazione di Quasi-Newton** `B_{k+1} s_k = y_k`
- [x] Regole di aggiornamento **diretta (B)** e **inversa (H)**
- [x] Aggiornamenti di **rango 1 e rango 2** (es. DFP, SR1)

### **Giorno 12: Quasi-Newton & Ottimizzazione Vincolata Base (Lec 16 Parte 2 - 17)**
**Riferimenti:** [LN 4.6.1-4.6.2], [GS 17.2.1-17.2.3]
- [x] **Metodo BFGS** (formula di aggiornamento inversa, proprietà di simmetria e definita positività)
- [x] **L-BFGS** per problemi su larga scala (memoria limitata)
- [x] Transizione a problemi **vincolati**: insieme ammissibile, direzioni ammissibili
- [x] **Condizione necessaria di ottimalità** per problemi vincolati generali (basata su direzioni ammissibili)
- [x] Caso di **vincoli convessi**: caratterizzazione delle direzioni ammissibili
- [x] Caso di **vincoli lineari** e di **vincoli di scatola (box)**: condizioni di ottimalità specifiche

### **Giorno 13: Metodi per Vincoli Connessi & KKT (Lec 18-19)**
**Riferimenti:** [GS 17.2.4, 17.3-17.5, D.1-D.2]
- [x] **Proiezione su un insieme convesso**: definizione, proprietà di non espansività
- [x] **Condizione di stazionarietà basata sulla proiezione**: `x* è minimo su C ⇔ x* = Proj_C(x* - ∇f(x*))`
- [x] Proiezioni su **scatola** e **palla** (formule esplicite)
- [x] Line search di Armijo **vincolata**
- [x] **Metodo del Gradiente Proiettato**: schema e proprietà di convergenza
- [x] **Metodo di Frank-Wolfe (Conditional Gradient)**: schema e proprietà
- [x] Problemi con **vincoli analitici** (uguaglianze/disuguaglianze)
- [x] **Condizioni di Fritz-John**
- [x] **Condizioni di Karush-Kuhn-Tucker (KKT)**: Lagrangiana, moltiplicatori, condizioni di stazionarietà, complementarità
- [x] **Qualificazioni dei vincoli (CQ)**: LCQ, LICQ (con dim.), SCQ

### **Giorno 14: Applicazioni Finali - SVM & Algoritmi Stocastici (Lec 20-24)**
**Riferimenti:** [GS D.5], [LN 7, 7.1-7.2, 4.7-4.8, 8, 8.1-8.2]
- [x] Caso particolare: **vincoli di simplesso**, condizione di ottimalità
- [x] **Problemi di classificazione binaria**
- [x] **Support Vector Machines (SVM)**: formulazione primale (minimizzazione hinge loss + L2), interpretazione geometrica (massimo margine)
- [x] **Duale di Wolfe**: proprietà generali
- [x] **Derivazione del duale SVM**, interpretazione geometrica della soluzione, **Kernel SVM** (idea)
- [ ] Skipped
	- [ ] **Tecniche a Decomposizione** per problemi di grandi dimensioni
	- [ ] **Risolvere il duale SVM per decomposizione**: algoritmo **SMO (Sequential Minimal Optimization)**
	- [ ] Aggiornamento a 2 variabili, direzioni ammissibili e di discesa, schema SMO, aggiornamento dei gradienti
	- [ ] Condizioni di ottimalità per il duale SVM, **Most Violating Pair**, convergenza di SMO
- [x] **Problemi finite-sum**, **Stochastic Gradient Descent (SGD)**, **Minibatch SGD**
- [x] Proprietà di convergenza e complessità di SGD (confronto con GD)
- [x] Panoramica sul **training di Deep Network**: caratteristiche del problema e motivazioni per Minibatch SGD
- [x] SGD nello scenario DL: termini di **accelerazione (momentum)** e **learning rate adattivo**
- [x] **Differenziazione Automatica e Backpropagation** (principio di funzionamento)

---

## 🎯 **GIORNO DELLA VERIFICA FINALE**
- [ ] **Ripasso Mappe Mentali**: Collegare esistenza (Weierstrass/Coercività) → convessità → condizioni ottimalità (KKT) → algoritmi (GD/Newton/Proiettato) → applicazioni (SVM/SGD)
- [ ] **Ripasso Dimostrazioni Chiave**: Weierstrass, condizioni I/II ordine, convergenza globale line-search
- [ ] **Esercizi Svolti**: Rifare esercizi su classificazione punti stazionari, condizioni KKT, passi di algoritmi
- [ ] **Simulazione Esame**: Svolgere una traccia completa a tempo

**STATO PREPARAZIONE:**
- [ ] **Fondamenti Teorici (Giorni 1-6)** Completati: ___6/6
- [ ] **Algoritmi & Applicazioni (Giorni 7-14)** Completati: ___1/8
- [ ] **Revisione Finale** Completata: [  ]

**Dimostrazioni da sapere:**
- [x] 3.0 Definizione punto di ottimo
- [x] 3.1 Esistenza soluzioni ottimali
	- [x] Proposizione 3.1.1 => Teorema di Weierstrass
	- [x] Proposizione 3.1.2 => Insiemi di livello compatti ammettono minimi globali
	- [x] Proposizione 3.1.3 => funzioni coercive ammettono punti di minimo
- [x] 3.2 Condizioni di ottimalità
	- [x] 3.2.1 Definizione ottimo locale
	- [x] Proposizione 3.2.1 => funzione convessa su insieme convessa => minimi locali sono anche globali
	- [x] Proposizione 3.2.2 => su funzioni strettamente convesse minimo globale **unico**
	- [x] Proposizione 3.2.3 => su funzioni fortemente convesse minimo globale unico su tutto $\mathbb{R}^n$
	- [x] 3.2.2 Definizione direzione di discesa
	- [x] Proposizione 3.2.4 => in minimo locale ? non esistono direzioni di discesa
	- [x] Proposizione 3.2.5 => definizione direzione di discesa per funzioni continuamente differenziabili
	- [x] Proposizione 3.2.6 => per funzioni cont. diff non esistono direzioni di discesa in minimizzatori locali
	- [x] Proposizione 3.2.7 => condizione necessaria di ottimalità prim ordine (minimizzatori locali hanno gradiente nullo) + definzione 3.2.3 punto stazionario
	- [x] Proposizione 3.2.8 => se funzione convessa oltre a cont. diff, direzione di discesa neccesariamente (e suff) ha derivata direzionale negativa
	- [x] Proposizione 3.2.9 => Condizione necessaria e sufficiente del prim ordine per problemi convessi => minimizzatori globali a gradiente nullo
	- [x] Definizione 3.2.4 => direzione di curvatura negativa
	- [x] Proposizione 3.2.10 => direzioni di discesa hanno curvature negative
	- [x] Proposizione 3.2.11 => Condizione **necessaria** ottimalità secondo ordine => minimi locali hanno gradiente nullo e hessiana semidefinita positiva
	- [x] Proposizione 3.2.12 => Condizione **sufficiente** di ottimalità locale del secondo ordine => punti stazionari se hanno hessiana definita pos o hessiana semidefinita positiva (in un intorno del punto), allora sono anche minimi locali
- [x] 4.1 Metodi iterativi di ottimizzazione
	- [x] regole aggiornamento
	- [x] Proposizione 4.1.1 => sequenze definite su insiemi di livello compatti hanno punti di accumulazione e la sequenza (se definita monotona decrescente) converge ad un valore finito
	- [x] Convergenza globale vs convergenza locale => esempi su convergenza => non sempre si converge a punti stazionari
	- [x] Definizione 4.1.1 => tasso di convergenza (sub vs linear vs super)
	- [x] Definizione 4.1.2 => notazione o grande
	- [x] Definizione 4.1.3 => errore di iterazione/complessità d'iterazione
- [x] 4.2 Metodi di discesa basati su line search
	- [x] Occhio a scelta direzione e passo => servono condizioni più forti su direzioni di discesa
	- [x] esempio line search esatta
	- [x] Algoritmo 1 => line search di armijo per ricerca passo ottimale (condizione di armijo)
	- [x] Proposizione 4.2.1 => line search termina in un numero di iterazioni
	- [x] Definizione 4.2.1 => direzioni gradient related 
	- [x] Proposizione 4.2.2 => convergenza globale a punti stazionari con passo scelto tramite armijo e direzioni gradient related ( e sequenza su insieme di livello compatto)
	- [x] Proposizione 4.2.3 => per funzioni l-smooth, passi ottenuti da armijo sono limitati da valore fisso
	- [x] Proposizione 4.2.4 => numero massimo di backtrack
	- [x] Proposizione 4.2.5 => complessità nel caso non convesso => sublineare $O(\epsilon^{-2})$ (valido anche per valutazione funzioni)
	- [x] Proposizione 4.2.6 => limite per metodi del primo ordine
- [ ] 4.3 Metodo di discesa del gradiente 
	- [ ] algoritmo 2 => line search con direzione antigrad e passo con algoritmo 1 => riottengo stesse proprietà viste prima => convergenza globale - complessità ottimale per metodi non convessi (sublineare) - num passi backtrack limitato => complessità per valutazione funzione rimane la stessa
	- [ ] Proposizione 4.3.1 => nel caso convesso (e con passo costante), ottengo complessità migliore (ma non ottimale => ancora sublineare) $O(\frac{1}{\epsilon})$ 

	- [ ] Proposizione 4.3.2 => nel caso fortemente convesso (e con passo costante), ottengo complessità  ancora migliore (stavolta lineare) $O(log{\frac{1}{\epsilon}})$ => convergo ad un unico punto di minimo globale 
- [ ] 4.4 Metodi del gradiente con momento
	- [ ] 4.4.1 Heavy ball (metodo locale) => tasso di conv lineare ma locale (e convesso)
	- [ ] Metodo del gradiente accelerato di nesterov => proposizione 4.4.1 => bound su funzioni convesse del primo ordine $O\left(\frac{1}{\sqrt{\epsilon}}\right)$  (meglio di grad descent) => ovvero solo con info dei gradienti
	- [ ] 4.4.2 gradiente coniugato => perdo direzioni grad related e quindi garanzie di convergenza => metodi per recuperare garanzie di conv. => salvaguardie e restart => torno a conv globale e complessità di grad descent
	- [ ] Line search di wolfe => condizione più forte di armijo => wolfe deboli vs wolfe forti => limito passo andando a guardare dove derivata direzionale soddisfa condizioni => aumentano costi computazionali => ma garantisco direzioni di discesa e convergenza globale
	- [ ] Caso quadrato + definzioni direzioni mutuamente coniugate
	- [ ] Proposizione 4.4.2 => convergenza finita del meodo del gradiente coniugato nel caso quadratico => raggiungo minimo globale in n iterazioni
- [ ] 4.5 Metodo di newton => convergenza dipende fortemente dal punto di partenza ma molto veloce
	- [ ] Proposizione 4.5.1 Proprietà metodo di newton => preso punto a gradiente nullo e hessiana non singolare => allora sequenza definita a partire da quel punto è ben definita e rimane **nell'intorno** - metodo converge con tasso superlineare => tasso = 0
	- [ ] metodo di discesa line search con newton => ottengo conv globale e veloce 
- [ ] 4.6 Metodi quasi newton => approx delle hessiane 
	- [ ] Algoritmo 4
	- [ ] Algoritmo bfgs => proposizione 4.6.1 => matrice di approx definita positiva sotto det condizioni => tipo wolfe => riottengo convergenza globale e tasso superlineare senza info del secondo ordine
	- [ ] low-bfgs => bfgs con approx interrotta... diminuiscono costi computazionali ma perdo proprietà teoriche => conv globale garantita con salvaguardie 

**Note e Punti Deboli da Ripassare:**
1.
2.
3.