## Commerce
Project 2 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` https://www.youtube.com/watch?v=Qnhv8x9NEZI

### Overview:
An e-commerce auction site which allows users to post listings, place bids, comment, and add listings to a watchlist.

### Specifications:
Built with `Python`, `Django`, `HTML/CSS`, `Bootstrap`, and `SQLite`.

The site also makes use of [Django's](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) humanize template filters, `intcomma` and `naturaltime`.

### To Run:
1. Pip install `Django`
2. In the terminal, cd into the commerce directory.
3. Run `python3 manage.py makemigrations commerce` to make migrations for the commerce app.
4. Run `python3 manage.py migrate` to apply migrations to the database.
5. Run `python3 manage.py runserver` to start the Django web server and visit the website in the browser.

-----

## New Listing: 
Users can create a new listing, specify a `title`, `description`, `price`, `imageURL`, and `category`.

<img width="1115" alt="Screen Shot 2023-01-20 at 4 54 58 PM" src="https://user-images.githubusercontent.com/105305546/213812951-e75f8063-9b75-4095-b8de-96515bc4d2de.png">

## Categories:
Users can choose from a list of `alphabatized` categories: `Art`, `Books`, `Clothing`, `Electronics`, `Food`, and `Other` by clicking on the name of a category it takes the user to said category page.

<img width="1136" alt="Screen Shot 2023-01-20 at 4 54 04 PM" src="https://user-images.githubusercontent.com/105305546/213812479-10a6ce92-8f41-4161-905f-ebfd73317b0e.png">
 
## Active Listings:
The default route allows users to view all current active listings displaying: `title`, `description`, `current price`, and `photo`. If the user clicks on `Details` of a given listing, it will diplay more information per that listing such as: `number of bids`, `last bid made`,`number of watchers`, `comments`, and `number of comments`.

<img width="1117" alt="Screen Shot 2023-01-20 at 4 54 33 PM" src="https://user-images.githubusercontent.com/105305546/213812787-72420e92-872d-4304-8b12-a0c927e3b155.png">

## Watchlist:
Users can add listings to their Watchlist page, which displays all of the listings a user has added to their watchlist.

<img width="1120" alt="Screen Shot 2023-01-20 at 4 55 13 PM" src="https://user-images.githubusercontent.com/105305546/213812584-2e7c7ad0-bb12-41a2-a83e-888300d6a790.png">

## Close Auction:
If the user is the owner of the auction, they can close the auction, the winning bid price is displayed, and the user who won the auction will be notified they won the auction.

<img width="1073" alt="Screen Shot 2023-01-22 at 11 32 20 AM" src="https://user-images.githubusercontent.com/105305546/213927383-98e1fe90-3668-4b5b-aadb-76af06fa07ac.png">

## Closed Listings:
Closed listings showcases the winner of each closed auction and the details therein.

<img width="1018" alt="Screen Shot 2023-01-22 at 12 14 09 PM" src="https://user-images.githubusercontent.com/105305546/213929930-bf1f604b-ea6f-483e-8e5a-b04d1d8fe923.png">

## Data Models:
Using `Django Admin` and `SQLite3` as the backend, the Python models are rendered to the Django framework `alphabetically` as `Bids`, `Categorys`, `Comments`, `Listings`, `Users`.

<img width="1216" alt="Screen Shot 2023-01-20 at 5 51 41 PM" src="https://user-images.githubusercontent.com/105305546/213819568-4f5410cd-9a4d-4dc1-b6fb-18707ca38ac8.png">


But seriously whole stole... [BOY WITH APPLE 🍏](https://www.youtube.com/watch?v=dGH8ZbD6U2o)?
