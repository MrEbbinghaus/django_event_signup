# EventShiftSchedule

This is a Django app to provide a simple shift schedule. E.g. for partys!
you _need_ to place this inside your Django project folder and configure it correctly!

## Installation
1.  Change to your Django project folder.
2.  If your project is in a git repository: `git submodule add https://github.com/MrOerni/django_event_signup`. If not. Just clone it!
3.  Add `django_event_signup` to your `INSTALLED_APPS` in `settings.py`.
4.  Add an url to `url.py`. E.g.: `url(r'^event-signup/', include("django_event_signup.urls", namespace='django_event_signup'))`.
5.  Install the requirements with `pip install -r requirements.txt`. Tipp: If you have a requirements file in your project folder, just add `-r django_event_signup/requirements.txt` to it!
6.  `makemigrations`, `migrate` as usual.
