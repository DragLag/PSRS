from rest_framework import serializers
from cronman.models import Cron


class CronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cron
        fields = ('egg', 'cron_string')