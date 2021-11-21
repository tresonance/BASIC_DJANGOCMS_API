# 1-migrate cms_myblog.py 
    # python manage.py makemigrations cms_myblog
    >
          - Create model BlogConfig
          - Create model BlogConfigTranslation
    # python manage.py migrate cms_myblog
    >
        Applying cms_myblog.0001_initial... OK

# 2-migrate myblog 
    # python manage.py makemigrations myblog
    >
        - Create model BlogCategory
        - Create model Post
        - Create model LatestPostsPlugin
        - Create model GenericBlogPlugin
        - Create model AuthorEntriesPlugin
        - Create model PostTranslation
        - Create model BlogCategoryTranslation
    
    # python manage.py migrate cms_myblog
    >
        Applying myblog.0001_initial... OK