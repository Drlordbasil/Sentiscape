import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class ProductReviewScraper:
    def __init__(self):
        self.reviews = []

    def scrape_reviews(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        review_elements = soup.find_all('div', class_='review')

        for review_element in review_elements:
            review = review_element.text.strip()
            self.reviews.append(review)

    def analyze_sentiment(self):
        sentiments = []

        for review in self.reviews:
            testimonial = TextBlob(review)
            sentiment = testimonial.sentiment.polarity
            sentiments.append(sentiment)

        return sentiments

    def generate_word_cloud(self):
        reviews_text = " ".join(self.reviews)
        wordcloud = WordCloud().generate(reviews_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def run(self):
        product_url = input("Enter the URL of the product page: ")
        self.scrape_reviews(product_url)

        print(f"Scraped {len(self.reviews)} reviews")

        sentiments = self.analyze_sentiment()
        positive_reviews = sum([1 for sentiment in sentiments if sentiment > 0])
        negative_reviews = sum([1 for sentiment in sentiments if sentiment < 0])
        neutral_reviews = sum([1 for sentiment in sentiments if sentiment == 0])

        print(f"Positive Reviews: {positive_reviews}")
        print(f"Negative Reviews: {negative_reviews}")
        print(f"Neutral Reviews: {neutral_reviews}")

        self.generate_word_cloud()


review_scraper = ProductReviewScraper()
review_scraper.run()