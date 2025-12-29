
**Definizione 1.2.1**
Una matrice $A \in \mathcal{S}_n$ è:
- *Semidefinita positiva*, denotata $A \succeq 0$, se $x^T A x \geq 0$ per ogni $x \in \mathbb{R}^n$;
- *Definita positiva*, denotata $A \succ 0$, se $x^T A x > 0$ per ogni $x \in \mathbb{R}^n, x \neq 0$.

**Proposizione 1.2.2**
Una matrice $A \in \mathcal{S}_n$ è *semidefinita positiva* se e solo se:
- Tutti gli autovalori di $A$ sono **non negativi**, cioè $\lambda_{\text{min}}(A) \geq 0$. 
Analogamente, $A$ è *definita positiva* se e solo se:
- Tutti gli autovalori di $A$ sono **strettamente positivi**, cioè $\lambda_{\text{min}}(A) > 0$.

**Proposizione 1.2.3**
Data $A \in \mathcal{S}_n, A \succeq 0$, per ogni $x \in \mathbb{R}^n$ abbiamo:
- $\lambda_{\text{min}}(A) ||x||^2 \leq x^T A x \leq \lambda_{\text{max}}(A) ||x||^2$;
- $\lambda_{\text{min}}(A) ||x|| \leq ||A x|| \leq \lambda_{\text{max}}(A) ||x||$.
