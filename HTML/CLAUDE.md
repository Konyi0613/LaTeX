# Writing these notes

Lecture notes for **Machine Learning (機器學習)**, NTU, Fall 2026, taught by
Hsuan-Tien Lin — <https://www.csie.ntu.edu.tw/~htlin/course/ml26fall/>.

Source material: `/home/konyi/Documents/Lecture/NTU/HTML/NN_handout.pdf`.
One handout becomes one chapter. `00_handout` is the course introduction and
lives in the Preface inside `HTML.tex`; `01_handout` is Chapter 1, and so on.
Chapter titles come from the course site (Ch.1 *The Learning Problem*, Ch.2
*Learning to Answer Yes/No*, Ch.3 *Types of Learning*, …).

## The cardinal rule

> 在保留簡報內容的前提下把脈絡補清楚。

Content may only ever be **added**, never removed. Every bullet, formula,
figure, table, quiz and bottom-line takeaway on a slide must survive into the
notes. What I contribute is the connective tissue the slides leave implicit:
why a definition is phrased that way, what a picture is actually showing, what
gap the next section fills.

Two failure modes to guard against, both of which have happened:

- **Silently dropping a figure or table.** `pdftotext` does not see them, so a
  deck read only as text looks complete when it is not. Before writing, render
  every slide (`pdftoppm -png -r 100 -f N -l N handout.pdf out`) and *look* at
  it. Compare the finished section against the deck slide by slide.
- **Redrawing a figure as a vague paraphrase.** A box-and-arrow sketch that
  loses the mechanism is worse than no figure. Reproduce what the original
  actually depicts (e.g. the recommender slide is two *aligned factor vectors*
  with dot size as magnitude, not a generic pipeline).

## Where things go

| File | Holds |
|---|---|
| `Lectures/lec_N.tex` | **content only** — starts at `\chapter`, no setup |
| `header.tex` | packages, theorem envs, page layout, **all `\tikzset` styles** |
| `Math.tex` | math macros and operators (`\sign`, `\argmin`, …) |
| `Figures/` | images lifted from a handout (photos, real-data plots) |
| `HTML.tex` | preamble, Preface, `\lec{1}{3}` range |

Never define a style or macro inside a lecture file. If a diagram needs a new
TikZ style, it goes in `header.tex` next to the existing ones, with a comment
saying what it is for — later chapters reuse it.

## Chapter skeleton

```latex
\chapter{Learning to Answer Yes/No}
\lecture{2}{16 Sep.}{}          % date from the course schedule

\begin{prev} ... \end{prev}     % what the previous chapter left open
                                % then the question this chapter answers

\section{Perceptron Hypothesis Set}\label{sec:...}
\source{slides p.2--6}          % slide range for every section
\subsection{...}
...

\hrulebar
\subsection*{Summary}
\begin{description} ... \end{description}   % the deck's own summary slide
                                % closing paragraph pointing at the next chapter
```

`\section` mirrors the deck's own sections. `tocdepth` is 1, so subsections are
free to be used generously.

## Environments — which one for what

| Slide element | Environment |
|---|---|
| bottom-line highlighted takeaway | `moral` |
| the banner/bottom line that **asks** something | `question` |
| a *Fun Time* quiz | `exercise[Fun Time]` + `\begin{proof}[Reference Answer]` |
| a definition | `definition`, term marked with `\vocab{}` |
| a worked application | `eg` |
| pseudocode | `algorithm` (algorithm2e), `\autoref`-able |
| a stated fact that I prove | `theorem` / `lemma` + `proof` |
| context I add | `remark`, `note`, `intuition`, `observation` |
| symbol conventions | `notation` |
| recall of earlier material | `prev`, `recall` |

`moral` is for conclusions. **A question never goes in a `moral` box.** When a
`question` box asks something, the surrounding prose must not ask it again.

Numbered envs (`theorem`, `question`, `exercise`, `eg`, `definition`, …) share
one counter, so they read in document order. Do not use numbered envs in the
Preface — the section counter is 0 there.

## Tables

`booktabs` rules and `|` separators do not meet: the rule separation leaves a
gap where the vertical line should cross. Any table that has both must open with
`\solidrules` (defined in `header.tex`) right before `\begin{tabular}`, so the
verticals run unbroken through `\toprule`, `\midrule` and `\bottomrule`. It is
a local length change — put it inside the surrounding `center`/`adjustbox`
group, never in the preamble.

## Figures

Redraw every slide figure in TikZ. Shared styles already in `header.tex`:

- `mlbox` / `mlop` / `mlarrow` — the learning-flow diagrams
- `dpos` / `dneg` / `poshalf` / `neghalf` / `sepline` / `wvec` — classification
  pictures (`\circ` for `+1`, `\times` for `-1`, shaded half-spaces, the weight
  vector)
- `dcls=<colour>` / `dunl` / `plotbox` — multi-class and unlabelled scatter plots

Wrap anything wide in `\begin{adjustbox}{max width=\textwidth}`. Prefer
explicit coordinates over `positioning` chains for multi-part diagrams — they
are predictable.

When a figure illustrates an **algorithm running**, simulate it rather than
drawing it by hand: compute the real iterates in a throwaway script, emit the
TikZ, and let every frame's separator, shading and weight arrow come from the
actual state. Say plainly in the text when the data set is mine rather than the
slide's.

### TikZ or a screenshot?

Default to TikZ — almost every slide figure is a schematic and redraws cleanly.
Fall back to lifting the image out of the handout only when it is

- a **real photograph** (the reinforcement-learning dog), or
- **real data rendered as an image** that cannot honestly be invented — a grid
  of actual handwritten digits, a scatter of thousands of real feature values.

Never dump screenshots loose in the project root or next to the `.tex` files.
They belong in `Figures/`, with a descriptive lower-case name, and are pulled in
with `\includegraphics[width=...]{Figures/name.png}`.

Get them out cleanly rather than cropping a screen capture by hand:

```sh
pdfimages -f N -l N -j handout.pdf out        # a genuine embedded photo
pdftoppm -png -r 400 -f N -l N handout.pdf p  # else render the page big, then crop
```

Crop to the artwork only — no slide titles, no surrounding coloured panels — and
flatten the slide's pale background gradient to white so the figure sits on the
page like the TikZ ones. A figure lifted this way still needs the same
surrounding prose as any other: say what it shows and why it is there.

## Notation

- `\mathcal{X}`, `\mathcal{Y}`, `\mathcal{D}`, `\mathcal{H}`, `\mathcal{A}`
- inputs are plain `x` in Ch.1 (still abstract) and bold `\bm{x}` from Ch.2 on,
  once they have coordinates — the switch is announced in a `notation` box
- transpose `^\top`; `\norm{}` and `\abs{}` from *physics*; `\sign`;
  Iverson bracket `\llbracket \cdot \rrbracket`
- `\vocab{}` on a term's first, defining appearance only

## Prose

Concise and declarative. Add context, don't pad — an explanation that restates
the slide in longer words is worse than the slide. Prefer one well-aimed
sentence to a bulleted walkthrough; bullets are for things the deck itself
bulleted. Keep a thread running between sections, so each one opens by saying
what the previous one left unfinished.

## Build and check

```sh
latexmk -xelatex -synctex=1 -interaction=nonstopmode HTML.tex
grep -n "^!\|Overfull\|Underfull" HTML.log      # must be empty
ls HTML.synctex.gz                              # must exist and be fresh
pdftoppm -png -r 80 -f A -l B HTML.pdf out      # then actually look
```

**`-synctex=1` is not optional.** It is what lets the editor jump between a
line of `.tex` and the spot on the page; without it `HTML.synctex.gz` silently
disappears and forward/inverse search stops working. Never compile this project
without it.

Always render the changed pages and inspect them; LaTeX compiling is not the
same as the page being right. Watch for:

- a figure stranded at the top of the next page, leaving the previous one half
  empty — fix by tightening the diagram's own vertical gaps, not with `\vspace`
- labels colliding in a TikZ picture
- an unbreakable `\texttt` URL or email overflowing — use `\nolinkurl`
