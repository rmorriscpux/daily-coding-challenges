'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

def flattenDictionary(dictionary: dict):
    def rFlattenDictionary(subsection, flat_dict, path):
        if not isinstance(subsection, dict):
            flat_dict[path] = subsection
            return

        for key in subsection:
            key_path = f"{path}.{key}" if path else key
            rFlattenDictionary(subsection[key], flat_dict, key_path)

        return

    flat_dict = {}
    rFlattenDictionary(dictionary, flat_dict, "")
    return flat_dict

d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

print(flattenDictionary(d))