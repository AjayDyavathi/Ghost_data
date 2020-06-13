#! /usr/bin/python3
# Description: Data_Ghost, concealing data into spaces and tabs making it impreceptable to human eyes.
# Author: Ajay Dyavathi
# Github: Radical Ajay

class Ghost():
    def __init__(self, file_name, output_format='txt'):
        ''' Converts ascii text to spaces and tabs '''

        self.file_name = file_name
        self.output_format = output_format

    def ascii2bin(self, asc):
        ''' Converting from ascii to bianry '''

        return ''.join('{:08b}'.format(ord(i)) for i in asc)

    def bin2ascii(self, bid):
        ''' Converting from binary to ascii '''

        return ''.join(chr(int(bid[i:i + 8], 2)) for i in range(0, len(bid), 8))

    def ghost(self, filename):
        ''' Ghosting data converting it to spaces and tabs '''

        with open(filename, 'w') as out_f:
            with open(self.file_name, 'r') as in_f:
                for in_data in in_f.readlines():
                    bin_data = self.ascii2bin(in_data)
                    out_data = bin_data.replace('1', '\t')
                    out_data = out_data.replace('0', ' ')
                    out_f.write(out_data)

    def unghost(self, in_filename, out_filename):
        ''' Unghosting data converting back from spaces and tabs to human-readable text '''

        with open(out_filename, 'w') as out_f:
            with open(in_filename, 'r') as in_f:
                for line in in_f.readlines():
                    line = line.replace('\t', '1')
                    line = line.replace(' ', '0')
                    out_f.write(self.bin2ascii(line))


# USAGE:

# ghoster = Ghost('data.txt')
# ghoster.ghost('ghosted.txt')
# ghoster.unghost('ghosted.txt', 'unghosted.txt')
