import re

class ReviewProcessor:
    """
    Base class for processing Goodreads reviews.
    Includes basic functionality for cleaning and preparing text.
    """
    def __init__(self, reviews):
        self.reviews = reviews

    def clean_review(self, text):
        return re.sub(r'[^\w\s]', '', text.lower())

    def clean_all_reviews(self):
        return [self.clean_review(review) for review in self.reviews]


class GenreClassifier(ReviewProcessor):
    """
    Inherited class for classifying book genres based on reviews.
    Extends ReviewProcessor with classification functionality.
    """
    def __init__(self, reviews, genres):
        super().__init__(reviews)
        self.genres = genres  

    def batch_generator(self, batch_size):
        """
        Generator function to yield batches of cleaned reviews and genres.
        """
        cleaned_reviews = self.clean_all_reviews()
        for i in range(0, len(cleaned_reviews), batch_size):
            yield cleaned_reviews[i:i + batch_size], self.genres[i:i + batch_size]


reviews = [
    "A brilliant story of love and resilience!",
    "Too slow-paced, but the characters are well-developed.",
    "Loved the magical realism! One of the best reads this year."
]

genres = ["Romance", "Drama", "Fantasy"]

classifier = GenreClassifier(reviews, genres)

batch_size = 2
for batch_reviews, batch_genres in classifier.batch_generator(batch_size):
    print("Batch Reviews:", batch_reviews)
    print("Batch Genres:", batch_genres)
