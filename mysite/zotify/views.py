from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def main(request):
    return render(request, 'zotify/main.html')


def albums(request):
    album_list = Album.objects.all()
    context = {'album_list': album_list}
    return render(request, 'zotify/albums.html', context)


def album_details(request, album_id):
    context = Song.objects.filter(album=album_id)
    return render(request, 'zotify/album_details.html', {'songs': context})


def artists(request):
    artist_list = Artist.objects.all()
    return render(request, 'zotify/artists.html', {'artist_list': artist_list})


def genres(request):
    genres_list = Genre.objects.all()
    return render(request, 'zotify/genres.html', {'genres_list': genres_list})


def playlists(request, user_id=None):
    if user_id is None:
        context = Playlist.objects.filter(private=False)
    else:
        context = Playlist.objects.filter(user=user_id)

    return render(request, 'zotify/playlists.html', {'playlists': context})


def users(request):
    return render(request, 'zotify/main.html')


def song_form(request):
    form = SongForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(songs)
    return render(request, 'zotify/song_form.html', {'form': form})


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        album.delete()
        return redirect(albums)
    return render(request, 'zotify/delete_album.html', {'album': album})


def delete_artist(request, artist_id):
    album = get_object_or_404(Artist, pk=artist_id)
    if request.method == "POST":
        album.delete()
        return redirect(artists)
    return render(request, 'zotify/delete_artist.html', {'album': album})


def edit_genre(request, item_id):
    album = get_object_or_404(Genre, pk=item_id)
    form = GenreForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect(genres)
    return render(request, 'zotify/simple_edit.html', {'form': form})


def album_form(request):
    form = ALbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(albums)
    return render(request, 'zotify/album_form.html', {'form': form})


def genre_form(request):
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        redirect(genres)
    return render(request, 'zotify/genre_form.html', {'form': form})


def profile_page(request, user_id):
    profile = Profile.objects.get(user=user_id)
    return render(request, 'zotify/profile_page.html', {'profile': profile})


def artist_details(request, artist_id):
    artist = MemberArtist.objects.filter(artist=artist_id)
    return render(request, 'zotify/artist_details.html', {'artist': artist})


def playlist_details(request, playlist_id):
    songs = PlaylistSong.objects.filter(playlist=playlist_id)
    return render(request, 'zotify/playlist_details.html', {'songs': songs})


def songs(request):
    songs2 = Song.objects.all()
    return render(request, 'zotify/songs.html', {'songs': songs2})


def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    form = ALbumForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect(albums)
    return render(request, 'zotify/edit_album.html', {'form': form})


def edit_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    form = SongForm(request.POST or None, request.FILES or None, instance=song)
    if form.is_valid():
        form.save()
        return redirect(songs)
    return render(request, 'zotify/edit_song.html', {'form': form})


def edit_member(request, member_id):
    item = get_object_or_404(Member, pk=member_id)
    form = MemberForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect(members)
    return render(request, 'zotify/edit_member.html', {'form': form})


def delete_member(request, member_id):
    album = get_object_or_404(Member, pk=member_id)
    if request.method == "POST":
        album.delete()
        return redirect(members)
    return render(request, 'zotify/delete_member.html', {'album': album})


def delete_playlist(request, playlist_id):
    album = get_object_or_404(Playlist, pk=playlist_id)
    if request.method == "POST":
        album.delete()
        return redirect(playlists)
    return render(request, 'zotify/delete_playlist.html', {'album': album})


def members(request):
    member = Member.objects.all()
    return render(request, 'zotify/members.html', {'members': member})


def roles(request):
    role = Role.objects.all()
    return render(request, 'zotify/roles.html', {'roles': role})


def add_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist2 = form.save(commit=False)
            playlist2.user = request.user
            playlist2.save()
            return redirect(playlists)
    else:
        form = PlaylistForm()
    return render(request, 'zotify/add_playlist.html', {'form': form})


def add_member(request):
    form = MemberForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(members)
    return render(request, 'zotify/add_member.html', {'form': form})


def add_role(request):
    form = RoleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(roles)
    return render(request, 'zotify/add_role.html', {'form': form})


def add_band(request):
    form = BandForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(artists)
    return render(request, 'zotify/add_band.html', {'form': form})


def profile_list(request):
    profile = Profile.objects.all()
    return render(request, 'zotify/profile_list.html', {'profiles': profile})


def add_song_to_playlist(request, song_id):
    if request.method == 'POST':
        form = PlaylistSongForm(request.user, request.POST)
        if form.is_valid():
            playlist2 = form.save(commit=False)
            playlist2.song = get_object_or_404(Song, pk=song_id)
            playlist2.save()
            return redirect(playlists)
    else:
        form = PlaylistSongForm(request.user)
    return render(request, 'zotify/add_song_to_playlist.html', {'form': form})


def edit_artist(request, artist_id):
    item = get_object_or_404(Artist, pk=artist_id)
    form = ArtistForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect(artists)
    return render(request, 'zotify/edit_artist.html', {'form': form})


def delete_song(request, song_id):
    album = get_object_or_404(Song, pk=song_id)
    if request.method == "POST":
        album.delete()
        return redirect(songs)
    return render(request, 'zotify/delete_song.html', {'album': album})


def add_member_to_band(request, member_id):
    if request.method == 'POST':
        form = BandMemberForm(request.POST)
        if form.is_valid():
            playlist2 = form.save(commit=False)
            playlist2.member = get_object_or_404(Member, pk=member_id)
            playlist2.save()
            return redirect(artists)
    else:
        form = BandMemberForm()
    return render(request, 'zotify/add_member_to_band.html', {'form': form})


def delete_profile(request, user_id):
    album = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        album.delete()
        return redirect(profile_list)
    return render(request, 'zotify/delete_profile.html', {'album': album})


def edit_playlist(request, playlist_id):
    album = get_object_or_404(Playlist, pk=playlist_id)
    form = PlaylistForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect(playlists)
    return render(request, 'zotify/edit_playlist.html', {'form': form})


def edit_profile(request, user_id):
    album = get_object_or_404(Profile, pk=user_id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect(profile_list)
    return render(request, 'zotify/edit_profile.html', {'form': form})


def delete_genre(request, genre_id):
    album = get_object_or_404(Genre, pk=genre_id)
    if request.method == "POST":
        album.delete()
        return redirect(genres)
    return render(request, 'zotify/delete_genre.html', {'album': album})

def delete_song_from_playlist(request, song_playlist_id):
    album = get_object_or_404(PlaylistSong, pk=song_playlist_id)
    if request.method == "POST":
        album.delete()
        return redirect(playlists)
    return render(request, 'zotify/delete_song_from_playlist.html', {'album': album})


def delete_member_from_band(request, band_member_id):
    album = get_object_or_404(MemberArtist, pk=band_member_id)
    if request.method == "POST":
        album.delete()
        return redirect(artists)
    return render(request, 'zotify/delete_member_from_band.html', {'album': album})

def widok(request):
    return HttpResponse("to jest widok")