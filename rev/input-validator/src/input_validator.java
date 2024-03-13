import java.util.Scanner;

public class input_validator{

    private static final int FLAG_LEN = 34;

    private static boolean validate(String input, String str) {
        int[] new_array = new int[FLAG_LEN];
        int[] final_array = {1102, 1067, 1032, 1562, 1612, 1257, 1562, 1067, 1012, 902, 882, 1397, 1472, 1312, 1442, 1582, 1067, 1263, 1363, 1413, 1379, 1311, 1187, 1285, 1217, 1313, 1297, 1431, 1137, 1273, 1161, 1339, 1267, 1427};

        for (int i = 0; i < FLAG_LEN; i++) {
            new_array[i] = (int) input.charAt(i) ^ (int) str.charAt(i);
        }

        for (int i = 0; i < FLAG_LEN; i++) {
            new_array[i] = new_array[i] - str.charAt(FLAG_LEN - 1 - i);
        }

        int[] newer_array = new int[FLAG_LEN];
        for (int i = 0; i < FLAG_LEN / 2; i++) {
            newer_array[i] = new_array[1 + i * 2] * 5;
            newer_array[i + (FLAG_LEN / 2)] = new_array[i * 2] * 2;
        }

        for (int i = 0; i < FLAG_LEN; i++)
            newer_array[i] += 1337;

        for (int i = 0; i < FLAG_LEN; i++) {
            if (newer_array[i] != final_array[i]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = "oF/M5BK_U<rqxCf8zWCPC(RK,/B'v3uARD";

        System.out.print("Enter input: ");
        String input = scanner.nextLine();

        if (input.length() != FLAG_LEN) {
            System.out.println("Input length does not match!");
            return;
        }

        if (validate(new String(input), str))
            System.out.println("Correct");
        else
            System.out.println("Wrong");
    }
}
