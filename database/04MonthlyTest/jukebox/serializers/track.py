from rest_framework import serializers
from ..models import Track, Album, Artist

class TopTrackListSerializer(serializers.ModelSerializer):
    class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = ('pk', 'name', )
    
    artists = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ('pk', 'title', 'artists', 'album', 'click', )


class TrackSerializer(serializers.ModelSerializer):
    class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = '__all__'

    class AlbumSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = '__all__'
    
    artists = ArtistSerializer(many=True, read_only=True)
    album = AlbumSerializer(read_only=True)
    lyric = serializers.CharField(required=False)
    artist_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        artist_pks = validated_data.pop('artist_pks')
        track = Track.objects.create(validated_data)
        for artist_pk in artist_pks:
            track.artists.add(artist_pk)
        return track

    def update(self, track, validated_data):
        artist_pks = validated_data.pop('artist_pks')
        for attr, value in validated_data.items():
            setattr(track, attr, value)
        track.save()
        track.artists.clear()
        for artist_pk in artist_pks:
            track.artists.add(artist_pk)
        return track

    class Meta:
        model = Track
        fields = ('pk', 'title', 'artists', 'album', 'lyric', 'click', )