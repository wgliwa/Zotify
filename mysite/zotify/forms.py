from django.forms import ModelForm
from django import forms
from .models import *


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album', 'artist']


class ALbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'cover', 'relase_date', 'genre', 'artist']


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'surname', 'pseudonym', 'age', 'role']


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'private', 'desc']


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class BandForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'cover', 'formed_in', 'wiki']


class PlaylistSongForm(ModelForm):
    def __init__(self, user_id, *args, **kwargs):
        super(PlaylistSongForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].queryset = Playlist.objects.filter(user=user_id)

    class Meta:
        model = PlaylistSong
        fields = ['playlist']


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class BandMemberForm(ModelForm):
    class Meta:
        model = MemberArtist
        fields = ['artist']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']