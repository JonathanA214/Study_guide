#!/usr/bin/env python3
"""Final Exam Study Guide — written in the user's Enhanced style for Ch 8–14 + Parallel."""

from pathlib import Path
from weasyprint import HTML

CSS = r"""
@page {
  size: A4;
  margin: 14mm 14mm 16mm 14mm;
  @bottom-center {
    content: "Final Exam Study Guide — page " counter(page);
    font-family: "DejaVu Sans", sans-serif;
    font-size: 7.5pt;
    color: #666;
  }
}
body {
  font-family: "DejaVu Sans", Arial, sans-serif;
  font-size: 8pt;
  line-height: 1.28;
  color: #1a1a1a;
}
h1 {
  font-size: 15pt;
  font-weight: bold;
  margin: 0 0 0.35em;
  padding-bottom: 0.2em;
  border-bottom: 2.5px solid #7A1F3D;
  color: #1a1a1a;
}
.toc {
  background: #f6f6f8;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.4em 0.65em 0.45em;
  margin: 0.45em 0 0.65em;
}
.toc .label { font-weight: bold; color: #7A1F3D; font-size: 8pt; }
.toc ul { margin: 0.2em 0 0 1.05em; padding: 0; }
.toc li { margin: 0.02em 0; }
h2.main {
  font-size: 10.5pt;
  color: #7A1F3D;
  margin: 0.55em 0 0.15em;
}
.meta {
  font-size: 7.5pt;
  font-style: italic;
  color: #444;
  margin: 0 0 0.45em;
}
.slides-note {
  background: #FAF5F6;
  border-left: 3px solid #7A1F3D;
  padding: 0.3em 0.5em;
  margin: 0 0 0.55em;
  font-size: 7.5pt;
}
.tag { color: #7A1F3D; font-weight: bold; }
h2.ch {
  font-size: 11.5pt;
  color: #7A1F3D;
  margin: 0.75em 0 0.2em;
  page-break-after: avoid;
}
h3 {
  font-size: 9pt;
  color: #7A1F3D;
  margin: 0.5em 0 0.12em;
  page-break-after: avoid;
}
p { margin: 0.15em 0 0.28em; }
ul, ol { margin: 0.12em 0 0.35em 1.15em; padding: 0; }
li { margin: 0.06em 0; }
strong { font-weight: bold; }
em { font-style: italic; }
code {
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 7pt;
  background: #eeeeee;
  padding: 0 0.15em;
  border-radius: 2px;
}
pre {
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 7pt;
  background: #f7f7f9;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0.35em 0.5em;
  margin: 0.25em 0 0.4em;
  white-space: pre-wrap;
  line-height: 1.22;
  page-break-inside: avoid;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.3em 0 0.45em;
  font-size: 7.2pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.16em 0.32em;
  text-align: left;
  vertical-align: top;
}
th { background: #f0e6ea; color: #7A1F3D; font-weight: bold; }
.struck { text-decoration: line-through; color: #888; }
hr.soft { border: none; border-top: 1px solid #ddd; margin: 0.55em 0; }
"""

BODY = r"""
<h1>Final Exam Study Guide</h1>

<div class="toc">
  <div class="label">Contents</div>
  <ul>
    <li>Chapter 8 — Decrease-by-Half (Divide and Conquer)</li>
    <li>Chapter 9 — Randomization</li>
    <li>Chapter 10 — Reduction</li>
    <li>Chapter 11 — Dynamic Programming</li>
    <li>Chapter 12 — Lower Bounds</li>
    <li>Chapter 13 — Easy and Impossible Problems</li>
    <li>Chapter 14 — NP-Hard Problems</li>
    <li>Parallel Algorithms</li>
    <li>Quick-Reference Table of Efficiency Classes</li>
    <li>Types of Exam Questions to Expect</li>
    <li>Study Strategy</li>
  </ul>
</div>

<h2 class="main">Final Exam Study Guide — Chapters 8–14 + Parallel Algorithms</h2>
<p class="meta">110-minute limit · one page of notes allowed · non-cumulative (covers Ch 8–14 only) · bring your CWID</p>

<div class="slides-note">
  Additions from the lecture slides are marked <span class="tag">[Slides]</span>.
  Struck-through topics are <strong>not on the exam</strong>: American Change Making; Ch.&nbsp;12.6 Reduction Arguments; the parallel merge step itself.
  You will <strong>not</strong> be asked to prove an NP-complete reduction.
</div>

<!-- ============================================================ -->
<h2 class="ch">Chapter 8 — Decrease-by-Half (Divide and Conquer)</h2>

<h3>8.1 The Big Idea</h3>
<p>Solve a problem by reducing it to a smaller instance of the same problem, then combining the sub-solution(s) into a full solution.</p>
<p>Decrease-by-half specifically shrinks the input by a <strong>constant fraction</strong> each step (not just by 1, as in decrease-by-one patterns like insertion sort).</p>

<p><span class="tag">[Slides]</span> General template (the pattern every decrease-by-half algorithm follows):</p>
<pre>decrease_by_half(INPUT):
    if INPUT is base case:
        return base case solution
    left_input, right_input = divide INPUT in half
    left_solution  = decrease_by_half(left_input)
    right_solution = decrease_by_half(right_input)
    entire_solution = combine left_solution with right_solution
    return entire_solution</pre>
<p>Three phases every time: <strong>Divide → Recursion → Combine</strong>.</p>

<p><span class="tag">[Slides]</span> Formal definition of algorithm (Def. 6): a process that, given a problem instance, produces a solution, and is (1) clear enough to implement, (2) correct (always produces a correct solution), and (3) terminates (finite time). Decrease-by-half algorithms must satisfy termination explicitly — see pitfall below.</p>

<p><span class="tag">[Slides]</span> <strong>Pitfall — infinite recursion:</strong> base cases and the combine phase must work together so recursion always bottoms out for every <code>n</code>. Best practice: design so the general-case threshold is <code>t = 2</code>, i.e. base cases explicitly handle <code>n = 0</code> and <code>n = 1</code>, general case handles <code>n ≥ 2</code>. Missing the <code>n = 1</code> base case (only handling <code>n = 0</code>) causes infinite recursion — e.g. <code>dbh_sum([7])</code> splits into <code>dbh_sum([])</code> and <code>dbh_sum([7])</code> forever, since <code>half = 1/2 = 0</code> gives an empty left and an unchanged right.</p>

<h3>8.2 Example: Summation</h3>
<p>Classic warm-up: split the array in half, recursively sum each half, add the results. Base case: array of size 0 or 1 returns immediately.</p>
<p><span class="tag">[Slides]</span> Final pseudocode:</p>
<pre>dbh_sum(L):
    n = len(L)
    if n == 0:
        return 0
    if n == 1:
        return L[0]
    half = n / 2
    left  = L[:half]
    right = L[half:]
    return dbh_sum(left) + dbh_sum(right)</pre>
<p><span class="tag">[Slides]</span> Dividing a list in half (Python slice notation): <code>half = n / 2</code> (integer truncation), <code>left = L[:half]</code>, <code>right = L[half:]</code> — each costs <code>n/2</code> steps to copy.</p>
<p><span class="tag">[Slides]</span> Step-count / variable-initialization counting pattern: primitive types = 1 step; a list with <code>k</code> elements = <code>k</code> steps to build.</p>
<p><span class="tag">[Slides]</span> Reality check: <code>dbh_sum</code> costs <strong>O(n log n)</strong> by the master method (below), while the naïve iterative sum (<code>total = 0; for x in L: total += x</code>) costs only <strong>O(n)</strong> and is simpler/easier to analyze. Lesson: decrease-by-half isn’t automatically the best choice — compare against the naïve algorithm before assuming divide-and-conquer wins.</p>

<h3>8.3 Analyzing Decrease-by-Fraction Algorithms — Master Method</h3>
<p>General recurrence form: <code>T(n) = a·T(n/b) + f(n)</code></p>
<ul>
  <li><code>a</code> = number of subproblems</li>
  <li><code>n/b</code> = size of each subproblem (input shrinks by factor <code>b</code>)</li>
  <li><code>f(n)</code> = work done outside the recursive calls (combining step)</li>
</ul>
<p>Compare <code>f(n)</code> to <code>n^(log_b a)</code>:</p>
<ol>
  <li>If <code>f(n) = O(n^(log_b a − ε))</code> → <code>T(n) = Θ(n^(log_b a))</code> (recursive work dominates)</li>
  <li>If <code>f(n) = Θ(n^(log_b a) · log^k n)</code> → <code>T(n) = Θ(n^(log_b a) · log^(k+1) n)</code> (balanced — usually k=0)</li>
  <li>If <code>f(n) = Ω(n^(log_b a + ε))</code> (and regularity holds) → <code>T(n) = Θ(f(n))</code> (combining work dominates)</li>
</ol>
<p>Be prepared to prove the efficiency class using the master method — show the case, compute <code>log_b a</code>, compare growth rates.</p>

<p><span class="tag">[Slides]</span> Formal “master-form recurrence” definition — the precise shape the master theorem requires:</p>
<pre>T(n) = r · T(n/d) + c(n)     ∀ n ≥ t
T(n) ∈ O(1)                  ∀ n &lt; t
where c(n) ∈ O(n^k); r, d, t, k ∈ O(1); r, t ≥ 1; d &gt; 1; k ≥ 0.</pre>
<table>
  <tr><th>Symbol</th><th>Meaning</th><th>Constraint</th></tr>
  <tr><td><code>r</code></td><td>number of recursive calls</td><td>r ≥ 1</td></tr>
  <tr><td><code>d</code></td><td>divisor of input size</td><td>d &gt; 1</td></tr>
  <tr><td><code>t</code></td><td>threshold for the general case</td><td>t ≥ 1</td></tr>
  <tr><td><code>k</code></td><td>exponent in the non-recursive work c(n)</td><td>k ≥ 0</td></tr>
</table>

<p><span class="tag">[Slides]</span> The Master Theorem (equivalent framing, stated directly in r, d, k):</p>
<ul>
  <li>If <code>r &lt; d^k</code> → <code>T(n) ∈ O(n^k)</code> (case 1)</li>
  <li>If <code>r = d^k</code> → <code>T(n) ∈ O(n^k log n)</code> (case 2)</li>
  <li>If <code>r &gt; d^k</code> → <code>T(n) ∈ O(n^(log_d r))</code> (case 3)</li>
</ul>

<p><span class="tag">[Slides]</span> The Master Method — <strong>6-step recipe</strong> to analyze any decrease-by-half algorithm (memorize this order for the exam):</p>
<ol>
  <li>Identify the general-case threshold <code>t</code> from the base-case pseudocode (best practice: <code>t = 2</code>).</li>
  <li>Analyze the base case (assume <code>n &lt; t</code>): step-count it, state <code>T(n) ∈ O(1) ∀ n &lt; t</code>.</li>
  <li>Step-count the general case (assume <code>n ≥ t</code>): count steps outside recursive calls, derive the master-form recurrence <code>T(n) = r·T(n/d) + c(n) ∀ n ≥ t</code>.</li>
  <li>Identify and check the master-form parts: pull out <code>c(n)</code>, <code>r</code>, <code>d</code>, <code>t</code>, <code>k</code>; verify all constraints hold.</li>
  <li>Compare <code>r</code> vs <code>d^k</code> to identify which of the 3 cases applies.</li>
  <li>Simplify and state the conclusion in plain <code>O(...)</code> form (e.g. <code>O(n^k log n)</code> with k=1 simplifies to <code>O(n log n)</code>).</li>
</ol>

<p><span class="tag">[Slides]</span> Worked example — <code>dbh_sum</code>:</p>
<ul>
  <li><code>t = 2</code>; base case <code>T(n) = 4 ∈ O(1) ∀ n &lt; 2</code></li>
  <li>General case: <code>T(n) = 2·T(n/2) + n + 4 ∀ n ≥ 2</code></li>
  <li>Parts: <code>c(n) = n + 4 ∈ O(n) → k = 1</code>; <code>r = 2</code>; <code>d = 2</code>; <code>t = 2</code> — all constraints check out.</li>
  <li>Compare: <code>r ? d^k → 2 ? 2^1 → 2 = 2 → case 2</code>.</li>
  <li>Conclusion: <code>T(n) ∈ O(n^1 log n) = O(n log n)</code>. <code>dbh_sum</code> takes <strong>O(n log n)</strong> time.</li>
</ul>

<h3>8.4 Merge Sort</h3>
<p>Recursively split array in half, sort each half, merge the two sorted halves.</p>
<p>Recurrence: <code>T(n) = 2T(n/2) + Θ(n)</code> → Case 2 of master method → <strong>Θ(n log n)</strong>.</p>
<p>Be able to <strong>trace it by hand</strong> on a small array (show the split tree and the merge steps). Know how to design similar divide-and-conquer algorithms and analyze them the same way.</p>

<p><span class="tag">[Slides]</span> History (context, likely not tested but good grounding): discovered by John von Neumann in 1945; practical in the 1950s–70s for sorting data on tape drives; historically important because it was faster than O(n²) but slower than O(n), disproving the early assumption that all time complexities are polynomial.</p>

<p><span class="tag">[Slides]</span> The Sorting Problem (formal definition): input: a list U of comparable elements; output: a list S containing the elements of U in non-decreasing order.</p>

<p><span class="tag">[Slides]</span> Key insight — lists of size ≤ 1 are trivially sorted: the empty list <code>[]</code> and any single-element list <code>[a]</code> vacuously satisfy “non-decreasing order,” so the base case is simply <code>if n ≤ 1: return U</code>.</p>

<p><span class="tag">[Slides]</span> Full pseudocode (with merge factored out as its own sub-algorithm):</p>
<pre>merge_sort(U):
    if n ≤ 1:
        return U
    half = n / 2
    left  = U[:half]
    right = U[half:]
    return merge(merge_sort(left), merge_sort(right))</pre>

<p><span class="tag">[Slides]</span> The Merge sub-problem: input two lists LS and RS, each already in non-decreasing order; output a list S containing all elements of LS and RS in non-decreasing order.</p>
<pre>merge(LS, RS):
    S = []
    li = 0   # index of next candidate in LS
    ri = 0   # index of next candidate in RS
    while li &lt; len(LS) and ri &lt; len(RS):
        if LS[li] &lt;= RS[ri]:
            S.add_back(LS[li]); li += 1
        else:
            S.add_back(RS[ri]); ri += 1
    return S + LS[li:] + RS[ri:]   # append any leftover elements</pre>
<p>Key insight enabling O(n): because LS and RS are each already sorted, the least remaining element in each list is always at its current front index — no need to search. Step count: <code>3 + 5n + n = 6n + 3 ∈ O(n)</code>. merge takes <strong>O(n)</strong> time.</p>

<p><span class="tag">[Slides]</span> Master method analysis of merge_sort: <code>t = 2</code>; base <code>T(n) = 2 ∈ O(1) ∀ n &lt; 2</code>; general <code>T(n) = 2·T(n/2) + 2n + 2 ∀ n ≥ 2</code>; parts r=2, d=2, k=1 → case 2 → <strong>O(n log n)</strong>.</p>
<p><span class="tag">[Slides]</span> Selection Sort vs Merge Sort: Selection Sort is O(n²); Merge Sort is O(n log n) and strictly better — Selection Sort is considered obsolete. Always prefer Merge Sort (or another O(n log n) sort).</p>

<p><span class="tag">[Slides]</span> <strong>Binary Search</strong> (third worked decrease-by-half example — know it). Preview of Reduction / pre-sorting: sort first, then search faster. Key insight: since L is sorted, compare q to the middle and recurse into <em>only one</em> half (r = 1).</p>
<pre>binary_search(L, s, e, q):
    n = e - s
    if n == 0: return None
    if n == 1: return s if L[s] == q else None
    half = s + (n / 2)
    if q == L[half]: return half
    if q &lt; L[half]: return binary_search(L, s, half, q)
    return binary_search(L, half + 1, e, q)</pre>
<p>Master method: r=1, d=2, k=0 → case 2 → <strong>O(log n)</strong>. Fastest efficiency class covered outside O(1) — good benchmark, and a good example of r = 1.</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 9 — Randomization</h2>

<h3>9.1 The Big Idea</h3>
<p>Randomization = intentionally designing an algorithm to make random choices. Deterministic algorithm = no random behavior (everything before this chapter). Randomized algorithm = does behave randomly.</p>
<p>Randomization helps when: (1) there are many alternatives, (2) most are good, (3) selecting the best one deterministically would be slow. (Analogy: picking a lunch place downtown — don’t waste time finding the optimal one, just pick a reasonable one at random.)</p>

<h3>9.2 Generating Random Numbers</h3>
<p><span class="tag">[Slides]</span> TRNG (True Random Number Generator): uses a physical entropy source — genuinely unpredictable. PRNG (Pseudo-Random Number Generator): uses a deterministic equation to produce random-seeming values — not philosophically random, but adequate outside cybersecurity. By default, “random” = PRNG.</p>
<table>
  <tr><th>Operation</th><th>Pseudocode</th><th>Time</th></tr>
  <tr><td>Random integer in [min, max]</td><td><code>random_int(min, max)</code></td><td>O(1)</td></tr>
  <tr><td>Random element of list L</td><td><code>random_choice(L)</code></td><td>O(1)</td></tr>
  <tr><td>Randomly shuffle list L</td><td><code>random_shuffle(L)</code></td><td>O(n)</td></tr>
</table>

<p><strong>Expected Time</strong> — Three “flavors” of efficiency class: deterministic (always applies, the default — “O(n) time” means deterministic), amortized (uneven due to lazy operations, but fast in total over a series), expected (unpredictable due to randomization, fast on average).</p>
<ul>
  <li>Expected value: for random variable X with outcomes x₁…xₖ having probabilities p₁…pₖ: E[X] = x₁p₁ + … + xₖpₖ.</li>
  <li>X ∈ O(f(n)) expected means E[X] ∈ O(f(n)) — averaged over all random outcomes, the time is O(f(n)).</li>
  <li>Preference ranking: O(1) deterministic (best, suitable for real-time) &gt; O(1) amortized &gt; O(1) expected (good, but slowdown is entirely unpredictable).</li>
  <li>Combining rule (be able to apply this): the “expected” flavor is sticky.
    <ul>
      <li>O(x) expected + O(y) deterministic = O(x + y) expected</li>
      <li>O(x) expected × n = O(xn) expected</li>
    </ul>
  </li>
</ul>

<h3>9.4 The Las Vegas Pattern</h3>
<p>A Las Vegas algorithm always returns a <strong>correct</strong> answer; randomness only affects <strong>runtime</strong> (may be slow with small probability). Randomized quick sort is the course’s main Las Vegas example: always sorts correctly; expected O(n log n), worst-case O(n²).</p>

<h3>9.5 Out-of-Place Quick Sort</h3>
<p>Divide-by-value, not by-index: unlike merge sort (which splits by position), quick sort’s divide phase moves each element into a sub-list based on its value relative to a chosen pivot.</p>
<p><strong>Pivot:</strong> an input element chosen as the boundary value. <strong>Partition:</strong> split the unsorted list into less (&lt; pivot), equal (== pivot, includes duplicates), greater (&gt; pivot) — partitioning does not sort, just divides.</p>
<p>Key insight: the equal sub-list never needs sorting (all elements tied = trivially non-decreasing).</p>
<p>Combine phase is just concatenation (not a merge!): since every element in less &lt; every element in equal &lt; every element in greater by construction, the answer is simply <code>quick_sort(less) + equal + quick_sort(greater)</code>.</p>
<pre>quick_sort(U):
    if n ≤ 1:
        return U
    pivot = random_choice(U)
    less    = [x for x in U if x &lt; pivot]
    equal   = [x for x in U if x == pivot]
    greater = [x for x in U if x &gt; pivot]
    return quick_sort(less) + equal + quick_sort(greater)</pre>
<p>Be able to <strong>run it by hand</strong> — trace every sub-list created and the result of each combine phase.</p>
<p>Deterministic pivot choice (e.g., always <code>U[0]</code>) gives <strong>O(n²)</strong> time — shown by recurrence <code>T(n) = T(n-1) + 4n + 2</code> when the pivot is always the min/max (not master-theorem form; solved by expansion/summation).</p>
<p>Randomized pivot choice fixes this: only 2 of n elements are “extreme” choices, so the probability every pivot across the whole recursion is extreme is astronomically small. So for practical purposes quick sort behaves like O(n log n), but the precise worst-case bound is still O(n²).</p>
<p><strong>Claim to know cold:</strong> randomized out-of-place quick sort takes <strong>O(n log n) expected time, and O(n²) worst-case time</strong>.</p>

<h3>9.6 In-Place Quick Sort</h3>
<p>Motivation: avoid allocating new less/equal/greater lists — sort within a range of indices <code>[s, e)</code> of the original array using swaps only (no copying).</p>
<p>In-Place Partition problem: given list U and range <code>[s, e)</code>, rearrange elements and return pivot index p such that every element in <code>U[s:p] &lt; U[p]</code>, and every element in <code>U[p+1:e] ≥ U[p]</code>.</p>
<p>Mechanism: swap a random pivot to the end (index e−1); maintain a “certified less” zone growing from the left (pointer i) and a “certified ≥” zone growing from the right (pointer j), with a shrinking “todo” zone in between:</p>
<ul>
  <li>If <code>U[i] &lt; pivot</code>: leave it, advance i.</li>
  <li>Else if <code>U[j] ≥ pivot</code>: leave it, retreat j.</li>
  <li>Else: swap <code>U[i]</code> and <code>U[j]</code>, advance i and retreat j.</li>
</ul>
<p>When <code>i &gt; j</code>, swap the pivot (at e−1) into position i — that’s the final pivot index p. <code>in_place_partition</code> runs in <strong>O(n)</strong> time.</p>
<p>Be able to <strong>run it by hand</strong> — trace the partition (zones/swaps) and the full sort (finished zones of every partition phase).</p>
<p>Same efficiency class as out-of-place: <strong>O(n log n) expected, O(n²) worst-case</strong> — the only difference is space (in-place uses O(1) extra space vs out-of-place’s O(n)).</p>

<p><strong>Comparing Sorting Algorithms</strong></p>
<table>
  <tr><th>Sorting Algorithm</th><th>Expected Time</th><th>Worst-Case Time</th><th>In-Place?</th></tr>
  <tr><td>Selection Sort</td><td>O(n²)</td><td>O(n²)</td><td>yes</td></tr>
  <tr><td>Merge Sort</td><td>O(n log n)</td><td>O(n log n)</td><td>no</td></tr>
  <tr><td>Quick Sort</td><td>O(n log n)</td><td>O(n²)</td><td>yes</td></tr>
</table>
<p>Selection Sort (and other O(n²) sorts: insertion, bubble) is strictly dominated — never use them. Merge Sort and Quick Sort are tied for fastest on average. Merge Sort’s advantage: guaranteed O(n log n) worst-case. Quick Sort’s advantage: in-place.</p>
<p>Best practice: default to Quick Sort; use Merge Sort instead when the O(n²) worst-case of Quick Sort is unacceptable (e.g., real-time / safety-critical systems).</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 10 — Reduction</h2>

<h3>10.1 The Big Idea</h3>
<p>Solve problem A by transforming (reducing) it to a problem B you already know how to solve, then use B’s solution/algorithm to solve A. Total cost = cost of the reduction/transformation + cost of solving B.</p>
<p><span class="tag">[Slides]</span> Two variants: reduction to an algorithm, and reduction to a data structure. Template for reduction to an algorithm:</p>
<pre>reduction_pattern(input_to_problem_A):
    input_to_problem_B = pre-process input_to_problem_A
    solution_to_problem_B = solve_B(input_to_problem_B)
    solution_to_problem_A = post-process solution_to_problem_B
    return solution_to_problem_A</pre>
<p>If A reduces to B, then A is easier than B (or tied). Binary search’s setup (pre-sorting) is a preview of this pattern. <span class="tag">[Slides]</span> Informal analysis (after midterm): evidence limited to big-O of bottleneck steps — omit full step counts when obvious.</p>

<h3>10.2 Reduction to Sorting</h3>
<p><strong>Median finding:</strong> sort the array, return the middle element(s). Cost dominated by sort → <strong>O(n log n)</strong>.</p>
<p><span class="tag">[Slides]</span> <strong>Set intersection:</strong> concatenate L+R, sort, then take elements that appear two-in-a-row (common elements appear twice) → <strong>O(n log n) expected</strong>.</p>
<pre>set_intersect_sort(L, R):
    sorted = quick_sort(L + R)
    output = []
    for i from 0 to len(sorted) - 2:
        if sorted[i] == sorted[i + 1]:
            output.add(sorted[i])
    return output</pre>
<p><span class="tag">[Slides]</span> Min-and-max by sorting: sort, return (first, last) → O(n log n) expected. (A linear scan is faster in practice; this is a reduction example.)</p>

<h3>10.3 Reduction to Hash Table Operations</h3>
<p><span class="tag">[Slides]</span> Know the big picture: a map stores associations (key → value). Hashing converts a key into an array index; collisions are inevitable (pigeonhole principle) and handled by chaining or open addressing.</p>
<p>Core operations (insert, delete, lookup) take <strong>O(1) expected time</strong>.</p>
<p>Reduction pattern: naïve algorithms that are O(n²) (e.g., nested search/count) can be sped up to <strong>O(n) expected</strong> by replacing the bottleneck O(n) search with O(1) expected hash-table ops.</p>
<p><span class="tag">[Slides]</span> Recipe: (1) write naïve, (2) identify bottleneck loop, (3) pre-populate a hash table and replace the slow lookup.</p>
<pre>set_intersect_hash(L, R):
    hm = HashMap()
    for r in R: hm[r] = True
    S = []
    for x in L:
        if x in hm: S.add(x)
    return S</pre>
<p>Mode average the same way: map each element to its count, then scan for the max → O(n) expected.</p>

<h3>10.4 Priority Search Queues; Prim–Jarník and Dijkstra</h3>
<p><span class="tag">[Slides]</span> A Priority Search Queue (PSQ) is a priority queue that also supports decreasing a key’s priority. With Fibonacci-heap-style bounds from the slides: Insert O(1), RemoveMin O(log n) amortized, DecreasePriority O(1) amortized.</p>
<p>Revisit Prim–Jarník (MST) and Dijkstra (non-negative single-source shortest paths) as applications of PSQs over graphs. Both run in <strong>O(m + n log n)</strong> with a suitable PSQ (without it: O(mn)).</p>
<p>Correspondence idea: Prim keys = edges (priority = weight if bridge, else ∞); Dijkstra keys = vertices (priority = known distance, else ∞). The sequential “find min bridge / closest unseen” search is replaced by RemoveMin / DecreasePriority.</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 11 — Dynamic Programming</h2>

<h3>11.1 The Big Idea</h3>
<p>Break a problem into overlapping subproblems, solve each subproblem once, store (tabulate) the result, and reuse it — avoids the exponential blow-up of naïve recursion. Requires optimal substructure + overlapping subproblems.</p>
<p><span class="tag">[Slides]</span> <strong>Tabulation:</strong> store solutions to problem instances in a table. Base cases initialized immediately; general cases initialized from other table elements; algorithm initializes all table elements; finally the solution is contained in the table.</p>
<p><span class="tag">[Slides]</span> Top-down thinking = recursion / decrease-by-half (break large into small). Bottom-up thinking = dynamic programming (combine small into large).</p>
<p><span class="tag">[Slides]</span> Design process: dimensions (1D/2D/…) → table invariant → base-case pseudocode → general-case pseudocode → complete bottom-up draft.</p>
<pre>dynamic_programming_1D(input):
    A = array that is large enough to avoid out-of-bounds bugs
    Initialize base-case elements of A
    for i from smallest general case to largest general case:
        A[i] = initialize A[i] using elements A[&lt;i]
    return A[solution index]</pre>

<h3>11.2 1D Dynamic Programming and Fibonacci Numbers</h3>
<p>Build a table F[0..n] bottom-up instead of recomputing recursively. Runs in <strong>O(n)</strong> time. Be able to run it by hand (fill in the table). Be able to design similar 1D DP algorithms: identify the recurrence, base case(s), fill order, and where the answer lives in the table.</p>
<p><span class="tag">[Slides]</span> Fibonacci Number Problem: input integer n ≥ 0; output F(n). F(0)=0, F(1)=1, F(n)=F(n−1)+F(n−2) for n≥2. First ten: 0,1,1,2,3,5,8,13,21,34.</p>
<p><span class="tag">[Slides]</span> Naïve recursion calls itself twice on n−1 and n−2 → exponential time — extremely slow.</p>
<p><span class="tag">[Slides]</span> Table invariant: <code>A[i] = the i-th Fibonacci number = F(i)</code>.</p>
<pre>fibonacci_dynamic_programming(n):
    A = [0] * (n + 1)
    A[1] = 1
    for i from 2 to n:
        A[i] = A[i-1] + A[i-2]
    return A[n]</pre>
<p>Analysis: initializing A takes O(n); the for loop takes O(n) → <strong>O(n)</strong> total. Huge speedup versus the exponential recursive algorithm. Slide demo: trace for n = 5 (show table A; output 5).</p>

<p class="struck">11.3 American Change-Making — not on exam (struck through).</p>

<h3>Edit Distance</h3>
<p>2D DP table where D[i][j] = min number of insertions/deletions/substitutions (overwrites) to convert a prefix of length i of string A into a prefix of length j of string B. Runs in <strong>O(n²)</strong> time (table has ~n×m cells, O(1) work per cell). Be able to run it by hand (fill the grid, trace the recurrence) and design similar 2D DP algorithms.</p>
<p><span class="tag">[Slides]</span> Formal problem: input start string s and goal string t; output the edit distance between s and t. Levenshtein operations: overwrite, insert, delete. Example: “dikestra” → “dijkstra” needs insert “j” + delete “e” → distance 2.</p>
<p><span class="tag">[Slides]</span> Dimensions: two ways to shrink the input (shrink s, shrink t) → 2D table. Invariant: <code>A[i][j] = edit distance between s[:i] and t[:j]</code>.</p>
<p>Base cases: <code>A[0][j] = j</code> (j inserts from empty string); <code>A[i][0] = i</code> (i deletes to empty string).</p>
<pre>if s[i-1] == t[j-1]:
    A[i][j] = A[i-1][j-1]            # match — no action
else:
    A[i][j] = min(1 + A[i-1][j],     # delete
                  1 + A[i][j-1],     # insert
                  1 + A[i-1][j-1])   # overwrite
# answer at A[s.size][t.size]</pre>
<p><span class="tag">[Slides]</span> Conclusion: edit_distance takes <strong>O(|s| × |t|)</strong> time. Slide demo: trace for s=“has”, t=“make” (show full table A; output 3).</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 12 — Lower Bounds</h2>

<h3>12.1 The Big Idea</h3>
<p>A lower bound tells you the best possible efficiency class any algorithm could achieve for a problem — it’s a statement about the <em>problem</em>, not a specific algorithm.</p>
<p><span class="tag">[Slides]</span> Act I designed algorithms. Act II studies limits: lower bounds (“speed limit”), NP-complete (apparently only exp. exhaustive search), undecidable (literally impossible).</p>

<h3>12.2 Notation and Terminology</h3>
<ul>
  <li><strong>Lower bound Ω</strong> — algorithm/problem takes at least this long.</li>
  <li><strong>Upper bound O</strong> — algorithm takes at most this long (for a problem: established by exhibiting an algorithm).</li>
  <li><strong>Tight bound Θ</strong> — matching upper and lower bounds (know it exactly) → algorithm design for this problem is “done / solved science.”</li>
</ul>
<p>Know precisely what it means for a <em>problem</em> (not algorithm) to have a lower bound.</p>

<h3>12.3 Proving Negatives</h3>
<p>Proving a positive is straightforward (show a receipt / an example). Proving a negative is difficult — “prove you never bought Funyuns” / “prove no algorithm is faster than…”. That is why lower-bound proofs feel different from Act I analyses.</p>

<h3>12.4 Trivial Lower Bounds</h3>
<p><span class="tag">[Slides]</span> Strategy: every correct algorithm must create the output object(s). Analyze the space complexity Ω(f(n)) of the problem output, then conclude the problem has lower bound Ω(f(n)).</p>
<p>Merge example: output list has n elements ⇒ Merge has lower bound <strong>Ω(n)</strong>. Combined with the O(n) merge algorithm ⇒ Merge has tight bound <strong>Θ(n)</strong>.</p>
<p>Sorting’s trivial lower bound is only Ω(n) — that leaves a gap under the O(n log n) upper bound from merge sort.</p>

<h3>12.5 The Tight Bound for Sorting</h3>
<p>Comparison-based sorting has a lower bound of <strong>Ω(n log n)</strong>, proven via an information-theoretic / decision-tree style argument: n! possible orderings; a binary comparison halves the candidate permutations; need depth ≥ log₂(n!) = Θ(n log n) to distinguish all outcomes.</p>
<p><span class="tag">[Slides]</span> Sketch to write on the exam: (1) n distinct elements ⇒ n! permutations; (2) each comparison of a vs b eliminates about half the remaining permutations; (3) need log₂(n!) comparisons; (4) log₂(n!) = Σᵢ log₂ i has n terms that are Ω(log n) each ⇒ log₂(n!) ∈ Ω(n log n); (5) therefore every comparison-based sorting algorithm takes Ω(n log n) time.</p>
<p>Combined with merge sort’s O(n log n) upper bound → comparison sorting is <strong>Θ(n log n)</strong> — tight bound. Solved science; no possibility of a faster efficiency class for comparison-based sorting.</p>

<p class="struck">12.6 Reduction Arguments — not on exam (struck through).</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 13 — Easy and Impossible Problems</h2>

<h3>13.1 The Big Idea</h3>
<p>Problems can be classified by how hard they are to solve algorithmically — from efficiently solvable, to hard-but-solvable, to not solvable by any algorithm at all.</p>

<h3>13.2 Efficiently-Solvable Problems and P</h3>
<p><strong>P</strong> = class of problems solvable in polynomial time (worst-case), i.e., O(n^k) for some constant k. “Efficient” is generally equated with “polynomial time” in this context.</p>
<p><span class="tag">[Slides]</span> Polynomial time includes O(1), O(log n), O(n), O(n log n), O(n²), O(n³). Not polynomial: O(2^n), O(n!). (Lemmas: log n ∈ O(n) and n log n ∈ O(n²), so log factors still count as polynomial.)</p>
<p><span class="tag">[Slides]</span> Prove X ∈ P (template): design any poly-time algorithm (naïve is fine) → analyze → conclude X ∈ P. Example: Pair Sum double loop is O(n²) ⇒ Pair Sum ∈ P.</p>

<h3>13.3 Unsolvable Problems and Decidability</h3>
<p>Undecidable problems exist — no algorithm can solve them for all inputs, no matter how much time is allowed.</p>
<p>The Halting Problem: no algorithm can determine, for an arbitrary program and input, whether that program will halt or run forever. Classic proof by contradiction/diagonalization.</p>
<p><span class="tag">[Slides]</span> Formal: decidable = some algorithm solves it (any finite time); undecidable = no such algorithm. P ⊆ Decidable.</p>
<p><span class="tag">[Slides]</span> Halting proof sketch: suppose <code>halts(proc, I)</code> exists → build <code>self_halts(proc) = halts(proc, proc)</code> → build <code>contrary(proc)</code> that loops forever if self_halts says True, else returns → evaluate <code>contrary(contrary)</code> → both cases contradict → <code>halts</code> cannot exist. Implication: compilers cannot detect all infinite loops.</p>

<!-- ============================================================ -->
<h2 class="ch">Chapter 14 — NP-Hard Problems</h2>

<h3>14.1 Verifiable Problems and NP</h3>
<p><strong>NP</strong> = class of problems where a proposed solution (“certificate” / candidate) can be verified in polynomial time, even if finding the solution might take longer. Note: P ⊆ NP (anything solvable in poly time is also poly-time verifiable).</p>
<p><span class="tag">[Slides]</span> Course definition: NP = problems with an exhaustive algorithm whose <em>verifier part</em> runs in polynomial time. Solve = transform input into output; verify = decide whether one candidate is valid.</p>
<p><span class="tag">[Slides]</span> Prove X ∈ NP: define a candidate → design the verifier → prove poly time → conclude ∈ NP. Example: Clique decision — candidate is a vertex set C; verifier checks |C|=k and every pair has an edge — polynomial ⇒ Clique ∈ NP.</p>

<h3>14.2 Hard Problems and NP-Hardness</h3>
<p>A problem is <strong>NP-hard</strong> if every problem in NP can be reduced to it in polynomial time — i.e., it’s at least as hard as the hardest problems in NP. A problem that is both NP-hard and in NP is <strong>NP-complete</strong>.</p>
<p><span class="tag">[Slides]</span> Goldilocks: ∈ NP (not impossible) + NP-hard (not easy) = “hard.” Formal: E ≤ₚ H means a reduction solves E by calling a solver for H with poly-time pre/post-processing (H harder than E, or tied). H is NP-hard if ∀ E ∈ NP, E ≤ₚ H.</p>

<h3>14.3 A First NP-Complete Problem</h3>
<p>Know the canonical first NP-complete problem (Circuit-SAT / SAT) and why establishing one NP-complete problem lets others be shown NP-complete by reduction from it.</p>
<p><span class="tag">[Slides]</span> Circuit Satisfaction (CSAT): input a Boolean circuit C (DAG of AND/OR/NOT/OUT/variables); output a satisfying assignment A, or None. Cook–Levin Theorem: CSAT is NP-complete. (1) ∈ NP: candidate = assignment; verifier evaluates the circuit — O(n²). (2) NP-hard: for any E ∈ NP, compile verify_E into a Boolean circuit (standard model: each CPU/pseudocode step → circuit layers); solving CSAT recovers a solution for E; pre/post-processing is polynomial.</p>

<h3>14.4 Proving NP-Completeness by Reduction</h3>
<p>General method: show the problem is in NP (verifiable in poly time) + reduce a known NP-complete problem to it in poly time.</p>
<p><strong>You will NOT be asked to prove an NP-complete reduction on the exam</strong> — but you should understand what the technique means conceptually, and be able to categorize problems as P / NP-complete / undecidable.</p>
<p><span class="tag">[Slides]</span> Notable NP-complete problems: CSAT, SAT, Clique, Vertex Cover, TSP, Set Partition, and many generalized games (Chess, Go, Sudoku, Mario, …). Commonalities: in NP (verify fast); hard (exhaustive search / exponential seems necessary; too slow in practice); but useful if solved.</p>

<h3>14.5 P versus NP Revisited</h3>
<p>The open question: does P = NP? Know what’s at stake (if P = NP, every efficiently verifiable problem would be efficiently solvable) and that it remains unproven either way.</p>
<p><span class="tag">[Slides]</span> We know P ⊆ NP. Open: P ⊂ NP or P = NP? ($1M Clay prize.) If you find a poly-time algorithm for one NP-complete problem ⇒ P = NP (all NP get fast algorithms via reduction; crypto breaks). Conjecture/advice from the slides: live as if P ⊂ NP — treat NP-complete problems as impractical; treat cryptography as secure.</p>

<!-- ============================================================ -->
<h2 class="ch">Parallel Algorithms</h2>

<h3>Overcoming Lower Bounds</h3>
<p>Sequential lower bounds (like Ω(n log n) for comparison sorting) apply to a single processor. With multiple processors working simultaneously, wall-clock time can be reduced below the sequential lower bound, even though total work doesn’t decrease.</p>
<p><span class="tag">[Slides]</span> Act III: sidestep limits. A tight sequential lower bound cannot be broken — but a parallel algorithm can make user wait time smaller while work still respects the bound.</p>

<h3>Analyzing Parallel Algorithms — Processors, Work, Span</h3>
<ul>
  <li><strong>p</strong> = number of processors.</li>
  <li><strong>Work</strong> = total number of operations across all processors (same as sequential time complexity if run on 1 processor). Analyze work by ignoring parallelism and counting steps as usual.</li>
  <li><strong>Span</strong> = length of the longest chain of dependent operations / elapsed time start→finish (the critical path) — take the <strong>maximum</strong> of parallel branches; sequential steps count as usual.</li>
</ul>
<pre>in parallel:
    statement 1
    statement 2
    ...
    statement k</pre>
<p>Goal: work matches the lower bound; span beats it. Scalable: span O(X / p) for a problem with lower bound Ω(X).</p>

<h3>Embarrassingly Parallel Problems</h3>
<p>Problems where subproblems are fully independent (no communication/coordination needed) — trivially easy to parallelize. <span class="tag">[Slides]</span> Formal: a problem is embarrassingly parallel when there is a scalable parallel algorithm with span that is constant with respect to n (e.g., p-processor summation with p = n).</p>

<h3>Parallel Sorting — O(n log n) Work, Sublinear Span</h3>
<p>A parallel sorting algorithm can achieve the same total work as sequential sorting, O(n log n), while reducing the span to something sublinear in n (e.g., polylogarithmic) by exploiting parallel merge/partition steps.</p>

<h3>Parallel Merge Sort</h3>
<p>Parallelize the recursive split-and-sort structure of merge sort across processors.</p>
<p>The parallel merge step itself will <strong>NOT</strong> be on the exam — but the overall parallel merge sort structure/idea is fair game. <span class="tag">[Slides]</span> With parallel merge: work <strong>O(n log n)</strong>, span <strong>O(log³ n)</strong>. First draft (parallel recurse, sequential merge) has span O(n) — merge is the bottleneck.</p>

<h3>Samplesort</h3>
<p>A parallel-friendly generalization of quicksort: pick multiple “splitter” samples to partition the data into p buckets in parallel, sort each bucket independently (in parallel), then concatenate — avoids the single-pivot bottleneck of standard quicksort when parallelizing.</p>
<p><span class="tag">[Slides]</span> Oversampling: randomly select p·k finalists, sort them, take every k-th as a splitter (prevents entirely worst-case splitters). Then in parallel, binary-search each element into a bucket and recurse. Work <strong>O(n log n) expected</strong>; span <strong>O(log n) expected</strong>. Trade-off vs parallel merge sort: better span, but expected/randomized (merge sort is deterministic).</p>

<!-- ============================================================ -->
<h2 class="ch">Quick-Reference Table of Efficiency Classes</h2>
<table>
  <tr><th>Topic</th><th>Time Complexity</th></tr>
  <tr><td>Merge Sort</td><td>Θ(n log n) / O(n log n)</td></tr>
  <tr><td>Binary Search <span class="tag">[Slides]</span></td><td>O(log n)</td></tr>
  <tr><td>Out-of-Place Quick Sort</td><td>O(n log n) expected / O(n²) worst</td></tr>
  <tr><td>In-Place Quick Sort</td><td>O(n log n) expected / O(n²) worst</td></tr>
  <tr><td>Reduction to Sorting (median, set intersection)</td><td>O(n log n)</td></tr>
  <tr><td>Hash table operations</td><td>O(1) expected</td></tr>
  <tr><td>Naive → hash-table-sped-up algorithms</td><td>O(n²) → O(n) expected</td></tr>
  <tr><td>Prim–Jarník / Dijkstra (priority search queue)</td><td>O(m + n log n)</td></tr>
  <tr><td>1D DP (Fibonacci)</td><td>O(n)</td></tr>
  <tr><td>Edit Distance (2D DP)</td><td>O(n²) / O(|s|×|t|)</td></tr>
  <tr><td>Comparison-based sorting lower bound</td><td>Ω(n log n), tight Θ(n log n)</td></tr>
  <tr><td>P</td><td>Polynomial time solvable</td></tr>
  <tr><td>NP</td><td>Polynomial time verifiable</td></tr>
  <tr><td>Parallel merge sort</td><td>O(n log n) work, O(log³ n) span</td></tr>
  <tr><td>Samplesort</td><td>O(n log n) work expected, O(log n) span expected</td></tr>
</table>

<h2 class="ch">Types of Exam Questions to Expect</h2>
<ul>
  <li>Define terminology in your own words</li>
  <li>Write a problem definition</li>
  <li>Perform a step count</li>
  <li>Prove an efficiency class (limits or properties of O)</li>
  <li>Analyze pseudocode (step count + efficiency class proof together)</li>
  <li>Trace algorithm execution by hand, showing work</li>
  <li>Design algorithms using decrease-by-half, reduction, or DP patterns</li>
  <li>Justify / prove a lower bound</li>
  <li>Categorize a problem as P, NP-complete, or undecidable</li>
  <li>Prove a problem is in P or in NP</li>
</ul>
<p><strong>NOT required:</strong> proving an NP-complete reduction; the parallel merge step; American Change-Making; Reduction Arguments (12.6).</p>

<h2 class="ch">Study Strategy</h2>
<ul>
  <li>Redo Problem Set questions from “Decrease-By-Half” onward — exam questions mirror their style.</li>
  <li>For each algorithm, practice: (1) tracing it by hand on a small example, (2) writing its recurrence or step count, (3) stating its efficiency class with justification.</li>
  <li>Memorize the <strong>6-step Master Method</strong> process cold (threshold → base case → general case → identify r,d,t,k → compare r vs d^k → simplify) — it’s the fastest way to justify divide-and-conquer efficiency classes under time pressure. <span class="tag">[Slides]</span></li>
  <li>Practice the Ω(n log n) sorting lower bound proof (information-theoretic / decision-tree argument) — a favorite “prove a lower bound” question.</li>
  <li>Be able to explain, in plain language, the difference between P, NP, NP-hard, NP-complete, and undecidable — a likely short-answer topic.</li>
  <li><span class="tag">[Slides]</span> Be comfortable hand-tracing the canonical examples end-to-end: <code>dbh_sum</code>, <code>merge_sort</code> (with merge factored out), <code>binary_search</code>, out-of-place and in-place quick sort, Fibonacci table, and an edit-distance grid — a “design/analyze a similar algorithm” question will likely resemble one of these.</li>
  <li>Compress essentials onto your <strong>one allowed page</strong> of notes (both sides OK). Write your name on the notes if you want them returned. Bring your <strong>CWID</strong>.</li>
</ul>
"""

out = Path("/workspace/study-guide/CPSC335_Final_Exam_Study_Guide.pdf")
HTML(string=f"<html><head><meta charset='utf-8'/><style>{CSS}</style></head><body>{BODY}</body></html>").write_pdf(out)
print(f"Wrote {out} ({out.stat().st_size} bytes)")
