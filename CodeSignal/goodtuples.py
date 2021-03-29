"""

1. GoodTuples
int count = 0;
 HashSet<Integer> set = new HashSet<>();
for (int i = 0; i < arr.length-2; i++) {
set.put(arr[i - 1]);
set.put(arr[i]);
set.put(arr[i + 1]);
if (set.size() == 2 ) {
count ++;
} else {
set.clear();
continue;
}
}

"""