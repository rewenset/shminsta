from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'  # defines the full Python path to the application
    verbose_name = 'Image bookmarks'  # sets the human-readable name for this application

    def ready(self):
        import images.signals
