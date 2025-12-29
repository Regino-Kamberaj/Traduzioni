
**Definizione 1.10.** 
Sia $f : \mathbb{R}^n \to \mathbb{R}$, con $f \in C^1(\mathbb{R}^n)$. Diciamo che $f$ è ***L-smooth*** se:
- Il gradiente $\nabla f$ è una funzione [[Lipschitz-continua]] con costante di Lipschitz $L$, ossia se $$\|\nabla f(x) - \nabla f(y)\| \leq L\|x - y\|$$per ogni $x, y \in \mathbb{R}^n$

**Proposizione 1.8** (**Lemma di discesa**). Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione **L-liscia**. Allora, per ogni $x \in \mathbb{R}^n$ e per ogni $d \in \mathbb{R}^n$, si ha	$$f (x + d) \leq f (x) + \nabla f (x)^T d + \frac{L}{2} \|d\|^2$$

