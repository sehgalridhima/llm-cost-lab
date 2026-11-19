# llm-cost-lab
## What is this
I performed these experiments to determine what increases expenses while using AI and how to minimise them.
## What I found
- On performing this experiment, I found out that Hinglish/Hindi texts use 2.1X(tested on 1 sentence) more tokens as compared to English texts. This is because LLMs are mostly trained on English text and when they come across difficult Hindi words, they tend to break those words down into parts which ends up using more tokens.
- AI does not remember earlier messages, so the app resends the whole chat history every time. In my test, a 30-message chat used about 15.5× more tokens than the same 30 messages sent without history.
