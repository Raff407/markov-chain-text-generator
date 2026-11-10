# Derivations — Markov Chain Text Generator

This document records the mathematical derivations underpinning the implementation,
written out in full before the corresponding code.

## Summary of results

| Component | Definition |
|---|---|
| Markov property | $P(w_t \mid w_{1:t-1}) \approx P(w_t \mid w_{t-k:t-1})$ |
| Maximum-likelihood estimate | $P(w \mid c) = \text{count}(c, w) / \text{count}(c)$ |
| Stationary distribution | $\pi = \pi P$ |
| Add-k smoothing | $P(w \mid c) = \frac{\text{count}(c, w) + k}{\text{count}(c) + kV}$ |
| Perplexity | $\exp\left(-\frac{1}{N} \sum_i \log P(w_i \mid c_i)\right)$ |

## Stage 1: Toy chain

_To be completed._

## Stage 2: Word-level bigram model

_To be completed._

## Stage 3: Order-k and boundaries

_To be completed._

## Stage 4: Character-level model

_To be completed._

## Stage 5: Evaluation

_To be completed._

## Stage 6: Command-line tool

_To be completed._
