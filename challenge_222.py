'''
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
'''

# Note: A properly-formed absolute pathname in Unix-like systems always begins with '/' (root).

def standardizePath(pathname: str):
    out_path = []

    for name in pathname.split('/'):
        if name == '..':
            if len(out_path) > 1:
                out_path.pop()
        elif name == '.':
            continue
        else:
            out_path.append(name)

    return '/'.join(out_path)

print(standardizePath("/usr/bin/../bin/./scripts/../"))