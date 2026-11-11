# goldbach_random.awk — randomized re-verification with fresh witnesses.
# Correct odds-only sieve (start i=3). Writes witnesses directly to OUT.
# Usage: awk -v N=1000000 -v R=2000 -v SEED=20261015 -v OUT=artifacts/goldbach_random_witnesses.txt -f goldbach_random.awk
BEGIN {
  if (N == "") N = 1000000
  if (R == "") R = 2000
  if (SEED == "") SEED = 20261015
  srand(SEED)
  for (i = 3; i * i <= N; i += 2)
    if (!C[int(i / 2)]) for (j = i * i; j <= N; j += 2 * i) C[int(j / 2)] = 1
  ok = 0; bad = 0
  for (t = 0; t < R; t++) {
    n = 4 + 2 * int(rand() * ((N - 4) / 2 + 1))
    if (n == 4) { print "4 2 2" > OUT; ok++; continue }
    found = 0
    for (p = 3; p <= int(n / 2); p += 2)
      if (!C[int(p / 2)] && !C[int((n - p) / 2)]) { print n, p, n - p > OUT; found = 1; break }
    if (found) ok++; else { bad++; printf "MISS %d\n", n > OUT }
  }
  close(OUT)
  printf "RANDOM CHECK seed=%d R=%d ok=%d bad=%d\n", SEED, R, ok, bad
}
