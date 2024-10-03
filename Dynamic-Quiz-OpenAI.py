import streamlit as st
from openai import OpenAI
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

class Question:
    def __init__(self, question, options, correct_answer, explanation=None):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

class Quiz:
    def __init__(self, topic, num_questions):
        self.topic = topic
        self.num_questions = num_questions
        self.questions = self.load_or_generate_questions()
        self.initialize_session_state()

    def load_or_generate_questions(self):
        if 'questions' not in st.session_state:
            st.session_state.questions = []
            for _ in range(self.num_questions):
                self.generate_and_append_question(self.topic)  # Generate unique questions for the chosen topic
        return st.session_state.questions

    def initialize_session_state(self):
        if 'current_question_index' not in st.session_state:
            st.session_state.current_question_index = 0
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'answers_submitted' not in st.session_state:
            st.session_state.answers_submitted = 0
        if 'answered' not in st.session_state:
            st.session_state.answered = False  # To track if the question has been answered

    def display_quiz(self):
        self.update_progress_bar()
        if st.session_state.answers_submitted >= len(self.questions):
            self.display_results()
        else:
            self.display_current_question()

    def display_current_question(self):
        question = self.questions[st.session_state.current_question_index]
        st.write(question.question)
        options = question.options
        answer = st.radio("Choose one:", options, key=f"question_{st.session_state.current_question_index}")
        
        # Show Submit Answer button if the question hasn't been answered yet
        if not st.session_state.answered:
            if st.button("Submit Answer", key=f"submit_{st.session_state.current_question_index}"):
                self.check_answer(answer)
                st.session_state.answered = True  # Mark question as answered
        
        # Show Next Question button after submitting the answer
        if st.session_state.answered:
            if st.button("Next Question"):
                self.next_question()
                st.rerun()  # Force re-render to immediately show the next question

    def check_answer(self, user_answer):
        correct_answer = self.questions[st.session_state.current_question_index].correct_answer
        if user_answer == correct_answer:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error("Wrong answer!")
        if self.questions[st.session_state.current_question_index].explanation:
            st.info(self.questions[st.session_state.current_question_index].explanation)

    def next_question(self):
        st.session_state.answers_submitted += 1
        if st.session_state.current_question_index < len(self.questions) - 1:
            st.session_state.current_question_index += 1
        st.session_state.answered = False  # Reset for the next question

    def display_results(self):
        total_questions = len(self.questions)
        score_percentage = (st.session_state.score / total_questions) * 100
        st.write(f"Quiz completed! You scored {st.session_state.score}/{total_questions} ({score_percentage:.2f}%).")
        if score_percentage == 100:
            st.success("Perfect score! Congratulations!")
            st.balloons()
        elif score_percentage >= 50:
            st.info("Good effort, try again for a perfect score.")
        else:
            st.error("Better luck next time!")
        if st.button("Restart Quiz"):
            self.restart_quiz()

    def update_progress_bar(self):
        total_questions = len(self.questions)
        progress = st.session_state.answers_submitted / total_questions
        st.progress(progress)

    def restart_quiz(self):
        # Clear all relevant session states to bring the user back to the topic and question selection screen
        st.session_state.clear()  # Clears all session state variables
        st.rerun()  # Force re-render to restart from the beginning

    def generate_and_append_question(self, user_prompt):
        history = "\n".join([f"Question: {q.question}, Answer: {q.correct_answer}" for q in st.session_state.questions])

        gpt_prompt = f'''
Generate a unique JSON response for a trivia question about {user_prompt}. 
The question must be different from the following already generated questions: 
{history}
The format should be as follows:

{{
  "Question": "The actual question text goes here?",
  "Options": ["Option1", "Option2", "Option3", "Option4"],
  "CorrectAnswer": "TheCorrectAnswer",
  "Explanation": "A detailed explanation on why the correct answer is correct."
}}
'''
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": gpt_prompt}
                ]
            )
            gpt_response = json.loads(response.choices[0].message.content)
            new_question = Question(
                question=gpt_response["Question"],
                options=gpt_response["Options"],
                correct_answer=gpt_response["CorrectAnswer"],
                explanation=gpt_response["Explanation"]
            )
            st.session_state.questions.append(new_question)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


# Main app logic
if 'quiz_initialized' not in st.session_state:
    user_topic = st.text_input("What topic do you want the quiz to cover?", value="AI")
    num_questions = st.number_input("How many questions would you like to generate?", min_value=1, max_value=10, value=5, step=1)
    
    if st.button('Start Quiz'):
        st.session_state.quiz = Quiz(user_topic, num_questions)
        st.session_state.quiz_initialized = True

if 'quiz_initialized' in st.session_state:
    st.session_state.quiz.display_quiz()
