# Experiments

Standalone scripts that reproduce the figures in the project README. Each script
accepts a `--seed` argument and saves its output to `../figures/`.

Run any script with:

```bash
uv run python experiments/<script>.py --seed 0
```

## Planned scripts

- `copy_rate.py` — fraction of generated n-grams found verbatim in the corpus
- `perplexity_vs_order.py` — held-out perplexity against model order
