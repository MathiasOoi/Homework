
attrs = {
        'spots': {0},
        'firebreathing': {0},
        'flying': {2, 3},
        'telepathic': {2},
        }

def attrs_ok(attrs):
    for a, aa in attrs.items():
        for b, bb in attrs.items():
            if a == b: continue
            if not aa.intersection(bb): continue
            if not (aa - bb): continue
            if not (bb - aa): continue
            print(a, aa, 'incompatible with', b, bb)
            return False
    return True

print(attrs_ok(attrs))
