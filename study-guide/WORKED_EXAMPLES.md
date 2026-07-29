# Worked Examples & Traces (practice these by hand)

These match the kinds of demos on the slides and the “trace by hand” exam prompts.

---

## 1. Merge Sort Trace

**Input:** `[2, 11, 1, 10]`

```
                    [2, 11, 1, 10]
                   /              \
              [2, 11]            [1, 10]
              /    \              /    \
           [2]    [11]         [1]    [10]
              \    /              \    /
           merge→[2,11]        merge→[1,10]
                   \              /
                merge→ [1, 2, 10, 11]
```

**Merge detail** for `[2,11]` and `[1,10]`:
- compare 2 vs 1 → take 1 → S=[1]
- compare 2 vs 10 → take 2 → S=[1,2]
- compare 11 vs 10 → take 10 → S=[1,2,10]
- leftover [11] → S=[1,2,10,11]

---

## 2. Out-of-Place Quick Sort Trace

**Input:** `[19, 9, 11, 5, 9, 2, 12]` — for practice, use **first element as pivot** each time (as exam demos often fix the random choice).

```
QS([19,9,11,5,9,2,12])  pivot=19
  less=[9,11,5,9,2,12]  equal=[19]  greater=[]
  QS([9,11,5,9,2,12])  pivot=9
    less=[5,2]  equal=[9,9]  greater=[11,12]
    QS([5,2]) pivot=5 → less=[2] equal=[5] greater=[] → [2,5]
    QS([11,12]) pivot=11 → less=[] equal=[11] greater=[12] → [11,12]
    combine → [2,5] + [9,9] + [11,12] = [2,5,9,9,11,12]
  combine → [2,5,9,9,11,12] + [19] + [] = [2,5,9,9,11,12,19]
```

---

## 3. In-Place Partition Trace

**Input range:** `[6, 7, 16, 4, 1]` with pivot chosen as front, then swapped to end (per slide demo style).

Suppose after moving pivot to end: list looks like `[1, 7, 16, 4, 6]` if pivot was 6…  
Walk the i/j pointers:
- Grow `<pivot` when `U[i] < pivot`
- Grow `≥pivot` when `U[j] ≥ pivot`
- Else swap `U[i], U[j]`
- Finally swap pivot into place between zones

**After partition guarantee:** everything left of p < pivot; everything right ≥ pivot.

---

## 4. Master Method Write-Up (exam style)

**Claim:** `merge_sort` takes O(n log n) time.

1. **t = 2** (general case when n ≥ 2)  
2. **Base (n < 2):** T(n) = O(1)  
3. **General:** T(n) = 2T(n/2) + 2n + 2  ∀ n ≥ 2  
4. **Parts:** r=2≥1 ✓, d=2>1 ✓, t=2≥1 ✓, c(n)∈O(n) so k=1≥0 ✓  
5. **r ≟ dᵏ:** 2 ≟ 2¹ → **equal → Case 2** → O(nᵏ log n)  
6. **Simplify:** O(n¹ log n) = **O(n log n)**. QED

---

## 5. Fibonacci DP Hand Trace (slide demo: n = 5)

Invariant: A[i] = F(i)

| i | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| A[i] | 0 | 1 | 1 | 2 | 3 | 5 |

**Output: A[5] = 5.** Time O(n).

---

## 6. Edit Distance Hand Trace (slide demo: s="has", t="make")

Invariant: A[i][j] = distance between s[:i] and t[:j].  
Ops: match → copy diagonal; else min(1+delete, 1+insert, 1+overwrite).

|     | ε | m | a | k | e |
|-----|---|---|---|---|---|
| ε   | 0 | 1 | 2 | 3 | 4 |
| h   | 1 | 1 | 2 | 3 | 4 |
| a   | 2 | 2 | 1 | 2 | 3 |
| s   | 3 | 3 | 2 | 2 | **3** |

**Output: A[3][4] = 3.** Time O(|s|×|t|)=O(n²).

---

## 7. Hash Reduction (Set Intersection)

**L=[5,19,1,3], R=[12,5,3,8]**

Naïve: for each x in L, scan R → O(n²).

Hash:
1. Insert R → map {12,5,3,8}  
2. Scan L: 5∈map ✓, 19✗, 1✗, 3✓ → output **[5,3]**  
O(n) expected.

---

## 8. Prove Pair Sum ∈ P (template)

```
naïve_pair_sum(L,k):
  for x in L:
    for y in L:
      if x+y==k: return (x,y)
  return None
```
O(n²) polynomial ⇒ **Pair Sum ∈ P**. QED

---

## 9. Prove Clique ∈ NP (template)

Candidate: vertex set C.  
Verifier: check |C|=k; for all pairs in C, edge exists.  
O(n³) (or better) polynomial ⇒ **Clique ∈ NP**. QED

---

## 10. Sorting Lower Bound (short form)

n! permutations. Each comparison halves candidates. Need log₂(n!) comparisons.  
log₂(n!)=Σᵢ log₂ i has n terms Ω(log n) each ⇒ **Ω(n log n)**.  
Applies to every comparison-based sort. + merge sort O(n log n) ⇒ **Θ(n log n)** tight.

---

## 11. Parallel work vs span (2-proc sum)

```
in parallel:
  l = sum_range(0, mid)   # n/2
  r = sum_range(mid, n)   # n/2
return l+r
```
- Work ≈ (n/2)+(n/2) = **Θ(n)** (matches Ω(n) LB)  
- Span ≈ **n/2** (faster user wait)  

That is how parallel “bypasses” a sequential lower bound without contradicting it.
