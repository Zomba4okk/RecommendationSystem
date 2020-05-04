# RecommendationSystem
Recommendation system for based on products rating.

## To configure project
### Set DB URI
Set *sqlalchemy.url* param in ```alembic.ini```

Set *SQLALCHEMY_DATABASE_URI * param in ```config/config.py```
### Install requirements
```pip install -r requirements.txt```

### Apply migrations
```alembic upgrade head```

## To generate test data
```python data_generator.py```

## To generate recomendations:
```python presentation.py```
