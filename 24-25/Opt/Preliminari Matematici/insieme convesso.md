**Definizione 1.3.12**
Un insieme $S \subseteq \mathbb{R}^n$ è convesso se per ogni $x,y \in S$ e per ogni $\lambda \in [0,1]$ abbiamo: $$(1-\lambda)x+\lambda y \in S$$
		![[Pasted image 20251222210049.png]]

**Esempio 1.3.2**
La palla $B(\bar x, \epsilon)$ è un insieme convesso. Infatti siano $x,y \in B(\bar x,\epsilon)$ e sia $\lambda \in [0,1]$, tale che $z = (1-\lambda)x +\lambda y$. Allora abbiamo: 
- $∥z − \bar x∥ \, = \, ∥(1 − λ)x + λy − \bar x∥ \, =$
- $∥(1 − λ)x + λy − \bar x + λ\bar x − λ\bar x∥ \, = \, ∥(1 − λ)(x − \bar x) + λ(y − \bar x)∥ \,$
- $≤ \, ∥(1 − λ)(x − \bar x)∥ + ∥λ(y − \bar x)∥ \, = \, (1 − λ)∥x − \bar x∥ + λ∥y − \bar x∥$
- $≤\, (1 − λ)ϵ + λϵ \, = \, ϵ$ 

Dove la ultima diseguaglianza deriva dalla definizione di $B(\bar x, \epsilon)$ e $x,y \in B(\bar x , \epsilon)$ (vedi [[compatto]] per definizione palla)