public class Question {
    private int id;
    private String Question;
    private String opt[];
    private String answer;

    public Question(int id, String question, String[] opt, String answer) {
        this.id = id;
        Question = question;
        this.opt = opt;
        this.answer = answer;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getQuestion() {
        return Question;
    }

    public void setQuestion(String question) {
        Question = question;
    }

    public String[] getOpt() {
        return opt;
    }

    public void setOpt(String[] opt) {
        this.opt = opt;
    }

    public String getOpt(int i) {
        return opt[i];
    }

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }

}
