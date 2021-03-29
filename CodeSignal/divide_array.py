"""

public static void main(String[] args) {
   int[] arr = new int[]{1, 2, 1,2,4, 5};
   List<int[]> list = divideHelper(arr);
   for (int[] a : list) {
     for (int i : a) {
       System.out.print(i + " ");
     }
     System.out.println();
   }
 }
 public static List<int[]> divideHelper(int[] arr) {
   if (arr.length % 2 != 0) {
     return null;
   }
   List <int[]> list = new LinkedList <>();
   HashMap<Integer, Integer> map = new HashMap<>(arr.length);
   for (int i = 0; i <arr.length ; i++) {
//      if (map.containsKey(arr[i])) {
//        map.put(arr[i], map.get(arr[i]) + 1);
//      } else {
//        map.put(arr[i], 1);
//      }
     map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
   }
   boolean checkIt = true;
   List<Integer> lista = new LinkedList <>();
   List<Integer> listb = new LinkedList <>();
   int checkEvenOrOdd = 0;
   for (Integer i : map.values()) {
     System.out.println("key" + i);
   }
   for (Integer i : map.keySet()) {
     if (map.get(i) > 2) {
       checkIt = false;
     }
     if (map.get(i) == 2) {
       lista.add(i);
       listb.add(i);
     }
     if (map.get(i) < 2) {
       checkEvenOrOdd++;
       if (checkEvenOrOdd % 2 != 0) {
         lista.add(i);
       }
       else {
         listb.add(i);
       }
     }
   }
   if (!checkIt) {
     return null;
   }
   if (checkEvenOrOdd % 2 != 0) {
     return null;
   }
   int[] arra = new int[lista.size()];
   for (int i  = 0; i < lista.size(); i++) {
     arra[i] = lista.get(i).intValue();
   }
   int[] arrb = new int[listb.size()];
   for (int i  = 0; i < listb.size(); i++) {
     arrb[i] = listb.get(i).intValue();
   }

   list.add(arra);
   list.add(arrb);
   return list;
 }


"""