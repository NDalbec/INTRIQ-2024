---
marp: true
theme: default
title : Accurate Unsupervised Photon Counting from Transition Edge Sensor Signals
author : Nicolas Dalbec-Constant
paginate: true
math : True
class:
  # - invert
  - lead
---

## Visibility

![bg contain 50%](assets/UMAP2d.png)

---

## Accurate Unsupervised Photon Counting from Transition Edge Sensor Signals

Nicolas Dalbec-Constant

---

##

![bg contain 80%](assets/Area.png)

---

## Confidence

$$
C_n = \int p(n|s) p(s|n) ds = \int \frac{p(s|n)^2p(n)}{p(s)} ds = \int \frac{p(s|n)^2p(n)}{\sum_k p(s|k)p(k)} ds 
$$

- $p(s|n)$ : Probability density for a specific outcome $s$ given an $n$-photon input to the detector.
- $p(n|s)$ : Probability density that the input contained $n$ photons given that the detector measured outcome $s$.

$$
\text{Bayes’ theorem : }\quad p(n|s) =  \frac{p(s|n)p(n)}{p(s)}
$$


---

## Test

![width:500px](assets/TomographyOfPhotonNumber.png)
