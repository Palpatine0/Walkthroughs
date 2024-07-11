# Python

## Task 1: Completion of the Function `wordcount`  

**Code**

```python
text = """
Got this panda plush toy for my daughter's birthday, 
who loves it and takes it everywhere. It's soft and 
super cute, and its face has a friendly look. It's 
a bit small for what I paid though. I think there 
might be other options that are bigger for the 
same price. It arrived a day earlier than expected, 
so I got to play with it myself before I gave it 
to her.
"""


def wordcount(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    words = text.split()
    cleaned_words = []

    # Remove punctuation from words
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word:
            cleaned_words.append(cleaned_word)

    # Count the occurrences of each word
    word_counts = {}
    for word in cleaned_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


result = wordcount(text)

# Format the result in a vertical list
formatted_result = "{\n"
for word, count in result.items():
    formatted_result += f"  '{word}': {count},\n"
formatted_result = formatted_result.rstrip(",\n") + "\n}"

print(formatted_result)
```

**Result**

<img src="https://i.imghippo.com/files/ER1Yt1720718584.jpg" alt="" border="0">

```python
{'got': 2, 'this': 1, 'panda': 1, 'plush': 1, 'toy': 1, 'for': 3, 'my': 1, 'daughters': 1, 'birthday': 1, 'who': 1, 'loves': 1, 'it': 5, 'and': 3, 'takes': 1, 'everywhere': 1, 'its': 3, 'soft': 1, 'super': 1, 'cute': 1, 'face': 1, 'has': 1, 'a': 3, 'friendly': 1, 'look': 1, 'bit': 1, 'small': 1, 'what': 1, 'i': 4, 'paid': 1, 'though': 1, 'think': 1, 'there': 1, 'might': 1, 'be': 1, 'other': 1, 'options': 1, 'that': 1, 'are': 1, 'bigger': 1, 'the': 1, 'same': 1, 'price': 1, 'arrived': 1, 'day': 1, 'earlier': 1, 'than': 1, 'expected': 1, 'so': 1, 'to': 2, 'play': 1, 'with': 1, 'myself': 1, 'before': 1, 'gave': 1, 'her': 1}
```

## Task 2: Debug Note (PyCharm)


### Debugging Steps (PyCharm)

1. **Open PyCharm and Load Your Project**:
   
   Launch PyCharm and open your project and open the Python file containing your script.

2. **Set Breakpoints**:
   
   Click in the left margin next to the line numbers to set breakpoints.
   
   Suggested breakpoints:
     - `text = text.lower()`
     - `words = text.split()`
     - `for word in words:`
     - `if cleaned_word:`
     - `if word in word_counts:`

   <img src="https://i.imghippo.com/files/eOEjK1720719048.jpg" alt="" border="0">

3. **Start Debugging**:

    Click the debug button to start the script in debug mode.  
   
   <img height="35" src="https://i.imghippo.com/files/fMScV1720719231.jpg" alt="" border="0">
   

4. **Step Through the Code**:

    When the debugger stops at the first breakpoint, use the following buttons to step through the code:
     - **Step Over (F8)**: Execute the current line and move to the next line.
     - **Step Into (F7)**: Enter into the function or method call.
     - **Step Out (Shift+F8)**: Step out of the current function or method.
     - **Resume Program (F9)**: Continue execution until the next breakpoint.
   
   <img height="35" src="https://i.imghippo.com/files/uJyok1720719393.jpg" alt="" border="0">

5. **Inspect Variables**:
   
   While the code is paused at a breakpoint, hover over variables to see their values. Use the Variables pane (usually at the bottom left) to inspect the values of all current variables.

   <img src="https://i.imghippo.com/files/Ilgdd1720720021.jpg" alt="" border="0">

 