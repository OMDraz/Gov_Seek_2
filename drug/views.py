import json
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import Drug
from .serializers import DrugSerializer
from rest_framework import generics


class UserListCreate(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    
    # def post(self, request):
    #     output = json.loads('drug-ndc-0001-of-0001.json')
    #     Drugs = Drug.objects.all()
    #     serializer = DrugSerializer(Drugs, many=True)
    #     for drug in output:
    #         if drug['id'] not in [drug.id for i in drug]:
    #             Drug.objects.create(
    #                 product_ndc = drug['product_ndc'],
    #                 generic_name = drug['generic_name'],
    #                 labeler_name = drug['labeler_name'],
    #                 brand_name = drug['brand_name'],
    #                 finished = drug['finished'],
    #                 packing = drug['packing'],
    #                 listing_expiration_date = drug['listing_expiration_date'],
    #                 openfda = drug['openfda'],
    #                 marketing_category = drug['marketing_category'],
    #                 dosage_form = drug['dosage_form'],
    #                 spl_id = drug['spl_id'],
    #                 product_type = drug['product_type'],
    #                 route = drug['route'],
    #                 marketing_start_date = drug['marketing_start_date'],
    #                 product_id = drug['product_id'],
    #                 application_number = drug['application_number'],
    #                 brand_name_base = drug['brand_name_base'],
    #                 pharm_class = drug['pharm_class'],
    #             )
    #     return Response(serializer.data)