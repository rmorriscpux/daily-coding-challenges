'''
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

# Making a nested dictionary to represent the directory structure.

def string_to_directory(dir_str):
    return dir_str.split('\n')

def count_tabs(str):
    count = 0
    while str[count] == '\t':
        count += 1
    return count

def determine_longest_file_path(dir_str):
    directory = dir_str.split('\n')
    max_length = 0
    max_str = []

    path_list = []

    for line in directory:
        # Truncate path list
        path_list = path_list[:count_tabs(line)]
        # Add new line
        path_list.append(line.strip('\t'))
        # Check if we have a file.
        if line.find('.') != -1: # Is a file.
            # Check the total path length and compare with max.
            path_length = 0
            for name in path_list:
                path_length += len(name) + 1
            path_length -= 1 # No trailing /

            if path_length > max_length:
                max_length = path_length
                max_str = path_list

    return max_length

print(determine_longest_file_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(determine_longest_file_path("dir\n\tsubdir1\n\t\tfile1ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2ext"))