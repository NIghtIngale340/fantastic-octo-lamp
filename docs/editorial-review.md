# Writeup cleanup completed

Updated 29 October 2026 (Asia/Manila).

The revised collection keeps the technical steps and removes repeated defensive wording, unnecessary terminal dumps, and explanations that did not agree with the evidence. The focus is a clear account of the clue, method, result and remaining uncertainty.

## What changed

- **181 of 192 drafts updated**, including prose, code, evidence captions and source-link repairs. This includes the earlier editorial changes; not every file required a full rewrite.
- **99 writeups now use fresh terminal captures.** The capture pass contains 105 successful runs, including the pilot and corrected versions. The selected images were captured while their commands executed in Konsole, rather than by replaying stored output.
- Short Caesar and ROT13 examples now use `tr`. Longer decoders use readable Python files whose complete source appears in the writeup and is available to download.
- Packet screenshots use the commands printed in the text, short input filenames, distinct values, and bounded output where needed. The broad network query shows infrastructure addresses as well as the three clients and explains the distinction.
- The collection now embeds **152 evidence images**, down from 274 before these passes. Repeated failure notices, missing-file inventories, and helper-script screenshots were removed where a linked record was clearer. The original images remain archived.
- Unreachable web challenges remain investigation notes. Missing-artifact methods and teammate-reported answers remain explicitly attributed.

## Technical corrections

The changes also repair factual and reproducibility problems:

- **#75 Hidden:** the apparent DLL is an NTFS disk image. The writeup now shows the partition offset, named-stream identifier, extraction commands and recovered JPEG.
- **#79 Sequence:** explains both words and the exact Fibonacci positions, with a runnable decoder.
- **#311 SQL Skillz:** uses the real `medications` table and its two medication columns.
- **#326–336 Aurora SQL:** restores the 11 queries preserved with the database verification, including the correct schemas, joins and column names.
- **#336 Two Places at Once:** distinguishes database username `kbhatt` from the teammate-reported accepted flag spelling `kbhat`.
- **#308 Infrastructure Pivot:** follows the saved DNS prompt and record rather than claiming the domain came from captured HTTP Host headers.
- **#18 Rotation 36:** distinguishes a reversible implementation from evidence for the intended shift and an accepted submission.
- **#296/#335/#336:** conclusions are limited to the observed traffic, outlier threshold and access records.

## Checks completed

All 192 drafts passed local link, code-fence, shell-syntax and Python-syntax checks. The 11 Aurora SQL blocks match their saved queries. All 335 images in the expanded capture manifest match their recorded hashes. The 105 successful capture runs retain their logs; the selected captures passed output-error and overflow checks. Representative new images and the recovered visual flags were also inspected directly.

Every existing flag code block was preserved. No new flag submissions or platform-acceptance claims were made.

## Evidence limits

Unavailable services were not retested during this offline cleanup. Missing original artifacts remain missing, and retained live-site results are historical checks. Images from the earlier terminal pass are labeled as transcript displays where still used. Fresh captures are later local reproductions, not original competition-session screenshots.

[Open the revised collection](writeup-index.md) · [Validation results](../data/cleanup-validation.json) · [Changed files](../data/cleanup-results.json) · [Capture records](../writeups/screenshots/capture-manifest.json)

Local backup folders preserve the versions from before each editorial pass. They are kept outside the published repository content.
