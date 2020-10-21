{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "base_url = \"https://api.yelp.com/v3/businesses/search?\"\n",
    "word = \"restaurants\"\n",
    "lat = 1\n",
    "lng = 2\n",
    "API_KEY = \"sss\"\n",
    "query_url = f\"{base_url}accessToken={API_KEY}&term={word}&latidude={lat}&longitude={lng}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://api.yelp.com/v3/businesses/search?accessToken=sss&term=restaurants&latidude=1&longitude=2\n"
     ]
    }
   ],
   "source": [
    "print(query_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
