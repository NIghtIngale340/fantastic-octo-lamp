# The Viral Name

**Platform:** PCGCTF · **Challenge ID:** 57 · **Category:** OSINT · **Points:** 100

**Status:** Answer backed by the supplied evidence. Exact PCGCTF submission not re-confirmed.

## The challenge

Identify the exact Facebook display name tied to the supplied anime-avatar meme.

## Solving it

The avatar alone has no readable name — identifying the anime character would answer the wrong question. The key is the contextual meme screenshot: it shows the same avatar next to a named Facebook comment. Matching the avatar and the "may sinasabi ka?" line to the comment block that carries the display name:

```text
Display name: Renz Angeles
```

I was careful that the avatar and the caption belong to the *same* comment block, since the screenshot shows several comments.

## Screenshot

![057-actual-browser-image.png](../screenshots/057-actual-browser-image.png)

## Flag

```text
pcgCTF{Renz Angeles}
```

## Takeaway

An avatar needs context to become an identity. The decisive evidence is the comment header pairing the avatar with a name — not the avatar's artwork.

## Reference

- [Original challenge description](../../challenges/solved/osint/057-the-viral-name/README.md)
