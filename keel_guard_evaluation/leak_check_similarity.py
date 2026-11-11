import csv,json,sys
from collections import Counter
from pathlib import Path
import numpy as np
from aura_agent.pblock_engine.embeddings import MiniLMEmbedder
K=Path(sys.argv[1]); out=sys.argv[2]
E=np.load(K/"stores"/"keel_guard_embeddings.npy").astype(np.float32); E/=np.linalg.norm(E,axis=1,keepdims=True)+1e-9
meta=[json.loads(l) for l in open(K/"stores"/"keel_guard_meta.jsonl",encoding="utf-8")]
T=list(csv.DictReader(open(K/"evaluation"/"test_set.csv",encoding="utf-8")))
emb=MiniLMEmbedder()
rows=[]
for r in T:
    x=np.asarray(emb.embed([r["text"]])[0],dtype=np.float32).ravel(); x/=np.linalg.norm(x)+1e-9
    s=E@x; j=int(s.argmax())
    rows.append({**{k:r[k] for k in("id","truth","source")},"maxsim":round(float(s[j]),4),"store_framing":meta[j]["framing"][:60],"store_text":meta[j]["situation"][:120],"text":r["text"][:120]})
with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
for th in (0.99,0.95,0.90):
    c=Counter((r["source"],r["truth"]) for r in rows if r["maxsim"]>=th)
    print(th, sum(c.values()), dict(c))
print("framings of >=0.95 matches:",Counter(r["store_framing"].split(":")[0] for r in rows if r["maxsim"]>=0.95).most_common(8))
