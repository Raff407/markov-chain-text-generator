# Markov Chain Text Generator

[![CI](https://github.com/Raff407/markov-chain-text-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/Raff407/markov-chain-text-generator/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-in%20development-orange)

An n-gram Markov chain language model written with the Python standard library, supporting word- and character-level generation of arbitrary order, smoothing, held-out perplexity evaluation and a command-line interface.

> **Status:** in development. The repository structure, tooling and test infrastructure are in place; implementation is proceeding stage by stage according to the roadmap below.

## Contents

- [Overview](#overview)
- [Features](#features)
- [Mathematical background](#mathematical-background)
- [Roadmap](#roadmap)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Experiments](#experiments)
- [Design principles](#design-principles)
- [References](#references)
- [License](#license)

## Overview

A language model assigns a probability distribution to the next token given its context. An order-$k$ Markov chain approximates that context by the previous $k$ tokens and estimates the distribution by counting. This project implements such a model from scratch and uses it to study the central trade-off of language modelling: higher orders produce more fluent samples but generalise worse, eventually reproducing the training text verbatim.

The model is trained on public-domain texts from Project Gutenberg and evaluated by held-out perplexity with smoothing and backoff, together with a copy-rate metric that measures how much generated text is lifted directly from the corpus.

## Features

- Word-level and character-level tokenisation with sentence-boundary tokens
- Order-k models with deterministic, seeded sampling
- Add-k smoothing and simple backoff for unseen contexts
- Held-out perplexity and verbatim copy-rate evaluation
- Toy transition-matrix chain with stationary distribution by power iteration
- Model serialisation to JSON and a command-line interface

## Mathematical background

| Component | Definition |
|---|---|
| Markov property | $P(w_t \mid w_{1:t-1}) \approx P(w_t \mid w_{t-k:t-1})$ |
| Maximum-likelihood estimate | $P(w \mid c) = \text{count}(c, w) / \text{count}(c)$ |
| Stationary distribution | $\pi = \pi P$ |
| Add-k smoothing | $P(w \mid c) = \frac{\text{count}(c, w) + k}{\text{count}(c) + kV}$ |
| Perplexity | $\exp\left(-\frac{1}{N} \sum_i \log P(w_i \mid c_i)\right)$ |

Full derivations are recorded in [`docs/derivations.md`](docs/derivations.md).

## Roadmap

- [ ] **Stage 1: Toy chain.** Three-state chain as a matrix; simulated frequencies agree with the stationary distribution.
- [ ] **Stage 2: Word-level bigram model.** Gutenberg corpus cleaning, tokenisation and weighted sampling.
- [ ] **Stage 3: Order-k and boundaries.** Arbitrary-order contexts with start/end tokens; deterministic seeded generation.
- [ ] **Stage 4: Character-level model.** Shared implementation over token type; copy rate against order.
- [ ] **Stage 5: Evaluation.** Contiguous train/test split; perplexity with add-k smoothing and backoff against order.
- [ ] **Stage 6: Command-line tool.** CLI, JSON persistence, documented API; ≥ 80% coverage.

## Project structure

```text
markov-chain-text-generator/
├── .github/workflows/ci.yml   # Lint, format check and tests on Python 3.12 / 3.13
├── data/                      # Downloaded datasets (git-ignored)
├── docs/derivations.md        # Mathematical derivations
├── experiments/               # Reproducible scripts that generate figures
├── figures/                   # Saved plots referenced in this README
├── src/
│   └── markov/
│       ├── __init__.py   # Package metadata
│       ├── tokenise.py   # Word and character tokenisers with sentence-boundary tokens
│       ├── model.py      # MarkovModel
│       ├── smoothing.py  # Add-k smoothing and backoff
│       ├── toy_chain.py  # Matrix Markov chain and stationary distribution
│       └── cli.py        # Command-line interface
├── tests/                     # pytest suite
├── pyproject.toml             # Packaging and tool configuration
└── uv.lock                    # Locked dependency versions
```

## Getting started

### Prerequisites

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

### Installation

```bash
git clone https://github.com/Raff407/markov-chain-text-generator.git
cd markov-chain-text-generator
uv sync
```

### Running the tests

```bash
uv run pytest
```

### Linting and formatting

```bash
uv run ruff check .
uv run ruff format .
```

### Command-line usage

```bash
uv run python -m markov.cli --corpus data/pg1342.txt --order 3 --words 100 --seed 1
```

## Experiments

Each script in [`experiments/`](experiments/) is deterministic given its seed and writes its output to [`figures/`](figures/).

- `copy_rate.py` — fraction of generated n-grams found verbatim in the corpus
- `perplexity_vs_order.py` — held-out perplexity against model order

Results and figures will be added to this section as each stage is completed.

## Design principles

- **From scratch.** The algorithm itself uses only Python and NumPy. scikit-learn (and, where noted, PyTorch) is used solely as a reference implementation in tests and for loading datasets.
- **Test-driven.** Each stage begins with a failing test against a hand-computed value or a reference implementation. Target coverage is at least 80%.
- **No mutation.** Public functions return new arrays and objects and never modify their inputs.
- **Reproducible.** Every stochastic routine and experiment accepts an explicit random seed.
- **Validated boundaries.** Public functions check input shapes and dtypes and fail with clear error messages.

## References

1. D. Jurafsky, J. H. Martin — *Speech and Language Processing*, ch. 3: N-gram Language Models. <https://web.stanford.edu/~jurafsky/slp3/>
2. C. E. Shannon — *A Mathematical Theory of Communication*, Bell System Technical Journal, 1948.
3. C. M. Grinstead, J. L. Snell — *Introduction to Probability*, ch. 11: Markov Chains.
4. A. Karpathy — *Neural Networks: Zero to Hero*, makemore part 1. <https://karpathy.ai/zero-to-hero.html>
5. Project Gutenberg. <https://www.gutenberg.org>

## License

Released under the [MIT License](LICENSE).
