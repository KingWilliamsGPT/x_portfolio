from django.db import models
from x_portfolio import settings


def _k(a):
    return (a, a)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # note bio should be html safe
    bio = models.TextField(blank=True, help_text='Give your viewers key details about what you do. Can include html.')

    # links
    facebook = models.URLField(blank=True, max_length=300)
    twitter = models.URLField(blank=True, max_length=300)
    linked_in = models.URLField(blank=True, max_length=300)
    github = models.URLField(blank=True, max_length=300)
    whatsapp = models.URLField(blank=True, max_length=300)
    instagram = models.URLField(blank=True, max_length=300)

    # contacts
    phone_number = models.CharField(max_length=20, blank=True)
    display_email = models.EmailField(blank=True)
    location = models.CharField(max_length=200, blank=True)

    # cv
    cv = models.FileField(upload_to='cv', help_text=f'file size must not exceed {settings.FILE_UPLOAD_MAX_MEMORY_SIZE}', blank=True, null=True)

    skills = models.ManyToManyField('Skill', blank=True)
    titles = models.ManyToManyField('Title', blank=True)

    # cover photo
    cover = models.ImageField(upload_to='cover', blank=True, null=True, help_text="Override the default cover photo")
    profile_photo = models.ImageField(upload_to='cover', blank=True, null=True, help_text="A handsome job enticing photo of yourself")

    # brags
    designs_made = models.PositiveIntegerField(blank=True, null=True)
    jobs_done = models.PositiveIntegerField(blank=True, null=True)
    happy_client = models.PositiveIntegerField(blank=True, null=True)
    token_launched = models.PositiveIntegerField(blank=True, null=True)
    students_taught = models.PositiveIntegerField(blank=True, null=True)
    startups_employed_in = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} Profile'

    def brags(self):
        return (
            ('designs made', self.designs_made, 'fa fa-paint-brush'),
            ('jobs done', self.jobs_done, 'fa fa-thumbs-up'),
            ('happy client', self.happy_client, 'fa fa-star'),
            ('token launched', self.token_launched, 'fa fa-rocket'),
            ('students taught', self.students_taught, 'fa fa-graduation-cap'),
            ('startups employed in', self.startups_employed_in, 'fa fa-users'),
        )
    
    def social_links(self):
        return (
            ('facebook', self.facebook),
            ('github', self.github),
            ('twitter', self.linked_in),
            ('linkedin', self.linked_in),
            ('whatsapp', self.whatsapp),
            ('instagram', self.instagram),
        )
    
    def professional_skills(self):
        return self.skills.all().filter(type='Professional')
    
    def personal_skills(self):
        return self.skills.all().filter(type='Personal')
    
    def get_project_categories(self):
        return {project.category for project in self.projects.all()}


class Skill(models.Model):
    skill_types = (
        ('Professional', 'Professional'),
        ('Personal', 'Personal'),
    )
    name = models.CharField(max_length=255, help_text='eg. UI/UX')
    type = models.CharField(max_length=12, choices=skill_types)
    
    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=255, help_text='eg. UI/UX Designer')

    def __str__(self):
        return self.name



class Project(models.Model):
    owners = models.ManyToManyField(UserProfile, related_name='projects', help_text="people involved in this project.")
    title = models.CharField(max_length=255, help_text='name your projects')
    link = models.URLField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, help_text='eg. Web design, Graphics Design, Blockchain, Games')
    image = models.ImageField(upload_to='project_images', help_text="Image to display project")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name