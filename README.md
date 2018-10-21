# Organizer

To organize my questioning, answering, musing, and listing

# To Do

## Questions
- unit tests
- clean up base.css
- /question/id
    - can save new resources, musings, and answers
    - can edit old history items in main editor
    - add necessary fields to model
    - make history sortable by type and ranking
    - add question creation date
- /archive
- /home
- /create
- /stats
- clean up css

## Books
- base
- /books/id
- /archive
- /home
- /create
- /stats

## Fun Facts
- base
- /facts/id
- /archive
- /home
- /create
- /stats

## Topics
- base
- /topic/id
- /archive
- /home
- /create
- /stats

# Main Objects

- Questions
- Fun Facts
- Books
- Topics

# Supporting Objects
- Question Resources
- Question Musings
- Question Answers
- Topic Resources
- Book Reviews
- Topic Explanations

-------

## 1. Questions
    Contains
    - created_at (datetime)
    - updated_at (datetime): latest updated_at of strongly connected object
    - attributed_to (string)
    - question (html)
    - num_views (int, default=0)
    - rating (int, default=0)

    Notes
    - can only edit rating
    - updated_at is only updatble by code
    - strongly connected objects: question_resources, question_musings, question_answers

- ### 1a. Question Resources
        Contains:
        - created_at (datetime)
        - updated_at (datetime)
        - title (string)
        - resource_url (string, nullable)
        - resource_images (array[string], nullable): file paths
        - resource_other (html, nullable)
        - notes (html, nullable)

        Notes
        - one of resource_url, resource_image, or resource_other must be non null

- ### 1b. Question Musings
        Contains:
        - created_at (datetime)
        - updated_at (datetime)
        - text (html)

- ### 1c. Question Answers
        Contains:
        - created_at (datetime)
        - update_at (datetime)
        - text (html)

---------

## 2. Fun Facts
    Contains
    - created_at (datetime)
    - updated_at (datetime)
    - veractiy_status (boolean, default=true)
    - fact (html)
    - justification (html, nullable)
    - resource (text, nullable)
    - rating (int, default=0)
    - views (int, default=0)

----------

## 3. Books
    Contains
    - created_at (datetime)
    - updated_at (datetime)
    - author (string)
    - title (string)
    - url (string, nullable)
    - status (string, category): to-read, read, reading
    - rating (int, default=0)
    - views (int, default=0)
    - review (html, nullable)

    Notes
    - note is html that has sections: notes, questions/answers, quotes
    - strongly connected objects: book_reviews

- ### 3a. Book Review
        Contains:
        - created_at (datetime)
        - updated_at (datetime)
        - text (html)

-------

## 4. Topics
    Contains
    - created_at (datetime)
    - updated_at (datetime)
    - title (string)
    - review (html, nullable)
    - rating (int, default=0)
    - views (int, default=0)

    Notes
    - strongly connected objects: topic_explanations

- ### 4a. Topic Explanations
        Contains:
        - created_at (datetime)
        - updated_at (datetime)
        - resource (string)
        - text (html)