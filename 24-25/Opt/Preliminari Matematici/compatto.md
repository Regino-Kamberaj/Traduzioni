**Definizione 1.1.6**
Un insieme $S \subseteq \mathcal{U}$ è *compatto* se ogni sequenza $\{x^k\} \subseteq S$ ammette un *punto di accumulazione* in $S$. In altre parole, per ogni $\{x^k\} \subseteq S$ esiste $K \subseteq \{1,2,...\}$ tale che $$\lim\limits_{\begin{subarray}{c}k\in K\\ k\to\infty\end{subarray}} x^{k} = \bar{x} \in S$$
**Corollario 1.1.2**
Un insieme $S \subseteq \mathbb{R}^n$ è compatto se e solo se è [[chiuso e limitato]] 

**Esempio 1.1.2**
Esempi di insiemi compatti in $\mathbb{R}^n$ sono:
- L'insieme vuoto $\mathbb{0}$ 
- Un singleton $\{x\}$
- Una palla $B(x,\epsilon) = \{y \in \mathbb{R}^n \, \text{t.c} \, ||y-x|| \leq \epsilon \}$ 
- Una box n-dimensionale $\{x \in \mathbb{R}^n \, \text{t.c} \, l_i \leq x_i \leq u_i \, \forall \, i = 1,...,n \}$ 
Non lo sono invece:
- L'intero spazio $\mathbb{R}^n$
- La palla aperta $\{y \in \mathbb{R}^n \, \text{t.c} \, ||y-x|| < \epsilon \}$  (non chiusa)

![[Pasted image 20251221223315.png]]