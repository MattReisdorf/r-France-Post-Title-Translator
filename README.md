# r/France-Post-Title-Translator

Python script to translate non-English posts on Reddit. Defaults to r/France because I'm trying to keep my literacy, but works for any non-English sub. 

Utilizes PRAW, so a dev account on reddit is needed, and a non-affiliated version of Google Translate API. 

You can change the desired subreddit in line 33. For example, changing "France" to "de" will translate post titles in the main German-speaking subreddit. 

sub.new in line 36 can be changed to sub.("hot", "rising", "controversial", or "top") for different posts.
  sub.top and sub.controversial can have the time frame changed by following the PRAW Documentation
  
 
