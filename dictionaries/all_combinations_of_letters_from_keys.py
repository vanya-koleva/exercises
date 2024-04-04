import itertools

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}
for combo in itertools.product(*[sample_data[k] for k in sorted(sample_data.keys())]):
    print(''.join(combo))
