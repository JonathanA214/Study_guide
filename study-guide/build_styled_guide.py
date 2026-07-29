#!/usr/bin/env python3
"""Build a study-guide PDF matching the user's Enhanced guide visual style."""

from pathlib import Path
from weasyprint import HTML

CSS = """
@page {
  size: A4;
  margin: 0.5in 0.55in 0.55in 0.55in;
  @bottom-center {
    content: "Final Exam Study Guide — page " counter(page);
    font-size: 7.5pt;
    color: #555;
  }
}
* { box-sizing: border-box; }
body {
  font-family: "DejaVu Sans", Arial, sans-serif;
  font-size: 8pt;
  line-height: 1.32;
  color: #1a1a1a;
}
h1.doc-title {
  font-size: 16pt;
  color: #1a1a1a;
  margin: 0 0 0.15em;
  border-bottom: 2px solid #7A1F3D;
  padding-bottom: 0.2em;
}
.subtitle {
  font-size: 9.5pt;
  font-weight: bold;
  color: #7A1F3D;
  margin: 0.4em 0 0.15em;
}
.meta {
  font-size: 7.5pt;
  color: #444;
  font-style: italic;
  margin-bottom: 0.5em;
}
.toc {
  background: #f7f7f9;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.45em 0.7em;
  margin: 0.5em 0 0.7em;
  font-size: 7.5pt;
}
.toc strong { color: #7A1F3D; }
.toc ul { margin: 0.2em 0 0 1.1em; padding: 0; }
.toc li { margin: 0.05em 0; }
.callout {
  background: #FAF5F6;
  border-left: 3px solid #7A1F3D;
  padding: 0.35em 0.55em;
  margin: 0.4em 0 0.55em;
  font-size: 7.5pt;
}
.callout .tag { color: #7A1F3D; font-weight: bold; }
h2 {
  font-size: 12pt;
  color: #7A1F3D;
  margin: 0.85em 0 0.25em;
  page-break-after: avoid;
}
h3 {
  font-size: 9pt;
  color: #7A1F3D;
  margin: 0.55em 0 0.15em;
  page-break-after: avoid;
}
h4 {
  font-size: 8pt;
  color: #333;
  margin: 0.4em 0 0.1em;
}
p { margin: 0.2em 0 0.35em; }
ul, ol { margin: 0.15em 0 0.4em 1.2em; padding: 0; }
li { margin: 0.08em 0; }
strong { font-weight: bold; }
em { font-style: italic; }
code {
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 6.9pt;
  background: #f0f0f0;
  padding: 0 0.2em;
  border-radius: 2px;
}
pre {
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 6.9pt;
  background: #f7f7f9;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0.4em 0.55em;
  margin: 0.3em 0 0.5em;
  white-space: pre-wrap;
  page-break-inside: avoid;
  line-height: 1.22;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.35em 0 0.55em;
  font-size: 7pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.18em 0.35em;
  text-align: left;
  vertical-align: top;
}
th { background: #f0e6ea; color: #7A1F3D; }
.tag { color: #7A1F3D; font-weight: bold; }
.struck { text-decoration: line-through; color: #888; }
.note-box {
  background: #FAF5F6;
  border: 1px solid #e0c8cf;
  padding: 0.35em 0.5em;
  margin: 0.35em 0;
  border-radius: 3px;
}
hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 0.7em 0;
}
"""

html = r"""
<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>Final Exam Study Guide</title></head>
<body>

<h1 class="doc-title">Final Exam Study Guide</h1>

<div class="toc">
  <strong>Contents</strong>
  <ul>
    <li>Chapter 8 — Decrease-by-Half (Divide and Conquer)</li>
    <li>Chapter 9 — Randomization</li>
    <li>Chapter 10 — Reduction</li>
    <li>Chapter 11 — Dynamic Programming</li>
    <li>Chapter 12 — Lower Bounds</li>
    <li>Chapter 13 — Easy and Impossible Problems</li>
    <li>Chapter 14 — NP-Hard / NP-Completeness</li>
    <li>Parallel Algorithms</li>
    <li>Quick-Reference Table · Exam Questions · Study Strategy</li>
  </ul>
</div>

<p class="subtitle">Final Exam Study Guide — Chapters 8–14 + Parallel Algorithms</p>
<p class="meta">110-minute limit · one page of notes allowed · non-cumulative (covers Ch 8–14 only) · bring your CWID</p>

<div class="callout">
  <span class="tag">[Slides]</span> marks material taken directly from Kevin A. Wortman lecture slides.
  Struck-through topics are <strong>not on the exam</strong>: American Change Making; Ch.&nbsp;12.6 Reduction Arguments; <strong>parallel merge</strong> details.
  You will <strong>not</strong> be asked to prove an NP-complete reduction.
</div>

<!-- ==================== CH 8 ==================== -->
<h2>Chapter 8 — Decrease-by-Half (Divide and Conquer)</h2>

<h3>8.1 The Big Idea</h3>
<p>Solve a problem by reducing it to a smaller instance of the same problem, then combining the sub-solution(s) into a full solution. Decrease-by-half specifically shrinks the input by a <strong>constant fraction</strong> each step (not just by 1, as in decrease-by-one patterns like insertion sort).</p>

<p><span class="tag">[Slides]</span> General template:</p>
<pre>decrease_by_half(INPUT):
    if INPUT is base case:
        return base case solution
    left_input, right_input = divide INPUT in half
    left_solution  = decrease_by_half(left_input)
    right_solution = decrease_by_half(right_input)
    entire_solution = combine left_solution with right_solution
    return entire_solution</pre>
<p>Three phases every time: <strong>Divide → Recursion → Combine</strong>.</p>

<p><span class="tag">[Slides]</span> Formal definition of algorithm (Def. 6): a process that, given a problem instance, produces a solution, and is (1) clear enough to implement, (2) correct, and (3) terminates (finite time).</p>

<p><span class="tag">[Slides]</span> <strong>Pitfall — infinite recursion:</strong> base cases and combine must work together so recursion bottoms out for every <code>n</code>. Best practice: general-case threshold <code>t = 2</code> (base cases handle <code>n = 0</code> and <code>n = 1</code>; general case <code>n ≥ 2</code>). Missing <code>n = 1</code> causes infinite recursion — e.g. <code>dbh_sum([7])</code> splits into <code>[]</code> and <code>[7]</code> forever.</p>

<h3>8.2 Example: Summation</h3>
<p>Split the array in half, recursively sum each half, add the results.</p>
<pre>dbh_sum(L):
    n = len(L)
    if n == 0: return 0
    if n == 1: return L[0]
    half = n / 2
    left  = L[:half]
    right = L[half:]
    return dbh_sum(left) + dbh_sum(right)</pre>
<p><span class="tag">[Slides]</span> Dividing: <code>half = n/2</code> (integer truncation); each slice copy costs <code>n/2</code> steps. Primitive = 1 step; list of <code>k</code> elements = <code>k</code> steps.</p>
<p><span class="tag">[Slides]</span> Reality check: <code>dbh_sum</code> is <strong>O(n log n)</strong>; naïve iterative sum is <strong>O(n)</strong> and simpler. Decrease-by-half is not automatically best — compare against naïve first.</p>

<h3>8.3 Analyzing Decrease-by-Fraction Algorithms — Master Method</h3>
<p><span class="tag">[Slides]</span> Master-form recurrence:</p>
<pre>T(n) = r · T(n/d) + c(n)     ∀ n ≥ t
T(n) ∈ O(1)                  ∀ n &lt; t
where c(n) ∈ O(n^k); r,t ≥ 1; d &gt; 1; k ≥ 0</pre>
<table>
  <tr><th>Symbol</th><th>Meaning</th><th>Constraint</th></tr>
  <tr><td><code>r</code></td><td>number of recursive calls</td><td>r ≥ 1</td></tr>
  <tr><td><code>d</code></td><td>divisor of input size</td><td>d &gt; 1</td></tr>
  <tr><td><code>t</code></td><td>general-case threshold</td><td>t ≥ 1</td></tr>
  <tr><td><code>k</code></td><td>exponent in non-recursive work c(n)</td><td>k ≥ 0</td></tr>
</table>
<p><span class="tag">[Slides]</span> <strong>Master Theorem:</strong></p>
<ol>
  <li>If <code>r &lt; d^k</code> → <code>T(n) ∈ O(n^k)</code> (case 1)</li>
  <li>If <code>r = d^k</code> → <code>T(n) ∈ O(n^k log n)</code> (case 2)</li>
  <li>If <code>r &gt; d^k</code> → <code>T(n) ∈ O(n^(log_d r))</code> (case 3)</li>
</ol>
<p><span class="tag">[Slides]</span> <strong>6-step Master Method</strong> (memorize):</p>
<ol>
  <li>Identify threshold <code>t</code> (best practice: <code>t = 2</code>)</li>
  <li>Analyze base case (<code>n &lt; t</code>) → usually O(1)</li>
  <li>Step-count general case → derive <code>T(n) = r·T(n/d) + c(n)</code></li>
  <li>Identify/check parts: <code>c(n), r, d, t, k</code></li>
  <li>Compare <code>r</code> vs <code>d^k</code> → pick case</li>
  <li>Simplify and conclude (e.g. O(n log n))</li>
</ol>
<p><span class="tag">[Slides]</span> Worked <code>dbh_sum</code>: t=2; T(n)=2T(n/2)+n+4; r=2,d=2,k=1 → 2=2 → case 2 → <strong>O(n log n)</strong>.</p>

<h3>8.4 Merge Sort</h3>
<p><span class="tag">[Slides]</span> Sorting problem: input list U of comparable elements; output S in non-decreasing order. Lists of size ≤ 1 are vacuously sorted.</p>
<pre>merge_sort(U):
    if n ≤ 1: return U
    half = n / 2
    left  = U[:half]; right = U[half:]
    return merge(merge_sort(left), merge_sort(right))

merge(LS, RS):
    S = []; li = 0; ri = 0
    while li &lt; len(LS) and ri &lt; len(RS):
        if LS[li] &lt;= RS[ri]: S.add_back(LS[li]); li += 1
        else:                S.add_back(RS[ri]); ri += 1
    return S + LS[li:] + RS[ri:]</pre>
<p>Merge is O(n) (two-finger; fronts are always the least remaining). Master method on merge_sort: T(n)=2T(n/2)+O(n) → case 2 → <strong>O(n log n)</strong>. Be able to <strong>trace</strong> splits and merges. Selection Sort O(n²) is obsolete — prefer Merge Sort or another O(n log n) sort.</p>

<p><span class="tag">[Slides]</span> <strong>Binary Search</strong> (third worked decrease-by-half example; also a pre-sorting / reduction preview): only recurse into one half → r=1, d=2, k=0 → case 2 → <strong>O(log n)</strong>.</p>
<pre>binary_search(L, s, e, q):
    n = e - s
    if n == 0: return None
    if n == 1: return s if L[s]==q else None
    half = s + (n / 2)
    if q == L[half]: return half
    if q &lt; L[half]: return binary_search(L, s, half, q)
    return binary_search(L, half + 1, e, q)</pre>

<!-- ==================== CH 9 ==================== -->
<h2>Chapter 9 — Randomization</h2>

<h3>9.1 The Big Idea</h3>
<p>Randomization = intentionally making random choices. Deterministic = no random behavior. Helps when (1) many alternatives, (2) most are good, (3) picking the best deterministically would be slow.</p>

<h3>9.2 Generating Random Numbers</h3>
<p><span class="tag">[Slides]</span> TRNG = physical entropy; PRNG = deterministic formula that looks random (default “random”).</p>
<table>
  <tr><th>Operation</th><th>Pseudocode</th><th>Time</th></tr>
  <tr><td>Random int in [min,max]</td><td><code>random_int(min, max)</code></td><td>O(1)</td></tr>
  <tr><td>Random element of L</td><td><code>random_choice(L)</code></td><td>O(1)</td></tr>
  <tr><td>Shuffle L</td><td><code>random_shuffle(L)</code></td><td>O(n)</td></tr>
</table>
<p><strong>Expected time:</strong> E[X] = weighted average of outcomes. “O(f(n)) expected” means E[runtime] ∈ O(f(n)). Preference: deterministic &gt; amortized &gt; expected. “Expected” is sticky: O(x) expected + O(y) det. = O(x+y) <em>expected</em>.</p>

<h3>9.4 The Las Vegas Pattern</h3>
<p>Las Vegas = always returns a <strong>correct</strong> answer; randomness only affects <strong>runtime</strong>. Randomized quick sort is Las Vegas: always sorts correctly; expected O(n log n), worst-case O(n²).</p>

<h3>9.5 Out-of-Place Quick Sort</h3>
<p>Divide by <strong>value</strong> (pivot/partition), not by index. Partition into less / equal / greater. Equal never needs sorting. Combine = concatenate (not merge).</p>
<pre>quick_sort(U):
    if n ≤ 1: return U
    pivot = random_choice(U)
    less    = [x for x in U if x &lt;  pivot]
    equal   = [x for x in U if x == pivot]
    greater = [x for x in U if x &gt;  pivot]
    return quick_sort(less) + equal + quick_sort(greater)</pre>
<p>Deterministic extreme pivots → T(n)=T(n−1)+O(n) → <strong>O(n²)</strong>. Random pivot → <strong>O(n log n) expected, O(n²) worst-case</strong>. Be able to <strong>trace by hand</strong>.</p>

<h3>9.6 In-Place Quick Sort</h3>
<p>Sort within index range [s,e) using swaps. Random pivot swapped to end; grow &lt; zone from left (i) and ≥ zone from right (j); final swap places pivot. Partition O(n). Same time as out-of-place: <strong>O(n log n) expected / O(n²) worst</strong>; better space.</p>
<table>
  <tr><th>Algorithm</th><th>Expected</th><th>Worst-case</th><th>In-place?</th></tr>
  <tr><td>Selection Sort</td><td>O(n²)</td><td>O(n²)</td><td>yes</td></tr>
  <tr><td>Merge Sort</td><td>O(n log n)</td><td>O(n log n)</td><td>no</td></tr>
  <tr><td>Quick Sort</td><td>O(n log n)</td><td>O(n²)</td><td>yes</td></tr>
</table>
<p>Never use O(n²) sorts. Default Quick Sort; use Merge Sort when worst-case O(n²) is unacceptable.</p>

<!-- ==================== CH 10 ==================== -->
<h2>Chapter 10 — Reduction</h2>

<h3>10.1 The Big Idea</h3>
<p><span class="tag">[Slides]</span> Design an algorithm that uses an off-the-shelf algorithm or data structure for the hard part. Template: preprocess → solve B → postprocess. If A reduces to B, A is easier than (or tied with) B. Informal analysis (after midterm): cite bottleneck big-O only.</p>

<h3>10.2 Reduction to Sorting</h3>
<p><strong>Median finding:</strong> sort, pick middle → O(n log n) expected.</p>
<p><span class="tag">[Slides]</span> <strong>Set intersection via sort:</strong> <code>quick_sort(L+R)</code>, then take adjacent duplicates → O(n log n) expected.</p>
<p><span class="tag">[Slides]</span> Min-and-max via sort: front/back of sorted list → O(n log n) expected (linear scan is faster in practice; this is a reduction example).</p>

<h3>10.3 Reduction to Hash Table Operations</h3>
<p><span class="tag">[Slides]</span> Map stores associations (key→value). Hashing: key → hash code → array index. Collisions inevitable (pigeonhole); chaining or open addressing. Critical ops: <strong>O(1) expected</strong>.</p>
<p>Pattern: find O(n) search/count bottleneck inside an O(n) loop → replace with hash ops → <strong>O(n²) → O(n) expected</strong>.</p>
<pre>set_intersect_hash(L, R):
    hm = HashMap()
    for r in R: hm[r] = True
    S = []
    for x in L:
        if x in hm: S.add(x)
    return S</pre>
<p>Mode average: count frequencies in a map, then find max → O(n) expected.</p>

<h3>10.4 Priority Search Queues; Prim–Jarník and Dijkstra</h3>
<p><span class="tag">[Slides]</span> PSQ: Insert O(1), RemoveMin O(log n) amortized, DecreasePriority O(1) amortized. Speeds Prim–Jarník (MST) and Dijkstra (NNSSSPP) to <strong>O(m + n log n)</strong> (without PSQ: O(mn)).</p>

<!-- ==================== CH 11 ==================== -->
<h2>Chapter 11 — Dynamic Programming</h2>

<h3>11.1 The Big Idea</h3>
<p><span class="tag">[Slides]</span> <strong>Tabulation:</strong> store instance solutions in a table. Base cases initialized immediately; general cases from other table cells; initialize all cells; answer lives in the table. Top-down = recursion/DBH; bottom-up = DP.</p>
<p>Design process: dimensions → <strong>table invariant</strong> → base → general → bottom-up draft.</p>
<pre>dynamic_programming_1D(input):
    A = array large enough
    Initialize base-case elements of A
    for i from smallest to largest general case:
        A[i] = initialize using A[&lt;i]
    return A[solution index]</pre>

<h3>11.2 1D DP and Fibonacci — O(n)</h3>
<p>F(0)=0, F(1)=1, F(n)=F(n−1)+F(n−2). Naïve recursion is exponential.</p>
<p><span class="tag">[Slides]</span> Invariant: <code>A[i] = F(i)</code>.</p>
<pre>fibonacci_dynamic_programming(n):
    A = [0] * (n + 1)
    A[1] = 1
    for i from 2 to n:
        A[i] = A[i-1] + A[i-2]
    return A[n]</pre>
<p><strong>O(n)</strong>. Be able to trace table A (demo: n=5 → output 5) and design similar 1D DP.</p>

<p class="struck">11.3 American Change Making — not on exam.</p>

<h3>Edit Distance — O(|s|×|t|) / O(n²)</h3>
<p><span class="tag">[Slides]</span> Min overwrite/insert/delete ops to transform start <code>s</code> into goal <code>t</code> (Levenshtein). 2D because you can shrink s or t.</p>
<p>Invariant: <code>A[i][j]</code> = edit distance between <code>s[:i]</code> and <code>t[:j]</code>.</p>
<p>Base: <code>A[0][j]=j</code> (j inserts); <code>A[i][0]=i</code> (i deletes).</p>
<pre>if s[i-1] == t[j-1]:
    A[i][j] = A[i-1][j-1]            # match
else:
    A[i][j] = min(1 + A[i-1][j],     # delete
                  1 + A[i][j-1],     # insert
                  1 + A[i-1][j-1])   # overwrite
# answer at A[s.size][t.size]</pre>
<p>Nested loops → <strong>O(|s|×|t|)</strong>. Trace demo: s="has", t="make" → distance 3.</p>

<!-- ==================== CH 12 ==================== -->
<h2>Chapter 12 — Lower Bounds</h2>

<h3>12.1 The Big Idea</h3>
<p><span class="tag">[Slides]</span> Act II: prove aspects of <em>problems</em>, not algorithms. Lower bound = “speed limit.” NP-complete ≈ only exp. exhaustive search seems to work. Undecidable = impossible.</p>

<h3>12.2 Notation and Terminology</h3>
<ul>
  <li><strong>Upper bound O</strong> for a problem: exhibit an algorithm (construction).</li>
  <li><strong>Lower bound Ω</strong>: every algorithm takes at least that long.</li>
  <li><strong>Tight bound Θ</strong>: upper and lower match → “solved science.”</li>
</ul>

<h3>12.3 Proving Negatives</h3>
<p>Proving a positive is easy (show an example). Proving “no algorithm is faster…” is hard — that is why lower-bound proofs feel different.</p>

<h3>12.4 Trivial Lower Bounds</h3>
<p><span class="tag">[Slides]</span> Strategy: any correct algorithm must create the output → time ≥ output size. Merge output has n elements ⇒ Ω(n). With merge’s O(n) algo ⇒ Merge is <strong>Θ(n)</strong>. Sorting trivial LB is only Ω(n) — leaves a gap under O(n log n).</p>

<h3>12.5 The Tight Bound for Sorting</h3>
<p><span class="tag">[Slides]</span> Comparison-based sorting: n! permutations; each comparison halves candidates; need log₂(n!)=Σ log₂ i comparisons; n terms that are Ω(log n) ⇒ <strong>Ω(n log n)</strong>. Merge sort gives O(n log n) upper bound ⇒ <strong>Θ(n log n)</strong> tight. No comparison sort can be asymptotically faster.</p>

<p class="struck">12.6 Reduction Arguments — not on exam.</p>

<!-- ==================== CH 13 ==================== -->
<h2>Chapter 13 — Easy and Impossible Problems</h2>

<h3>13.1 / 13.2 Efficiently-Solvable Problems and P</h3>
<p><span class="tag">[Slides]</span> Complexity class = set of problems. <strong>P</strong> = solvable in polynomial time = O(n^k) for some k≥0. Includes O(1), O(log n), O(n), O(n log n), O(n²), … Not poly: O(2^n), O(n!).</p>
<p>Prove X ∈ P: exhibit any poly-time algorithm (naïve OK) + analyze. Example: Pair Sum double loop O(n²) ⇒ ∈ P.</p>

<h3>13.3 Unsolvable Problems and Decidability</h3>
<p>Decidable = some algorithm solves it (any finite time). Undecidable = no algorithm exists. P ⊆ Decidable.</p>
<p><span class="tag">[Slides]</span> <strong>Halting Problem:</strong> input (proc, I); True iff proc(I)halts. Undecidable by contradiction: assume <code>halts</code> → <code>self_halts</code> → <code>contrary</code> → <code>contrary(contrary)</code> both cases contradict. Compilers cannot detect all infinite loops.</p>

<!-- ==================== CH 14 ==================== -->
<h2>Chapter 14 — NP-Hard / NP-Completeness</h2>

<h3>14.1 Verifiable Problems and NP</h3>
<p><span class="tag">[Slides]</span> <strong>NP</strong> = exhaustive search with a poly-time <em>verifier</em>. Solve = produce output; verify = check one candidate. Prove ∈ NP: define candidate + poly verifier. P ⊆ NP. Clique decision: candidate = vertex set C; check edges — poly ⇒ ∈ NP.</p>

<h3>14.2 Hard Problems and NP-Hardness</h3>
<p><span class="tag">[Slides]</span> E ≤ₚ H = poly-time reduction solving E via H (H harder or tied). H is <strong>NP-hard</strong> if ∀ E∈NP, E ≤ₚ H. <strong>NP-complete</strong> = ∈ NP and NP-hard (Goldilocks: not impossible + not easy).</p>

<h3>14.3 A First NP-Complete Problem</h3>
<p><span class="tag">[Slides]</span> <strong>Circuit Satisfaction (CSAT):</strong> input Boolean circuit C (DAG of AND/OR/NOT/OUT/vars); output satisfying assignment or None. Cook–Levin: CSAT is NP-complete. (1) ∈ NP: evaluate circuit on candidate assignment, O(n²). (2) NP-hard: compile any NP verifier into a circuit; solving CSAT recovers a solution for arbitrary E∈NP.</p>

<h3>14.4 Proving NP-Completeness by Reduction</h3>
<p>Once one NPC exists: pick known NPC E, reduce E→H with poly pre/post, show H∈NP. <strong>You will NOT prove an NPC reduction on the exam</strong> — know the idea and categorize problems.</p>
<p>Notable NPC: CSAT, SAT, Clique, Vertex Cover, TSP, Set Partition, many generalized games.</p>

<h3>14.5 P Versus NP Revisited</h3>
<p>Know P ⊆ NP; open whether P⊂NP or P=NP ($1M Clay). If any NPC is in P ⇒ P=NP (all NP get poly algos; crypto breaks). Conjecture/advice: live as if P⊂NP — treat NPC as impractical.</p>
<table>
  <tr><th>Class</th><th>Meaning</th><th>Example</th></tr>
  <tr><td>P</td><td>poly-time solvable</td><td>Sorting, Edit Distance, Fib, Pair Sum</td></tr>
  <tr><td>NP-complete</td><td>in NP + NP-hard</td><td>CSAT, SAT, Clique, Vertex Cover, TSP</td></tr>
  <tr><td>Undecidable</td><td>no algorithm exists</td><td>Halting Problem</td></tr>
</table>

<!-- ==================== PARALLEL ==================== -->
<h2>Parallel Algorithms</h2>

<h3>Overcoming Lower Bounds</h3>
<p><span class="tag">[Slides]</span> Sequential lower bounds still hold for total work, but parallel algorithms can reduce <em>user wait time</em> below the sequential bound.</p>

<h3>Analyzing Parallel Algorithms — p, Work, Span</h3>
<ul>
  <li><strong>p</strong> = number of processors</li>
  <li><strong>Work</strong> = total steps by all processors (ignore parallel; count as usual)</li>
  <li><strong>Span</strong> = elapsed time start→finish (take <strong>max</strong> of parallel branches)</li>
</ul>
<pre>in parallel:
    statement 1
    statement 2</pre>
<p>Goal: work matches lower bound; span beats it. Scalable: span O(X/p) for LB Ω(X). Embarrassingly parallel: span constant in n.</p>

<h3>Parallel Sorting — O(n log n) work, sublinear span</h3>
<p><strong>Parallel merge sort:</strong> recurse on halves in parallel. <span class="struck">Parallel merge itself is NOT on the exam</span>, but know overall: work <strong>O(n log n)</strong>, span <strong>O(log³ n)</strong>.</p>
<p><strong>Samplesort:</strong> oversample to pick p−1 splitters; bucket elements in parallel; recursively sort buckets; concatenate. Work <strong>O(n log n) expected</strong>; span <strong>O(log n) expected</strong>. Better span than parallel merge sort, but expected/randomized.</p>

<!-- ==================== QUICK REF ==================== -->
<h2>Quick-Reference Table of Efficiency Classes</h2>
<table>
  <tr><th>Topic</th><th>Time Complexity</th></tr>
  <tr><td>Merge Sort</td><td>Θ(n log n) / O(n log n)</td></tr>
  <tr><td>Binary Search</td><td>O(log n)</td></tr>
  <tr><td>Out-of-Place / In-Place Quick Sort</td><td>O(n log n) expected / O(n²) worst</td></tr>
  <tr><td>Reduction to Sorting (median, set ∩)</td><td>O(n log n)</td></tr>
  <tr><td>Hash table critical ops</td><td>O(1) expected</td></tr>
  <tr><td>Naive → hash-sped-up</td><td>O(n²) → O(n) expected</td></tr>
  <tr><td>Prim–Jarník / Dijkstra + PSQ</td><td>O(m + n log n)</td></tr>
  <tr><td>1D DP (Fibonacci)</td><td>O(n)</td></tr>
  <tr><td>Edit Distance (2D DP)</td><td>O(n²) / O(|s|×|t|)</td></tr>
  <tr><td>Comparison sorting lower bound</td><td>Ω(n log n), tight Θ(n log n)</td></tr>
  <tr><td>Parallel merge sort</td><td>work O(n log n), span O(log³ n)</td></tr>
  <tr><td>Samplesort</td><td>work O(n log n) exp, span O(log n) exp</td></tr>
</table>

<h2>Types of Exam Questions to Expect</h2>
<ul>
  <li>Define terminology in your own words</li>
  <li>Write a problem definition</li>
  <li>Perform a step count</li>
  <li>Prove an efficiency class (limits or properties of O)</li>
  <li>Analyze pseudocode (step count + efficiency proof together)</li>
  <li>Trace algorithm execution by hand, showing work</li>
  <li>Design algorithms using decrease-by-half, reduction, or DP patterns</li>
  <li>Justify / prove a lower bound</li>
  <li>Categorize a problem as P, NP-complete, or undecidable</li>
  <li>Prove a problem is in P or in NP</li>
</ul>
<p><strong>NOT required:</strong> proving an NP-complete reduction; the parallel merge step; American Change-Making; Reduction Arguments (12.6).</p>

<h2>Study Strategy</h2>
<ul>
  <li>Redo Problem Sets from Decrease-By-Half onward — exam questions mirror that style.</li>
  <li>For each algorithm practice: (1) hand trace, (2) recurrence/step count, (3) efficiency class with justification.</li>
  <li>Memorize the <strong>6-step Master Method</strong> cold. <span class="tag">[Slides]</span></li>
  <li>Practice the Ω(n log n) sorting lower bound proof (info-theoretic / decision-tree style).</li>
  <li>Explain in plain language: P vs NP vs NP-hard vs NP-complete vs undecidable.</li>
  <li><span class="tag">[Slides]</span> Hand-trace dbh_sum, merge_sort (+ merge), binary_search, quick sort, fib table, edit-distance grid.</li>
  <li>Compress essentials onto your <strong>one allowed page</strong> of notes (both sides OK); write your name on it.</li>
</ul>

</body></html>
"""

out_pdf = Path("/workspace/study-guide/CPSC335_Final_Exam_Study_Guide.pdf")
HTML(string=f"<style>{CSS}</style>{html}").write_pdf(out_pdf)
print(f"Wrote {out_pdf} ({out_pdf.stat().st_size} bytes)")
