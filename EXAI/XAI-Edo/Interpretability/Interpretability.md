Alcuni modelli sono spiegabili per costruzione (by design); in questo caso si parla di interpretability.
# Modelli lineari
I modelli lineari calcolano l'output come $f(x)=\sum_{i=1}^P\beta_ix_i+\beta_0$, dove $P$ è il numero di featues. I modelli lineari sono molto interpretabili perché i coefficienti $\beta_i$ mi dicono il peso di ogni features, cioè mi dicono l'impatto che ha una modifica di $x_i$ sul risultato; in pratica se $x_i$ incrementa di una unità allora $f(x)$ incrementa di $\beta_i$.
Il problema dei modelli lineari è dato dal fatto che il mondo non è lineare. Non riescono infatti a imparare la variazione dell'output rispetto alla variazione di più features contemporaneamente.
# Modelli
I segurenti modelli si basano, chi più chi meno, sugli [alberi di decisione](Decision%20tree.md):
- [Rule-based system](regio/Interpretability/Rule-based%20system.md)
- [Rule fit](regio/Interpretability/Rule%20fit.md)
- [Generalized additive models (GAMs)](regio/Interpretability/Generalized%20additive%20models%20(GAMs).md)