from input import fresh, available

fresh = sorted(fresh, key=lambda x: x[0])
coalesced_fresh = []
for f in fresh:
    if len(coalesced_fresh) == 0:
        coalesced_fresh.append(f)
        continue
    last_new = coalesced_fresh[len(coalesced_fresh)-1]
    if f[0] <= last_new[1]:
        coalesced_fresh[len(coalesced_fresh)-1] = (last_new[0], max(f[1], last_new[1]))
    else:
        coalesced_fresh.append(f)

# fresh_count = 0
# for a in available:
#     for cf in coalesced_fresh:
#         if a < cf[0]:
#             break
#         if a >= cf[0]:
#             if a <= cf[1]:
#                 fresh_count += 1
#                 break
# print(fresh_count)

fresh_count = 0
for cf in coalesced_fresh:
    fresh_count += cf[1]-cf[0]+1
print(fresh_count)