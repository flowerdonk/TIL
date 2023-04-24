from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Album, Track

from .serializers.album import AlbumSerializer, AlbumListSerializer
from .serializers.artist import ArtistSerializer, ArtistListSerializer
from .serializers.track import TopTrackListSerializer, TrackSerializer

@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    # list => pk, name
    def artist_list(request):
        artists = Artist.objects.all()
        serializers = ArtistListSerializer(artists, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def create_artist(request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return artist_list(request)
    else:
        return create_artist(request)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def artist_detail_or_update_or_delete(request, artist_pk):
    # detail => pk, name, albums, tracks
    artist = get_object_or_404(Artist, pk=artist_pk)

    def artist_detail(request):
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def artist_update(request):
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_artist(request):
        artist.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return artist_detail(request)
    elif request.method == 'PUT' or request.method == 'PATCH':
        return artist_update(request)
    elif request.method == 'DELETE':
        return delete_artist


@api_view(['GET', 'POST'])
def album_list_or_create(request):
    # list => pk, name

    def album_list(request):
        albums = Album.objects.all()
        serializer = AlbumListSerializer(albums, many=True)
        return Response(serializer.data)

    def create_album(request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'GET':
        return album_list(request)
    else:
        return create_album(request)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def album_detail_or_update_or_detail(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)

    def album_detail(request):
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def update_album(request):
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_album(request):
        album.delete()
        return Response(data="Data deleted permanantly", status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return album_detail(request)
    elif request.method == 'PUT' or request.method == 'PATCH':
        return update_album(request)
    elif request.method =="DELETE":
        return delete_album(request)

@api_view(['GET'])
def top_track_list(request):
    tracks = Track.objects.order_by('-click')
    serializer = TopTrackListSerializer(tracks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_track(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(album=album)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def track_detail_or_update_or_delete(request, album_pk, track_pk):
    album = get_object_or_404(Album, pk=album_pk)
    track = get_object_or_404(Track, pk=track_pk)

    def track_detail(request):
        track.click += 1
        track.save()
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    def update_track(request):
        serializer = TrackSerializer(instance=track, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(album=album)
            return Response(serializer.data)

    def delete_track(request):
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return track_detail(request)
    elif request.method == 'PUT' or request.method == 'PATCH':
        return update_track(request)
    else:
        return delete_track(request)