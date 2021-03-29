"""

public class shipGame {
  //题目意思是给一堆船ships，然后给一串数组moves代表发射导弹的位置，.表示水， # 表示船， 几个连在一起的船一定是上下左右的连在一起
  //这个题给了限制条件，1. 连在一起的船的数量不会超过5，所以用不到dfs 2. 不同俩船队不会对角线挨在一起
  public static void main(String[] args) {
    char[][] ships = new char[][]{{'#', '.','.','#'},
                                  {'#', '.','.','#'},
                                  {'.', '.','.','.'},
                                  {'#', '#','.','#'},
                                  {'.', '#','.','#'}};
    int[][] moves = new int[][]{{0,0},{1,0},{0,3},{0,2},{4,3},{3,3},{3,0},{3,1},{4,1},{1,3}};
    for (String s : gameResult(ships, moves)) {
      System.out.println(s);
    }
  }
  public static String[] gameResult(char[][] ships,int[][] moves) {
    String[] result = new String[moves.length];
    int shipsNum = 0;
    int count = 0;
    for (int i = 0; i <ships.length ; i++) {
      for (int j = 0; j <ships[0].length ; j++) {
        if (ships[i][j] == '#') {
          shipsNum ++;
        }
      }
    }
    for (int i = 0; i <moves.length ; i++) {
      if (ships[moves[i][0]][moves[i][1]] == '.') {
        result[i] = "Miss";
      } else {
        //击中，周围没船 dead
        //击中，周围有船，周围的船都已经被击中 dead
        //击中，周围不是所有船都被击中 hit
        //设击中为0
        if (ships[moves[i][0]][moves[i][1]] == '#') {
          ships[moves[i][0]][moves[i][1]] = '0';
          count ++;
          if (count == shipsNum) {
            result[i] = "Game over";
          } else if (checkAround(ships, moves[i][0] + 1,moves[i][1]) ||
                  checkAround(ships, moves[i][0] - 1,moves[i][1]) ||
                  checkAround(ships, moves[i][0] ,moves[i][1] + 1) ||
                  checkAround(ships, moves[i][0] ,moves[i][1] - 1)) {
            result[i] = "Hit";
          } else {
            result[i] = "Dead";
          }
        }
      }
    }
    return result;
  }
  public static boolean checkAround(char[][] ships, int i, int j) {
    if (i < 0 || i >= ships.length || j < 0 || j >= ships[0].length) {
      return false;
    }
    if (ships[i][j] == '#') return true;
    if (ships[i][j] == '0') {
      return false;
    }
    return false;
  }
}


"""