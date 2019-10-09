import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from core.models import Category, Book

BASE_URL = 'http://books.toscrape.com/'


class Command(BaseCommand):
    help = 'Fetch the category and books data from the web'

    def handle(self, *args, **options):
        page = requests.get(BASE_URL+'index.html')
        soup_index = BeautifulSoup(page.text, 'html.parser')

        categories = soup_index.find(class_='nav nav-list').find(
            'ul').find_all('a')

        for c in categories:
            name = c.contents[0].strip()
            category, created = Category.objects.get_or_create(name=name)
            category_link = BASE_URL + c.get('href')
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category {name}')
                )

            page = requests.get(category_link)
            soup_category = BeautifulSoup(page.text, 'html.parser')
            has_next = True

            while(has_next):
                books = soup_category.find(
                    'ol', {'class': 'row'}).find_all('h3')
                for b in books:
                    book_link = b.find('a').get('href').replace(
                        '../../../', BASE_URL+'catalogue/'
                    )
                    page = requests.get(book_link)
                    soup = BeautifulSoup(page.text, 'html.parser')

                    description_div = soup.find(
                            'div', {"id": "product_description"}
                        )
                    product_description = None
                    if description_div:
                        product_description = description_div.findNext(
                            'p').contents[0].strip()

                    defaults = {
                        'category': category,
                        'title': soup.find('h1').contents[0].strip(),
                        'thumbnail_url': soup.find(
                            class_='carousel-inner').find(
                                'img'
                            ).get('src').replace('../../', BASE_URL),
                        'price': soup.find(
                            'p', {'class': 'price_color'}
                        ).contents[0].strip(),
                        'stock': 'In stock' in soup.find(
                            'th', text='Availability'
                        ).findNext('td').contents[0].strip(),
                        'product_description': product_description,
                        'upc': soup.find("th", text="UPC").findNext(
                            'td'
                        ).contents[0].strip(),
                    }

                    book, created = Book.objects.update_or_create(
                        upc=defaults['upc'],
                        defaults=defaults
                    )

                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'Created book {book.title}'
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'Updated book {book.title}'
                            )
                        )

                a_next = soup_category.find('a', text='next')
                has_next = a_next is not None
                if has_next:
                    link = category_link.replace(
                        'index.html',
                        a_next.get('href')
                    )
                    page = requests.get(link)
                    soup_category = BeautifulSoup(page.text, 'html.parser')
