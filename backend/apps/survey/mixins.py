from rest_framework import viewsets


class MultiSerializerMixin(viewsets.ReadOnlyModelViewSet):
    serializer_classes = {}
    default_serializer_class = None

    def get_serializer_class(self):
        if not self.serializer_classes and not self.default_serializer_class:
            return super().get_serializer_class()
        return self.serializer_classes.get(
            self.action, self.default_serializer_class
        )
