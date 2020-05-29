from rest_framework import serializers

from quests.models import Quest, Task, Answer, Tip


class TipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = '__all__'


class TipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = '__all__'
        read_only_fields = ['task']


class TipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['tip']


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['task']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True, required=False)
    tips = TipDetailSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['quest', 'answers', 'tips']


class TaskListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    tips = TipListSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['answers', 'content', 'tips']

    def get_answers(self, obj):
        return [answer.answer for answer in obj.answers.all()]


class QuestDetailSerializer(serializers.ModelSerializer):
    tasks = TaskListSerializer(many=True, required=False)

    class Meta:
        model = Quest
        fields = '__all__'
        read_only_fields = ['tasks', 'answers']


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'place', 'start_time', 'duration']