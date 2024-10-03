# Dynamic Quiz Application using OpenAI

An interactive Streamlit application that generates dynamic quizzes on any topic using the OpenAI API. Users can choose a topic and the number of questions, and the app will create unique quiz questions on the fly, providing an engaging and educational experience.

## Features

- **Customizable Topics**: Input any topic of your choice (e.g., AI, history, science) to generate quiz questions tailored to that subject.
- **Dynamic Question Generation**: Leverages OpenAI's GPT-3.5-turbo model to create unique trivia questions, ensuring a fresh experience every time.
- **Customizable Quiz Length**: Choose the number of questions you want in your quiz (between 1 and 10).
- **Interactive Interface**: Simple and user-friendly interface built with Streamlit for seamless interaction.
- **Progress Tracking**: Visual progress bar to track your completion status throughout the quiz.
- **Immediate Feedback**: Provides instant feedback on whether your answer was correct or incorrect, along with detailed explanations.
- **Score Display**: Shows your total score and percentage at the end of the quiz, with encouraging messages based on performance.
- **Restart Option**: Easily restart the quiz with new questions or change the topic and number of questions.

## Technologies Used

- **Python 3**
- **Streamlit**
- **OpenAI API**
- **JSON**

## Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- An **OpenAI API key**. Obtain one by signing up on the [OpenAI website](https://openai.com/).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/Dynamic-Quiz-OpenAI.git
   cd Dynamic-Quiz-OpenAI
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**

   - Create a `.streamlit` directory in the root of your project:

     ```bash
     mkdir .streamlit
     ```

   - Inside `.streamlit`, create a `secrets.toml` file:

     ```toml
     # .streamlit/secrets.toml
     OPENAI_API_KEY = "your_openai_api_key_here"
     ```

   - **Important**: Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

### Running the Application

```bash
streamlit run app.py
```

- Replace `app.py` with the name of your main Python script if it's different.

## Usage

1. **Enter Quiz Topic**

   - In the input field, type the topic you want the quiz to cover (e.g., "Artificial Intelligence", "World War II", "Python Programming").

2. **Select Number of Questions**

   - Choose how many questions you'd like in your quiz (minimum 1, maximum 10).

3. **Start Quiz**

   - Click the **"Start Quiz"** button to generate the quiz questions.

4. **Answer Questions**

   - Read each question and select your answer from the provided options.
   - Click **"Submit Answer"** to check if you got it right.
   - Review the immediate feedback and explanation provided.

5. **Proceed to Next Question**

   - Click **"Next Question"** to move on.
   - The progress bar at the top shows your completion status.

6. **View Results**

   - After answering all questions, your total score and percentage will be displayed.
   - Receive personalized feedback based on your performance.

7. **Restart Quiz**

   - Click **"Restart Quiz"** to begin a new quiz with the same or different parameters.

## Acknowledgments

- Thanks to the developers of Streamlit and OpenAI for their powerful tools.
- Inspired by educators and quiz enthusiasts who make learning interactive and fun.project.
