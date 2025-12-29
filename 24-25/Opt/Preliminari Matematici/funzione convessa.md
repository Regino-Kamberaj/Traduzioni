
**Definizione 1.3.13** 
Diciamo che una funzione $f : \mathbb{R}^n \to \mathbb{R}$ è:
- **convessa** se, per ogni $x, y \in \mathbb{R}^n$ e $\lambda \in [0,1]$, si ha:	$$f (\lambda x + (1 - \lambda) y) \leq \lambda f (x) + (1 - \lambda) f (y)$$ (funzione sta sotto per qualsiasi $x,y$)

- **strettamente convessa** se, per ogni $x, y \in \mathbb{R}^n$ e $\lambda \in (0,1)$, si ha:$$f (\lambda x + (1 - \lambda) y) < \lambda f (x) + (1 - \lambda) f (y)$$
- **fortemente convessa** se esiste $\mu > 0$ tale che $f (x) - \mu \|x\|^2$ è una **funzione convessa**, ovvero $f (x) = g (x) + \mu \|x\|^2$ con $g$ funzione convessa.

=> Ad esempio le norme sono funzioni convesse. Infatti preso $\lambda in [0,1]$ e $x,y \in \mathbb{R}^n$ abbiamo: $$ ||(1-\lambda)x+\lambda y|| \, \leq \, ||(1-\lambda)x|| + \lambda ||y||  \, = \, (1-\lambda)||x|| + \lambda ||y|| $$
![[Pasted image 20251222213451.png]]

**Proposizione 1.3.7** Sia $f : \mathbb{R}^n \to \mathbb{R}$ una funzione *fortemente convessa*. Allora $f$ è [[coerciva]] e **strettamente convessa**.

![[Pasted image 20251222213714.png]]

**Proposizione 1.3.8** Sia $f : \mathbb{R}^n \to \mathbb{R}$. Le seguenti proprietà valgono:
- Se  $f \in C^1 (\mathbb{R}^n)$, allora $f$ è **convessa** se e solo se:	$$f (y) \geq f (x) + \nabla f (x)^T (y - x) \quad \forall x, y \in \mathbb{R}^n$$ (funzione sta sopra)

- Se $f \in C^2 (\mathbb{R}^n)$, allora $f$ è **convessa** se e solo se $$\nabla^2 f (x) \succeq 0 \quad \forall x \in \mathbb{R}^n$$ (Hessiana semidefinita positiva)

- Inoltre, se $\nabla^2 f (x) \succ 0$ per ogni $x \in \mathbb{R}^n$, allora $f$ è **strettamente convessa**.

- Infine $f$ è **strettamente convessa** se e solo se $\exists m > 0$ t.c $\lambda_{min}(\nabla^2 f(x))\geq m \, \forall x \in \mathbb{R}^n$

	![[Pasted image 20251222213901.png]]