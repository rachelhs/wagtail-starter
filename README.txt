To install requirements
- pip3 install -r requirements.txt

To activate local enviroment
- source wagtail_env/bin/activate

To run on local host 8000 (http://localhost:8000/admin and http://localhost:8000)
- python3 manage.py runserver

##############################################################################################

To add a section to the editable CMS admin
- in models.py choose a type of field and a name for each section and add it to content_panels

class HomePage(Page):
    project_name = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('project_name', classname="full")
    ]

- run python3 manage.py makemigrations
- run python3 manage.py migrate

- in the corresponding html file, access the section with {{ self.project_name }} where project_name is the name chosen above
- classname="full" refers to how box appears in the admin screen


##############################################################################################

Folder Structure is important

eg. for the home site templates must be in home/templates/home and static assets in home/static/home

##############################################################################################

Supported formats: GIF, JPEG, PNG, WEBP. Maximum filesize: 10.0 MB.

##############################################################################################

Need to do a hard reload to see css changes (ctrl + F5 in browserr)

##############################################################################################

Square image as title image

##############################################################################################
Site based on Freelancer, a free to use, MIT licensed Bootstrap theme created by Start Bootstrap