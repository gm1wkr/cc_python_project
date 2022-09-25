# CodeClan Python Project Week 5
## Solo project 6 days.

![wireframe-python_project-dashboard](https://user-images.githubusercontent.com/6051686/192164402-d24ae942-2061-4db0-a3c8-44e616796383.png)

## The Brief

<blockquote>
Build an app to track someone's travel adventures.

## MVP

- The app should allow the user to track `Country`s and `City`s they want to visit and those they have visited.
- The user should be able to create and edit `Country`s.
- Each `Country` should have one or more `City`s to visit.
- The user should be able to create and delete `City`s.
- The app should allow the user to mark destinations as visited or not.

## Inspired By

Lonely Planet, Atlas Obscura

## Possible Extensions

- Add sights to see at the destination `City`s.
- Be able to filter `City`s based on whether they have been visited.
- Allow the user to search for a destination by city name, region, or continent
</blockquote>
  
In addition to the above, I also included the ability for the user to create 'Notes' to annotate travel destinations before, during or after their trip.

During this project I also took the oppertunity to become more fluent with CSS3.
  
  
## The Stack

The brief required a full stack application written using Python and the Flask framework and Jinja2 Templates.  The database is PostgreSQL connected to python with the psycopg2 library. 
<br>    
<br>
<div align="center" style="background-color: #ddd">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" alt="Python" width="80" height="80"/>&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"  width="80" height="80" />&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"  width="80" height="80" /> &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="80" height="80"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="80" height="80"/>&nbsp;
</div>
<br>
<br>

## The Process

The process began with planning using wireframes to get some idea of where the app was heading.  Class diagrams and user journeys were then completed.  Being over eager I did not plan this project as diligently as I could and this became one of the major learning points of the project.

Database tables and models followed.

## What I learned

While making some planning efforts I could have done better.  I learned that it is very difficult to code something that is not known.

As the first CodeClan project the learning points are too numerous to mention so here are but a few ...
- Managing a project
- Workflows & Git
- Importance of planning database tables and python models in detail
- Complex CSS / pretty front-end is difficult to balance while maintaining accessibility.
- Time management and estimating time needed (estimates are always wrong, double them twice :smirk: )

## What I would do Differently

### Front End
I would take more time to plan out a responsive and accessible front end and also organise my CSS.  The CSS does not properly leverage the cascade and started to become very messy during late night sessions!  A solution may have been to use postCSS or SASS to keep the CSS organised and reusable.  The templates are not responsive enough, the layout breaks at about 800px.  

### Back End
The back end went together quite easily due to the time spent planning the models and repositories.  Implementing the repositories was uncomfortable at times, largely due to inexperience and not understanding which part of the stack was generating an error (the database, connector or flask).

## Conclusion
This was a 6 day project and I feel I accomplished and learned a great deal.  I really enjoyed the journey from the back end engineering to making the front end usable with hopefully a dash of flair.  

This project was an enjoyable and meaningful milestone in my journey to becoming a developer.



