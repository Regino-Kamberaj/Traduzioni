**Definizione 1.1.1**
Una funzione $\|\cdot\| : \mathcal U \to \mathbb R_+$ è una *norma* se soddisfa le seguenti proprietà:
- $\|x\| \geq 0$ per ogni $x\in\mathcal U$ e $\|x\| = 0$ se e solo se  $x=0 \quad (\text{definita positiva})$
- $\|\alpha x\| = \|\alpha\|\|x\|$ per ogni $x\in\mathcal U$ e $\alpha \in \mathbb R \quad (\text{homogeneità})$
- $\|x+y\| \leq \|x\|+\|y\|$ per ogni $x,y\in\mathcal U \quad (\text{disuguaglianza triangolare})$ 

**Esempio 1.1.1**
Esempi di norme nello spazio Euclideo ($\mathcal U = \mathbb R^n$) sono:
- La *norma Euclidea* ($\ell_2$): $\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x^Tx}$
- La *norma Manhattan* ($\ell_1$): $\|x\|_1 = \sum_{i=1}^n |x_i|$
- La *norma Infinito* ($\ell_{\infty}$): $\|x\|_{\infty} = \max_{i=1,\dots,n}|x_i|$
- La *norma* $\ell_p$, per $0<p<\infty$: $\|x\|_p = \sqrt{\sum_{i=1}^n |x_i|^p}$