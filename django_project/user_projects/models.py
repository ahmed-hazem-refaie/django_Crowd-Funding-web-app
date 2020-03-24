from django.db import models
from  login.models import User

# ==> will be imported from hazem task--done


# category model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)


#projects model
class Projects (models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=40)
    project_details = models.TextField(default=' ')
    total_target = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_show=models.BooleanField(default=0)



#donation model
class Donation (models.Model):
    donation_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    donation_amount = models.IntegerField()


class Rate (models.Model):
    rate_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    rate = models.IntegerField()


#tags model
class Tags (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=40)


#images class
class Images (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media/projects/img")


#comment model
class Comment (models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects , on_delete=models.CASCADE)
    comment_content = models.TextField(default=' ')


#SUBcomment model
class SubComment (models.Model):
    comment_id = models.ForeignKey(Comment , on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    comment_content = models.TextField(default=' ')


class CommentReports(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)


class ProjectReports (models.Model):
    project_id = models.ForeignKey(Projects , on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
