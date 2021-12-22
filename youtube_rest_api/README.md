# YouTube API 
API to fetch YouTube's most recently published videos for a pre-define search query (/tag) in a paginated response.

# Project Features:
    • Updating database asynchronously (using django-background-tasks) with Youtube APIs to fetch latest videos
    • Indexing Database for faster search and sort queries
    • Dashboard to view synced database with searching and sorting functionalities
    • Multiple API keys support (to overcome quota exhaustion)

# Setup and Run Locally:
1. Clone the repo
2. Set up a virtual environment with requiements.txt
3. Change directory to:  youtube-api\youtube_rest_api
4. Create superuser (optional) 
    `python manage.py createsuperuser `
5. Make migrations and migrate to setup database :
    ` python manage.py makemigrations` 
    `python manage.py migrate `
6. Run the following commands in 2 separate terminals:
    ` python manage.py process_tasks `
    ` python manage.py runserver `
7. Visit http://127.0.0.1:8000/ to view the dashboard
