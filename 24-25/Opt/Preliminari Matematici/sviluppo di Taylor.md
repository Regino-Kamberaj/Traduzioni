**Proposizione 1.3.4** 
Sia $f : \mathbb{R}^n \to \mathbb{R}$. Allora:
Se $f \in C^2 (\mathbb{R}^n)$, per ogni $x \in \mathbb{R}^n$ e $d \in \mathbb{R}^n$, esiste $t \in (0,1)$ tale che $\xi = x + td$ e
- Per lo sviluppo al secondo ordine, vale: $$f (x + d) = f (x) + \nabla f (x)^T d + \frac{1}{2} d^T \nabla^2 f (\xi) d$$
- Inoltre: $$f (x + d) = f (x) + \nabla f (x)^T d + \frac{1}{2} d^T \nabla^2 f (x) d + \beta (x, d)$$ dove $$\lim_{\|d\| \to 0} \frac{\beta (x, d)}{\|d\|^2} = 0$$
