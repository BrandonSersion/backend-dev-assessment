from rest_framework import serializers


class RestrictStatusUpdate(object):
    
    def __init__(self, status):
        self.status = status

    def __call__(self, status):
        print(self.status)
        print(self.instance.status)
        if self.status == 'accepted' and self.instance.status == 'rejected':

            message = """Can't update accepted candidate into rejected.
                         Must update candidate to pending in between."""
            raise serializers.ValidationError(message)

        if self.status == 'rejected' and self.instance.status == 'accepted':
            message = """Can't update rejected candidate into accepted.
                         Must update candidate to pending in between."""
            raise serializers.ValidationError(message)






    # def set_context(self, serializer):
    #     # Determine the existing instance, if this is an update operation.
    #     self.instance = getattr(serializer, 'instance', None)


    # def validate_status(self, status):
    #     print(value.initial_data)
    #     print(value.status)

    # def get_initial_field_value(self):
#     print(self.status)
#     print('WEOO')