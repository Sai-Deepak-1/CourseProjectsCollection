import java.util.Scanner;

public class QuestionService {
    Question[] questions = new Question[5];
    String[] answers = new String[5];
    int score = 0;

    public QuestionService() {
        questions[0] = new Question(1, "What is the capital of India?",
                new String[] { "Delhi", "Mumbai", "Kolkata", "Chennai" }, "Delhi");
        questions[1] = new Question(2, "What is the capital of Australia?",
                new String[] { "Sydney", "Melbourne", "Canberra", "Perth" }, "Canberra");
        questions[2] = new Question(3, "What is the capital of USA?",
                new String[] { "New York", "Washington D.C.", "Los Angeles", "Chicago" }, "Washington D.C.");
        questions[3] = new Question(4, "What is the capital of Japan?",
                new String[] { "Tokyo", "Osaka", "Kyoto", "Hiroshima" }, "Tokyo");
        questions[4] = new Question(5, "What is the capital of France?",
                new String[] { "Paris", "Lyon", "Marseille", "Nice" }, "Paris");
    }

    public void displayQuestions() {
        Scanner sc = new Scanner(System.in);
        int i = 0;
        for (Question q : questions) {
            System.out.println("Question " + q.getId() + " : " + q.getQuestion());
            int count = 1;
            for (String option : q.getOpt()) {
                System.out.println("Opt " + count + " " + option);
                count++;
            }
            System.out.println("Enter your answer : ");
            answers[i] = sc.nextLine();
            i++;
        }
        for (int j = 0; j < answers.length; j++) {
            if (questions[j].getOpt()[Integer.parseInt(answers[j]) - 1].equalsIgnoreCase(questions[j].getAnswer())) {
                System.out.println("Answer " + (j + 1) + " " + questions[j].getOpt()[Integer.parseInt(answers[j]) - 1]
                        + " is correct");
                score++;
            } else {
                System.out.println("Answer " + (j + 1) + " " + questions[j].getOpt()[Integer.parseInt(answers[j]) - 1]
                        + " is incorrect, Correct Answer is " + questions[j].getAnswer());
            }
        }
        System.out.println("Your score is : " + score + "/5");
        sc.close();
    }
}
