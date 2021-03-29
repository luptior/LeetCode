"""

public static int wordsIsValid(String[] words, char[] letters) {
        Set<Character> set = new HashSet<>();
        for(char c : letters) {
            set.add(Character.toLowerCase(c));
        }
        int res = 0;
        for(String word : words) {
            char[] wordChar = word.toCharArray();
            boolean isValid = true;
            for(int i = 0; i < wordChar.length; i++) {
                char curr = wordChar[i];
                if(Character.isLowerCase(curr) || Character.isUpperCase(curr)) {
                    curr = Character.toLowerCase(curr);
                    if(!set.contains(curr)) {
                        isValid = false;
                        break;
                    }
                }
            }
            if(isValid) {
                res++;
            }
        }
        return res;
    }


"""