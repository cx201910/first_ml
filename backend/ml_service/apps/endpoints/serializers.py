from rest_framework import serializers
from .models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest
from apps.endpoints.models import ABTest
from apps.endpoints.models import PredictStore

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint 
        fields = ['id', 'name', 'owner', 'created_at']
        read_only_fields = fields  

class MLAlgorithmSerializer(serializers.ModelSerializer):

    current_status = serializers.SerializerMethodField()

    class Meta:
        model = MLAlgorithm
        fields = ['id', 'name', 'description', 'code', 'version', 'owner',
                'created_at', 'parent_endpoint', 'current_status']
        read_only_fields = fields

    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status

class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        fields = ['id', 'active', 'status', 'created_by', 'created_at',
        'parent_mlalgorithm']
        read_only_fields = ['id', 'active'] 

class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        fields = [
            'id',
            'input_data',
            'full_response',
            'response',
            'feedback',
            'created_at',
            'parent_mlalgorithm'
        ]
        read_only_fields = [
            'id',
            'input_data',
            'full_response',
            'response',
            'created_at',
            'parent_mlalgorithm'
        ]

class ABTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABTest   
        fields = [
            'id',
            'title',
            'created_by',
            'created_at',
            'ended_at',
            'summary',
            'parent_mlalgorithm_1',
            'parent_mlalgorithm_2',
        ] 
        read_only_fields = [
            'id',
            'ended_at',
            'created_at',
            'summary',
        ]

class PredictStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictStore
        fields = [
                'id',
                'input_data',
                'created_by',
                'created_at',
                'ml_algorithm',
                'prediction',
                'target', 
        ]
        read_only_fields = [
                'created_at',
                'prediction',
        ] 
