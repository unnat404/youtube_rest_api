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
7. Visit http://127.0.0.1:8000/<endpoint> to view different end-points metioned below

# Test Endpoints

1. GET API for paginated response to query : http://127.0.0.1:8000/api/get_feed/
    ![image](https://user-images.githubusercontent.com/53619178/147278586-366f2872-5601-4649-b08f-a0b352b0bb67.png)
    
2. To view dashboard visit: http://127.0.0.1:8000/dashboard/
    ![image](https://user-images.githubusercontent.com/53619178/147278603-0d379663-9f80-4851-9543-3e7f691928e9.png)
    
3. To view top 9 responses of input search query visit: http://127.0.0.1:8000/search/  
    ![image](https://user-images.githubusercontent.com/53619178/147278622-a5786ec2-db0d-4aa3-a0f5-8cac4e8ce0d7.png)
    


