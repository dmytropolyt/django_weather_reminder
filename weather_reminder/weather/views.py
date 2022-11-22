from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import City, Subscribe
from .serializers import CitySerializer, SubscribeSerializer
from .permissions import IsAdminOrIsAuthenticated, IsOwnerOrIsAuthenticated
from .funcs import add_weather_info


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrIsAuthenticated]
    queryset = City.objects.all().order_by('-name')
    serializer_class = CitySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        cities = serializer.data
        weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4990360ecbb3086ea3865e1c7b4988c4'
        cities = add_weather_info(cities, weather_api_url)

        return Response(cities)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        cities = serializer.data
        weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4990360ecbb3086ea3865e1c7b4988c4'
        cities = add_weather_info(cities, weather_api_url)

        return Response(cities)


class SubscribeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrIsAuthenticated]
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserSubscribesListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all cities which user is subscribed
        '''
        subscribes = Subscribe.objects.filter(user=request.user).all()
        serializer = SubscribeSerializer(subscribes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# class CityListApiView(APIView):
#    permission_classes = [permissions.IsAuthenticated]

#    def get(self, request, *args, **kwargs):
#        '''
#        List all cities for given requested user
#        '''
#        cities = City.objects.all()
#        serializer = CitySerializer(cities, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)

#    def post(self, request, *args, **kwargs):
#        '''
#        Create the city with given city data
#        '''
#        data = {
#            'name': request.data.get('name')
#        }
#        serializer = CitySerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)

#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CityDetailApiView(APIView):
#    permission_classes = [permissions.IsAuthenticated]

#    def get_object(self, city_id):
#        '''
#        Helper method to get the object with given city_id
#        '''
#        try:
#            return City.objects.get(id=city_id)
#        except City.DoesNotExist:
#            return None

#   def get(self, request, city_id, *args, **kwargs):
#        '''
#        Retrieves the ity with given city_id
#        '''
#        city_instance = self.get_object(city_id)
#        if not city_instance:
#           return Response(
#                {"res": "Object with city id does not exists"},
#                status=status.HTTP_400_BAD_REQUEST
#            )

#        serializer = CitySerializer(city_instance)
#        return Response(serializer.data, status=status.HTTP_200_OK)

#    def put(self, request, city_id, *args, **kwargs):
#        '''
#        Updates the city with given city_id if exists
#        '''
#        city_instance = self.get_object(city_id)
#        if not city_instance:
#            return Response(
#                {"res": "Object with city id does not exists"},
#                status=status.HTTP_400_BAD_REQUEST
#            )

#        data = {
#            "name": request.data.get('name')
#        }
#        serializer = CitySerializer(instance=city_instance, data=data, partial=True)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, city_id, *args, **kwargs):
#        '''
#        Deletes the city with given city_id if exists
#        '''
#        city_instance = self.get_object(city_id)
#        if not city_instance:
#            return Response(
#                {"res": "Object with city id does not exists"},
#                status=status.HTTP_400_BAD_REQUEST
#            )
#        city_instance.delete()
#        return Response(
#            {"res": "Object deleted"},
#            status=status.HTTP_200_OK
#        )
