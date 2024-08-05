# Document Partition and Similarity Analysis

**Challenges in LLM practices in commercial scenarios**

- Performance
- Privacy
- Hallucination

A controllable generation is required, we cant afford LLM make any mistake.

## RAG

1. gather info

   To perform a RAG, u need to first prepare some documents that contains the information the LLM need to know.

2. partitioning

   Cut the whole documents to many chunks, since it’s gonna take too long to read the whole article just for a short
   lines in it,

   These chucks can be found a lot faster after storing in vector databases, where similar content be storing together.

   When there’s a question sent, the answer will be found based on the similarity of data with the tokens in question

### Hallucination

Ask the model to return answers only from the designated context, this can largely solve the problem anyway but not
entirely
Here’s the reason:

1. LLM may sometime fail to do the searching work. For some fields like medical or financial, this is very fatal
2. LLM may comprehend the context incorrect
3. Some inquiries may too complex so LLM can’t solve it correctly

### Trunks partitioning

1. **Divide by sentence**

2. **Divide by char**
   Some word may be incomplete, may miss some letters or parts.
   For example if size is 13, the result will be like "Recording wor"

3. **Overlapping size divide**

   Still divides by character , by configures overlapping window so the words won’t be cut out when designated size is
   reached but keep recording until the whole word is recorded

4. **Recursive character text splitting**

   The most popular approach, the combination of 2 approaches above, but will also takes the context into account when
   doing partitioning

## Vectorization

### Vectorize the chunks

Using encoder to vectorize the chunks

### Vector similarity

Assume we have 3 vectors A(1,2), B(1.2, 1.8), C(2, 1)

<img height=100 src="https://i.imghippo.com/files/U77nl1722778756.jpg" alt="" border="0">

We could draw the conclusion that the similarity between A and B, like `sim(A,B)` is bigger than `sim(B,C)` and `sim(A,C)`.
The angle between A and B is smaller, making a higher similarity between them.

#### Cosine Similarity 
Assume we have 2 3D vectors, `a(a1, a2, a3)` `b(b1, b2, b3)`. The cosine similarity between them is 
```python
def cosine_sim(A, B):
    dot_product = np.dot(A, B)
    normA = np.linalg, norm(A)
    normB = np.linalg, norm(B)
    return dot_product / (normA * normB)
```