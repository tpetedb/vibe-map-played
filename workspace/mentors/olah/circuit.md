# Why my mail client thinks a message is spam

## What I looked at
I moved three messages to spam and three out of it, then watched which ones it
guessed right the next day. The sender domain seems to weigh more than the
words.

```mermaid
flowchart LR
  A[sender domain] --> D[score]
  B[words in subject] --> D
  C[did I reply before] --> D
  D --> E{over the line}
  E -->|yes| F[spam folder]
  E -->|no| G[inbox]
```
