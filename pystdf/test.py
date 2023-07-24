import sys
from pystdf.IO import Parser
from pystdf.Writers import TextWriter


def analyse():
    filePath = "C5UC3.3_C425021596_62230A10V10mCP62230AE01_DCSORT_V01_CP62230AE01_ETS154131_04202023.stdf"
    new_file_path = "C5UC3.3_C425021596_62230A10V10mCP62230AE01_DCSORT_V01_CP62230AE01_ETS154131_04202023.stdf.csv"
    reopen_fn = None
    f = open(filePath, 'rb')
    p = Parser(inp=f, reopen_fn=reopen_fn)

    with open(new_file_path, 'w') as fout:
        p.addSink(TextWriter(stream=fout, delimiter=","))
        p.parse()
    f.close()

if __name__ == '__main__':
    analyse()
