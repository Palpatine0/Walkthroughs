# LLM Training and development

## 2 Generating Process

<div align="center"><img  height="200px" src="https://i.imghippo.com/files/cc2vN1720566536.jpg" alt="" border="0"></div>

## 3 Training Process

### Case

A financial tech company needs LLM to replace their insurance customer service program

### Solution A: Implementing ChatGPT

<div align="center"><img height="200px" src="https://i.imghippo.com/files/QcNvO1720837391.jpg" alt="" border="0"></div>

The application sends custom prompts to CharGPT. With RAG setting, we can build a custom memory that includes some
company documents for users, like product info, FAQs. For a higher security purpose, the answers from CharGPT can only
be based on the custom memory

### Solution B: Train a private model

#### Step 1: Model Pre-train

**Model Design**

- 1 Size

  ~1B

- 2 Architecture

- 3 Tokenizer

  Insurance field tokens

**Clarify Using Scenarios**

- Model performance

  This model should know everything related with insurance, etc.

**Benchmark**

**Data Design**

- Data type

  Vertical data like economic data, insurance data and general data.

- Data quantity

  200B-500B token

- Data ratio

  Different percentage for different types of data or data source. General data should have slightly lager scale.

**Data Sanitize**

- Repeated data

- Punctuations

**Data Injection**

- Provide these data u collect to the model, then u got a pre-trained model.

##### BASE MODEL COMPLETE

Your model now should be able to guess out what is the next token when u give it a token.
But it's not for conversation.

Consider it like a new grad, it simply has the basic knowledge, but it know nothing about how to work.

#### Step 2: Fine-tuning

**Instruction Data**

- Provide model with some instruction data, which is some conversation examples.
  The input as question and output as answer the model should learn.

- These data needs to cover a vast range of real case scenarios. So these data need to have a higher diversity.

##### CHECK MODEL COMPLETE

- The model is now ready for conversation. Like a trained service will all knowledge he need to know about how to please
  its client.

#### Step 3: Alignment

**Hallucination and Safeness**

- The model make respond something unwanted, of might give out some inappropriate answer.

- So u need to give it some rules. 



