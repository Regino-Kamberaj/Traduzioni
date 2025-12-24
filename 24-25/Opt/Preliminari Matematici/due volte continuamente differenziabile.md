**Definizione 1.3.11** 
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che $f$ è **due volte continuamente differenziabile** su $\mathbb{R}^n$, e lo denotiamo con $f \in C^2(\mathbb{R}^n)$ se:
- La [[matrice Hessiana]] $\nabla^2 f(x)$ **esiste per ogni** $x \in \mathbb{R}^n$
- La funzione $\nabla^2 f : \mathbb{R}^n \to \mathbb{R}^{n \times n}$ è **continua** su $\mathbb{R}^n$ (al posto del gradiente richiedo l'hessiana continua)

**Proposizione 1.3.3** 
Sia $f (x) = \frac{1}{2} x^T Qx + c^T x$, con $Q \in S^n$ e $x \in \mathbb{R}^n$.Allora si ha:
- $\nabla f (x) = Qx + c$;
- $\nabla^2 f (x) = Q$

