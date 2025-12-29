Prima se serve, riguardare un po' di definizioni sulla [[differenziabilità]] delle funzioni

**Definizione 1.3.6. (Funzione continuamente differenziabile)** 
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che $f$ è *continuamente differenziabile* su $\mathbb{R}^n$, e lo denotiamo con $f \in C^1(\mathbb{R}^n)$, se:
- Il gradiente $\nabla f(x)$ **esiste** per ogni $x \in \mathbb{R}^n$
- E la funzione $\nabla f : \mathbb{R}^n \to \mathbb{R}^n$ è **continua** su $\mathbb{R}^n$

**Proposizione 1.4.** 
Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione **continuamente differenziabile**. Allora, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, si ha:$$Df(x, d) = \nabla f(x)^T d$$ => la sua derivata parziale (derivata direzionale lungo la direzione d) è parti al prodotto scalare del gradiente per la direzione $d$ 