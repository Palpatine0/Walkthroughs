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

1. LLM may sometime failed to do the searching work. For some fields like medical or financial, this is very fatal
2. LLM may comprehend the context incorrect
3. Some inquiries may too complex so LLM can’t solve it correctly

### Trunks partition

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