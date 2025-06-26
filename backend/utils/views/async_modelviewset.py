from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed


class AsyncModelViewSet(viewsets.ModelViewSet):
    """
    Async ModelViewSet with selectable methods.
    Example:
        enabled_methods = {"list", "retrieve", "create"}
    """
    enabled_methods = {"list", "retrieve", "create", "update", "destroy"}

    def check_method(self, method_name):
        if method_name not in self.enabled_methods:
            raise MethodNotAllowed(self.request.method)

    async def list(self, request, *args, **kwargs):
        self.check_method("list")
        queryset = await self.get_queryset_async()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    async def retrieve(self, request, *args, **kwargs):
        self.check_method("retrieve")
        instance = await self.get_object_async()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    async def create(self, request, *args, **kwargs):
        self.check_method("create")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        await self.perform_create_async(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    async def update(self, request, *args, **kwargs):
        self.check_method("update")
        partial = kwargs.pop('partial', False)
        instance = await self.get_object_async()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        await self.perform_update_async(serializer)
        return Response(serializer.data)

    async def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return await self.update(request, *args, **kwargs)

    async def destroy(self, request, *args, **kwargs):
        self.check_method("destroy")
        instance = await self.get_object_async()
        await self.perform_destroy_async(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    async def get_queryset_async(self):
        from asgiref.sync import sync_to_async
        return await sync_to_async(list)(self.filter_queryset(self.get_queryset()))

    async def get_object_async(self):
        from asgiref.sync import sync_to_async
        return await sync_to_async(self.get_object)()

    async def perform_create_async(self, serializer):
        from asgiref.sync import sync_to_async
        await sync_to_async(serializer.save)()

    async def perform_update_async(self, serializer):
        from asgiref.sync import sync_to_async
        await sync_to_async(serializer.save)()

    async def perform_destroy_async(self, instance):
        from asgiref.sync import sync_to_async
        await sync_to_async(instance.delete)()
