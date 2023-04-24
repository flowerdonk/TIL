from rest_framework import serializers
from ..models import Artist, Album, Track

# list
class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pk', 'name', )

# create, detail, update
class ArtistSerializer(serializers.ModelSerializer):
    class AlbumSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = ('pk', 'name', )

    class TrackSerializer(serializers.ModelSerializer):
        class Meta:
            model = Track
            fields = ('pk', 'title', )

    # validation
    name = serializers.CharField(min_length=1, max_length=20)

    # album serializing
    albums = AlbumSerializer(many=True, read_only=True)

    # track serializing
    tracks = TrackSerializer(many=True, read_only=True)

    album_count = serializers.IntegerField(
        source='albums.count', # related_name.method
        read_only=True,
    )

    class Meta:
        model = Artist
        fields = ('pk', 'name', 'debut', 'albums', 'album_count', 'tracks', )