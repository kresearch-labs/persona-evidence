# goldbach.awk — strong Goldbach verifier for all even n in [4, N], N=1,000,000
# Algorithm: sieve of Eratosthenes (odds only) + ascending-prime scan for first
# representation n = p + q, p <= q. Emits one witness line "n p q" per even n.
# Usage: awk -v N=1000000 -v WIT=artifacts/goldbach_witnesses.txt -f goldbach.awk
BEGIN {
  if (N == "") N = 1000000
  if (WIT == "") WIT = "artifacts/goldbach_witnesses.txt"
  # --- sieve: C[int(m/2)]=1  <=>  odd m (3<=m<=N) is composite ---
  for (i = 3; i * i <= N; i += 2) {
    if (!C[int(i / 2)]) {
      for (j = i * i; j <= N; j += 2 * i) C[int(j / 2)] = 1
    }
  }
  # --- dense prime list of ALL primes <= N (for pi(N) self-check + scan) ---
  np = 1; P[1] = 2
  for (m = 3; m <= N; m += 2) if (!C[int(m / 2)]) P[++np] = m
  piN = np
  # pi(N/2): primes available as summand p <= n/2
  piHalf = 0
  for (k = 1; k <= np && P[k] <= int(N / 2); k++) piHalf++
  largest = P[np]
  # --- main scan ---
  cnt = 0
  for (n = 4; n <= N; n += 2) {
    if (n == 4) { print "4 2 2" > WIT; cnt++; continue }
    half = int(n / 2)
    found = 0
    for (k = 2; k <= np; k++) {        # k=1 is p=2; n-2 even>2 => composite, skip
      p = P[k]
      if (p > half) break
      if (!C[int((n - p) / 2)]) { print n, p, n - p > WIT; found = 1; break }
    }
    if (!found) { printf "COUNTEREXAMPLE %d\n", n > "/dev/stderr"; bad++; exit 2 }
    cnt++
  }
  close(WIT)
  printf "RESULT OK even_n_checked=%d range=[4,%d] pi(%d)=%d pi(%d)=%d largest_prime<=%d\n", cnt, N, N, piN, int(N / 2), piHalf, largest
}
