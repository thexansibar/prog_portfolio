

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Ben Page
 */
public class Lab6PageBen {
     public static double squareroot(double num)
            throws IllegalArgumentException
    {
        return Math.sqrt(num);
    } 

    public static void main( String args[] )
    {

        Scanner scanner = new Scanner( System.in );
        boolean continueLoop = true; 
        
        do
        {
            try 
            {
                System.out.print( "Please enter an integer: \n" );
                double num = scanner.nextInt();
                if(num < 0){
                    throw new IllegalArgumentException();
                }
                double result = squareroot(num);
                System.out.printf( "\nResult: Square root of " + num + " is " + result + "\n");
            } 
            catch ( InputMismatchException inputMismatchException )
            {
                System.err.printf( "\nException: %s\n",
                        inputMismatchException );
                scanner.nextLine(); 
                System.out.println(
                        "You must enter integers. Please try again.\n" );
            } 
            catch ( IllegalArgumentException illegalArgumentException )
            {
                System.err.printf( "\nException: %s\n", illegalArgumentException );
                System.out.println(
                        "You cannot square a negative number in Java! Please try again.\n" );
            } 
        } while ( continueLoop ); 

    } 
    
}
