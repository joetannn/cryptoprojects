import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.ArrayList;

public class CaesarCipherWarmup
{
    public static void main(String [] args)
    {
        System.out.println("Option 1: brute force\nOption 2: Select the number of rotations");
        System.out.print("Your input: ");
        Scanner sc = new Scanner(System.in);

        int u_input = -1;

        try 
        {
            u_input = sc.nextInt();
            sc.nextLine();
            if (u_input != 1 && u_input != 2) throw new InputMismatchException();
        } 
        catch (Exception InputMismatchException) 
        {
            System.out.println("Invalid Input. Please type either 1 or 2. Exiting..");
            System.exit(0);
        }

        System.out.print("Please enter an input string: ");
        String data = sc.nextLine();
        ArrayList<Integer> prev_upperCase = new ArrayList<Integer>();
        for(int i = 0; i < data.length(); i++)
        {
            if (Character.isUpperCase(data.charAt(i)))
            {
                prev_upperCase.add(i);
            }
        }

        data = data.toLowerCase();
        String new_data = "";
        
        if(u_input == 1)
        {
            for(int rot_number = 1; rot_number < 26; rot_number++)
            {
                int curr_char = -1;
                new_data = rotate(rot_number, data);
                new_data = capitalize(prev_upperCase, new_data);
                System.out.println(rot_number + ": " + new_data);
                
            }
        }
        else if (u_input == 2)
        {
            System.out.print("Please enter the number of rotations: ");
            int rot_number = -1;
            try 
            {
                rot_number = sc.nextInt();
                if (rot_number < 0 || rot_number > 26) throw new InputMismatchException();
                if (rot_number == 26) rot_number = 0;
            } 
            catch (Exception InputMismatchException) 
            {
                System.out.println("Invalid Input. Exiting..");
                System.exit(0);
            }

            new_data = rotate(rot_number, data);
            new_data = capitalize(prev_upperCase, new_data);
            System.out.println("Output String: " +  new_data);

        }

    }

    public static String rotate(int rotation_number, String curr_data)
    {
            int curr_char = -1;
            String ret_data = "";
            for(int j = 0; j < curr_data.length(); j++)
            {
                curr_char = (int)curr_data.charAt(j);
                if(!Character.isLetter((char)curr_char))
                {
                    ret_data += (char)curr_char;
                    continue;
                }
                if(curr_char > 96 && curr_char < 123)
                {
                    if(curr_char + rotation_number < 123) ret_data += (char)(curr_char + rotation_number);
                    else ret_data += (char)(96 + rotation_number - (122 - curr_char));
                }
            }
        return ret_data;
    }

    public static String capitalize(ArrayList<Integer> cap_letters, String curr_data)
    {
        for(int k = 0; k < cap_letters.size(); k++)
        {
            int index = cap_letters.get(k);
            curr_data = curr_data.substring(0, index) + Character.toUpperCase(curr_data.charAt(index)) + curr_data.substring(index + 1, curr_data.length());
        }
        return curr_data;
    }
}