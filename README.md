# Roast Lawmakers — The Long Roast

An entry for the [make.fun](https://make.fun) bounty
**"The Long Roast: Lawmakers and the File They Cannot Convert"**
(`u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7`).

## The entry

> The lawmakers writing the rules for AI, crypto, and the entire internet just forwarded their own bill to the IT helpdesk with the subject line 'PLEASE MAKE PDF' — attached as a Word document.

One satirical sentence, 191 characters — well under the 320-character cap.

## The joke

The setup grants lawmakers their full authority: they are writing the rules
for AI, crypto, and the entire internet. The turn undercuts it with the most
mundane failure imaginable — they cannot turn their own bill into a PDF, so
they forward it to the IT helpdesk begging in all caps. The punch lands on
the last few words: the desperate email was itself attached as a Word
document, the very format they could not escape. The detail is specific
(a forwarded bill, an IT helpdesk ticket, a subject line) rather than a
generic "old people don't understand computers" cliché, and the aim stays
on the lawmakers and the rules they write.

## How it works

`main.py` is deterministic Python using only the standard library. It holds
the sentence as a constant, verifies it against the competition gate
(UTF-8, 1–320 characters, a single line, not only whitespace), then writes
it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
re-reads the file to confirm the bytes on disk match exactly. It exits
non-zero if any check fails.

## How to run

```sh
python3 main.py
```

To write somewhere else (for example, local testing):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
