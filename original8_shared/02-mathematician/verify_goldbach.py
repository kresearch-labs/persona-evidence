#!/usr/bin/env python3
"""Goldbach strong-conjecture verification for every even n in [4, 100000].

Methods:
  A: full representation counts by double loop over prime pairs (sieve)
  B: per-n pull count by scanning p and testing n-p (sieve)  -- must match A
  C: existence with early exit, primality via deterministic Miller-Rabin
     (independent oracle; bases valid for n < 3.3e24)          -- must pass all
  D: exhaustive pair enumeration on a random sample of 1000 evens -- must match A
Negative controls:
  N1: sieve vs Miller-Rabin agreement on every integer in [0, 100000]
  N2: checker with prime 2 excluded must FAIL on n=4 (proves harness detects failure)
"""
import json, hashlib, random, sys

LIMIT = 100000

# ---------- sieve ----------
def build_sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    i = 2
    while i * i <= n:
        if s[i]:
            start = i * i
            s[start::i] = bytearray(len(range(start, n + 1, i)))
        i += 1
    return s

sieve = build_sieve(LIMIT)
primes = [i for i in range(2, LIMIT + 1) if sieve[i]]
pi_limit = len(primes)
print(f"[sieve] pi({LIMIT}) = {pi_limit}", flush=True)

# ---------- Miller-Rabin (deterministic for n < 3,317,044,064,679,887,385,961,981) ----------
def is_prime_mr(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        ok = False
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                ok = True
                break
        if not ok:
            return False
    return True

mr_prime = [is_prime_mr(i) for i in range(LIMIT + 1)]
mr_primes = [i for i in range(2, LIMIT + 1) if mr_prime[i]]
mr_set = set(mr_primes)
print(f"[mr]    pi({LIMIT}) = {len(mr_primes)}", flush=True)

# N1: oracle cross-check on every integer
mismatch_oracle = [i for i in range(LIMIT + 1) if bool(sieve[i]) != mr_prime[i]]
print(f"[N1]    sieve vs Miller-Rabin mismatches on [0,{LIMIT}]: {len(mismatch_oracle)}", flush=True)

# ---------- Method A: pair-push full counts ----------
reps = [0] * (LIMIT + 1)
for q in primes:
    for p in primes:
        s = p + q
        if s > LIMIT:
            break
        if p > q:
            break
        reps[s] += 1
print("[A]     pair-push counts done", flush=True)

# ---------- Method B: per-n pull counts (all evens) ----------
def count_pull(n):
    c = 0
    half = n // 2
    for p in primes:
        if p > half:
            break
        if sieve[n - p]:
            c += 1
    return c

evens = list(range(4, LIMIT + 1, 2))
num_evens = len(evens)
mismatch_pull = [n for n in evens if count_pull(n) != reps[n]]
print(f"[B]     pull vs push mismatches: {len(mismatch_pull)}", flush=True)

# ---------- Method C: Miller-Rabin existence, early exit ----------
def exists_mr(n):
    half = n // 2
    for p in mr_primes:
        if p > half:
            break
        if (n - p) in mr_set:
            return True
    return False

fail_mr = [n for n in evens if not exists_mr(n)]
print(f"[C]     Miller-Rabin existence failures: {len(fail_mr)}", flush=True)

# ---------- Method D: exhaustive enumeration on random sample ----------
rng = random.Random(20240602)
sample = rng.sample(evens, 1000)
sample_mismatch = [n for n in sample if count_pull(n) != reps[n]]
print(f"[D]     sample(1000) vs full-count mismatches: {len(sample_mismatch)}", flush=True)

# ---------- N2: negative control (exclude prime 2) ----------
def exists_no2(n):
    half = n // 2
    for p in mr_primes:
        if p == 2:
            continue
        if p > half:
            break
        if (n - p) in mr_set:
            return True
    return False

control_n4 = exists_no2(4)   # expect False (4 = 2+2 only)
control_n6 = exists_no2(6)   # expect True  (6 = 3+3)
print(f"[N2]    control exists_no2(4)={control_n4} (expect False), exists_no2(6)={control_n6} (expect True)", flush=True)

# ---------- stats ----------
fail_A = [n for n in evens if reps[n] < 1]
min_reps = min(reps[n] for n in evens)
argmins = [n for n in evens if reps[n] == min_reps]
max_reps = max(reps[n] for n in evens)
argmaxs = [n for n in evens if reps[n] == max_reps]
unique = sum(1 for n in evens if reps[n] == 1)
total_pairs = sum(reps[n] for n in evens)
mean_reps = total_pairs / num_evens

def pairs_of(n):
    out = []
    half = n // 2
    for p in primes:
        if p > half:
            break
        if sieve[n - p]:
            out.append((p, n - p))
    return out

rep_100000 = pairs_of(100000)[0]
small_knowns = {n: pairs_of(n) for n in (4, 6, 8, 10, 12, 98)}
argmin_pairs = {n: pairs_of(n) for n in argmins[:6]}

script_sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()

results = {
    "limit_inclusive": LIMIT,
    "evens_checked": num_evens,
    "first_even": evens[0],
    "last_even": evens[-1],
    "pi_100000_sieve": pi_limit,
    "pi_100000_millerrabin": len(mr_primes),
    "N1_oracle_mismatches": len(mismatch_oracle),
    "A_failures": len(fail_A),
    "B_pull_vs_push_mismatches": len(mismatch_pull),
    "C_millerrabin_existence_failures": len(fail_mr),
    "D_sample_mismatches": len(sample_mismatch),
    "N2_control_n4_excludes2": control_n4,
    "N2_control_n6_excl2": control_n6,
    "min_reps": min_reps,
    "argmin_reps": argmins,
    "argmin_pairs_sample": {str(k): v for k, v in argmin_pairs.items()},
    "max_reps": max_reps,
    "argmax_reps_first10": argmaxs[:10],
    "num_evens_with_exactly_1_rep": unique,
    "total_goldbach_pairs_counted": total_pairs,
    "mean_reps": round(mean_reps, 3),
    "rep_100000_first": rep_100000,
    "small_known_pairs": {str(k): v for k, v in small_knowns.items()},
    "script_sha256": script_sha,
}
with open("goldbach_results.json", "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
print("VERDICT:", "ALL PASS" if (not fail_A and not mismatch_pull and not fail_mr
      and not sample_mismatch and not mismatch_oracle
      and control_n4 is False and control_n6 is True) else "FAILURE", flush=True)
