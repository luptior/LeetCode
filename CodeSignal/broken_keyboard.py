"""
import java.util.Arrays;
import java.util.HashSet;

public class brokenKeyBoard {

 public static void main(String[] args) {
   String input = "world! Hello, world! hee oo";
   char[] legalLetters = {'h','e','l','o'};
   boolean[] letterSet = new boolean[256]
   for (char c : legalLetters) {
     letterSet[c] = true;
   }
   String[] newStr = input.toLowerCase().split(" ");
   int num = 0;
   long result = Arrays.stream(newStr).filter(str -> {
     for (char c : str.toCharArray()) {
       if (!letterSet[c] && Character.isLetter(c)) {
         return false;
       }
     }
     return true;
   }).count();
   System.out.println(result);
 }
}

https://www.hackerrank.com/contests/csindia14-qr1/challenges/broken-keyboard


输入一组words和一组valid letters，判断有多少个words是valid。判断条件是words里的所有 upper and lower letter必须在valid letters里面。
如果word里面有special character不用管。注 意valid letter只有小写，但是words里面有大写的也算valid。比如words = [hEllo##, This^^],
valid letter = [h, e, l, 0, t, h, s]; "hello##" 就是valid，因为h，e，l，o都在valid letter 里面， “This^^” 不valid,
因为i不在valid letter里面
input: a = "Hello, my dear friend!", b = ['h', 'e', 'l', 'o', 'm']
output: 1 题目是键盘坏了，只剩下b中的字母按键和所有的数字和符号案件能用，同时shift键是好的， 所以可以切换大小写。
问a中的单词有几个可以用当前坏掉的键盘打出来。

"""



input = "hello, world!"

source = ['i','e','o','l','h']

words = input.split(" ")

count = 0

for word in words:
    if sum([ 0 if x in source or not x.isalpha() else 1 for x in word]) == 0:
        count += 1


print(count)