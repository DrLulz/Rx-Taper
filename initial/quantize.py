import bisect

def quantize(num, quant):
    mids = [(quant[i] + quant[i + 1]) / 2.0
            for i in xrange(len(quant) - 1)]
    ind = bisect.bisect_right(mids, num)
    return quant[ind]

quantnum = [5, 10, 30, 60, 120, 180]

inputnum = [120]

for n in inputnum:
    print quantize(2 * n, quantnum)