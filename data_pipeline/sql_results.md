## QUERY 1 — Books with rating 4 or higher

### SQL Query

```sql
SELECT title, rating, price_gbp
FROM books
WHERE rating >= 4;
```

### Output

```text
('Sharp Objects', 4, 47.82)
('Sapiens: A Brief History of Humankind', 5, 54.23)
('The Dirty Little Secrets of Getting Your Dream Job', 4, 33.34)
('The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 4, 22.6)
("Shakespeare's Sonnets", 4, 20.66)
('Set Me Free', 5, 17.46)
("Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 5, 52.29)
('Rip it Up and Start Again', 5, 35.02)
('Chase Me (Paris Nights #2)', 5, 25.27)
('Black Dust', 5, 34.53)
('Worlds Elsewhere: Journeys Around Shakespeareâ\x80\x99s Globe', 5, 40.3)
('Wall and Piece', 4, 44.18)
('The Four Agreements: A Practical Guide to Personal Freedom', 5, 17.66)
('The Elephant Tree', 5, 23.82)
("Sophie's World", 5, 15.94)
('Behind Closed Doors', 4, 52.22)
('Private Paris (Private #10)', 5, 47.61)
('#HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.', 5, 23.11)
('We Love You, Charlie Freeman', 5, 50.27)
('Untitled Collection: Sabbath Poems 2014', 4, 14.27)
('Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness', 4, 44.18)
('This One Summer', 4, 19.49)
('Thirst', 5, 17.27)
('The Past Never Ends', 4, 56.5)
('The Nameless City (The Nameless City #1)', 4, 38.16)
("The Most Perfect Thing: Inside (and Outside) a Bird's Egg", 4, 42.96)
('The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy', 4, 23.89)
('The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer', 5, 20.59)
('The Death of Humanity: and the Case for Life', 4, 58.11)
("The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution", 5, 32.24)
('Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up', 4, 41.83)
('Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)', 5, 13.61)
('Princess Between Worlds (Wide-Awake Princess #5)', 5, 13.34)
('Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)', 4, 15.44)
('Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed', 4, 14.02)
('Join', 5, 35.67)
('In the Country We Love: My Family Divided', 4, 22.0)
```

## QUERY 2 — 10 Most Expensive Books

### SQL Query

```sql
SELECT title, price_gbp
FROM books
ORDER BY price_gbp DESC
LIMIT 10;
```

### Output

```text
('The Death of Humanity: and the Case for Life', 58.11)
('Slow States of Collapse: Poems', 57.31)
('Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 57.25)
('The Past Never Ends', 56.5)
('The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!', 56.41)
('Masks and Shadows', 56.4)
('The Secret of Dreadwillow Carse', 56.13)
('The Electric Pencil: Drawings from Inside State Hospital No. 3', 56.06)
('Birdsong: A Story in Pictures', 54.64)
('Sapiens: A Brief History of Humankind', 54.23)
```

## QUERY 3 — Selected Categories

### SQL Query

```sql
SELECT DISTINCT c.category_name
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
WHERE c.category_name IN ('Poetry', 'Fiction', 'Mystery');
```

### Output

```text
('Fiction',)
('Mystery',)
('Poetry',)
```

## QUERY 4 — Books priced between £20 and £40

### SQL Query

```sql
SELECT title, price_gbp, rating
FROM books
WHERE price_gbp BETWEEN 20 AND 40
ORDER BY price_gbp;
```

### Output

```text
('The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer', 20.59, 5)
("Shakespeare's Sonnets", 20.66, 4)
('In the Country We Love: My Family Divided', 22.0, 4)
("America's Cradle of Quarterbacks: Western Pennsylvania's Football Factory from Johnny Unitas to Joe Montana", 22.5, 3)
('The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 22.6, 4)
('The Requiem Red', 22.65, 1)
('#HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.', 23.11, 5)
('The Elephant Tree', 23.82, 5)
('Olio', 23.88, 1)
('The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy', 23.89, 4)
('Saga, Volume 6 (Saga (Collected Editions) #6)', 25.02, 3)
('Chase Me (Paris Nights #2)', 25.27, 5)
('Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink', 25.52, 1)
('Reasons to Stay Alive', 26.41, 2)
('Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More', 30.52, 3)
('The Five Love Languages: How to Express Heartfelt Commitment to Your Mate', 31.05, 3)
('Throwing Rocks at the Google Bus: How Growth Became the Enemy of Prosperity', 31.12, 3)
('When We Collided', 31.77, 1)
("The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution", 32.24, 5)
('Penny Maybe', 33.29, 3)
('The Dirty Little Secrets of Getting Your Dream Job', 33.34, 4)
('My Paris Kitchen: Recipes and Stories', 33.37, 2)
("You can't bury them all: Poems", 33.63, 2)
('Black Dust', 34.53, 5)
('Rip it Up and Start Again', 35.02, 5)
('Join', 35.67, 5)
('Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics', 36.28, 2)
('The Bear and the Piano', 36.89, 1)
('The Gutsy Girl: Escapades for Your Life of Epic Adventure', 37.13, 1)
('How Music Works', 37.32, 2)
('Mesaerion: The Best Science Fiction Stories 1800-1849', 37.59, 1)
('The Nameless City (The Nameless City #1)', 38.16, 4)
('Security', 39.25, 2)
('Soul Reader', 39.58, 2)
```

## QUERY 5 — Top 10 Highly Rated Books with Categories

### SQL Query

```sql
SELECT
    b.title,
    c.category_name,
    b.rating,
    b.price_gbp
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
WHERE b.rating >= 4
ORDER BY b.rating DESC, b.price_gbp DESC
LIMIT 10;
```

### Output

```text
('Sapiens: A Brief History of Humankind', 'History', 5, 54.23)
("Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'Sequential Art', 5, 52.29)
('We Love You, Charlie Freeman', 'Fiction', 5, 50.27)
('Private Paris (Private #10)', 'Fiction', 5, 47.61)
('Worlds Elsewhere: Journeys Around Shakespeareâ\x80\x99s Globe', 'Nonfiction', 5, 40.3)
('Join', 'Science Fiction', 5, 35.67)
('Rip it Up and Start Again', 'Music', 5, 35.02)
('Black Dust', 'Romance', 5, 34.53)
("The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution", 'Spirituality', 5, 32.24)
('Chase Me (Paris Nights #2)', 'Romance', 5, 25.27)
```

