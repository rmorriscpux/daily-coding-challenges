'''
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
'''

# Note: A properly-formed absolute pathname in Unix-like systems always begins with '/' (root).

def standardizePath(pathname: str):
    out_path_list = []

    for name in pathname.split('/'):
        # '.' means "Current Directory". Do nothing.
        if name == '.':
            continue
        # '..' means "Parent Directory". Remove last from directory list.
        elif name == '..':
            # '..' at the root level should be ignored, i.e. only remove the last item in out_path_list if it's past the root.
            if len(out_path_list) > 1:
                out_path_list.pop()
        # Add to directory list.
        else:
            out_path_list.append(name)

    out_path = '/'.join(out_path_list)
    # Remove duplicate '/' characters.
    while out_path.find('//') != -1:
        out_path = out_path.replace('//', '/')

    return out_path

print(standardizePath("/usr/bin/../bin/./scripts/../"))