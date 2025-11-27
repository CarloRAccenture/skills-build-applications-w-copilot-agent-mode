from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return data

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = ObjectIdField(source='team._id', read_only=True)
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(source='user._id', read_only=True)
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_id', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(source='user._id', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'user_id', 'score']
