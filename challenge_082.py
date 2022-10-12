'''
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
'''

class FileReader:
    def __init__(self, file_name: str):
        # Check that the file exists before fully instantiating the class.
        self._file_name = None
        self.file_name = file_name
        if self._file_name == None:
            raise FileNotFoundError(f"Unable to create FileReader instance using file name \'{file_name}\'")
        self._offset = 0

    # Using getter and setter methods for file_name. This helps prevent invalid inputs if the file name is modified after instantiation.
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, fn: str):
        try:
            f = open(fn)
        except:
            print(f"File \'{fn}\' does not exist or permission denied.")
        else:
            f.close()
            self._file_name = fn
        finally:
            return

    def read7(self):
        try:
            f = open(self.file_name, mode="r", encoding="utf-8")
        except:
            raise FileNotFoundError(f"File '{self.file_name}' Not Found or Permission Denied.")

        f.seek(self._offset)
        out_stream = f.read(7)
        self._offset = f.tell()
        f.close()
        return out_stream

    def readN(self, n: int):
        if n < 0:
            raise ValueError("n must be positive.")

        old_offset = self._offset

        # Read characters up until we have at least n.
        out_stream = ""
        chars_read = 0
        while chars_read < n:
            next_stream = self.read7()
            chars_read += len(next_stream)
            out_stream += next_stream
            if len(next_stream) < 7: # End of file.
                break

        # Move back the offset for when the last read7() call returned more characters than we need.
        if chars_read > n:
            self._offset -= chars_read-n
            # Workaround for Windows formatted line breaks outside the buffer length.
            # Python auto-converts from '\r\n' (2 characters) to '\n' (1 character) while incrementing the file pointer by 2.
            # Therefore, to get an accurate offset at the end of the method, Windows formatted line breaks in the tail have to be counted twice.
            if chars_read < self._offset - old_offset:
                self._offset -= next_stream[7-(chars_read-n):].count('\n')

        return out_stream[:n]

    def resetOffset(self, pos: int=0):
        if pos < 0:
            raise ValueError("pos must be positive.")
        self._offset = pos
        return

if __name__ == "__main__":
    # Using another py file here as a test file for this. Any text file will do.
    f_r = FileReader("challenge_81.py")
    print([f_r.readN(10), f_r.readN(10)])
    # Near end of file.
    f_r.resetOffset(1610)
    print([f_r.readN(25)])