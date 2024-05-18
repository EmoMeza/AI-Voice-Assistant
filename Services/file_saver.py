# file_saver.py
class FileSaver:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'wb') as f:
            f.write(data)
