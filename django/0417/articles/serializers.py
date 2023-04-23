from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', ) # 직렬화할 때만 사용
        # 해당 시리얼라이저는 직렬화, 역직렬화 모두 가능

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep

class ArticleListSerializer(serializers.ModelSerializer):
    ''' 역참조 데이터 조회
    특정 게시글에 작성된 댓글 목록 출력, comment_set를 필드로 사용

    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    '''
    
    ''' Nested relationships
    해당 방법 사용 시 commentserializer와 articleseriazlizer 순서 변경 필요
    '''
    comment_set = CommentSerializer(many=True, read_only=True) 

    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content') - 필드 추가로 인해 삭제
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep