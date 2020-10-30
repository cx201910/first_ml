""" 
    @action(detail=True, methods=['post'])
    def predict(self, request, pk=None, format=None):
        predictstore = self.get_object() 
        serializer = PredictStoreSerializer(data=request.data)
        alg_status = MLAlgorithmStatus(status='production',
                        created_by=predictstore.created_by,
                        parent_mlalgorithm=predictstore.ml_algorithm, active=True)
        alg_status.save()
        deactivate_other_statuses(alg_status)
        algorithm_status = 'production'
        
        data = json.loads(request.data['input_data'])
        algs = MLAlgorithm.objects.filter(status__status=algorithm_status, status__active=True)

        algorithm_object = registry.endpoints[algs[0].id]
        prediction = algorithm_object.compute_prediction(data)
        label = prediction['label'] if 'label' in prediction else 'error'

        if serializer.is_valid(): 
            serializer.validated_data['prediction'] = prediction 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
""" 
