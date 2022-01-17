package Lab4;
import java.util.*;
/**
 *
 * @author ben page
 */
public class TicTacToe {
	
    public enum Game_Board { X, O, EMPTY;

        
    }
    
    private Game_Board[][] play_space;
    
    public TicTacToe(){
        play_space = new Game_Board[3][3];
        for (int i = 0; i < play_space.length; i++)
            for (int j = 0; j < play_space[i].length; j++){
                play_space[i][j] = Game_Board.EMPTY;
            }       
    } 
    
    public void Make_Board(int rows, int cols, Game_Board p_space){
        play_space[rows][cols] = p_space;
    }
    public String show(){
        return play_space[1][1].EMPTY.toString();
    }
   
    public String toString(){
        String display = "";
        for (Game_Board[] rows : play_space){
            for (Game_Board cols : rows){
                if (cols == Game_Board.EMPTY)
                    display = display + "-";
                else
                    display = display + cols;
            }
            display = display + "\n";
        }
        return display;
    }
  
    public boolean gameover(int rows, int cols){
        if (play_space[0][cols] == play_space[1][cols] && play_space[0][cols] 
                == play_space[2][cols])
            return true;
        if (play_space[rows][0] == play_space[rows][1] && play_space[rows][0] 
                == play_space[rows][2])
            return true;
        if (play_space[0][0] == play_space[1][1] && play_space[0][0] == play_space[2][2] 
                && show() == "EMPTY")
            return true;
        if (play_space[0][2] == play_space[1][1] && play_space[0][2] == play_space[2][0] 
                && show() == "EMPTY")
            return true;
        return false;
       
    }
   
    public static void main(String[] args){
        TicTacToe t = new TicTacToe();
        System.out.println(t.show());
    }
}
