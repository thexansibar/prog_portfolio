import java.util.Scanner;
import java.io.*;
public class PalindromeTestPageBen {     
	static boolean palTest(String pal){
            if (pal.length() == 0 || pal.length() == 1)
                return true;
            if (pal.charAt(0)== pal.charAt(pal.length()-1))
                return palTest(pal.substring(1, pal.length()-1));
            return false;
        }     
	public static void main(String[] args) throws Exception{
                File pals = new File("D:\\Java\\text\\wordList.txt");
                File write = new File("D:\\Java\\text\\palindromes.txt");
                write.createNewFile();
                PrintWriter writeToFile = new PrintWriter("D:\\Java\\text\\palindromes.txt");               
		Scanner testStr = new Scanner(pals);
		while (testStr.hasNextLine()) {
                    String tempString = testStr.nextLine();
                    if(palTest(tempString)==true){
                        writeToFile.println(tempString);
                    }			
		}
                writeToFile.close();
                System.out.println("Done.");
	}
}
