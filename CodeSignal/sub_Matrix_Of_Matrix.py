"""

public class testHashMap {
 public static void main(String[] args) {
   Map<String, Integer> map = new HashMap();
   map.put("1", 8);
   map.put("2", 12);
   map.put("3", 53);
   map.put("4", 33);
   map.put("5", 11);
   map.put("6", 3);
   map.put("7", 3);
//对value进行排序，从小到大，然后放到一个list里面
   List<Map.Entry<String,Integer>> list = new ArrayList(map.entrySet());
   Collections.sort(list, (o1, o2) -> (o1.getValue() - o2.getValue()));
   for (Map.Entry i : list) {
     System.out.println(i.getKey() + " "+ i.getValue());
   }
 }
}
按value在排序，如果value相等，则按key的大小排序
numMap.entrySet().stream().sorted((a, b) -> b.getValue() - a.getValue() == 0 ? a.getKey() - b.getKey() : b.getValue() - a.getValue()).collect(Collectors.toList());

//array的prefixSum
for (int i = 0; i < arr.length; ++i) {
 prefixSum[i + 1] = prefixSum[i] + arr[i];
}


"""