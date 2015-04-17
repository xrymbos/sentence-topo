Topologically sorting Alice in Wonderland
=========================================

Recently my brother told me about Duolingo, which he's using to learn Swedish. I don't have the motivation or
persistence to actually learn languages but I'm kind of fascinated by the process.

http://www.antimoon.com/how/readwhat.htm recommends reading/watching "i+1" input to introduce new words and concepts
gradually.  I was kind of curious about this idea: what would happen if you created, say, a flashcard deck of sentences
gradually increasing in difficulty, each adding only one or two new words? What kind of sentences would you be able to
understand after going through, say, 1000 of these flashcards? I wrote a small program to find out.

The program is very simple and dumb: it repeatedly takes the sentence with the fewest new words. I ran it on Alice in Wonderland, which according to my programs somewhat dodgy counting has about 1352 sentences.

The first few sentences it spits out are duplicates: 'Well', 'Well!', 'Down, down, down', etc.

After introducing 0, 1, or 2 new words per sentence, when we get to the 100th sentence we're up to things like '"Of
course you don't!"'  and '"I don't know what you mean," said Alice.'

Skip along to the 500th sentence, and we can understand 'Where did they draw the treacle from?'.

When we get to the 100th sentence, we start getting to reasonably complex constructions such as 'As she said this, she
looked up, and there was the Cat again, sitting on the branch of a tree.' and '"You might just as well say," added the
March Hare, "that 'I like what I get' is the same thing as 'I get what I like'!"'

We also start getting a few sentences 'for free' around here as well: once we learn the phrase 'March Hare' we get a
whole slew of sentences involving the March Hare using only words that are in previous sentences.

We're forced to add a whopping 3 new words at sentence #1187: 'The rabbit-hole went straight on like a tunnel for some
way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she
found herself falling down what seemed to be a very deep well.'

There's also a deceptively short sentence with 3 new words: '"Please, Ma'am, is this New Zealand or Australia?"'

The long, rambling sentences are the last to go. The last sentence in the list adds 11 words and is near the end of the book as well:

'So she sat on with closed eyes, and half believed herself in Wonderland, though she knew she had but to open them
again, and all would change to dull reality--the grass would be only rustling in the wind, and the pool rippling to the
waving of the reeds--the rattling teacups would change to the tinkling sheep-bells, and the Queen's shrill cries to the
voice of the shepherd boy--and the sneeze of the baby, the shriek of the Gryphon, and all the other queer noises, would
change (she knew) to the confused clamour of the busy farm-yard--while the lowing of the cattle in the distance would
take the place of the Mock Turtle's heavy sobs.'

Anyway, I found this interesting, if not necessarily useful.
