# **Computer Quiz Application**
The Computer Quiz Application is a fun and interactive project designed to test and enhance users' knowledge of computer science topics. This project provides both a Graphical User Interface (GUI) for a modern experience and a Command-Line Interface (CLI) for simple functionality. The application is built using Python with the tkinter library, offering an engaging platform for users to learn while competing for high scores.

### **Key Features**
1. **User-Friendly Interface**
  - The GUI is developed with tkinter, providing a sleek, modern, and intuitive design.
  - Buttons, labels, and entry fields are designed for ease of use and aesthetic appeal.

2. **Quiz Categories**
  - Users can choose from three categories of computer science topics:
    - **Hardware**: Questions about CPUs, GPUs, and other hardware concepts.
    - **Software**: Questions about operating systems, IDEs, and related topics.
    - **Networking**: Questions about IP addresses, DNS, and other networking fundamentals.

3. **Real-Time Quiz Interaction**
  - Each quiz session presents questions one at a time.
  - Users answer questions through an input field in the GUI.
  - A 10-second timer adds an element of challenge and urgency for each question.

4. **Scoring and Feedback**
  - Users receive instant feedback for their answers:
    - A "Correct!" or "Incorrect!" message is displayed for each question.
    - The final score is shown at the end of the quiz.
    - Scores are calculated based on the number of correct answers, allowing users to assess their knowledge level.

5. **High Score Leaderboard**
  - The application maintains a leaderboard for each category.
  - High scores are saved locally in a JSON file (high_scores.json).
  - If a user achieves a new high score, it is prominently displayed at the end of the quiz.

6. **CLI Mode**
  - For users who prefer a simpler experience, the command-line mode provides basic functionality:
    - Users can answer questions in a text-based environment.
    - Scores and answers are displayed in the console.

7. **Modular Design**
  - The project is structured with clear separation of concerns:
    - Utility functions for file handling and basic operations.
    - GUI components for user interaction.
    - Core logic for quiz progression, scoring, and high score management.

8. **Educational Value**
  - Encourages learning through gamification.
  - Covers essential computer science concepts in a structured manner.


### **Technical Details**
- Programming Language
- Python 3
- Libraries Used
- **tkinter**: For building the GUI.
- **os**: For file path and existence checks.
- **json**: For storing and retrieving high scores.
- **time**: For implementing the timer.



### **Target Audience**
  - **Students**: Ideal for students learning computer science concepts.
  - **Professionals**: A fun way for tech enthusiasts to refresh their knowledge.
  - **General Audience**: Suitable for anyone interested in testing their computer science knowledge.


### **Conclusion**
This project is an excellent example of combining learning with entertainment. By integrating a modern GUI with interactive features like real-time feedback and leaderboards, the application creates an engaging experience for users. Its modular design and clear structure make it a great learning tool for Python developers interested in GUI development, file handling, and application design.
