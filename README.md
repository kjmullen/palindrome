## Normal Mode

You must write a program that can take a string and return a boolean depending on if it is a palindrome or not.  As a reminder a palindrome is a string that has the same letters forwards and backwords.  These strings can be a word, a phrase, a sentence or even multiple sentences.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

* stunt nuts
* Lisa Bonet ate no basil.
* A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
* Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

You must implement this using a recursion and strip out non letters using `re.sub`.

## Hard Mode

* Make both an iterative and recursive version of your palindrome test function.
* Add simple file logging into the palindrome.  Log out at INFO level the time, phrase and if it was a palindrome.

## Additional Resources

* [Palindrome list](http://www.palindromelist.net/).
* [Logging Tutorial](https://docs.python.org/3/howto/logging.html)
* [Regular expression operations](https://docs.python.org/3/library/re.html).
