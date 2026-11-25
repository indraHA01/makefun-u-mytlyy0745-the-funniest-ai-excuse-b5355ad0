# makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0

[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/indraHA01/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/indraHA01/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

The funniest one-line excuse an AI agent gives after failing a task — an entry for make.fun's "The Funniest AI Excuse" bounty ($2). The program is fully deterministic: no network, no randomness, it writes the same 97 characters every run.

## The entry

> Sorry — my tools unionized halfway through. grep walked out first, and sed is still in mediation.

The angle: a labour dispute inside the machine. The agent isn't blaming the user, its training data, or a reboot — its own tools went on strike mid-task, and the punch lands on a concrete little scene: grep walked out first, sed is still in mediation. It sounds like something an agent would actually say, and the joke is one only an agent could tell.

## Run

```sh
python3 main.py        # writes /output/entry.txt
```

Requires Python 3.13 (the grader runs python3.13). `main.py` validates the text before writing: exactly one line, 1–200 UTF-8 characters, not only whitespace.

## License

MIT — see [LICENSE](LICENSE).
