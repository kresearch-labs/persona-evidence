// goldbach.c — verify strong Goldbach for all even n in [4, 1e6]
// Method: sieve of Eratosthenes (odds-only bitset), then for each even n
// scan p = 3,5,7,... up to n/2 and test primality of n-p via sieve.
// Compile: gcc -O2 -o goldbach goldbach.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define LIMIT 1000000

static uint8_t *is_comp; // is_comp[i]=1 => i composite; index by odd number m -> (m>>1)

static inline int is_prime(uint32_t m) {
    if (m < 2) return 0;
    if (m == 2) return 1;
    if (!(m & 1)) return 0;
    return !is_comp[m >> 1];
}

int main(void) {
    // sieve odds up to LIMIT: is_comp bit for odd m>=3 at index m>>1
    size_t sz = (LIMIT >> 1) + 1;
    is_comp = calloc(sz, 1);
    if (!is_comp) { fprintf(stderr, "alloc fail\n"); return 1; }
    for (uint32_t i = 3; (uint64_t)i * i <= LIMIT; i += 2) {
        if (!is_comp[i >> 1]) {
            for (uint64_t j = (uint64_t)i * i; j <= LIMIT; j += 2u * i)
                is_comp[j >> 1] = 1;
        }
    }

    FILE *f = fopen("artifacts/goldbach_witnesses.txt", "w");
    if (!f) { fprintf(stderr, "open witnesses fail\n"); return 1; }

    uint64_t checked = 0;
    uint32_t max_primes_needed = 0;
    clock_t t0 = clock();
    for (uint32_t n = 4; n <= LIMIT; n += 2) {
        int found = 0;
        if (is_prime(n - 2)) { // p=2 case
            fprintf(f, "%u 2 %u\n", n, n - 2);
            found = 1;
            checked++;
            continue;
        }
        for (uint32_t p = 3; p <= n / 2; p += 2) {
            if (is_prime(p) && is_prime(n - p)) {
                fprintf(f, "%u %u %u\n", n, p, n - p);
                found = 1;
                break;
            }
        }
        if (!found) {
            printf("COUNTEREXAMPLE: %u\n", n);
            fclose(f);
            return 2;
        }
        checked++;
    }
    clock_t t1 = clock();
    double secs = (double)(t1 - t0) / CLOCKS_PER_SEC;
    printf("OK: verified all %llu even n in [4, %d]\n", (unsigned long long)checked, LIMIT);
    printf("time: %.3f s\n", secs);
    fclose(f);
    return 0;
}
