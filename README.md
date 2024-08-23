# FEFU-queries
Serivce for populating yandex forms with students' data. Created using the best architectural design patterns.
It's main goal is to reduce the number of incorrect data when surveying students
> [!IMPORTANT]  
> Currently project is under the construction and can change significantly
## General
Service provides authentication with Yandex ID

## Backend
Based on clean arcitecture with DDD and hexagonal arcitecture
### Stack
- litestar     API
- pydantic     Domain layer optimisation
- beanie ODM   MongoDB ODM

## Frontend
Provides UI for the awesome backend :)
### Stack
- React        Client rendering
