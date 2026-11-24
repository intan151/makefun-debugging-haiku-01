# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/intan151/makefun-debugging-haiku-01/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/intan151/makefun-debugging-haiku-01/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

An entry for the [make.fun](https://make.fun) bounty **"Seventeen Syllables of
Debugging"**: one haiku about debugging, in the classic 5-7-5 syllable shape,
at most 200 characters.

## The haiku

> Cursor blinks at three
> the breakpoint holds its breath
> my own typo grins

Three in the morning, the cursor blinking, a breakpoint waiting — and then the
turn: the bug was never hiding in the code. It was my own typo, grinning back
at me.

Syllables: 5 + 7 + 5 = 17. Total length: 72 characters.

## How it works

`main.py` (Python standard library only, no dependencies) writes the haiku to
`/output/entry.txt`. It is fully deterministic — every run produces byte-identical
output.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the haiku to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — the claim wallet for this entry
