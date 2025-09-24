from django.core.exceptions import ValidationError

def validate_image_format(image):
    valid_extensions = ('.png', '.ico')
    if not image.name.lower().endswith(valid_extensions):
        raise ValidationError('Imagem precisa ser PNG ou ICO')
