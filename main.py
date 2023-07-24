import pandas as pd
import re
import sys

try:
    import gzip

    have_gzip = True
except ImportError:
    have_gzip = False
try:
    import bz2

    have_bz2 = True
except ImportError:
    have_bz2 = False

from pystdf.IO import Parser
from pystdf.Writers import TextWriter
import pystdf.V4

gzPattern = re.compile('\.g?z', re.I)
bz2Pattern = re.compile('\.bz2', re.I)


def analyse():
    filePath = "F43C1.1_C425026086_62220A_DCSORT_V01_CP62220AE01_ETS175659_04212023.stdf"
    new_file_path = "F43C1.1_C425026086_62220A_DCSORT_V01_CP62220AE01_ETS175659_04212023.stdf.csv"
    reopen_fn = None
    if filePath is None:
        f = sys.stdin
    elif gzPattern.search(filePath):
        if not have_gzip:
            print("gzip is not supported on this system", file=sys.stderr)
            sys.exit(1)
        reopen_fn = lambda: gzip.open(filePath, 'rb')
        f = reopen_fn()
    elif bz2Pattern.search(filePath):
        if not have_bz2:
            print("bz2 is not supported on this system", file=sys.stderr)
            sys.exit(1)
        reopen_fn = lambda: bz2.BZ2File(filePath, 'rb')
        f = reopen_fn()
    else:
        f = open(filePath, 'rb')
    p = Parser(inp=f, reopen_fn=reopen_fn)

    with open(new_file_path, 'w') as fout:
        p.addSink(TextWriter(stream=fout, delimiter=","))
        p.parse()
    f.close()

if __name__ == '__main__':
    analyse()

# 打开STDF文件
# with open('C5UC3.3_C425021596_62230A10V10mCP62230AE01_DCSORT_V01_CP62230AE01_ETS154131_04202023.stdf', 'rb') as f:
#     # 解析STDF文件
#     stdf_data = pystdf.stdf_reader(f)
#
#     # 将STDF数据存储在数据帧中
#     df = pd.DataFrame.from_records(stdf_data.records)
#
#     # 将数据帧写入CSV文件
#     df.to_csv('example.csv', index=False)
