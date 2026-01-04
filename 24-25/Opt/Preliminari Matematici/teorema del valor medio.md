**Proposizione 1.3.4.** (**Teorema del valor medio**)
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Allora:
Se $f \in C^1 (\mathbb{R}^n)$, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, esiste $t \in (0,1)$ tale che $\xi = x + td$ allora:$$f (x + d) = f (x) + \nabla f (\xi)^T d$$ oppure:$$f (x + d) = f (x) + \nabla f (x)^T d + \beta (x, d)$$  dove $$\lim_{\|d\| \to 0} \frac{\beta (x, d)}{\|d\|} = 0$$

**Proposizione 1.3.5** (**Teorema del valor medio per gli integrali**).
Sia $F : \mathbb{R}^n \to \mathbb{R}^m$ una funzione **continuamente differenziabile**. Allora, per ogni $x, y \in \mathbb{R}^n$, si ha $$F (x) = F (y) + \int_0^1 J_F (y + t (x - y)) (x - y) dt$$
dove all'interno dell'integrale ho la [[matrice Jacobiana]]
