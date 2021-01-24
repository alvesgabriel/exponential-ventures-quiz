from quiz.answers.models import Answer, QuizAnswer
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "question",
            "selecte_answere",
        )


class QuizAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = QuizAnswer
        fields = "__all__"

    def create(self, validated_data):
        print("SERIALIZER CREATE")
        answers = validated_data.pop("answers")

        user = self.context.get("user")
        quiz_id = self.context.get("quiz_id")

        quiz_answer = QuizAnswer(**validated_data, user=user, quiz_id=quiz_id)
        quiz_answer.save()

        for answer in answers:
            print(answer)
