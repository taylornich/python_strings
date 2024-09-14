# question 1 task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "bad", "excellent", "poor", "average"]

def keyword_highlighter(reviews, keywords):
    for review in reviews:
        new_review = review
        for keyword in keywords:

            keyword_lower = keyword.lower()
            keyword_upper = keyword.upper()

            if keyword_lower in new_review.lower():
                new_review = review.replace(keyword, keyword_upper)

        print(new_review)


keyword_highlighter(reviews, keywords)


# question 1 task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def review_summary(reviews, positive_words, negative_words):

    pos_count = 0
    neg_count = 0

    for review in reviews:
        words = review.lower().split()

        for word in words:
            if word in positive_words:
                pos_count += 1
            elif word in negative_words:
                neg_count += 1
        
    print(f"There are {pos_count} positive words in the reviews.")
    print(f"There are {neg_count} negative words in the reviews.")

review_summary(reviews, positive_words, negative_words)


# question 1 task 3

def review_summary(reviews):

    summaries = []
    for review in reviews:
        summary = review[:30]

        if len(review) > 30:
            summary += '...'

        summaries.append(summary)

    print(summaries)

review_summary(reviews)