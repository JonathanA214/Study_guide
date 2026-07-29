# CPSC 335 Final — One-Page Notes (print BOTH sides) — Write your NAME on this sheet

## SIDE A — Algorithms & Design Patterns

### Master Method (decrease-by-half)
T(n)=r·T(n/d)+c(n) ∀n≥t; T(n)∈O(1) ∀n<t; c(n)∈O(nᵏ); r,t≥1; d>1; k≥0.
Compare **r ≟ dᵏ**: (1) r<dᵏ → O(nᵏ) | (2) r=dᵏ → O(nᵏ log n) | (3) r>dᵏ → O(n^{log_d r})
Steps: t → base → general count → ID r,d,t,k → case → conclude.
Merge sort: 2T(n/2)+O(n) → case2 → **O(n log n)**. Binary search: T(n/2)+O(1) → **O(log n)**.

### Merge Sort
`if n≤1: return U; half=n/2; return merge(MS(left),MS(right))`
merge: two-finger scan; leftovers append → **O(n)**. Trace: show every split + merge.

### Quick Sort (Las Vegas: always correct; random runtime)
**Out-of-place:** `pivot=random_choice(U); L/E/G lists; return QS(L)+E+QS(G)`  
**In-place:** partition zones < | todo | ≥ | pivot@end; final swap; recurse both sides.
**O(n log n) expected, O(n²) worst.** Extreme pivots ⇒ T(n)=T(n−1)+O(n). Prefer QS; if expected bad → Merge Sort; never O(n²) sorts.

### Reduction
**To algorithm:** preprocess → solve B → postprocess. A reduces to B ⇒ A easier/tied.
**To sorting:** sort then scan → usually **O(n log n) exp.** Median: sort, pick mid. Set∩: sort(L+R), take adjacent dupes.
**To hash:** naïve O(n²) bottleneck (search/count in loop) → HashMap O(1) exp → **O(n) expected**.
Set∩: put R in map; scan L. Mode: count_map then max.

### Hash / PSQ
Hash ops critical: **O(1) expected** (collisions + chaining; pigeonhole ⇒ collisions inevitable).
PSQ: Insert O(1), RemoveMin O(log n) amort., DecreasePriority O(1) amort.
Prim–Jarník & Dijkstra + PSQ: **O(m + n log n)** (else O(mn)).

### Dynamic Programming (tabulation; bottom-up)
Design: dimensions → **table invariant** → base → general → fill table.
**Fib (1D):** A[i]=F(i); A[0]=0,A[1]=1; A[i]=A[i−1]+A[i−2] → **O(n)**.
**Edit distance (2D):** A[i][j]=dist(s[:i],t[:j]). Base A[i][0]=i, A[0][j]=j.
If s[i−1]==t[j−1]: A[i−1][j−1]; else min(1+del A[i−1][j], 1+ins A[i][j−1], 1+ow A[i−1][j−1]).
Return A[|s|][|t|] → **O(|s|×|t|)=O(n²)**. Trace grids (ex: has→make).
~~American Change Making NOT ON EXAM~~

### Parallel (Act III)
**p**=#processors. **Work**=total steps (ignore parallel). **Span**=elapsed (max of parallel).
Goal: work respects lower bound; span beats it. Embarrassingly parallel: span const in n.
Parallel merge sort: work **O(n log n)**, span **O(log³ n)**. ~~parallel merge NOT on exam~~
Samplesort: p−1 splitters (oversample), bucket in parallel, recurse; work **O(n log n) exp**, span **O(log n) exp**.

---

## SIDE B — Limits, Classes, Proof Templates

### Complexity cheat table
| | MergeSort | QuickSort | Hash | Fib DP | EditDist | Prim/Dijk+PSQ | Par.MS | Samplesort |
|---|---|---|---|---|---|---|---|---|
| Time | O(n log n) | O(n log n) exp / O(n²) wc | O(1) exp | O(n) | O(n²) | O(m+n log n) | work O(n log n) span O(log³ n) | same work; span O(log n) exp |

### Lower bounds (Ch 12)
**Upper** (problem): exhibit algorithm. **Lower Ω**: EVERY algorithm ≥ that. **Tight Θ**: match ⇒ solved science.
**Trivial LB:** must create output of size f(n) ⇒ Ω(f(n)). Merge: Ω(n)+O(n)=**Θ(n)**.
**Sorting:** trivial Ω(n) leaves gap. Info-theoretic: n! perms; each cmp halves; need log₂(n!)=Σ log i ∈ **Ω(n log n)** for comparison-based. + merge sort O ⇒ **Θ(n log n)** tight. ~~12.6 reduction LB proofs NOT ON EXAM~~

### P / NP / Undecidable (Ch 13–14)
**P** = poly-time solvable (O(nᵏ); includes n log n). **NP** = poly-time **verifiable** (exhaustive + poly verifier). **NP-complete** = in NP + NP-hard. **Undecidable** = no algorithm exists.
P ⊆ NP ⊆ Decidable; Undecidable outside. **P=NP?** open. If one NPC in P ⇒ all NP in P.
**Halting:** input (proc,I); True iff halts. Undecidable: assume halts → self_halts → contrary → contrary(contrary) contradiction.

### Proof templates (copy onto exam answers)
**∈ P:** “Algorithm ___ solves X in O(___) poly time. QED.”
**∈ NP:** “Candidate = ___. Verifier: ___. Takes O(___) poly time ⇒ X∈NP. QED.”
**Trivial LB:** “Any algo must create output of size ___ ⇒ Ω(___).”
**Sorting Ω(n log n):** “n! perms; cmp halves candidates; log₂(n!)∈Ω(n log n); applies to all comparison sorts.”
**Halting:** “Suppose halts exists; build contrary; contrary(contrary) both cases contradict; no such algo.”

### Design / categorize tips
Decrease-by-half: base n≤1 (avoid ∞ recursion); divide; recurse both; combine; Master Method.
Reduction: ask “does sorting or a hash map do the hard part?”
DP: define E(i)/E(i,j); recurrence; base; fill bottom-up; read answer.
Categorize: poly algo exists? → **P**. Only verify fast / NPC famous? → **NP-complete**. Literally impossible? → **undecidable** (Halting).
Will NOT ask: NP-complete reduction proofs. Bring **CWID**. Name on notes.
