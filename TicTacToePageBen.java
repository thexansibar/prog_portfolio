package Lab4;
import Lab4.TicTacToe.*;
import static Lab4.TicTacToe.Game_Board.*;

import java.util.*;
/**
 *
 * @author ben page
 */
public class TicTacToePageBen {
    public static void main(String[] args){
        boolean gameover = true;
        int player = 0;
        
        TicTacToe gametime = new TicTacToe();
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("Welcome to Tic-Tac-Toe!");
        System.out.println("Player 1, make your first move:");
        System.out.println("Pick a set of coordinates you wish \nto put on the "
                + "board, one at a time('1,1' IS CENTER)");
        
        System.out.println(gametime);
        
        int x = input.nextInt();
        int y = input.nextInt();
        
        gametime.Make_Board(x,y,X);
        System.out.println(gametime);
        player = player + 1;
        while (gameover){
             x = input.nextInt();
             y = input.nextInt();
            if (player == 0){
               
                System.out.println("Player 1's Turn:");
                
                gametime.Make_Board(x,y,X);
                System.out.println(gametime);
                if (gametime.gameover(x, y)){
                    gameover = false;
                    System.out.println("Player 1 Wins");
                }
                else{   
                player = player + 1;
                }
            }
            else if (player == 1){
                System.out.println("Player 2's Turn:");
                
                gametime.Make_Board(x,y,O);
                System.out.println(gametime);
                if (gametime.gameover(x, y)){
                    gameover = false;
                    System.out.println("Player 2 Wins");
                }
                else{   
                player = player - 1;
                }
            }
            else{
                System.out.println("INVALID INPUT");
            }
        }
       
    }
}
