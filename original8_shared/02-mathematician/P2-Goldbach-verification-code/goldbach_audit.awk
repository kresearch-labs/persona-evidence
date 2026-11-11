# goldbach_audit.awk — independent cross-check, different algorithm & data path.
# Differences vs goldbach.awk:
#   * full boolean sieve (not odds-only), trial-division-free
#   * DESCENDING scan from the largest prime <= n/2 (opposite direction)
#   * reads the witness file from run 1 and RE-VERIFIES each witness line
#     (n even, p<=q, p+q=n, p and q prime) using its own sieve
#   * recomputes the count of even n and compares to witness-line count
# Usage: awk -v N=1000000 -v WIT=artifacts/goldbach_witnesses.txt -f goldbach_audit.awk
BEGIN {
  if (N == "") N = 1000000
  # --- full sieve: S[m]=1 <=> m prime, 0<=m<=N ---
  for (m = 2; m <= N; m++) S[m] = 1
  for (m = 2; m * m <= N; m++) if (S[m]) for (j = m * m; j <= N; j += m) S[j] = 0
  # --- re-verify every witness line from run 1 ---
  wlines = 0; wbad = 0
  while ((getline line < WIT) > 0) {
    wlines++
    split(line, a, " ")
    n = a[1] + 0; p = a[2] + 0; q = a[3] + 0
    if (n % 2 != 0 || n < 4 || n > N) { wbad++; if (wbad <= 5) print "BADLINE", line }
    else if (p + q != n) { wbad++; if (wbad <= 5) print "BADSUM", line }
    else if (p > q) { wbad++; if (wbad <= 5) print "BADORDER", line }
    else if (!S[p] || !S[q]) { wbad++; if (wbad <= 5) print "BADPRIME", line }
  }
  close(WIT)
  # --- independent descending re-scan of all even n ---
  miss = 0; cnt = 0
  for (n = 4; n <= N; n += 2) {
    cnt++
    found = 0
    for (p = int(n / 2); p >= 2; p--) {
      if (S[p] && S[n - p]) { found = 1; break }
    }
    if (!found) { print "AUDIT-COUNTEREXAMPLE", n; miss++ }
  }
  printf "AUDIT RESULT witness_lines=%d witness_bad=%d even_n=%d misses=%d\n", wlines, wbad, cnt, miss
  if (wlines != cnt) printf "AUDIT MISMATCH witness_lines(%d) != even_n(%d)\n", wlines, cnt
  if (wbad == 0 && miss == 0 && wlines == cnt) print "AUDIT VERDICT: PASS"
  else print "AUDIT VERDICT: FAIL"
}
