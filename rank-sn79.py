import bittensor as bt

HOTKEY = "5FWNjwdsJ1bC3vLWRkeUgRf59Z9Z1JNGYMBokybPVBDJaYaa"
UID = 227

s = bt.Subtensor(network="finney")
mg = s.metagraph(79)
n = len(mg.uids)
rows = sorted(
    (
        float(mg.incentive[i]),
        float(mg.emission[i]),
        int(mg.uids[i]),
    )
    for i in range(n)
)
rows.reverse()
rank = next(i + 1 for i, r in enumerate(rows) if r[2] == UID)
mine = next(r for r in rows if r[2] == UID)
ix = next(i for i in range(n) if int(mg.uids[i]) == UID)
print("uid", UID)
print("incentive", f"{mine[0]:.12f}")
print("emission", f"{mine[1]:.12f}")
print("active", bool(mg.active[ix]))
print("last_update", int(mg.last_update[ix]))
print("block", s.block)
print("rank", rank)
print("n_uids", n)
print("nonzero", sum(1 for r in rows if r[0] > 0))
print("top1_uid", rows[0][2])
print("top1_inc", rows[0][0])
print("top1_emi", rows[0][1])
lo = max(0, rank - 3)
hi = min(n, rank + 2)
print(
    "nbs",
    ";".join(
        f"{j+1},{rows[j][2]},{rows[j][0]:.10f},{rows[j][1]:.6f}"
        for j in range(lo, hi)
    ),
)
