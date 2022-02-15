import pandas as pd
import sys
import os


class Combiner:

    @staticmethod
    def checkFilePath(argv):
        """
        This function checks whether the arguments input by the user are valid or not.
        """

        if len(argv) <= 1:
            print("Error: file path inputs not find. Please run the code in the following format: \n" +
                  "python ./csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv")
            return False

        filelst = argv[1:]

        for file_path in filelst:
            if not os.path.exists(file_path):
                print("Error: File or directory not found: " + file_path)
                return False
            if os.stat(file_path).st_size == 0:
                print("Warning: The following file is empty: " + file_path)
                return False
        return True

    def combineFiles(self, argv: list):
        """
        This function adds a new column to the original file and combines all rows in the given files
        """
        chunksize = 10 ** 4
        chunk_list = []

        if self.checkFilePath(argv):
            # if file inputs are correct
            filelst = argv[1:]

            for file_path in filelst:

                # read as chunks to prevent memory issues
                for chunk in pd.read_csv(file_path, chunksize=chunksize):

                    # get the file name from the path
                    filename = os.path.basename(file_path)

                    # add the 'filename' column to the chunk
                    chunk['filename'] = filename
                    chunk_list.append(chunk)

            # flag to indicate if a header should be added
            header = True

            # combine all chunks
            for chunk in chunk_list:
                print(chunk.to_csv(index=False, header=header, line_terminator='\n', chunksize=chunksize), end='')
                header = False
        else:
            # if file inputs are wrong, print error/warning message
            return


def main():
    combiner = Combiner()
    combiner.combineFiles(sys.argv)

if __name__ == '__main__':
    main()
