from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Artist(models.Model):
    name = models.CharField(max_length=50)
    cover = models.FileField(null=True, blank=True)
    formed_in = models.CharField(max_length=50, null=True, blank=True)
    wiki = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=50)
    cover = models.FileField(null=True, blank=True)
    relase_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def add_song(self):
        self.no_songs += 1


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    bio = models.CharField(max_length=500, null=True)
    image = models.FileField(blank=True, null=True, default='image0.gif')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    private = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=30, blank=True, null=True, default='Default description')

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):
    position = models.PositiveBigIntegerField
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    pseudonym = models.CharField(max_length=50)
    age = models.SmallIntegerField(blank=True, null=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE, default='brak')

    def __str__(self):
        return self.name


class MemberArtist(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Siemka(models.Model):
    ok = models.CharField(max_length=10)
