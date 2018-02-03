# sentiment-analysis
an online sentiment analyzer trained on standard IMDB dataset that can classify sentiments based on emoticons as well.

online link
http://jaydeepthik.pythonanywhere.com/
(use a single negative (eg "bad" in place of "not good") instead of negating)

# structure
the parent folder should contain the IMDB dataset that will be loaded using the load.py script into a csv file

the driver.py is the trainer code for training the sentiment analizer

store.py pickels the weights (classifier)
