# CvCvCv

A run-it-locally Django app to manage CVs

## Tech

- my standard AI-fed "local Django CMS" approach

## Structure

- `cvcvcv` is the default app that does essentially nothing
- `cv` is where the actual magic happens, and has a classic Django folders+files structure.

- We are loading Tailwind and Daisy via CDN, because this is personal, locally-run software anyways
- Happily using `sqlite` for the same reason

### Running It

- make a `venv`
- `pip install -r requirements`
- (you may wanna run `python manage.py migrate`)
- `python manage.py runserver`