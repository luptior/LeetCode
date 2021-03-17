class Solution:

    def __init__(self):

        self.result = 0

    def numTeams(self, rating: [int]) -> int:
        self.countNextStep([], rating)
        return self.result

    def if_valid(self, arr: [int]):
        if len(arr) != 3: 
            return

        if (arr[0] > arr[1] > arr[2]) or (arr[0] < arr[1] < arr[2]):
            self.result += 1

    def countNextStep(self, prev, left):

        if len(prev) > 3 or len(prev) < 3 and not left:
            return

        if len(prev) == 3:
            # print(prev, left, self.result)
            self.if_valid(prev)
            return

        for i, element in enumerate(left):
            self.countNextStep(prev+[element], left[i+1:])


if __name__ == '__main__':
    s = Solution()
    
    ratings = [443,1720,2354,1344,2905,2401,1097,1521,2636,1412,132,2906,1748,731,1003,977,1693,601,1143,1121,53,2005,
              722,2170,2341,231,1414,735,1723,581,1917,853,955,2860,2186,1027,1141,969,106,1455,2453,155,1945,2998,237,
              2065,2466,2416,172,293,2424,2562,453,676,2219,1966,893,2011,1827,602,168,777,484,1886,392,2955,741,1532,
              1478,559,2680,1743,1082,1523,1212,787,1662,2594,402,441,879,313,1505,2258,2303,2166,1820,2580,2893,1234,
              48,2533,1884,1504,1763,193,1477,1926,2259,264,2683,1362,2031,2859,20,1223,983,2849,2571,299,628,1722,1608,
              945,932,2832,554,2503,1096,759,2458,2322,2469,2964,1114,1417,577,634,2720,749,442,37,778,784,1297,1235,
              681,1229,68,2704,307,930,2681,2937,1810,2843,992,2396,1853,160,1073,486,800,837,2523,1995,789,226,2000,
              2110,2545,3000,1010,1840,2095,1685,259,1951,2249,1545,2356,2510,848,975,550,410,2599,2902,164,2896,2012,
              314,1632,536,3,1161,2693,1327,1347,2962,2420,1757,1415,2073,116,261,834,1786,673,2519,2020,2437,1034,
              828,205,1702,820,2716,2406,1854,145,2305,968,288,361,461,56,2806,2909,1134,2158,1880,494,699,1719,2162,
              2386,1266,671,1548,2419,552,1237,2036,1875,976,2923,1922,435,2904,1553,1336,1579,733,1173,2353,2413,2456,
              2813,1463,2863,696,2837,1964,1986,935,1712,459,1787,101,2035,2765,2978,1318,2403,885,1194,2981,2798,2435,
              1286,1974,877,354,728,111,2477,1383,2993,570,1513,619,2732,2788,426]

    print(s.numTeams(ratings))