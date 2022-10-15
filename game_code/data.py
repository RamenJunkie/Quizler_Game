import requests
from question_model import Question


def poll_api(num_qs, cat_id, skill):

    try:
        url = f"https://opentdb.com/api.php?amount={num_qs}&category={cat_id}&difficulty={skill}&type=boolean"
        #print(url)
        poll_data = requests.get(url=url)
        poll_data.raise_for_status()
        #print(poll_data.json()["results"])
        if poll_data.json()["results"] == []:
            return backup_data
        return poll_data.json()["results"]
    except:
        return backup_data


backup_data = [
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The HTML5 standard was published in 2014.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "&quot;Windows NT&quot; is a monolithic kernel.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "MacOS is based on Linux.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The open source program Redis is a relational database server.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "AMD created the first consumer 64-bit processor.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "hard",
     "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                      "question": "The Windows 7 operating system has six main editions.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first dual-core CPU was the Intel Pentium D.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linux was first created as an alternative to Windows XP.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "Android versions are named in alphabetical order.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "hard",
     "question": "The T-Mobile Sidekick smartphone is a re-branded version of the Danger Hiptop.",
     "correct_answer": "True", "incorrect_answers": ["False"]}]
