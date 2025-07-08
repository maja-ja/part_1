with open('root', 'r') as f:
    idx = int(f.read().strip())

module_name = f'module-{idx}.py'
exec(open(module_name).read())
