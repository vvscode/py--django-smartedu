from django.core.management.base import BaseCommand
from faker import Faker
import random

from training_sheet.models import Tag, Teacher, Course, CustomUser

fake = Faker()

tags = ["django", "flask", "python", "js", "qa"]
job_titles = ["Developer", "Engineer", "Senior Developer", "Team Lead", "QA"]
companies = ["Epam", "Luxsoft", "Upsilon", "Bolt"]


def get_job_title():
    return f"{random.choice(job_titles)} at {random.choice(companies)}"


class Command(BaseCommand):
    help = "Initial seed for DB"

    tags = []
    teachers = []
    courses = []

    def create_tags(self):
        for tag in tags:
            self.tags.append(Tag.objects.create(title=tag, slug=tag))
        self.stdout.write(self.style.SUCCESS("Tags created"))

    def create_teachers(self):
        for i in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            user = CustomUser(
                email=f"{first_name}_{last_name}_{i + 1}@gmail.com",
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            self.teachers.append(
                Teacher.objects.create(
                    user=user,
                    job_title=get_job_title(),
                    about_description=fake.paragraph(),
                )
            )
        self.stdout.write(self.style.SUCCESS("Teachers created"))

    def create_courses(self):
        for i in range(10):
            course = Course.objects.create(
                title=fake.sentence(), description="\n".join(fake.paragraphs()),
            )
            course.tags.set(random.sample(self.tags, random.randint(1, len(self.tags))))
            course.course_teachers.set(
                random.sample(self.teachers, random.randint(1, len(self.teachers)))
            )
            self.courses.append(course)
        self.stdout.write(self.style.SUCCESS("Courses created"))

    def handle(self, *args, **options):
        self.create_tags()
        self.create_teachers()
        self.create_courses()

        self.stdout.write(self.style.SUCCESS("Done. Seeding completed"))
