from rest_framework import serializers
from .models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest

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
        read_only_fiels = [
            'id',
            'input_data',
            'full_response',
            'response',
            'created_at',
            'parent_mlalgorithm'
        ]
