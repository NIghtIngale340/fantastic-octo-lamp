# Silent Signal

**Platform:** PCGCTF · **Challenge ID:** 5 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Translate a string of Morse into text. The description adds one formatting rule: spaces become underscores.

## Solving it

Dots, dashes, letter-gaps and `/` between words make it obvious it's Morse before you touch a tool. I mapped the groups to letters, kept `/` as the word separator, and joined the decoded words with underscores as the challenge asked:

```sh
python3 -c "
m=dict(zip('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
msg='... -- ...'  # paste the Morse groups here
print('_'.join(''.join(m[t] for t in w.split()) for w in msg.split('/')))"
```

Run against the challenge's Morse, that gives:

```text
CYBER_SECURITY_IS_EVERYONES_RESPONSIBILITY
```

Grammatical English, every group decoding with the same alphabet — that's the message.

## Screenshot

![005-step-01.png](../screenshots/005-step-01.png)

## Flag

```text
pcgCTF{CYBER_SECURITY_IS_EVERYONES_RESPONSIBILITY}
```

## Takeaway

The separators are part of the data. Decode first, then apply only the formatting rule the challenge actually states.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/005-silent-signal/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/cryptography/005-silent-signal/solution.md>)
