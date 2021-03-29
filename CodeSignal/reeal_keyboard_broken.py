"""
public class realBrokenKeyBoard {
  public static void main(String[] args) {
   String input = "Hello, my dear friend!";
   char[] b = {'h','e','l','m','o'};
   String[] wordsSet = input.toLowerCase().split(" ");
   boolean[] validLettersSet = new boolean[256];
   for (char c : b) {
     validLettersSet[c] = true;
   }
   int validWordCount = 0;
   for (String s : wordsSet) {
     boolean checkLegal = true;
     for (char c : s.toCharArray()) {
       if (validLettersSet[c] != true && Character.isLetter(c)) {
         checkLegal = false;
       }
     }
     if (checkLegal == true) {
       System.out.println(s);
       ++validWordCount;
     }
   }
   System.out.println(validWordCount);

 }
}


"""