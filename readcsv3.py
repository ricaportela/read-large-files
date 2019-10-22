import csv
import hashlib as hash

class CSVLoader:
    _data = []
    _checksum_table = {}
    _checksum_errors = []
    _parsed = False
    _reader = None
    _with_header = True
    _header = []

    def __init__(self, file_name, with_header=True):
        try:
            self._with_header = with_header
            file = open(file_name)
            self._reader = csv.reader(file, delimiter=',')
        except:
            print("Error found while trying to access file %s." % (file_name,))
    
    def _parse(self, checksum_table=None):
        try:
            if not self._parsed:
                current_row = 0
                rows = list(self._reader)
                for row in rows:
                    if current_row == 0 and self._with_header:
                        self._header = row
                        current_row += 1
                        continue
                    current_row += 1

                    parsed = dict(zip(self._header, row)) if self._with_header else list(row)
                    checksum = hash.md5(''.join(row)).hexdigest()

                    if checksum_table.has_key(checksum):
                        self._checksum_errors.append({
                            "row": current_row,
                            "hash": checksum
                        })
                    
                    self._checksum_table[checksum] = True
                    self._data.append(parsed)    
        except:
            print("Error while trying to parse CSV file contents.")
    
    def load(self, checksum_table={}):
        self._parse(checksum_table)

        return self

    def fetch_all(self):
        return self._data
    
    def get_checksum_table(self):
        return self._checksum_table
    
    def get_checksum_errors(self):
        return self._checksum_errors
    
    def has_checksum_errors(self):
        return len(self._checksum_errors) > 0

if __name__ == "__main__":
    arq1 = CSVLoader("arq_1.csv")
    arq2 = CSVLoader("arq_2.csv")

    arq1_checksum = arq1.load().get_checksum_table()

    print(arq2.load(arq1_checksum).get_checksum_errors())