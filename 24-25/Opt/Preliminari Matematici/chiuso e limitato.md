**Definizione 1.1.4**
Un insieme $S \subseteq \mathcal{U}$ è **chiuso** se il suo complementare $\bar{S} = \mathcal{U} / S$ è un insieme *aperto*. Dove per **aperto**, si intende un insieme  $S \subseteq \mathcal{U}$ che per ogni $x \in S$, esiste $\epsilon > 0$ tale che $B(x,\epsilon)$ è interamente contenuta in $S$, ovvero $B(x,\epsilon) \subseteq S$

**Definizione 1.1.5**
Un insieme $S \subseteq \mathcal{U}$ è **limitato** se esiste $M > 0$ tale che, per ogni $x \in S$, $||x|| \leq M$

**Proposizione 1.1.1** 
Sia $S \subseteq \mathbb{R}^n$ allora:
- $S$ è limitato se e solo se ogni *sottosequenza* $\{x^k\} \subseteq S$ ammette ==almeno un punto di accumulazione==, ovvero esiste una *sottosequenza* $K \subseteq \{1,2,...\}$ tale che $\lim\limits_{\begin{subarray}{c}k\in K\\ k\to\infty\end{subarray}} x^{k} = \bar{x} \in \mathbb{R}^n$ (nota che $\bar{x}$ può non appartenere a $S$)
-  $S$ è chiuso se e solo se, per ogni sequenza ${x^k}\subseteq S$, ==tutti i suoi punti di accumulazione (se ce ne sono) sono in $S$==, ovvero per ogni *sottosequenza* $K \subseteq \{1,2,...\}$ tale che $\lim\limits_{\begin{subarray}{c}k\in K\\ k\to\infty\end{subarray}} x^{k} = \bar{x}$, abbiamo che $\bar{x} \in S$ 