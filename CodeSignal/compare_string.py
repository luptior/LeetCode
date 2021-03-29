"""

boolean compareResult = true;
 String className = "abbzccc";
 String methodName = "babzzcz";
 int[] classLettersSet = new int[256];
 for (char c : className.toCharArray()) {
   classLettersSet[c] += 1;
 }
 for (char c : methodName.toCharArray()) {
   if (classLettersSet[c] == 0) {
     compareResult = false;
   }
 }
 int[] methodLetterSet = new int[256];
 for (char c : methodName.toCharArray()) {
   methodLetterSet[c] += 1;
 }
 for (char c : className.toCharArray()) {
   if (methodLetterSet[c] == 0) {
     compareResult = false;
   }
 }
 Arrays.sort(classLettersSet);
 Arrays.sort(methodLetterSet);
 if (!Arrays.equals(classLettersSet, methodLetterSet)) {
   compareResult = false;
 }
 System.out.println(compareResult);
}
}


"""