**Definizione 1.3.3 (Derivata Direzionale)**
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che una funzione ha ***derivata direzionale*** $Df(x, d)$ in un punto $x \in \mathbb{R}^n$ lungo la direzione $d \in \mathbb{R}^n$ se il limite: $$\lim_{t \to 0^+} \frac{f(x + td) - f(x)}{t} = Df(x, d)$$ **esiste ed è finito**.

**Definizione 1.3.4 (Derivata Parziale)**
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Diciamo che una funzione ha ***derivata parziale*** $\frac{\partial f}{\partial x_j}(x)$ in un punto $x \in \mathbb{R}^n$ rispetto alla variabile $x_j$ se $f$ ha **una derivata direzionale lungo** $e_j$ e  $$Df(x, e_j) = \frac{\partial f (x)}{\partial x_j}$$

**Definizione 1.3.5 (Gradiente)**
Sia $f : \mathbb{R}^n \to \mathbb{R}$ e si supponga che $f$ ammetta in un punto $x$ la **derivata parziale** rispetto a ciascuna variabile $x_i$, con $i = 1, \dots, n$. => Derivata parziale definita su ogni direzione
Definiamo il ***gradiente*** $\nabla f(x)$ di $f$ in $x$ come il vettore dato da:$$\nabla f(x) = \begin{pmatrix} \frac{\partial f (x)}{\partial x_1} \\ \vdots \\ \frac{\partial f (x)}{\partial x_n}\end{pmatrix}$$
=> nota che ongi funzione continuamente differenziale è sempre continua!