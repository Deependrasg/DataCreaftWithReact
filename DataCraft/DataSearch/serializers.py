from rest_framework import serializers
from . import models


class DataCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
			'publisher',
			'department',
			'subdepartment',
			'inventory_ID',
			'title',
			'description',
			'data_classification',
			'category',
			'data_change_frequency',
			'automated_fashion',
			'dataset_come_from',
			'automation_option',
			'api_endpoint',
			'upload',
			'data_classification_comments',
        )
        model = models.PublishserData

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'name',
			)
		model = models.Department 

class SubDepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		fields =(
			'id',
			'name',
			'code',
			'department',
			)
		model = models.SubDepartment
