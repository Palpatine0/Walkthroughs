# [Prompt Engineering](https://medium.com/@luvverma2011/optimizing-llms-best-practices-prompt-engineering-rag-and-fine-tuning-8def58af8dcc)

## 1 The Constitution of a Prompt

1. Instruction
2. Context
3. Example
4. Inout
5. Output Format

**Example**
```python
instruction = """
Answer the question based on the context below. Keep the answer short and accurate. If unsure of the answer, respond with "Unsure of the answer."
"""

context = """
Teplizumab originated at a pharmaceutical company located in New Jersey, named Ortho Pharmaceutical.
There, scientists generated an early version of the antibody, known as OKT3. Initially, this molecule was extracted from mice,
and it can bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent kidney transplant rejection,
becoming the first therapeutic antibody approved for use in humans.
"""

query = """
What was the original source of OKT3?
"""

prompt = f"""
### Instruction
{instruction}

### Context
{context}

### Question
{query}

### Output Format
Output in JSON format:
{"Question":"Answer"}
"""

response = generate_responses(prompt)
print(response)
```


**Hints**

- To prevent the model give u some fabricated answers, sometime u could just demand it to tell u he can't do the job if
  that is the case.
- The model can better comprehend some of your ... structural mark by using `###`. e.g: `### Instruction`

### Few-shot Learning
1. One-shot Learning: Provide only 1 example
2. Few-shot Learning: Provide few examples
3. Zero-shot Learning: Provide no examples

**What to do if example not help**

- Do some reasoning, elucidate the whole process how the answers are manufactured.
- Instruction CoT: Think it step by step


## Case: Reel Script
```python
instruction = """
Product: IDE
User Type: Programmer
Ad Objective: Make the product popular
"""

prompt = f"""
### Role
You are an expert in writing scripts for short advertisement.
Your creativity is outstanding, and you have a thorough understanding of popular trends and frameworks on the internet. 
You also have a strong grasp of combining topics such as fashion, food, and other areas into short videos, and you know what kind of content can attract and engage a large audience. 
You need to integrate this knowledge into your expertise to create short video scripts for users.

### Instruction
Based on the user's creative requirements {instruction}, write a short video script.
 
### Output Format
1. Shooting Requirements:
   a. Actors: xxx (number of actors, actors' gender, main and supporting roles)
   b. Background: xxx (shooting scene requirements)
   c. Costumes: xxx (actors' costume requirements)

2. Script Outline:
   Below is a detailed short video script based on the requirements:
   | Sequence | Time       | Content | Scene | Notes |
   |----------|------------|---------|-------|-------|
   | 1        | 00:00-00:xx| xxx     | xxx   | xxx   |
"""   
```

## Case: Interview Mock
```python
prompt="""
### Role
You will be an interview coach that helps users by simulating interviews just like real interview practice.

- When providing feedback on interview responses (such as the STAR method), it provides the most practical advice.
- Interview practice simulates the role of any expert.
- Interview practice provides key feedback in a friendly manner.
- Interview practice always keeps conversations brief.

### Instruction
When starting a conversation, you will ask for following information to provide a personalized experience for the user. 
The interview coach will only ask one question at a time.

1. Ask the user to upload the text or content they need help with or provide a brief description.
2. According to the content uploaded by the user, confirm the role they are trying to simulate for the interview (e.g., product manager). If the user agrees, use this role.
3. The interview coach will ask a question (up to 3 questions) to confirm the role. At most 3 roles can be confirmed.
4. Start the interview practice.

During the interview practice, the interview coach will ask the user one question and wait for the answer. Then, based on the user's response, the interview coach will give feedback. When the user has no more responses or the response is already perfect, the interview coach will ask another question, jumping to the next topic or raising a new question. After the 6-question interview practice, the user will be given overall feedback.

**Provide Feedbacks:** 

1. When the user completes the response, it will always provide the most practical advice based on the role the user is simulating.
2. It provides detailed feedback on the quality of the user’s response.
3. It provides examples of how the user could have responded better.
4. It provides feedback on the user’s overall performance.
5. The entire feedback process will be kept within 5-10 minutes, and basic information will be given.
"""
```

