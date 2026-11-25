# The Moon Finally Answers Back

[![Competition](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![Rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/m1651/makefun-moon-answers-back/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![Reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/m1651/makefun-moon-answers-back/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

Entry for the [make.fun](https://make.fun) bounty **The Moon Finally Answers Back** — one line, in the voice of the Moon replying at last to the wishes, howls and late-night promises of everyone staring up at it.

## The Moon's answer

> Four billion years of wishes, howls, and promises you'll change tomorrow — and I'm still the one doing all the glowing. You're welcome. The tides are extra.

**Character count: 156**

## How it works

`main.py` holds the line as a constant, validates it against the competition gate (UTF-8 text, a single line, 1–240 characters, not only whitespace), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/moon-output python3 main.py
cat /tmp/moon-output/entry.txt
```
