from app import db
from app.models import Quiz, Question, Answer

def add_quiz_data():
    # Add History Quiz
    history_quiz = Quiz(title='History Quiz', category='history')
    db.session.add(history_quiz)
    db.session.commit()

    history_questions = [
        {
            'text': 'Who was the first President of the United States?',
            'answers': [
                {'text': 'George Washington', 'is_correct': True},
                {'text': 'Thomas Jefferson', 'is_correct': False},
                {'text': 'Abraham Lincoln', 'is_correct': False},
                {'text': 'John Adams', 'is_correct': False}
            ]
        },
        {
            'text': 'Which event started World War I?',
            'answers': [
                {'text': 'Assassination of Archduke Franz Ferdinand', 'is_correct': True},
                {'text': 'Sinking of the Lusitania', 'is_correct': False},
                {'text': 'Invasion of Poland', 'is_correct': False},
                {'text': 'Treaty of Versailles', 'is_correct': False}
            ]
        },
        {
            'text': 'Who was known as the "Iron Lady"?',
            'answers': [
                {'text': 'Margaret Thatcher', 'is_correct': True},
                {'text': 'Angela Merkel', 'is_correct': False},
                {'text': 'Hillary Clinton', 'is_correct': False},
                {'text': 'Condoleezza Rice', 'is_correct': False}
            ]
        },
        {
            'text': 'In which year did the Berlin Wall fall?',
            'answers': [
                {'text': '1989', 'is_correct': True},
                {'text': '1991', 'is_correct': False},
                {'text': '1985', 'is_correct': False},
                {'text': '1993', 'is_correct': False}
            ]
        },
        {
            'text': 'Who discovered America?',
            'answers': [
                {'text': 'Christopher Columbus', 'is_correct': True},
                {'text': 'Amerigo Vespucci', 'is_correct': False},
                {'text': 'Leif Erikson', 'is_correct': False},
                {'text': 'Ferdinand Magellan', 'is_correct': False}
            ]
        },
        {
            'text': 'Which ancient civilization built the pyramids?',
            'answers': [
                {'text': 'Egyptians', 'is_correct': True},
                {'text': 'Romans', 'is_correct': False},
                {'text': 'Greeks', 'is_correct': False},
                {'text': 'Aztecs', 'is_correct': False}
            ]
        },
        {
            'text': 'Who was the first man to step on the moon?',
            'answers': [
                {'text': 'Neil Armstrong', 'is_correct': True},
                {'text': 'Buzz Aldrin', 'is_correct': False},
                {'text': 'Yuri Gagarin', 'is_correct': False},
                {'text': 'Michael Collins', 'is_correct': False}
            ]
        },
        {
            'text': 'What was the main cause of the Cold War?',
            'answers': [
                {'text': 'Ideological conflict between the US and the USSR', 'is_correct': True},
                {'text': 'Territorial disputes', 'is_correct': False},
                {'text': 'Economic sanctions', 'is_correct': False},
                {'text': 'Religious differences', 'is_correct': False}
            ]
        },
        {
            'text': 'Who wrote the "I Have a Dream" speech?',
            'answers': [
                {'text': 'Martin Luther King Jr.', 'is_correct': True},
                {'text': 'Malcolm X', 'is_correct': False},
                {'text': 'Frederick Douglass', 'is_correct': False},
                {'text': 'Rosa Parks', 'is_correct': False}
            ]
        },
        {
            'text': 'Which empire was known as the "Empire on which the sun never sets"?',
            'answers': [
                {'text': 'British Empire', 'is_correct': True},
                {'text': 'Roman Empire', 'is_correct': False},
                {'text': 'Ottoman Empire', 'is_correct': False},
                {'text': 'Spanish Empire', 'is_correct': False}
            ]
        }
    ]

    for q in history_questions:
        question = Question(text=q['text'], quiz_id=history_quiz.id)
        db.session.add(question)
        db.session.commit()
        for a in q['answers']:
            answer = Answer(text=a['text'], is_correct=a['is_correct'], question_id=question.id)
            db.session.add(answer)
        db.session.commit()

    # Add Science Quiz
    science_quiz = Quiz(title='Science Quiz', category='science')
    db.session.add(science_quiz)
    db.session.commit()

    science_questions = [
        {
            'text': 'What is the chemical symbol for water?',
            'answers': [
                {'text': 'H2O', 'is_correct': True},
                {'text': 'O2', 'is_correct': False},
                {'text': 'CO2', 'is_correct': False},
                {'text': 'H2', 'is_correct': False}
            ]
        },
        {
            'text': 'What planet is known as the Red Planet?',
            'answers': [
                {'text': 'Mars', 'is_correct': True},
                {'text': 'Jupiter', 'is_correct': False},
                {'text': 'Saturn', 'is_correct': False},
                {'text': 'Venus', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the powerhouse of the cell?',
            'answers': [
                {'text': 'Mitochondria', 'is_correct': True},
                {'text': 'Nucleus', 'is_correct': False},
                {'text': 'Ribosome', 'is_correct': False},
                {'text': 'Chloroplast', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the speed of light?',
            'answers': [
                {'text': '299,792,458 meters per second', 'is_correct': True},
                {'text': '300,000,000 meters per second', 'is_correct': False},
                {'text': '150,000,000 meters per second', 'is_correct': False},
                {'text': '299,792,458 kilometers per hour', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the most abundant gas in Earth’s atmosphere?',
            'answers': [
                {'text': 'Nitrogen', 'is_correct': True},
                {'text': 'Oxygen', 'is_correct': False},
                {'text': 'Carbon Dioxide', 'is_correct': False},
                {'text': 'Hydrogen', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the hardest natural substance on Earth?',
            'answers': [
                {'text': 'Diamond', 'is_correct': True},
                {'text': 'Gold', 'is_correct': False},
                {'text': 'Iron', 'is_correct': False},
                {'text': 'Silver', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the main element found in the sun?',
            'answers': [
                {'text': 'Hydrogen', 'is_correct': True},
                {'text': 'Helium', 'is_correct': False},
                {'text': 'Oxygen', 'is_correct': False},
                {'text': 'Carbon', 'is_correct': False}
            ]
        },
        {
            'text': 'Who developed the theory of relativity?',
            'answers': [
                {'text': 'Albert Einstein', 'is_correct': True},
                {'text': 'Isaac Newton', 'is_correct': False},
                {'text': 'Niels Bohr', 'is_correct': False},
                {'text': 'Galileo Galilei', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the study of fungi called?',
            'answers': [
                {'text': 'Mycology', 'is_correct': True},
                {'text': 'Botany', 'is_correct': False},
                {'text': 'Zoology', 'is_correct': False},
                {'text': 'Ecology', 'is_correct': False}
            ]
        },
        {
            'text': 'What part of the brain controls balance and coordination?',
            'answers': [
                {'text': 'Cerebellum', 'is_correct': True},
                {'text': 'Cerebrum', 'is_correct': False},
                {'text': 'Brainstem', 'is_correct': False},
                {'text': 'Hypothalamus', 'is_correct': False}
            ]
        }
    ]

    for q in science_questions:
        question = Question(text=q['text'], quiz_id=science_quiz.id)
        db.session.add(question)
        db.session.commit()
        for a in q['answers']:
            answer = Answer(text=a['text'], is_correct=a['is_correct'], question_id=question.id)
            db.session.add(answer)
        db.session.commit()

    # Add Programming Quiz
    programming_quiz = Quiz(title='Programming Quiz', category='programming')
    db.session.add(programming_quiz)
    db.session.commit()
  
    programming_questions = [
        {
            'text': 'Which language is known as the backbone of web development?',
            'answers': [
                {'text': 'JavaScript', 'is_correct': True},
                {'text': 'Python', 'is_correct': False},
                {'text': 'Java', 'is_correct': False},
                {'text': 'C++', 'is_correct': False}
            ]
        },
        {
            'text': 'What does HTML stand for?',
            'answers': [
                {'text': 'HyperText Markup Language', 'is_correct': True},
                {'text': 'HyperText Makeup Language', 'is_correct': False},
                {'text': 'HighText Markup Language', 'is_correct': False},
                {'text': 'Hyperlink Markup Language', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the main purpose of a loop in programming?',
            'answers': [
                {'text': 'To repeat a block of code multiple times', 'is_correct': True},
                {'text': 'To define a new variable', 'is_correct': False},
                {'text': 'To create a new function', 'is_correct': False},
                {'text': 'To compare two values', 'is_correct': False}
            ]
        },
        {
            'text': 'Which data structure uses a "First In, First Out" (FIFO) principle?',
            'answers': [
                {'text': 'Queue', 'is_correct': True},
                {'text': 'Stack', 'is_correct': False},
                {'text': 'Array', 'is_correct': False},
                {'text': 'Tree', 'is_correct': False}
            ]
        },
        {
            'text': 'What does the != operator mean in most programming languages?',
            'answers': [
                {'text': 'Not equal to', 'is_correct': True},
                {'text': 'Equal to', 'is_correct': False},
                {'text': 'Less than', 'is_correct': False},
                {'text': 'Greater than', 'is_correct': False}
            ]
        },
        {
            'text': 'Which keyword is used to define a function in Python?',
            'answers': [
                {'text': 'def', 'is_correct': True},
                {'text': 'function', 'is_correct': False},
                {'text': 'func', 'is_correct': False},
                {'text': 'define', 'is_correct': False}
            ]
        },
        {
            'text': 'What does SQL stand for?',
            'answers': [
                {'text': 'Structured Query Language', 'is_correct': True},
                {'text': 'Simple Query Language', 'is_correct': False},
                {'text': 'Standard Query Language', 'is_correct': False},
                {'text': 'Sequential Query Language', 'is_correct': False}
            ]
        },
        {
            'text': 'In object-oriented programming, what is a class?',
            'answers': [
                {'text': 'A blueprint for creating objects', 'is_correct': True},
                {'text': 'A function that performs a specific task', 'is_correct': False},
                {'text': 'A variable that holds data', 'is_correct': False},
                {'text': 'A method to manage memory', 'is_correct': False}
            ]
        },
        {
            'text': 'Which of the following is a valid way to declare an array in Java?',
            'answers': [
                {'text': 'int[] array = new int[10];', 'is_correct': True},
                {'text': 'array<int> = new int[10];', 'is_correct': False},
                {'text': 'int array = new int[10];', 'is_correct': False},
                {'text': 'int array[10] = new int;', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the output of the following Python code: print("Hello " + "World")?',
            'answers': [
                {'text': 'Hello World', 'is_correct': True},
                {'text': 'HelloWorld', 'is_correct': False},
                {'text': 'Hello + World', 'is_correct': False},
                {'text': 'HelloWorld()', 'is_correct': False}
            ]
        }
    ]
    for q in programming_questions:
        question = Question(text=q['text'], quiz_id=programming_quiz.id)
        db.session.add(question)
        db.session.commit()
        for a in q['answers']:
            answer = Answer(text=a['text'], is_correct=a['is_correct'], question_id=question.id)
            db.session.add(answer)
        db.session.commit()

if __name__ == "__main__":
    add_quiz_data()
